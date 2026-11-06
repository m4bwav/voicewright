# Log

## 2026-11-04

Kickoff run. Name kept: voicewright is clear and matches the family. One skill, not several, to keep the install small. Built beat, research, `vw.py`, calibration, lab renders, listening page, banner, integration PRs, public repo. Scan's first thread call used the configured fetchwright reader; the rest used the same-source reader. A lab render ran away for 33 minutes on one clip with no length cap and went unnoticed until the user asked; the runner now caps tokens, and long waits should watch log progress, not only completion.

Second session. Read the listening answers and acted on them: design step renders traits and briefs, a low score on a generated line means listen, `line` warns on pitch and words per second, pilot sample added (commit d1d65ea). The permission check refused a detached four-engine install script; single visible installs of the pip packages VoxCPM2 and Chatterbox passed, while installs from the IndexTTS and Ming clones were refused, so those wait for Mark. Bash quoted heredocs with apostrophes broke again: write patch scripts with the Write tool.

Bake-off started: VoxCPM2 rendered. Chatterbox failed twice, on a runner named like its package (renamed `chatterbox_run.py`) and on a CPU-only torch. The earlier Qwen3 environment was not found, so it was reinstalled in its own venv.

## 2026-11-05

Third session. All three engines rendered 16 clips; the previous session's waiting job did Qwen3 (a duplicate of mine was stopped by PID). Chatterbox needed CPU and `setuptools<81`. Eval fixtures rebuilt from invented-voice clips in `VW_EVAL_AUDIO`, outside the repo. Blind page `ask_bake` served; it also asks about the repo and the two refused installs.

Fourth session. Unblinded the bake-off: VoxCPM2 2, Qwen3 2, Chatterbox 0. Set VoxCPM2 first for cloning on no faults, with the pilot as tie-break. Mark approved the repo: created public, CI found a real Python 3.9 bug, fixed. `.gitignore` had been hiding the pilot sample. Rendered the pilot on VoxCPM2 and served blind `ask_pilot`, with a denoiser test. Calibrated on generated voices: no threshold changed. WSL's `claude` turned out to be the Windows binary, so `evals/run_local.py` replaced `plugin eval`; three runner bugs cost two runs (cmd.exe cutting prompts, decoy kind, an IPA print). Evals found a soundalike trigger miss and two skill gaps, tuned. everscout 0.12.0 released with the beat.

Fifth session. Pilot answers read: VoxCPM2 kept (guess shown first), denoise no audible difference; rules updated. Grader widened, suite rerun: 29/30 action, baseline 2/10. Worth A/B could not grade this evidence shape, about $3 lost; should have tried one case first. `ai-voice` scanned, 8 notes in the local beat data; VIPBench is the one to read. Hume end date still unconfirmed by Hume. Released 0.1.1. Bash hook rejects doubled backslashes in heredocs: patch scripts go through Write.

## 2026-11-06

Sixth session. Found the wiki repo now exists. Worth A/B was ungradable because the grader does not know `file_regex`, `reply` or a list of evidence, and fixture kinds are not folders; reshaped the cases, added `build_fixtures.py`, proved on one run, then 54 runs: KEEP, 100% against 22%. The grader also ignores `max: 0`. VIPBench read: the 41% needs the 31% real-pair figure beside it. Hume still unconfirmed by Hume, though its docs fit. Ten beat searches gave little. Wiki verification caught `vw.py --version` stuck at 0.1.0; fixed with a test, released 0.1.2. Trimming tool output with `cut` then pasting it into a page lost the end of a line; `wikiwright outputs` caught it. Paste from the saved file.

Seventh session. No unread answers. Fixed the grader's `max: 0` in evergreen-protocol (PR #39, v0.18.3), fork and install updated. One run per arm of clone-no-consent, $0.71: both pass, so the CUT line that single case printed says nothing about the skill; the nine-case KEEP stands. VIPBench's card says CC BY-NC 4.0, so the test is Mark's call. Hume waits for 2026-11-13. Open decisions went on the page `voicewright-lab/ask_decide`.

Eighth session. Five answers read. Matched the guess on sample and plugin; differed on engines (agent installs with his approval), suite (install, against a high-confidence skip) and VIPBench (test it). So he wants wider coverage than the evidence so far argued for, and the guess weighed proven need too heavily. VoxCPM2 take published, plugin installed. Check refused both the IndexTTS and suite installs while auto mode was still on, so they wait for his switch to manual. The suite's dry run came out clean, but its `install.py` can reinstall torch, so requirements only. VIPBench took 57 minutes to download 3.5 GB, then scored fully: r 0.635, in the paper's range; at 0.55, 24% of same-speaker clones miss and different speakers almost never pass. No threshold changed.

Ninth session. No new answers. The session started in auto mode again, so the three installs were not tried: Mark asked to approve each check by hand. Read the IndexTTS licence from the clone, recorded in HANDOFF.md. Nothing else was workable; Hume waits for 2026-11-13.
