---
name: eng-model
description: "Show or set DEVELOPERS OFFICE model and effort. Usage: /eng-model [model] [effort]"
---

# Eng Model Skill (DEVELOPERS OFFICE)

Manages model and effort for DEVELOPERS OFFICE only: `team-lead-build` AND all its
subs (env-gate, frontend, backend, data, integration, snapshot, recovery, git,
transaction, scope-guard, commit-gate) run on the same model + effort.

## Commands

- `/eng-model` — show current DEVELOPERS OFFICE setting.
- `/eng-model [model] [effort]` — set DEVELOPERS OFFICE model and effort.
- `/eng-model default` — reset DEVELOPERS OFFICE to the session model.

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

1. READ `departments.json` key `build` + `agents/team-lead-build.md` frontmatter.
2. No args: PRINT current model, effort, source (custom vs inherit).
3. With args: normalize the model, validate the effort, then UPDATE
   - json key `build` → `{"model": "<resolved>", "effort": "<effort>"}`
   - `model:` and `effort:` in `agents/team-lead-build.md`
   - `effort:` in **every** `agents/sub-*.md` of this office (the Agent tool
     cannot pass effort per call, so the subs must carry it).
4. `default`: json key `build` → `null`; delete the `model:` line and the
   `effort:` line from the lead and from every sub of this office.
5. REPORT Persian simple:
   «مدل اتاق برنامه‌نویسی روی [مدل] با effort [ایفورت] تنظیم شد. سرپرست و هر ۱۱ ساب همگام شدند.»
