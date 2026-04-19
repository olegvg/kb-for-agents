# Test-Driven Development with AI Pair Programming

How to use AI assistance in a TDD workflow, and how TDD supports AI-assisted development.

## TDD as a constraint for AI pair programming

`notes/tool-020-test-driven-development-with-ai.md` makes the core argument: writing tests first constrains what the AI pair can generate. When the model generates implementation code, having an existing test suite gives it an objective success criterion — instead of generating code that "looks right", it generates code that passes tests. The result is that AI-generated code is more reliably correct and requires less review.

The note confirms the pattern from agent-loop design: treating each tool call as a unit test (verify input, verify output) is essentially test-driven development applied to the agent loop. The disciplines reinforce each other.

## TDD as audit follow-on

After an AI-assisted audit (`notes/tool-009-audit-of-legacy-codebases-with-.md`), TDD is a natural next step: the audit surfaces undocumented behaviors, and writing tests formalizes those behaviors as expected contracts. The model can help write the tests given the audit findings as context.

## Diff-based editing with agents

`notes/tool-012-diff-based-code-editing-with-ag.md` covers a related technique: asking the model to produce diffs rather than full file rewrites. In a TDD workflow, diff-based editing is especially valuable — it is easier to verify that a diff implements exactly one behavior change than to verify a rewritten file.

## References

- Source: `notes/tool-020-test-driven-development-with-ai.md`, `notes/tool-012-diff-based-code-editing-with-ag.md`
- Paper: `notes/paper-019-software-engineering-with-larg.md`
- Related: [audit-workflow](audit-workflow.md), [agent-patterns/agent-loop-design](../../agent-patterns/agent-loop-design.md)
