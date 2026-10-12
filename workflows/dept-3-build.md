# Dept 3 Build — Department Workflow

Lead: `team-lead-build` (unified Orchestrator-Lead, inherits session model). Mode: Build Mode, scoped only. Subs: 12, gate + RW bounded + runner.

## Trigger

Master sends ONE EN TaskContract per batch (`MODE=build`, scope files, acceptance, verify cmd, lease, rollback, stop, optional `scaffold-choice` from Dept 2).

## Step 0 — Environment Gate (blocking, must pass first)

`sub-env-gate` runs FIRST. It detects the stack from real files (package.json → node; requirements.txt / pyproject.toml → python), verifies runtime vs pinned deps, prepares the env (npm ci / venv + pip), ensures template from the example file exists, validates with build or py_compile plus dry-run, and reports GATE_OK with the verified runtime or GATE_BLOCKED with reason. Lead broadcasts the verified runtime: all sibling subs must use it only.

If GATE_BLOCKED, workflow stops, no build subs start, blocker returned to master.

## Lease check (lead, after gate)

Lead verifies write-sets disjoint across subs in this batch. Conflict goes to serialize or split batch. Snapshot HEAD noted.

## Step 0.5 — Scaffold (one-shot, only when TaskContract carries `scaffold-choice`)

`sub-transaction-runner` applies the whole approved template in ONE batch: create-project from the chosen template (Vite/Next/FastAPI), then install deps via the verified runtime. Write-set is relaxed for THIS batch only (still snapshotted first via `sub-snapshot-manager`); the 1-2 file rule activates only after scaffold completes. Scaffold report: files created, exit codes, template source.

## Fan-out (lead to subs, EN, parallel where disjoint, inside verified runtime)

- `sub-frontend`: UI files. `sub-backend`: API and services. `sub-data`: schema (needs migration approval). `sub-integration`: adapters (keys server-side only).
- Each sub: inspect, snapshot, minimal change, run verify inside verified runtime, report (files, exit codes, SHA).

## Step 3 — Run the app (last build step, before commit handoff)

`sub-app-runner` boots the dev server on a free port (default 3000 node / 8000 python), health-checks until 200 (30s timeout), restarts once on crash, and reports RUNNING + URL + port + PID + log tail — or RUN_BLOCKED with reason. Lead attaches the run URL to the master report.

## Aggregate

Lead collects sub reports, runs merged-state check, small commits (never add -A). ONE EN report to master: files, exit codes, SHAs, evidence labels, blocker, run URL.

## Reject paths

No contract = reject. No GATE_OK = reject. Outside write-set = abort. Missing migration approval = hold. RUN_BLOCKED = build not done; fix then rerun.

## Handoff

Code plus SHAs plus run URL goes to master routes to `team-lead-qa`.
