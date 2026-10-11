---
name: pro-model
description: "Show or set Dept 1 Product model and effort. Usage: /pro-model [model] [effort]"
---

# Pro Model Skill (Dept 1 Product)

Manages model and effort for Dept 1 Product only. All 5 subs follow automatically (`same-as-lead`).

## Commands

- `/pro-model` — show current Dept 1 setting.
- `/pro-model [model] [effort]` — set Dept 1 model and effort.
- `/pro-model default` — reset Dept 1 to inherit master (`null` in json).

Valid models: `fable`, `sonnet`, `opus`, `haiku`. Valid efforts: `low`, `medium`, `high`.

## Execution Protocol

1. READ `departments.json` key `product` + `agents/team-lead-product.md` frontmatter.
2. No args: PRINT current model, effort, source (custom vs inherit).
3. With args: validate, UPDATE json key `product` + `model:`/`effort:` in `team-lead-product.md`. Never edit subs. REPORT Persian simple: «مدل دپارتمان محصول روی [مدل] با effort [ایفورت] تنظیم شد. هر ۵ ساب همگام شدند.»
