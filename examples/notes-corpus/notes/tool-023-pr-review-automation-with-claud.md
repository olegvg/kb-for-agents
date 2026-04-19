---
title: Using PR review automation with Claude: notes and reflections
kind: tool
date: 2025-12-06
---

I kept putting off a proper look at PR review automation with Claude, but a failing deadline pushed me into it.

What worked: Incremental commits kept the feedback loop tight, which prevented runaway context growth. Giving the model a concrete example before asking for the real thing cut hallucinations significantly.

What didn't: Over-relying on the model's memory of earlier turns produced subtle inconsistencies by step four or five. Ignoring context-window limits mid-session caused silent truncation that was hard to diagnose.

Still forming a verdict. What I have is enough to keep experimenting.
