---
description: Build a fresh three-layer KB for a corpus (default: current directory)
argument-hint: optional path to corpus root
---

Invoke the `kb-ingest` skill. The target corpus is `$ARGUMENTS` if provided, otherwise the current working directory. If the argument is empty, confirm with the user before proceeding to build `.kb/` in the cwd.
