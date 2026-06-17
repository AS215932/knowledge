---
type: Architecture
title: Engineering Loop vs NOC Loop
description: Boundary between agentic development automation and production incident
  investigation.
tags:
- architecture
- curated
- proposed
truth_owner: okf
authority: advisory
source_refs:
- repo: AS215932/engineering-loop
  path: docs/agentic-development-loop.md
  commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/docs/agentic-development-loop.md
- repo: AS215932/network-operations
  path: docs/agentic-development-loop.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/agentic-development-loop.md
- repo: AS215932/network-operations
  path: docs/autonomous-noc.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/autonomous-noc.md
last_verified_at: '2026-06-17T10:18:30Z'
confidence: medium
dispute_policy: adjudicate
review_status: proposed
---

# Boundary

The Hyrule Engineering Loop and Hyrule NOC Loop are separate systems.

# Engineering Loop

Designs changes, coordinates coding agents, validates worktrees, prepares draft PRs, and stops for human sign-off.

# NOC Loop

Responds to alerts, investigates production, detects drift, proposes remediation, verifies recovery, and records human decisions.

# Allowed connection

Engineering Loop can provide deploy notes, expected impact, and rollback plans to NOC context. NOC observations can create issue feedback for Engineering Loop.

# Forbidden connection

NOC Agent must not become a normal feature-planning or PR-generation system.

# Citations

[1] [AS215932/engineering-loop:docs/agentic-development-loop.md](https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/docs/agentic-development-loop.md)
[2] [AS215932/network-operations:docs/agentic-development-loop.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/agentic-development-loop.md)
[3] [AS215932/network-operations:docs/autonomous-noc.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/autonomous-noc.md)
