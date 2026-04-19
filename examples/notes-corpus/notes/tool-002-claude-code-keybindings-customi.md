---
title: Using Claude Code keybindings customisation: notes and reflections
kind: tool
date: 2026-02-04
---

Three hours in with Claude Code keybindings customisation and I already had opinions. Here's what I found.

What worked: Incremental commits kept the feedback loop tight, which prevented runaway context growth. The iteration speed was noticeably faster once I stopped second-guessing the output. Logging every agent turn to a file let me spot the exact step where things went sideways.

What didn't: Over-relying on the model's memory of earlier turns produced subtle inconsistencies by step four or five. Ignoring context-window limits mid-session caused silent truncation that was hard to diagnose.

Would recommend to anyone already comfortable with the basics — not a first step.
