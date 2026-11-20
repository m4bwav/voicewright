# Learnings: voicewright

Procedural lessons for SKILL.md. Trigger and Hypothesis are required. Format: MAINTENANCE.md.

## Active

### L-004 · 2026-11-20 · `voxmel-4-steps-runaway`: 4 steps let a clip run away
- Trigger: 30 VoxMel lines at 4 / 8 / 32 steps, same seeds: WER 38.0% / 2.6% / 1.0%; at 4 steps one clip became a long stutter
- Hypothesis: the steps are guided Euler steps on the GRPO model, not a distilled few-step student (arXiv:2611.20254), so 4 is under-sampled
- Rule: default 8 steps; 4 only for drafts that will be heard; check WER, not just similarity, when changing steps (similarity barely moved, 0.874 to 0.893)
- Scope: skill
- Status: new · helpful 0 · harmful 0 · last_confirmed 2026-11-20

### L-002 · 2026-11-04 · `traits-tie-briefs`: trait prompts did not win by ear
- Trigger: blind listen, four briefs: traits won maid and villain, plain brief won dwarf and young woman
- Hypothesis: on Qwen3 either prompt style can land near a stock voice; one take per condition is thin
- Rule: render both styles and let the ear choose; make no claim that traits are better
- Scope: skill
- Status: new · helpful 0 · harmful 0 · last_confirmed 2026-11-04

### L-003 · 2026-11-04 · `low-score-same-person`: 0.350 was heard as one person
- Trigger: dwarf clone line 4 scored 0.350 at +11.6 semitones; the listener heard all six as one person
- Hypothesis: CAM++ is thrown by pitch and pace on generated lines, so it can over-flag them
- Rule: DRIFT on a generated line means listen, not reject; the floor stays until more listening
- Scope: skill
- Status: new · helpful 0 · harmful 0 · last_confirmed 2026-11-04

### L-001 · 2026-11-04 · `tone-on-the-join`: steady tones show on long audio only
- Trigger: inherited from cinewright-voice L-004: Qwen3 clones carried a tone near 1085 Hz that summed on the joined track
- Hypothesis: a codec artefact constant across takes
- Rule: measure tones on the join, with 1 Hz bins against a median baseline; notch 30 Hz wide at -12 dB
- Scope: skill
- Status: new · helpful 1 · harmful 0 · last_confirmed 2026-10-10
