# TaskContract Schema (v1) — Where Contracts Live

Rule: a contract is a written order. No contract = reject. Outside scope = abort.
Three layers, not one. Never ask a sub to build a full 20-field contract.

## Layer 1 — Master Contract (Master → Office Lead): FULL 20 fields

Sent once per office dispatch. Defines the whole office job.

| # | Field | Required | Meaning |
|---|-------|----------|---------|
| 1 | id | yes | unique task id (T-001) |
| 2 | title | yes | short title |
| 3 | mode | yes | clarify / plan / build / verify / release / handoff |
| 4 | project | yes | project name |
| 5 | objective | yes | WHY (goal, not task list) |
| 6 | outcome | yes | concrete expected output |
| 7 | verified-state | yes | what is already green (evidence) |
| 8 | owner | yes | office lead name |
| 9 | scope | yes | allowed files/areas |
| 10 | non-goals | yes | what must NOT be touched |
| 11 | locked | yes | contract immutable after master locks it |
| 12 | deps | yes | blocking task ids |
| 13 | risk/blast-radius | yes | what breaks if this fails |
| 14 | acceptance | yes | pass/fail criteria |
| 15 | verify-cmd | yes | exact command proving acceptance |
| 16 | evidence | yes | labels only: VALID / STALE / INVALID / UNKNOWN |
| 17 | rollback | yes | how to undo |
| 18 | commit | yes | allowed commit scope |
| 19 | stop | yes | stop condition (default: same failure twice) |
| 20 | report | yes | required shape of the EN report back to master |

Plus (from audit P-10): `model-rationale` — one line naming the cheapest sufficient model and why.

## Layer 2 — Planning Contract (Planning Lead → atomic task): SAME 20 fields

produced by sub-planner, one per atomic task (1-2 files each).
NOTE: sub-planner.md says "21 fields" — that is a doc error. Correct count is 20.

## Layer 3 — Scoped Contract (Build Lead → RW sub): 9 fields only

| Field | From |
|-------|------|
| id, title | master contract |
| mode | always "build" |
| owner | the RW sub itself |
| scope | this sub's write-set only |
| acceptance | copied from master contract |
| verify-cmd | copied |
| rollback | copied |
| stop | copied |
| lease | write-lease proving the write-set is disjoint and approved |

RW subs (frontend, backend, data, integration, repair, devops) receive Layer 3 only.

## Who validates, who builds

- BUILD: master (Layer 1), planning lead + sub-planner (Layer 2), build lead (Layer 3).
- VALIDATE only (read, never write contracts): sub-scope-guard, sub-commit-gate,
  sub-tech-judge, sub-sec-judge, sub-rel-judge. They check the contract, not create it.
- RO subs (QA/release/memory) receive the contract as INPUT, never author one.

## Global rules

1. `verify-cmd` is mandatory. A contract without a runnable proof is invalid.
2. `non-goals` is mandatory. Silence here means scope creep.
3. `locked` is set by master only; subs never edit a locked contract.
4. Repair sub NEVER rewrites `acceptance` (bounded repair principle).
5. Every contract travels EN only. Owner sees FA-simple summary, never the contract.
6. Write Leases: state/* → dept-6:state-keeper, evidence/* → dept-4:evidence-store,
   decisions/* → dept-1:decision-registry, dashboard/* → dept-6:dashboard-view.
   One writer per concern; hooks block violators.
