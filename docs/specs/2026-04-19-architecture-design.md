# Architecture: Demo Corpus and Benchmark Mode

**Date:** 2026-04-19
**Status:** Design — pending implementation

## Goal

Make `kb-for-agents` usable as both a starter-kit (fork-and-apply to your corpus) and a self-contained demonstration (install plugin → try it on a built-in corpus without preparing anything). The demonstration must produce visible, reproducible evidence that the three-layer pattern outperforms naive baselines on a non-trivial corpus.

## Scope

This spec adds three things to the existing plugin:

1. A built-in demo corpus at `examples/notes-corpus/`
2. A demo orchestrator skill `/kb-demo` that gives users guided entry points
3. A benchmark runner `/kb-bench` that produces side-by-side traces

Out of scope: changes to existing skills (`kb-ingest`, `kb-query`, `kb-lint`, `kb-check-drift`, `kb-distill`), changes to the three-layer concept, additional example corpora.

## Alignment with existing concept

The architecture preserves everything in [docs/concept.md](../concept.md):

- `.kb/` lives inside the corpus, not in the plugin. The demo corpus follows the same rule — its `.kb/` lives inside `examples/notes-corpus/`, not in plugin root.
- Three layers + decisions store, indexes-first navigation, manual lint, semantic grouping — all unchanged.
- The plugin remains stateless with respect to any specific corpus. New skills (`kb-demo`, `kb-bench`) take the demo corpus path as a hardcoded internal default, but underlying operations still go through the agnostic core skills.

## Repo layout (delta only)

```
kb-for-agents/
├── commands/
│   ├── kb-demo.md                ← new
│   └── kb-bench.md               ← new
├── skills/
│   ├── kb-demo/SKILL.md          ← new
│   └── kb-bench/SKILL.md         ← new
├── examples/
│   └── notes-corpus/             ← new
│       ├── notes/                  ~150–200 generated .md files (committed)
│       ├── .kb/                    pre-built KB (committed)
│       │   ├── indexes/
│       │   ├── summaries/
│       │   ├── decisions/
│       │   └── .kb-state.json
│       ├── generate.py             corpus generator (optional regen)
│       └── README.md               what's inside, how it was built
└── benchmarks/
    └── notes-corpus/             ← new
        ├── tasks.md                8–12 questions, fixed format
        ├── traces/                 pre-recorded reference runs
        │   ├── T01-with-kb.md
        │   ├── T01-without-kb.md
        │   └── ...
        └── runs/                   user's fresh runs (gitignored except .gitkeep)
            └── <timestamp>/
```

Existing directories (`docs/`, `templates/`, `.claude-plugin/`, top-level `commands/` and `skills/` for the core five) are unchanged.

## The demo corpus

### Composition

~150–200 markdown files in `examples/notes-corpus/notes/`, flat structure (no subdirectories — the point is to demonstrate that `.kb/` brings order to disorder). Mix:

- 40–60 notes about tools and workflow (Claude Code usage, MCP experiments, local setups)
- 30–40 article/paper excerpts (with source attribution in front matter)
- 20–30 project log entries across 2–3 fictional projects (dated, capturing decisions and abandoned approaches)
- 20–30 short idea sketches (incomplete thoughts, half-formed)
- 10–20 ops notes (command recipes, config snippets, troubleshooting)

### Cross-cutting topics

Several topics intentionally appear across multiple note types — for example, "context window management" surfaces in a paper excerpt, two project log entries, and an idea sketch. This stresses the index layer: a good index must group these by topic, not by file type.

### Generation

`generate.py` produces the corpus from public-domain seeds + structured templates. Deterministic given a fixed random seed. Committed output is the source of truth — running the generator is optional (for users who want to vary the corpus).

### Pre-built `.kb/`

`examples/notes-corpus/.kb/` is committed in its expected post-ingest state. Users see the result immediately on plugin install. Anyone who wants to see ingest in action deletes `.kb/` and runs `/kb-ingest examples/notes-corpus/`.

This is a deliberate choice: lowering the barrier to first impression matters more than forcing every user through the build step. The build step is one command away.

## `/kb-demo` — guided entry

Single command, no arguments. Opens an interactive menu:

```
1. Inspect the demo corpus structure (overview of notes/ and .kb/)
2. Ask a question through the KB        → /kb-query examples/notes-corpus/ <Q>
3. Compare KB vs grep on the same Q      → invoke kb-bench for one ad-hoc Q
4. Rebuild .kb/ from scratch             → delete + /kb-ingest examples/notes-corpus/
5. Run the benchmark suite               → /kb-bench
```

Each option is a thin wrapper that calls the underlying agnostic skill with the demo corpus path baked in. The skill itself contains no novel logic — its job is to remove friction for first-time users who don't yet know the command surface.

Option 4 includes a confirmation step ("this will delete `.kb/` and rebuild — continue?") because rebuild takes minutes and pre-built `.kb/` is the expected default state.

## `/kb-bench` — benchmark runner

Signature: `/kb-bench [task-id]`. Without argument, runs all tasks. With `task-id` (e.g. `T03`), runs one.

### Two modes per task

For each task in `benchmarks/notes-corpus/tasks.md`, the skill runs the same question twice:

- **with-kb:** invoke `/kb-query examples/notes-corpus/ <question>`. Agent enters via `_root.md`, descends per indexes-first navigation rules.
- **without-kb:** answer the same question with only `Grep` and `Glob` over `examples/notes-corpus/notes/`. The skill's prompt explicitly forbids reading `.kb/`. This is the "developer-with-grep" baseline.

### Output

For each (task, mode) pair, the skill writes a markdown trace to `benchmarks/notes-corpus/runs/<timestamp>/<task-id>-<mode>.md` containing:

- The question
- Ordered list of files the agent opened
- Final answer
- Crude metrics: total tokens read from the corpus, total tool calls

After all tasks complete, the skill prints a side-by-side summary table comparing the fresh run to the reference traces in `benchmarks/notes-corpus/traces/`.

### Why these two modes only

A naive RAG baseline (chunked embeddings + top-k retrieval) would be a fairer comparison and would address the article's claim that compiled summaries beat RAG. But it requires embedding infrastructure, vector storage, and dependency management — too heavy for a starter-kit. The README acknowledges this explicitly: the grep baseline is intentionally simple, and the comparison is structural (how much context the agent consumes, how many files it touches), not a quality benchmark.

### Reference traces

`benchmarks/notes-corpus/traces/` contains pre-recorded runs from a known-good configuration. Users compare their fresh runs against these to verify their setup behaves as expected and to spot regressions in the underlying skills.

## Task format

`benchmarks/notes-corpus/tasks.md` uses one section per task:

```
## T01 — Cross-cutting concept lookup
**Question:** What approaches to context window management have I tried,
and which did I abandon?
**Why this task:** Forces traversal of multiple indexes (tools, projects,
ideas) and synthesis across note types.
**Expected behavior:** Agent reads _root.md → tools index + projects index
→ 3–5 summaries → answers with concrete examples and abandoned approaches.
```

8–12 tasks total, mixing:
- Concentrated domain queries (one index, deep)
- Cross-cutting queries (multiple indexes, broad)
- Decision-tracing queries (summary → decision record)
- Negative queries (correct answer is "not present in this corpus")

The negative queries matter — they catch hallucination, which is the failure mode the article identifies in RAG.

## Open questions

None blocking implementation. Two for after first release:

- Whether to add a third benchmark mode using a real RAG implementation, gated behind an optional dependency
- Whether the corpus should ship in two sizes (small/large) so users can see how the pattern scales

## Implementation order

1. `examples/notes-corpus/generate.py` + generated `notes/`
2. Run `/kb-ingest` on the corpus, commit resulting `.kb/`
3. `benchmarks/notes-corpus/tasks.md` (8–12 tasks)
4. Record reference traces by running each task manually with both modes; commit to `traces/`
5. `skills/kb-bench/` + `commands/kb-bench.md`
6. `skills/kb-demo/` + `commands/kb-demo.md`
7. Update root `README.md` with quick-start that points at `/kb-demo`
