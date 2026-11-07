# Handoff: voicewright

State on 2026-11-06, session 10. Start here.

## Done

- Public repo https://github.com/m4bwav/voicewright, release v0.1.2, wiki at 0.1.2: https://github.com/m4bwav/voicewright/wiki (`ai-docs/notes/2026-11-06-github-wiki.md`). everscout has the `ai-voice` beat.
- Clone default settled: VoxCPM2 first. Bake-off tied 2 to 2; pilot scene kept VoxCPM2, guess shown first: `research/2026-11-04-lab.md`. Denoise test: no audible difference on clean takes.
- Worth verdict KEEP, 100% against 22%: `skills/voicewright/TESTS.md`. Stereotype-trap 3/3 there, so no tuning.
- VIPBench read and cited in `references/thresholds.md`, no threshold changed. Beat searches run: `research/2026-11-06-beat-searches.md`.
- Lab audio is outside the repo at `Ai/voicewright-lab`. The one exception: Mark cleared the VoxCPM2 pilot take on 2026-11-06, and it is now the README sample (PR #8).
- CAM++ tested on VIPBench, private report in `research/2026-11-06-beat-searches.md`: r 0.635, no threshold changed.
- Plugin installed on this PC as `voicewright@voicewright`, from the public repo, so `claude plugin update voicewright@voicewright` now applies.

- evergreen 0.18.3 honours `min` and `max` on a trace in the A/B grader (evergreen-protocol PR #39), released and installed. clone-no-consent graded correctly, but it passes without the skill too, so it stays marked redundant.

## Waiting on Mark

- **Blind listen, five engines:** `voicewright-lab/ask_bake2`, key in `bake2_key.json`. Read with `ask.py read voicewright-lab/ask_bake2`; `serve --detach` if down. Picks decide whether IndexTTS-2.5 or Ming-3.0 tiny changes the default in `references/engines.md`. Do not change the ranking before then.
- Social preview upload is a click in GitHub settings: `.github/images/social-preview.jpg`.

## Installed 2026-11-06 (session 10, manual approval)

- IndexTTS-2.5: `uv sync` with no extras, because `flash-attn` in `accel` needs a CUDA toolkit. Licence terms: clips must not train or tune a commercial model; separate licence above 100 million monthly users or RMB 1 billion revenue; read the downstream duties before commercial advice.
- Ming-3.0 tiny: own venv, Python 3.10.15, `requirements-tiny-win.txt` in the clone (torch 2.7.1+cu128, `triton-windows`), because cu118 cannot drive the RTX 5060 Ti and `triton` has no Windows wheel. Text normalization off (no `pynini`). About 20 s per line.
- TTS Audio Suite in `D:/ComfyUI/custom_nodes`, from requirements minus `pyworld`, which needs a C++ compiler and serves only RVC harvest/dio. `install.py` not run. 92 packages added, only `huggingface-hub` changed; freezes in `voicewright-lab/comfyui_freeze_*`. No suite engine has been rendered yet.

## Owed

1. Hume's own notice was never read: its docs now show only Audio Decisions. After 2026-11-13, note whether the APIs did end.
## Rules that bind

Installs, paid APIs, real voices and outward posts need Mark. Do not publish lab audio until he clears it.
