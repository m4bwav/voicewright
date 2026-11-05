"""Build eval state with invented synthetic audio. Formant-ish buzz differs per voice, so identity checks have something to read."""
import json
import math
import random
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


def main(case):
    d = Path(".")
    if case == "noisy":
        voice(d / "takes/take1.wav", 120, [500, 1500, 2500], 1, noise=0.08)
        voice(d / "takes/take2.wav", 120, [500, 1500, 2500], 1)
    elif case == "cast":
        vs = []
        for i in range(10):
            f = "cast/v%d.wav" % i
            if i == 7:  # planted near duplicate of v2
                voice(d / f, 150 + 2 * 25, [600 + 2 * 170, 1400 + 2 * 240, 2600 - 2 * 130], 2)
            else:
                voice(d / f, 90 + i * 25, [400 + i * 170, 1000 + i * 240, 3200 - i * 130], i)
            vs.append(entry("v%d" % i, "v%d.wav" % i))
        (d / "cast/voices.json").write_text(json.dumps({"schema": 1, "voices": vs}, indent=1), encoding="utf-8")
    elif case == "dwarf":
        voice(d / "voices/keeper.wav", 95, [450, 1100, 2400], 5, sec=6)
        (d / "voices.json").write_text(json.dumps({"schema": 1, "voices": [entry("keeper", "voices/keeper.wav")]}, indent=1), encoding="utf-8")
        for i in range(10):
            if i == 6:
                voice(d / "lines/line06.wav", 210, [800, 2000, 3400], 50)
            else:
                voice(d / ("lines/line%02d.wav" % i), 95, [450, 1100, 2400], 5 + i)
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
