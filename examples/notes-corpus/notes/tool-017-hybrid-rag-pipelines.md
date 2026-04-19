---
title: Using hybrid RAG pipelines: notes and reflections
kind: tool
date: 2026-03-09
---

After a week of using hybrid RAG pipelines in production work, I have notes worth writing down.

What worked: The iteration speed was noticeably faster once I stopped second-guessing the output. Breaking the task into single-responsibility subtasks made each agent invocation predictable. Giving the model a concrete example before asking for the real thing cut hallucinations significantly.

What didn't: Asking for explanations and code in the same response reliably produced worse code. Not pinning the model version meant a surprise behavior change after a silent rollout. Mixing two unrelated concerns in one subagent call muddied the output and doubled the review time.

The setup cost is real, but it pays back on the third use. Probably worth it.
