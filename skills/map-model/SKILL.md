---
name: map-model
description: "Show or set Dept 2 Planning model and effort. Usage: /map-model [model] [effort]"
---

# Map Model Skill (Dept 2 Planning)

Manages model and effort for Dept 2 Planning only. All 6 subs (planner, deps, ux, arch, visual-scout, foundation-keeper) follow automatically (`same-as-lead`).

## Commands

- `/map-model` — show current Dept 2 setting.
- `/map-model [model] [effort]` — set Dept 2 model and effort.
- `/map-model default` — reset Dept 2 to inherit master (`null` in json).

Valid models: `fable`, `sonnet`, `opus`, `haiku`. Valid efforts: `low`, `medium`, `high`.

## Execution Protocol

1. READ `departments.json` key `planning` + `agents/team-lead-planning.md` frontmatter.
2. No args: PRINT current model, effort, source (custom vs inherit).
3. With args: validate, UPDATE json key `planning` + `model:`/`effort:` in `team-lead-planning.md`. Never edit subs. REPORT Persian simple: «مدل دپارتمان نقشه روی [مدل] با effort [ایفورت] تنظیم شد. هر ۶ ساب همگام شدند.»
