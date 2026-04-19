---
title: Using semantic search over notes corpus: notes and reflections
kind: tool
date: 2025-09-17
---

Three hours in with semantic search over notes corpus and I already had opinions. Here's what I found.

What worked: Breaking the task into single-responsibility subtasks made each agent invocation predictable. Treating each tool call as a unit test — verify input, verify output — kept drift in check. Keeping CLAUDE.md up to date with project-specific decisions saved me repeated explanatory preambles.

What didn't: Not pinning the model version meant a surprise behavior change after a silent rollout. I wasted time when I let the model pick its own tools without providing a bounded tool list.

After a week of using structured output extraction in production work, I have notes worth writing down.

The pattern is clear enough that I've already folded it into my default workflow.
