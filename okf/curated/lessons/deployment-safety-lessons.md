---
type: Lesson
title: Deployment Safety Lessons
description: Durable safety lessons extracted from deployment and infrastructure guidance.
tags:
- curated
- lesson
- proposed
truth_owner: okf
authority: advisory
source_refs:
- repo: AS215932/network-operations
  path: CLAUDE.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/CLAUDE.md
- repo: AS215932/network-operations
  path: docs/ci/deploy-runbook.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/deploy-runbook.md
- repo: AS215932/network-operations
  path: AGENTS.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/AGENTS.md
last_verified_at: '2026-06-17T10:33:31Z'
confidence: medium
dispute_policy: adjudicate
review_status: proposed
---

# Lessons

1. App merges are not production deploys; production is represented by pinned SHAs in `network-operations`.
2. Real deployments need Icinga snapshots before and after applies so operators can separate already-broken from newly-broken state.
3. Firewall changes must update the network-flow inventory first, then host vars, then rendered artifacts.
4. Branch hygiene matters: start from fresh `main` branches for unrelated work to avoid accidental PR contamination.
5. Generated knowledge must cite source repos, or it is advisory at best.

# Citations

[1] [AS215932/network-operations:CLAUDE.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/CLAUDE.md)
[2] [AS215932/network-operations:docs/ci/deploy-runbook.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/deploy-runbook.md)
[3] [AS215932/network-operations:AGENTS.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/AGENTS.md)
