# User Guide / راهنمای استفاده

Bilingual (EN + FA). For a beginner with zero technical knowledge.

---

## What this plugin is

EN: A team of AI specialists inside Claude Code. You type your raw idea in
plain words. The master-orchestrator reads it, understands it, and hands it
to the right department. Departments work in parallel. Nothing is installed
on your computer — no extra app, no dashboard.

FA: یک تیم از متخصصان هوش مصنوعی داخل کلود کد. فقط ایدهٔ خام خود را به
زبان ساده می‌نویسید. ارکستر مستر آن را می‌خواند، می‌فهمد و به دپارتمان
درست می‌دهد. دپارتمان‌ها موازی کار می‌کنند. هیچ نرم‌افزار جداگانه‌ای
نیاز نیست.

## Install / نصب

EN: copy the plugin folder (the repo root) to `~/.claude/skills/ai-agent-team/`
(user scope, every project) or to `<project>/.claude/skills/ai-agent-team/`
(one project only). Then run `/reload-plugins`.

FA: پوشهٔ پلاگین (ریشهٔ همین مخزن) را به `~/.claude/skills/ai-agent-team/` (همهٔ
پروژه‌ها) یا `<پروژه>/.claude/skills/ai-agent-team/` (فقط یک پروژه) کپی
کنید. بعد دستور `/reload-plugins` را بزنید.

## Turn auto-routing on/off / روشن و خاموش

EN: `/ai-agent-team:dis-on` makes EVERY message pass through the
orchestrator. `/ai-agent-team:dis-off` returns to a normal session. When
on, the hook reads `.ai-agent-team/state` (value `on` or `off`).

FA: `/ai-agent-team:dis-on` می‌کند هر پیامی که می‌فرستی از ارکستر مستر
رد شود. `/ai-agent-team:dis-off` سشن را به حالت معمولی برمی‌گرداند.
در حالت روشن، هوک فایل `.ai-agent-team/state` را می‌خواند.

## Give your idea / ایده را بدهید

EN: just write it. Example: «I want a Telegram news bot for my channel».
If auto-routing is on, the orchestrator detects it is a NEW idea and sends
it to Dept 1 Product. If you are continuing an existing project, it reads
Project_Brief.md, Architecture.md and HANDOFF.md first, then routes to the
current department.

FA: فقط بنویسید. مثال: «ربات تلگرام برای کانال خبری می‌خوام». اگر
روشن باشد، ارکستر تشخیص می‌دهد ایدهٔ جدید است و به دپارتمان محصول
می‌فرستد. اگر پروژهٔ قبلی را ادامه می‌دهید، اول سندهای پروژه را می‌خواند
و بعد به دپارتمان فعلی می‌فرستد.

## What happens next / چه اتفاقی می‌افتد

EN: Dept 1 asks at most 3 plain questions, one at a time, each with 2-4
options to pick from. Then Dept 2 makes the plan and shows 2-3 design
directions visually. You approve. Then Dept 3 builds, Dept 4 tests
independently, Dept 5 checks security, Dept 6 keeps memory. You see simple
Persian updates: one result + one next step.

FA: دپارتمان ۱ حداکثر ۳ سؤال ساده می‌پرسد، یکی‌یکی، هر کدام با ۲ تا ۴
گزینه برای انتخاب. بعد دپارتمان ۲ نقشه می‌کشد و ۲-۳ نمونهٔ طراحی به
شما نشان می‌دهد. تأیید می‌کنید. بعد دپارتمان ۳ می‌سازد، ۴ مستقل آزمون
می‌کند، ۵ امنیت را چک می‌کند، ۶ حافظه را نگه می‌دارد. شما فقط یک نتیجه
و یک گام بعدی را ساده می‌بینید.

## Commands / دستورات

| Command | What it does |
|---|---|
| `/ai-agent-team:dis-on` | فعال‌سازی ردّ خودکار همهٔ پیام‌ها |
| `/ai-agent-team:dis-off` | خاموش کردن؛ سشن معمولی |
| `/ai-agent-team:team-workflow` | راه‌اندازی دستی تیم برای یک ایده |
| `/ai-agent-team:pro-model [model] [effort]` | تغییر مدل دپارتمان محصول |
| `/ai-agent-team:map-model ...` | تغییر مدل دپارتمان نقشه |
| `/ai-agent-team:eng-model ...` | تغییر مدل دپارتمان ساخت |
| `/ai-agent-team:qa-model ...` | تغییر مدل دپارتمان آزمون |
| `/ai-agent-team:rel-model ...` | تغییر مدل دپارتمان انتشار |
| `/ai-agent-team:mem-model ...` | تغییر مدل دپارتمان حافظه |
| `/ai-agent-team:master-model ...` | تغییر مدل پیش‌فرض اصلی |
| `/ai-agent-team:project-handoff` | ساخت فایل HANDOFF برای ادامهٔ کار |
| `/ai-agent-team:mindmap` | نمودار گرافیکی ساختار تیم |

Model input: whatever `/model` shows you, you can use —
`desktop` or `inherit` (session model: CLAUDE-DESKTOP, CLAUDE-DESKTOP 1M),
`haiku` (CLAUDE-HAIKU-4.5), `sonnet`, `opus`, `fable`, or any full id
(`claude-haiku-4-5-20251001`; anything `claude-*` passes through verbatim).
Efforts: `low`, `medium`, `high`, `xhigh`, `max`.
`default` resets a department to inherit the session model.

## Set a whole department / ست کردن کل دپارتمان

EN: `/ai-agent-team:eng-model desktop xhigh` — Dept 3 Build (lead AND every
sub) now runs on the session model with effort xhigh. Same form works for
every department and every model in your list.

FA: `/ai-agent-team:eng-model desktop xhigh` — از این پس دپارتمان ساخت
(سرپرست و همهٔ ساب‌ها) روی مدل سشن فعلی با effort ایکس‌های اجرا می‌شود.
همین شکل دستور برای همهٔ دپارتمان‌ها و همهٔ مدل‌های لیست شما کار می‌کند.

## Default model rule / قانون مدل پیش‌فرض

EN: By default every department uses THE SAME MODEL AS YOUR CURRENT SESSION
(model: inherit in departments.json). If your session runs on Claude Haiku
4.5, the whole team runs on Haiku 4.5. Only if you explicitly assign a
model to a department does that department (lead + all its subs) switch.

FA: به‌طور پیش‌فرض همهٔ دپارتمان‌ها همان مدل سشن فعلی شما را استفاده
می‌کنند. اگر سشن شما روی کلود هایکوی ۴.۵ باشد، کل تیم روی هایکوی ۴.۵
اجرا می‌شود. فقط اگر خودتان به یک دپارتمان مدل بدهید، آن دپارتمان
(به همراه همهٔ ساب‌ایجنت‌هایش) عوض می‌شود.

## Safety / امنیت

EN: built-in guards block destructive git commands, real secret-file reads
and writes, and out-of-scope edits. The team never commits without
evidence and never deploys without your gate approval.

FA: محافظ‌های داخلی دستورات مخرب گیت، خواندن و نوشتن فایل‌های رمز واقعی
و ویرایش بیرون از محدوده را مسدود می‌کنند. تیم بدون شواهد کامیت نمی‌کند
و بدون تأیید شما دیپلوی نمی‌کند.
