"""Run clone jobs on IndexTTS-2.5, from the clone's folder with its venv. Resumes: an existing output is skipped.

  cd <index-tts clone> && .venv/Scripts/python <this file> jobs.json

jobs.json is a list of {"out", "text", "ref", "seed"}; optional "lang" (default "en").
Licence: clips must not train or tune a commercial model; caps above 100M monthly users or RMB 1B revenue.
"""
import json
import random
import sys
import time
from pathlib import Path

import numpy as np
import soundfile as sf
import torch
from indextts.infer_v2_5 import IndexTTS2

MODEL = "IndexTeam/IndexTTS-2.5"


def main():
    jobs = [j for j in json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")) if not Path(j["out"]).exists()]
    if jobs:
        tts = IndexTTS2(cfg_path="checkpoints/config.yaml", model_dir="checkpoints", use_bf16=True)
    for j in jobs:
        seed = j.get("seed", 0)
        random.seed(seed)
        np.random.seed(seed % 2**32)
        torch.manual_seed(seed)
        t = time.time()
        out = Path(j["out"])
        out.parent.mkdir(parents=True, exist_ok=True)
        tts.infer(spk_audio_prompt=j["ref"], text=j["text"], output_path=str(out), lang=j.get("lang", "EN"))
        out.with_suffix(".json").write_text(json.dumps({**j, "model": MODEL}, indent=2) + "\n", encoding="utf-8")
        print("%s %.1fs audio in %.0fs" % (out.name, sf.info(str(out)).duration, time.time() - t), flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
