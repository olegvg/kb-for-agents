# MCP and Tools — Overview

This domain covers the Model Context Protocol (MCP) for building and connecting tool servers to agents, plus the engineering of individual tools: JSON schema design, streaming, environment variable management, prompt injection defense, and rate limiting.

MCP is the protocol that exposes tools (functions) to LLMs at runtime. This domain covers it from both the server-authoring side (building an MCP server) and the agent-consumption side (designing tools an agent can use reliably).

## Leaves in this domain

- **[mcp-setup](mcp-setup.md)** — setting up and configuring MCP servers; connection and auth patterns.
- **[tool-design](tool-design.md)** — JSON schema design for tool definitions, structured output, few-shot selection.
- **[operational-concerns](operational-concerns.md)** — streaming, rate limits, env vars, prompt injection defense.

## References

- Tool notes: `notes/tool-008-mcp-server-setup-and-configurat.md`, `notes/tool-007-tool-use-json-schema-design.md`, `notes/tool-011-streaming-responses-in-claude-a.md`, `notes/tool-010-environment-variable-management.md`, `notes/tool-001-prompt-injection-defence-patter.md`, `notes/tool-032-rate-limit-handling-in-agent-pi.md`, `notes/tool-005-few-shot-example-selection-stra.md`
- Papers: `notes/paper-004-large-language-models-as-tool-.md`, `notes/paper-020-prompt-injection-attacks-and-d.md`, `notes/paper-021-toolformer-language-models-can.md`
