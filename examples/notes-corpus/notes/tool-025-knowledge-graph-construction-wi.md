---
title: Using knowledge graph construction with LLMs: notes and reflections
kind: tool
date: 2025-12-13
---

I kept putting off a proper look at knowledge graph construction with LLMs, but a failing deadline pushed me into it.

What worked: Treating each tool call as a unit test — verify input, verify output — kept drift in check. Incremental commits kept the feedback loop tight, which prevented runaway context growth. Giving the model a concrete example before asking for the real thing cut hallucinations significantly.

What didn't: Asking for too much in a single prompt consistently led to shallow, generic output. Over-relying on the model's memory of earlier turns produced subtle inconsistencies by step four or five. Asking for explanations and code in the same response reliably produced worse code.

The pattern is clear enough that I've already folded it into my default workflow.
