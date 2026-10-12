---
name: team-workflow
description: Run the AI Agent Team pipeline from raw idea to verified release with contracts, leases, gates, and evidence.
---

# Team Workflow

Master orchestrator runs this in main session.

1. Clarify (RESEARCH OFFICE): Brief with Fact/Assumption/Unknown. Gate 1 owner approval, FA simple.
2. Plan (PLANNING OFFICE): Architecture + TaskContract + deps. Foundation keeper writes 5 files. Gate 2 + 2.5.
3. Build (DEVELOPERS OFFICE): scoped Build Mode, lease, snapshot, small commits.
4. QA (QUALITY OFFICE): diagnosis RO, repair bounded, judges RO, visual QA real screenshot, browser-driver verdict when a run URL exists.
5. Release (SECURITY & RELEASE OFFICE): sec + release judges RO. Critical override. Rollback plan.
6. Handoff (MEMORY OFFICE): HANDOFF.md 14 fields.

Machine edges EN. Owner edge FA simple. Subs same-as-lead model. No gate skipped.
Naming rule: in every owner-visible line (reports, task lists, progress), offices appear ONLY as RESEARCH OFFICE / PLANNING OFFICE / DEVELOPERS OFFICE / QUALITY OFFICE / SECURITY & RELEASE OFFICE / MEMORY OFFICE (اتاق تحقیق و کشف / اتاق برنامه‌ریزی و نقشه‌کشی / اتاق برنامه‌نویسی / اتاق کنترل کیفیت / اتاق امنیت و انتشار / اتاق حافظه و دانش). Never "Dept N", never bare `team-lead-*` ids.
Owner questions: ONE at a time, strict order, 2-4 options each plus free-text fallback. Wait for answer before next.
