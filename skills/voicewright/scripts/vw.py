#!/usr/bin/env python3
"""voicewright: voice bible, measurements and checks. Standard library for the bible and level checks; numpy adds
pitch and spectrum; numpy + onnxruntime + a 27 MB speaker model add identity checks. Every number is a heuristic
calibrated as stated in references/thresholds.md; a person's ear is the final test."""
import argparse
import array
import hashlib
import json
import math
import os
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import wave
from pathlib import Path

VERSION = "0.1.0"
SCHEMA = 1
MODEL_URL = "https://github.com/k2-fsa/sherpa-onnx/releases/download/speaker-recongition-models/wespeaker_en_voxceleb_CAM++.onnx"
MODEL_NAME = "wespeaker_en_voxceleb_CAM++.onnx"

# Provisional thresholds on CAM++ cosine. references/thresholds.md says what each was calibrated on.
T = {
    "cast_fail": 0.55,      # two voices in a cast this close read as one speaker
    "cast_warn": 0.45,
    "library_fail": 0.55,   # same scale, across projects and stock voices
    "pitch_warn_st": 4.0,   # line pitch away from the reference; starter value, means listen
    "wps_low": 1.5,         # words per second, slower is a likely runaway; starter value
    "wps_high": 4.5,        # faster is a likely rush; starter value
    "line_floor": 0.55,     # absolute floor for a line against its own reference
    "clip_peak": -0.1,      # dBFS
    "noise_floor": -60.0,
    "jump_db": 6.0,         # median speech level step between neighbouring phrases
    "tail_s": 0.5,
    "sibilance_db": 0.0,    # 5-9 kHz against 1-4 kHz in the loudest frames
    "tone_db": 8.0,
}

# Loudness per destination. Whole-mix targets are marked: they do not apply to a line on its own.
DEST = {
    "acx": {"rms": (-23, -18), "peak": -3, "noise": -60, "rate": 44100, "note": "ACX; human narration unless authorized"},
    "audiobook": {"rms": (-23, -18), "peak": -3, "noise": -60, "rate": 44100, "note": "ACX numbers as the yardstick"},
    "narration": {"lufs": -16, "peak": -1, "rate": 48000, "note": "Apple podcast spec, -16 LKFS +/-1"},
    "film": {"lufs": -27, "peak": -2, "rate": 48000, "note": "dialogue-gated streaming delivery, secondary sources"},
    "game": {"lufs": -24, "peak": -1, "rate": 48000, "whole_mix": True, "note": "-24 console, -18 mobile apply to the mix; lines stay consistent with each other"},
    "web": {"lufs": -16, "peak": -1, "rate": 48000, "note": "web video"},
}


def die(msg, code=2):
    print("ERROR " + msg)
    sys.exit(code)


# ---- audio reading

def to_wav(path, rate=None):
    """Return (path, is_temp). Converts through ffmpeg when the file is not plain PCM16 mono at the wanted rate."""
    try:
        with wave.open(str(path), "rb") as w:
            if w.getsampwidth() == 2 and w.getnchannels() == 1 and (rate is None or w.getframerate() == rate):
                return str(path), False
    except (wave.Error, EOFError):
        pass
    if not shutil.which("ffmpeg"):
        die("%s is not 16-bit mono WAV and ffmpeg is missing" % path)
    fd, tmp = tempfile.mkstemp(suffix=".wav")
    os.close(fd)
    cmd = ["ffmpeg", "-y", "-v", "error", "-i", str(path), "-ac", "1", "-c:a", "pcm_s16le"]
    if rate:
        cmd += ["-ar", str(rate)]
    subprocess.run(cmd + [tmp], check=True)
    return tmp, True


def read_pcm(path, rate=None):
    p, temp = to_wav(path, rate)
    with wave.open(p, "rb") as w:
        sr = w.getframerate()
        a = array.array("h")
        a.frombytes(w.readframes(w.getnframes()))
    if temp:
        os.unlink(p)
    if sys.byteorder == "big":
        a.byteswap()
    return a, sr


def db(x):
    return 20 * math.log10(x) if x > 1e-9 else -180.0


def frame_rms(a, sr, ms=50):
    n = max(1, int(sr * ms / 1000))
    out = []
    for i in range(0, max(1, len(a) - n + 1), n):
        chunk = a[i:i + n]
        out.append(math.sqrt(sum(s * s for s in chunk) / max(1, len(chunk))) / 32768.0)
    return out


def measure_level(a, sr):
    """Standard library only."""
    if not a:
        return {"error": "empty"}
    peak = max(abs(min(a)), abs(max(a))) / 32768.0
    clipped = sum(1 for s in a if abs(s) >= 32700)
    frames = frame_rms(a, sr)
    dbs = [db(f) for f in frames]
    top = max(dbs)
    speech = [i for i, d in enumerate(dbs) if d > top - 30]
    quiet = sorted(dbs)[:max(1, len(dbs) // 10)]
    r = {
        "duration_s": round(len(a) / sr, 2), "rate": sr, "peak_db": round(db(peak), 1), "clipped_samples": clipped,
        "rms_db": round(db(math.sqrt(sum(s * s for s in a) / len(a)) / 32768.0), 1),
        "noise_floor_db": round(sum(quiet) / len(quiet), 1),
    }
    if speech:
        r["speech_rms_db"] = round(db(math.sqrt(sum(frames[i] ** 2 for i in speech) / len(speech))), 1)
        r["tail_s"] = round((len(dbs) - 1 - speech[-1]) * 0.05, 2)
        r["head_s"] = round(speech[0] * 0.05, 2)
        # phrases: runs of speech split by 200 ms or more of silence; compare neighbouring medians
        phrases, cur, gap = [], [], 0
        for i in range(speech[0], speech[-1] + 1):
            if dbs[i] > top - 30:
                cur.append(dbs[i])
                gap = 0
            else:
                gap += 1
                if gap >= 4 and cur:
                    phrases.append(cur)
                    cur = []
        if cur:
            phrases.append(cur)
        meds = [sorted(p)[len(p) // 2] for p in phrases if len(p) >= 4]
        r["max_phrase_jump_db"] = round(max([abs(x - y) for x, y in zip(meds, meds[1:])] or [0.0]), 1)
    return r


def need_numpy():
    try:
        import numpy
        return numpy
    except ImportError:
        return None


def measure_spectrum(a, sr):
    """Needs numpy. Sibilance, high-frequency cutoff, spectral flatness, steady tones, pitch."""
    np = need_numpy()
    if np is None:
        return {"spectrum": "skipped: numpy missing"}
    x = np.asarray(a, dtype=np.float64) / 32768.0
    n = 2048
    if len(x) < n * 2:
        return {"spectrum": "skipped: clip too short"}
    win = np.hanning(n)
    fr = np.lib.stride_tricks.sliding_window_view(x, n)[::n // 2] * win
    p = np.abs(np.fft.rfft(fr, axis=1)) ** 2
    f = np.fft.rfftfreq(n, 1 / sr)
    e = p.sum(axis=1)
    loud = p[e > np.percentile(e, 60)]
    avg = loud.mean(axis=0) + 1e-14

    def band(lo, hi):
        return float(avg[(f >= lo) & (f < hi)].mean()) if hi <= sr / 2 + 1 and ((f >= lo) & (f < hi)).any() else None
    r = {}
    mid, sib = band(1000, 4000), band(5000, min(9000, sr / 2))
    if mid and sib:
        r["sibilance_db"] = round(10 * math.log10(sib / mid), 1)
    ldb = 10 * np.log10(avg)
    above = f[ldb > ldb.max() - 70]
    r["hf_cutoff_hz"] = int(above.max()) if len(above) else 0
    hi = (f >= 4000) & (f < min(8000, sr / 2))
    if hi.any():
        r["flatness_4_8k"] = round(float(np.exp(np.log(avg[hi]).mean()) / avg[hi].mean()), 3)
    if len(x) > sr * 30:  # held vowels read as tones on short clips, so joined tracks only: 1 Hz bins, against a median baseline (L-001)
        nl = min(sr, len(x) // 2)
        lf = np.lib.stride_tricks.sliding_window_view(x, nl)[::nl // 2] * np.hanning(nl)
        lp = 10 * np.log10((np.abs(np.fft.rfft(lf, axis=1)) ** 2).mean(axis=0) + 1e-14)
        ff = np.fft.rfftfreq(nl, 1 / sr)
        k = 61
        step = lp[::4]
        base = np.interp(np.arange(len(lp)), np.arange(len(step)) * 4,
                         np.median(np.lib.stride_tricks.sliding_window_view(np.pad(step, k // 2, mode="edge"), k), axis=1))
        d = (lp - base)[(ff > 500) & (ff < min(8000, sr / 2))]
        fb = ff[(ff > 500) & (ff < min(8000, sr / 2))]
        if len(d):
            i = int(d.argmax())
            r["tone_peak_db"], r["tone_peak_hz"] = round(float(d[i]), 1), int(fb[i])
    r.update(pitch(x, sr, np))
    return r


def pitch(x, sr, np):
    """Median F0 by a normalized autocorrelation over voiced frames, 60-500 Hz. Measure a dry line, never a mix."""
    step = max(1, sr // 8000)
    y = x[::step]
    fs = sr / step
    n = int(fs * 0.04)
    lo, hi = int(fs / 500), int(fs / 60)
    vals = []
    if len(y) <= n + hi:
        return {}
    gate = np.sqrt((y ** 2).mean()) * 0.5
    for i in range(0, len(y) - n - hi, int(fs * 0.01)):
        a = y[i:i + n]
        if np.sqrt((a ** 2).mean()) < gate:
            continue
        best, lag = 0.0, 0
        c = np.correlate(y[i:i + n + hi], a, "valid")
        e = np.sqrt(np.convolve(y[i:i + n + hi] ** 2, np.ones(n), "valid")) * np.sqrt((a ** 2).sum()) + 1e-12
        nc = c / e
        seg = nc[lo:hi]
        if len(seg):
            lag = int(seg.argmax()) + lo
            best = float(nc[lag])
            # prefer the shortest lag near the best, which avoids octave-low errors
            peaks = [k for k in range(1, len(seg) - 1) if seg[k] > best * 0.93 and seg[k] >= seg[k - 1] and seg[k] >= seg[k + 1]]
            if peaks:
                lag = peaks[0] + lo
        if best > 0.6 and lag:
            y0, y1, y2 = nc[lag - 1], nc[lag], nc[lag + 1] if lag + 1 < len(nc) else nc[lag]
            den = y0 - 2 * y1 + y2
            vals.append(fs / (lag + (0.5 * (y0 - y2) / den if abs(den) > 1e-9 else 0.0)))
    if len(vals) < 5:
        return {"f0_note": "too few voiced frames"}
    v = np.array(vals)
    st = 12 * np.log2(v / np.median(v))
    return {"f0_median_hz": round(float(np.median(v)), 1), "f0_range_st": round(float(np.percentile(st, 95) - np.percentile(st, 5)), 1),
            "voiced_share": round(len(vals) / max(1, int((len(y) - n - hi) / (fs * 0.01))), 2)}


def judge(m):
    """Return (errors, warnings) for one measured clip. Heuristics, not verdicts."""
    e, w = [], []
    if m.get("clipped_samples", 0) > 2 or m.get("peak_db", -99) >= T["clip_peak"]:
        e.append("clipping: peak %s dB, %s samples" % (m.get("peak_db"), m.get("clipped_samples")))
    if m.get("noise_floor_db", -99) > T["noise_floor"]:
        (e if m["noise_floor_db"] > -40 else w).append("noise floor %s dB (want %s or lower)" % (m["noise_floor_db"], T["noise_floor"]))
    if m.get("max_phrase_jump_db", 0) > T["jump_db"]:
        w.append("level jump %s dB between phrases" % m["max_phrase_jump_db"])
    if m.get("tail_s", 0) > T["tail_s"]:
        w.append("tail %s s: trim and listen for junk" % m["tail_s"])
    if m.get("sibilance_db", -99) > T["sibilance_db"]:
        w.append("sibilance %s dB: 5-9 kHz is above 1-4 kHz" % m["sibilance_db"])
    if m.get("tone_peak_db", 0) > T["tone_db"]:
        w.append("steady tone %s dB at %s Hz: check the joined track, notch if real" % (m["tone_peak_db"], m.get("tone_peak_hz")))
    if m.get("f0_range_st") is not None and m["f0_range_st"] < 2.5:
        w.append("flat read: pitch range %s semitones" % m["f0_range_st"])
    return e, w


# ---- speaker embedding (optional extras)

def cache_dir():
    return Path(os.environ.get("VOICEWRIGHT_CACHE") or Path.home() / ".cache" / "voicewright")


def model_path():
    return cache_dir() / MODEL_NAME


def embedder():
    np = need_numpy()
    try:
        import onnxruntime as ort
    except ImportError:
        ort = None
    if np is None or ort is None:
        die("identity checks need numpy and onnxruntime: pip install numpy onnxruntime", 3)
    if not model_path().is_file():
        die("speaker model missing: run `vw.py setup` (downloads 27 MB, WeSpeaker CAM++, CC BY 4.0)", 3)
    s = ort.InferenceSession(str(model_path()), providers=["CPUExecutionProvider"])
    return np, s


def fbank(a, np):
    """80-dim log mel with per-utterance mean removal, Kaldi-like, at 16 kHz."""
    x = np.asarray(a, dtype=np.float64)
    fl, sh, nfft = 400, 160, 512
    if len(x) < fl:
        x = np.pad(x, (0, fl - len(x)))
    fr = np.lib.stride_tricks.sliding_window_view(x, fl)[::sh].copy()
    fr -= fr.mean(axis=1, keepdims=True)
    fr[:, 1:] -= 0.97 * fr[:, :-1]
    fr[:, 0] *= 0.03
    fr *= np.hanning(fl + 1)[:-1] ** 0.85
    sp = np.abs(np.fft.rfft(fr, nfft)) ** 2
    mel = lambda h: 1127 * np.log(1 + h / 700.0)
    pts = np.linspace(mel(20.0), mel(8000.0), 82)
    bins = mel(np.fft.rfftfreq(nfft, 1 / 16000.0))
    fb = np.zeros((80, nfft // 2 + 1))
    for i in range(80):
        l, c, r = pts[i], pts[i + 1], pts[i + 2]
        fb[i] = np.maximum(0, np.minimum((bins - l) / (c - l), (r - bins) / (r - c)))
    feat = np.log(np.maximum(sp @ fb.T, 1e-10))
    return (feat - feat.mean(axis=0)).astype(np.float32)


def embed(paths, ctx=None):
    np, s = ctx or embedder()
    out = []
    for p in paths:
        a, _ = read_pcm(p, 16000)
        f = fbank(a, np)
        names = [i.name for i in s.get_inputs()]
        v = s.run(None, {names[0]: f[None]})[0][0]
        out.append(v / (np.linalg.norm(v) + 1e-9))
    return out


def centroid(paths, ctx):
    np = ctx[0]
    v = np.mean(embed(paths, ctx), axis=0)
    return v / (np.linalg.norm(v) + 1e-9)


# ---- the bible

def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def bible_file(p):
    p = Path(p)
    if p.is_dir():
        for c in (p / "voices.json", p / "bibles" / "voices.json"):
            if c.is_file():
                return c
        return p / "voices.json"
    return p


def load(p):
    f = bible_file(p)
    if not f.is_file():
        die("no bible at %s" % f)
    return f, json.loads(f.read_text(encoding="utf-8"))


def write_lf(f, text):
    """Path.write_text has no newline argument before Python 3.10."""
    with open(f, "w", encoding="utf-8", newline="\n") as h:
        h.write(text)


def save(f, d):
    f.parent.mkdir(parents=True, exist_ok=True)
    write_lf(f, json.dumps(d, indent=2, ensure_ascii=False) + "\n")


def voice_id(v):
    return v.get("id") or v.get("character")


def root_of(f):
    return f.parent.parent if f.parent.name == "bibles" else f.parent


def bible_errors(f, d):
    """Rebuild contract: a new session on any product must be able to remake each voice from this file."""
    errs, warns = [], []
    if d.get("schema") != SCHEMA:
        warns.append("schema is %s, expected %s: run `vw.py migrate`" % (d.get("schema"), SCHEMA))
    root = root_of(f)
    seen = set()
    for v in d.get("voices", []):
        i = voice_id(v) or "?"
        if i in seen:
            errs.append("%s: duplicate id" % i)
        seen.add(i)
        for k in ("sheet", "refs", "engine", "rights"):
            if not v.get(k):
                errs.append("%s: missing %s" % (i, k))
        eng = v.get("engine") or {}
        for k in ("name", "model"):
            if not eng.get(k):
                errs.append("%s: engine.%s missing, cannot rebuild" % (i, k))
        if eng and not (eng.get("seed") is not None or eng.get("voice_id") or (v.get("refs"))):
            errs.append("%s: no seed, voice id or reference to rebuild from" % i)
        if not (eng.get("model_version") or eng.get("version")):
            warns.append("%s: engine.model_version not pinned" % i)
        for r in v.get("refs") or []:
            fp = root / r.get("file", "")
            if not fp.is_file():
                errs.append("%s: reference %s missing" % (i, r.get("file")))
            elif r.get("sha256") and sha(fp) != r["sha256"]:
                errs.append("%s: reference %s changed (sha256 differs)" % (i, r.get("file")))
            elif not r.get("sha256"):
                warns.append("%s: reference %s has no hash" % (i, r.get("file")))
            if not r.get("text"):
                errs.append("%s: reference %s has no transcript" % (i, r.get("file")))
        rt = v.get("rights") or {}
        kind = rt.get("kind") if isinstance(rt, dict) else None
        if isinstance(rt, dict):
            if kind == "real-person" and not rt.get("consent"):
                errs.append("%s: a real person's voice with no consent record" % i)
            if kind not in ("designed", "real-person", "library", "self", None):
                warns.append("%s: unknown rights.kind %s" % (i, kind))
            if not rt.get("licence"):
                warns.append("%s: rights.licence missing (the engine's output terms)" % i)
    return errs, warns


def cmd_init(a):
    f = bible_file(a.path)
    if f.exists():
        die("%s exists" % f)
    save(f, {"schema": SCHEMA, "voices": []})
    print("wrote %s" % f)


def cmd_add(a):
    f, d = load(a.bible)
    v = json.loads(Path(a.voice_json).read_text(encoding="utf-8"))
    if voice_id(v) in [voice_id(x) for x in d["voices"]]:
        die("%s already in the bible; edit it and raise its version" % voice_id(v))
    root = root_of(f)
    for r in v.get("refs", []):
        fp = root / r["file"]
        if fp.is_file():
            r["sha256"] = sha(fp)
    v.setdefault("version", 1)
    d["voices"].append(v)
    save(f, d)
    errs, warns = bible_errors(f, d)
    print("added %s; %d errors, %d warnings" % (voice_id(v), len(errs), len(warns)))
    for x in errs:
        print("ERROR " + x)
    return 1 if errs else 0


def cmd_validate(a):
    f, d = load(a.bible)
    errs, warns = bible_errors(f, d)
    for x in errs:
        print("ERROR " + x)
    for x in warns:
        print("warn  " + x)
    print("%d voices, %d errors, %d warnings" % (len(d.get("voices", [])), len(errs), len(warns)))
    return 1 if errs else 0


def cmd_migrate(a):
    """cinewright's voices.json to this schema. Keeps `character`, so cinewright keeps reading the file."""
    f, d = load(a.bible)
    root = root_of(f)
    n = 0
    for v in d.get("voices", []):
        v.setdefault("id", v.get("character"))
        v.setdefault("version", 1)
        rt = v.get("rights")
        if isinstance(rt, str):
            v["rights"] = {"kind": "designed", "note": rt}
        for r in v.get("refs") or []:
            fp = root / r.get("file", "")
            if fp.is_file() and not r.get("sha256"):
                r["sha256"] = sha(fp)
        n += 1
    d["schema"] = SCHEMA
    if a.dry_run:
        print(json.dumps(d, indent=2, ensure_ascii=False))
    else:
        save(f, d)
    print("migrated %d voices" % n)


def cmd_card(a):
    """Print everything needed to rebuild one voice."""
    f, d = load(a.bible)
    for v in d["voices"]:
        if voice_id(v) == a.voice:
            print(json.dumps(v, indent=2, ensure_ascii=False))
            return 0
    die("no voice %s" % a.voice)


# ---- checks

def cmd_measure(a):
    bad = 0
    for p in a.files:
        pcm, sr = read_pcm(p)
        m = measure_level(pcm, sr)
        m.update(measure_spectrum(pcm, sr))
        e, w = judge(m)
        if a.json:
            print(json.dumps({"file": str(p), **m, "errors": e, "warnings": w}))
        else:
            print("%s  %s" % (p, " ".join("%s=%s" % kv for kv in m.items())))
            for x in e:
                print("  FAIL " + x)
            for x in w:
                print("  warn " + x)
        bad += bool(e)
    return 1 if bad else 0


def voice_clips(f, v):
    root = root_of(f)
    return [str(root / r["file"]) for r in v.get("refs", []) if (root / r["file"]).is_file()]


def pairs_report(names, vecs, fail, warn):
    np = need_numpy()
    rows = []
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            rows.append((float(np.dot(vecs[i], vecs[j])), names[i], names[j]))
    rows.sort(reverse=True)
    bad = 0
    for s, x, y in rows:
        tag = "FAIL" if s >= fail else "warn" if s >= warn else "ok"
        bad += tag == "FAIL"
        if tag != "ok":
            print("%s %.3f %s / %s" % (tag, s, x, y))
    if rows:
        print("closest %.3f (%s / %s), mean %.3f, %d pairs, %d too close" % (rows[0][0], rows[0][1], rows[0][2], sum(r[0] for r in rows) / len(rows), len(rows), bad))
    return bad


def cmd_cast(a):
    """Variety: every pair in a bible, or in a folder of one clip per voice."""
    ctx = embedder()
    if a.clips:
        names = [Path(p).stem for p in a.clips]
        vecs = embed(a.clips, ctx)
    else:
        f, d = load(a.bible)
        names, vecs = [], []
        for v in d["voices"]:
            c = voice_clips(f, v)
            if not c:
                print("warn %s has no reference to compare" % voice_id(v))
                continue
            names.append(voice_id(v))
            vecs.append(centroid(c, ctx))
    return 1 if pairs_report(names, vecs, T["cast_fail"], T["cast_warn"]) else 0


def cmd_library(a):
    """Originality: one new clip against every voice in the libraries and stock folders."""
    ctx = embedder()
    np = ctx[0]
    new = centroid(a.clip, ctx)
    rows = []
    for lib in a.against:
        lp = Path(lib)
        if lp.is_dir() and not (lp / "voices.json").is_file() and not (lp / "bibles" / "voices.json").is_file():
            for w in sorted(lp.rglob("*.wav")):
                rows.append((float(np.dot(new, embed([w], ctx)[0])), str(w)))
        else:
            f, d = load(lib)
            for v in d["voices"]:
                c = voice_clips(f, v)
                if c:
                    rows.append((float(np.dot(new, centroid(c, ctx))), "%s:%s" % (f, voice_id(v))))
    rows.sort(reverse=True)
    for s, n in rows[:a.top]:
        print("%s %.3f %s" % ("FAIL" if s >= T["library_fail"] else "ok  ", s, n))
    bad = [r for r in rows if r[0] >= T["library_fail"]]
    print("%d compared, %d too close (fail at %.2f)" % (len(rows), len(bad), T["library_fail"]))
    return 1 if bad else 0


def line_warnings(st, seconds, words):
    """Faults that identity misses. They ask for a listen and do not change the exit code."""
    out = []
    if st is not None and abs(st) > T["pitch_warn_st"]:
        out.append("PITCH")
    if words and seconds > 0:
        wps = words / seconds
        if wps < T["wps_low"]:
            out.append("SLOW %.1f w/s" % wps)
        elif wps > T["wps_high"]:
            out.append("FAST %.1f w/s" % wps)
    return out


def sidecar_words(path):
    """Word count from the .json the engine runners write beside a clip, if any."""
    f = Path(path).with_suffix(".json")
    try:
        return len(json.loads(f.read_text(encoding="utf-8")).get("text", "").split())
    except (OSError, ValueError, AttributeError):
        return 0


def cmd_line(a):
    """Consistency: lines against the voice's references. Bar: the floor, or the lines' own mean minus 2 SD."""
    ctx = embedder()
    np = ctx[0]
    f, d = load(a.bible)
    v = next((x for x in d["voices"] if voice_id(x) == a.voice), None)
    if not v:
        die("no voice %s" % a.voice)
    c = voice_clips(f, v)
    if not c:
        die("%s has no reference" % a.voice)
    ref = centroid(c, ctx)
    sims = [float(np.dot(ref, e)) for e in embed(a.lines, ctx)]
    bar = T["line_floor"]
    if len(sims) >= 5:
        bar = max(bar, float(np.mean(sims) - 2 * np.std(sims)))
    bad = 0
    refpcm, sr = read_pcm(c[0])
    rs = measure_spectrum(refpcm, sr)
    for p, s in zip(a.lines, sims):
        pcm, sr2 = read_pcm(p)
        m = measure_spectrum(pcm, sr2)
        note = ""
        st = None
        if rs.get("f0_median_hz") and m.get("f0_median_hz"):
            st = 12 * math.log2(m["f0_median_hz"] / rs["f0_median_hz"])
            note = " f0 %+.1f st" % st
        for w in line_warnings(st, len(pcm) / sr2, sidecar_words(p)):
            note += " LISTEN:" + w
        tag = "DRIFT" if s < bar else "ok"
        bad += tag == "DRIFT"
        print("%s %.3f%s %s" % (tag, s, note, p))
    print("%d lines, mean %.3f, bar %.3f, %d drift" % (len(sims), sum(sims) / len(sims), bar, bad))
    return 1 if bad else 0


def cmd_setup(a):
    p = model_path()
    if p.is_file():
        print("speaker model present: %s" % p)
        return 0
    p.parent.mkdir(parents=True, exist_ok=True)
    print("downloading 27 MB to %s" % p)
    urllib.request.urlretrieve(MODEL_URL, str(p) + ".part")
    os.replace(str(p) + ".part", p)
    print("sha256 %s" % sha(p))
    return 0


# ---- finish and review

def cmd_finish(a):
    """Trim and level for a destination. No denoiser: a check must find noise first (references/finish.md)."""
    if a.dest not in DEST:
        die("unknown destination %s; one of %s" % (a.dest, ", ".join(DEST)))
    if not shutil.which("ffmpeg"):
        die("finish needs ffmpeg")
    t = DEST[a.dest]
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    trim = "silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.05,areverse,silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.15,areverse"
    if "lufs" in t:
        level = "loudnorm=I=%d:TP=%d:LRA=11" % (t["lufs"], t["peak"])
        if a.short:  # loudness normalization misjudges very short clips: use a plain gain instead
            pcm, sr = read_pcm(a.input)
            gain = t["lufs"] + 3 - measure_level(pcm, sr).get("speech_rms_db", -20)
            level = "volume=%.1fdB,alimiter=limit=%.3f" % (gain, 10 ** (t["peak"] / 20))
    else:
        pcm, sr = read_pcm(a.input)
        gain = sum(t["rms"]) / 2 - measure_level(pcm, sr)["rms_db"]
        level = "volume=%.1fdB,alimiter=limit=%.3f" % (gain, 10 ** (t["peak"] / 20))
    cmd = ["ffmpeg", "-y", "-v", "error", "-i", a.input, "-af", trim + "," + level, "-ac", "1", "-ar", str(t["rate"]), "-c:a", "pcm_s16le", a.out]
    subprocess.run(cmd, check=True)
    print("%s: %s (%s)" % (a.out, a.dest, t["note"]))
    return 0


def cmd_review(a):
    """Join a batch into one review clip with gaps, and write the list of what plays when."""
    if not shutil.which("ffmpeg"):
        die("review needs ffmpeg")
    t, rows, inputs = 0.0, [], []
    tmp = tempfile.mkdtemp()
    try:
        lst = Path(tmp) / "l.txt"
        gap = Path(tmp) / "gap.wav"
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono", "-t", "0.7", "-c:a", "pcm_s16le", str(gap)], check=True)
        for i, p in enumerate(a.files):
            c = Path(tmp) / ("c%d.wav" % i)
            subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", p, "-ac", "1", "-ar", "48000", "-c:a", "pcm_s16le", str(c)], check=True)
            pcm, sr = read_pcm(c)
            rows.append("%7.2f  %s" % (t, p))
            t += len(pcm) / sr + 0.7
            inputs += ["file '%s'" % c.as_posix(), "file '%s'" % gap.as_posix()]
        lst.write_text("\n".join(inputs), encoding="utf-8")
        Path(a.out).parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c:a", "pcm_s16le", a.out], check=True)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    write_lf(Path(a.out + ".txt"), "\n".join(rows) + "\n")
    print("%s: %d clips, %.1f s; timing in %s.txt" % (a.out, len(a.files), t, a.out))
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(prog="vw.py", description=__doc__)
    ap.add_argument("--version", action="version", version=VERSION)
    sp = ap.add_subparsers(dest="cmd", required=True)
    s = sp.add_parser("setup", help="download the speaker model")
    s.set_defaults(fn=cmd_setup)
    s = sp.add_parser("init", help="new bible")
    s.add_argument("path")
    s.set_defaults(fn=cmd_init)
    s = sp.add_parser("add", help="add a voice from a JSON file, hashing its references")
    s.add_argument("bible")
    s.add_argument("voice_json")
    s.set_defaults(fn=cmd_add)
    s = sp.add_parser("validate", help="can every voice be rebuilt from disk")
    s.add_argument("bible")
    s.set_defaults(fn=cmd_validate)
    s = sp.add_parser("migrate", help="upgrade a cinewright voices.json in place")
    s.add_argument("bible")
    s.add_argument("--dry-run", action="store_true")
    s.set_defaults(fn=cmd_migrate)
    s = sp.add_parser("card", help="print one voice")
    s.add_argument("bible")
    s.add_argument("voice")
    s.set_defaults(fn=cmd_card)
    s = sp.add_parser("measure", help="level, noise, clipping, jumps, tail, sibilance, tones, pitch")
    s.add_argument("files", nargs="+")
    s.add_argument("--json", action="store_true")
    s.set_defaults(fn=cmd_measure)
    s = sp.add_parser("cast", help="every pair in a cast")
    s.add_argument("bible", nargs="?")
    s.add_argument("--clips", nargs="+")
    s.set_defaults(fn=cmd_cast)
    s = sp.add_parser("library", help="a new voice against other bibles and stock folders")
    s.add_argument("clip", nargs="+")
    s.add_argument("--against", nargs="+", required=True)
    s.add_argument("--top", type=int, default=5)
    s.set_defaults(fn=cmd_library)
    s = sp.add_parser("line", help="new lines against a voice's references")
    s.add_argument("bible")
    s.add_argument("voice")
    s.add_argument("lines", nargs="+")
    s.set_defaults(fn=cmd_line)
    s = sp.add_parser("finish", help="trim and level for a destination")
    s.add_argument("input")
    s.add_argument("out")
    s.add_argument("--dest", required=True)
    s.add_argument("--short", action="store_true", help="for clips under about 3 s")
    s.set_defaults(fn=cmd_finish)
    s = sp.add_parser("review", help="join a batch into one review clip")
    s.add_argument("files", nargs="+")
    s.add_argument("--out", required=True)
    s.set_defaults(fn=cmd_review)
    a = ap.parse_args(argv)
    return a.fn(a) or 0


if __name__ == "__main__":
    sys.exit(main())
