#!/usr/bin/env bash
# Runs only with `claude plugin eval --scaffold`.
set -euo pipefail
python3 "$VW_REPO/skills/voicewright/evals/fixtures/make_fixture.py" rebuild
