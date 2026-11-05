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

## Engines

`D:\AI\voice-engines`, one venv each, HF cache in `hf`. VoxCPM2 and Chatterbox packages installed; see the log for weights. Engine runners not written yet. The GPU was held by another session's Viggle render: queue behind it.

## Owed

1. Bake-off: runners for VoxCPM2 and Chatterbox, fixed script, `vw.py` checks, listening page. Add IndexTTS and Ming if cleared.
2. Calibrate thresholds on generated voices and on hearing: same-prompt seeds score 0.48 to 0.67, straddling the 0.55 bar; a 0.350 line passed by ear.
3. Evals NOT run. Fix fixtures first: synthetic buzz does not separate on CAM++ (`cast` fails 11 pairs, so the planted pair is not singled out) and the `noisy` clean take fails on noise floor because it has no gaps. Use real invented-voice clips with clear rights. Run under WSL, since native Windows has no Bash sandbox. Then TESTS.md and the worth check.
4. Denoiser test by ear: ffmpeg `afftdn` on clean takes moved identity to 0.92-0.94 and flatness slightly; no listening yet.
5. Pipeline scan under Reddit RSS ending 2026-11-13. Everscout release with the beat. Hume API end date unconfirmed.
6. Social preview upload is a click in GitHub settings: `.github/images/social-preview.jpg`.

## Rules that bind

Installs, paid APIs, real voices and outward posts need Mark. Do not publish lab audio until he clears it.
