# Changelog: voicewright

## 0.1.10 (unreleased)

From Linklater, Freeing the Natural Voice (2006): split `say` by thought with breath points at thought changes; mark turns (but, if, though) and say what shifts there; tactic and why-these-words in direction; named take faults (sing-song, head monotone, strained, thin, flat-rich bass, nasal, generalised, held pitch) with retry moves; a same-dynamics run in a scene is a fault; five background facts before traits. Because: the book's text checklist and fault patterns give direction and listening words. Body-training book, unverified on engines: guidance only, no script check or threshold.

## 0.1.9 (released 2026-11-17)

design.md gains two optional sheet axes, `energy` (gentle or sharp) and `colour` (light to dark), and a line to keep a cloned voice's quirks and pitch unless asked. Because: Sadolin, Complete Vocal Technique (2012), speech and sound-colour chapters (PDF p. 153-159). Book rule, unverified on engines; no anatomy or exercise content carried.

## 0.1.8 (released 2026-11-17)

`voxcpm2.py` passes the reference transcript (`ref_text`) as `prompt_text` when a clone job has one. Because: in a 2026-11-17 GPU test speaker similarity rose 0.734 to 0.822 at RTF about 1.2 instead of 1.03. New optional engine `engines/voxmel_run.py` (VoxMel-0.6B, 4 steps) runs an existing VoxMel install named by `VOXMEL_HOME`; nothing vendored. It measured similarity 0.894, RTF about 1.0, 3.7 GB VRAM, but speaks only English and Chinese and its training data is CC BY-NC, so personal projects only. VoxCPM2 stays the default until the takes are heard.

## 0.1.7 (released 2026-11-14)

From Tannen, Conversational Style: an optional style block on the sheet (`turn_gap`, `overlap`, `silence`, `irony`) kept apart from timbre, with a warning that style is not accent; alike voices also separate by gap, rate, pitch range and loudness; dialogue gaps start from `turn_gap`, back-channels lie under the speaker, cooperative overlap and takeover are joined differently; three more retry moves. Because: the book shows timing and overlap carry character as much as voice quality. Book rules, unverified on engines.

## 0.1.6 (released 2026-11-07)

From Sueur, Sound Analysis and Synthesis with R: `measure` reports `formants_hz` (LPC, no pass mark), and thresholds.md says spectral numbers compare only at the same settings and why aligned scores need the same words.

## 0.1.5 (released 2026-11-06)

Sfxwright, when installed: Hand sound effects to sfxwright when present and read its sounds.json; this plugin's own steps stay as the fallback.

## 0.1.4 (released 2026-11-06)

From two books, Alburger and Tan: direction by event, listener and thought; writing `say` for the ear; timing in the join; retry notes; text normalising; a first test by fault; `rhythm` and `key_line` on the sheet; published scores explained. All untested on current engines and marked so. No threshold changed.

## 0.1.3 (released 2026-11-06)

Batch runners for IndexTTS-2.5 and Ming-3.0 tiny. Five-engine listen: VoxCPM2 stays first for cloning; neither new engine won a voice. Windows and RTX 50 install notes for both.

## 0.1.2 (released 2026-11-06)

`vw.py --version` printed 0.1.0 in 0.1.1; fixed, with a test that keeps it level with the manifests. Thresholds cite VIPBench: the 41% clone figure sits beside 31% for real pairs. Engines warn off Hume Octave and EVI. Eval cases now in the shape `worth --ab` grades, with `evals/build_fixtures.py`; worth verdict KEEP.

## 0.1.1 (released 2026-11-05)

VoxCPM2 confirmed first for cloning after a pilot scene listen. Denoise note records one test on clean takes: no audible difference. SKILL.md names all three batch runners. Eval grader accepts a bible in any folder.

## 0.1.0 (released 2026-11-05)

Evals found and fixed: a soundalike trigger miss, type words in prompt files, no route for a stock preset. VoxCPM2 first for cloning, provisional. Python 3.9 fix.

Blind listen: traits and plain briefs tied 2 to 2, so the design step now renders both and no longer claims traits win. A 0.350 line was heard as the same person, so a low score on a generated line means listen. `line` warns on pitch creep and on words per second. Pilot scene cleared as a sample.

## First build (2026-11-04)

First version: workflow skill, voice bible schema 1 with migration from cinewright, `vw.py` checks, Qwen3-TTS runner. From the survey in `ai-docs/research/` and the `ai-voice` beat.
