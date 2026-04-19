---
title: Using parallel subagent orchestration: notes and reflections
kind: tool
date: 2025-08-18
---

My first serious session with parallel subagent orchestration surfaced patterns I hadn't anticipated.

What worked: I found that explicit constraints in the prompt outperformed general instructions every time. Breaking the task into single-responsibility subtasks made each agent invocation predictable. Logging every agent turn to a file let me spot the exact step where things went sideways.

What didn't: Mixing two unrelated concerns in one subagent call muddied the output and doubled the review time. Not pinning the model version meant a surprise behavior change after a silent rollout.

I'll keep this in the rotation and revisit after a month to see if the rough edges smooth out.
