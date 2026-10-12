# User Guide / راهنمای استفاده

Bilingual (EN + FA). For a beginner with zero technical knowledge.

---

## What this plugin is

EN: A team of AI specialists inside Claude Code. You type your raw idea in
plain words. The master-orchestrator reads it, understands it, and hands it
to the right office. Offices work in parallel. Nothing is installed
on your computer — no extra app, no dashboard.

FA: یک تیم از متخصصان هوش مصنوعی داخل کلود کد. فقط ایدهٔ خام خود را به
زبان ساده می‌نویسید. ارکستر مستر آن را می‌خواند، می‌فهمد و به اتاق
درست می‌دهد. اتاق‌ها موازی کار می‌کنند. هیچ نرم‌افزار جداگانه‌ای
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
it to RESEARCH OFFICE. If you are continuing an existing project, it reads
Project_Brief.md, Architecture.md and HANDOFF.md first, then routes to the
current office.

FA: فقط بنویسید. مثال: «ربات تلگرام برای کانال خبری می‌خوام». اگر
روشن باشد، ارکستر تشخیص می‌دهد ایدهٔ جدید است و به اتاق تحقیق و کشف
می‌فرستد. اگر پروژهٔ قبلی را ادامه می‌دهید، اول سندهای پروژه را می‌خواند
و بعد به اتاق فعلی می‌فرستد.

## What happens next / چه اتفاقی می‌افتد

EN: RESEARCH OFFICE asks at most 3 plain questions, one at a time, each with 2-4
options to pick from. Then PLANNING OFFICE makes the plan and shows 2-3 design
directions visually. You approve. Then DEVELOPERS OFFICE builds, QUALITY OFFICE tests
independently, SECURITY & RELEASE OFFICE checks security, MEMORY OFFICE keeps memory. You see simple
Persian updates: one result + one next step.

FA: اتاق تحقیق و کشف حداکثر ۳ سؤال ساده می‌پرسد، یکی‌یکی، هر کدام با ۲ تا ۴
گزینه برای انتخاب. بعد اتاق برنامه‌ریزی و نقشه‌کشی نقشه می‌کشد و ۲-۳ نمونهٔ طراحی به
شما نشان می‌دهد. تأیید می‌کنید. بعد اتاق برنامه‌نویسی می‌سازد، اتاق کنترل کیفیت مستقل آزمون
می‌کند، اتاق امنیت و انتشار امنیت را چک می‌کند، اتاق حافظه و دانش حافظه را نگه می‌دارد. شما فقط یک نتیجه
و یک گام بعدی را ساده می‌بینید.

## Commands / دستورات

| Command | What it does |
|---|---|
| `/ai-agent-team:dis-on` | فعال‌سازی ردّ خودکار همهٔ پیام‌ها |
| `/ai-agent-team:dis-off` | خاموش کردن؛ سشن معمولی |
| `/ai-agent-team:team-workflow` | راه‌اندازی دستی تیم برای یک ایده |
| `/ai-agent-team:pro-model [model] [effort]` | تغییر مدل اتاق تحقیق و کشف |
| `/ai-agent-team:map-model ...` | تغییر مدل اتاق برنامه‌ریزی و نقشه‌کشی |
| `/ai-agent-team:eng-model ...` | تغییر مدل اتاق برنامه‌نویسی |
| `/ai-agent-team:qa-model ...` | تغییر مدل اتاق کنترل کیفیت |
| `/ai-agent-team:rel-model ...` | تغییر مدل اتاق امنیت و انتشار |
| `/ai-agent-team:mem-model ...` | تغییر مدل اتاق حافظه و دانش |
| `/ai-agent-team:master-model ...` | تغییر مدل پیش‌فرض اصلی |
| `/ai-agent-team:project-handoff` | ساخت فایل HANDOFF برای ادامهٔ کار |
| `/ai-agent-team:app-preview` | اجرای اپ ساخته‌شده و نمایش در مرورگر |
| `/ai-agent-team:mindmap` | نمودار گرافیکی ساختار تیم |

Model input: whatever `/model` shows you, you can use —
`desktop` or `inherit` (session model: CLAUDE-DESKTOP, CLAUDE-DESKTOP 1M),
`haiku` (CLAUDE-HAIKU-4.5), `sonnet`, `opus`, `fable`, or any full id
(`claude-haiku-4-5-20251001`; anything `claude-*` passes through verbatim).
Efforts: `low`, `medium`, `high`, `xhigh`, `max`.
`default` resets an office to inherit the session model.

## Set a whole office / ست کردن کل اتاق

EN: `/ai-agent-team:eng-model desktop xhigh` — DEVELOPERS OFFICE (lead AND every
sub) now runs on the session model with effort xhigh. Same form works for
every office and every model in your list.

FA: `/ai-agent-team:eng-model desktop xhigh` — از این پس اتاق برنامه‌نویسی
(سرپرست و همهٔ ساب‌ها) روی مدل سشن فعلی با effort ایکس‌های اجرا می‌شود.
همین شکل دستور برای همهٔ اتاق‌ها و همهٔ مدل‌های لیست شما کار می‌کند.

## Default model rule / قانون مدل پیش‌فرض

EN: By default every office uses THE SAME MODEL AS YOUR CURRENT SESSION
(model: inherit in departments.json). If your session runs on Claude Haiku
4.5, the whole team runs on Haiku 4.5. Only if you explicitly assign a
model to a office does that office (lead + all its subs) switch.

FA: به‌طور پیش‌فرض همهٔ اتاق‌ها همان مدل سشن فعلی شما را استفاده
می‌کنند. اگر سشن شما روی کلود هایکوی ۴.۵ باشد، کل تیم روی هایکوی ۴.۵
اجرا می‌شود. فقط اگر خودتان به یک اتاق مدل بدهید، آن اتاق
(به همراه همهٔ ساب‌ایجنت‌هایش) عوض می‌شود.

## App builder: build → run → see it / اپ‌بیلدر: ساخت → اجرا → دیدن

EN: The team is now a full AI app builder. Type your app idea (via
`/ai-agent-team:team-workflow`). PLANNING OFFICE picks a proven template
(Vite/Next/FastAPI), DEVELOPERS OFFICE scaffolds it one-shot and boots the dev server,
QUALITY OFFICE drives the running app in a real headless browser (clicks the core
journey, reads console errors, takes screenshots). When the build is green,
run `/ai-agent-team:app-preview` — the app opens in your browser pane and you
see it running.

FA: تیم الان یک اپ‌بیلدر کامل است. ایدهٔ اپ خود را بنویسید (با
`/ai-agent-team:team-workflow`). اتاق برنامه‌ریزی و نقشه‌کشی یک تمپلیت اثبات‌شده انتخاب می‌کند،
اتاق برنامه‌نویسی آن را یک‌باره می‌سازد و سرور را بالا می‌آورد، اتاق کنترل کیفیت اپِ در حال
اجرا را با مرورگر واقعی تست می‌کند (کلیک مسیر اصلی، خطاهای کنسول، اسکرین‌شات).
وقتی ساخت سبز شد، دستور `/ai-agent-team:app-preview` را بزنید — اپ در پنجرهٔ
مرورگر شما باز می‌شود و آن را در حال اجرا می‌بینید.

## Safety / امنیت

EN: built-in guards block destructive git commands, real secret-file reads
and writes, and out-of-scope edits. The team never commits without
evidence and never deploys without your gate approval.

FA: محافظ‌های داخلی دستورات مخرب گیت، خواندن و نوشتن فایل‌های رمز واقعی
و ویرایش بیرون از محدوده را مسدود می‌کنند. تیم بدون شواهد کامیت نمی‌کند
و بدون تأیید شما دیپلوی نمی‌کند.
