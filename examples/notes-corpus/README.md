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
