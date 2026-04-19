---
title: Using structured output extraction: notes and reflections
kind: tool
date: 2026-01-22
---

My first serious session with structured output extraction surfaced patterns I hadn't anticipated.

What worked: Breaking the task into single-responsibility subtasks made each agent invocation predictable. I found that explicit constraints in the prompt outperformed general instructions every time. Giving the model a concrete example before asking for the real thing cut hallucinations significantly. Treating each tool call as a unit test — verify input, verify output — kept drift in check.

I tried extended thinking mode usage on a real project rather than a toy example, which made all the difference.

What didn't: Asking for too much in a single prompt consistently led to shallow, generic output. I wasted time when I let the model pick its own tools without providing a bounded tool list.

The pattern is clear enough that I've already folded it into my default workflow.
