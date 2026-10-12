# Dept 4 QA — Department Workflow

Lead: `team-lead-qa` (unified Orchestrator-Lead, inherits master). Test and repair split. Subs: 19 (judges + reality + browsing + diagnosis + repair + evidence + guards).

## Trigger

Master sends EN contract (`MODE=verify`, changed files, claimed results, original acceptance, optional run URL from Dept 3).

## Flow (lead orchestrates, all reports via lead)

1. `sub-tech-judge` (RO): reruns tests/typecheck/lint, verdict PASS/FAIL with file:line.
2. `sub-product-qa` (RO): traces requirements to behavior, walks real journey.
3. `sub-visual-qa` (RO): real screenshot vs approved design.
4. `sub-browser-driver` (RO verdict): when a run URL arrives from Dept 3, drives the RUNNING app in a real headless browser over CLI — navigates the core journey, clicks, reads console errors, screenshots desktop + mobile. Verdict BROWSER_PASS or BROWSER_FAIL. Skipped when no run URL (report notes built-only verification).
5. On FAIL: `sub-diagnosis` (RO) classifies cause + hypotheses → `sub-repair` (RW bounded) minimal fix, never rewrites criteria → rerun verification.

BROWSER_FAIL returns to master like any FAIL: master routes diagnosis + the browser evidence back to build, NOT to QA directly.

## Aggregate

Lead merges verdicts. ONE EN report to master: commands, counts, honest failures, SHA.

## Loops (via master only, never direct)

- Red → master → `team-lead-build` with diagnosis.
- Green → master → `team-lead-release`.
- Same-failure twice = stop, escalate.
