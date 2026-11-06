import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class Version(unittest.TestCase):
    def test_all_versions_match(self):
        want = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))["version"]
        self.assertEqual(json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))["version"], want)
        vw = (ROOT / "skills/voicewright/scripts/vw.py").read_text(encoding="utf-8")
        self.assertEqual(re.search(r'^VERSION = "(.+)"', vw, re.M).group(1), want)
        skill = (ROOT / "skills/voicewright/SKILL.md").read_text(encoding="utf-8")
        self.assertEqual(re.search(r"^  version: (.+)$", skill, re.M).group(1).strip(), want)


if __name__ == "__main__":
    unittest.main()
