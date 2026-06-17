---
type: Policy
title: Source of Truth and Canonicality Policy
description: Typed source-first hybrid truth model for AS215932 knowledge.
tags:
- curated
- policy
- proposed
truth_owner: okf
authority: advisory
source_refs:
- repo: AS215932/network-operations
  path: AGENTS.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/AGENTS.md
- repo: AS215932/network-operations
  path: README.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/README.md
- repo: AS215932/hyrule-cloud
  path: AGENTS.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/AGENTS.md
last_verified_at: '2026-06-17T10:33:31Z'
confidence: medium
dispute_policy: adjudicate
review_status: proposed
---

# Policy

Source repositories are canonical for implemented behavior, executable state, APIs, configuration, schemas, tests, CI/CD, deployment workflows, repo-local docs, and intended infrastructure state committed as code.

OKF generated concepts are derivative: they summarize and cross-link source material but must cite repo paths and commits.

OKF curated concepts can be canonical only for cross-repo institutional knowledge that does not naturally belong in one repo. New curated pages start as `review_status: proposed` and `authority: advisory` until reviewed.

Observed telemetry is evidence only. It can prove drift or support investigation but does not silently redefine intended state.

# Citations

[1] [AS215932/network-operations:AGENTS.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/AGENTS.md)
[2] [AS215932/network-operations:README.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/README.md)
[3] [AS215932/hyrule-cloud:AGENTS.md](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/AGENTS.md)
