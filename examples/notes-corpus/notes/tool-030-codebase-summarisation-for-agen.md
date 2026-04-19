---
title: Using codebase summarisation for agents: notes and reflections
kind: tool
date: 2025-12-21
---

My first serious session with codebase summarisation for agents surfaced patterns I hadn't anticipated.

What worked: Giving the model a concrete example before asking for the real thing cut hallucinations significantly. Incremental commits kept the feedback loop tight, which prevented runaway context growth.

What didn't: Ignoring context-window limits mid-session caused silent truncation that was hard to diagnose. Skipping the 'what-not-to-do' section of the prompt left obvious failure modes unguarded. Over-relying on the model's memory of earlier turns produced subtle inconsistencies by step four or five.

I'll keep this in the rotation and revisit after a month to see if the rough edges smooth out.
