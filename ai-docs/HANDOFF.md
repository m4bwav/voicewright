# Handoff: voicewright

State on 2026-11-06, session 7. Start here.

## Done

- Public repo https://github.com/m4bwav/voicewright, release v0.1.2, wiki at 0.1.2: https://github.com/m4bwav/voicewright/wiki (`ai-docs/notes/2026-11-06-github-wiki.md`). everscout has the `ai-voice` beat.
- Clone default settled: VoxCPM2 first. Bake-off tied 2 to 2; pilot scene kept VoxCPM2, guess shown first: `research/2026-11-04-lab.md`. Denoise test: no audible difference on clean takes.
- Worth verdict KEEP, 100% against 22%: `skills/voicewright/TESTS.md`. Stereotype-trap 3/3 there, so no tuning.
- VIPBench read and cited in `references/thresholds.md`, no threshold changed. Beat searches run: `research/2026-11-06-beat-searches.md`.
- Lab audio is outside the repo at `Ai/voicewright-lab`.

- evergreen 0.18.3 honours `min` and `max` on a trace in the A/B grader (evergreen-protocol PR #39), released and installed. clone-no-consent graded correctly, but it passes without the skill too, so it stays marked redundant.

## Waiting on Mark

All five decisions below are on one page: `python ../askwright/skills/askwright/scripts/ask.py read ../voicewright-lab/ask_decide` from this repo (if down, `serve ../voicewright-lab/ask_decide --detach`). Served 2026-11-06, unanswered.

- IndexTTS-2.5 and Ming-3.0: he chose to run the installs or add a rule himself. Cloned to the engines folder, nothing installed. Do not route around this. Then add both to the bake-off.
- TTS Audio Suite still waits.
- Testing CAM++ on VIPBench: the dataset card says CC BY-NC 4.0 (read 2026-11-06). On the page; optional.
- Social preview upload is a click in GitHub settings: `.github/images/social-preview.jpg`.
- voicewright is not installed as a plugin on this PC, so `claude plugin update` has nothing to update. Install only on his word.
- Whether the pilot take may replace the public sample. Not asked yet; the sample stays until he clears one.

## Owed

1. Hume's own notice was never read: its docs now show only Audio Decisions. After 2026-11-13, note whether the APIs did end.
## Rules that bind

Installs, paid APIs, real voices and outward posts need Mark. Do not publish lab audio until he clears it.
