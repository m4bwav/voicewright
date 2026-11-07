"""Offline tests on synthetic audio. Identity checks run only where the speaker model is installed."""
import array
import contextlib
import io
import json
import math
import random
import sys
import tempfile
import unittest
import wave
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "skills" / "voicewright" / "scripts"))
import vw  # noqa: E402

SR = 24000


def write(path, samples, sr=SR):
    a = array.array("h", [max(-32768, min(32767, int(s))) for s in samples])
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(a.tobytes())


def tone(sec, hz=150.0, amp=8000.0):
    return [amp * math.sin(2 * math.pi * hz * i / SR) for i in range(int(sec * SR))]


def silence(sec):
    return [0.0] * int(sec * SR)


def run(*argv):
    b = io.StringIO()
    with contextlib.redirect_stdout(b):
        try:
            code = vw.main(list(argv))
        except SystemExit as e:
            code = e.code
    return code, b.getvalue()


class LineWarnings(unittest.TestCase):
    def test_runaway_from_the_lab(self):
        self.assertEqual(vw.line_warnings(11.6, 9.5, 12), ["PITCH", "SLOW 1.3 w/s"])

    def test_normal_line_and_missing_data(self):
        self.assertEqual(vw.line_warnings(2.0, 4.0, 10), [])
        self.assertEqual(vw.line_warnings(None, 4.0, 0), [])

    def test_rush(self):
        self.assertEqual(vw.line_warnings(-5.0, 1.0, 6), ["PITCH", "FAST 6.0 w/s"])


class Level(unittest.TestCase):
    def m(self, samples):
        return vw.measure_level(array.array("h", [max(-32768, min(32767, int(s))) for s in samples]), SR)

    def test_clean_passes(self):
        m = self.m(silence(0.2) + tone(1) + silence(0.2))
        self.assertEqual(vw.judge(m)[0], [])
        self.assertLess(m["noise_floor_db"], -90)

    def test_clipping_fails(self):
        e, _ = vw.judge(self.m(tone(1, amp=60000)))
        self.assertTrue(any("clipping" in x for x in e))

    def test_noise_fails(self):
        r = random.Random(1)
        s = [x + r.gauss(0, 1500) for x in silence(0.5) + tone(1) + silence(0.5)]
        e, w = vw.judge(self.m(s))
        self.assertTrue(any("noise floor" in x for x in e + w))

    def test_level_jump_and_tail(self):
        s = tone(1, amp=20000) + silence(0.4) + tone(1, amp=4000) + silence(1.0)
        _, w = vw.judge(self.m(s))
        self.assertTrue(any("level jump" in x for x in w))
        self.assertTrue(any("tail" in x for x in w))


class Bible(unittest.TestCase):
    def setUp(self):
        self.t = tempfile.TemporaryDirectory()
        self.d = Path(self.t.name)
        write(self.d / "a.wav", tone(1))
        self.voice = {"id": "a", "sheet": {"pitch": "low"}, "refs": [{"file": "a.wav", "text": "words"}],
                      "engine": {"name": "e", "model": "m", "model_version": "1", "seed": 1},
                      "rights": {"kind": "designed", "licence": "x"}}

    def tearDown(self):
        self.t.cleanup()

    def add(self, v):
        (self.d / "v.json").write_text(json.dumps(v), encoding="utf-8")
        return run("add", str(self.d), str(self.d / "v.json"))

    def test_add_hashes_and_validates(self):
        run("init", str(self.d))
        self.assertEqual(self.add(self.voice)[0], 0)
        self.assertEqual(run("validate", str(self.d))[0], 0)

    def test_changed_reference_fails(self):
        run("init", str(self.d))
        self.add(self.voice)
        write(self.d / "a.wav", tone(1, hz=200))
        code, out = run("validate", str(self.d))
        self.assertEqual(code, 1)
        self.assertIn("changed", out)

    def test_real_person_needs_consent(self):
        run("init", str(self.d))
        self.voice["rights"] = {"kind": "real-person", "licence": "x"}
        self.assertEqual(self.add(self.voice)[0], 1)

    def test_missing_engine_cannot_rebuild(self):
        run("init", str(self.d))
        self.voice["engine"] = {"name": "e"}
        self.assertEqual(self.add(self.voice)[0], 1)

    def test_migrates_cinewright(self):
        old = {"voices": [{"character": "a", "sheet": {"age": "x"}, "refs": [{"file": "a.wav", "text": "w", "emotion": "neutral", "source": "take"}],
                           "engine": {"name": "e", "model": "m"}, "rights": "designed"}]}
        (self.d / "voices.json").write_text(json.dumps(old), encoding="utf-8")
        run("migrate", str(self.d))
        d = json.loads((self.d / "voices.json").read_text(encoding="utf-8"))
        v = d["voices"][0]
        self.assertEqual((d["schema"], v["id"], v["character"], v["rights"]["kind"]), (1, "a", "a", "designed"))
        self.assertIn("sha256", v["refs"][0])


class Finish(unittest.TestCase):
    def test_unknown_destination_refused(self):
        self.assertEqual(run("finish", "x.wav", "y.wav", "--dest", "moon")[0], 2)


@unittest.skipUnless(vw.need_numpy(), "numpy missing")
class Spectrum(unittest.TestCase):
    def test_pitch(self):
        a = array.array("h", [int(x) for x in tone(2, hz=150)])
        self.assertAlmostEqual(vw.measure_spectrum(a, SR)["f0_median_hz"], 150, delta=5)

    def test_formants_found_on_a_synthetic_vowel_at_two_rates(self):
        for sr in (24000, 44100):
            samples = [0.0] * sr
            for k in range(0, sr, sr // 120):
                samples[k] = 1.0
            for fc, bw in ((700, 80), (1200, 90), (2600, 120)):   # Klatt-style cascade of resonators
                r = math.exp(-math.pi * bw / sr)
                a1, a2 = 2 * r * math.cos(2 * math.pi * fc / sr), -r * r
                y1 = y2 = 0.0
                for i, v in enumerate(samples):
                    y = v + a1 * y1 + a2 * y2
                    samples[i], y2, y1 = y, y1, y
            peak = max(abs(v) for v in samples)
            a = array.array("h", (int(v / peak * 20000) for v in samples))
            got = vw.measure_spectrum(a, sr)["formants_hz"]
            for g, want in zip(got, (700, 1200, 2600)):
                self.assertAlmostEqual(g, want, delta=want * 0.1)


if __name__ == "__main__":
    unittest.main()
