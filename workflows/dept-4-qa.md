# Dept 4 QA — Department Workflow

Lead: `team-lead-qa` (unified Orchestrator-Lead, inherits master). Test and repair split. Subs: 5.

## Trigger

Master sends EN contract (`MODE=verify`, changed files, claimed results, original acceptance).

## Flow (lead orchestrates, all reports via lead)

1. `sub-tech-judge` (RO): reruns tests/typecheck/lint, verdict PASS/FAIL with file:line.
2. `sub-product-qa` (RO): traces requirements to behavior, walks real journey.
3. `sub-visual-qa` (RO): real screenshot vs approved design.
4. On FAIL: `sub-diagnosis` (RO) classifies cause + hypotheses → `sub-repair` (RW bounded) minimal fix, never rewrites criteria → rerun verification.
5. Anti-gaming enforced: weakened/deleted tests, changed criteria, self-approval = reject.

## Aggregate

Lead merges verdicts. ONE EN report to master: commands, counts, honest failures, SHA.

## Loops (via master only, never direct)

- Red → master → `team-lead-build` with diagnosis.
- Green → master → `team-lead-release`.
- Same-failure twice = stop, escalate.
