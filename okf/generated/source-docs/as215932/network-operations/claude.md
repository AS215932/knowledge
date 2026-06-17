---
type: Agent Instruction
title: AS215932 Network Operations
description: Infrastructure-as-code for AS215932 (Hyrule/Servify), an IPv6-first ISP
  running on XCP-NG.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/CLAUDE.md
tags:
- agent-instruction
- as215932
- network-operations
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: CLAUDE.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-322
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/CLAUDE.md#L1-L322
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: CLAUDE.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `CLAUDE.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `322` |

# Detected headings

* `# AS215932 Network Operations`
* `## Project overview`
* `## Network fundamentals`
* `## Architecture`
* `### Routers`
* `### WireGuard mesh`
* `### OVH VM layout`
* `## Addressing`
* `## Repository layout`
* `## Key conventions`
* `## BGP policy`
* `## NAT64/DNS64`
* `### Components`
* `### VRF route leaking`
* `# Forward: overlay → default VRF (so Jool sees the packet)`
* `# Return: default → overlay VRF (so the translated reply reaches the VM)`
* `### IPv4 addressing`
* `### Key files`
* `### Verifying`
* `## Critical details`
* `## Firewalls — Ansible + traffic-flow inventory`
* `## Deployment safety — always check Icinga before and after`
* `## Commit discipline`
* `## Monitoring — every host gets node_exporter + Icinga2`

# Deterministic excerpt

```markdown
# AS215932 Network Operations

Infrastructure-as-code for AS215932 (Hyrule/Servify), an IPv6-first ISP running on XCP-NG.

## Project overview

This repo contains live router configs, service templates, provisioning scripts, and deployment docs for the AS215932 network. The primary deployment target is an OVH RISE-S dedicated server running XCP-NG with multiple VMs.

## Network fundamentals

- **ASN**: 215932 (RIPE)
- **Prefix**: `2a0c:b641:b50::/44`
- **Internal networking is IPv6-only** — no RFC1918. All VMs use public AS215932 addresses.
- IPv4 exists only on dom0's WAN bridge (OVH-provided /32).
- Domain policy:
  `AGENTS.md` is canonical. Keep customer-facing Hyrule Cloud identity under
  `hyrule.host`, infrastructure identity under `servify.network`, and AS215932
  overlay/routing identity under `as215932.net`.

## Architecture

Underlay (hosting provider networks) is separate from overlay (AS215932 `2a0c:b641:b50::/44`). WireGuard tunnels connect routers over underlay; overlay traffic runs inside the tunnels. WireGuard endpoints MUST be underlay addresses, never overlay.

### Routers

| Router | Location | OS | Underlay address | Loopback (overlay) | Router-ID |
|--------|----------|-----|------------------|-------------------|-----------|
| cr1.nl1 | Servperso NL | FreeBSD + FRRouting | `2a0c:b640:8:69::1` | `::a` | 1.1.1.1 |
| cr1.de1 | Servperso DE | FreeBSD + FRRouting | `2a0c:b640:10::213` | `::b` | 2.2.2.2 |
| rtr | OVH FR | Debian 13 + FRRouting | `2001:41d0:303:48a::2` | `::d` | 0.0.0.13 |

All loopbacks are in `2a0c:b641:b50::/128` (e.g. `2a0c:b641:b50::a`).

### WireGuard mesh

| Tunnel | Endpoints | Overlay /127 |
|--------|-----------|--------------|
| cr1.nl1 wg0 ↔ cr1.de1 wg0 | :1337 ↔ :1337 | `ff00::/127` |
| cr1.nl1 wg3 ↔ rtr wg0 | :1340 ↔ :1337 |
...
```

# Citations

[1] [CLAUDE.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/CLAUDE.md)
