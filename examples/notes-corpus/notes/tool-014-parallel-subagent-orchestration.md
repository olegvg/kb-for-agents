---
title: Using parallel subagent orchestration: notes and reflections
kind: tool
date: 2025-12-07
---

After a week of using parallel subagent orchestration in production work, I have notes worth writing down.

Three hours in with agent memory architectures and I already had opinions. Here's what I found.

What worked: Breaking the task into single-responsibility subtasks made each agent invocation predictable. Logging every agent turn to a file let me spot the exact step where things went sideways. Giving the model a concrete example before asking for the real thing cut hallucinations significantly. I found that explicit constraints in the prompt outperformed general instructions every time.

What didn't: Not pinning the model version meant a surprise behavior change after a silent rollout. Asking for too much in a single prompt consistently led to shallow, generic output. Ignoring context-window limits mid-session caused silent truncation that was hard to diagnose.

Going to write up a more structured experiment next time so I have numbers, not just vibes.
