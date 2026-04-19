---
title: Reading notes: Constitutional AI: Harmlessness from AI Feedback
kind: paper
date: 2025-09-24
source: "https://arxiv.org/abs/2212.08073"
---

Just finished reading "Constitutional AI: Harmlessness from AI Feedback" (https://arxiv.org/abs/2212.08073).

The evaluation methodology is worth borrowing, separate from the results. I disagreed with one assumption in the setup, but the conclusions are robust enough to survive it. The pattern shows up in how RAG-vs-compiled-knowledge tradeoffs should actually be evaluated. I can see a direct application to how I structure context for long agent sessions. This would pair well with a compiled-knowledge layer to reduce retrieval latency.
