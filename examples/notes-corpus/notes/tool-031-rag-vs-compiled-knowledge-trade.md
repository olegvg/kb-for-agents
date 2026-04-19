---
title: Using rag-vs-compiled-knowledge tradeoffs: notes and reflections
kind: tool
date: 2025-08-31
---

I kept putting off a proper look at rag-vs-compiled-knowledge tradeoffs, but a failing deadline pushed me into it.

What worked: Giving the model a concrete example before asking for the real thing cut hallucinations significantly. I found that explicit constraints in the prompt outperformed general instructions every time. Breaking the task into single-responsibility subtasks made each agent invocation predictable.

What didn't: Asking for explanations and code in the same response reliably produced worse code. Ignoring context-window limits mid-session caused silent truncation that was hard to diagnose. Asking for too much in a single prompt consistently led to shallow, generic output.

Going to write up a more structured experiment next time so I have numbers, not just vibes.
