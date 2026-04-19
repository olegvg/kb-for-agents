---
title: Using tool-use JSON schema design: notes and reflections
kind: tool
date: 2026-03-04
---

I spent the last few days experimenting with tool-use JSON schema design and came away with a clearer picture than when I started.

I tried audit-of-legacy-codebases with AI assistance on a real project rather than a toy example, which made all the difference.

What worked: Giving the model a concrete example before asking for the real thing cut hallucinations significantly. I found that explicit constraints in the prompt outperformed general instructions every time. Treating each tool call as a unit test — verify input, verify output — kept drift in check.

What didn't: Not pinning the model version meant a surprise behavior change after a silent rollout. Mixing two unrelated concerns in one subagent call muddied the output and doubled the review time. Over-relying on the model's memory of earlier turns produced subtle inconsistencies by step four or five.

I'll keep this in the rotation and revisit after a month to see if the rough edges smooth out.
