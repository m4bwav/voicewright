"""Run a job list on Chatterbox, in the Python environment that has chatterbox-tts. Clone only; output is watermarked.
Resumes: an existing output is skipped.

  python chatterbox_run.py jobs.json [--device cpu|cuda]

jobs.json is a list of {"out", "text", "ref", "seed"}. Each output gets a .json beside it for rebuilding.
"""
import json
import sys
import time
from pathlib import Path

import soundfile as sf
import torch
from chatterbox.tts import ChatterboxTTS


def main():
    device = sys.argv[sys.argv.index("--device") + 1] if "--device" in sys.argv else "cuda"
    jobs = [j for j in json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")) if not Path(j["out"]).exists()]
    if jobs:
        model = ChatterboxTTS.from_pretrained(device=device)
    for j in jobs:
        torch.manual_seed(j.get("seed", 0))
        t = time.time()
        w = model.generate(j["text"], audio_prompt_path=j["ref"]).squeeze().cpu().numpy()
        out = Path(j["out"])
        out.parent.mkdir(parents=True, exist_ok=True)
        sf.write(out, w, model.sr)
        out.with_suffix(".json").write_text(json.dumps({**j, "model": "ResembleAI/chatterbox", "device": device}, indent=2) + "\n", encoding="utf-8")
        print("%s %.1fs audio in %.0fs" % (out.name, len(w) / model.sr, time.time() - t), flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
