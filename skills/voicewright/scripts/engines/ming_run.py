"""Run clone jobs on Ming-3.0-tts-tiny, from the clone's folder with its venv. Resumes: an existing output is skipped.

  cd <Ming clone> && PYTHONPATH=. .venv/Scripts/python <this file> jobs.json checkpoints/tiny

jobs.json is a list of {"out", "text", "ref", "ref_text", "seed"}.
Windows and an RTX 50 card need torch 2.7.1+cu128 and triton-windows, not the published cu118 and triton pins.
Text normalization is off: it needs pynini, which has no universal wheel, so write numbers out as words.
"""
import json
import sys
import time
from pathlib import Path

from ming_tiny import MingTinyTTS

MODEL = "inclusionAI/Ming-3.0-tts-tiny"


def main():
    jobs = [j for j in json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")) if not Path(j["out"]).exists()]
    if jobs:
        tts = MingTinyTTS.from_pretrained(sys.argv[2], device="cuda:0", text_normalization=False)
    for j in jobs:
        t = time.time()
        out = Path(j["out"])
        out.parent.mkdir(parents=True, exist_ok=True)
        o = tts.generate(task="seed", text=j["text"], prompt_wav=j["ref"], prompt_text=j["ref_text"], target_language="English", output_path=str(out), seed=j.get("seed", 0))
        secs = o.waveform.shape[-1] / tts.sample_rate
        out.with_suffix(".json").write_text(json.dumps({**j, "model": MODEL, "stopped": bool(o.stopped)}, indent=2) + "\n", encoding="utf-8")
        print("%s %.1fs audio in %.0fs stopped=%s" % (out.name, secs, time.time() - t, bool(o.stopped)), flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
