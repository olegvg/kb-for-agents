---
title: Reading notes: Large Language Models as Tool Makers
kind: paper
date: 2025-11-21
source: "https://arxiv.org/abs/2305.17126"
---

Just finished reading "Large Language Models as Tool Makers" (https://arxiv.org/abs/2305.17126).

This reframed how I think about the knowledge freshness problem in retrieval systems. The ablation tables are where the real insight lives — the abstract undersells the nuance. The pattern shows up in how RAG-vs-compiled-knowledge tradeoffs should actually be evaluated. The approach suggests a way to audit legacy code systematically rather than heuristically. This would pair well with a compiled-knowledge layer to reduce retrieval latency.
