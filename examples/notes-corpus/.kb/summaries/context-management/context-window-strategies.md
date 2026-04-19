# Context Window Management Strategies

Practical experiments with keeping agent sessions inside the context limit without losing coherence.

## What works

The clearest finding from `notes/tool-029-context-window-management-strat.md` is that **single-responsibility subtasks** are the primary lever. When each agent invocation has one well-defined job, the context budget becomes predictable and the output verifiable. Explicit constraints in the prompt consistently outperformed general instructions — vague guidance caused the model to expand scope, consuming budget unnecessarily.

A second technique from the same note: treat each tool call as a unit test. Verify input shape before the call and output shape after. This discipline surfaces silent truncation early — the failure mode where ignoring context-window limits mid-session causes data to be dropped without any error signal.

The duplicate note `notes/tool-064-context-window-management-strat.md` (if present in the corpus as tool-029 copy) confirms these findings held across different project contexts.

## What doesn't work

Mixing two unrelated concerns in one agent call predictably muddies output. The combined response is worse than two separate calls on both dimensions. Asking for explanation and code together is the canonical example: the code degrades.

Over-relying on the model's memory of earlier turns — rather than re-injecting key facts explicitly — produces subtle inconsistencies by step four or five of a multi-step session.

## Connection to paper literature

`notes/paper-009-long-context-language-models-a.md` provides the theoretical framing: long-context models do not uniformly attend to all positions in the window; content in the middle is attended to less reliably than content at the start or end. This explains why re-injecting key state at each turn outperforms relying on implicit memory.

## References

- Source: `notes/tool-029-context-window-management-strat.md`
- Paper: `notes/paper-009-long-context-language-models-a.md`, `notes/paper-031-long-context-language-models-a.md`
- Related: [rag-vs-compiled](rag-vs-compiled.md)
