# Handoff: voicewright

State on 2026-11-06. Start here.

## Done

- Public repo https://github.com/m4bwav/voicewright, release v0.1.2, wiki at 0.1.2: https://github.com/m4bwav/voicewright/wiki (`ai-docs/notes/2026-11-06-github-wiki.md`). everscout has the `ai-voice` beat.
- Clone default settled: VoxCPM2 first. Bake-off tied 2 to 2; pilot scene kept VoxCPM2, guess shown first: `research/2026-11-04-lab.md`. Denoise test: no audible difference on clean takes.
- Worth verdict KEEP, 100% against 22%: `skills/voicewright/TESTS.md`. Stereotype-trap 3/3 there, so no tuning.
- VIPBench read and cited in `references/thresholds.md`, no threshold changed. Beat searches run: `research/2026-11-06-beat-searches.md`.
- Lab audio is outside the repo at `Ai/voicewright-lab`.

## Waiting on Mark

- IndexTTS-2.5 and Ming-3.0: he chose to run the installs or add a rule himself. Cloned to the engines folder, nothing installed. Do not route around this. Then add both to the bake-off.
- TTS Audio Suite still waits.
- Social preview upload is a click in GitHub settings: `.github/images/social-preview.jpg`.
- voicewright is not installed as a plugin on this PC, so `claude plugin update` has nothing to update. Install only on his word.
- Whether the pilot take may replace the public sample. Not asked yet; the sample stays until he clears one.

## Owed

1. Hume's own notice was never read: its docs now show only Audio Decisions. After 2026-11-13, note whether the APIs did end.
2. Testing CAM++ on VIPBench data needs its licence checked first (none stated on the page read). Optional.
3. evergreen's A/B grader ignores `max: 0` on a trace, which inverts a ban: report or fix it in the evergreen repo. clone-no-consent stays out of the A/B until then.

## Rules that bind

Installs, paid APIs, real voices and outward posts need Mark. Do not publish lab audio until he clears it.
