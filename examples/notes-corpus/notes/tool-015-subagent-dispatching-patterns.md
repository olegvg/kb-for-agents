---
title: Using subagent dispatching patterns: notes and reflections
kind: tool
date: 2025-09-14
---

Three hours in with subagent dispatching patterns and I already had opinions. Here's what I found.

What worked: Logging every agent turn to a file let me spot the exact step where things went sideways. Incremental commits kept the feedback loop tight, which prevented runaway context growth.

I kept putting off a proper look at audit-of-legacy-codebases with AI assistance, but a failing deadline pushed me into it.

What didn't: Skipping the 'what-not-to-do' section of the prompt left obvious failure modes unguarded. Ignoring context-window limits mid-session caused silent truncation that was hard to diagnose. Over-relying on the model's memory of earlier turns produced subtle inconsistencies by step four or five.

Going to write up a more structured experiment next time so I have numbers, not just vibes.
