# AI Agent Team Plugin (v7, auto-routing + session-model default + contract schema)

Hierarchical subagent team for Claude Code. Master = your main session.
6 unified dept orchestrator-leads. 86 subs. Contracts, gates, evidence.
Owner edge: simple Persian. Machine edges: strict English.

## Install (auto in every project)

1. Validate: `claude plugin validate ./staged-team`
2. Test one session: `claude --plugin-dir ./staged-team`, then `/ai-agent-team:team-workflow`
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

Full bilingual guide: USAGE.md. Contract schema: contracts/task-contract.md.

```text
/ai-agent-team:pro-model sonnet high
/ai-agent-team:map-model default
/ai-agent-team:eng-model haiku low
/ai-agent-team:project-handoff
```

Per-dept model skills: `master-model`, `pro-model`, `map-model`, `eng-model`,
`qa-model`, `rel-model`, `mem-model`. Bare call shows setting.
`[model] [effort]` sets it. `default` resets to inherit master.
Models: `fable|sonnet|opus|haiku`. Efforts: `low|medium|high`.

## How it runs (spec notes)

- NOT Agent Teams (experimental, one team/session, no nesting). Subagents + skills + hooks.
- Master = main session via `team-workflow`. Leads/subs = subagent definitions via Task.
- Null-depts inherit caller model at runtime (`model: inherit`).
- Foreground only. Planning lead read-only until plan approved.
- Guards in `hooks/hooks.json`: no `git add -A`/history rewrite, no real `.env` reads/writes.
- Plugin auto-loads in every project once installed at user scope. No per-project setup.
