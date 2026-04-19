# Demo Corpus and Benchmark Mode — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a built-in demo corpus, an orchestrator skill `/kb-demo`, and a benchmark runner `/kb-bench` so that anyone installing the plugin can experience the three-layer KB pattern on a non-trivial corpus without preparing one.

**Architecture:** Demo corpus lives under `examples/notes-corpus/`. Generator script produces ~150–200 markdown notes deterministically. Pre-built `.kb/` is committed alongside. New skills wrap existing agnostic skills (`kb-ingest`, `kb-query`) with the demo path baked in. Benchmark runner produces side-by-side traces (with KB vs grep-only baseline) for fixed tasks. No automated test suite — verification is by reading and dogfooding, per repo convention (see CLAUDE.md).

**Tech Stack:** Markdown skills/commands. Python 3.11+ (single stdlib-only generator script, no dependencies). Git for state tracking.

**Reference spec:** [docs/specs/2026-04-19-architecture-design.md](../specs/2026-04-19-architecture-design.md)

---

## Notes for the implementer

This repo is **markdown-only with a single Python generator**. There is no test suite, no build system, no package manager (see CLAUDE.md). Verification means: (1) read the file and check it matches the spec, (2) for behavior changes, run the affected skill against the demo corpus and inspect the result.

The generator is the only Python in the repo. Keep it stdlib-only — no `uv add`, no `pip install`. If you need randomness, use `random.Random(seed)` for determinism.

Every task ends with a commit. Commit messages follow the repo style: lowercase prefix (`feat:`, `docs:`, `chore:`), short imperative subject. See `git log --oneline` for examples.

---

## Task 1: Demo corpus generator skeleton

**Files:**
- Create: `examples/notes-corpus/generate.py`
- Create: `examples/notes-corpus/README.md`
- Create: `examples/notes-corpus/.gitkeep` (placeholder until `notes/` exists)

- [ ] **Step 1: Create `examples/notes-corpus/generate.py`**

Stdlib-only Python script. Deterministic given fixed seed. Produces 150–200 markdown files in `notes/` relative to script location. Each file has YAML front matter (`title`, `kind`, `date`, optional `source`).

Five `kind` values: `tool`, `paper`, `project-log`, `idea`, `ops`. Counts per kind:

```python
COUNTS = {
    "tool":        50,   # 40–60 range
    "paper":       35,   # 30–40
    "project-log": 25,   # 20–30
    "idea":        25,   # 20–30
    "ops":         15,   # 10–20
}
```

Total: 150 files. Within budget.

Script structure:

```python
#!/usr/bin/env python3
"""Generate a synthetic notes corpus for the kb-for-agents demo.

Stdlib-only. Deterministic given SEED. Writes .md files under notes/.
"""
import random
import shutil
from pathlib import Path
from datetime import date, timedelta

SEED = 20260419
HERE = Path(__file__).parent
OUT = HERE / "notes"

COUNTS = {
    "tool": 50,
    "paper": 35,
    "project-log": 25,
    "idea": 25,
    "ops": 15,
}

# Seed pools — extracted to module-level constants so they're easy to
# inspect and edit without touching generation logic.

TOOL_TOPICS = [
    "claude-code-skills", "mcp-servers", "context-window-management",
    "subagents", "slash-commands", "plugin-development",
    # ... (see below for full list expectations)
]

PAPER_SOURCES = [
    {"title": "Attention Is All You Need", "url": "arxiv.org/abs/1706.03762"},
    {"title": "Constitutional AI", "url": "arxiv.org/abs/2212.08073"},
    # ...
]

PROJECTS = [
    {"slug": "casino-audit", "started": date(2025, 9, 1)},
    {"slug": "notion-archive", "started": date(2025, 11, 15)},
    {"slug": "kb-for-agents", "started": date(2026, 2, 10)},
]

CROSS_CUTTING = [
    "context-window-management",
    "rag-vs-compiled-knowledge",
    "audit-of-legacy-codebases",
]
# Each cross-cutting topic must appear in at least 3 different `kind`s.

def main() -> None:
    rng = random.Random(SEED)
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    for kind, n in COUNTS.items():
        generate_kind(kind, n, rng)

    enforce_cross_cutting(rng)
    print(f"wrote {sum(COUNTS.values())} files to {OUT}")

# generate_kind, enforce_cross_cutting, write_note, etc.
# follow — full bodies in Task 2.

if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Create `examples/notes-corpus/README.md`**

```markdown
# notes-corpus

Synthetic corpus for demonstrating the three-layer knowledge base pattern.

## Composition

150 markdown notes in `notes/`, flat layout (no subdirectories — the
unstructured starting state is the point). Five kinds:

| kind          | count | content                                       |
|---------------|-------|-----------------------------------------------|
| `tool`        | 50    | tools, workflow, Claude Code, MCP, plugins    |
| `paper`       | 35    | excerpts from papers/articles, with sources   |
| `project-log` | 25    | dated entries across 3 fictional projects     |
| `idea`        | 25    | short, half-formed sketches                   |
| `ops`         | 15    | command recipes, config snippets, fixes       |

Several topics deliberately appear across multiple kinds (e.g.
"context-window-management" surfaces in tool notes, paper excerpts, and
project logs). This stresses the index layer to group by topic, not by
file kind.

## Regenerating

```
python3 generate.py
```

Stdlib-only. Deterministic given the fixed seed in `generate.py`.
Committed `notes/` is the source of truth; regeneration is optional.

## Pre-built `.kb/`

The `.kb/` directory in this folder is the result of running
`/kb-ingest examples/notes-corpus/` once and committing the output.
To rebuild: delete `.kb/` and re-run the skill.
```

- [ ] **Step 3: Create empty placeholder `examples/notes-corpus/.gitkeep`**

Single empty file. Keeps the directory in git before `notes/` and `.kb/` are populated.

- [ ] **Step 4: Verify by inspection**

Read all three files. Check that `generate.py` is syntactically importable:

```bash
python3 -c "import ast; ast.parse(open('examples/notes-corpus/generate.py').read())"
```

Expected: no output (silent success).

- [ ] **Step 5: Commit**

```bash
git add examples/notes-corpus/
git commit -m "feat: scaffold notes-corpus generator and README"
```

---

## Task 2: Flesh out the generator

**Files:**
- Modify: `examples/notes-corpus/generate.py`

The skeleton from Task 1 calls helpers (`generate_kind`, `enforce_cross_cutting`, `write_note`) that don't exist yet. Implement them.

- [ ] **Step 1: Add `write_note` helper**

```python
def write_note(slug: str, kind: str, title: str, body: str,
               note_date: date, source: str | None = None) -> None:
    """Write a single .md file with YAML front matter."""
    front = ["---",
             f'title: "{title}"',
             f"kind: {kind}",
             f"date: {note_date.isoformat()}"]
    if source:
        front.append(f'source: "{source}"')
    front.append("---")
    content = "\n".join(front) + "\n\n" + body.strip() + "\n"
    (OUT / f"{slug}.md").write_text(content)
```

- [ ] **Step 2: Add `generate_kind` dispatcher**

```python
def generate_kind(kind: str, n: int, rng: random.Random) -> None:
    generators = {
        "tool":        gen_tool,
        "paper":       gen_paper,
        "project-log": gen_project_log,
        "idea":        gen_idea,
        "ops":         gen_ops,
    }
    for i in range(n):
        generators[kind](i, rng)
```

- [ ] **Step 3: Implement the five `gen_*` functions**

Each takes `(i: int, rng: random.Random)` and calls `write_note`. Bodies are 3–8 paragraphs of synthetic text built from seed pools by templated combination. Constraints:

- `gen_tool`: title from `TOOL_TOPICS` + suffix; body discusses the topic in first person ("I tried…", "What worked…"). Slug: `tool-{i:03d}-{topic-slug}`.
- `gen_paper`: pick from `PAPER_SOURCES`; body is a 4–6 sentence "what I took away" excerpt. Slug: `paper-{i:03d}-{title-slug}`. Include `source` in front matter.
- `gen_project_log`: pick a project, pick a date offset from project's `started`, write a dated log entry ("Day 12: realized X, abandoned Y, leaning toward Z"). Slug: `log-{project-slug}-{YYYY-MM-DD}`.
- `gen_idea`: 1–3 short paragraphs, deliberately incomplete ("what if…", "haven't figured out…"). Slug: `idea-{i:03d}-{kebab-phrase}`.
- `gen_ops`: command recipe or config snippet with a sentence of context. Slug: `ops-{i:03d}-{topic}`.

For each function, compose body text by concatenating fragments from per-kind seed pools using `rng.choice()` and `rng.sample()`. Keep the seed pools at module top so they're easy to extend without touching logic.

- [ ] **Step 4: Implement `enforce_cross_cutting`**

After per-kind generation, ensure each topic in `CROSS_CUTTING` appears in at least 3 different `kind`s. Approach: rewrite a randomly selected note from each underrepresented `kind` to include the topic in its title and body.

```python
def enforce_cross_cutting(rng: random.Random) -> None:
    for topic in CROSS_CUTTING:
        present_kinds = scan_topic_presence(topic)
        missing = {"tool", "paper", "project-log", "idea", "ops"} - present_kinds
        # Pick up to (3 - len(present_kinds)) kinds from `missing` and
        # rewrite one note in each to include the topic.
        ...
```

`scan_topic_presence` walks `OUT/*.md`, returns set of `kind`s where topic substring appears in title or body.

- [ ] **Step 5: Run the generator**

```bash
cd examples/notes-corpus && python3 generate.py
```

Expected: `wrote 150 files to .../notes`. Check:

```bash
ls examples/notes-corpus/notes/ | wc -l
# expect: 150
```

Verify cross-cutting:

```bash
grep -l "context-window-management" examples/notes-corpus/notes/*.md | \
  xargs grep -h "^kind:" | sort -u | wc -l
# expect: at least 3
```

- [ ] **Step 6: Commit generator + corpus**

```bash
git add examples/notes-corpus/generate.py examples/notes-corpus/notes/
git rm examples/notes-corpus/.gitkeep
git commit -m "feat: generate 150-note synthetic demo corpus"
```

---

## Task 3: Build pre-committed `.kb/` for the demo corpus

**Files:**
- Create (via skill): `examples/notes-corpus/.kb/indexes/_root.md`
- Create (via skill): `examples/notes-corpus/.kb/indexes/<area>.md` (multiple)
- Create (via skill): `examples/notes-corpus/.kb/summaries/<area>/*.md`
- Create (via skill): `examples/notes-corpus/.kb/.kb-state.json`

This task dogfoods `kb-ingest` against the freshly generated corpus.

- [ ] **Step 1: Run `kb-ingest` against the corpus**

In a Claude Code session with the plugin installed:

```
/kb-ingest examples/notes-corpus/
```

The skill executes its three-pass workflow (survey → parallel deep-ingest → main-agent index assembly). Produces `.kb/` inside the corpus.

- [ ] **Step 2: Verify the structure**

```bash
find examples/notes-corpus/.kb/ -type f | sort
```

Expected:
- `examples/notes-corpus/.kb/indexes/_root.md` (exists)
- `examples/notes-corpus/.kb/indexes/<area>.md` (4–8 files)
- `examples/notes-corpus/.kb/summaries/<area>/<topic>.md` (15–40 files)
- `examples/notes-corpus/.kb/.kb-state.json` (exists, contains current SHA)

Verify index budget:

```bash
for f in examples/notes-corpus/.kb/indexes/*.md; do
  wc -w "$f"
done
```

No file should exceed ~225 words (≈300 tokens). If any does, the ingest needs to split it — note this and fix in a follow-up rather than committing oversized indexes.

- [ ] **Step 3: Smoke-test with a query**

```
/kb-query examples/notes-corpus/ What approaches to context window management have I tried?
```

Expected behavior: agent reads `_root.md`, picks 2–3 area indexes, opens 2–4 summaries, returns an answer that names at least two approaches and at least one abandoned one. If the agent reads more than ~6 files or returns hallucinated content, the indexes need rework — fix before committing.

- [ ] **Step 4: Commit the pre-built KB**

```bash
git add examples/notes-corpus/.kb/
git commit -m "feat: commit pre-built .kb/ for notes-corpus demo"
```

---

## Task 4: Benchmark task definitions

**Files:**
- Create: `benchmarks/notes-corpus/tasks.md`
- Create: `benchmarks/notes-corpus/runs/.gitkeep`
- Create: `benchmarks/notes-corpus/traces/.gitkeep`
- Modify: `.gitignore`

- [ ] **Step 1: Create `benchmarks/notes-corpus/tasks.md`**

10 tasks covering the four required categories: concentrated-domain, cross-cutting, decision-tracing, negative.

```markdown
# notes-corpus benchmark tasks

Each task is run twice by `/kb-bench`: once with KB (`/kb-query`) and
once without (grep-only baseline). Compare the resulting traces in
`runs/` against the references in `traces/`.

---

## T01 — Cross-cutting concept lookup
**Question:** What approaches to context window management have I tried,
and which did I abandon?
**Why this task:** Forces traversal of multiple indexes (tool, paper,
project-log) and synthesis across kinds.
**Expected with KB:** _root.md → 2–3 area indexes → 3–5 summaries → answer
with concrete approaches and at least one abandoned one.
**Expected without KB:** grep finds many matches, agent likely opens
8–15 files, may miss the abandonment context.

---

## T02 — Concentrated domain query
**Question:** What do I know about MCP server development from these notes?
**Why this task:** Single domain, deep. Should resolve via one area index
and 2–3 summaries.

---

## T03 — Decision-tracing query
**Question:** Why did the casino-audit project switch away from RAG?
**Why this task:** Answer should reach a decision record via summary's
`## Key decisions` section.

---

## T04 — Negative query (correct answer is "not present")
**Question:** What does this corpus say about Kubernetes operators?
**Why this task:** Catches hallucination. Correct answer: "no notes on
this topic." Without KB, baseline may fabricate by stitching unrelated
mentions.

[continue with T05–T10 following the same structure, mixing the four
categories: concentrated-domain (×2), cross-cutting (×2 more),
decision-tracing (×1 more), negative (×1 more), plus 2 free-form
realistic questions]
```

Write all 10 tasks fully — no `[continue with ...]` placeholders in the actual file. The placeholder above is in this plan only; the engineer drafts the remaining task bodies following the format.

- [ ] **Step 2: Create `runs/` and `traces/` placeholder files**

```bash
mkdir -p benchmarks/notes-corpus/runs benchmarks/notes-corpus/traces
touch benchmarks/notes-corpus/runs/.gitkeep
touch benchmarks/notes-corpus/traces/.gitkeep
```

- [ ] **Step 3: Update `.gitignore`**

Append:

```
# benchmark fresh runs (only .gitkeep is tracked)
benchmarks/*/runs/*
!benchmarks/*/runs/.gitkeep
```

Verify:

```bash
echo "test" > benchmarks/notes-corpus/runs/foo.md
git status --short benchmarks/notes-corpus/runs/
# expect: no output (foo.md is ignored)
rm benchmarks/notes-corpus/runs/foo.md
```

- [ ] **Step 4: Commit**

```bash
git add benchmarks/ .gitignore
git commit -m "feat: define notes-corpus benchmark tasks and runs layout"
```

---

## Task 5: Record reference traces

**Files:**
- Create: `benchmarks/notes-corpus/traces/T01-with-kb.md` (and T01-without-kb, T02-with-kb, …, T10-without-kb — 20 files total)

This task is manual recording of expected behavior. The traces become the comparison baseline for fresh runs.

- [ ] **Step 1: Define the trace format**

Each trace file follows this exact shape:

```markdown
# T01 — with-kb

**Question:** [verbatim question from tasks.md]
**Mode:** with-kb (or without-kb)
**Recorded:** 2026-04-19

## Files opened (in order)
1. `examples/notes-corpus/.kb/indexes/_root.md`
2. `examples/notes-corpus/.kb/indexes/tools.md`
3. ...

## Tool calls
- Read × 5
- Grep × 0

## Tokens read from corpus
~2400

## Answer

[verbatim agent answer]
```

For `without-kb` traces: the "files opened" list will be longer and include `notes/` files; tool calls will include `Grep` and `Glob`.

- [ ] **Step 2: Run T01 with KB and record**

In Claude Code with plugin installed:

```
/kb-query examples/notes-corpus/ <T01 question>
```

Capture the file list, tool counts, and answer into `traces/T01-with-kb.md` using the format from Step 1.

- [ ] **Step 3: Run T01 without KB and record**

Use the same question but instruct the agent: "Answer using only Grep and Glob over `examples/notes-corpus/notes/`. Do not read anything under `.kb/`."

Capture into `traces/T01-without-kb.md`.

- [ ] **Step 4: Repeat for T02–T10**

Same pattern. 18 more files. This is mechanical but slow — budget ~2 hours.

- [ ] **Step 5: Commit traces in batches**

After T01–T05:

```bash
git add benchmarks/notes-corpus/traces/T0[1-5]-*.md
git commit -m "chore: record reference traces T01–T05"
```

After T06–T10:

```bash
git add benchmarks/notes-corpus/traces/T0[6-9]-*.md benchmarks/notes-corpus/traces/T10-*.md
git commit -m "chore: record reference traces T06–T10"
```

Two commits keep diffs reviewable.

---

## Task 6: `kb-bench` skill and command

**Files:**
- Create: `skills/kb-bench/SKILL.md`
- Create: `commands/kb-bench.md`

- [ ] **Step 1: Create `skills/kb-bench/SKILL.md`**

```markdown
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
```

- [ ] **Step 2: Create `commands/kb-bench.md`**

```markdown
---
description: Run benchmark tasks against examples/notes-corpus, comparing KB-driven retrieval with a grep-only baseline
argument-hint: optional task ID (e.g. T03), or empty for all tasks
---

Invoke the `kb-bench` skill with: `$ARGUMENTS`

If `$ARGUMENTS` is empty, run all benchmark tasks. Otherwise filter
to the supplied task ID.
```

- [ ] **Step 3: Verify by inspection**

Read both files. Cross-check against existing skills in `skills/` for frontmatter shape. Specifically:
- `name` matches directory name
- `description` includes English + Russian trigger phrases
- Command file is one-line wrapper

- [ ] **Step 4: Smoke-test against one task**

In Claude Code:

```
/kb-bench T01
```

Expected: produces two trace files in `benchmarks/notes-corpus/runs/<timestamp>/`, prints summary table comparing to references. If the comparison says "matches" or close (~10% drift on tokens), reference traces are calibrated correctly.

- [ ] **Step 5: Commit**

```bash
git add skills/kb-bench/ commands/kb-bench.md
git commit -m "feat: add kb-bench skill and command"
```

---

## Task 7: `kb-demo` skill and command

**Files:**
- Create: `skills/kb-demo/SKILL.md`
- Create: `commands/kb-demo.md`

- [ ] **Step 1: Create `skills/kb-demo/SKILL.md`**

```markdown
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
```

- [ ] **Step 2: Create `commands/kb-demo.md`**

```markdown
---
description: Guided entry to the built-in notes-corpus demo — try ingest, query, bench, and compare against a grep baseline
argument-hint: none (always opens the menu)
---

Invoke the `kb-demo` skill. Ignore any arguments — this skill always
opens the menu.
```

- [ ] **Step 3: Verify by inspection**

Same checks as Task 6 Step 3: frontmatter shape, trigger phrases include Russian, command is a thin wrapper.

- [ ] **Step 4: Smoke-test the menu**

In Claude Code:

```
/kb-demo
```

Expected: menu prints, agent waits for choice. Pick option 1, verify it lists corpus and `.kb/` contents.

- [ ] **Step 5: Commit**

```bash
git add skills/kb-demo/ commands/kb-demo.md
git commit -m "feat: add kb-demo orchestrator skill and command"
```

---

## Task 8: Update top-level docs

**Files:**
- Modify: `README.md`
- Modify: `README.ru.md`
- Modify: `.claude-plugin/plugin.json`

- [ ] **Step 1: Update `README.md` quickstart**

Read current `README.md`. In the Quickstart section, add a "Try it without setup" subsection before any "Apply to your own corpus" content:

```markdown
## Try it without setup

After installing the plugin, run:

`/kb-demo`

This opens a 5-option menu against a built-in 150-note synthetic corpus
in `examples/notes-corpus/`. You can inspect the structure, ask
questions through the KB, compare against a grep-only baseline, rebuild
the KB from scratch, or run the full benchmark suite.

For honest comparison numbers on fixed tasks:

`/kb-bench`

Runs the 10 benchmark questions in two modes (with KB / grep-only) and
prints a side-by-side table. Reference traces in
`benchmarks/notes-corpus/traces/` are the calibrated baseline.
```

Also add `kb-demo` and `kb-bench` to any "What's inside" / commands list.

- [ ] **Step 2: Mirror the update in `README.ru.md`**

Same content in Russian. Match the existing translation tone and structure.

- [ ] **Step 3: Bump `.claude-plugin/plugin.json` version**

Change `"version": "0.1.0"` to `"version": "0.2.0"` (minor bump — additive feature, no breaking changes to existing skills).

- [ ] **Step 4: Verify by reading**

Re-read both READMEs end-to-end. The Quickstart should land on `/kb-demo` as the easiest first step.

- [ ] **Step 5: Commit**

```bash
git add README.md README.ru.md .claude-plugin/plugin.json
git commit -m "docs: document /kb-demo and /kb-bench, bump to 0.2.0"
```

---

## Task 9: Final dogfood verification

**Files:** none (read-only verification)

- [ ] **Step 1: Reinstall the plugin from local**

In a fresh Claude Code session:

```
/plugin marketplace add olegvg/kb-for-agents
/plugin install kb-for-agents@kb-for-agents
```

(Or update if already installed.)

- [ ] **Step 2: Walk through `/kb-demo` end-to-end**

Pick each menu option in order, verify each works:
- Option 1 lists files
- Option 2 returns a coherent answer through `/kb-query`
- Option 3 produces a side-by-side comparison
- Option 4 confirms before rebuilding (cancel without rebuilding)
- Option 5 launches `/kb-bench` for all 10 tasks

- [ ] **Step 3: Run `/kb-bench` and check trace stability**

```
/kb-bench
```

Compare the freshly produced traces in `runs/<timestamp>/` against `traces/`. Expect "matches" or small drift on most tasks. If a task shows large drift (>30% file count difference), the reference trace was recorded under different conditions — re-record it as a fix.

- [ ] **Step 4: Final commit if any fixes were needed**

```bash
git add -p
git commit -m "fix: <specific issue found during dogfood>"
```

If no fixes needed, no commit.

---

## Self-review checklist (run before declaring done)

- [ ] Spec coverage: every section of `docs/specs/2026-04-19-architecture-design.md` is implemented or explicitly deferred
- [ ] No skill writes under another corpus's `.kb/` than the one it was invoked on
- [ ] `kb-demo` and `kb-bench` only touch `examples/notes-corpus/` and `benchmarks/notes-corpus/runs/`
- [ ] All commit messages follow repo style (`feat:`, `docs:`, `chore:`, lowercase, imperative)
- [ ] No oversized indexes (>300 tokens) in `examples/notes-corpus/.kb/indexes/`
- [ ] `README.md` and `README.ru.md` Quickstart points at `/kb-demo` as first step
- [ ] `plugin.json` version bumped to 0.2.0
