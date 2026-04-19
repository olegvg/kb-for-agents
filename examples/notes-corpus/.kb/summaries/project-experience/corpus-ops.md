# Corpus Operations Recipes

Shell and Python recipes for maintaining, validating, and querying the notes corpus.

## Available recipes

The ops notes (`notes/ops-000-list-kinds.md` through `notes/ops-014-count-by-kind.md`) provide 15 ready-to-use recipes. The unique recipe types (before the duplicate set at ops-010 onward):

**`ops-000-list-kinds.md`** — `grep -h "^kind:" notes/*.md | sort -u` — list all unique kind values. Run when the corpus has grown enough that you can't remember what kinds exist.

**`ops-001-find-empty-body.md`** — finds notes with empty body (only frontmatter). Run to detect accidentally-created stub notes.

**`ops-002-corpus-size-check.md`** — count total notes. Run before and after a batch import.

**`ops-003-validate-frontmatter.md`** — validate that required frontmatter fields (title, kind, date) are present in all notes. Run before a KB rebuild.

**`ops-004-count-by-kind.md`** — count notes per kind. Useful for spotting imbalance (e.g., 80 tool notes and 5 idea notes suggests ideas are being underrecorded).

**`ops-005-grep-cross-cutting.md`** — grep for cross-cutting topic keywords across all notes. Used during KB ingest Pass 1 to identify which topics appear across multiple files.

**`ops-006-determinism-check.md`** — verify that re-running the corpus generation produces the same output. Relevant for synthetic corpora like this demo.

**`ops-007-rebuild-title-index.md`** — rebuild a flat index of all note titles. Useful for quick navigation without reading the full KB.

**`ops-008-word-count-dist.md`** — word count distribution across notes. Run to check for outliers (very short notes may be stubs; very long notes may need splitting).

**`ops-009-topic-coverage-py.md`** — Python script to check that all confirmed cross-cutting topics have at least one note. Run before publishing a corpus to verify coverage.

## References

- Source: `notes/ops-000-list-kinds.md` through `notes/ops-009-topic-coverage-py.md` (and duplicates ops-010 through ops-014)
