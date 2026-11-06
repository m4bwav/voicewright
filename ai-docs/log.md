# Log

## 2026-11-04

Kickoff run. Name kept: voicewright is clear and matches the family. One skill, not several, to keep the install small. Built beat, research, `vw.py`, calibration, lab renders, listening page, banner, integration PRs, public repo. Scan's first thread call used the configured fetchwright reader; the rest used the same-source reader. A lab render ran away for 33 minutes on one clip with no length cap and went unnoticed until the user asked; the runner now caps tokens, and long waits should watch log progress, not only completion.

Second session. Read the listening answers and acted on them: design step renders traits and briefs, a low score on a generated line means listen, `line` warns on pitch and words per second, pilot sample added (commit d1d65ea). The permission check refused a detached four-engine install script; single visible installs of the pip packages VoxCPM2 and Chatterbox passed, while installs from the IndexTTS and Ming clones were refused, so those wait for Mark. Bash quoted heredocs with apostrophes broke again: write patch scripts with the Write tool.

Bake-off started: VoxCPM2 rendered. Chatterbox failed twice, on a runner named like its package (renamed `chatterbox_run.py`) and on a CPU-only torch. The earlier Qwen3 environment was not found, so it was reinstalled in its own venv.

## 2026-11-05

Third session. All three engines rendered 16 clips; the previous session's waiting job did Qwen3 (a duplicate of mine was stopped by PID). Chatterbox needed CPU and `setuptools<81`. Eval fixtures rebuilt from invented-voice clips in `VW_EVAL_AUDIO`, outside the repo. Blind page `ask_bake` served; it also asks about the repo and the two refused installs.

Fourth session. Unblinded the bake-off: VoxCPM2 2, Qwen3 2, Chatterbox 0. Set VoxCPM2 first for cloning on no faults, with the pilot as tie-break. Mark approved the repo: created public, CI found a real Python 3.9 bug, fixed. `.gitignore` had been hiding the pilot sample. Rendered the pilot on VoxCPM2 and served blind `ask_pilot`, with a denoiser test. Calibrated on generated voices: no threshold changed. WSL's `claude` turned out to be the Windows binary, so `evals/run_local.py` replaced `plugin eval`; three runner bugs cost two runs (cmd.exe cutting prompts, decoy kind, an IPA print). Evals found a soundalike trigger miss and two skill gaps, tuned. everscout 0.12.0 released with the beat.
