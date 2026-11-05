# What the numbers mean

Heuristics, not verdicts. A person's ear decides.

## Identity: CAM++ cosine (`cast`, `library`, `line`)

Calibrated 2026-11-04 on Mini LibriSpeech dev-clean-2 (CC BY 4.0): 26 real speakers, 4 clips each, median 8 s, single-clip pairs.

| pairs | p1 | p5 | median | p95 | p99 | extreme |
|---|---|---|---|---|---|---|
| same speaker (156) | 0.594 | 0.660 | 0.818 | 0.926 | 0.938 | min 0.569 |
| different speakers (5,200) | -0.085 | -0.025 | 0.133 | 0.366 | 0.464 | max 0.625 |

- `cast_fail` and `library_fail` 0.55: 0% of same-speaker pairs fell below it; 0.06% of different-speaker pairs reached it.
- `cast_warn` 0.45: 1.4% of different-speaker pairs reach it. A warning means listen.
- `line_floor` 0.55. With 5 or more lines, the bar rises to the batch's mean minus 2 SD.

Limits: clean read English speech of real people, not TTS, not acted, not short lines. Clones can fool speaker models, so a pass never proves a voice is good or right. Use one model only; scores do not transfer to other models. Thresholds on generated voices: see the lab note in `ai-docs/research/`.

## Clip faults (`measure`)

| check | value | basis |
|---|---|---|
| clipping | peak at -0.1 dBFS or over 2 clipped samples | arithmetic |
| noise floor | fail over -40 dB, warn over -60 dB | -60 is the ACX limit; -40 is a starter value, uncalibrated |
| phrase level jump | 6 dB | starter value, uncalibrated |
| tail | 0.5 s | starter value from reports of junk in tails |
| sibilance | 5-9 kHz above 1-4 kHz | starter value, uncalibrated |
| steady tone | 8 dB over baseline, on 30 s or more (every short take falsely flagged in the lab) | one measured Qwen3 case, 10 dB before a notch |
| flat read | pitch range under 2.5 semitones | starter value; research links low variation to lower ratings |

No validated script detects metallic sound. `flatness_4_8k` and `hf_cutoff_hz` are reported for comparing takes, with no pass mark. NISQA weights are non-commercial, so it is not bundled.

Pitch and pace are not identity. Measure a dry line, never a mix.
