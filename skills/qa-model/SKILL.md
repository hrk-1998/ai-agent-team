---
name: qa-model
description: "Show or set Dept 4 QA model and effort. Usage: /qa-model [model] [effort]"
---

# QA Model Skill (Dept 4 QA)

Manages model and effort for Dept 4 QA only. All 5 subs (diagnosis, repair, tech-judge, product-qa, visual-qa) follow automatically (`same-as-lead`).

## Commands

- `/qa-model` — show current Dept 4 setting.
- `/qa-model [model] [effort]` — set Dept 4 model and effort.
- `/qa-model default` — reset Dept 4 to inherit master (`null` in json).

Valid models: `fable`, `sonnet`, `opus`, `haiku`. Valid efforts: `low`, `medium`, `high`.

## Execution Protocol

1. READ `departments.json` key `qa` + `agents/team-lead-qa.md` frontmatter.
2. No args: PRINT current model, effort, source (custom vs inherit).
3. With args: validate, UPDATE json key `qa` + `model:`/`effort:` in `team-lead-qa.md`. Never edit subs. REPORT Persian simple: «مدل دپارتمان آزمون روی [مدل] با effort [ایفورت] تنظیم شد. هر ۵ ساب همگام شدند.»
