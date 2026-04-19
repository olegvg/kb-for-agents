---
title: Using agent loop design patterns: notes and reflections
kind: tool
date: 2025-09-30
---

I tried agent loop design patterns on a real project rather than a toy example, which made all the difference.

Three hours in with Claude Code slash commands and I already had opinions. Here's what I found.

What worked: Logging every agent turn to a file let me spot the exact step where things went sideways. Breaking the task into single-responsibility subtasks made each agent invocation predictable. Treating each tool call as a unit test — verify input, verify output — kept drift in check.

What didn't: Mixing two unrelated concerns in one subagent call muddied the output and doubled the review time. Ignoring context-window limits mid-session caused silent truncation that was hard to diagnose. Over-relying on the model's memory of earlier turns produced subtle inconsistencies by step four or five.

Would recommend to anyone already comfortable with the basics — not a first step.
