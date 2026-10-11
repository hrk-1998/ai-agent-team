---
name: project-handoff
description: Generate portable 14-field project handoff for resume in any tool or session.
---

# Project Handoff

Invoke team-lead-memory.

1. Read Git status, branch, HEAD, recent commits.
2. Collect verified tests with exact commands + exit codes.
3. Separate verified (VALID) from claims (STALE/INVALID/UNKNOWN).
4. Write HANDOFF.md: identity, task + criteria, changed files, tests, failures, blockers, forbidden actions, next single action.
5. Confirm ready to share. Receiver re-verifies Git independently.
