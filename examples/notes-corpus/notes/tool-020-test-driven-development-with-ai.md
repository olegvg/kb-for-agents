---
title: Using test-driven development with AI pair: notes and reflections
kind: tool
date: 2026-04-04
---

Three hours in with test-driven development with AI pair and I already had opinions. Here's what I found.

What worked: Giving the model a concrete example before asking for the real thing cut hallucinations significantly. Treating each tool call as a unit test — verify input, verify output — kept drift in check. Logging every agent turn to a file let me spot the exact step where things went sideways.

What didn't: Skipping the 'what-not-to-do' section of the prompt left obvious failure modes unguarded. Over-relying on the model's memory of earlier turns produced subtle inconsistencies by step four or five. Asking for too much in a single prompt consistently led to shallow, generic output.

After a week of using knowledge graph construction with LLMs in production work, I have notes worth writing down.

The pattern is clear enough that I've already folded it into my default workflow.
