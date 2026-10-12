---
name: master-model
description: "Show or set the master root default model and effort. Usage: /master-model [model] [effort]"
---

# Master Model Skill (Root Default)

Manages the COMMAND OFFICE root default. Offices with null inherit this.
`master-orchestrator` is forced to `model: inherit` (the session model); only
its `effort` changes here. Null-office leads + subs inherit the session model at
runtime.

## Commands

- `/master-model` — show master + full 6-office matrix (custom vs inherit).
- `/master-model [model] [effort]` — set root default.

## Model input (whatever `/model` shows you, you can use)

Claude Code itself only accepts a fixed set of model identifiers, so this skill
normalizes what you type. Use ANY of these:

| You type | What is written (resolves to) |
|---|---|
| `desktop` | `inherit` — the model of THIS session (CLAUDE-DESKTOP, CLAUDE-DESKTOP 1M) |
| `inherit` | `inherit` — same as `desktop` |
| `haiku` | `haiku` — CLAUDE-HAIKU-4.5 |
| `sonnet` | `sonnet` |
| `opus` | `opus` |
| `fable` | `fable` |
| `claude-haiku-4-5-20251001` (any full id) | passed through verbatim |

Anything matching `claude-*` is accepted as-is, so a model added to Claude Code
after this skill was written still works. An unrecognized value is rejected
with the valid list.

Valid efforts: `low`, `medium`, `high`, `xhigh`, `max`.

## Execution Protocol

1. READ `departments.json` + `agents/master-orchestrator.md`.
2. No args: PRINT full matrix table (office, model, effort, custom/inherit).
3. With args: normalize the model, validate the effort, then UPDATE
   - `departments.json` master entry → `{"model": "<resolved>", "effort": "<effort>"}`
   - `effort:` in `agents/master-orchestrator.md` (model stays `inherit`)
4. REPORT Persian simple.
