"""Run a clone job list on VoxMel-0.6B (optional engine). Resumes: an existing output is skipped.

  python voxmel_run.py jobs.json

Run it with the Python of an existing VoxMel install (github.com/VoxDance-Lab/VoxMel, its own venv).
Nothing of VoxMel is vendored here. Set VOXMEL_HOME (or "voxmel_home" in a job) to the cloned repo,
and VOXMEL_WEIGHTS (or "voxmel_weights") to the folder with the checkpoint and vocos/; it defaults to
<home>/weights.

jobs.json is a list of {"out", "text", "ref", "ref_text"} plus "seed" and optional "steps" (default 4).
VoxMel clones only, needs the reference's exact transcript, and speaks English and Chinese only.
Licence: code and weights Apache-2.0, but trained on Emilia (CC BY-NC): personal projects only,
nothing that will be sold. Measured 2026-11-17 at 4 steps: similarity 0.894, RTF about 1.0, 3.7 GB VRAM.
"""
import json
import os
import sys
import time
from pathlib import Path

MODEL = "VoxMel-0.6B"
STEPS = 4


def paths(job=None):
    """VoxMel repo and weights folders from the job or the environment."""
    job = job or {}
    home = job.get("voxmel_home") or os.environ.get("VOXMEL_HOME")
    if not home:
        raise SystemExit("set VOXMEL_HOME to an existing VoxMel clone")
    home = Path(home)
    weights = Path(job.get("voxmel_weights") or os.environ.get("VOXMEL_WEIGHTS") or home / "weights")
    return home, weights


def check(j):
    """Problems with one job, as a list of strings."""
    errs = [k for k in ("out", "text", "ref") if not j.get(k)]
    errs = ["missing %s" % k for k in errs]
    if not (j.get("ref_text") or "").strip():
        errs.append("missing ref_text: VoxMel needs the reference transcript")
    if j.get("mode", "clone") != "clone":
        errs.append("VoxMel clones only; use voxcpm2.py to design")
    return errs


def main():
    jobs = [j for j in json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")) if not Path(j["out"]).exists()]
    bad = {j.get("out"): check(j) for j in jobs if check(j)}
    if bad:
        raise SystemExit("bad jobs: %s" % json.dumps(bad))
    if not jobs:
        print("DONE", flush=True)
        return
    for j in jobs:  # before the chdir below
        j["out"], j["ref"] = str(Path(j["out"]).resolve()), str(Path(j["ref"]).resolve())
    home, weights = paths(jobs[0])
    import soundfile as sf
    import torch
    import torchaudio

    def _load(path, *a, **k):  # torchaudio 2.9+ load wants torchcodec; soundfile does the job
        d, sr = sf.read(str(path), dtype="float32", always_2d=True)
        return torch.from_numpy(d.T.copy()), sr

    torchaudio.load = _load
    sys.path.insert(0, str(home))
    os.chdir(home / "examples" / "voxmel")  # its config names the tokenizer by a relative path
    from voxcore import VoxMel

    model = VoxMel.from_pretrained(str(weights), tokenizer_path=str(home / "examples" / "voxmel" / "qwen_tokenizer"),
                                   vocos_path=str(weights / "vocos"), device="cuda" if torch.cuda.is_available() else "cpu")
    for j in jobs:
        steps = int(j.get("steps", STEPS))
        t = time.time()
        w = model.generate(j["text"], prompt_wav_path=j["ref"], prompt_text=j["ref_text"].strip(),
                           seed=j.get("seed", 0), inference_timesteps=steps, up_num_steps=steps)
        out = Path(j["out"])
        out.parent.mkdir(parents=True, exist_ok=True)
        sf.write(out, w, model.sample_rate)
        out.with_suffix(".json").write_text(json.dumps({**j, "model": MODEL, "steps": steps}, indent=2) + "\n", encoding="utf-8")
        print("%s %.1fs audio in %.0fs" % (out.name, len(w) / model.sample_rate, time.time() - t), flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
