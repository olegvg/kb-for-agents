---
title: Using audit-of-legacy-codebases with AI assistance: notes and reflections
kind: tool
date: 2026-01-16
---

My first serious session with audit-of-legacy-codebases with AI assistance surfaced patterns I hadn't anticipated.

After a week of using agent memory architectures in production work, I have notes worth writing down.

What worked: Incremental commits kept the feedback loop tight, which prevented runaway context growth. Giving the model a concrete example before asking for the real thing cut hallucinations significantly. I found that explicit constraints in the prompt outperformed general instructions every time. Breaking the task into single-responsibility subtasks made each agent invocation predictable.

What didn't: Not pinning the model version meant a surprise behavior change after a silent rollout. Asking for too much in a single prompt consistently led to shallow, generic output. I wasted time when I let the model pick its own tools without providing a bounded tool list.

The pattern is clear enough that I've already folded it into my default workflow.
