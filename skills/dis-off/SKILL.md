---
name: dis-off
description: "Disable AI Sub Agent Team auto-routing on every message. Usage: /ai-agent-team:dis-off"
---

# DIS-OFF — Deactivate auto-routing

Owner effect: messages behave like a normal Claude Code session again; nothing is
routed through the team automatically.

Steps:

1. WRITE file `.ai-agent-team/state` (create it if missing) containing exactly the single word: off
2. REPLY in simple Persian, one line: «تیم زیر-ایجنت غیرفعال شد. پیام‌ها دیگر از ارکستر مستر رد نمی‌شوند. برای روشن کردن: /ai-agent-team:dis-on»
3. If already off: «از قبل غیرفعال بود.»

Rules: keep the file present with value "off" so state is explicit, not missing.
Never touch real secret env files.
