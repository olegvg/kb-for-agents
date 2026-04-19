---
title: Using error recovery in multi-step agents: notes and reflections
kind: tool
date: 2026-01-07
---

After a week of using error recovery in multi-step agents in production work, I have notes worth writing down.

What worked: Logging every agent turn to a file let me spot the exact step where things went sideways. Giving the model a concrete example before asking for the real thing cut hallucinations significantly.

My first serious session with parallel subagent orchestration surfaced patterns I hadn't anticipated.

What didn't: Ignoring context-window limits mid-session caused silent truncation that was hard to diagnose. Not pinning the model version meant a surprise behavior change after a silent rollout. I wasted time when I let the model pick its own tools without providing a bounded tool list.

Still forming a verdict. What I have is enough to keep experimenting.
