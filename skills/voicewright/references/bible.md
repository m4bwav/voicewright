# The voice bible

`voices.json`, schema 1, in a project root or `bibles/`. It is the contract between plugins: cinewright and musicwright read this file, and no plugin imports another. It extends cinewright's format, keeping `character`. `VW migrate` upgrades an old file; `VW validate` is the rebuild test.

```json
{"schema": 1, "voices": [{
  "id": "keeper", "character": "keeper", "version": 1,
  "sheet": {"age": "elderly", "pitch": "low", "resonance": "chest", "texture": "slightly breathy", "pace": "slow bursts", "pitch_movement": "narrow", "attitude": "dry, patient"},
  "refs": [{"file": "voices/keeper/neutral.wav", "text": "exact words", "emotion": "neutral", "source": "designed", "sha256": "written by VW add"}],
  "engine": {"name": "qwen3-tts", "model": "Qwen/Qwen3-TTS-12Hz-1.7B-Base", "model_version": "hub commit", "seed": 4100, "settings": {}, "design_prompt": "the traits prompt"},
  "pronunciation": {"Tharsis": "THAR-sis"},
  "rights": {"kind": "designed", "licence": "Apache-2.0 engine", "consent": null, "provenance": "designed from text, no real reference"},
  "used_by": ["project-name"]
}]}
```

- `rights.kind`: `designed`, `real-person` (needs `consent`: who, date, uses, where the signed copy is), `library`, `self`.
- Change a voice: raise `version`, keep old clips. Never edit a reference in place; the hash catches it.
- Keep a user library at a path of their choosing and pass it to `VW library --against`.
- Machines: pin the model revision and record device and dtype; a CPU and a GPU render can differ, so check with `VW line`.
