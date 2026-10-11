# Dept 5 Release — Department Workflow

Lead: `team-lead-release` (unified Orchestrator-Lead, `opus/medium`). Both judges RO. Subs: 3.

## Trigger

Master sends EN contract (`MODE=release`, candidate + evidence bundle).

## Flow

1. `sub-sec-judge` (RO): scans keys/RLS/injection/IDOR/traversal. Any critical = BLOCKED. High score never overrides.
2. `sub-rel-judge` (RO): mandatory reqs green, core journey in target env, evidence current, rollback plan present. Local build never counts.
3. `sub-devops` (RW bounded, only if judges CLEAR): preflight check → build → deploy per policy → verify real behavior → record rollback target.

## Aggregate

Lead sends ONE EN report to master: verdicts + deploy evidence + SHA + rollback plan.

## Stops (escalate via master only)

Leak, broken auth, corrupt data, broken journey = full stop, even at high score. Never auto-deploy production without gate.
