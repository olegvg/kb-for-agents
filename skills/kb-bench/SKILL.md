---
name: kb-bench
description: Use when running benchmark tasks against the demo notes-corpus to compare KB-driven retrieval with a grep-only baseline. Records side-by-side traces for inspection. Triggers on "run kb benchmark", "kb bench", "запусти бенчмарк kb", "сравни kb и grep".
---

# kb-bench — Benchmark KB navigation against grep baseline

## When to use

User wants to see, on the built-in `examples/notes-corpus/`, how the
three-layer KB compares to a naive grep-only baseline. Either runs all
tasks from `benchmarks/notes-corpus/tasks.md`, or one task by ID
(e.g. `T03`).

This skill operates **only on the built-in demo corpus**. For arbitrary
corpora, use `/kb-query` directly.

## Input

- Optional task ID (e.g. `T03`). If absent, run all tasks.

## Workflow

### 1. Determine task list

Read `benchmarks/notes-corpus/tasks.md`. If a task ID was supplied,
filter to that one task. Otherwise use all.

### 2. Create run directory

```
benchmarks/notes-corpus/runs/<UTC-ISO-timestamp>/
```

Use `date -u +%Y%m%dT%H%M%SZ` for the timestamp.

### 3. For each task, run two modes

**With-KB mode:** Invoke `kb-query` on `examples/notes-corpus/` with
the task's question. Track every file opened (in order), every tool
call, and the final answer. Estimate tokens by summing the byte size
of each opened file divided by 4.

**Without-KB mode:** Answer the same question using only `Grep` and
`Glob` over `examples/notes-corpus/notes/`. **Do not read anything
under `.kb/`.** Track the same metrics.

### 4. Write trace files

For each (task, mode) write to:
`benchmarks/notes-corpus/runs/<timestamp>/<task-id>-<mode>.md`

Use the format defined in `benchmarks/notes-corpus/traces/T01-with-kb.md`
as the canonical template (read one reference trace before writing fresh
traces, then mirror its structure exactly).

### 5. Print side-by-side summary

After all tasks complete, print a table to the user:

```
| Task | Mode       | Files | Tools | Tokens | vs reference |
|------|------------|-------|-------|--------|--------------|
| T01  | with-kb    | 5     | 5     | 2400   | matches      |
| T01  | without-kb | 12    | 18    | 14000  | +2 files     |
| ...
```

The "vs reference" column compares fresh trace to
`benchmarks/notes-corpus/traces/<task-id>-<mode>.md` — `matches`,
`+N files / -M tokens`, or `differs` (with brief one-line note).

## Output

- Trace files in `runs/<timestamp>/`
- Summary table printed to user
- Pointer message: "Compare runs/<timestamp>/ against traces/ for any
  task that didn't match."

## Hard limits

- Never write under `.kb/`. This skill is read-only with respect to
  the knowledge base.
- Never run on a corpus other than `examples/notes-corpus/`. The
  benchmark tasks are calibrated for that corpus only.
