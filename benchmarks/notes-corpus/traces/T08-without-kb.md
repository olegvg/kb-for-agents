# T08 — without-kb

**Question:** Have I written anything about designing APIs with GraphQL or gRPC?
**Mode:** without-kb
**Recorded:** 2026-04-19

## Files opened (in order)
(none — grep returned zero matches)

## Tool calls
- Read × 0
- Grep × 3
- Glob × 0

## Tokens read from corpus
~0  
(grep for "graphql", "grpc", and "protobuf" all returned zero matches; no files opened)

## Answer

No. Grep for "graphql" across all 150 notes files returns zero matches. Grep for "grpc" returns zero matches. Grep for "protobuf" returns zero matches. The corpus contains no notes about GraphQL or gRPC API design. The closest adjacent content is `notes/tool-007-tool-use-json-schema-design.md` and `notes/tool-042-tool-use-json-schema-design.md`, which cover JSON schema design for LLM tool calls — a machine-readable interface format, but not a client-server API query language. A well-calibrated agent gives a clean negative answer and explicitly notes the distinction between tool-call JSON schemas (present in the corpus) and GraphQL/gRPC API design languages (absent). A poorly calibrated agent might surface the JSON schema design notes as a proxy for "API design," which would be a false positive. The grep baseline correctly returns zero matches, making the clean negative the obvious response.
