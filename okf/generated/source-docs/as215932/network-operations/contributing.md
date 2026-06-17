---
type: Source Document
title: Contributing to AS215932 network-operations
description: Thanks for your interest in Hyrule Networks (AS215932). This repository
  is both a public record of ISP operations and a place for community contribution.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/CONTRIBUTING.md
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: CONTRIBUTING.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-64
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/CONTRIBUTING.md#L1-L64
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: CONTRIBUTING.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `CONTRIBUTING.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `64` |

# Detected headings

* `# Contributing to AS215932 network-operations`
* `## Ways to contribute`
* `## Peering requests`
* `## Style guide`
* `## Repository structure conventions`
* `## Automation & CI`
* `## License`
* `## Code of conduct`

# Deterministic excerpt

```markdown
# Contributing to AS215932 network-operations

Thanks for your interest in Hyrule Networks (AS215932). This repository is both
a public record of ISP operations and a place for community contribution.

## Ways to contribute

1. **Peering requests** — Use the `peering` label and the peering issue template.
2. **Bug reports** — Routing anomalies, documentation errors, or broken automation.
3. **Configuration improvements** — Reusable FRRouting, WireGuard, or monitoring templates.
4. **Documentation** — Architecture notes, runbook clarifications, or tutorial sections.
5. **Questions** — Open a discussion issue if something about the network is unclear.

## Peering requests

Before opening a peering request, please ensure your network meets our policy:

- Valid PeeringDB entry for your ASN
- IRR objects registered in the RIPE Database
- 24/7 NOC contact
- RPKI ROA configured for your prefixes

Open an issue with the `peering` label and include:

- Your ASN
- IXP location(s) where you want to peer
- PeeringDB link
- Contact email

## Style guide

- Keep configuration examples as generic and reusable as possible.
- Use Jinja2 variables rather than hard-coded values where applicable.
- Prefer shell scripts that fail fast (`set -euo pipefail`).
- Document new playbooks or scripts with a short header comment.
- Follow the existing 80-column soft target for documentation.

## Repository structure conventions

```
configs/     # Jinja2 templates and generated router configs
docs/        # Architecture, runbooks, and peering docs
scripts/     # Bootstrap and operational helpers
autoinstall/ # OS autoinstall and QMP tooling
.github/     # Issue templates and CI workflows
```

## Automation & CI

- App repos do **not** deploy production on merge.
- After an app repo CI succeeds on `m
...
```

# Citations

[1] [CONTRIBUTING.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/CONTRIBUTING.md)
