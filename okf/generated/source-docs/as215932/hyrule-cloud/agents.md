---
type: Agent Instruction
title: Hyrule Cloud Agent Guide
description: '- `hyrule.host` is customer-facing Hyrule Cloud/product identity. Public
  API clients use `https://cloud.hyrule.host`; automatic VM hostnames live under `deploy.hyrule.host`.
  - `servify.network` is infrastructure identity for nameservers,...'
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/AGENTS.md
tags:
- agent-instruction
- as215932
- hyrule-cloud
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: AGENTS.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1-9
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/AGENTS.md#L1-L9
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
source_path: AGENTS.md
commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-cloud` |
| Path | `AGENTS.md` |
| Commit | `81e4316f3d1f4e7f770bc2589bd84a2c7972aad5` |
| Lines | `9` |

# Detected headings

* `# Hyrule Cloud Agent Guide`
* `## Domain Policy`

# Deterministic excerpt

```markdown
# Hyrule Cloud Agent Guide

## Domain Policy

- `hyrule.host` is customer-facing Hyrule Cloud/product identity. Public API clients use `https://cloud.hyrule.host`; automatic VM hostnames live under `deploy.hyrule.host`.
- `servify.network` is infrastructure identity for nameservers, underlay and management references, provider relationships, internal UIs, and partner-facing hostnames.
- `as215932.net` is AS215932 overlay/routing identity only. DNS records in this zone must point only at prefixes owned by AS215932.

Do not blindly replace `servify.network`: nameservers such as `ns1.servify.network` and `ns2.servify.network` are intentionally infrastructure identity.
```

# Citations

[1] [AGENTS.md](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/AGENTS.md)
