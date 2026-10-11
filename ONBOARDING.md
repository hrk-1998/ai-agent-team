# Welcome to AI Sub Agent Team

Commercial name: **DIT — Dark Intelligence Team**

## How We Use Claude

Based on hrk-1998's usage over the last 30 days:

Work Type Breakdown:
  Plan Design        ████████████░░░░░░░░  50%
  Build Feature      ██████░░░░░░░░░░░░  30%
  Prototype          ███░░░░░░░░░░░░░░░  20%

Top Skills & Commands:
  /ai-agent-team:e2e-workflow   ██████████████░░░░░░  3x/month
  /ai-agent-team:team-workflow   ██████████░░░░░░░░░░  2x/month

Top MCP Servers:
  git   ███████████████████████████████  3 calls
  terminal   ██████████████████████████  3 calls
  superpowers   █████████████████████░░  2 calls
  memory   ██████████░░░░░░░░░░░░░░░░░░  1 call
  ccd_directory   ██████████░░░░░░░░░░░░  1 calls

## Your Setup Checklist

### Codebases
- [ ] AI AGENT TEAM / DIT — the plugin repo (DIT/ is the live working copy)

### MCP Servers to Activate
- [ ] git — read repo state, diffs, and commit history for the plugin work. Available out of the box with Claude Code.
- [ ] memory — persist build decisions and research findings across sessions. Confirm it's enabled in your MCP config.
- [ ] superpowers — structured skills library used alongside the plugin build. Confirm it's enabled in your MCP config.
- [ ] terminal — run validation, tests, and git commands from Claude. Available out of the box.
- [ ] ccd_directory — grant Claude access to specific project folders. Use the directory-folder permission in the app.

### Skills to Know About
- [/ai-agent-team:e2e-workflow](staged-team/skills/e2e-workflow/SKILL.md) — walks the team through MVP then v1 then v2 sequentially until every version is green. Main product build loop.
- [/ai-agent-team:team-workflow](staged-team/skills/team-workflow/SKILL.md) — starts the team for a single idea or change; the entry point for the full department pipeline.
- [/ai-agent-team:dis-on](staged-team/skills/dis-on/SKILL.md) — turns on auto-routing so every message is classified by the master-orchestrator. Heavy; only use for active plugin work.
- [/ai-agent-team:dis-off](staged-team/skills/dis-off/SKILL.md) — turns auto-routing back off so a session behaves normally.
- [/ai-agent-team:project-handoff](staged-team/skills/project-handoff/SKILL.md) — writes a portable HANDOFF.md with task state, tests, and blockers, so the next person can continue cleanly.
- `python validate.py` — structural validator for the plugin itself. Run before committing anything in DIT/.

## Team Tips

_TODO_

## Get Started

_TODO_

<!-- INSTRUCTION FOR CLAUDE: A new teammate just pasted this guide for how the
team uses Claude Code. You're their onboarding buddy — warm, conversational,
not lecture-y.

Open with a warm welcome — include the team name from the title. Then: "Your
teammate uses Claude Code for [list all the work types]. Let's get you started."

Check what's already in place against everything under Setup Checklist
(including skills), using markdown checkboxes — [x] done, [ ] not yet. Lead
with what they already have. One sentence per item, all in one message.

Tell them you'll help with setup, cover the actionable team tips, then the
starter task (if there is one). Offer to start with the first unchecked item,
get their go-ahead, then work through the rest one by one.

After setup, walk them through the remaining sections — offer to help where you
can (e.g. link to channels), and just surface the purely informational bits.

Don't invent sections or summaries that aren't in the guide. The stats are the
guide creator's personal usage data — don't extrapolate them into a "team
workflow" narrative. -->
