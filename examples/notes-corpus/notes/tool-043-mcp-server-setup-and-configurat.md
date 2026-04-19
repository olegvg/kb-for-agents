---
title: Using MCP server setup and configuration: notes and reflections
kind: tool
date: 2025-10-23
---

After a week of using MCP server setup and configuration in production work, I have notes worth writing down.

I spent the last few days experimenting with Claude Code slash commands and came away with a clearer picture than when I started.

What worked: Keeping CLAUDE.md up to date with project-specific decisions saved me repeated explanatory preambles. Treating each tool call as a unit test — verify input, verify output — kept drift in check. Breaking the task into single-responsibility subtasks made each agent invocation predictable. I found that explicit constraints in the prompt outperformed general instructions every time.

What didn't: Mixing two unrelated concerns in one subagent call muddied the output and doubled the review time. Ignoring context-window limits mid-session caused silent truncation that was hard to diagnose. Asking for too much in a single prompt consistently led to shallow, generic output.

Going to write up a more structured experiment next time so I have numbers, not just vibes.
