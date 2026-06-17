---
type: Domain Policy
title: AS215932 Domain Policy
description: Identity split for hyrule.host, servify.network, and as215932.net.
tags:
- as215932
- domains
- identity
- policy
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: AGENTS.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/AGENTS.md
- repo: AS215932/network-operations
  path: CLAUDE.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/CLAUDE.md
- repo: AS215932/network-operations
  path: README.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/README.md
- repo: AS215932/hyrule-cloud
  path: AGENTS.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/AGENTS.md
- repo: AS215932/hyrule-cloud
  path: CLAUDE.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/CLAUDE.md
- repo: AS215932/hyrule-cloud
  path: README.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/README.md
- repo: AS215932/hyrule-network-proxy
  path: AGENTS.md
  commit: b82dc72bbf382167062bff272606ce84ec20538c
  url: https://github.com/AS215932/hyrule-network-proxy/blob/b82dc72bbf382167062bff272606ce84ec20538c/AGENTS.md
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
---

# Domain policy

The deterministic source documents agree on this identity split:

- `hyrule.host` is customer-facing Hyrule Cloud/product identity.
- `servify.network` is infrastructure identity for nameservers, underlay, management, provider relationships, internal UIs, and partner-facing infrastructure hostnames.
- `as215932.net` is AS215932 overlay/routing identity only.

This concept is generated from cited repo-local agent guidance and docs. If a repo-owned domain policy changes, regenerate this concept.

# Citations

[1] [AS215932/network-operations:AGENTS.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/AGENTS.md)
[2] [AS215932/network-operations:CLAUDE.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/CLAUDE.md)
[3] [AS215932/network-operations:README.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/README.md)
[4] [AS215932/hyrule-cloud:AGENTS.md](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/AGENTS.md)
[5] [AS215932/hyrule-cloud:CLAUDE.md](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/CLAUDE.md)
[6] [AS215932/hyrule-cloud:README.md](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/README.md)
[7] [AS215932/hyrule-network-proxy:AGENTS.md](https://github.com/AS215932/hyrule-network-proxy/blob/b82dc72bbf382167062bff272606ce84ec20538c/AGENTS.md)
