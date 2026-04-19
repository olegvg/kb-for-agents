---
title: Using prompt injection defence patterns: notes and reflections
kind: tool
date: 2025-08-31
---

Picked up prompt injection defence patterns after seeing it mentioned twice in the same week. Decided it warranted a proper try.

What worked: Treating each tool call as a unit test — verify input, verify output — kept drift in check. Giving the model a concrete example before asking for the real thing cut hallucinations significantly.

What didn't: Not pinning the model version meant a surprise behavior change after a silent rollout. Mixing two unrelated concerns in one subagent call muddied the output and doubled the review time. Ignoring context-window limits mid-session caused silent truncation that was hard to diagnose.

The setup cost is real, but it pays back on the third use. Probably worth it.
