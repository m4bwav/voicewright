"""Run a job list on VoxCPM2, in the Python environment that has voxcpm. Resumes: an existing output is skipped.

  python voxcpm2.py jobs.json

jobs.json is a list of {"out", "mode": "design"|"clone", "text"} plus "seed", for design "instruct", for clone "ref".
Each output gets a .json beside it with everything needed to rebuild it.
"""
import json
import sys
import time
from pathlib import Path

import soundfile as sf
import torch
from voxcpm import VoxCPM

MODEL = "openbmb/VoxCPM2"


def main():
    jobs = [j for j in json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")) if not Path(j["out"]).exists()]
    if jobs:
        model = VoxCPM.from_pretrained(MODEL, load_denoiser=False)
        sr = model.tts_model.sample_rate
    for j in jobs:
        torch.manual_seed(j.get("seed", 0))
        t = time.time()
        kw = {"cfg_value": 2.0, "inference_timesteps": 10}
        text = j["text"]
        if j["mode"] == "design":
            text = "(%s)%s" % (j["instruct"], text)
        else:
            kw["reference_wav_path"] = j["ref"]
        w = model.generate(text=text, **kw)
        out = Path(j["out"])
        out.parent.mkdir(parents=True, exist_ok=True)
        sf.write(out, w, sr)
        out.with_suffix(".json").write_text(json.dumps({**j, "model": MODEL, **kw}, indent=2) + "\n", encoding="utf-8")
        print("%s %.1fs audio in %.0fs" % (out.name, len(w) / sr, time.time() - t), flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
