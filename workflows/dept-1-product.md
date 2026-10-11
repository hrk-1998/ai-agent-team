# Dept 1 Product — Department Workflow

Lead: `team-lead-product` (unified Orchestrator-Lead, `sonnet/high`). Subs: 5, all RO, parallel.

## Trigger

Master sends EN TaskContract (`MODE=clarify`, raw idea + material refs).

## Fan-out (lead → subs, EN, parallel)

1. Lead sends intent material to `sub-brain` → returns intent block.
2. Lead sends intent block to `sub-discovery` + `sub-research` in parallel.
3. Lead feeds answers + findings to `sub-requirements` → requirements list.
4. Lead feeds requirements to `sub-productization` → MVP scope (max 3) + NOT list.

## Aggregate (subs → lead → master)

Lead merges into `Project_Brief.md` (Fact/Assumption/Unknown split). Lead sends ONE EN report to master: brief ref + evidence labels + blocker.

## Gate

Gate 1: master renders FA-simple summary to owner. Owner approves goal, user, MVP. No approval = back to lead with owner note.

## Handoff

Approved Brief → master routes to `team-lead-planning`. Subs never contacted again for this phase.
