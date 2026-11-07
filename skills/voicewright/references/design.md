# Designing a voice

Prompts move delivery more than identity. Trait prompts are a way to get different candidates, not a proven way to get a better one: in a blind listen (2026-11-04, Qwen3, four briefs, one take each, one listener) traits sounded less stock on the maid and villain, the plain brief on the dwarf and the young woman. So render both and let the ear choose. Short labels can still land on an engine's defaults: in a 2026 study, adjective-only prompts to one hosted engine were heard as 93% white, 86.6% male and 60% US (figures from a search summary; treat as indicative). The sheet records what the chosen voice does acoustically, whichever prompt found it.

## The sheet

Required: `age`, `pitch` (a band in words, then measured Hz once rendered), `resonance` (chest, mouth, nasal, head), `texture` (breathy, creaky, hoarse, smooth), `pace`, `pitch_movement`, `attitude`. Optional: `accent`, `quirks`, `breath`, `rhythm` (a repeated emphasis pattern, separate from `pace`; direct it per line, since a prompt may not hold it), `key_line` (one short natural phrase rendered first when checking this voice), `not` (what to avoid).

## Turning a type into traits

| brief | default trap | ask instead |
|---|---|---|
| gruff old dwarf | constant growl, pantomime | chesty, breath runs out at phrase ends, slow bursts, dry patience |
| sassy maid | squeaky, flirty, a class or race caricature | mid-low, tired and level, precise, bored competence |
| sweet young woman | bright, breathy, smiling | whatever the character is: low, dry, long pauses |
| evil villain | deep, slow, hissing | high, gentle, polite, hesitant |

Contrast against the type where the story allows it. Keep the type word out of trait prompts. A plain-brief candidate may use it, unless the brief itself is a caricature of a class, race or gender: then skip that candidate.

## Accent and identity

An accent is part of who someone is, not a colour. Use one only when the character has a reason, keep it within what the engine does credibly, and have someone from that place hear it if it ships. Labels such as "foreign" and "exotic" give inconsistent and unkind results. Language or dialect labels often do not match what listeners hear (FAccT 2025).

## Widening the range when candidates collapse

When two voices sit close, change several of pitch, texture, pace, rhythm and resonance at once, then prove it with `VW cast` (acting craft, untested on engines). In order of cost: different traits; a different seed (works only on engines with no fixed speaker); a different reference with unusual material you have rights to; speaker-embedding blending where the engine exposes it; voice conversion over a base performance. Blends far from training data hold less steadily. Formant and pitch moves over about 2 semitones start to sound processed: listen.

## Proving it

Blind, level-matched, same line, with a plain-brief candidate in the set. Agent opinion does not count. Measurements only show the voices differ. Do not claim traits beat briefs: so far they tie, 2 to 2.
