# Continue voicewright

Start in `D:\m4bwa\Claude\Projects\Ai`. This prompt does not change between sessions; state lives in `ai-docs/HANDOFF.md`.

## Load state

Read `voicewright/ai-docs/HANDOFF.md`, `ai-docs/log.md`, `ai-docs/research/2026-11-04-lab.md`, and the original brief at `prompts/2026-11-04-voicewright-plugin-kickoff.md` (success measures and stop points). Then `voicewright/skills/voicewright/SKILL.md`. Use `evergreen-test` for evals, `wikiwright` for the wiki, `comfyui-gen` rules for hosts.

## What waits on Mark

Any open listening page: `python askwright/skills/askwright/scripts/ask.py read voicewright-lab/<page>`; if it is down, `serve --detach`. The items under Waiting on Mark in HANDOFF.md. Installs, paid APIs, real voices, outward posts, directory or registry submissions, hooks outside these repos.

## Order of work

1. Read answers; unblind the picks; act on them. Answers that invalidate a rule change the rule.
2. Work the Owed list in HANDOFF.md in order, skipping what waits on Mark and queueing those on a new askwright page.
3. Bake-off, then pilot, once engines are approved.
4. Wiki, then release a new version when checks pass; pull the main clone and run `claude plugin update`.

## Rules

Worktrees for shared clones. Kill by PID only. A refused permission check goes to Mark; do not route around it. Watch long renders by log progress, with a deadline for no new output. Lab audio stays out of the public repo until Mark clears it. No AI attribution. Merge your own PRs after checks pass; leave one open for the risk cases in the global rules. Thresholds change only with a calibration note.

## Hand over

Update HANDOFF.md and the log, then print this same start command with the folder:

`Execute D:/m4bwa/Claude/Projects/Ai/voicewright/ai-docs/plans/2026-11-04-voicewright-continue-prompt.md`
