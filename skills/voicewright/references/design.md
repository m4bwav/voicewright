# Designing a voice

Prompts move delivery more than identity, and short type labels land on the engine's defaults. In a 2026 study, adjective-only prompts to one hosted engine were heard as 93% white, 86.6% male and 60% US (figures from a search summary; treat as indicative). So the sheet says what the voice does acoustically.

## The sheet

Required: `age`, `pitch` (a band in words, then measured Hz once rendered), `resonance` (chest, mouth, nasal, head), `texture` (breathy, creaky, hoarse, smooth), `pace`, `pitch_movement`, `attitude`. Optional: `accent`, `quirks`, `breath`, `not` (what to avoid).

## Turning a type into traits

| brief | default trap | ask instead |
|---|---|---|
| gruff old dwarf | constant growl, pantomime | chesty, breath runs out at phrase ends, slow bursts, dry patience |
| sassy maid | squeaky, flirty, a class or race caricature | mid-low, tired and level, precise, bored competence |
| sweet young woman | bright, breathy, smiling | whatever the character is: low, dry, long pauses |
| evil villain | deep, slow, hissing | high, gentle, polite, hesitant |

Contrast against the type where the story allows it. Leave the word for the type out of the prompt.

## Accent and identity

An accent is part of who someone is, not a colour. Use one only when the character has a reason, keep it within what the engine does credibly, and have someone from that place hear it if it ships. Labels such as "foreign" and "exotic" give inconsistent and unkind results. Language or dialect labels often do not match what listeners hear (FAccT 2025).

## Widening the range when candidates collapse

In order of cost: different traits; a different seed (works only on engines with no fixed speaker); a different reference with unusual material you have rights to; speaker-embedding blending where the engine exposes it; voice conversion over a base performance. Blends far from training data hold less steadily. Formant and pitch moves over about 2 semitones start to sound processed: listen.

## Proving it

Blind, level-matched, same line, against a label-prompt baseline. Agent opinion does not count. Measurements only show the voices differ.
