---
title: Reading notes: ReAct: Synergizing Reasoning and Acting in Language Models
kind: paper
date: 2025-09-25
source: "https://arxiv.org/abs/2210.03629"
---

Just finished reading "ReAct: Synergizing Reasoning and Acting in Language Models" (https://arxiv.org/abs/2210.03629).

I had heard the headline finding cited dozens of times, but reading the actual method section changed my interpretation. Several ideas here transfer directly to agent pipeline design, even though that wasn't the paper's framing. I disagreed with one assumption in the setup, but the conclusions are robust enough to survive it. I'll try the main heuristic on a real codebase next week to see if it generalises. I can see a direct application to how I structure context for long agent sessions. The pattern shows up in how RAG-vs-compiled-knowledge tradeoffs should actually be evaluated.
