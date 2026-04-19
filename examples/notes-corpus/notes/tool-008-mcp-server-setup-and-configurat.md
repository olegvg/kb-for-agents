---
title: Using MCP server setup and configuration: notes and reflections
kind: tool
date: 2025-08-28
---

Picked up MCP server setup and configuration after seeing it mentioned twice in the same week. Decided it warranted a proper try.

What worked: Logging every agent turn to a file let me spot the exact step where things went sideways. Keeping CLAUDE.md up to date with project-specific decisions saved me repeated explanatory preambles. I found that explicit constraints in the prompt outperformed general instructions every time.

What didn't: Mixing two unrelated concerns in one subagent call muddied the output and doubled the review time. Over-relying on the model's memory of earlier turns produced subtle inconsistencies by step four or five. Asking for too much in a single prompt consistently led to shallow, generic output.

The setup cost is real, but it pays back on the third use. Probably worth it.
