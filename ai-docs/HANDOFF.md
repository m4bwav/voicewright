# Handoff: voicewright

State on 2026-11-05. Start here.

## Done

- Public repo https://github.com/m4bwav/voicewright, release v0.1.0. Plugin code, skill, tests, bible schema 1, pilot sample. everscout 0.12.0 released with the `ai-voice` beat.
- Bake-off unblinded: VoxCPM2 2, Qwen3 2, Chatterbox 0. VoxCPM2 first for cloning: `research/2026-11-04-lab.md`.
- Thresholds checked on generated voices, none changed: `references/thresholds.md`.
- Evals run and tuned: `skills/voicewright/TESTS.md`. Runner `evals/run_local.py`; cases `evals/build_cases.py`.
- Lab audio is outside the repo at `Ai/voicewright-lab`.

## Waiting on Mark

- Blind page `Ai/voicewright-lab/ask_pilot`: the pilot scene on two engines and a denoiser test. Read with `python Ai/askwright/skills/askwright/scripts/ask.py read <dir>`, restart with `serve --detach`, unblind with `voicewright-lab/pilot_key.json`.
- IndexTTS-2.5 and Ming-3.0: he chose to run the installs or add a rule himself. Cloned to the engines folder, nothing installed. Do not route around this.
- TTS Audio Suite still waits.
- Wiki: `voicewright.wiki.git` does not exist until a first page is saved at https://github.com/m4bwav/voicewright/wiki/_new (any text). Then write it with `wikiwright`.
- Social preview upload is a click in GitHub settings: `.github/images/social-preview.jpg`.

## Owed

1. Read `ask_pilot`. Scene pick sets the clone default: on a Qwen3 win, swap the order in `references/engines.md`; on "neither", say so and try IndexTTS and Ming if installed. Denoise pick confirms or changes the rule in `references/finish.md`. Update the public sample only with a cleared take.
2. Add IndexTTS and Ming to the bake-off once he has installed them.
3. Widen the stock-default grader path, rerun soundalike and the suite, then the worth check.
4. Scan the `ai-voice` beat before Reddit RSS ends on 2026-11-13. Hume API end date unconfirmed.

## Rules that bind

Installs, paid APIs, real voices and outward posts need Mark. Do not publish lab audio until he clears it.
