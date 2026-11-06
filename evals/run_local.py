"""Run the suite through `claude -p` where `claude plugin eval` cannot grant Bash (native Windows has no sandbox).

  VW_EVAL_AUDIO=<clips> python evals/run_local.py --out <dir> [--case <substring>] [--runs 3] [--model sonnet] [--jobs 4] [--budget 15]

Each run gets a new folder, user settings left out (`--setting-sources project`), and the plugin by `--plugin-dir`;
action cases also get one baseline run without it. Grades on the stream-json trace, the reply and files, as evals.json
names them. Not a sandbox: only run cases you wrote. Needs numpy and onnxruntime for the speaker checks.
"""
import argparse
import concurrent.futures as cf
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "evals"))
from build_cases import LINES  # noqa: E402

FIX = REPO / "skills/voicewright/evals/fixtures/make_fixture.py"
SKILL = r'"skill"\s*:\s*"(?:[\w-]+:)?voicewright"'


def prompt_of(cid):
    t = (REPO / "evals/cases" / cid / "prompt.md").read_text(encoding="utf-8")
    return t.split("---", 2)[2].strip()


def scaffold(kind, cwd):
    if kind == "lines":
        (cwd / "lines.json").write_text(LINES + "\n", encoding="utf-8")
    elif kind == "ref":
        shutil.copy(Path(os.environ["VW_EVAL_AUDIO"]) / "merchant.wav", cwd / "ref.wav")
    elif kind:
        subprocess.run([sys.executable, str(FIX), kind], cwd=cwd, check=True, capture_output=True)


def run_claude(prompt, cwd, plugin, model, turns, timeout):
    # The prompt goes over stdin: on Windows `claude` is a .cmd, and cmd.exe cuts an argument at a newline or parenthesis.
    cmd = [shutil.which("claude"), "-p", "--output-format", "stream-json", "--verbose", "--model", model, "--max-turns", str(turns),
           "--setting-sources", "project", "--allowedTools", "Read,Glob,Grep,Skill,Bash,Write,Edit"]
    if plugin:
        cmd += ["--plugin-dir", str(REPO)]
    try:
        p = subprocess.run(cmd, cwd=cwd, input=prompt, capture_output=True, encoding="utf-8", errors="replace", timeout=timeout)
        out = p.stdout
    except subprocess.TimeoutExpired as e:
        out = (e.stdout or b"").decode("utf-8", "replace") if isinstance(e.stdout, bytes) else (e.stdout or "")
    calls, text, cost = [], "", 0.0
    for line in out.splitlines():
        try:
            m = json.loads(line)
        except ValueError:
            continue
        if m.get("type") == "assistant":
            for b in m["message"].get("content", []):
                if b.get("type") == "tool_use":
                    calls.append((b["name"], json.dumps(b["input"], ensure_ascii=False)))
        elif m.get("type") == "result":
            text, cost = m.get("result") or "", m.get("total_cost_usd") or 0.0
    return calls, text, cost


def check(e, cwd, calls):
    """Evidence in the shape `evergreen.py worth --ab` grades, including `max: 0` on a trace (evergreen 0.18.3 or later)."""
    if "any" in e:
        return any(check(x, cwd, calls) for x in e["any"])
    if e["type"] == "trace":
        hit = sum(n == e["tool"] and bool(re.search(e["input_match"], i, re.I)) for n, i in calls)
        return hit == 0 if e.get("max") == 0 else hit >= 1
    files = [f for f in cwd.glob(e["path"]) if f.is_file()]
    if e.get("absent"):
        return not files
    return any(re.search(e["match"], f.read_text(encoding="utf-8", errors="replace"), re.I | re.M) for f in files)


def grade(case, cwd, calls, text):
    res = []
    kind = case["kind"]
    fired = any(n == "Skill" and re.search(SKILL, i) for n, i in calls)
    if kind != "action":
        decoy = bool(case.get("decoy")) or kind == "decoy"
        return [("skill stayed quiet" if decoy else "skill fired", fired != decoy)]
    for e in case.get("evidence", {}).get("all", []):
        res.append((json.dumps(e, ensure_ascii=False), check(e, cwd, calls)))
    for x in case.get("expectations", []):
        pat = x.split(":", 1)[1].strip()
        res.append(("reply " + pat, bool(re.search(pat, text, re.I | re.S))))
    return res


def one(case, arm, n, a, lock, state):
    with lock:
        if state["cost"] >= a.budget:
            return None
    cwd = Path(tempfile.mkdtemp(prefix="vw-eval-"))
    try:
        scaffold(case.get("fixture"), cwd)
        action = case["kind"] == "action"
        calls, text, cost = run_claude(prompt_of(case["id"]), cwd, arm == "with", a.model, 25 if action else 8, 600 if action else 240)
        g = grade(case, cwd, calls, text)
    except Exception as e:  # one broken run must not lose the suite
        calls, text, cost, g = [], repr(e), 0.0, [("run error", False)]
    finally:
        shutil.rmtree(cwd, ignore_errors=True)
    r = {"case": case["id"], "kind": case["kind"], "decoy": bool(case.get("decoy")), "arm": arm, "run": n, "pass": all(p for _, p in g), "graders": g,
         "cost": cost, "calls": [[c, i[:4000]] for c, i in calls], "reply": text[:1500]}
    with lock:
        state["cost"] += cost
        Path(a.out).mkdir(parents=True, exist_ok=True)
        with open(Path(a.out) / "runs.jsonl", "a", encoding="utf-8") as h:  # survives a crash later in the suite
            h.write(json.dumps(r, ensure_ascii=False) + "\n")
        print("%-18s %-4s %d %s $%.2f %s" % (case["id"], arm, n, "PASS" if r["pass"] else "FAIL", cost, ascii([x for x, p in g if not p])), flush=True)
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--case", default="")
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--model", default="sonnet")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--budget", type=float, default=15.0)
    a = ap.parse_args()
    cases = [c for c in json.loads((REPO / "skills/voicewright/evals/evals.json").read_text(encoding="utf-8"))["evals"] if a.case in c["id"]]
    jobs = [(c, "with", n) for c in cases for n in range(1, a.runs + 1)] + [(c, "base", 1) for c in cases if c["kind"] == "action"]
    lock, state = threading.Lock(), {"cost": 0.0}
    with cf.ThreadPoolExecutor(a.jobs) as ex:
        rows = [r for r in ex.map(lambda j: one(j[0], j[1], j[2], a, lock, state), jobs) if r]
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "results.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False), encoding="utf-8")
    print("DONE runs %d of %d, cost $%.2f" % (len(rows), len(jobs), state["cost"]), flush=True)
    for c in cases:
        w = [r for r in rows if r["case"] == c["id"] and r["arm"] == "with"]
        b = [r for r in rows if r["case"] == c["id"] and r["arm"] == "base"]
        print("%-18s with %d/%d  baseline %s" % (c["id"], sum(r["pass"] for r in w), len(w), "%d/%d" % (sum(r["pass"] for r in b), len(b)) if b else "-"), flush=True)


if __name__ == "__main__":
    main()
