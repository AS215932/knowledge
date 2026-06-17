---
type: Source Document
title: Hyrule Cloud
description: Agentic VPS hosting on Hyrule Networks (AS215932) with x402 payments.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/README.md
tags:
- as215932
- hyrule-cloud
- source-document
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: README.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1-180
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/README.md#L1-L180
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
source_path: README.md
commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-cloud` |
| Path | `README.md` |
| Commit | `81e4316f3d1f4e7f770bc2589bd84a2c7972aad5` |
| Lines | `180` |

# Detected headings

* `# Hyrule Cloud`
* `## Architecture`
* `## Endpoints`
* `## Quick Start`
* `# Start Postgres`
* `# Configure`
* `# Fill in XCP-NG, Openprovider, and wallet details`
* `# Install`
* `# Run migrations`
* `# Start`
* `## XCP-NG Template Preparation`
* `# On a Debian 12 VM that will become a template:`
* `# Clean up, then convert to template in Xen Orchestra`
* `### OpenBSD root disk sizing`
* `## Network`
* `## Domain Policy`
* `## Payment`
* `## Database`
* `# Create a new migration after model changes`
* `# Apply`
* `## Project Structure`

# Deterministic excerpt

```markdown
# Hyrule Cloud

Agentic VPS hosting on Hyrule Networks (AS215932) with x402 payments.

Agents discover this service via the x402 Bazaar or `/.well-known/x402.json`, pay with USDC on Base, and receive bare VMs with SSH access, automatic DNS, and IPv6-native networking.

## Architecture

```
Agent (OpenClaw, Claude MCP, x402-aware client)
  |
  |-- discovers via /.well-known/x402.json or Bazaar
  |
  |-- POST /v1/vm/create  (no payment) --> 402 + pricing + specs
  |-- pays via x402 facilitator (USDC on Base)
  |-- POST /v1/vm/create  (with X-PAYMENT header) --> 202 + status_url
  |-- GET  /v1/vm/{id}    (poll) --> { ipv6, hostname, ssh }
  |
  |-- ssh root@<hostname>  --> agent owns the VM from here
```

```
Hyrule Cloud API (FastAPI + x402 SDK)
  |-- XCP-NG XAPI       VM lifecycle (clone, start, stop, destroy)
  |-- cloud-init         SSH key, default UFW rules, optional setup script
  |-- DNS (RFC 2136)     AAAA records on authoritative NS
  |-- Openprovider       Domain registration (custom domain mode)
  |-- PostgreSQL         Persistent state (VMs, domains, tunnels)
  |-- x402 facilitator   Payment verification and settlement (official SDK)
  |-- network proxy      Internal Go sidecar for paid Direct/Tor/I2P/Yggdrasil requests
```

## Endpoints

| Endpoint              | Method | Paid | Description                  |
|-----------------------|--------|------|------------------------------|
| `/v1/vm/create`       | POST   | Yes  | Provision a bare VM          |
| `/v1/vm/{id}`         | GET    | No   | Status, IP, expiry           |
| `/v1/vm/{id}/extend`  | POST   | Yes  | Add days to VM               |
| `/v1/vm/{id}/reboot`  | POST   | No   | Hard reboot                  |
| `/v1/vm/{id}`         | DELETE | No   | Destroy VM                   |
| `/v1/vm/{id}/logs`
...
```

# Citations

[1] [README.md](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/README.md)
