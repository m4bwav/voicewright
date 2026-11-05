---
name: voicewright
description: "Make original, consistent, high-quality voices and keep them: a voice sheet in acoustic traits, truly different candidates for a blind listen, a versioned voice bible anyone can rebuild from disk, lines per script or dialogue file, and measured checks for a cast that collapses into a few voices, reuse across projects, drift between takes, artifacts and flat reads. Use whenever a game, film, narration, audiobook or kids' story needs a voice or a cast: 'design a voice', 'voice these NPCs', 'keep this voice the same', 'these voices all sound alike', 'it sounds metallic', 'which TTS should I use', 'clone this voice', 'make it sound like <actor>'. Handles consent and sound-alike requests. Film shot workflow is cinewright-voice, which calls this; whole songs are musicwright. Also 'refresh voicewright'."
license: MIT
metadata:
  version: 0.1.0
---

# voicewright

Outcome: every voice exists as an entry in a `voices.json` bible with its sheet, reference clip and transcript, engine, model version, seed, pronunciation list and rights, and every delivered clip has a measured check line. Numbers catch faults; a person's ear decides. Mark anything unheard as unheard.

`VW` means `python scripts/vw.py` from this folder (run it, do not read it). Read one reference when its step needs it. Batch runner: `scripts/engines/qwen3.py`.

## Step 0: freshness

Read `evergreen.json`. If `contradiction` is set or today is on or after `next_due`, say so in one line, do the task, then run `evergreen-refresh`. If `verify_at_use` is true, re-check engine and legal claims before relying on them: they age within weeks. The `ai-voice` everscout beat feeds refreshes when present.

## Step 1: rights first

- A real person's voice, including family or the user's own for others to use: written consent listing the uses, recorded in `rights.consent`, before any clip is touched. No consent, no clone. Ask for it; do not proceed on "they would not mind".
- "Sounds like <named actor, singer or public figure>": decline the imitation, in one sentence, and offer a designed voice from neutral traits. Do not write the name, or thinly veiled identifying details, into a prompt.
- Never promise a voice is exclusive or safe: [references/rights.md](references/rights.md).

## Step 2: pick the engine

By job, licence and hardware, one engine per project: [references/engines.md](references/engines.md). Say the pick and why in one line. Installing an engine, a node or a large model, and any paid API call, needs the user's yes first; use what is installed meanwhile. A non-commercial licence blocks shipping: check before the first render.

## Step 3: design a voice

1. Write the sheet in acoustic traits, not types: [references/design.md](references/design.md). A request like "a sassy maid" or "a gruff dwarf" is a character brief, not a voice: turn it into pitch, resonance, texture, pace and behaviour, and drop the type word from the prompt. Never use an accent as a costume.
2. Make at least three truly different candidates on one fixed line (differ in traits, not just seed).
3. `VW cast --clips <candidates>`: replace any pair that fails, so the listener chooses between real alternatives.
4. `VW library <clip> --against <other bibles> <stock folder>`: a new voice must not be last month's narrator or an engine preset.
5. Level-match, then a blind listen on an askwright page when present (else a labelled list of files). The pick goes in the bible through `VW add`.

## Step 4: lock it

`VW validate <bible>` must pass: [references/bible.md](references/bible.md). A voice with no engine, model version, seed or reference is not locked. A model update is a recast: re-test against the locked clips.

## Step 5: generate lines

Keep a line list with `text` for subtitles and `say` for the engine, and a pronunciation list per project: [references/generate.md](references/generate.md). Name clips per line. Generate through the locked reference and settings; change one thing per retry; budget several takes for acted lines. Direct by scene, the line before, and intent.

## Step 6: check every batch

```
VW measure <clips>               # level, noise, clipping, jumps, tail, sibilance, tones, flat reads
VW line <bible> <voice> <clips>  # same voice as the reference
VW cast <bible>                  # the cast stays apart
VW review <clips> --out r.wav    # one clip to listen to
```

FAIL and DRIFT are not verdicts until heard, but do not deliver them unheard. What each number means and what it was calibrated on: [references/thresholds.md](references/thresholds.md). Speaker scores measure sameness, never quality; a score cannot prove a voice is good or not stereotyped.

## Step 7: finish

`VW finish <in> <out> --dest film|game|narration|audiobook|web|acx`. An unknown destination is an error: ask. Do not denoise unless `measure` finds noise; denoisers can add their own artifacts: [references/finish.md](references/finish.md). Use `mw.py master` for a final mix when musicwright is present. Audiobook and store rules, including disclosure: `references/rights.md`.

## Output

The route, the bible path, per-clip check lines, what was heard and by whom, and disclosure duties for the destination.

## Rules

- Never state "no AI" or credit a human narrator for a generated voice.
- Prompts move delivery, not identity: fix identity with a reference, not longer direction.
- Samples published with the plugin must be voices with clear rights.

## While working: capture learnings

If the user corrects you, an error repeats, or a workaround turns up, add it to [LEARNINGS.md](LEARNINGS.md). If it proves a rule wrong, fix the rule, log it in [CHANGELOG.md](CHANGELOG.md) and set `contradiction` in `evergreen.json`.

## Maintenance

Evergreen unit, tier `fast`; state in `evergreen.json`. See [MAINTENANCE.md](MAINTENANCE.md), [RESEARCH.md](RESEARCH.md), [TESTS.md](TESTS.md), `evals/`.
