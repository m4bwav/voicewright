# Handoff: voicewright

State on 2026-11-04. Start here.

## Done

- Research: `research/2026-11-04-voice-survey.md` and its parts. Beat `ai-voice` merged into everscout (PR #141, unreleased), first scan 29 notes, literature filled.
- Plugin 0.1.0 code: skill, references, `vw.py`, `engines/qwen3.py`, tests, bible schema 1. Speaker thresholds calibrated on real speech.
- Lab results: `research/2026-11-04-lab.md`. Lab audio lives outside the repo at `Ai/voicewright-lab`.
- Listening page: `Ai/voicewright-lab/ask_listen1`. Read with `python Ai/askwright/skills/askwright/scripts/ask.py read <dir>`. Restart with `serve --detach`.
- Integration PRs: see `log.md`.

## Waiting on Mark

Public repo not created: the auto-mode permission check refused `gh repo create m4bwav/voicewright --public`. Everything is committed locally on main. With his go-ahead: create it, push, tag v0.1.0 after CI, write the wiki, then update installed copies.

Answers on the listening page: four blind trait-against-brief picks, is the dwarf one person, is the pilot scene publishable, which engines to install. TTS Audio Suite also still waits.

## Owed

1. Act on the answers. If traits do not win by ear, rewrite the design step.
2. Bake-off once engines are approved; fixed script, `vw.py` checks, listening page.
3. Calibrate thresholds on generated voices and on hearing: same-prompt seeds score 0.48 to 0.67, straddling the 0.55 bar.
4. Add a pitch-creep warning to `line`: dwarf clones ran 1 to 10 semitones above the reference while passing identity. Length sanity: a runaway line ran 9.5 s for 12 words; add words-per-second to `line`.
5. Evals NOT run. Fix fixtures first: synthetic buzz does not separate on CAM++ (`cast` fails 11 pairs, so the planted pair is not singled out) and the `noisy` clean take fails on noise floor because it has no gaps. Use real invented-voice clips with clear rights. Run under WSL, since native Windows has no Bash sandbox. Then TESTS.md and the worth check.
6. Denoiser test by ear: ffmpeg `afftdn` on clean takes moved identity to 0.92-0.94 and flatness slightly; no listening yet.
7. Pipeline scan under Reddit RSS ending 2026-11-13. Everscout release with the beat. Hume API end date unconfirmed.
8. Social preview upload is a click in GitHub settings: `.github/images/social-preview.jpg`.

## Rules that bind

Installs, paid APIs, real voices and outward posts need Mark. Do not publish lab audio until he clears it.
