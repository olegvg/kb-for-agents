---
title: Using diff-based code editing with agents: notes and reflections
kind: tool
date: 2025-11-24
---

Three hours in with diff-based code editing with agents and I already had opinions. Here's what I found.

What worked: I found that explicit constraints in the prompt outperformed general instructions every time. Giving the model a concrete example before asking for the real thing cut hallucinations significantly. Logging every agent turn to a file let me spot the exact step where things went sideways. Incremental commits kept the feedback loop tight, which prevented runaway context growth.

What didn't: I wasted time when I let the model pick its own tools without providing a bounded tool list. Not pinning the model version meant a surprise behavior change after a silent rollout. Mixing two unrelated concerns in one subagent call muddied the output and doubled the review time.

I kept putting off a proper look at few-shot example selection strategies, but a failing deadline pushed me into it.

Still forming a verdict. What I have is enough to keep experimenting.
