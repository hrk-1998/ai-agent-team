---
name: dis-on
description: "Enable AI Sub Agent Team auto-routing on every message. Usage: /ai-agent-team:dis-on"
---

# DIS-ON — Activate auto-routing

Owner effect: from the next message on, every message you send passes through the
master-orchestrator, which classifies it and routes it to the right office.

Steps:

1. CREATE directory `.ai-agent-team` in the current project if it does not exist.
2. WRITE file `.ai-agent-team/state` containing exactly the single word: on
3. REPLY in simple Persian, one line: «تیم زیر-ایجنت فعال شد. از این پیام به بعد هر پیامی که می‌فرستی از ارکستر مستر رد می‌شود. برای خاموش کردن: /ai-agent-team:dis-off»
4. If already on: «از قبل فعال بود.»

Rules: never write anything else into the state file. Never touch real secret env
files; only the empty-key template is ever written. Project scope only; a user-scope
fallback is ~/.ai-agent-team/state.
