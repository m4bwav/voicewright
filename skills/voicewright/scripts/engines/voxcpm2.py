"""Run a job list on VoxCPM2, in the Python environment that has voxcpm. Resumes: an existing output is skipped.

  python voxcpm2.py jobs.json

jobs.json is a list of {"out", "mode": "design"|"clone", "text"} plus "seed", for design "instruct", for clone "ref"
and, when the bible or reference has one, "ref_text" (the reference clip's exact transcript). With the transcript
VoxCPM2 clones closer: speaker similarity 0.734 -> 0.822 in a 2026-11-17 test, at RTF about 1.2 instead of 1.03.
Each output gets a .json beside it with everything needed to rebuild it.
"""
import json
import sys
import time
from pathlib import Path

MODEL = "openbmb/VoxCPM2"


def build(j):
    """Text and generate() keywords for one job. The transcript goes in only with a clone reference."""
    kw = {"cfg_value": 2.0, "inference_timesteps": 10}
    text = j["text"]
    if j["mode"] == "design":
        text = "(%s)%s" % (j["instruct"], text)
    else:
        ref_text = (j.get("ref_text") or "").strip()
        if ref_text:
            kw["prompt_wav_path"] = j["ref"]
            kw["prompt_text"] = ref_text
        else:
            kw["reference_wav_path"] = j["ref"]
    return text, kw


def main():
    import soundfile as sf
    import torch
    from voxcpm import VoxCPM

    jobs = [j for j in json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")) if not Path(j["out"]).exists()]
    if jobs:
        model = VoxCPM.from_pretrained(MODEL, load_denoiser=False)
        sr = model.tts_model.sample_rate
    for j in jobs:
        torch.manual_seed(j.get("seed", 0))
        t = time.time()
        text, kw = build(j)
        w = model.generate(text=text, **kw)
        out = Path(j["out"])
        out.parent.mkdir(parents=True, exist_ok=True)
        sf.write(out, w, sr)
        out.with_suffix(".json").write_text(json.dumps({**j, "model": MODEL, **kw}, indent=2) + "\n", encoding="utf-8")
        print("%s %.1fs audio in %.0fs" % (out.name, len(w) / sr, time.time() - t), flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
