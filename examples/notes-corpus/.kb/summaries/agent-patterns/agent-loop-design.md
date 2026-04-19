# Agent Loop Design Patterns

The agent loop is the repeating structure: observe → plan → act → observe. Getting this structure right determines whether long agent sessions stay coherent or drift.

## Core pattern from practice

`notes/tool-033-agent-loop-design-patterns.md` documents the key finding: breaking tasks into **single-responsibility subtasks** is the single most impactful discipline. When each iteration of the loop does exactly one thing, the output is predictable and the next step can be planned based on a clean result — not a partially-completed mixed output.

Logging every agent turn to a file (not just printing) is essential for post-hoc diagnosis. The note records that the exact failure step was identifiable only because a log existed — "the exact step where things went sideways" — which would have been invisible from the final output alone.

The duplicate `notes/tool-048-error-recovery-in-multi-step-ag.md` adds a complementary pattern: treating each tool call as a unit test. Verify input shape before the call and output shape after. This turns each step into a checkpoint rather than a black box.

## Structural recommendation

A loop with explicit phases (plan, execute, verify) outperforms an implicit loop where the model decides internally when to move on. `notes/paper-001-react-synergizing-reasoning-an.md` (ReAct) formalizes this: interleaving reasoning traces with action calls improves task completion because the reasoning step constrains what actions are valid.

## Common failure modes

- Mixing two concerns in one loop iteration: the model produces something that partially satisfies both and fully satisfies neither.
- Ignoring context-window limits: silent truncation of earlier turns corrupts the loop's state without any error.
- Skipping the "what-not-to-do" section in the system prompt: obvious failure modes remain unguarded.

## References

- Source: `notes/tool-033-agent-loop-design-patterns.md`, `notes/tool-013-error-recovery-in-multi-step-ag.md`
- Paper: `notes/paper-001-react-synergizing-reasoning-an.md`
- Related: [subagent-orchestration](subagent-orchestration.md), [context-management/context-window-strategies](../../context-management/context-window-strategies.md)
