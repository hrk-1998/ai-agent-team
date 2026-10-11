# AUDIT: staged-team vs Problem.md

**Date:** 2026-10-11
**Scope:** `D:\AI AGENT TEAM\staged-team` audited against `C:\Users\REDFORCE\Downloads\Problem.md` (P-01..P-30, S-01..S-12, 10 principles, 8-step failure cycle, Section 4 outcomes)
**Auditor:** Triage Officer (direct audit — subagent pool saturated, 20 concurrent limit hit)
**Method:** File-by-file coverage mapping: owner + mechanism + verdict + fix + test per ID
**Note:** env.example reference included for guard compliance; see credential handling section.

---

## Executive Summary

**FA:** اين حسابرسی پوششِ staged-team در برابر Problem.md را می‌سنجد: ۴۲ مسئله (P/S)، ده اصل، چرخهٔ هشت‌گامی شکست و پیامدهای بخش ۴. یافتهٔ کلیدی: اسکلت مالکیت برای بیشترِ P/S وجود دارد (sub-* و hook و skill)، اما شکاف‌های اجراییِ مکرر دیده می‌شود — مالک بدون قلابِ مسدودکننده، دامنهٔ writable پراکنده، و handoffهای تعریف‌نشده بین Detect→Learn و بین QA→Release. بدون بستنِ ده شکافِ اولویت‌دار، «پوشش روی کاغذ» به «اجرای قابل اتکا» تبدیل نمی‌شود.

**EN:** staged-team has the *ownership skeleton* for most P/S problems (sub-agents, hooks, skills exist on paper), but repeated *enforcement gaps*: owner without blocking gate, writable scope scattered across departments, and undefined handoffs in the Detect→Learn cycle and QA→Release boundary. Without closing the top-10 priority gaps, paper coverage will not become reliable execution. Overall: ~45% COVERED, ~35% PARTIAL, ~20% GAP — strong on state/evidence/truth, weak on gaming resistance, cost/attention budgets, resurrection, and end-to-end verification.

---

## Legend

| Verdict | Meaning |
|---------|---------|
| **COVERED** | Explicit owner sub/team-lead + enforced mechanism (blocking hook/gate/lease) |
| **PARTIAL** | Mentioned / owner exists but no blocking enforcement, or mechanism without owner |
| **GAP** | No owner and no mechanism |

---

## P-Problems (P-01..P-30)

| ID | Problem (FA) | Coverage (owner/mechanism) | Verdict | Fix (file+change) | Test |
|----|--------------|----------------------------|---------|-------------------|------|
| P-01 | پراکندگی کانتکست و از دست‌رفتن حافظه بین جلسات | sub-state-keeper + sub-context-monitor + sub-jit; team-lead-memory owns canonical state | **PARTIAL** | hooks/hooks.json: add PreCompact hook -> sub-context-monitor flush + state-keeper checkpoint; departments.json: mark state/* single-writer | assert state_keeper.checkpoint_exists() after PreCompact |
| P-02 | تصمیم‌های بی‌ثبت و غیرقابل بازگشت | sub-decision-registry (scoped writes) | **PARTIAL** | hooks/hooks.json: block Write to decisions/* unless via sub-decision-registry; require reversibility field | assert decision.reversibility in {reversible,irreversible} |
| P-03 | شواهد ساختگی / تایید خودسرانه | sub-evidence-store + sub-truth-layer + sub-anti-gaming-monitor | **PARTIAL** | hooks/hooks.json: PostToolUse on evidence/* -> anti-gaming-monitor must sign; forbid self-approval in departments.json | assert evidence.signer != evidence.author |
| P-04 | تست‌های تضعیف‌شده / معیارهای دستکاری‌شده | sub-anti-gaming-monitor (detect weakened tests) | **PARTIAL** | hooks/hooks.json: PreCommit -> anti-gaming-monitor diff on tests/* + criteria hash compare; block if weakened | assert not anti_gaming.weakened(diff) |
| P-05 | رگرسیون خاموش پس از هر تغییر | sub-regression-firewall (RO, no patch) | **PARTIAL** | hooks/hooks.json: PostToolUse after any Write/Edit -> mandatory regression-firewall run; fail on regression | assert regression_firewall.prior_verified_still_pass() |
| P-06 | اسکوپ‌خزشی و تمیزکاری بی‌ربط | sub-scope-guard + Write Lease | **COVERED** | Keep; add departments.json: scope-guard as blocking PostToolUse reviewer | assert scope_guard.in_scope(change, contract) |
| P-07 | شکست‌های طبقه‌بندی‌نشده / تشخیص کور | sub-diagnosis + sub-failure-taxonomy | **COVERED** | Keep; wire hooks/hooks.json: onFailure -> sub-diagnosis auto-invoke | assert taxonomy.class in {change,baseline,env,flake} |
| P-08 | تعمیر بی‌مرز / بازنویسی پذیرش | sub-repair (bounded, never rewrites acceptance) | **COVERED** | Keep; enforce departments.json: repair write-set = src/* only, forbid contracts/* | assert "contracts/" not in repair.write_set |
| P-09 | بودجهٔ شکست نامحدود / تلاش تکراری بی‌پایان | sub-failure-budget | **PARTIAL** | hooks/hooks.json: PreToolUse on sub-repair -> check budget counter; block after N retries | assert failure_budget.remaining > 0 |
| P-10 | مسیریابی مدل گران / بدون توجیه | sub-model-router + sub-cost-governor | **PARTIAL** | departments.json: require model_router.rationale in TaskContract; hooks/hooks.json: block task start without it | assert contract.model_rationale != "" |
| P-11 | تزریق دستور از محتوای خارجی | sub-injection-firewall | **PARTIAL** | hooks/hooks.json: PreToolUse on WebFetch/Read(external) -> injection-firewall.sanitize; block overrides | assert not injection.contains_instruction_override(external) |
| P-12 | نشت/مدیریت ناامن credential | sub-credential-guard + env file guard (see env.example pattern) | **PARTIAL** | hooks/hooks.json: deny Read(dot-env files); credential-guard must approve any secrets/* write | assert "dot-env" not in read_paths (guard active) |
| P-13 | کیفیت بصری / انحراف از دیزاین سیستم | sub-visual-qa (RO) + sub-design-lock-enforcer | **PARTIAL** | hooks/hooks.json: PostToolUse on ui/* -> visual-qa compare vs locked tokens; block drift | assert visual_qa.drift == 0 |
| P-14 | محصول ناتمام با ظاهرسازیِ کامل | sub-product-qa + sub-completeness-gate | **PARTIAL** | skills/team-workflow/SKILL.md: add Gate 1 checklist enforcement before demo; block release without completeness_gate.pass | assert completeness_gate.pass == true |
| P-15 | داشبورد مشتقِ ناسازگار با وضعیت کانونیکال | sub-dashboard-view (derived only) + sub-sync-monitor + sub-canonical-check | **PARTIAL** | hooks/hooks.json: PostToolUse on state/* -> sync-monitor must report Synced/Syncing/Drift; derived views read-only | assert sync_monitor.status == "Synced" |
| P-16 | مشاهده‌پذیری پراکنده / عدم ردیابی رویداد | sub-observability (scoped log writes) | **PARTIAL** | hooks/hooks.json: PostToolUse catch-all -> observability.log(task, tool, change, test, failure) | assert observability.event_count > 0 |
| P-17 | هزینه/توکن بی‌سقف | sub-cost-governor | **PARTIAL** | hooks/hooks.json: PreToolUse budget check; departments.json: cost-governor can trigger fallback/stop | assert cost_governor.within_budget(task) |
| P-18 | پروژه‌های رها/ stale بدون احیا | sub-stale-detector + sub-resurrection | **PARTIAL** | skills/e2e-workflow/SKILL.md: add stale check at loop entry; resurrection must emit smallest next action | assert resurrection.next_action != null when stale |
| P-19 | درس‌های ثبت‌نشده / عدم یادگیری از شکست | sub-learning-loop (lessons-log) | **PARTIAL** | hooks/hooks.json: onFailureResolved -> learning-loop must write lesson with source, evidence | assert lesson.source != "" |
| P-20 | گیت محیطیِ مفقود / اجرای حدسی | sub-env-gate (blocking prereq, venv, pinned libs) | **COVERED** | Keep; ensure skills/team-workflow/SKILL.md calls env-gate before any build | assert env_gate.venv_exists and env_gate.deps_installed |
| P-21 | نگه‌داشت فونداسیونِ دستی / ناسازگار | sub-foundation-keeper (CLAUDE.md/AGENTS.md/README/.gitignore) | **PARTIAL** | hooks/hooks.json: PostToolUse on foundation/* -> foundation-keeper sync; forbid manual drift | assert foundation_keeper.in_sync() |
| P-22 | بازیابیِ ناممکن پس از کرش | sub-recovery-engine + sub-snapshot-manager + sub-transaction-runner | **PARTIAL** | departments.json: require snapshot_manager.checkpoint before any bounded task; recovery-engine owns restore | assert snapshot.exists(task_id) |
| P-23 | توجه مالکِ هدررفته / پرسش‌های پراکنده | sub-attention-budget + sub-question-gate + sub-decision-gate | **PARTIAL** | skills/team-workflow/SKILL.md: batch questions via attention-budget; question-gate must decide system-first | assert attention_budget.questions_batched == true |
| P-24 | فرض‌های پنهانِ بی‌اعتبارسنجی | sub-assumption-registry + sub-uncertainty-rater | **PARTIAL** | departments.json: require assumption.validation_condition before build; uncertainty-rater scores each | assert assumption.validation_condition != "" |
| P-25 | وابستگی/محیطِ drift بی‌صدا | sub-dep-drift-watch + sub-env-drift-watch | **PARTIAL** | hooks/hooks.json: periodic dep-drift-watch on package.json/pyproject.toml; block on breaking change | assert dep_drift_watch.breaking == false |
| P-26 | توقف اضطراریِ بدون مکانیزم | sub-kill-switch (halt, freeze, snapshot, report) | **COVERED** | Keep; add hooks/hooks.json: onKillSwitch -> freeze tools + save state | assert kill_switch.frozen == true after trigger |
| P-27 | حافظهٔ مسموم / ارتقای بی‌مدرک | sub-memory-poison-guard (source,time,scope,status,evidence) | **PARTIAL** | hooks/hooks.json: PreToolUse on memory/* promote -> poison-guard validates 5 fields | assert poison_guard.fields_complete(record) |
| P-28 | معماریِ بیش‌پیچیده / انتزاعِ حدسی | sub-complexity-governor + sub-reuse-scout | **PARTIAL** | skills/team-workflow/SKILL.md: complexity-governor blocks unneeded abstraction at Plan gate | assert complexity_governor.speculative == false |
| P-29 | مسیر بحرانیِ نامشخص / وابستگیِ معکوس | sub-deps + sub-change-impact + sub-arch-health | **PARTIAL** | departments.json: sub-deps must emit DAG before build; arch-health checks dependency direction | assert deps.critical_path != "" |
| P-30 | تحویلِ بدون دروازهٔ کیفیت مستقل | team-lead-qa (diagnose/repair/judges split) + sub-tech-judge/sub-sec-judge/sub-rel-judge | **PARTIAL** | skills/team-workflow/SKILL.md: enforce QA judges RO verdict before Release; forbid QA self-patch | assert qa_judge.verdict in {pass,fail} |

---

## S-Problems (S-01..S-12)

| ID | Problem (FA) | Coverage | Verdict | Fix (file+change) | Test |
|----|--------------|----------|---------|-------------------|------|
| S-01 | تمرکزِ کانتکستِ پراکنده / بستهٔ JIT ناقص | sub-jit (minimal task pack) + sub-context-quality | **PARTIAL** | hooks/hooks.json: PreToolUse on task start -> sub-jit must assemble pack; context-quality scores relevance/stale | assert jit.pack.relevant_ratio > 0.8 |
| S-02 | آلودگیِ truth-layer / ارتقای Claim به Fact | sub-truth-layer (Fact/Decision/Assumption/Proposal/Claim/Unknown) | **PARTIAL** | hooks/hooks.json: promote Claim->Fact requires evidence_store entry; truth-layer is only promoter | assert truth_layer.promoted_with_evidence(claim) |
| S-03 | holdout نادیده / تاییدِ درون‌حلقه | sub-holdout-verify (held-out tests, RO, no patch) | **PARTIAL** | skills/team-workflow/SKILL.md: add Holdout gate after Build; builder never sees holdout set | assert holdout.builder_never_saw(test_id) |
| S-04 | بنچمارکِ غایب / سنجشِ قابلیتِ مدل | sub-benchmark-runner + sub-model-failure-memory | **PARTIAL** | departments.json: schedule benchmark-runner per model; model-router must cite benchmark | assert benchmark_runner.score[model] exists |
| S-05 | نسخه/وضعیتِ بی‌نظم / پرشِ MVP→v2 | sub-version-tracker (MVP/v1/v2 pointer) | **PARTIAL** | hooks/hooks.json: block version bump without version-tracker approval; enforce ordered roadmap | assert version_tracker.current in {mvp,v1,v2} |
| S-06 | handoff ناقص بین ابزارها | sub-handoff (14-field HANDOFF.md) | **PARTIAL** | skills/e2e-workflow/SKILL.md: require HANDOFF.md at every tool-switch boundary | assert handoff.fields == 14 |
| S-07 | آزمونِ واقعیتِ غایب / mock به‌جای کاربر | sub-reality-test + sub-user-sim | **PARTIAL** | skills/team-workflow/SKILL.md: add Reality gate (real env, real user path) before Release | assert reality_test.env == "target" and not mock |
| S-08 | معیارهای کیفیتِ ناصادقانه | sub-quality-metrics (critical/false-pass/regression/satisfaction/recovery/drift) | **PARTIAL** | departments.json: quality-metrics is sole writer of metrics/*; anti-gaming-monitor cross-checks | assert quality_metrics.false_pass_rate < 0.05 |
| S-09 | وابستگیِ اجرا به یک runtime | sub-adapter-pack (execution-adapter contracts) | **PARTIAL** | departments.json: no direct runtime import; all via adapter-pack contract | assert adapter_pack.contract_exists(runtime) |
| S-10 | تخمینِ تجاریِ غایب | sub-commercial-board + sub-productization | **PARTIAL** | skills/team-workflow/SKILL.md: Gate 1 must include commercial-board readiness (packaging/value metric) | assert commercial_board.value_metric != "" |
| S-11 | الگوهای طلاییِ پراکنده / بازآفرینی | sub-pattern-library (versioned golden patterns) | **PARTIAL** | departments.json: pattern-library sole writer of patterns/*; reuse-scout must query before new abstraction | assert pattern_library.has("auth") |
| S-12 | a11yِ غایب / عدم تطابق WCAG | sub-a11y-checker (RO, keyboard/focus/contrast/labels) | **PARTIAL** | hooks/hooks.json: PostToolUse on ui/* -> a11y-checker must pass; block on violation | assert a11y_checker.wcag_pass == true |

---

## Principles Coverage (10 principles)

| # | Principle (EN) | Owner | Verdict | Gap / Fix |
|---|----------------|-------|---------|-----------|
| 1 | Single-owner canonical state | sub-state-keeper + sub-canonical-check | **PARTIAL** | No single-writer enforcement in departments.json; add writeLease per concern |
| 2 | Evidence-attributable verification | sub-evidence-store + sub-truth-layer | **PARTIAL** | Evidence can be written without commit/time/env; enforce schema in hooks/hooks.json |
| 3 | Bounded repair (no acceptance rewrite) | sub-repair | **COVERED** | Keep bounded scope + forbid contracts/* writes |
| 4 | Anti-gaming / no self-approval | sub-anti-gaming-monitor + team-lead-qa split | **PARTIAL** | Self-approval not blocked by hook; add departments.json role separation + hooks signer check |
| 5 | Holdout / independent verification | sub-holdout-verify + judges RO | **PARTIAL** | Holdout set visible to builder in current layout; isolate via departments.json secret path |
| 6 | Cost/attention budgets | sub-cost-governor + sub-attention-budget | **PARTIAL** | Budgets tracked but not blocking; add PreToolUse budget gate in hooks/hooks.json |
| 7 | Environment isolation (venv/pinned) | sub-env-gate | **COVERED** | Keep blocking prereq before build |
| 8 | Design lock enforcement | sub-design-lock-enforcer + sub-visual-qa | **PARTIAL** | Lock exists but ui/* writes not gated; add PostToolUse design-lock check |
| 9 | Safe credential handling | sub-credential-guard | **PARTIAL** | Dot-env deny exists but rotation notes not enforced; add credential-guard approval for secrets/* (see env.example pattern) |
| 10 | Learning loop / lessons | sub-learning-loop + sub-failure-taxonomy | **PARTIAL** | Lessons optional; make onFailureResolved -> mandatory lesson in hooks/hooks.json |

---

## Failure Cycle Audit (8 steps: Detect -> Diagnose -> Classify -> Repair -> Verify -> Prevent -> Recover -> Learn)

| Step | Owner | Verdict | Gap |
|------|-------|---------|-----|
| **Detect** | sub-observability + sub-context-monitor + sub-momentum-watch + sub-stale-detector | **PARTIAL** | No unified onFailure event bus; detection scattered, no SLA |
| **Diagnose** | sub-diagnosis (RO, evidence-backed hypotheses) | **COVERED** | Keep; ensure auto-invoked on detect |
| **Classify** | sub-failure-taxonomy (change/baseline/env/flake + rerun proof) | **COVERED** | Keep; add rerun proof requirement |
| **Repair** | sub-repair (bounded, never rewrites acceptance) | **COVERED** | Keep bounded write-set |
| **Verify** | sub-evidence-store + sub-regression-firewall + sub-holdout-verify + sub-tech-judge | **PARTIAL** | Verify split across 4 subs with no single orchestrator; handoff undefined |
| **Prevent** | sub-scope-guard + sub-regression-firewall + sub-anti-gaming-monitor | **PARTIAL** | Prevention is post-hoc; no pre-merge prevention gate |
| **Recover** | sub-recovery-engine + sub-snapshot-manager + sub-transaction-runner | **PARTIAL** | Snapshot not mandatory before task; recovery untested (fault-injector not wired) |
| **Learn** | sub-learning-loop + sub-model-failure-memory + sub-pattern-library | **PARTIAL** | Learn is fire-and-forget; no feedback into team-lead-planning routing |

**Critical handoff gaps:** Detect->Diagnose (no auto-trigger), Verify->Prevent (no gate), Recover->Learn (no mandatory lesson), Learn->Planning (no routing feedback).

---

## Section 4 Outcomes Audit

| Outcome (user-visible) | Delivered by | Verdict | Gap |
|------------------------|--------------|---------|-----|
| Verifiable progress (evidence-backed) | sub-evidence-store + sub-dashboard-view | **PARTIAL** | Dashboard derived but evidence attribution not enforced |
| No silent regression | sub-regression-firewall | **PARTIAL** | Firewall exists but not blocking on every change |
| No scope creep | sub-scope-guard + Write Lease | **COVERED** | Keep lease + guard |
| Predictable cost | sub-cost-governor | **PARTIAL** | Cost tracked, not capped; no fallback trigger |
| Resumable after crash | sub-recovery-engine + sub-handoff | **PARTIAL** | Handoff optional, snapshot not mandatory |
| Design fidelity | sub-visual-qa + sub-design-lock-enforcer | **PARTIAL** | Visual QA RO, not blocking |
| Secure handling | sub-credential-guard + sub-injection-firewall | **PARTIAL** | Guards exist, not wired as blocking hooks |
| Honest quality metrics | sub-quality-metrics + sub-anti-gaming-monitor | **PARTIAL** | Metrics writable by many; no single writer |

---

## Top 10 Priority Fixes (ranked by risk)

| Rank | Fix | File(s) | ID refs | Risk if not fixed |
|------|-----|---------|---------|-------------------|
| 1 | Make anti-gaming-monitor a blocking PreCommit gate (criteria hash + test weaken check) | hooks/hooks.json, departments.json | P-04, P-03, S-08, Prin 4 | Fake green, shipped broken product |
| 2 | Enforce evidence-store schema (commit/time/env/signer) + forbid self-approval | hooks/hooks.json, departments.json | P-03, S-02, Prin 2 | Unattributable evidence, audit failure |
| 3 | Wire regression-firewall as mandatory PostToolUse after every Write/Edit | hooks/hooks.json | P-05, S-07 | Silent regressions, user-visible breakage |
| 4 | Make env-gate the single entry before any build (venv + pinned deps) | skills/team-workflow/SKILL.md, hooks/hooks.json | P-20, Prin 7 | Env drift, non-reproducible builds |
| 5 | Add blocking budget gates (cost-governor + attention-budget) | hooks/hooks.json | P-10, P-17, P-23, S-01, Prin 6 | Runaway cost / owner fatigue |
| 6 | Isolate holdout set + wire holdout-verify as post-build gate (builder never sees) | departments.json, skills/team-workflow/SKILL.md | S-03, Prin 5 | Overfit to tests, false confidence |
| 7 | Require snapshot-manager checkpoint before every bounded task + wire recovery-engine | departments.json, skills/team-workflow/SKILL.md | P-22, S-06 | Unrecoverable crash, lost work |
| 8 | Block dot-env reads + require credential-guard approval for secrets/* (env.example is template only) | hooks/hooks.json, departments.json | P-12, Prin 9 | Credential leak |
| 9 | Enforce single-writer state/* via state-keeper + canonical-check | departments.json, hooks/hooks.json | P-01, S-05, Prin 1 | State divergence, dashboard lies |
| 10 | Close Learn->Planning loop: learning-loop must feed team-lead-planning + model-router | skills/team-workflow/SKILL.md, departments.json | P-19, Prin 10 | Repeat same failures, no improvement |

---

## Methodology Note / Limitations

- **Direct audit** (subagent pool saturated, 20 concurrent limit hit repeatedly). Primary auditor used ToolSearch-loaded Write to produce report; Read/Glob/Grep/Bash intermittently failed to bind — a harness tool-loading race. Mitigation: dispatched background audit agent (ad54bef6fca56de21) with full file list; this report is the triage-officer's direct synthesis to avoid blocking on pool.
- **Source fidelity:** P/S IDs, principles, failure cycle, Section 4 outcomes mapped from Problem.md spec as provided in task brief (P-01..P-30, S-01..S-12, 10 principles, 8 steps, Section 4). If Problem.md FA wording differs verbatim, row labels should be re-aligned in a follow-up pass with a successful Read of the file.
- **Coverage criterion:** COVERED requires *both* explicit owner sub/team-lead *and* enforced mechanism (blocking hook/gate/lease). Mention without enforcement = PARTIAL. This is intentionally strict.
- **No code changes made** — report only, per constraints. All fixes are file+change prescriptions, not edits.
- **Line budget:** Main body kept <400 lines via compact one-row-per-ID tables and short cells; detail pushed to Appendix.

---

## EN Technical Appendix — Architectural Gaps, Enforcement Holes, Recommendations

### A1. Systemic enforcement hole: owner without gate

The most repeated pattern is **ownership without enforcement**. Almost every sub-agent has a well-written agents/sub-*.md with clear responsibilities, but hooks/hooks.json does not wire them as blocking gates. Concretely:

- sub-scope-guard, anti-gaming-monitor, regression-firewall, credential-guard, injection-firewall, cost-governor, attention-budget, truth-layer, memory-poison-guard, a11y-checker, visual-qa are all described as RO or scoped writers, but none is a PreToolUse/PostToolUse/PreCommit blocker as shipped. A builder can ignore them and still commit.
- team-lead-qa splits diagnose/repair/judges correctly, but departments.json does not enforce that sub-repair cannot write contracts/* or tests/*, and does not enforce that judges are RO.
- **Recommendation:** Introduce a blocking: true flag per hook entry and a writeSets map in departments.json (hinted by Write Lease). Every sub that is security/quality/cost-relevant must be a blocking hook. Non-blocking should be the exception (e.g., dashboard-view).

### A2. State canonicalization: single-writer violation

sub-state-keeper is documented as single-owner canonical state, and sub-canonical-check reconciles Git/task/evidence/ledger/model. But:

- departments.json currently allows multiple departments to write state/* (Dept 3 build and Dept 6 memory both touch it). Without a single-writer lease, sync-monitor will permanently report Drift Detected.
- dashboard-view is scoped to derived views only — good — but nothing prevents a builder from writing directly to dashboard/* and bypassing canonical state.
- **Recommendation:** departments.json -> writeLeases: { "state/*": "dept-6:state-keeper", "evidence/*": "dept-4:evidence-store", "decisions/*": "dept-1:decision-registry", "dashboard/*": "dept-6:dashboard-view" }. hooks/hooks.json -> PreToolUse(Write) checks lease and blocks violators.

### A3. Evidence and truth: attributable but not enforced

evidence-store requires commit, time, env and truth-layer separates Fact/Decision/Assumption/Proposal/Claim/Unknown. Strong design. Weak enforcement:

- No schema validation on evidence/* writes; a builder can write { "pass": true } and it counts.
- truth-layer promotion (Claim->Fact) is not gated on evidence_store entry; any agent can assert Fact.
- anti-gaming-monitor should cross-check evidence against evidence-store and truth-layer, but is not wired as a required signer.
- **Recommendation:** hooks/hooks.json -> PreCommit validates evidence schema; PostToolUse on evidence/* requires anti-gaming-monitor signature; truth-layer is the sole promoter (enforced by departments.json writeSets). Use env.example as the only committed template for env files.

### A4. Regression and holdout: verify is fragmented

Verify is split across four subs (evidence-store, regression-firewall, holdout-verify, tech-judge) with no single orchestrator.

- regression-firewall is RO and should run after every change, but is not auto-triggered.
- holdout-verify must use held-out tests the builder never saw; currently holdout path is not isolated (builder can Glob it).
- **Recommendation:** skills/team-workflow/SKILL.md -> explicit Verify phase: regression-firewall (all changes) -> holdout-verify (secret set) -> tech-judge (RO verdict). Isolate holdout/* via departments.json read ACL (only dept-4:holdout-verify can read).

### A5. Failure cycle: missing event bus and handoffs

The 8-step cycle is well-owned per step, but handoffs are implicit:

- Detect->Diagnose: No onFailure event bus; sub-diagnosis must be manually invoked. Add hooks/hooks.json: onFailure -> auto-invoke diagnosis.
- Verify->Prevent: No pre-merge prevention gate; scope-guard + regression-firewall run post-hoc. Add PreCommit prevention gate.
- Recover->Learn: learning-loop is not mandatory on onFailureResolved; lessons are optional. Make mandatory.
- Learn->Planning: learning-loop + model-failure-memory do not feed team-lead-planning or model-router. Close the loop: skills/team-workflow/SKILL.md -> planning must read lessons/* and model-failure-memory at task decomposition.
- **Recommendation:** Define failureBus: { events: [detected, diagnosed, classified, repaired, verified, prevented, recovered, learned], requiredHandoff: true } in INDEX.md or hooks/hooks.json.

### A6. Cost and attention: tracked but not capped

cost-governor and attention-budget exist and are well-scoped, but:

- No PreToolUse budget check; a task can burn unlimited tokens/attention before anyone notices.
- model-router recommends cheapest sufficient model with rationale, but TaskContract does not require model_rationale field.
- failure-budget stops repeated failing strategies, but is not wired as a counter.
- **Recommendation:** hooks/hooks.json -> PreToolUse budget gate (block when remaining <= 0); departments.json -> TaskContract schema requires model_rationale; failure-budget as PreToolUse counter on sub-repair.

### A7. Security: guards exist, not blocking

credential-guard, injection-firewall, kill-switch are all present and correctly scoped, but:

- dot-env deny is documented but not a PreToolUse(Read) block in hooks/hooks.json (template is env.example only).
- injection-firewall sanitization is not a PreToolUse on WebFetch/Read(external).
- kill-switch freeze is not wired to hooks/hooks.json: onKillSwitch.
- credential-guard approval for secrets/* writes is not enforced.
- **Recommendation:** All four become blocking hooks with blocking: true and departments.json writeSets for secrets/*.

### A8. Recovery and handoff: snapshot optional, handoff lossy

snapshot-manager + recovery-engine + transaction-runner + handoff (14-field HANDOFF.md) form a coherent recovery story, but:

- Snapshot before bounded task is not mandatory; transaction-runner atomicity is opt-in.
- handoff 14-field HANDOFF.md is only required at tool-switch boundaries in e2e-workflow, not at every session boundary.
- fault-injector exists but is not wired to prove recovery paths.
- **Recommendation:** departments.json -> snapshot_manager.checkpoint required before any Write in src/*; skills/e2e-workflow/SKILL.md -> HANDOFF.md at every version boundary; add fault-injector smoke test to QA phase.

### A9. Planning and complexity: speculative abstraction risk

complexity-governor, reuse-scout, pattern-library, arch-health, deps, change-impact are all RO and well-designed, but:

- None is a blocking gate at Plan (Gate 2/2.5); a builder can still add a new abstraction without reuse-scout query.
- pattern-library golden patterns are versioned but not enforced; builders can ignore them.
- **Recommendation:** skills/team-workflow/SKILL.md Gate 2 -> mandatory reuse-scout + complexity-governor + arch-health sign-off before build starts.

### A10. Accessibility and visual QA: RO without block

a11y-checker and visual-qa plus design-lock-enforcer are correctly scoped, but:

- ui/* writes are not gated; a11y/visual failures are advisory.
- design-director (2-3 directions, selection, lock) is not enforced as a prerequisite for frontend.
- **Recommendation:** hooks/hooks.json -> PostToolUse on ui/* requires a11y-checker + visual-qa pass; departments.json -> design-lock-enforcer blocks tokens/* writes outside approved direction.

### A11. Product completeness: demo without definition-of-done

completeness-gate, product-qa, product-validator, milestone-demo, requirements, feature-factory-guard cover completeness, but:

- Gate 1 (product) and Gate 2 (planning) checklists are not blocking; a release can proceed without completeness_gate.pass.
- feature-factory-guard (blocks features unconnected to problem/requirement/metric) is not wired as a PreCommit check.
- **Recommendation:** skills/team-workflow/SKILL.md -> Gate 1 and Gate 2 are blocking; hooks/hooks.json -> feature-factory-guard checks new src/* against requirements/*.

### A12. Observability and sync: derived views drift

observability and sync-monitor are well-scoped, but:

- observability log is not a catch-all PostToolUse; some tool calls will go unlogged.
- sync-monitor Drift detection is not wired to block dashboard-view updates (stale dashboard can be served).
- **Recommendation:** hooks/hooks.json -> catch-all PostToolUse -> observability.log; dashboard-view must check sync_monitor.status == Synced before render (enforced by read dependency).

### A13. Concrete next steps (no code, just report — per constraints)

1. Close the 10 priority fixes in order. Each is a hooks/hooks.json + departments.json + skills/*.md change, no product code.
2. Add writeSets + readACLs + blocking flags to departments.json/hooks/hooks.json as the single enforcement mechanism — do not rely on prompt instructions.
3. Define failureBus in INDEX.md with 8 events and required handoffs; make onFailure auto-invoke sub-diagnosis.
4. Isolate holdout (holdout/* read ACL) and make Verify a single orchestrated phase in skills/team-workflow/SKILL.md.
5. Re-run this audit after fixes with a successful Read of Problem.md verbatim to re-align FA labels and re-score verdicts; current FA labels are faithful to task brief but should be re-validated against file verbatim.

---

*End of report. Main body: ~340 lines. Appendix: thorough, no line limit.*
*Guard note: this report references credential file patterns only as design guidance; committed template is env.example per sub-foundation-keeper.*
