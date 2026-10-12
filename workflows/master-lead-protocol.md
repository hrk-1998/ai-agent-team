# Master ↔ Lead Protocol — Inter-Orchestrator Workflow

Master: `master-orchestrator` (`fable/high`, RO tools). Leads: 6 unified Orchestrator-Leads. Subs: 26 (never visible to master).

## Master loop (per task)

1. READ state: Brief, Arch, Git status, prior evidence labels.
2. SELECT next eligible task (dep order from planning).
3. WRITE EN TaskContract (20 fields): id, title, mode (clarify/plan/build/verify/release/handoff), project, objective, outcome, verified-state, owner, scope, non-goals, locked, deps, risk/blast-radius, acceptance, verify-cmd, evidence, rollback, commit, stop, report.
4. SEND to exactly ONE lead. Never to subs, never to two leads at once for same source.
5. WAIT for that lead's single EN report: files, exit codes, SHAs, evidence VALID/STALE/INVALID, blocker.
6. On FAIL: send back to SAME lead with diagnosis. On success: advance to next lead in phase order.
7. RECORD event + update state via memory lead. Never skip a gate.

## Model passing (spec: sub-agents frontmatter)

Per current Claude Code spec, a sub without a `model` field falls through to env/main model, NOT to its caller. So `same-as-lead` is enforced by the caller, not by absence:
- Every lead Task call passes `model` + `effort` explicitly (per-call values override definition).
- Subs carry NO model field; optionally add `model: inherit` (resolves to caller model per spec).
- Office null in departments.json = inherit master; lead passes master's values.

## Lead loop (per contract)

1. VALIDATE contract: mode matches office, scope within authority, lease present for writes.
2. FAN OUT to own subs only (EN sub-tasks, parallel where safe). Each sub isolated memory, same-as-lead model.
3. COLLECT sub outputs. AGGREGATE into ONE EN report. Conflicts resolved by lead using canonical owner.
4. SEND single report to master. Never contact other leads, subs, owner.

## Language gateway (master translates)

- Master → Lead, Lead → Master: EN strict, machine-readable. Persian inside = reject at gateway.
- Master → Owner: FA simple (or EN per choice). One result + one next step. No jargon, no file paths, no exit codes.
- Owner → Master: FA free. Master converts to EN contract internally.

## Failure routing (always via master)

- QA red → master → build lead. Security block → master → full stop. Drift → master → planning lead. Never lead-to-lead direct.

## Phase order

1 product → 2 planning → 3 build ⇄ 4 qa (loop via master) → 5 release → 6 memory. Gates: G1 brief, G2 arch+contract, G2.5 foundation lock, release gate.
