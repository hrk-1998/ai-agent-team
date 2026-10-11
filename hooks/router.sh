#!/usr/bin/env bash
# UserPromptSubmit hook: activates master-orchestrator routing when enabled.
# State file: <project>/.ai-agent-team/state  (fallback: ~/.ai-agent-team/state)
# Values: "on" = route every message through the team, "off" = normal session.
set -u

state_file=""
if [ -f ".ai-agent-team/state" ]; then
  state_file=".ai-agent-team/state"
elif [ -f "$HOME/.ai-agent-team/state" ]; then
  state_file="$HOME/.ai-agent-team/state"
fi

if [ -n "$state_file" ]; then
  state_value="$(cat "$state_file" 2>/dev/null | tr -d '[:space:]')"
  if [ "$state_value" = "on" ]; then
    echo "[AI Sub Agent Team] auto-routing ON. Act as master-orchestrator for this message: classify intent (new idea / continue existing project / question / ordinary chat) and route through the dept leads per workflows/team-workflow.md. Raw product idea -> Dept 1 Product. Continue in-progress work -> read Project_Brief.md, Architecture.md, HANDOFF.md, then route to the current dept. Ordinary chat or direct one-off coding request -> answer normally, no team dispatch."
  fi
fi

exit 0
