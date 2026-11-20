"""Engine runners: job handling that needs no GPU or model."""
import importlib.util
import os
import unittest
from pathlib import Path

ENG = Path(__file__).resolve().parent.parent / "skills" / "voicewright" / "scripts" / "engines"


def load(name):
    spec = importlib.util.spec_from_file_location(name, ENG / (name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class VoxCPM2Build(unittest.TestCase):
    def setUp(self):
        self.m = load("voxcpm2")

    def test_clone_with_transcript_passes_prompt_text(self):
        text, kw = self.m.build({"mode": "clone", "text": "Hi.", "ref": "r.wav", "ref_text": " The ref line. "})
        self.assertEqual(text, "Hi.")
        self.assertEqual(kw["prompt_wav_path"], "r.wav")
        self.assertEqual(kw["prompt_text"], "The ref line.")
        self.assertNotIn("reference_wav_path", kw)

    def test_clone_without_transcript_keeps_reference_only(self):
        for job in ({"mode": "clone", "text": "Hi.", "ref": "r.wav"}, {"mode": "clone", "text": "Hi.", "ref": "r.wav", "ref_text": "  "}):
            _, kw = self.m.build(job)
            self.assertEqual(kw["reference_wav_path"], "r.wav")
            self.assertNotIn("prompt_text", kw)
            self.assertNotIn("prompt_wav_path", kw)

    def test_design_ignores_transcript(self):
        text, kw = self.m.build({"mode": "design", "text": "Hi.", "instruct": "old man", "ref_text": "x"})
        self.assertEqual(text, "(old man)Hi.")
        self.assertNotIn("prompt_text", kw)


class VoxMelJobs(unittest.TestCase):
    def setUp(self):
        self.m = load("voxmel_run")

    def test_check_needs_transcript_and_clone(self):
        self.assertEqual(self.m.check({"out": "a.wav", "text": "t", "ref": "r.wav", "ref_text": "x"}), [])
        self.assertTrue(any("ref_text" in e for e in self.m.check({"out": "a.wav", "text": "t", "ref": "r.wav"})))
        self.assertTrue(any("clones only" in e for e in self.m.check({"out": "a", "text": "t", "ref": "r", "ref_text": "x", "mode": "design"})))

    def test_paths_from_env_and_job(self):
        old = dict(os.environ)
        try:
            os.environ.pop("VOXMEL_WEIGHTS", None)
            os.environ["VOXMEL_HOME"] = "/opt/voxmel"
            home, weights = self.m.paths()
            self.assertEqual(weights, Path("/opt/voxmel") / "weights")
            home, weights = self.m.paths({"voxmel_home": "/x", "voxmel_weights": "/w"})
            self.assertEqual((home, weights), (Path("/x"), Path("/w")))
            del os.environ["VOXMEL_HOME"]
            with self.assertRaises(SystemExit):
                self.m.paths()
        finally:
            os.environ.clear()
            os.environ.update(old)

    def test_no_vendored_code(self):
        self.assertFalse((ENG / "voxcore").exists())

    def test_default_steps_eight(self):
        self.assertEqual(self.m.STEPS, 8)


if __name__ == "__main__":
    unittest.main()
