# T10 — with-kb

**Question:** What scripts or shell recipes have I documented for checking, validating, or counting the notes corpus — things like finding empty notes, counting kinds, or checking frontmatter?
**Mode:** with-kb
**Recorded:** 2026-04-19

## Files opened (in order)
1. `examples/notes-corpus/.kb/indexes/_root.md`
2. `examples/notes-corpus/.kb/indexes/project-experience.md`
3. `examples/notes-corpus/.kb/summaries/project-experience/corpus-ops.md`

## Tool calls
- Read × 3
- Grep × 0
- Glob × 0

## Tokens read from corpus
~1230  
(_root.md 404 + project-experience index 321 + corpus-ops summary 509)

## Answer

The KB exposes 10 distinct ops recipes (plus duplicates ops-010 through ops-014) in the `project-experience/corpus-ops` summary, all sourced from `notes/ops-000-list-kinds.md` through `notes/ops-009-topic-coverage-py.md`. The catalog: (1) `ops-000` — `grep -h "^kind:" notes/*.md | sort -u` lists all unique kind values; (2) `ops-001` — awk recipe finds notes with empty body (only frontmatter), for detecting stub notes; (3) `ops-002` — count total notes, run before and after batch imports; (4) `ops-003` — validate that required frontmatter fields (title, kind, date) are present in all notes, run before KB rebuild; (5) `ops-004` — count notes per kind, spot corpus imbalance; (6) `ops-005` — grep for cross-cutting topic keywords across all notes, used during KB ingest Pass 1; (7) `ops-006` — determinism check, verify re-running corpus generation produces same output; (8) `ops-007` — rebuild flat index of all note titles for quick navigation; (9) `ops-008` — word count distribution, detect outlier notes (stubs or overly long notes needing splitting); (10) `ops-009` — Python script checking that all confirmed cross-cutting topics have at least one note. The KB surfaces this as a coherent catalog in a single read; no need to grep individual ops files.
