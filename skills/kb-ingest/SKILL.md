---
name: kb-ingest
description: Use when building a fresh three-layer knowledge base for a corpus. Walks the corpus, groups files by semantic domain, writes summaries and indexes into .kb/. Triggers on "ingest the corpus", "build the knowledge base", "создать kb", "сгенерировать базу знаний".
---

# kb-ingest — Build a Three-Layer Knowledge Base

## When to use

User points you at a corpus (codebase, notes archive, docs folder) and wants a fresh `.kb/` built from scratch. One-shot operation.

If `.kb/` already exists at the target path, STOP. Ask the user whether to overwrite, and get explicit confirmation before proceeding.

## Input

- **Corpus root path** — argument from the user. If missing, ask for it before starting. Default is not the current directory unless the user confirms.

## Output (created inside the corpus root)

```
.kb/
├── indexes/_root.md
├── indexes/<area>.md       (one per semantic domain)
├── summaries/<area>/overview.md
├── summaries/<area>/<leaf>.md
├── decisions/              (empty directory — populated only by /kb-distill)
└── .kb-state.json
```

## Default exclusions

Timestamp-based journals and vendored directories are excluded by default. These are not knowledge — they are operational noise that muddles semantic grouping. Never ingest:

- `docs/plans/**`, `docs/specs/**` (dated planning artifacts — distill via `/kb-distill` instead)
- `**/CHANGELOG.md` (git log is authoritative)
- `node_modules/**`, `.venv/**`, `target/**`, `build/**`, `dist/**`, `.git/**`
- `temp/**`, `tmp/**`, any directory whose name is a date/timestamp pattern at the corpus root

The user may override with `--include <path>` when they genuinely want a normally-excluded path in the KB.

## Workflow

Ingest runs in **three passes**. This structure is deliberate: it keeps the main agent's context bounded regardless of corpus size, and it parallelizes the expensive pass. Do NOT collapse it into a single pass even on small corpora — the workflow is the teaching.

### Pass 1 — Survey and group (main agent, light context)

Walk the corpus at a high level. Do NOT read full file contents in this pass.

- `ls <corpus-root>` for the top-level layout.
- Read README if present.
- For each directory worth sampling, read only **file headers**: first 30–50 lines, docstrings, imports, exported names.
- Cluster files into semantic domains (see Grouping, below). Produce a draft of `_root.md` in memory — list of areas + which files belong to each.

Context budget for Pass 1: roughly 5–10% of the corpus. If you catch yourself opening full file bodies in Pass 1, stop — that's Pass 2's job.

#### Grouping (the critical step)

Group files by **what a user would ask about them**, not by where they sit in the filesystem.

- Good: "auth", "billing", "search-indexing", "ops-runbooks".
- Bad: "src", "tests", "utils", "scripts" (these are directories, not domains).

Grouping rule: a domain is a set of files someone would want to understand together when working on a task. A "billing" domain pulls code from `src/api/billing.ts`, `src/db/billing_schema.sql`, `docs/billing-model.md`, and `tests/billing.spec.ts` — across four directories — because they answer one class of question.

Name each domain with a short kebab-case slug. 4–10 domains is typical. Fewer than 3 means you're under-segmenting; more than 15 means over-segmenting.

### Pass 2 — Deep ingest per domain (dispatch subagents)

For each domain identified in Pass 1, dispatch a subagent via the Task tool. The subagent starts with a fresh context and sees only its slice of the corpus.

Subagent prompt shape (adapt wording, keep the contract):

```
Domain: <area-slug>
Files in this domain:
  - <path/to/file1>
  - <path/to/file2>
  ...
Task:
  1. Read the listed files.
  2. Write .kb/summaries/<area-slug>/overview.md — orientation for the domain.
  3. Write one leaf file per distinct topic at .kb/summaries/<area-slug>/<topic>.md.
  4. Follow templates/summary.template.md for file shape.
  5. Return a 200-word brief: area name, list of leaf files created, one-line description of each.
Rules:
  - One topic per leaf file.
  - Prose, not bullet dumps. Cite file paths and line numbers.
  - Mermaid where a diagram beats prose.
  - Do NOT write to .kb/indexes/ — the main agent handles indexes in Pass 3.
```

Dispatch subagents in parallel where corpus size permits — one per domain.

You (main agent) do NOT read corpus files during Pass 2. You hold only the briefs returned by subagents. This is the key context-window guarantee of the pattern.

### Pass 3 — Index assembly (main agent, holds only briefs)

Based on the briefs returned from Pass 2:

#### 3a. Write area indexes (Layer 3)

For each domain, create `.kb/indexes/<area>.md` following `templates/index.template.md`.

- Maximum 300 tokens. Measure. If you overshoot, split the area or drop signposts.
- Sections: what the area covers, when to enter it, list of leaves with one-line descriptions, optional "see also".

#### 3b. Write `_root.md`

Create `.kb/indexes/_root.md` following `templates/_root.template.md`.

- Maximum 300 tokens.
- One line per area: pointer + one-sentence description.
- Include navigation rules inline so an agent reading it knows the conventions.

#### 3c. Create empty `decisions/` directory

```bash
mkdir -p <corpus-root>/.kb/decisions
```

This is empty on fresh ingest. It is populated by `/kb-distill` when the user asks to extract a decision record from a completed plan. Never populate it during ingest — ingest looks at current state, not history.

#### 3d. Write `.kb-state.json`

Capture the current corpus git SHA and an ISO-8601 UTC timestamp:

```bash
git -C <corpus-root> rev-parse HEAD
date -u +"%Y-%m-%dT%H:%M:%SZ"
```

Write to `.kb/.kb-state.json` with `schema_version: 1`. Shape: see `templates/.kb-state.template.json`.

If the corpus is not a git repo, set `last_linted_sha` to the string `"no-git"` and note this to the user — `/kb-lint` and `/kb-check-drift` will not work until the corpus is in git.

### Fallback when subagents are unavailable

If the caller's environment cannot dispatch subagents, run ingest iteratively across separate Claude Code sessions, one per domain: `/kb-ingest <domain-path>`. Each session does a narrow Pass 2 for one domain and writes its own area index. A final session runs Pass 3 to write `_root.md` and `.kb-state.json`. Slower and less clean than the subagent path, but works.

## Discipline

- **Index token budget is 300 tokens, not "about 300".** Enforce on write. If you overshoot, split or trim.
- **Indexes contain signposts, not content.** No prose explanations in index files. If you need prose, it belongs in a summary.
- **Semantic grouping beats structural grouping.** When in doubt, ask: "would a user ask about these files together?" — not "are these files in the same folder?".

## Common failure modes

- **Ingesting by directory** — produces indexes that mirror `ls` and add no navigational value. Re-group by task surface.
- **Overlong indexes** — usually the area should be split into two.
- **Empty summaries** — if a leaf has nothing to say beyond a pointer, it's an index entry, not a summary.
- **Reading full file bodies in Pass 1 or Pass 3** — blows the main agent's context. Pass 1 reads headers only; Pass 3 reads only briefs. All full-file reading happens inside Pass 2 subagents.
- **Running Pass 2 sequentially on a large corpus** — slow and unnecessary. Dispatch subagents in parallel; each holds its own context.
- **Using auto-compact instead of the three-pass structure** — compact is lossy and uncontrolled. The three passes exist precisely so compaction is never needed.

## References

- Pattern rationale: [docs/concept.md](../../docs/concept.md)
- Navigation rules: [docs/navigation-rules.md](../../docs/navigation-rules.md)
- Templates: [templates/](../../templates/)
