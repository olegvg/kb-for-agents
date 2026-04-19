---
title: Using embeddings for knowledge retrieval: notes and reflections
kind: tool
date: 2025-11-09
---

Three hours in with embeddings for knowledge retrieval and I already had opinions. Here's what I found.

What worked: The iteration speed was noticeably faster once I stopped second-guessing the output. Treating each tool call as a unit test — verify input, verify output — kept drift in check. I found that explicit constraints in the prompt outperformed general instructions every time.

What didn't: Over-relying on the model's memory of earlier turns produced subtle inconsistencies by step four or five. Skipping the 'what-not-to-do' section of the prompt left obvious failure modes unguarded. Asking for too much in a single prompt consistently led to shallow, generic output.

Going to write up a more structured experiment next time so I have numbers, not just vibes.
