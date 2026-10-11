---
name: master-model
description: "Show or set the master root default model and effort. Usage: /master-model [model] [effort]"
---

# Master Model Skill (Root Default)

Manages the master root default. Depts with null inherit this.

## Commands

- `/master-model` — show master + full 6-dept matrix (custom vs inherit).
- `/master-model [model] [effort]` — set root default.

Valid models: `fable`, `sonnet`, `opus`, `haiku`. Valid efforts: `low`, `medium`, `high`.

## Execution Protocol

1. READ `departments.json` + `agents/master-orchestrator.md`.
2. No args: PRINT full matrix table (dept, model, effort, custom/inherit).
3. With args: validate, UPDATE `departments.json` master entry + `model:`/`effort:` in `master-orchestrator.md` frontmatter. All null (inherit) depts follow automatically. REPORT Persian simple.
