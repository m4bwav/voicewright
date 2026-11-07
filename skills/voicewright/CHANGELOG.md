# Changelog: voicewright

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
