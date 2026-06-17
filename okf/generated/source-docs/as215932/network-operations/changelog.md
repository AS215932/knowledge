---
type: Source Document
title: Changelog
description: All notable changes to Hyrule Networks (AS215932) `network-operations`
  are documented in this file.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/CHANGELOG.md
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: CHANGELOG.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-47
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/CHANGELOG.md#L1-L47
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: CHANGELOG.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `CHANGELOG.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `47` |

# Detected headings

* `# Changelog`
* `## [Unreleased]`
* `### Added`
* `## [2025.06] — Infrastructure hardening & automation`
* `### Added`
* `### Changed`
* `## [2025.05] — Multi-homing & IXP expansion`
* `### Added`
* `### Changed`
* `## [2025.04] — Core routing fabric`
* `### Added`
* `## [2025.03] — ASN & prefix allocation`
* `### Added`

# Deterministic excerpt

```markdown
# Changelog

All notable changes to Hyrule Networks (AS215932) `network-operations` are
documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Profile/README optimization pass: roadmap, architecture diagrams, screenshots, contributing guide, and changelog.

## [2025.06] — Infrastructure hardening & automation

### Added
- Promotion-runbook documentation for app deployments.
- `apply.yml` playbook orchestration with GitHub environment gates.
- Agentic engineering loop extracted into its own repository (`engineering-loop`).

### Changed
- Moved production deploy authority from app repos into `network-operations`.
- Switched Icinga queries to REST-API-first in `hyrule-mcp`.

## [2025.05] — Multi-homing & IXP expansion

### Added
- Additional IXP presence and peering sessions.
- RPKI ROA and IRR object registration finalized.
- WireGuard full-mesh overlay for stateless routing.

### Changed
- Refined BGP routing policy and ECMP load balancing.

## [2025.04] — Core routing fabric

### Added
- Deployed core routers `cr1-nl1`, `cr1-de1`, `cr1-ch1` on FreeBSD + FRRouting.
- Deployed edge router `rtr` at OVH on Debian 13 + FRRouting.
- OSPFv3 internal connectivity established.

## [2025.03] — ASN & prefix allocation

### Added
- AS215932 assigned.
- IPv6 prefix allocation received.
- PeeringDB and RIPE IRR records created.
```

# Citations

[1] [CHANGELOG.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/CHANGELOG.md)
