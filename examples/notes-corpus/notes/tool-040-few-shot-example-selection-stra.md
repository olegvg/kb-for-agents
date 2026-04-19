---
title: Using few-shot example selection strategies: notes and reflections
kind: tool
date: 2025-09-24
---

Picked up few-shot example selection strategies after seeing it mentioned twice in the same week. Decided it warranted a proper try.

What worked: Keeping CLAUDE.md up to date with project-specific decisions saved me repeated explanatory preambles. I found that explicit constraints in the prompt outperformed general instructions every time. The iteration speed was noticeably faster once I stopped second-guessing the output.

Three hours in with audit-of-legacy-codebases with AI assistance and I already had opinions. Here's what I found.

What didn't: Over-relying on the model's memory of earlier turns produced subtle inconsistencies by step four or five. Skipping the 'what-not-to-do' section of the prompt left obvious failure modes unguarded. Mixing two unrelated concerns in one subagent call muddied the output and doubled the review time.

The pattern is clear enough that I've already folded it into my default workflow.
