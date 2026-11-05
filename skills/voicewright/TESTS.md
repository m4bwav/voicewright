# Tests: voicewright

Cases are in `evals/evals.json`; unit tests in the repository's `tests/`. A test passes on evidence, never on prose.

## Runs

None yet.

## Fixtures

`make_fixture.py` needs `VW_EVAL_AUDIO`: a folder of invented-voice clips, kept out of the repo until cleared. Mark's copy is `voicewright-lab/fixture_src`. It holds nine distinct voices (`captain dwarf kid maid merchant soldier villain wizard queen`, all under 0.55 pairwise), `captain_dup` (a clone of captain, 0.806), `other_voice_line` (planted drift, 0.259) and `lines/` (dwarf clones, the flagged 0.350 line removed).

Verified 2026-11-05: `cast` fails only v0 / v7; `noisy` fails take1 at -30.5 dB and passes take2; `dwarf` drifts line06. Build each case in its own folder: `rebuild` overwrites `voices/keeper.wav`.
