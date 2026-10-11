---
name: eng-model
description: "Show or set Dept 3 Build model and effort. Usage: /eng-model [model] [effort]"
---

# Eng Model Skill (Dept 3 Build)

Manages model and effort for Dept 3 Build only. All 4 subs (frontend, backend, data, integration) follow automatically (`same-as-lead`).

## Commands

- `/eng-model` — show current Dept 3 setting.
- `/eng-model [model] [effort]` — set Dept 3 model and effort.
- `/eng-model default` — reset Dept 3 to inherit master (`null` in json).

Valid models: `fable`, `sonnet`, `opus`, `haiku`. Valid efforts: `low`, `medium`, `high`.

## Execution Protocol

1. READ `departments.json` key `build` + `agents/team-lead-build.md` frontmatter.
2. No args: PRINT current model, effort, source (custom vs inherit).
3. With args: validate, UPDATE json key `build` + `model:`/`effort:` in `team-lead-build.md`. Never edit subs. REPORT Persian simple: «مدل دپارتمان ساخت روی [مدل] با effort [ایفورت] تنظیم شد. هر ۴ ساب همگام شدند.»
