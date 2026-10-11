# Dept 3 Build — Department Workflow

Lead: `team-lead-build` (unified Orchestrator-Lead, `sonnet/medium`). Mode: Build Mode, scoped only. Subs: 11, gate + RW bounded.

## Trigger

Master sends ONE EN TaskContract per batch (`MODE=build`, scope files, acceptance, verify cmd, lease, rollback, stop).

## Step 0 — Environment Gate (blocking, must pass first)

`sub-env-gate` runs FIRST. It verifies Python vs pinned libs compatibility, creates isolated venv, installs deps via venv python -m pip (or uv), ensures template from the example file exists, validates with py_compile plus dry-run import, and reports GATE_OK with verified interpreter path or GATE_BLOCKED with reason. Lead broadcasts the verified path: all sibling subs must use that venv only.

If GATE_BLOCKED, workflow stops, no build subs start, blocker returned to master.

## Lease check (lead, after gate)

Lead verifies write-sets disjoint across subs in this batch. Conflict goes to serialize or split batch. Snapshot HEAD noted.

## Fan-out (lead to subs, EN, parallel where disjoint, inside verified venv)

- `sub-frontend`: UI files. `sub-backend`: API and services. `sub-data`: schema (needs migration approval). `sub-integration`: adapters (keys server-side only).
- Each sub: inspect, snapshot, minimal change, run verify inside venv, report (files, exit codes, SHA).

## Aggregate

Lead collects sub reports, runs merged-state check, small commits (never add -A). ONE EN report to master: files, exit codes, SHAs, evidence labels, blocker.

## Reject paths

No contract = reject. No GATE_OK = reject. Outside write-set = abort. Missing migration approval = hold.

## Handoff

Code plus SHAs goes to master routes to `team-lead-qa`.
