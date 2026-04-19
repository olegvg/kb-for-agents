---
title: Using context-window-management strategies: notes and reflections
kind: tool
date: 2025-10-06
---

I spent the last few days experimenting with context-window-management strategies and came away with a clearer picture than when I started.

What worked: Breaking the task into single-responsibility subtasks made each agent invocation predictable. I found that explicit constraints in the prompt outperformed general instructions every time. Treating each tool call as a unit test — verify input, verify output — kept drift in check.

What didn't: Mixing two unrelated concerns in one subagent call muddied the output and doubled the review time. Asking for too much in a single prompt consistently led to shallow, generic output.

Going to write up a more structured experiment next time so I have numbers, not just vibes.
