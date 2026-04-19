---
title: Using error recovery in multi-step agents: notes and reflections
kind: tool
date: 2025-09-13
---

Three hours in with error recovery in multi-step agents and I already had opinions. Here's what I found.

What worked: Keeping CLAUDE.md up to date with project-specific decisions saved me repeated explanatory preambles. Breaking the task into single-responsibility subtasks made each agent invocation predictable. I found that explicit constraints in the prompt outperformed general instructions every time.

What didn't: I wasted time when I let the model pick its own tools without providing a bounded tool list. Asking for too much in a single prompt consistently led to shallow, generic output. Ignoring context-window limits mid-session caused silent truncation that was hard to diagnose.

Would recommend to anyone already comfortable with the basics — not a first step.
