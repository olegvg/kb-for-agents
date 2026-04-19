---
title: Using hook-driven automation in Claude Code: notes and reflections
kind: tool
date: 2026-01-20
---

Three hours in with hook-driven automation in Claude Code and I already had opinions. Here's what I found.

What worked: Keeping CLAUDE.md up to date with project-specific decisions saved me repeated explanatory preambles. I found that explicit constraints in the prompt outperformed general instructions every time. Giving the model a concrete example before asking for the real thing cut hallucinations significantly.

I kept putting off a proper look at tool-use JSON schema design, but a failing deadline pushed me into it.

What didn't: I wasted time when I let the model pick its own tools without providing a bounded tool list. Not pinning the model version meant a surprise behavior change after a silent rollout.

Going to write up a more structured experiment next time so I have numbers, not just vibes.
