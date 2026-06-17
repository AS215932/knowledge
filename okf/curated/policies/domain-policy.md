---
type: Policy
title: Domain Policy
description: Curated statement of AS215932 domain identity boundaries.
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
- repo: AS215932/hyrule-cloud
  path: AGENTS.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/AGENTS.md
- repo: AS215932/hyrule-network-proxy
  path: AGENTS.md
  commit: b82dc72bbf382167062bff272606ce84ec20538c
  url: https://github.com/AS215932/hyrule-network-proxy/blob/b82dc72bbf382167062bff272606ce84ec20538c/AGENTS.md
last_verified_at: '2026-06-17T10:33:31Z'
confidence: medium
dispute_policy: adjudicate
review_status: proposed
---

# Domain policy

- `hyrule.host` is customer-facing Hyrule Cloud/product identity.
- `servify.network` is infrastructure identity for nameservers, underlay, management, providers, internal UIs, and partner-facing infrastructure hostnames.
- `as215932.net` is AS215932 overlay/routing identity only.

Do not blindly replace `servify.network`; many infrastructure references intentionally live there.

# Citations

[1] [AS215932/network-operations:AGENTS.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/AGENTS.md)
[2] [AS215932/hyrule-cloud:AGENTS.md](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/AGENTS.md)
[3] [AS215932/hyrule-network-proxy:AGENTS.md](https://github.com/AS215932/hyrule-network-proxy/blob/b82dc72bbf382167062bff272606ce84ec20538c/AGENTS.md)
