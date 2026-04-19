---
title: Reading notes: Audit of Legacy Codebases Using Static Analysis and LLMs (synthetic)
kind: paper
date: 2025-10-16
source: "https://arxiv.org/abs/2402.00001"
---

Just finished reading "Audit of Legacy Codebases Using Static Analysis and LLMs (synthetic)" (https://arxiv.org/abs/2402.00001).

Several ideas here transfer directly to agent pipeline design, even though that wasn't the paper's framing. I had heard the headline finding cited dozens of times, but reading the actual method section changed my interpretation. The evaluation methodology is worth borrowing, separate from the results. I can see a direct application to how I structure context for long agent sessions. The pattern shows up in how RAG-vs-compiled-knowledge tradeoffs should actually be evaluated. The approach suggests a way to audit legacy code systematically rather than heuristically.
