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
# inspect and edit without touching generation logic. Filled in Task 2.

TOOL_TOPICS: list[str] = []
PAPER_SOURCES: list[dict] = []
PROJECTS: list[dict] = []
CROSS_CUTTING: list[str] = [
    "context-window-management",
    "rag-vs-compiled-knowledge",
    "audit-of-legacy-codebases",
]


def main() -> None:
    rng = random.Random(SEED)
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    for kind, n in COUNTS.items():
        generate_kind(kind, n, rng)

    enforce_cross_cutting(rng)
    print(f"wrote {sum(COUNTS.values())} files to {OUT}")


def generate_kind(kind: str, n: int, rng: random.Random) -> None:
    raise NotImplementedError("Implemented in Task 2")


def enforce_cross_cutting(rng: random.Random) -> None:
    raise NotImplementedError("Implemented in Task 2")


def write_note(slug: str, kind: str, title: str, body: str,
               note_date: date, source: str | None = None) -> None:
    raise NotImplementedError("Implemented in Task 2")


if __name__ == "__main__":
    main()
