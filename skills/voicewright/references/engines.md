# Engines

Checked 2026-11-04 from votes, papers and reports, mostly not by ear. Local clone rank updated 2026-11-05 from a blind listen: VoxCPM2 2, Qwen3-TTS 2, Chatterbox 0, one listener, four voices. VoxCPM2 goes first: it had no faults, where Qwen3 had a runaway clipped take, and the same listener kept its version of a ten-line, four-voice scene over Qwen3's (that page showed the agent's guess first, so it was not fully blind). This is a default to try, not a ranking; other rows are still provisional. Full table, sources: repository `ai-docs/research/2026-11-04-engines.md`.

| job | hosted | local, in order to try |
|---|---|---|
| design from text | ElevenLabs Voice Design (try v3 first) | VoxCPM2, Qwen3-TTS, MOSS-VoiceGenerator |
| clone a short clip | Eleven v4 Instant | VoxCPM2, Qwen3-TTS, Chatterbox V3 (always watermarked; CPU only on an RTX 5060 Ti) |
| long narration | Eleven v4 | Qwen3-TTS 1.7B, MOSS-TTS v1.5, VoxCPM2; Kokoro for fast presets |
| acted emotion | Eleven v4 tags | IndexTTS-2.5, Higgs TTS 3; budget many takes, systems under-act |
| dialogue | ElevenLabs Text to Dialogue | per line with frozen voices, then join |
| non-English | Eleven v4 | VoxCPM2, MOSS v1.5, Chatterbox V3 |
| real time | Cartesia Sonic, Eleven v4 Turbo | Kokoro, Pocket TTS |
| conversion | ElevenLabs Voice Changer | RVC (trained); Seed-VC is archived, GPL-3.0 |

Licence traps: OmniVoice weights CC-BY-NC; F5-TTS weights CC-BY-NC; VibeVoice research only; Voxtral and Breeze non-commercial; Fish S2 Pro research only; IndexTTS has revenue and user caps; Higgs needs a credit. Read the licence on the day.

16 GB PC fits: Qwen3, VoxCPM2, Chatterbox, CosyVoice3. Tight: IndexTTS. No: Drama 3. A Mac listing in mlx-audio is not a tested fit.

## Singing

Boundary, decided 2026-11-04: voicewright owns the voice's identity record, including a `singing` note in the bible; musicwright owns generating songs. No singing route here. The evidence for singing engines is the weakest in the survey and has no independent comparison.
