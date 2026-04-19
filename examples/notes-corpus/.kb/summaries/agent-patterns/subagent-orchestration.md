# Subagent Orchestration Patterns

How to design, dispatch, and collect results from subagents — whether running sequentially or in parallel.

## Parallel vs sequential dispatch

`notes/tool-014-parallel-subagent-orchestration.md` establishes the main finding: parallel dispatch is feasible and valuable when subtasks are independent. Single-responsibility is a prerequisite — subtasks with shared mutable state cannot be parallelized safely. The note confirms the practical rule: if two tasks can be described without referencing each other's intermediate outputs, they can run in parallel.

`notes/tool-015-subagent-dispatching-patterns.md` adds the dispatch-side view: providing a **bounded tool list** in the subagent prompt is critical. When the model was allowed to pick its own tools without constraint, time was wasted on tool selection and the results were less focused.

## Context isolation

The key benefit of subagent dispatch is context isolation: each subagent sees only the files it needs. `notes/tool-014` notes that this prevented runaway context growth in practice — "incremental commits kept the feedback loop tight." Without isolation, context accumulates across unrelated topics and the main agent's attention becomes diffuse.

## Aggregating results

After parallel subagents complete, the main agent aggregates their briefs. The recommended pattern is for each subagent to return a structured brief (200-word summary, list of outputs created) rather than raw results. This allows the main agent to synthesize across briefs without re-reading full subagent outputs.

`notes/paper-007-voyager-an-open-ended-embodied.md` (Voyager) provides a research reference for this pattern: the curriculum agent dispatches skill-learning subagents and receives compact skill representations, not execution traces.

## References

- Source: `notes/tool-014-parallel-subagent-orchestration.md`, `notes/tool-015-subagent-dispatching-patterns.md`
- Paper: `notes/paper-007-voyager-an-open-ended-embodied.md`
- Related: [agent-loop-design](agent-loop-design.md)
