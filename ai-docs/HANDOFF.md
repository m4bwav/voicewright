# Handoff: voicewright

State on 2026-11-06, session 9. Start here.

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

Page `voicewright-lab/ask_decide` read 2026-11-06, all five answered; `sample` and `plugin` done and closed. `vipbench` also done and closed. `engines` and `suite` stay open until done.

- **Permission for three installs.** He chose installs by the agent, approved by him, and said he would switch to manual. The session was still in auto mode, and its check refused both `uv sync --all-extras` in `D:/AI/voice-engines/index-tts` and `uv pip install -r requirements.txt` for the suite. Do not route around it. Once he has switched to manual, run them in this order:
  1. IndexTTS-2.5: `uv sync --all-extras` in its clone, then `hf download IndexTeam/IndexTTS-2.5 --local-dir=checkpoints`. Own venv. Licence read 2026-11-06 (clone d9e41aa): a separate licence is needed above 100 million monthly users or RMB 1 billion annual revenue; section 3 bars using the model or any Derivative Work, a term that covers model outputs, to improve any AI model other than itself, its derivatives or non-commercial models. So its clips must not train or tune a commercial model. Using clips in a product fits the grant, but the agreement also passes duties to downstream recipients; read those before commercial advice.
  2. Ming-3.0: use the `tiny` model and `requirements-tiny.txt`, Python 3.10.15 and a venv of its own. The 0.5b build was tested only on 80 GB and 96 GB cards. Tiny's pins are CUDA 11.8 wheels, so they may not run on the RTX 5060 Ti (Chatterbox hit the same "no kernel image" fault); test that first.
  3. TTS Audio Suite: clone at `D:/ComfyUI/custom_nodes_staging/TTS-Audio-Suite` (ccc2404, v5.10.8), not yet in `custom_nodes`. Dry run against the ComfyUI venv: 93 new packages, only `huggingface-hub` changes, torch, numpy and transformers untouched. Save `pip freeze` first. Install with `uv pip install --python D:/ComfyUI/.venv/Scripts/python.exe -r requirements.txt`. Do NOT run its `install.py`: it can uninstall and reinstall torch in the venv the film work shares. Copy into `custom_nodes`, restart ComfyUI only with an empty queue, load a film workflow to prove it still runs, then close `suite`.
- Then add both engines to the bake-off and listen blind.
- Social preview upload is a click in GitHub settings: `.github/images/social-preview.jpg`.

## Owed

1. Hume's own notice was never read: its docs now show only Audio Decisions. After 2026-11-13, note whether the APIs did end.
## Rules that bind

Installs, paid APIs, real voices and outward posts need Mark. Do not publish lab audio until he clears it.
