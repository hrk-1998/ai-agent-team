# AI Agent Team — Plugin Index (v7, auto-routing via dis-on/dis-off, session-model default, contract schema)

Plugin root: this repo (`D:\AI AGENT TEAM\DIT`). Install: copy to `~/.claude/skills/ai-agent-team/` (auto-loads every session) or `<project>/.claude/skills/ai-agent-team/` (one repo). Then `/reload-plugins`. Marketplace: `.claude-plugin/marketplace.json` (add repo as `hrk-1998/ai-agent-team`).

## Orchestrators (7)

| File | Model | Effort | Tools |
|---|---|---|---|
| master-orchestrator.md | fable | high | Read,Grep,Glob,Agent |
| team-lead-product.md | sonnet | high | Read,Grep,Glob,Agent |
| team-lead-planning.md | inherit | high | Read,Grep,Glob,Agent |
| team-lead-build.md | sonnet | medium | Read,Grep,Glob,Bash,Agent |
| team-lead-qa.md | inherit | high | Read,Grep,Glob,Bash,Agent |
| team-lead-release.md | opus | medium | Read,Grep,Glob,Bash,Agent |
| team-lead-memory.md | inherit | high | Read,Write,Grep,Glob,Agent |

## Subs by Dept (87 plus env-gate and version-tracker = 95 total agent files)

Dept 1 (18): sub-intake, sub-brain, sub-discovery, sub-research, sub-requirements, sub-uncertainty-rater, sub-productization, sub-assumption-registry, sub-decision-registry, sub-decision-gate, sub-question-gate, sub-attention-budget, sub-completeness-gate, sub-feature-factory-guard, sub-commercial-board, sub-milestone-demo, sub-validation-loop, sub-product-validator.
Dept 2 (17): sub-planner, sub-change-impact, sub-deps, sub-ux, sub-visual-scout, sub-design-director, sub-design-lock-enforcer, sub-slop-filter, sub-arch, sub-arch-health, sub-reuse-scout, sub-complexity-governor, sub-pattern-library, sub-model-router, sub-model-failure-memory, sub-adapter-pack, sub-foundation-keeper.
Dept 3 (11): sub-env-gate (blocking first, live-source check), sub-frontend, sub-backend, sub-data, sub-integration, sub-snapshot-manager, sub-recovery-engine, sub-git-operator, sub-transaction-runner, sub-scope-guard, sub-commit-gate.
Dept 4 (18): sub-diagnosis, sub-failure-taxonomy, sub-repair, sub-tech-judge, sub-product-qa, sub-visual-qa, sub-reality-test, sub-user-sim, sub-holdout-verify, sub-a11y-checker, sub-regression-firewall, sub-evidence-store, sub-truth-layer, sub-anti-gaming-monitor, sub-failure-budget, sub-quality-metrics, sub-benchmark-runner, sub-fault-injector.
Dept 5 (9): sub-sec-judge, sub-injection-firewall, sub-credential-guard, sub-rel-judge, sub-kill-switch, sub-observability, sub-dep-drift-watch, sub-env-drift-watch, sub-devops.
Dept 6 (15): sub-state-keeper, sub-context-monitor, sub-context-quality, sub-jit, sub-memory-poison-guard, sub-sync-monitor, sub-canonical-check, sub-cost-governor, sub-momentum-watch, sub-stale-detector, sub-resurrection, sub-learning-loop, sub-dashboard-view, sub-handoff, sub-version-tracker.

Total: 95 agent files. Rule: sub = same-as-lead.

## Workflows (8+1)

master-lead-protocol, sub-lifecycle, dept-1-product, dept-2-planning, dept-3-build, dept-4-qa, dept-5-release, dept-6-memory, plus test-flow-build (smoke).

## Skills (13)

team-workflow, e2e-workflow (/ai-agent-team:e2e-workflow runs MVP then v1 then v2 sequentially until final green), project-handoff, master-model, pro-model, map-model, eng-model, qa-model, rel-model, mem-model, mindmap, dis-on, dis-off.

## Versioning

Each version is gated: MVP green then feedback then repair then next version. E2E loops without skipping. Stop only on last green or on a Master Brief or PRD question truly needing owner.

## Config

departments.json: all keys null = every dept (master included) inherits the CURRENT SESSION model. Set per-dept via /master-model, /pro-model, /map-model, /eng-model, /qa-model, /rel-model, /mem-model; lead + all its subs switch together.

Model input matches whatever `/model` shows: `desktop`/`inherit` (session model), `haiku`, `sonnet`, `opus`, `fable`, or any full id (`claude-*` passes through verbatim). Efforts: `low`, `medium`, `high`, `xhigh`, `max`. A set dept stores `{"model": ..., "effort": ...}` in departments.json and writes model/effort into the lead + effort into every sub.

## Activation

Skills dis-on / dis-off toggle auto-routing on every message via UserPromptSubmit hook (hooks/router.sh). State file: .ai-agent-team/state with value on/off. User guide: USAGE.md (bilingual EN/FA).

## Env gate

sub-env-gate is blocking before any build work: Python vs lib compat with live-source proof, isolated venv, installs via that venv only, template copy, then broadcast verified interpreter path to peers.

## Builds

Repo root is the plugin — copy to skills dir as above. Do not add `agents/` to `~/.claude/agents/` separately; the plugin already carries them.
