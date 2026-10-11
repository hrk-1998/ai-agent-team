# DIT Session Handoff (copy this file's "Bootstrap" section into a new session)

Project: AI SUB AGENT TEAM — commercial name **DIT = Dark Intelligence Team (تیم هوش سیاه)**
Root (source of truth): `D:\AI AGENT TEAM\DIT`   ← work here
`D:\AI AGENT TEAM\staged-team` is the stale v7 copy — do not edit it.

## State (2026-10-11)

- git `main`, clean tree, 128 files tracked, NO remote configured (push impossible until `git remote add origin ...`)
- Commits: `8ca4c92` feat: DIT v1.0 (95 agents, 13 skills, 9 workflows) → `a5086d6` chore: drop ONBOARDING.md
- `python validate.py` → PASS (95 agents / 13 skills / 9 workflows / 88 dept subs)
- Git identity pre-set: hrk-1998 <hamidredforce@atomicmail.io>

## What exists

- agents/ 95 files: `master-orchestrator` + 6 `team-lead-{product,planning,build,qa,release,memory}` + 88 `sub-*`
- workflows/ 9: master-lead-protocol, dept-1..6, sub-lifecycle, test-flow-build
- skills/ 13: team-workflow, e2e-workflow, dis-on, dis-off, mindmap, project-handoff, {master,pro,map,eng,qa,rel,mem}-model
- contracts/task-contract.md — 3-layer TaskContract: L1 Master→Lead (20 fields), L2 Planning→atomic task (20), L3 Lead→RW sub (9: id,title,mode,owner,scope,acceptance,verify-cmd,rollback,stop,lease)
- hooks/hooks.json + hooks/router.sh — UserPromptSubmit auto-routing (on/off via dis-on/dis-off writing `.ai-agent-team/state`)
- departments.json — all keys null = every dept inherits the session model; per-dept override via `/ai-agent-team:<x>-model <model> <effort>`
- USAGE.md — bilingual FA/EN user guide

## Rules that bite (project's own hooks enforce them)

- PreToolUse blocks: `git add -A`/`git add .`, `rm -rf`, `rebase`, `reset --hard`, any real `.env` read/write (only `.env.example` with empty keys). Use explicit `git add <path>`.
- Hierarchy: master → leads → own subs only. Subs never talk cross-dept or to owner.
- Machine edges strict English; Master→Owner simple Persian.
- Model ladder: master root default; lead `model: inherit`; subs carry no model at all (validator enforces).

## Open decisions (user has not picked)

1. staged-team/ stale — delete or sync?
2. No git remote — set one and push?
3. Plugin release path (packaging/marketplace entry) — the known gap from the audit.

## Bootstrap for the new session (paste this)

> پروژه DIT در D:\AI AGENT TEAM\DIT ادامه ده. قبل از هر کار SESSION.md را بخوان.
> وضعیت را با `git log --oneline` و `python validate.py` چک کن. منتظر دستور من بمان.

(That one paragraph is all a fresh session needs — everything else is on disk and re-readable.)
