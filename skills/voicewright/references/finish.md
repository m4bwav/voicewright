# Finishing

Order: pick the cleanest take, trim, fix faults a check found, match EQ between sources, add room tone, level for the destination.

- **Denoise only on evidence.** No direct test of denoisers on TTS output was found in research. Our one test: ffmpeg `afftdn` on two clean takes, one listener could not tell them from the originals, so it gained nothing and showed no harm. Generative enhancers can invent sound and were not tested. Default: do not denoise unless `measure` reports noise; compare before and after blind.
- A steady tone across a joined track: `ffmpeg -af equalizer=f=<Hz>:t=h:w=30:g=-12`. Measure on the join, not per take; never trust a line in a spectrogram picture.
- Room tone: a shared bed about -50 to -60 dB hides dead digital silence between lines (lightly sourced).
- Short clips: use `--short`, because loudness normalization misjudges them, then set the level by ear.

| destination | target | note |
|---|---|---|
| acx, audiobook | RMS -23 to -18 dB, peak -3 dB, noise -60 dB, 44.1 kHz | ACX requires human narration unless authorized: do not advise upload otherwise |
| narration | -16 LKFS +/-1, -1 dBTP | Apple podcast spec |
| film | -27 dialogue-gated, -2 dBTP | streaming delivery, from secondary sources |
| game | keep lines even; -24 console, -18 mobile apply to the whole mix | not per line |
| web | -16 LUFS, -1 dBTP | common practice |
