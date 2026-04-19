# T10 — without-kb

**Question:** What scripts or shell recipes have I documented for checking, validating, or counting the notes corpus — things like finding empty notes, counting kinds, or checking frontmatter?
**Mode:** without-kb
**Recorded:** 2026-04-19

## Files opened (in order)
1. `examples/notes-corpus/notes/ops-000-list-kinds.md`
2. `examples/notes-corpus/notes/ops-001-find-empty-body.md`
3. `examples/notes-corpus/notes/ops-002-corpus-size-check.md`
4. `examples/notes-corpus/notes/ops-003-validate-frontmatter.md`
5. `examples/notes-corpus/notes/ops-004-count-by-kind.md`
6. `examples/notes-corpus/notes/ops-005-grep-cross-cutting.md`
7. `examples/notes-corpus/notes/ops-006-determinism-check.md`
8. `examples/notes-corpus/notes/ops-007-rebuild-title-index.md`
9. `examples/notes-corpus/notes/ops-008-word-count-dist.md`
10. `examples/notes-corpus/notes/ops-009-topic-coverage-py.md`

## Tool calls
- Read × 10
- Grep × 2
- Glob × 1

## Tokens read from corpus
~1200  
(Glob for ops-*.md lists 15 files; agent reads unique 10 ops files at ~300 bytes avg ≈ 1200 tokens; skips 5 duplicates ops-010 through ops-014)

## Answer

Glob for `ops-*.md` in `notes/` returns 15 files (ops-000 through ops-014, where ops-010 through ops-014 are duplicates of ops-000 through ops-004). Reading the unique 10 recipes: `ops-000` — `grep -h "^kind:" notes/*.md | sort -u` to list unique kinds; `ops-001` — awk script to find notes with empty body; `ops-002` — count total notes with `ls notes/*.md | wc -l`; `ops-003` — validate required frontmatter fields (title, kind, date); `ops-004` — count notes per kind; `ops-005` — grep for cross-cutting topic keywords; `ops-006` — determinism check for synthetic corpus generation; `ops-007` — rebuild flat title index; `ops-008` — word count distribution; `ops-009` — Python script for topic coverage. Without the KB the agent reads 10 individual files to compile this catalog — correct and complete, but takes 10 reads and a Glob versus 3 reads for the KB path. The KB advantage is meaningful here: the `corpus-ops` summary distills all 10 recipes into one structured prose catalog, avoiding the need to read each raw note and mentally aggregate them.
