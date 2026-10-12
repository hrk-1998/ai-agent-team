# AI Agent Team Plugin (v8, AI App Builder: scaffold + run + browse)

Hierarchical subagent team for Claude Code. Master = your main session.
6 unified office orchestrator-leads. 91 subs. Contracts, gates, evidence.
Owner edge: simple Persian. Machine edges: strict English.
App builder: scaffold from a proven template, boot the app, drive it in a
real browser, show it in your pane.

## Install (auto in every project)

Install from the marketplace (Claude Code 2.1.275+):

```
/plugin install ai-agent-team --marketplace hrk-1998/ai-agent-team
```

First add the marketplace once: `/plugin marketplace add hrk-1998/ai-agent-team`

Manual install (no marketplace):

1. Validate: `claude plugin validate .`
2. Test one session: `claude --plugin-dir .`, then `/ai-agent-team:team-workflow`
3. Install for you, every project: copy this folder to `~/.claude/skills/ai-agent-team/`
   (any folder there with `.claude-plugin/plugin.json` auto-loads every session).
   Then `/reload-plugins` in the session.
4. Install for one repo only: copy to `<project>/.claude/skills/ai-agent-team/` instead.

## Use (commands, prefixed after install)

```text
/ai-agent-team:dis-on
```
then just type your idea in any message:

```text
/ai-agent-team:team-workflow
ایده من: ربات تلگرام برای کانال خبری
```

```text
/ai-agent-team:dis-off
/ai-agent-team:mindmap
```

Build an app and see it running:

```text
/ai-agent-team:team-workflow
ایده من: فروشگاه ساده با سبد خرید
```

then, once the build is green:

```text
/ai-agent-team:app-preview
```

DEVELOPERS OFFICE boots the app, QUALITY OFFICE drives it with a real browser, and this skill
opens the URL in your session's browser pane. Browser display lives only in
the main session — subs verify over CLI, never in a pane.

Full bilingual guide: USAGE.md. Contract schema: contracts/task-contract.md.

```text
/ai-agent-team:pro-model sonnet high
/ai-agent-team:map-model default
/ai-agent-team:eng-model desktop xhigh
/ai-agent-team:project-handoff
```

Per-office model skills: `master-model`, `pro-model`, `map-model`, `eng-model`,
`qa-model`, `rel-model`, `mem-model`. Bare call shows setting.
`[model] [effort]` sets it for the lead AND every sub of that office.
`default` resets to the session model.

Model input: whatever `/model` shows you, you can use —
`desktop` or `inherit` (the session model: CLAUDE-DESKTOP, CLAUDE-DESKTOP 1M),
`haiku` (CLAUDE-HAIKU-4.5), `sonnet`, `opus`, `fable`, or any full id
(`claude-haiku-4-5-20251001`). A `claude-*` id is passed through verbatim,
so models added later still work.

Efforts: `low`, `medium`, `high`, `xhigh`, `max`.

## How it runs (spec notes)

- NOT Agent Teams (experimental, one team/session, no nesting). Subagents + skills + hooks.
- Master = main session via `team-workflow`. Leads/subs = subagent definitions via Task.
- Null-offices inherit the session model at runtime (`model: inherit`).
  A set office writes `{"model": ..., "effort": ...}` to `departments.json`
  and into the lead + all its subs, so the whole office runs on it.
- App builder chain: PLANNING OFFICE `sub-scaffold-picker` chooses a proven template
  (Vite/Next/FastAPI) → DEVELOPERS OFFICE one-shot scaffold via transaction-runner →
  `sub-app-runner` boots the dev server → QUALITY OFFICE `sub-browser-driver` drives
  the running app headless (journey + console errors + screenshots) →
  `/ai-agent-team:app-preview` shows the URL in the owner's browser pane.
- Foreground only. Planning lead read-only until plan approved.
- Guards in `hooks/hooks.json`: no `git add -A`/history rewrite, no real `.env` reads/writes.
- Plugin auto-loads in every project once installed at user scope. No per-project setup.
