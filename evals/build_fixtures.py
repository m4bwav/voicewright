"""Lay every eval fixture into skills/voicewright/evals/fixtures/<kind>/, where `evergreen.py worth --ab` copies them from.

  VW_EVAL_AUDIO=<clips> python evals/build_fixtures.py

The folders are git-ignored: three hold invented-voice lab clips that are not cleared for publishing.
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "evals"))
from build_cases import LINES  # noqa: E402

FIX = REPO / "skills/voicewright/evals/fixtures"
for kind in ("cast", "noisy", "dwarf", "rebuild", "lines", "ref"):
    d = FIX / kind
    shutil.rmtree(d, ignore_errors=True)
    d.mkdir()
    if kind == "lines":
        (d / "lines.json").write_text(LINES + "\n", encoding="utf-8")
    elif kind == "ref":
        shutil.copy(Path(os.environ["VW_EVAL_AUDIO"]) / "merchant.wav", d / "ref.wav")
    else:
        subprocess.run([sys.executable, str(FIX / "make_fixture.py"), kind], cwd=d, check=True)
    print("built", kind)
