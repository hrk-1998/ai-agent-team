---
name: e2e-workflow
description: Run sequential MVP then version loop until the last approved version is fully verified. Stops only on owner question or final green. Invoke with /ai-agent-team:e2e-workflow.
---

# E2E Workflow (sequential version loop)

Master owns this loop. Do not skip versions.

## Entry

Owner runs `/ai-agent-team:e2e-workflow` after approving the roadmap of versions (MVP, v1, v2, etc).

## Loop per version

1. Plan the version (team-lead-planning) then gate.
2. Build the version (team-lead-build, env-gate first) then tests in order.
3. Harden (team-lead-qa, team-lead-release): judges, evidence, rollback plan.
4. Demo FA-simple to owner, collect feedback, repair bounded, re-verify.

## Continue rule

If a version has fixes: repair loop until green. If clean and versions remain: go to next version. Repeat.

## Stop rule

Stop only when last version is green with all tests passed and no owner question pending. Or stop early on a Master Brief or PRD question truly needing owner answer.

## Notes

Keep tests sequential per version. Never mark tests passed without running them inside the verified venv with exit codes.
