"""Run a job list on Qwen3-TTS, in the Python environment that has qwen_tts. Resumes: an existing output is skipped.

  python qwen3.py jobs.json [--device cpu|cuda]

jobs.json is a list of {"out", "mode": "design"|"clone", "text", "seed", "language"?} plus, for design, "instruct", and
for clone, "ref", "ref_text" and optional "x_vector": true (keeps timbre, lets the text drive delivery; use for shouts).
Each output gets a .json beside it with everything needed to rebuild it.
"""
import json
import sys
import time
from pathlib import Path

import soundfile as sf
import torch
from qwen_tts import Qwen3TTSModel

MODELS = {"design": "Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign", "clone": "Qwen/Qwen3-TTS-12Hz-1.7B-Base"}


def main():
    jobs = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    device = sys.argv[sys.argv.index("--device") + 1] if "--device" in sys.argv else "cpu"
    for mode, name in MODELS.items():
        todo = [j for j in jobs if j["mode"] == mode and not Path(j["out"]).exists()]
        if not todo:
            continue
        dtype = torch.float32 if device == "cpu" else torch.bfloat16
        model = Qwen3TTSModel.from_pretrained(name, device_map=device, dtype=dtype)
        for j in todo:
            torch.manual_seed(j["seed"])
            t = time.time()
            # Generation can run away on a short line and never stop (33 min on one clip, lab 2026-11-04): cap it.
            cap = {"max_new_tokens": max(120, len(j["text"]) * 2)}
            if mode == "design":
                w, sr = model.generate_voice_design(text=j["text"], language=j.get("language", "English"), instruct=j["instruct"], **cap)
            else:
                kw = {"x_vector_only_mode": True} if j.get("x_vector") else {"ref_text": j["ref_text"]}
                w, sr = model.generate_voice_clone(text=j["text"], language=j.get("language", "English"), ref_audio=j["ref"], **kw, **cap)
            out = Path(j["out"])
            out.parent.mkdir(parents=True, exist_ok=True)
            sf.write(out, w[0], sr)
            out.with_suffix(".json").write_text(json.dumps({**j, "model": name, "device": device}, indent=2) + "\n", encoding="utf-8")
            print("%s %.1fs audio in %.0fs" % (out.name, len(w[0]) / sr, time.time() - t), flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
