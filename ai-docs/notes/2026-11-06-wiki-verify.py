#!/usr/bin/env python3
"""Runs every example on the wiki against a fresh clone of the released repository, in a scratch folder.
Usage: python 2026-11-06-wiki-verify.py [tag]. Output goes to stdout; save it beside this file.
Audio is synthetic buzz from the repository's fixture code: good for showing output, says nothing of voice quality."""
import json, re, shutil, subprocess, sys, tempfile
from pathlib import Path

REF = sys.argv[1] if len(sys.argv) > 1 else "v0.1.1"
ROOT = Path(tempfile.mkdtemp(prefix="vw-wiki-"))
subprocess.run(["git", "clone", "-q", "--branch", REF, "https://github.com/m4bwav/voicewright", str(ROOT / "plugin")], check=True, capture_output=True)
SKILL = ROOT / "plugin/skills/voicewright"
GAME = ROOT / "game"
(GAME / "voices").mkdir(parents=True)
BS = chr(92)
sys.path.insert(0, str(SKILL / "evals/fixtures"))
import make_fixture as fx  # noqa: E402

fx.voice(GAME / "voices/keeper.wav", 95, [450, 1100, 2400], 5)
fx.voice(GAME / "voices/maid.wav", 210, [800, 1900, 3000], 7)
fx.voice(GAME / "voices/noisy.wav", 140, [600, 1500, 2600], 9, noise=0.05)
keeper = {"id": "keeper", "character": "keeper", "version": 1, "sheet": {"pitch": "low", "pace": "slow bursts"},
          "refs": [{"file": "voices/keeper.wav", "text": "A fixed test line.", "emotion": "neutral", "source": "designed"}],
          "engine": {"name": "voxcpm2", "model": "VoxCPM2", "model_version": "abc123", "seed": 4100},
          "rights": {"kind": "designed", "licence": "see the engine"}}


def term(section, line):
    """Run line as the page shows it; vw.py stands for the released script."""
    print(f"=== {section} ===")
    print("$ " + line)
    real = f"\"{sys.executable}\" \"{SKILL / 'scripts/vw.py'}\"" + line[len("vw.py"):]
    done = subprocess.run(real, shell=True, cwd=GAME, capture_output=True, text=True, encoding="utf-8", stdin=subprocess.DEVNULL)
    out = done.stdout + done.stderr
    for old in (BS + BS, BS):
        out = out.replace(str(ROOT).replace(BS, old), "<scratch>")
    print(out.replace(BS + BS, "/").replace(BS, "/").rstrip())
    print("$ echo $?")
    print(done.returncode)


term("version", "vw.py --version")
term("init", "vw.py init voices.json")
term("init twice", "vw.py init voices.json")
(GAME / "keeper.json").write_text(json.dumps(keeper), encoding="utf-8")
term("add", "vw.py add voices.json keeper.json")
term("add twice", "vw.py add voices.json keeper.json")
term("validate", "vw.py validate voices.json")
term("card", "vw.py card voices.json keeper")
term("card unknown", "vw.py card voices.json nobody")
term("measure", "vw.py measure voices/keeper.wav voices/noisy.wav")
term("cast clips", "vw.py cast --clips voices/keeper.wav voices/maid.wav")
term("line", "vw.py line voices.json keeper voices/keeper.wav voices/maid.wav")
term("library", "vw.py library voices/maid.wav --against voices.json")
term("finish", "vw.py finish voices/keeper.wav keeper_game.wav --dest game")
term("finish unknown", "vw.py finish voices/keeper.wav x.wav --dest radio")
term("review", "vw.py review voices/keeper.wav voices/maid.wav --out review.wav")
data = json.loads((GAME / "voices.json").read_text(encoding="utf-8"))
print("=== stored ref ===")
print(sorted(data["voices"][0]["refs"][0]))
(GAME / "voices/keeper.wav").write_bytes((GAME / "voices/keeper.wav").read_bytes() + b"\0\0")
term("validate after an edit", "vw.py validate voices.json")
shutil.rmtree(ROOT, ignore_errors=True)
