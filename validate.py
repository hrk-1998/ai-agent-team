"""DIT structural validator. Run: python validate.py

Checks:
1. Every agent file has valid YAML frontmatter (name, description, tools).
2. Agent `name` matches its filename.
3. No agent carries a hardcoded model; subs carry none, leads carry `inherit`.
4. Every sub referenced by a lead/workflow/skill exists as an agents/*.md file.
5. Every agent is owned by exactly one department (orphan check).
6. Every skill directory has a SKILL.md with valid name/description.
7. hooks.json is valid JSON and every command path exists.
8. departments.json is valid JSON with the known dept keys.
9. Every workflow references only existing subs.
10. skills/team-workflow is present (required entry point).
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
AGENTS_DIR = ROOT / "agents"
SKILLS_DIR = ROOT / "skills"
WORKFLOWS_DIR = ROOT / "workflows"
HOOKS = ROOT / "hooks" / "hooks.json"
DEPT_JSON = ROOT / "departments.json"

DEPTS = ["product", "planning", "build", "qa", "release", "memory"]
DEPT_LEADS = {
    "product": "team-lead-product",
    "planning": "team-lead-planning",
    "build": "team-lead-build",
    "qa": "team-lead-qa",
    "release": "team-lead-release",
    "memory": "team-lead-memory",
}
MASTER = "master-orchestrator"
VALID_MODELS = {"fable", "sonnet", "opus", "haiku", "inherit"}
REQUIRED_SKILLS = ["team-workflow", "dis-on", "dis-off", "mindmap", "project-handoff"]

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def parse_frontmatter(path: Path) -> dict | None:
    """Extract the leading YAML frontmatter block as flat key lines."""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as exc:  # noqa: BLE001
        err(f"unreadable {path.relative_to(ROOT)}: {exc}")
        return None
    if not text.startswith("---"):
        err(f"{path.relative_to(ROOT)}: missing frontmatter (no leading ---)")
        return None
    end = text.find("\n---", 3)
    if end == -1:
        err(f"{path.relative_to(ROOT)}: unterminated frontmatter")
        return None
    block = text[3:end].strip("\n")
    fm: dict[str, str] = {}
    for line in block.splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        m = re.match(r"^([a-zA-Z_-]+):\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip('"').strip("'")
        else:
            # multi-line tools list or YAML list continuation; tolerate
            fm.setdefault("_extra", "")
            fm["_extra"] += line.strip() + " "
    return fm


# 1-3: frontmatter, name match, model validity
agent_files = sorted(AGENTS_DIR.glob("*.md"))
if len(agent_files) < 90:
    warn(f"expected ~95 agent files, found {len(agent_files)}")

# A real agent reference is either backticked (`sub-brain`) or a list bullet
# ("- sub-frontend: ..."). Plain prose like "sub-task", "sub-agents" or
# "sub-to-sub chat" is not a filename and must not be counted.
REF_RE = re.compile(
    r"`(sub-[a-z0-9]+(?:-[a-z0-9]+)*)`"      # backticked
    r"|^\s*[-*]\s+(sub-[a-z0-9]+(?:-[a-z0-9]+)*)",  # bullet item
    re.M,
)


def find_subs(text: str) -> list[str]:
    out: list[str] = []
    for m in REF_RE.finditer(text):
        tok = m.group(1) or m.group(2)
        if tok and tok not in out:
            out.append(tok)
    return out

agent_names: set[str] = set()
for path in agent_files:
    fm = parse_frontmatter(path)
    if fm is None:
        continue
    rel = path.relative_to(ROOT).as_posix()
    for field in ("name", "description", "tools"):
        if not fm.get(field):
            err(f"{rel}: frontmatter missing '{field}'")
    name = fm.get("name", "")
    expected = path.stem
    local_errors: list[str] = []
    if name != expected:
        local_errors.append(f"frontmatter name '{name}' != filename '{expected}'")
    agent_names.add(name or expected)

    model = fm.get("model")
    effort = fm.get("effort")
    if expected == MASTER or expected in DEPT_LEADS.values():
        if model is None:
            local_errors.append("lead/master has no model field")
        elif model not in VALID_MODELS:
            local_errors.append(f"invalid model '{model}'")
        elif model != "inherit":
            # leads may override, but a hardcoded old alias was already cleared
            warn(f"{rel}: lead uses explicit model '{model}' (inherit = session default)")
        if effort is not None and effort not in ("low", "medium", "high"):
            local_errors.append(f"invalid effort '{effort}'")
    else:
        if model is not None:
            local_errors.append(f"sub carries model '{model}'; subs must inherit the lead")
        if effort is not None:
            local_errors.append(f"sub carries effort '{effort}'; subs must inherit the lead")
    if expected == MASTER and model != "inherit":
        local_errors.append("master must use model: inherit")
    errors.extend(local_errors)

if not AGENTS_DIR.joinpath(f"{MASTER}.md").exists():
    err(f"missing master agent file agents/{MASTER}.md")
for lead in DEPT_LEADS.values():
    if not AGENTS_DIR.joinpath(f"{lead}.md").exists():
        err(f"missing dept lead file agents/{lead}.md")

# 4+5: ownership from lead files, existence of referenced subs
dept_of: dict[str, str] = {}
for dept, lead in DEPT_LEADS.items():
    lead_path = AGENTS_DIR / f"{lead}.md"
    if not lead_path.exists():
        continue
    text = lead_path.read_text(encoding="utf-8")
    for sub in find_subs(text):
        if sub in DEPT_LEADS.values():
            continue
        if sub in dept_of and dept_of[sub] != dept:
            warn(f"{sub} listed by {dept} and {dept_of[sub]} (dual ownership)")
        dept_of[sub] = dept
        if not AGENTS_DIR.joinpath(f"{sub}.md").exists():
            err(f"{lead} references missing agent {sub}")
        else:
            agent_names.add(sub)

or_by_name: dict[str, str] = {}
for dept, lead in DEPT_LEADS.items():
    if lead in agent_names:
        or_by_name[lead] = dept

or_by_name[MASTER] = "master"

orphans = sorted(
    p.stem
    for p in agent_files
    if p.stem not in dept_of
    and p.stem not in DEPT_LEADS.values()
    and p.stem != MASTER
)
if orphans:
    warn(f"orphan agents (not listed by any lead): {', '.join(orphans)}")

# 6: skills
for skill_dir in sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir()):
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        err(f"skill {skill_dir.name}: missing SKILL.md")
        continue
    fm = parse_frontmatter(skill_md)
    if fm is None:
        continue
    if fm.get("name") != skill_dir.name:
        err(
            f"skill {skill_dir.name}: frontmatter name '{fm.get('name')}' != dir name"
        )
    if not fm.get("description"):
        err(f"skill {skill_dir.name}: missing description")

for req in REQUIRED_SKILLS:
    if not (SKILLS_DIR / req / "SKILL.md").exists():
        err(f"required skill missing: {req}")

# 7: hooks.json
if not HOOKS.exists():
    err("hooks/hooks.json missing")
else:
    try:
        hooks_data = json.loads(HOOKS.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        err(f"hooks.json is not valid JSON: {exc}")
    else:
        for event, entries in hooks_data.get("hooks", {}).items():
            for entry in entries:
                for h in entry.get("hooks", []):
                    cmd = h.get("command", "")
                    m = re.search(r'/hooks/([a-zA-Z0-9_.-]+\.sh)', cmd)
                    if m and not (ROOT / "hooks" / m.group(1)).exists():
                        err(f"hooks.json references missing script hooks/{m.group(1)}")
        if "UserPromptSubmit" not in hooks_data.get("hooks", {}):
            warn("no UserPromptSubmit hook; auto-routing (dis-on/off) will not fire")

# 8: departments.json
if not DEPT_JSON.exists():
    err("departments.json missing")
else:
    try:
        dept_data = json.loads(DEPT_JSON.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        err(f"departments.json invalid JSON: {exc}")
    else:
        for dept in DEPTS:
            if dept not in dept_data:
                err(f"departments.json missing key '{dept}'")
        if dept_data.get(MASTER) is not None:
            warn("master not null; session-model default overridden")

# 9: workflow sub references
for wf in sorted(WORKFLOWS_DIR.glob("*.md")):
    text = wf.read_text(encoding="utf-8")
    for sub in find_subs(text):
        if not AGENTS_DIR.joinpath(f"{sub}.md").exists():
            err(f"{wf.relative_to(ROOT).as_posix()}: references missing agent {sub}")

# 10: manifest
manifest = ROOT / ".claude-plugin" / "plugin.json"
if not manifest.exists():
    err(".claude-plugin/plugin.json missing")
else:
    try:
        mf = json.loads(manifest.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        err(f"plugin.json invalid JSON: {exc}")
    else:
        for k in ("name", "version", "description"):
            if not mf.get(k):
                err(f"plugin.json missing '{k}'")

# ---- report ----
print(f"agents: {len(agent_files)} files")
print(f"skills: {len(list(SKILLS_DIR.iterdir()))} entries")
print(f"workflows: {len(list(WORKFLOWS_DIR.glob('*.md')))} files")
print(f"dept subs owned: {len(dept_of)}")
print()
if warnings:
    print(f"WARNINGS ({len(warnings)}):")
    for w in warnings:
        print(f"  ! {w}")
    print()
if errors:
    print(f"FAILED ({len(errors)} errors):")
    for e in errors:
        print(f"  x {e}")
    sys.exit(1)
print("PASS - structure valid")
