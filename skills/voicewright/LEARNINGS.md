# Learnings: voicewright

Procedural lessons for SKILL.md. Trigger and Hypothesis are required. Format: MAINTENANCE.md.

## Active

### L-001 · 2026-11-04 · `tone-on-the-join`: steady tones show on long audio only
- Trigger: inherited from cinewright-voice L-004: Qwen3 clones carried a tone near 1085 Hz that summed on the joined track
- Hypothesis: a codec artefact constant across takes
- Rule: measure tones on the join, with 1 Hz bins against a median baseline; notch 30 Hz wide at -12 dB
- Scope: skill
- Status: new · helpful 1 · harmful 0 · last_confirmed 2026-10-10
