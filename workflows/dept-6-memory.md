# Dept 6 Memory — Department Workflow

Lead: `team-lead-memory` (unified Orchestrator-Lead, inherits master). Command `/project-handoff`. Subs: 3.

## Triggers

End of any phase, pre-build check, pre-handoff, drift check, explicit `/project-handoff`.

## Flow

1. `sub-state-keeper`: persists single-owner state atomically, invalidates dependent STALE evidence.
2. `sub-jit`: builds minimal context pack for next agent (objective, contract, revision, relevant decisions, files, deps, verified work, claims, failures, tests, risks, forbidden, Git state, next action). No history dump, no secrets.
3. `sub-handoff`: writes 14-field HANDOFF.md (identity, branch/HEAD, worktree, task+criteria, changes+why, verified cmds/results, claims, locked decisions, files+deps, test outcomes, failures+reruns, blockers, forbidden/protected, next single action).

## Aggregate

Lead confirms file + revision. ONE EN report to master.

## Rules

Per-project isolation always. Receiver re-verifies Git independently.
