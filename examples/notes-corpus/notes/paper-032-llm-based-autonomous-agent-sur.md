---
title: Reading notes: LLM-based Autonomous Agent Survey (synthetic)
kind: paper
date: 2025-12-13
source: "https://arxiv.org/abs/2308.11432"
---

Just finished reading "LLM-based Autonomous Agent Survey (synthetic)" (https://arxiv.org/abs/2308.11432).

This reframed how I think about the knowledge freshness problem in retrieval systems. Several ideas here transfer directly to agent pipeline design, even though that wasn't the paper's framing. I had heard the headline finding cited dozens of times, but reading the actual method section changed my interpretation. The pattern shows up in how RAG-vs-compiled-knowledge tradeoffs should actually be evaluated. The approach suggests a way to audit legacy code systematically rather than heuristically. This would pair well with a compiled-knowledge layer to reduce retrieval latency.
