# Generating lines

- Line list: JSON or CSV of `id`, `voice`, `text`, `say`, `direction`, `emotion`. `text` is for subtitles, `say` is for the engine. Name clips `<voice>_<id>_t<take>.wav`. A game dialogue file is converted to this list, never edited.
- Pronunciation: respell in `say` to a spelling with one reading ("bough" for a ship's bow). Speech-to-text writes words, not sounds, so it passes the wrong homograph; check the vowel with a phoneme recogniser or by ear.
- Chunks: engines drift and speed up on long text and break on very short lines. Stay under about 20 s or 350 characters a chunk; pad a one-word line inside a phrase and cut it out.
- References: 5-30 s of dry speech, one clear delivery, nothing under it; room sound in a reference carries into every take. In-context clones copy the reference's delivery; for a shout use embedding-only mode (Qwen3 `x_vector`) and one reference per emotion.
- Direction: scene, the line before, the intent. Long director's notes are a known cause of voice drift, so keep identity out of them.
- Dialogue: render each line alone with frozen voices and join, unless a test proves a native multi-speaker engine holds its voices.
- Batches: use the idle host; on a busy shared GPU queue behind it and wait. `engines/qwen3.py jobs.json` runs a resumable batch.
- Review: `VW review`; note heard or unheard for each clip.
