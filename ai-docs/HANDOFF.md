# Handoff: voicewright

State on 2026-11-04. Start here.

## Done

- Research: `research/2026-11-04-voice-survey.md` and its parts. Beat `ai-voice` merged into everscout (PR #141, unreleased), first scan 29 notes, literature filled.
- Plugin 0.1.0 code: skill, references, `vw.py`, `engines/qwen3.py`, tests, bible schema 1. Speaker thresholds calibrated on real speech.
- Lab results: `research/2026-11-04-lab.md`. Lab audio lives outside the repo at `Ai/voicewright-lab`.
- Listening page: `Ai/voicewright-lab/ask_listen1`. Read with `python Ai/askwright/skills/askwright/scripts/ask.py read <dir>`. Restart with `serve --detach`.
- Integration PRs: see `log.md`.

## Waiting on Mark

- Public repo not created: the auto-mode permission check refused `gh repo create m4bwav/voicewright --public` last session. Everything is committed locally on main. With his go-ahead or a permission rule: create it, push, tag after CI, write the wiki, then update installed copies.
- IndexTTS-2.5 and Ming-3.0 installs: he approved them on the listening page, but the permission check refused running their installs from the clones (`uv sync` in `index-tts`, `requirements.txt` in `Ming-3.0-tts`; reason given for Ming: Code from External). Both are cloned to `D:\AI\voice-engines`, nothing installed. Do not route around this; he runs them or adds a rule.
- TTS Audio Suite still waits.

## Listening answers (2026-11-04), acted on

Traits against brief tied 2-2 (traits: maid, villain; brief: dwarf, young woman). Dwarf heard as one person including the 0.350 line. Pilot scene cleared and added as `.github/samples/pilot-scene.mp3`. Four engines approved. Licences read; none gated.

## Engines and bake-off state

`D:\AI\voice-engines`, one venv each. VoxCPM2 and Chatterbox weights are in `hf` (set `HF_HOME=D:/AI/voice-engines/hf`); Qwen3 weights are in the default user cache. Runners: `skills/voicewright/scripts/engines/` (`voxcpm2.py`, `chatterbox_run.py`, `qwen3.py`).

Jobs: `Ai/voicewright-lab/bake_<engine>.json` from `make_bake.py`: four invented references by four fixed lines, 16 clips per engine, output in `bake/<engine>/`. Runners resume, skipping clips that exist.

- VoxCPM2: 16 of 16 rendered, about 2.5x real time on the GPU.
- Chatterbox and Qwen3: 0 of 16 when this was written. A background job in the previous session was fixing Chatterbox's torch (its venv had a CPU-only build) and then waiting for the GPU. It may have died with that session. First check `bake/`, and `torch.cuda.is_available()` in the Chatterbox venv. Rerun what is missing, with `--device cuda` for Qwen3.
- The GPU is shared and was busy for hours with other sessions' renders. Queue behind them; never stop them.

Next: `vw.py measure`, `line` and `cast` on each engine, level-match, then a listening page with a real guess. Prefer a blind one.

## Owed

1. Bake-off: runners for VoxCPM2 and Chatterbox, fixed script, `vw.py` checks, listening page. Add IndexTTS and Ming if cleared.
2. Calibrate thresholds on generated voices and on hearing: same-prompt seeds score 0.48 to 0.67, straddling the 0.55 bar; a 0.350 line passed by ear.
3. Evals NOT run. Fix fixtures first: synthetic buzz does not separate on CAM++ (`cast` fails 11 pairs, so the planted pair is not singled out) and the `noisy` clean take fails on noise floor because it has no gaps. Use real invented-voice clips with clear rights. Run under WSL, since native Windows has no Bash sandbox. Then TESTS.md and the worth check.
4. Denoiser test by ear: ffmpeg `afftdn` on clean takes moved identity to 0.92-0.94 and flatness slightly; no listening yet.
5. Pipeline scan under Reddit RSS ending 2026-11-13. Everscout release with the beat. Hume API end date unconfirmed.
6. Social preview upload is a click in GitHub settings: `.github/images/social-preview.jpg`.

## Rules that bind

Installs, paid APIs, real voices and outward posts need Mark. Do not publish lab audio until he clears it.
