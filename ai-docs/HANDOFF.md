# Handoff: voicewright

State on 2026-11-05. Start here.

## Done

- Public repo https://github.com/m4bwav/voicewright, release v0.1.1. everscout has the `ai-voice` beat.
- Clone default settled: VoxCPM2 first. Bake-off tied 2 to 2; pilot scene kept VoxCPM2, guess shown first: `research/2026-11-04-lab.md`. Denoise test: no audible difference on clean takes.
- Evals rerun: triggers 9/9, decoys 9/9, action 29/30, baseline 2/10: `skills/voicewright/TESTS.md`. Runner `evals/run_local.py`.
- `ai-voice` scanned 2026-11-05: 37 notes in `~/.everscout/data/ai-voice`. The beat's weekly web searches were not run.
- Lab audio is outside the repo at `Ai/voicewright-lab`.

## Waiting on Mark

- IndexTTS-2.5 and Ming-3.0: he chose to run the installs or add a rule himself. Cloned to the engines folder, nothing installed. Do not route around this.
- TTS Audio Suite still waits.
- Wiki: `voicewright.wiki.git` does not exist until a first page is saved at https://github.com/m4bwav/voicewright/wiki/_new (any text). Then write it with `wikiwright`.
- Social preview upload is a click in GitHub settings: `.github/images/social-preview.jpg`.
- Whether the pilot take may replace the public sample. Not asked yet; the sample stays until he clears one.

## Owed

1. Worth verdict is still UNPROVEN: `worth --ab` returned ungradable on this evidence shape. Convert the cases to its expectations, or give a harness adapter, proving on one case at one run before paying for more.
2. stereotype-trap 2/3: one prompt file held a type word. Read the case and tune if it repeats.
3. Read the VIPBench paper (arXiv 2611.05638): listeners called 41% of clone pairs different people. Consider it for `references/thresholds.md`, with a calibration note.
4. Add IndexTTS and Ming to the bake-off once he has installed them.
5. Confirm the Hume end date from Hume (an aggregator says 2026-11-13; Hume's intro page does not mention it). Run the beat's web searches.

## Rules that bind

Installs, paid APIs, real voices and outward posts need Mark. Do not publish lab audio until he clears it.
