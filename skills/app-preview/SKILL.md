---
name: app-preview
description: "Build the app, boot it, and open it in the session browser pane. Usage: /app-preview (uses the built project; /ai-agent-team:app-preview after install)"
---

# App Preview Skill (Build → Run → Show)

Turns DIT into an AI app builder: after Dept 3 has built (or Dept 2 approved a
plan), this skill RUNS the app and SHOWS it to the owner in the browser pane.

This is the ONLY place the app is shown to the owner: browser panes live in
the main session (master), never in subs.

## Commands

- `/ai-agent-team:app-preview` — run the built app and open it in the pane.
- No project built yet → first run `/ai-agent-team:team-workflow` or answer the
  master's plan gate; this skill needs code on disk to run.

## What to run (detect, never guess)

1. READ the project root: package.json → `npm ci` (when lockfile missing:
   npm install) then `npm run dev` (or the `dev`/`start` script it declares).
   requirements.txt / pyproject.toml → venv python + `uvicorn`/`flask run`/
   the README's run command. No run command found → ask the owner one FA
   question with the closest candidates, do not guess.
2. Verify the env gate already passed (GATE_OK on record). If not, say so in
   FA and stop — the env gate is a blocking prerequisite, not something this
   skill skips.
3. BOOT on a free port (default 3000 node / 8000 python). Poll
   `curl http://localhost:<port>/` until 200 (timeout 30s). One crash →
   restart once. Second crash → RUN_BLOCKED + log tail, stop.
4. SHOW: open the URL in the session's browser pane (preview tools in this
   session, NOT a sub). Desktop viewport first.
5. REPORT Persian simple, at most 5 lines: what is running, the URL, one
   known limitation if any, next step.

## Rules

- Never edits product code. Restarts only from clean state. Never installs
  global packages. Never exposes tokens in logs or the report.
- If the port is taken, increment. Never kill foreign processes.
- Machine edges EN; owner report FA simple. This skill runs in the main
  session under master — it is not a sub.
