---
title: Project log: personal-brand-ai — 2025-10-01
kind: project-log
date: 2025-10-01
---

Short entry — context is fresher than it will be tomorrow.

The difference between RAG-vs-compiled-knowledge retrieval approaches showed up in latency, not quality.

Discovered that the bottleneck was context-window-management rather than model capability.

Refactored the core loop to be side-effect-free, which made the agent calls trivially testable.

Tomorrow: finish the edge-case handling and write a regression test.
