---
name: rel-model
description: "Show or set Dept 5 Release model and effort. Usage: /rel-model [model] [effort]"
---

# Rel Model Skill (Dept 5 Release)

Manages model and effort for Dept 5 Release only: `team-lead-release` AND all
its subs run on the same model + effort.

## Commands

- `/rel-model` — show current Dept 5 setting.
- `/rel-model [model] [effort]` — set Dept 5 model and effort.
- `/rel-model default` — reset Dept 5 to the session model.

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

1. READ `departments.json` key `release` + `agents/team-lead-release.md` frontmatter.
2. No args: PRINT current model, effort, source (custom vs inherit).
3. With args: normalize the model, validate the effort, then UPDATE
   - json key `release` → `{"model": "<resolved>", "effort": "<effort>"}`
   - `model:` and `effort:` in `agents/team-lead-release.md`
   - `effort:` in **every** `agents/sub-*.md` of this dept (the Agent tool
     cannot pass effort per call, so the subs must carry it).
4. `default`: json key `release` → `null`; delete the `model:` line and the
   `effort:` line from the lead and from every sub of this dept.
5. REPORT Persian simple:
   «مدل دپارتمان انتشار روی [مدل] با effort [ایفورت] تنظیم شد. سرپرست و همهٔ ساب‌ها همگام شدند.»
