---
name: kb-demo
description: Use when the user wants to try the kb-for-agents plugin on the built-in notes-corpus without preparing their own corpus. Presents a 5-option menu and routes to the right underlying skill. Triggers on "kb demo", "try kb", "show me kb", "демо kb", "попробовать kb".
---

# kb-demo — Guided entry to the built-in demo corpus

## When to use

First-time user installed the plugin and wants to see what it does on
real content before applying it to their own corpus. This skill is a
thin orchestrator — it does not implement KB logic, only routes to
the agnostic skills with the demo path baked in.

## Input

None. Always opens the menu.

## Workflow

### 1. Print the menu

```
What would you like to try?

  1. Inspect the demo corpus structure
  2. Ask a question through the KB
  3. Compare KB vs grep on the same question
  4. Rebuild .kb/ from scratch
  5. Run the benchmark suite
```

Wait for the user to choose 1–5 (or quit).

### 2. Dispatch by choice

- **1:** Run `ls examples/notes-corpus/notes/ | head -30`, then
  `find examples/notes-corpus/.kb/ -type f | sort`. Briefly describe
  what they're looking at (notes are flat and unstructured; .kb/ has
  indexes + summaries that the agent navigates).

- **2:** Ask the user for a question, then invoke `kb-query` on
  `examples/notes-corpus/` with that question. Suggest examples from
  `benchmarks/notes-corpus/tasks.md` if the user wants ideas.

- **3:** Ask for a question, then invoke `kb-bench` for an ad-hoc
  question (NOT a benchmark task). Run both modes manually as in
  `kb-bench`'s workflow, but write traces to a temporary location
  and print results inline rather than persisting.

- **4:** Confirm: "This will delete `examples/notes-corpus/.kb/` and
  rebuild it via `/kb-ingest`. The pre-built KB is the expected
  default state. Continue? (y/N)". On `y`, `rm -rf
  examples/notes-corpus/.kb/` then invoke `kb-ingest` on the corpus.
  On `N` or anything else, abort.

- **5:** Invoke `kb-bench` with no arguments (runs all tasks).

### 3. After dispatch

Offer to return to the menu for another option, or stop.

## Hard limits

- Operates only on `examples/notes-corpus/`. Never accept a different
  corpus path — that's what `/kb-query`, `/kb-ingest`, `/kb-bench`
  are for.
- Never write outside `examples/notes-corpus/` or
  `benchmarks/notes-corpus/runs/`.
