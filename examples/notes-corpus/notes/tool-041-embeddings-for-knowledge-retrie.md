---
title: Using embeddings for knowledge retrieval: notes and reflections
kind: tool
date: 2026-03-20
---

I spent the last few days experimenting with embeddings for knowledge retrieval and came away with a clearer picture than when I started.

What worked: Breaking the task into single-responsibility subtasks made each agent invocation predictable. The iteration speed was noticeably faster once I stopped second-guessing the output.

What didn't: Asking for explanations and code in the same response reliably produced worse code. Mixing two unrelated concerns in one subagent call muddied the output and doubled the review time. Not pinning the model version meant a surprise behavior change after a silent rollout.

The pattern is clear enough that I've already folded it into my default workflow.
