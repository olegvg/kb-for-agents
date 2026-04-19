---
title: Using plugin authoring for Claude Code: notes and reflections
kind: tool
date: 2025-09-10
---

I spent the last few days experimenting with plugin authoring for Claude Code and came away with a clearer picture than when I started.

What worked: Keeping CLAUDE.md up to date with project-specific decisions saved me repeated explanatory preambles. The iteration speed was noticeably faster once I stopped second-guessing the output. Treating each tool call as a unit test — verify input, verify output — kept drift in check.

What didn't: Asking for too much in a single prompt consistently led to shallow, generic output. Skipping the 'what-not-to-do' section of the prompt left obvious failure modes unguarded.

Picked up Claude Code slash commands after seeing it mentioned twice in the same week. Decided it warranted a proper try.

The pattern is clear enough that I've already folded it into my default workflow.
