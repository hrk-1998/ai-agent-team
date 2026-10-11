# Dept 2 Planning — Department Workflow

Lead: `team-lead-planning` (unified Orchestrator-Lead, inherits master). Mode: Plan Mode (RO, except keeper). Subs: 6.

## Trigger

Master sends EN TaskContract (`MODE=plan`, approved Brief).

## Fan-out (lead → subs, EN, parallel)

1. `sub-arch` + `sub-ux` + `sub-visual-scout` in parallel → arch spec, ux spec, visual direction.
2. `sub-planner` turns scope into atomic tasks (1-2 files each, full 20-field contract each per contracts/task-contract.md).
3. `sub-deps` orders tasks: critical path, parallel-safe batches, blockers.
4. `sub-foundation-keeper` writes/syncs 5 files (CLAUDE/AGENTS/README/.gitignore/.env.example) from approved sources + live scan. Guess = TBD. Never reads .env.

## Aggregate

Lead merges into `Architecture.md` + ordered TaskContracts. ONE EN report to master.

## Gates

Gate 2: owner approves plan (FA simple). Gate 2.5: foundation files locked. Build stays blocked while deps open.

## Handoff

Approved contracts → master routes batches to `team-lead-build` in dep order.
