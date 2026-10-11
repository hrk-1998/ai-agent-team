---
name: mem-model
description: "Show or set Dept 6 Memory model and effort. Usage: /mem-model [model] [effort]"
---

# Mem Model Skill (Dept 6 Memory)

Manages model and effort for Dept 6 Memory only. All 3 subs (state-keeper, jit, handoff) follow automatically (`same-as-lead`).

## Commands

- `/mem-model` — show current Dept 6 setting.
- `/mem-model [model] [effort]` — set Dept 6 model and effort.
- `/mem-model default` — reset Dept 6 to inherit master (`null` in json).

Valid models: `fable`, `sonnet`, `opus`, `haiku`. Valid efforts: `low`, `medium`, `high`.

## Execution Protocol

1. READ `departments.json` key `memory` + `agents/team-lead-memory.md` frontmatter.
2. No args: PRINT current model, effort, source (custom vs inherit).
3. With args: validate, UPDATE json key `memory` + `model:`/`effort:` in `team-lead-memory.md`. Never edit subs. REPORT Persian simple: «مدل دپارتمان حافظه روی [مدل] با effort [ایفورت] تنظیم شد. هر ۳ ساب همگام شدند.»
