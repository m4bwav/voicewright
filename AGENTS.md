# AGENTS.md

Rules for any AI agent working in this repository. `CLAUDE.md` imports this file; `.github/copilot-instructions.md` points here.

## What this is

voicewright: one skill, `skills/voicewright/`. SKILL.md holds the workflow, `references/` the details, `scripts/vw.py` the bible and checks, `scripts/engines/` engine runners. Research, decisions, the log and the handoff are under `ai-docs/` (start with `ai-docs/HANDOFF.md`). Map: `CODEMAP.md`.

## Rules

- `vw.py`: standard library for the bible and level checks; numpy, onnxruntime and the speaker model stay optional. Python 3.9+, UTF-8, LF. Every change gets a test. Run `python -m unittest discover -s tests`.
- `voices.json` is the contract with cinewright and musicwright. Change it only with a schema bump and `migrate`. Plugins read the file and never import each other.
- This repo is public. No private names, hostnames, paths or lab audio. Audio samples only from voices with clear rights.
- No real person's voice without written consent. No imitations of named people, in prompts, evals or samples.
- Thresholds change only with a calibration note in `references/thresholds.md`. A heuristic is never a verdict.
- Size budget: `python scripts/budget.py`.
- Evergreen unit: read `skills/voicewright/evergreen.json` before editing; log changes in its CHANGELOG with the reason, lessons in LEARNINGS with Trigger and Hypothesis. Beat `ai-voice` feeds refreshes.
- A release bumps `.claude-plugin/plugin.json`, `plugin.json`, `VERSION` in `vw.py`, `metadata.version` in SKILL.md and the CHANGELOG together.
- Plain short sentences, no em dashes, relative links. No AI attribution anywhere.

## Commands

- Tests: `python -m unittest discover -s tests`
- Budget: `python scripts/budget.py`
- Evals: `claude plugin eval . --no-publish --trust-plugin --case "trigger-*"`
