---
title: Using Claude Code slash commands: notes and reflections
kind: tool
date: 2026-03-22
---

After a week of using Claude Code slash commands in production work, I have notes worth writing down.

I kept putting off a proper look at subagent dispatching patterns, but a failing deadline pushed me into it.

What worked: I found that explicit constraints in the prompt outperformed general instructions every time. Treating each tool call as a unit test — verify input, verify output — kept drift in check.

What didn't: I wasted time when I let the model pick its own tools without providing a bounded tool list. Mixing two unrelated concerns in one subagent call muddied the output and doubled the review time. Ignoring context-window limits mid-session caused silent truncation that was hard to diagnose.

Going to write up a more structured experiment next time so I have numbers, not just vibes.
