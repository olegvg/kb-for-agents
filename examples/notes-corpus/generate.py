#!/usr/bin/env python3
"""Generate a synthetic notes corpus for the kb-for-agents demo.

Stdlib-only. Deterministic given SEED. Writes .md files under notes/.
"""
import re
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

# ---------------------------------------------------------------------------
# Seed pools
# ---------------------------------------------------------------------------

TOOL_TOPICS: list[str] = [
    "Claude Code slash commands",
    "MCP server setup and configuration",
    "subagent dispatching patterns",
    "context-window-management strategies",
    "prompt caching with the Anthropic SDK",
    "hook-driven automation in Claude Code",
    "rag-vs-compiled-knowledge tradeoffs",
    "agent memory architectures",
    "audit-of-legacy-codebases with AI assistance",
    "multi-turn conversation design",
    "tool-use JSON schema design",
    "streaming responses in Claude API",
    "plugin authoring for Claude Code",
    "CLAUDE.md project instructions",
    "extended thinking mode usage",
    "parallel subagent orchestration",
    "cost management for long agent runs",
    "diff-based code editing with agents",
    "semantic search over notes corpus",
    "embeddings for knowledge retrieval",
    "hybrid RAG pipelines",
    "agent loop design patterns",
    "error recovery in multi-step agents",
    "structured output extraction",
    "rate-limit handling in agent pipelines",
    "prompt injection defence patterns",
    "Claude Code keybindings customisation",
    "environment variable management in agents",
    "self-evaluation and reflection prompts",
    "few-shot example selection strategies",
    "chain-of-thought prompting",
    "knowledge graph construction with LLMs",
    "codebase summarisation for agents",
    "test-driven development with AI pair",
    "PR review automation with Claude",
]

PAPER_SOURCES: list[dict] = [
    {
        "title": "Attention Is All You Need",
        "url": "https://arxiv.org/abs/1706.03762",
    },
    {
        "title": "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks",
        "url": "https://arxiv.org/abs/2005.11401",
    },
    {
        "title": "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models",
        "url": "https://arxiv.org/abs/2201.11903",
    },
    {
        "title": "Toolformer: Language Models Can Teach Themselves to Use Tools",
        "url": "https://arxiv.org/abs/2302.04761",
    },
    {
        "title": "ReAct: Synergizing Reasoning and Acting in Language Models",
        "url": "https://arxiv.org/abs/2210.03629",
    },
    {
        "title": "Self-Consistency Improves Chain of Thought Reasoning in Language Models",
        "url": "https://arxiv.org/abs/2203.11171",
    },
    {
        "title": "LLM-based Autonomous Agent Survey (synthetic)",
        "url": "https://arxiv.org/abs/2308.11432",
    },
    {
        "title": "HyDE: Hypothetical Document Embeddings for Zero-Shot Dense Retrieval",
        "url": "https://arxiv.org/abs/2212.10496",
    },
    {
        "title": "Constitutional AI: Harmlessness from AI Feedback",
        "url": "https://arxiv.org/abs/2212.08073",
    },
    {
        "title": "Large Language Models as Tool Makers",
        "url": "https://arxiv.org/abs/2305.17126",
    },
    {
        "title": "Tree of Thoughts: Deliberate Problem Solving with Large Language Models",
        "url": "https://arxiv.org/abs/2305.10601",
    },
    {
        "title": "Reflexion: Language Agents with Verbal Reinforcement Learning",
        "url": "https://arxiv.org/abs/2303.11366",
    },
    {
        "title": "Software Engineering with Large Language Models: Survey (synthetic)",
        "url": "https://arxiv.org/abs/2308.00001",
    },
    {
        "title": "Prompt Injection Attacks and Defences in LLM-Integrated Applications (synthetic)",
        "url": "https://arxiv.org/abs/2310.12815",
    },
    {
        "title": "FLARE: Active Retrieval Augmented Generation",
        "url": "https://arxiv.org/abs/2305.06983",
    },
    {
        "title": "Long-Context Language Models and Context Window Management (synthetic)",
        "url": "https://arxiv.org/abs/2401.00001",
    },
    {
        "title": "Audit of Legacy Codebases Using Static Analysis and LLMs (synthetic)",
        "url": "https://arxiv.org/abs/2402.00001",
    },
    {
        "title": "RAG vs Fine-tuning: Pipelines, Tradeoffs, and a Case Study (synthetic)",
        "url": "https://arxiv.org/abs/2401.18059",
    },
    {
        "title": "Voyager: An Open-Ended Embodied Agent with Large Language Models",
        "url": "https://arxiv.org/abs/2305.16291",
    },
    {
        "title": "AgentBench: Evaluating LLMs as Agents",
        "url": "https://arxiv.org/abs/2308.03688",
    },
    {
        "title": "Generative Agents: Interactive Simulacra of Human Behavior",
        "url": "https://arxiv.org/abs/2304.03442",
    },
    {
        "title": "Cognitive Architectures for Language Agents",
        "url": "https://arxiv.org/abs/2309.02427",
    },
]

PROJECTS: list[dict] = [
    {"slug": "kb-for-agents", "started": date(2025, 11, 3)},
    {"slug": "personal-brand-ai", "started": date(2025, 9, 15)},
    {"slug": "mcp-telegram-bot", "started": date(2026, 1, 7)},
]

CROSS_CUTTING: list[str] = [
    "context-window-management",
    "rag-vs-compiled-knowledge",
    "audit-of-legacy-codebases",
]

# ---------------------------------------------------------------------------
# Body fragment pools (≥6 per kind)
# ---------------------------------------------------------------------------

TOOL_OPENS: list[str] = [
    "I spent the last few days experimenting with {topic} and came away with a clearer picture than when I started.",
    "After a week of using {topic} in production work, I have notes worth writing down.",
    "My first serious session with {topic} surfaced patterns I hadn't anticipated.",
    "I kept putting off a proper look at {topic}, but a failing deadline pushed me into it.",
    "Three hours in with {topic} and I already had opinions. Here's what I found.",
    "I tried {topic} on a real project rather than a toy example, which made all the difference.",
    "Picked up {topic} after seeing it mentioned twice in the same week. Decided it warranted a proper try.",
]

TOOL_WORKED: list[str] = [
    "The iteration speed was noticeably faster once I stopped second-guessing the output.",
    "Incremental commits kept the feedback loop tight, which prevented runaway context growth.",
    "Breaking the task into single-responsibility subtasks made each agent invocation predictable.",
    "I found that explicit constraints in the prompt outperformed general instructions every time.",
    "Giving the model a concrete example before asking for the real thing cut hallucinations significantly.",
    "Treating each tool call as a unit test — verify input, verify output — kept drift in check.",
    "Logging every agent turn to a file let me spot the exact step where things went sideways.",
    "Keeping CLAUDE.md up to date with project-specific decisions saved me repeated explanatory preambles.",
]

TOOL_DIDNT: list[str] = [
    "Asking for too much in a single prompt consistently led to shallow, generic output.",
    "Ignoring context-window limits mid-session caused silent truncation that was hard to diagnose.",
    "Over-relying on the model's memory of earlier turns produced subtle inconsistencies by step four or five.",
    "Skipping the 'what-not-to-do' section of the prompt left obvious failure modes unguarded.",
    "I wasted time when I let the model pick its own tools without providing a bounded tool list.",
    "Mixing two unrelated concerns in one subagent call muddied the output and doubled the review time.",
    "Not pinning the model version meant a surprise behavior change after a silent rollout.",
    "Asking for explanations and code in the same response reliably produced worse code.",
]

TOOL_CLOSERS: list[str] = [
    "I'll keep this in the rotation and revisit after a month to see if the rough edges smooth out.",
    "The setup cost is real, but it pays back on the third use. Probably worth it.",
    "Would recommend to anyone already comfortable with the basics — not a first step.",
    "Going to write up a more structured experiment next time so I have numbers, not just vibes.",
    "Still forming a verdict. What I have is enough to keep experimenting.",
    "The pattern is clear enough that I've already folded it into my default workflow.",
]

PAPER_TAKEAWAYS: list[str] = [
    "The core claim held up better than I expected when I applied it to my own setup.",
    "Several ideas here transfer directly to agent pipeline design, even though that wasn't the paper's framing.",
    "The evaluation methodology is worth borrowing, separate from the results.",
    "I had heard the headline finding cited dozens of times, but reading the actual method section changed my interpretation.",
    "The ablation tables are where the real insight lives — the abstract undersells the nuance.",
    "This reframed how I think about the knowledge freshness problem in retrieval systems.",
    "The failure cases section was more useful to me than the success cases.",
    "I disagreed with one assumption in the setup, but the conclusions are robust enough to survive it.",
]

PAPER_APPLICATIONS: list[str] = [
    "I can see a direct application to how I structure context for long agent sessions.",
    "The technique maps cleanly onto the notes-corpus ingestion pipeline I'm designing.",
    "This would pair well with a compiled-knowledge layer to reduce retrieval latency.",
    "The approach suggests a way to audit legacy code systematically rather than heuristically.",
    "Applying this to context-window management could cut token usage by a meaningful fraction.",
    "The pattern shows up in how RAG-vs-compiled-knowledge tradeoffs should actually be evaluated.",
    "I'll try the main heuristic on a real codebase next week to see if it generalises.",
]

LOG_OPENS: list[str] = [
    "Quick log entry before I lose the thread.",
    "End-of-day notes on what actually happened.",
    "Picking up from yesterday's session.",
    "Unblocked this morning after sleeping on the problem.",
    "Short entry — context is fresher than it will be tomorrow.",
    "Checkpoint before switching to a different part of the codebase.",
    "Writing this mid-session because the insight is too perishable to save for later.",
]

LOG_MIDDLES: list[str] = [
    "The piece that was blocking me turned out to be a wrong assumption about the data shape, not a code bug.",
    "Spent the first hour on setup, which felt wasteful but probably saved three hours of misaligned effort.",
    "The schema change rippled further than expected — four files needed touching, not one.",
    "I leaned on the agent more than planned and it held up, which was a pleasant surprise.",
    "Discovered that the bottleneck was context-window-management rather than model capability.",
    "The difference between RAG-vs-compiled-knowledge retrieval approaches showed up in latency, not quality.",
    "Found three undocumented behaviors in the legacy module — classic audit-of-legacy-codebases territory.",
    "The integration test caught something the unit test missed, which is the right order of events.",
    "Refactored the core loop to be side-effect-free, which made the agent calls trivially testable.",
    "The PR review surfaced a naming inconsistency I'd normalised to invisible.",
]

LOG_CLOSERS: list[str] = [
    "Tomorrow: finish the edge-case handling and write a regression test.",
    "Next session: wire up the end-to-end test and do a timing run.",
    "Leaving a TODO at line 47 — not forgotten, just deferred.",
    "Good enough to commit. Will revisit after the next integration test run.",
    "Enough for today. The hard part is done.",
    "Closing the loop on this task. Moving to the next one in the morning.",
]

IDEA_SEEDS: list[str] = [
    "What if the notes corpus itself was the training signal for personalising retrieval?",
    "Haven't figured out how to make context-window-management automatic without losing control.",
    "There might be a simpler boundary between RAG-vs-compiled-knowledge than anyone has drawn yet.",
    "What if audit-of-legacy-codebases could be done incrementally, one module per agent session?",
    "I keep wondering whether compiled knowledge degrades slower than retrieval indexes.",
    "There's probably a way to derive the right chunk size from the query distribution, not from intuition.",
    "What if the agent's own uncertainty estimates could drive when to fall back to retrieval?",
    "Haven't tested whether a short compiled summary outperforms a long retrieved passage at inference time.",
    "The boundary between a tool and a subagent feels arbitrary — maybe it shouldn't be a binary.",
    "What if every note had a confidence score attached, updated each time retrieval succeeded or failed?",
    "There's an open question about whether context-window limits should be managed by the agent or the harness.",
    "I suspect the right abstraction for knowledge bases hasn't been invented yet.",
    "What if the 'fresh vs stale' dimension of knowledge was first-class in the query interface?",
    "Haven't worked out how to make the audit trail of an agent session queryable after the fact.",
]

IDEA_CLOSERS: list[str] = [
    "Not ready to build this yet. Needs more time on the shelf.",
    "Would take a weekend prototype to know if this is real or just appealing.",
    "Leaving this open. Might come back after the current project settles.",
    "Probably worth a focused experiment before committing to a direction.",
    "Too many unknowns to plan around. Noting it anyway.",
    "Filing this under 'interesting if true'. Needs evidence.",
]

OPS_CONTEXTS: list[str] = [
    "Useful when the notes directory has grown beyond what a single grep can survey cleanly.",
    "Run this before each release to catch any files that drifted out of schema.",
    "Handy for debugging context-window-management issues in long agent sessions.",
    "This one-liner saved me twenty minutes of manual checking.",
    "Part of my standard audit-of-legacy-codebases checklist.",
    "Use this to verify that retrieval indexes are consistent with the source notes.",
    "Helps when deciding between RAG-vs-compiled-knowledge for a specific corpus size.",
    "Quick sanity check after any bulk file operation.",
    "Essential before handing the corpus to an agent that expects a specific schema.",
    "Pairs well with a pre-commit hook to keep the notes directory clean.",
]

OPS_COMMANDS: list[str] = [
    """\
```bash
# Count files by kind (front matter)
grep -rl "^kind:" notes/ | xargs grep -h "^kind:" | sort | uniq -c | sort -rn
```""",
    """\
```bash
# Validate YAML front matter has required fields
for f in notes/*.md; do
  python3 -c "
import sys, re
txt = open('$f').read()
fm = re.search(r'^---\\n(.*?)\\n---', txt, re.S)
if not fm: sys.exit('missing front matter: $f')
block = fm.group(1)
for field in ('title', 'kind', 'date'):
    if field + ':' not in block:
        sys.exit(f'missing {field}: $f')
"
done && echo "all ok"
```""",
    """\
```bash
# Find notes mentioning a cross-cutting topic
grep -li "context-window-management" notes/*.md
```""",
    """\
```bash
# Check corpus size
ls notes/*.md | wc -l
```""",
    """\
```bash
# List all unique kind values
grep -h "^kind:" notes/*.md | sort -u
```""",
    """\
```bash
# Find notes without a body (only front matter)
awk '/^---/{c++} c==2{body=1} END{if(!body) print FILENAME}' notes/*.md
```""",
    """\
```bash
# Quick word-count distribution
wc -w notes/*.md | sort -n | tail -20
```""",
    """\
```bash
# Rebuild index of note titles
grep -h "^title:" notes/*.md | sed 's/^title: //' | sort > /tmp/note-titles.txt
wc -l /tmp/note-titles.txt
```""",
    """\
```python
# Detect cross-cutting topic coverage across kinds
import re
from pathlib import Path

topics = ["context-window-management", "rag-vs-compiled-knowledge", "audit-of-legacy-codebases"]
notes = list(Path("notes").glob("*.md"))

for topic in topics:
    kinds = set()
    for note in notes:
        txt = note.read_text().lower()
        if topic in txt:
            m = re.search(r"^kind:\\s*(\\S+)", txt, re.M)
            if m:
                kinds.add(m.group(1))
    print(f"{topic}: {sorted(kinds)}")
```""",
    """\
```bash
# Git diff to verify determinism after re-running generator
python3 generate.py && git diff --stat notes/
```""",
]

OPS_TOPICS: list[str] = [
    "count-by-kind",
    "validate-frontmatter",
    "grep-cross-cutting",
    "corpus-size-check",
    "list-kinds",
    "find-empty-body",
    "word-count-dist",
    "rebuild-title-index",
    "topic-coverage-py",
    "determinism-check",
]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

BASE_DATE = date(2025, 8, 1)
END_DATE = date(2026, 4, 19)


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return text[:40]


def random_date(rng: random.Random, start: date = BASE_DATE, end: date = END_DATE) -> date:
    delta = (end - start).days
    return start + timedelta(days=rng.randint(0, delta))


def write_note(slug: str, kind: str, title: str, body: str,
               note_date: date, source: str | None = None) -> None:
    lines = ["---", f"title: {title}", f"kind: {kind}", f"date: {note_date.isoformat()}"]
    if source:
        lines.append(f"source: \"{source}\"")
    lines += ["---", "", body, ""]
    (OUT / f"{slug}.md").write_text("\n".join(lines))


# ---------------------------------------------------------------------------
# Per-kind generators
# ---------------------------------------------------------------------------

def gen_tool(n: int, rng: random.Random) -> None:
    topics = list(TOOL_TOPICS)
    rng.shuffle(topics)
    for i in range(n):
        topic = topics[i % len(topics)]
        title = f"Using {topic}: notes and reflections"
        slug = slugify(f"tool-{i:03d}-{topic}")

        opener = rng.choice(TOOL_OPENS).format(topic=topic)
        worked = rng.sample(TOOL_WORKED, k=rng.randint(2, 4))
        didnt = rng.sample(TOOL_DIDNT, k=rng.randint(2, 3))
        closer = rng.choice(TOOL_CLOSERS)

        paras = [opener]
        paras.append("What worked: " + " ".join(worked))
        paras.append("What didn't: " + " ".join(didnt))
        paras.append(closer)

        # Occasionally add extra paragraph for length variety
        if rng.random() < 0.4:
            extra = rng.choice(TOOL_OPENS).format(topic=rng.choice(TOOL_TOPICS))
            paras.insert(rng.randint(1, len(paras) - 1), extra)

        body = "\n\n".join(paras)
        note_date = random_date(rng)
        write_note(slug, "tool", title, body, note_date)


def gen_paper(n: int, rng: random.Random) -> None:
    sources = list(PAPER_SOURCES)
    rng.shuffle(sources)
    for i in range(n):
        paper = sources[i % len(sources)]
        title = f"Reading notes: {paper['title']}"
        title_slug = slugify(f"paper-{i:03d}-{paper['title']}")

        takeaway = rng.sample(PAPER_TAKEAWAYS, k=rng.randint(2, 3))
        application = rng.sample(PAPER_APPLICATIONS, k=rng.randint(1, 3))

        opener = f"Just finished reading \"{paper['title']}\" ({paper['url']})."
        paras = [opener]
        paras.extend(takeaway)
        paras.extend(application)

        # 4–6 sentence constraint: merge into fewer paragraphs
        body_sentences = " ".join(paras[1:])
        body = paras[0] + "\n\n" + body_sentences

        note_date = random_date(rng)
        write_note(title_slug, "paper", title, body, note_date, source=paper["url"])


def gen_project_log(n: int, rng: random.Random) -> None:
    # Distribute evenly across 3 projects
    assignments = []
    per_project = n // len(PROJECTS)
    remainder = n % len(PROJECTS)
    for idx, project in enumerate(PROJECTS):
        count = per_project + (1 if idx < remainder else 0)
        assignments.extend([project] * count)
    rng.shuffle(assignments)

    used_slugs: set[str] = set()
    for project in assignments:
        start = project["started"]
        max_offset = (END_DATE - start).days
        offset = rng.randint(0, max_offset)
        entry_date = start + timedelta(days=offset)

        slug = f"log-{project['slug']}-{entry_date.isoformat()}"
        # Handle rare date collision
        suffix = 0
        base_slug = slug
        while slug in used_slugs:
            suffix += 1
            slug = f"{base_slug}-{suffix}"
        used_slugs.add(slug)

        title = f"Project log: {project['slug']} — {entry_date.isoformat()}"

        opener = rng.choice(LOG_OPENS)
        middle = rng.sample(LOG_MIDDLES, k=rng.randint(2, 4))
        closer = rng.choice(LOG_CLOSERS)

        paras = [opener] + middle + [closer]
        body = "\n\n".join(paras)
        write_note(slug, "project-log", title, body, entry_date)


def gen_idea(n: int, rng: random.Random) -> None:
    seeds = list(IDEA_SEEDS)
    rng.shuffle(seeds)
    for i in range(n):
        seed = seeds[i % len(seeds)]
        title = f"Idea: {seed[:60].rstrip()}"
        slug = slugify(f"idea-{i:03d}-{seed[:30]}")

        paras = [seed]
        extra_count = rng.randint(0, 2)
        for _ in range(extra_count):
            paras.append(rng.choice(IDEA_SEEDS))
        paras.append(rng.choice(IDEA_CLOSERS))

        body = "\n\n".join(paras)
        note_date = random_date(rng)
        write_note(slug, "idea", title, body, note_date)


def gen_ops(n: int, rng: random.Random) -> None:
    combined = list(zip(OPS_TOPICS, OPS_COMMANDS))
    rng.shuffle(combined)
    for i in range(n):
        topic_str, command = combined[i % len(combined)]
        title = f"Ops recipe: {topic_str.replace('-', ' ')}"
        slug = slugify(f"ops-{i:03d}-{topic_str}")

        context = rng.choice(OPS_CONTEXTS)
        body = f"{context}\n\n{command}"
        note_date = random_date(rng)
        write_note(slug, "ops", title, body, note_date)


# ---------------------------------------------------------------------------
# Cross-cutting enforcement
# ---------------------------------------------------------------------------

KIND_MAP = {
    "tool": gen_tool,
    "paper": gen_paper,
    "project-log": gen_project_log,
    "idea": gen_idea,
    "ops": gen_ops,
}


def scan_topic_presence(topic: str) -> dict[str, list[Path]]:
    """Return mapping kind -> list of files where topic appears (case-insensitive)."""
    result: dict[str, list[Path]] = {}
    for note_file in OUT.glob("*.md"):
        text = note_file.read_text().lower()
        if topic.lower() in text:
            # Extract kind from front matter
            m = re.search(r"^kind:\s*(\S+)", note_file.read_text(), re.M)
            if m:
                kind = m.group(1)
                result.setdefault(kind, []).append(note_file)
    return result


def _rewrite_note_with_topic(note_file: Path, topic: str, rng: random.Random) -> None:
    """Inject the cross-cutting topic into an existing note's title and body."""
    text = note_file.read_text()

    # Parse front matter
    fm_match = re.match(r"^---\n(.*?)\n---\n(.*)", text, re.S | re.DOTALL)
    if not fm_match:
        return
    fm_block = fm_match.group(1)
    body = fm_match.group(2).strip()

    # Update title
    topic_phrase = topic.replace("-", " ")
    old_title_m = re.search(r"^title: (.+)$", fm_block, re.M)
    if old_title_m:
        old_title = old_title_m.group(1)
        new_title = f"{old_title} [re: {topic_phrase}]"
        fm_block = fm_block.replace(old_title_m.group(0), f"title: {new_title}")

    # Inject topic sentence into body
    injection = (
        f"One angle I keep coming back to is {topic_phrase}. "
        f"It keeps showing up in different forms across my notes."
    )
    body = body + "\n\n" + injection

    # Extract other fields
    kind_m = re.search(r"^kind:\s*(\S+)", fm_block, re.M)
    date_m = re.search(r"^date:\s*(\S+)", fm_block, re.M)
    src_m = re.search(r'^source:\s*"?([^"\n]+)"?', fm_block, re.M)

    kind = kind_m.group(1) if kind_m else "unknown"
    note_date_str = date_m.group(1) if date_m else END_DATE.isoformat()
    note_date = date.fromisoformat(note_date_str)
    source = src_m.group(1) if src_m else None

    # Extract title from updated fm_block
    title_m = re.search(r"^title: (.+)$", fm_block, re.M)
    title = title_m.group(1) if title_m else "Untitled"

    # Overwrite file using write_note logic
    lines = ["---", f"title: {title}", f"kind: {kind}", f"date: {note_date.isoformat()}"]
    if source:
        lines.append(f"source: \"{source}\"")
    lines += ["---", "", body, ""]
    note_file.write_text("\n".join(lines))


def enforce_cross_cutting(rng: random.Random) -> None:
    all_kinds = list(COUNTS.keys())

    for topic in CROSS_CUTTING:
        presence = scan_topic_presence(topic)
        covered_kinds = set(presence.keys())

        if len(covered_kinds) >= 3:
            continue

        missing_kinds = [k for k in all_kinds if k not in covered_kinds]
        for kind in missing_kinds:
            if len(covered_kinds) >= 3:
                break
            # Pick a random note of this kind
            candidates = list(OUT.glob("*.md"))
            kind_candidates = []
            for f in candidates:
                m = re.search(r"^kind:\s*(\S+)", f.read_text(), re.M)
                if m and m.group(1) == kind:
                    kind_candidates.append(f)

            if not kind_candidates:
                continue

            chosen = rng.choice(kind_candidates)
            _rewrite_note_with_topic(chosen, topic, rng)
            covered_kinds.add(kind)


# ---------------------------------------------------------------------------
# Kind dispatch
# ---------------------------------------------------------------------------

def generate_kind(kind: str, n: int, rng: random.Random) -> None:
    dispatch = {
        "tool": gen_tool,
        "paper": gen_paper,
        "project-log": gen_project_log,
        "idea": gen_idea,
        "ops": gen_ops,
    }
    dispatch[kind](n, rng)


def main() -> None:
    rng = random.Random(SEED)
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    for kind, n in COUNTS.items():
        generate_kind(kind, n, rng)

    enforce_cross_cutting(rng)
    print(f"wrote {sum(COUNTS.values())} files to {OUT}")


if __name__ == "__main__":
    main()
