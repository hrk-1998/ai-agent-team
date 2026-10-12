---
name: mindmap
description: "Render a professional graphical HTML mindmap (pyramid, top-down, color-coded) instead of any plain-text diagram. Use whenever the user asks for a map, diagram, structure overview, or project explanation."
---

# Graphical Mindmap Skill (always visual, never plain text)

Whenever a map or structure is requested, write a standalone RTL HTML file and show it. No ASCII diagrams, no Mermaid-only answers.

## Required layout (agreed graphic rules)

1. Pyramid top-down: Layer 0 owner → Layer 1 COMMAND OFFICE (master-orchestrator) → Layer 2 office cards.
2. Each office card: office name (RESEARCH / PLANNING / DEVELOPERS / QUALITY / SECURITY & RELEASE / MEMORY OFFICE) + model tag + sub list (name + one-line role) + output doc + gate pill. User sees office names only — never `team-lead-*` ids, never "Dept N".
3. Legend row on top: solid blue line = direct flow, dashed red = error loop, dashed green = live watch, RO/RW/mode tags.
4. SVG connectors between layers (real lines, not implied).
5. Relation matrix table: sender → receiver, line type, allowed/forbidden + one-line why.
6. Dark theme (`#090d16` bg, `#131b2e` cards), Vazirmatn font, color per office, responsive grid. Office titles: اتاق تحقیق و کشف / اتاق برنامه‌ریزی و نقشه‌کشی / اتاق برنامه‌نویسی / اتاق کنترل کیفیت / اتاق امنیت و انتشار / اتاق حافظه و دانش, header: اتاق فرماندهی.
7. Human language: Persian simple for owner-facing parts; EN only inside machine contract examples.

## Workflow

1. Collect the real structure (agents, edges, gates, files) from the repo — never invent nodes.
2. Write `<topic>-mindmap.html` next to the request (or in the project root).
3. Present the file so it opens in the browser pane. Summarize in at most 10 short Persian lines.

## Quality bar

A beginner with zero technical knowledge must understand who talks to whom, in what order, and what each box outputs — from the picture alone.
