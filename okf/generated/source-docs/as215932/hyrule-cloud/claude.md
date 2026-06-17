---
type: Agent Instruction
title: Hyrule Cloud
description: Agentic VPS hosting API on AS215932, paid via x402 (USDC on Base). Agents
  discover the service via x402 Bazaar or `/.well-known/x402.json`, pay per-request,
  and receive bare VMs with SSH access, automatic DNS subdomains, and IPv6-native...
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/CLAUDE.md
tags:
- agent-instruction
- as215932
- hyrule-cloud
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: CLAUDE.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1-165
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/CLAUDE.md#L1-L165
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
source_path: CLAUDE.md
commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-cloud` |
| Path | `CLAUDE.md` |
| Commit | `81e4316f3d1f4e7f770bc2589bd84a2c7972aad5` |
| Lines | `165` |

# Detected headings

* `# Hyrule Cloud`
* `## Business Context`
* `## Domain Policy`
* `## Stack`
* `## Architecture`
* `## Key Design Decisions`
* `## Endpoints`
* `## File Structure`
* `## Development`
* `# Postgres runs in an Incus container (not Docker)`
* `# If not already running:`
* `#   incus launch images:debian/13 hyrule-postgres`
* `#   incus exec hyrule-postgres -- apt install -y postgresql`
* `#   incus exec hyrule-postgres -- sudo -u postgres createuser -s hyrule`
* `#   incus exec hyrule-postgres -- sudo -u postgres createdb -O hyrule hyrule`
* `#   incus exec hyrule-postgres -- sudo -u postgres psql -c "ALTER USER hyrule PASSWORD 'hyrule';"`
* `#   # Edit pg_hba.conf to allow md5 auth from host network`
* `# Set HYRULE_DATABASE_URL=postgresql+asyncpg://hyrule:hyrule@<incus-ip>/hyrule`
* `# Dev payment bypass: set PAYMENT_DEV_BYPASS_SECRET in .env, then pass`
* `# X-DEV-BYPASS: <secret> header to skip x402 payment verification.`
* `## MCP Server`
* `## What's Not Yet Built`
* `## Conventions`

# Deterministic excerpt

```markdown
# Hyrule Cloud

Agentic VPS hosting API on AS215932, paid via x402 (USDC on Base). Agents discover the service via x402 Bazaar or `/.well-known/x402.json`, pay per-request, and receive bare VMs with SSH access, automatic DNS subdomains, and IPv6-native networking.

## Business Context

Target market: AI agents (especially OpenClaw) that "vibe code" apps and need to deploy them. The API is the first full-stack infrastructure offering in the x402 Bazaar (VPS + domain + DNS). Revenue model is prepaid compute-time in USDC via the x402 exact scheme.

The operator holds AS215932 (RIPE), runs XCP-NG hypervisors, uses Openprovider as domain registrar, and runs authoritative DNS (BIND/Knot with TSIG for RFC 2136 dynamic updates). All VMs are IPv6-only with NAT64/DNS64 for IPv4-only destinations. If IPv6-only proves insufficient for agent workloads, an IPv4 subnet lease is possible but not preferred.

TODO: Hosted OpenClaw instances, with a custom web interface for management

## Domain Policy

`AGENTS.md` is the canonical domain-policy reference for this repo. Keep
customer-facing Hyrule Cloud identity under `hyrule.host`, infrastructure
identity under `servify.network`, and AS215932 overlay/routing identity under
`as215932.net`.

## Stack

- Python 3.12, FastAPI, Pydantic v2
- Official Coinbase x402 Python SDK (`x402[fastapi,evm]>=2.0`) for payment gating
- SQLAlchemy 2.0 async + asyncpg (Postgres 17) for persistence
- Alembic for migrations
- XCP-NG XAPI (XML-RPC over HTTPS) for VM lifecycle
- Openprovider REST API for domain registration
- RFC 2136 (`nsupdate` + TSIG) for dynamic DNS (AAAA records)
- cloud-init for VM bootstrapping (SSH key, UFW defaults, optional setup script)
- APScheduler for periodic VM expiry checks
- structlog for structured logging
- Ruff for linting (
...
```

# Citations

[1] [CLAUDE.md](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/CLAUDE.md)
