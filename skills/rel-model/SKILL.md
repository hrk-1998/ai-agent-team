---
name: rel-model
description: "Show or set Dept 5 Release model and effort. Usage: /rel-model [model] [effort]"
---

# Rel Model Skill (Dept 5 Release)

Manages model and effort for Dept 5 Release only. All 3 subs (sec-judge, rel-judge, devops) follow automatically (`same-as-lead`).

## Commands

- `/rel-model` — show current Dept 5 setting.
- `/rel-model [model] [effort]` — set Dept 5 model and effort.
- `/rel-model default` — reset Dept 5 to inherit master (`null` in json).

Valid models: `fable`, `sonnet`, `opus`, `haiku`. Valid efforts: `low`, `medium`, `high`.

## Execution Protocol

1. READ `departments.json` key `release` + `agents/team-lead-release.md` frontmatter.
2. No args: PRINT current model, effort, source (custom vs inherit).
3. With args: validate, UPDATE json key `release` + `model:`/`effort:` in `team-lead-release.md`. Never edit subs. REPORT Persian simple: «مدل دپارتمان انتشار روی [مدل] با effort [ایفورت] تنظیم شد. هر ۳ ساب همگام شدند.»
