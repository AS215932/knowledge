---
type: Source Document
title: AS215932 Network Operations
description: This repository is the production deployment record for `noc-agent`,
  `hyrule-mcp`, `hyrule-cloud`, `hyrule-web`, and `hyrule-network-proxy`. App repos
  do not deploy production on merge.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/README.md
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: README.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-207
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/README.md#L1-L207
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: README.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `README.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `207` |

# Detected headings

* `# AS215932 Network Operations`
* `## Production Deploys: Read This First`
* `## About`
* `## Network Status`
* `### Current Infrastructure`
* `### Upstream Connectivity`
* `## Domain Policy`
* `### Internet Exchange Points`
* `## Technical Stack`
* `### Routing & Network`
* `### Architecture Highlights`
* `## Architecture diagrams`
* `## Screenshots`
* `## Repository Structure`
* `## Peering`
* `## Documentation`
* `## Roadmap & milestones`
* `### Near-term priorities`
* `## Using This Repository`
* `## Resources`
* `## Related repositories`
* `## Contact`

# Deterministic excerpt

```markdown
# AS215932 Network Operations

## Production Deploys: Read This First

This repository is the production deployment record for `noc-agent`,
`hyrule-mcp`, `hyrule-cloud`, `hyrule-web`, and `hyrule-network-proxy`. App repos do not deploy
production on merge.

After an app repo's `ci` workflow succeeds on `main`, its
**request-promotion** workflow asks this repo to open or update the promotion PR
that pins exact SHAs in inventory. **Actions -> promote-apps** remains the
manual fallback when a promotion request needs to be replayed or coordinated by
hand. After the promotion PR merges, **app-promotion-deploy** automatically
calls `apply.yml` for the affected playbooks and waits at the GitHub
`production` environment approval gate. The human operator's normal job is to
review the promotion PR, merge it, approve the production gate, and review the
Icinga snapshot diff.

Full runbook: [docs/ci/deploy-runbook.md](docs/ci/deploy-runbook.md).

Public operations repository for **Hyrule Networks (AS215932)** — building a complete Internet Service Provider from scratch.

## About

AS215932 is a solo project to build and operate a full-stack ISP with modern BGP routing, multi-homing, and IPv6-first architecture. This repository tracks infrastructure work, configuration management, and operational decisions.

**Working in public** to share knowledge with the networking community and demonstrate real-world ISP operations.

## Network Status

### Current Infrastructure

- **ASN**: AS215932
- **Network Name**: Hyrule / Servify
- **NOC**: noc@as215932.net
- **Peering Policy**: Open (see PeeringDB)
- **PeeringDB**: [AS215932](https://www.peeringdb.com/asn/215932)

### Upstream Connectivity

- Multiple BGP transit providers
- Presence at multiple Internet Exchange Points (IXPs)
- IPv6-only
...
```

# Citations

[1] [README.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/README.md)
