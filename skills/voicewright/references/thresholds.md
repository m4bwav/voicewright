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

Generated voices, one listener, 2026-11-04: Mark heard six Qwen3 dwarf clone lines as one person, including one at 0.350 that the check flagged. So DRIFT below the bar on a generated line means listen, not reject. The floor is unchanged: one take and one listener do not recalibrate it.

`line` also prints `LISTEN:` warnings that never change the exit code: `PITCH` over 4 semitones from the reference, and `SLOW` or `FAST` outside 1.5 to 4.5 words per second, using `text` from the `.json` beside the clip. Starter values, uncalibrated, set from the lab's runaway line (+11.6 semitones, 1.3 words per second).

Generated voices, measured 2026-11-05 on three engines, 66 short clips of four invented voices, line against line (88 same-voice pairs, 362 different): same median 0.736, min 0.457, 11% under 0.55; different median 0.153, p95 0.431, 0.3% at 0.55 or over. So `cast_fail` holds on generated voices. `line_floor` over-flags them, and by engine: 0% under it for Chatterbox, 21% and 38% for VoxCPM2, so compare a generated line within its engine and listen. No threshold changed. "Same voice" here means cloned from one reference; only a few were heard.

Why a person's ear still decides: VIPBench (Tang and Groh, arXiv 2611.05638, read 2026-11-06), 124,876 same-or-different judgments from 1,290 listeners, mostly unfamiliar with the speakers. Listeners said "different" to 41% of real-against-clone same-speaker responses, but also to 31% of real-against-real ones, and "same" to 26% of different-speaker real pairs. So the clone penalty is about 10 points, and a single listener's "not the same" is weak evidence alone; ask more than once. No model reached the noise ceiling (best 61% of explainable variance), and the paper recommends no fixed cosine cut-off. CAM++ was not among its eleven models, and nearly all clones came from one engine (Cartesia Sonic 3), so none of these numbers transfers to ours. No threshold changed.

Limits for the first table: clean read English speech of real people, not TTS, not acted, not short lines. Clones can fool speaker models, so a pass never proves a voice is good or right. Use one model only; scores do not transfer to other models. Thresholds on generated voices: see the lab note in `ai-docs/research/`.

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
