# GitHub wiki notes

Wiki https://github.com/m4bwav/voicewright/wiki, describing 0.1.2. Working copy: `Ai/voicewright.wiki`, branch master, plain push.

Pages: Home, Getting-Started, Commands, The-Voice-Bible, Reading-The-Numbers, Errors-And-Edge-Cases, FAQ, Versions-And-Upgrading, Development, _Sidebar, _Footer.

Verification: `2026-11-06-wiki-verify.py <tag>` clones the tag and runs each command on synthetic buzz; output beside it. The plugin is on no registry, so the tag stands for the published package.

Not tested: the two install lines, `setup`, `migrate`, `finish --short`, `measure --json`, the messages for missing numpy, model and ffmpeg (read from source).

Facts the README lacks: exit codes; `cast` warnings exit 0; `add` refuses a known id; `validate` catches an edited reference by hash.

Inaccuracies found: 1. `vw.py --version` printed 0.1.0 at 0.1.1, fixed in 0.1.2. 2. CODEMAP named only the Qwen3 runner, fixed. 3. README says it includes a batch runner for Qwen3-TTS; there are three. Left for the next release.

Update: bump the tag, rerun, `wikiwright.py diffout` against the saved output, then change `_Footer.md` and the Versions-And-Upgrading table, then `check`, `outputs`, `snippets`, `live`.
