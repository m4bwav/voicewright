"""Build eval state. cast, noisy and dwarf copy invented-voice clips from VW_EVAL_AUDIO; rebuild uses synthetic buzz, since it only reads files."""
import json
import math
import os
import random
import shutil
import sys
import wave
from array import array
from pathlib import Path

SR = 16000


def voice(path, f0, formants, seed, sec=4.0, noise=0.0):
    r = random.Random(seed)
    out, phase = array("h"), 0.0
    for i in range(int(sec * SR)):
        t = i / SR
        f = f0 * (1 + 0.08 * math.sin(2 * math.pi * 3 * t + seed))
        phase += f / SR
        env = 0.5 + 0.5 * math.sin(2 * math.pi * 2.3 * t) ** 2
        s = sum(math.sin(2 * math.pi * phase * round(fm / f0)) / (1 + k) for k, fm in enumerate(formants))
        out.append(int(max(-1, min(1, 0.25 * env * s + r.gauss(0, noise))) * 32767))
    path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(out.tobytes())


def entry(i, f):
    return {"id": i, "character": i, "sheet": {"pitch": "see measure"}, "refs": [{"file": f, "text": "A fixed test line.", "emotion": "neutral", "source": "designed"}],
            "engine": {"name": "qwen3-tts", "model": "Qwen/Qwen3-TTS-12Hz-1.7B-Base", "model_version": "abc123", "seed": 4100},
            "rights": {"kind": "designed", "licence": "Apache-2.0 engine"}}


def src():
    """Real invented-voice clips: synthetic buzz does not separate on CAM++, and has no gaps for the noise floor."""
    s = os.environ.get("VW_EVAL_AUDIO")
    if not s or not Path(s).is_dir():
        sys.exit("set VW_EVAL_AUDIO to the folder of invented-voice clips (see TESTS.md); they are not in the repo")
    return Path(s)


def noisy_copy(a, b, level=0.03):
    with wave.open(str(a), "rb") as w:
        params, x = w.getparams(), array("h", w.readframes(w.getnframes()))
    r = random.Random(1)
    y = array("h", (int(max(-1, min(1, v / 32768 + r.gauss(0, level))) * 32767) for v in x))
    b.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(b), "wb") as w:
        w.setparams(params)
        w.writeframes(y.tobytes())


def main(case):
    d = Path(".")
    if case == "noisy":
        s = src()
        noisy_copy(s / "captain.wav", d / "takes/take1.wav")
        (d / "takes").mkdir(exist_ok=True)
        shutil.copy(s / "captain.wav", d / "takes/take2.wav")
    elif case == "cast":
        s = src()
        (d / "cast").mkdir(exist_ok=True)
        names = ["captain", "dwarf", "kid", "maid", "merchant", "soldier", "villain", "captain_dup", "wizard", "queen"]  # v7 is a clone of v0
        vs = []
        for i, n in enumerate(names):
            shutil.copy(s / (n + ".wav"), d / ("cast/v%d.wav" % i))
            vs.append(entry("v%d" % i, "v%d.wav" % i))
        (d / "cast/voices.json").write_text(json.dumps({"schema": 1, "voices": vs}, indent=1), encoding="utf-8")
    elif case == "dwarf":
        s = src()
        (d / "voices").mkdir(exist_ok=True)
        (d / "lines").mkdir(exist_ok=True)
        shutil.copy(s / "dwarf.wav", d / "voices/keeper.wav")
        (d / "voices.json").write_text(json.dumps({"schema": 1, "voices": [entry("keeper", "voices/keeper.wav")]}, indent=1), encoding="utf-8")
        good = sorted((s / "lines").glob("*.wav"))
        for i in range(10):
            shutil.copy(s / "other_voice_line.wav" if i == 6 else good[i], d / ("lines/line%02d.wav" % i))
    elif case == "rebuild":
        voice(d / "voices/keeper.wav", 95, [450, 1100, 2400], 5)
        (d / "voices.json").write_text(json.dumps({"schema": 1, "voices": [entry("keeper", "voices/keeper.wav")]}, indent=1), encoding="utf-8")
        voice(d / "old/a.wav", 130, [500, 1500, 2500], 3)
        old = entry("a", "a.wav")
        del old["id"]
        old["rights"] = "designed, no real reference"
        (d / "old/voices.json").write_text(json.dumps({"voices": [old]}, indent=1), encoding="utf-8")
    else:
        sys.exit("unknown case")
    print("built " + case)


if __name__ == "__main__":
    main(sys.argv[1])
