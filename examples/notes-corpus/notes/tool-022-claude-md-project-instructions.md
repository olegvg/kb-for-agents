---
title: Using CLAUDE.md project instructions: notes and reflections
kind: tool
date: 2025-09-21
---

Picked up CLAUDE.md project instructions after seeing it mentioned twice in the same week. Decided it warranted a proper try.

What worked: Keeping CLAUDE.md up to date with project-specific decisions saved me repeated explanatory preambles. I found that explicit constraints in the prompt outperformed general instructions every time. Giving the model a concrete example before asking for the real thing cut hallucinations significantly. Breaking the task into single-responsibility subtasks made each agent invocation predictable.

What didn't: Mixing two unrelated concerns in one subagent call muddied the output and doubled the review time. Asking for explanations and code in the same response reliably produced worse code. Ignoring context-window limits mid-session caused silent truncation that was hard to diagnose.

The setup cost is real, but it pays back on the third use. Probably worth it.
