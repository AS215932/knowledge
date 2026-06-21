---
type: Reference
title: AS215932 (Hyrule Networks) — Service & Project Landscape
description: A structured knowledge-base enrichment for AS215932 (Hyrule Networks),
  covering all indexed services, projects, their responsibilities, deployment shapes,
  interfaces, dependencies, safety constraints, and inter-service relationships. Derived
  exclusively from the supplied source pack.
tags:
- enriched
- llm
- services
truth_owner: derived
authority: advisory
source_refs:
- repo: AS215932/hyrule-business
  path: hosting-cost-analysis.md
  commit: 89febc9c95fb6766df071e054cb44fba0b1ec8e4
  lines: 1-174
  url: https://github.com/AS215932/hyrule-business/blob/89febc9c95fb6766df071e054cb44fba0b1ec8e4/hosting-cost-analysis.md#L1-L174
- repo: AS215932/network-operations
  path: README.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-207
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/README.md#L1-L207
- repo: AS215932/network-operations
  path: AGENTS.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-53
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/AGENTS.md#L1-L53
- repo: AS215932/network-operations
  path: CLAUDE.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-240
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/CLAUDE.md#L1-L240
- repo: AS215932/as215932.net
  path: README.md
  commit: 9c0ee2d8f2bb793ea799589ca0fe4f77571b2572
  lines: 1-54
  url: https://github.com/AS215932/as215932.net/blob/9c0ee2d8f2bb793ea799589ca0fe4f77571b2572/README.md#L1-L54
- repo: AS215932/engineering-loop
  path: README.md
  commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
  lines: 1-75
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/README.md#L1-L75
- repo: AS215932/hyrule-cloud
  path: README.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1-180
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/README.md#L1-L180
- repo: AS215932/hyrule-cloud
  path: AGENTS.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1-9
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/AGENTS.md#L1-L9
- repo: AS215932/hyrule-cloud
  path: CLAUDE.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1-165
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/CLAUDE.md#L1-L165
- repo: AS215932/hyrule-mcp
  path: README.md
  commit: 326bcc85e1c69f0d7c1839ebaa4abb73acd84185
  lines: 1-177
  url: https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/README.md#L1-L177
- repo: AS215932/hyrule-mcp
  path: TESTING.md
  commit: 326bcc85e1c69f0d7c1839ebaa4abb73acd84185
  lines: 1-15
  url: https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/TESTING.md#L1-L15
- repo: AS215932/hyrule-network-proxy
  path: README.md
  commit: b82dc72bbf382167062bff272606ce84ec20538c
  lines: 1-98
  url: https://github.com/AS215932/hyrule-network-proxy/blob/b82dc72bbf382167062bff272606ce84ec20538c/README.md#L1-L98
- repo: AS215932/hyrule-network-proxy
  path: AGENTS.md
  commit: b82dc72bbf382167062bff272606ce84ec20538c
  lines: 1-21
  url: https://github.com/AS215932/hyrule-network-proxy/blob/b82dc72bbf382167062bff272606ce84ec20538c/AGENTS.md#L1-L21
- repo: AS215932/hyrule-web
  path: README.md
  commit: d94146e67f9eb05f8eeb5c57cab74cbe676f5c79
  lines: 1-17
  url: https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/README.md#L1-L17
- repo: AS215932/noc-agent
  path: README.md
  commit: 98e5010648e34ac0ea6ad8e6a925fef76d0dbea9
  lines: 1-240
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/README.md#L1-L240
- repo: AS215932/noc-agent
  path: TESTING.md
  commit: 98e5010648e34ac0ea6ad8e6a925fef76d0dbea9
  lines: 1-16
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/TESTING.md#L1-L16
last_verified_at: '2026-06-21T22:14:20Z'
confidence: medium
dispute_policy: repo_wins
review_status: proposed
enrichment:
  mode: llm
  provider: openrouter
  model: anthropic/claude-sonnet-4.6
  prompt_version: useful-v1
  input_hash: 1faf01faf61c5457f8692ff1bb578354e24e3197ce960a4fd776125d322da692
  output_hash: fd76ea8c5d894de52b6b93ecc0b6efe9d0c997b2ae4feea66f304dbe99be0f04
  generated_at: '2026-06-21T22:14:20Z'
enrichment_json: '{"generated_at":"2026-06-21T22:14:20Z","input_hash":"1faf01faf61c5457f8692ff1bb578354e24e3197ce960a4fd776125d322da692","mode":"llm","model":"anthropic/claude-sonnet-4.6","output_hash":"fd76ea8c5d894de52b6b93ecc0b6efe9d0c997b2ae4feea66f304dbe99be0f04","prompt_version":"useful-v1","provider":"openrouter"}'
---

# LLM enrichment

Review status: proposed. Treat this as advisory until human-reviewed.

# Overview of AS215932 (Hyrule Networks)

AS215932, operating under the brand 'Hyrule Networks', is building a complete ISP from scratch, encompassing BGP/OSPFv3 routing, IXP peering, and automation — all developed in public. The organisation operates a portfolio of interconnected services and projects spanning network operations, agentic VPS hosting, autonomous NOC operations, an engineering automation loop, diagnostic tooling, a public-facing website, and a network proxy sidecar. Business planning and hosting economics are tracked separately in the hyrule-business project.

Citations: `generated/projects/network-operations`, `generated/services/hyrule-cloud`, `generated/projects/hyrule-business`

# Network Operations Project

The network-operations project is the production deployment record and source of intended infrastructure state for AS215932. It owns Ansible inventory, host vars, firewall rules, monitoring configuration, DNS zones, and deployment workflows. Promotion PRs pin exact application SHAs before production applies. Key GitHub Actions workflows include: app-promotion-deploy, apply, drift-detection, netops-nightly, pr-agent, promote-apps, iac-tests, and lint. The project depends on the `langgraph` Python package. Source-of-truth files include README.md, AGENTS.md, CLAUDE.md, pyproject.toml, and a suite of agent-loop and CI documentation files. The operational runbook is located at docs/ci/deploy-runbook.md. Safety constraints require human approval through GitHub 'production' environment gates for all production applies, Icinga snapshot comparisons before and after every live deployment, and atomic updates to docs/network-flows.md, host vars, and rendered artifacts for any firewall change.

Citations: `generated/projects/network-operations`, `https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/README.md#L1-L207`, `https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/AGENTS.md#L1-L53`, `https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/CLAUDE.md#L1-L240`

# Hyrule Business Project

The hyrule-business project contains private business planning and profitability notes for Hyrule/AS215932, covering business analysis, hosting economics, pricing, profitability, and strategy. The primary indexed source file is hosting-cost-analysis.md (lines 1–174). No public or internal API/workflow interfaces, package-level dependencies, or operational runbooks were detected from indexed sources. Runtime and deployment shape are unknown from indexed sources. The project is related to hyrule-cloud and network-operations.

Citations: `generated/projects/hyrule-business`, `https://github.com/AS215932/hyrule-business/blob/89febc9c95fb6766df071e054cb44fba0b1ec8e4/hosting-cost-analysis.md#L1-L174`

# Hyrule Cloud Service

Hyrule Cloud is an agentic VPS hosting API with x402 payment gating, deployed on host `api` at version pinned to commit 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5. It coordinates VM lifecycle, DNS, XCP-NG, PostgreSQL state, domain registration, and paid diagnostic/network resources. The API surface is extensive, including authentication endpoints (register, login, logout, recovery, wallet challenge/verify, API key management), BGP lookup and pricing endpoints, DNS capability endpoints, and VM management. Workflows include ci, deploy-validation, pr-agent, request-promotion, and semgrep. Key Python dependencies include asyncpg, fastapi, and httpx. Related services include hyrule-web, hyrule-network-proxy, engineering-loop, and network-operations.

Citations: `generated/services/hyrule-cloud`, `https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/README.md#L1-L180`, `https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/AGENTS.md#L1-L9`, `https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/CLAUDE.md#L1-L165`

# Hyrule Web Service

Hyrule Web is the main branded public website and Hyrule Cloud order/dashboard frontend. It is a server-rendered application that ships committed Vite assets for hosts without Node in production. It is deployed on host `web` at version pinned to commit d94146e67f9eb05f8eeb5c57cab74cbe676f5c79. Workflows include ci, deploy-validation, pr-agent, request-promotion, and semgrep. Key routes include the homepage, /services, /order, /dashboard (with VM reboot/destroy/claim actions), /signup, /login, /logout, /recover, /transparency, /faq, /terms, /privacy, /abuse, /legal, /sitemap.xml, /llms.txt, and /robots.txt. Python dependencies include fastapi, httpx, structlog, and uvicorn; frontend dependencies include tailwindcss, typescript, vite, vitest, and walletconnect.

Citations: `generated/services/hyrule-web`, `https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/README.md#L1-L17`

# Hyrule NOC Agent Service

The NOC Agent is an autonomous Network Operations Centre agent for AS215932, deployed on host `noc` at version pinned to commit 98e5010648e34ac0ea6ad8e6a925fef76d0dbea9. Its responsibilities include alert intake, incident analysis, proactive hotspot scanning, operator approval, and Discord/local control surfaces. It consumes Hyrule MCP telemetry and stops at reviewable, human-gated proposals. The API surface includes webhook endpoints for Alertmanager and Icinga, mail polling, task submission, health checks, incident and case management, proactive loop controls (pause, resume, run-once, suppression management), and a Prometheus metrics endpoint. Python dependencies include fastapi, httpx, langgraph, mcp, structlog, and uvicorn. Production remediation is human-gated; the proactive loop is budgeted and read-only for investigation, handing changes to engineering-loop issues.

Citations: `generated/services/noc-agent`, `https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/README.md#L1-L240`, `https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/TESTING.md#L1-L16`

# Hyrule MCP Service

Hyrule MCP is a bounded live diagnostic MCP (Model Context Protocol) substrate for routing, monitoring, firewall, host, DNS, and packet-path inspection. It is a read-biased tool server used by the NOC agent and operators, deployed on host `noc` at version pinned to commit 326bcc85e1c69f0d7c1839ebaa4abb73acd84185. Workflows include ci, pr-agent, request-promotion, and semgrep. Python dependencies include fastapi, httpx, mcp, structlog, and uvicorn. Safety constraints specify that raw SSH is bounded and mutative commands are rejected unless explicit action gates are enabled, and that heavy diagnostics are capped server-side. Open issues include adding firewall_state, ndp_state/arp_state, multi_source_probe, ecmp_path_select, service_restart_history, vault_agent_status tools, and smaller helpers such as prometheus_list_targets and dns_probe_burst.

Citations: `generated/services/hyrule-mcp`, `https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/README.md#L1-L177`, `https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/TESTING.md#L1-L15`

# Hyrule Engineering Loop Service

The Engineering Loop is an autonomous development loop for AS215932 built on LangGraph. It creates draft PRs from approved issues and requests, running guarded worktrees, policy checks, gates, role judgments, and reflection. It is deployed on host `loop` at version pinned to commit 768cde6c996e42f3f91d395347ba9809e2e020e5. The only workflow interface is `ci` from .github/workflows/ci.yml. It depends on `langgraph`. Safety constraints specify it stops at draft PR for human review — merges and production applies remain human-gated — and it must not run on privileged GitHub Actions contexts with untrusted code. Known open issues include gate execution falsely reporting 'passed' when ruff/mypy are absent, feature-class issues exceeding per-run budget, planner using generic acceptance criteria, and cost tracking recording 0.0 due to a parser/backend mismatch.

Citations: `generated/services/engineering-loop`, `https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/README.md#L1-L75`

# Hyrule Network Proxy Service

The Hyrule Network Proxy is an internal sidecar that executes already-authorized Hyrule Cloud x402 network requests. It enforces egress policy and supports explicit direct/Tor/I2P/Yggdrasil modes. It is deployed on host `netproxy` at version pinned to commit b82dc72bbf382167062bff272606ce84ec20538c. The API surface includes GET /v1/health, GET /v1/modes, POST /v1/request, GET /healthz, GET /readyz, and /metrics. It is implemented in Go (dependencies from go.mod). Safety constraints require that the internal API must not be public, and that bodies, payment headers, authorization headers, and cookies must not be logged; residential proxying must not be added.

Citations: `generated/services/hyrule-network-proxy`, `https://github.com/AS215932/hyrule-network-proxy/blob/b82dc72bbf382167062bff272606ce84ec20538c/README.md#L1-L98`, `https://github.com/AS215932/hyrule-network-proxy/blob/b82dc72bbf382167062bff272606ce84ec20538c/AGENTS.md#L1-L21`

# as215932.net Service

as215932.net is a static informational website for AS215932 (Hyrule Networks), presenting ASN facts, peering policy, a network weathermap, prefix allocations, and a stub for an upcoming Looking Glass. The only workflow interface is pr-agent (plus semgrep). No package-level dependencies were detected from indexed sources. The sole source-of-truth file is README.md. An open issue (#2) tracks adding a lint/link-check gate as a required CI step.

Citations: `generated/services/as215932-net`, `https://github.com/AS215932/as215932.net/blob/9c0ee2d8f2bb793ea799589ca0fe4f77571b2572/README.md#L1-L54`

# Inter-Service Dependency Map

The services and projects of AS215932 form a tightly coupled graph. Hyrule Cloud is the central hosting API, related to hyrule-web (frontend), hyrule-network-proxy (egress sidecar), engineering-loop, and network-operations. The NOC Agent consumes Hyrule MCP telemetry and hands change proposals to engineering-loop issues; it is also related to network-operations. The Engineering Loop is related to network-operations, noc-agent, hyrule-cloud, and hyrule-web. Hyrule MCP is related to noc-agent and network-operations. The hyrule-business project is related to hyrule-cloud and network-operations. as215932.net is related to network-operations and hyrule-web.

Citations: `generated/services/hyrule-cloud`, `generated/services/noc-agent`, `generated/services/engineering-loop`, `generated/services/hyrule-mcp`, `generated/services/hyrule-network-proxy`, `generated/services/hyrule-web`, `generated/services/as215932-net`, `generated/projects/hyrule-business`, `generated/projects/network-operations`

# Human-Gating and Safety Constraints Across Services

Multiple services enforce explicit human-gating policies. Network-operations requires human approval through GitHub 'production' environment gates for all production applies, and mandates Icinga snapshot comparisons before and after every live deployment. The Engineering Loop stops at draft PR — merges and production applies are human-gated — and must not run on privileged GitHub Actions contexts with untrusted code. The NOC Agent keeps production remediation human-gated, with no-op rollback guards preceding any mutating execution; its proactive loop is budgeted and read-only for investigation. Hyrule MCP rejects mutative SSH commands unless explicit action gates are enabled and caps heavy diagnostics server-side. Hyrule Network Proxy must not expose its internal API publicly and must not log sensitive headers or bodies.

Citations: `generated/projects/network-operations`, `generated/services/engineering-loop`, `generated/services/noc-agent`, `generated/services/hyrule-mcp`, `generated/services/hyrule-network-proxy`

# Technology Stack Summary

The AS215932 service portfolio uses a consistent Python-based backend stack: FastAPI and uvicorn for HTTP services, httpx for HTTP client calls, structlog for structured logging, and langgraph for agentic/autonomous loop services (NOC Agent, Engineering Loop, network-operations). asyncpg is used by Hyrule Cloud for PostgreSQL access. The MCP protocol library (`mcp`) is used by both Hyrule MCP and the NOC Agent. The Hyrule Network Proxy is implemented in Go. The Hyrule Web frontend uses Vite, TypeScript, TailwindCSS, vitest, and WalletConnect. Infrastructure automation uses Ansible with Jinja2 templating, and the network stack includes FRRouting, BGP, OSPFv3, WireGuard, RPKI, IRR, and XCP-NG.

Citations: `generated/services/hyrule-cloud`, `generated/services/hyrule-web`, `generated/services/noc-agent`, `generated/services/hyrule-mcp`, `generated/services/engineering-loop`, `generated/services/hyrule-network-proxy`, `generated/projects/network-operations`

# Claims

* AS215932 (Hyrule Networks) is building a complete ISP from scratch, including BGP/OSPFv3 routing, IXP peering, and automation, and is doing so in public. — citations: `['generated/projects/network-operations', 'https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/README.md#L1-L207']`
* The network-operations project owns the production deployment record, Ansible inventory, workflow gates, and application version pins for AS215932. — citations: `['generated/projects/network-operations', 'https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/README.md#L1-L207']`
* Production applies in network-operations require human approval through GitHub 'production' environment gates. — citations: `['generated/projects/network-operations', 'https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/AGENTS.md#L1-L53']`
* Every live deployment in network-operations must compare Icinga snapshots before and after the change. — citations: `['generated/projects/network-operations', 'https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/AGENTS.md#L1-L53']`
* Firewall changes in network-operations must update docs/network-flows.md, host vars, and rendered artifacts together. — citations: `['generated/projects/network-operations', 'https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/AGENTS.md#L1-L53']`
* Hyrule Cloud is an agentic VPS hosting API with x402 payment gating, deployed on host `api`. — citations: `['generated/services/hyrule-cloud', 'https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/README.md#L1-L180']`
* Hyrule Cloud coordinates VM lifecycle, DNS, XCP-NG, PostgreSQL state, domain registration, and paid diagnostic/network resources. — citations: `['generated/services/hyrule-cloud', 'https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/README.md#L1-L180']`
* Hyrule Cloud is pinned to commit 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5 in the network-operations deployment inventory. — citations: `['generated/services/hyrule-cloud']`
* Hyrule Web is a server-rendered public website and Hyrule Cloud order/dashboard frontend, deployed on host `web`, pinned to commit d94146e67f9eb05f8eeb5c57cab74cbe676f5c79. — citations: `['generated/services/hyrule-web', 'https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/README.md#L1-L17']`
* Hyrule Web ships committed Vite assets for hosts without Node in production. — citations: `['generated/services/hyrule-web', 'https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/README.md#L1-L17']`
* The NOC Agent is deployed on host `noc`, pinned to commit 98e5010648e34ac0ea6ad8e6a925fef76d0dbea9, and handles alert intake, incident analysis, proactive hotspot scanning, and operator approval. — citations: `['generated/services/noc-agent', 'https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/README.md#L1-L240']`
* The NOC Agent consumes Hyrule MCP telemetry and stops at reviewable, human-gated proposals; production remediation remains human-gated. — citations: `['generated/services/noc-agent', 'https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/README.md#L1-L240']`
* The NOC Agent's proactive loop is budgeted and read-only for investigation, handing changes to engineering-loop issues. — citations: `['generated/services/noc-agent', 'https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/README.md#L1-L240']`
* Hyrule MCP is a read-biased, bounded live diagnostic MCP substrate deployed on host `noc`, pinned to commit 326bcc85e1c69f0d7c1839ebaa4abb73acd84185. — citations: `['generated/services/hyrule-mcp', 'https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/README.md#L1-L177']`
* Hyrule MCP rejects mutative SSH commands unless explicit action gates are enabled, and caps heavy diagnostics server-side. — citations: `['generated/services/hyrule-mcp', 'https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/README.md#L1-L177']`
* The Engineering Loop is an autonomous development loop built on LangGraph, deployed on host `loop`, pinned to commit 768cde6c996e42f3f91d395347ba9809e2e020e5. — citations: `['generated/services/engineering-loop', 'https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/README.md#L1-L75']`
* The Engineering Loop stops at draft PR for human review; merges and production applies remain human-gated. — citations: `['generated/services/engineering-loop', 'https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/README.md#L1-L75']`
* The Engineering Loop must not run on privileged GitHub Actions contexts with untrusted code. — citations: `['generated/services/engineering-loop', 'https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/README.md#L1-L75']`
* The Hyrule Network Proxy is an internal sidecar for x402-gated network requests, deployed on host `netproxy`, pinned to commit b82dc72bbf382167062bff272606ce84ec20538c, and implemented in Go. — citations: `['generated/services/hyrule-network-proxy', 'https://github.com/AS215932/hyrule-network-proxy/blob/b82dc72bbf382167062bff272606ce84ec20538c/README.md#L1-L98']`
* The Hyrule Network Proxy enforces egress policy and supports explicit direct/Tor/I2P/Yggdrasil modes. — citations: `['generated/services/hyrule-network-proxy', 'https://github.com/AS215932/hyrule-network-proxy/blob/b82dc72bbf382167062bff272606ce84ec20538c/README.md#L1-L98']`
* The Hyrule Network Proxy's internal API must not be public, and bodies, payment headers, authorization headers, and cookies must not be logged. — citations: `['generated/services/hyrule-network-proxy', 'https://github.com/AS215932/hyrule-network-proxy/blob/b82dc72bbf382167062bff272606ce84ec20538c/AGENTS.md#L1-L21']`
* as215932.net is a static informational website presenting ASN facts, peering policy, a network weathermap, prefix allocations, and a stub for an upcoming Looking Glass. — citations: `['generated/services/as215932-net', 'https://github.com/AS215932/as215932.net/blob/9c0ee2d8f2bb793ea799589ca0fe4f77571b2572/README.md#L1-L54']`
* The hyrule-business project contains private business planning and profitability notes covering hosting economics, pricing, and strategy; its primary indexed source is hosting-cost-analysis.md. — citations: `['generated/projects/hyrule-business', 'https://github.com/AS215932/hyrule-business/blob/89febc9c95fb6766df071e054cb44fba0b1ec8e4/hosting-cost-analysis.md#L1-L174']`
* LangGraph is a shared dependency across the Engineering Loop, NOC Agent, and network-operations project. — citations: `['generated/services/engineering-loop', 'generated/services/noc-agent', 'generated/projects/network-operations']`
* FastAPI and uvicorn are used as the HTTP framework and server across Hyrule Cloud, Hyrule Web, Hyrule MCP, and the NOC Agent. — citations: `['generated/services/hyrule-cloud', 'generated/services/hyrule-web', 'generated/services/hyrule-mcp', 'generated/services/noc-agent']`
* The network-operations project has an open issue (#272) to skip the heavy IaC matrix on app-promotion CI runs. — citations: `['generated/projects/network-operations', 'https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/README.md#L1-L207']`
* The Engineering Loop has an open issue (#6) where the loop records cost_usd: 0.0 because the PiBackend uses text mode but the parser expects JSON. — citations: `['generated/services/engineering-loop', 'https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/README.md#L1-L75']`
* Hyrule MCP has multiple open issues for new diagnostic tools including firewall_state, ndp_state, arp_state, multi_source_probe, ecmp_path_select, service_restart_history, and vault_agent_status. — citations: `['generated/services/hyrule-mcp', 'https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/README.md#L1-L177']`
* as215932.net has an open issue (#2) to add a lint/link-check gate and make it a required CI step. — citations: `['generated/services/as215932-net', 'https://github.com/AS215932/as215932.net/blob/9c0ee2d8f2bb793ea799589ca0fe4f77571b2572/README.md#L1-L54']`
* The network-operations project's operational runbook is located at docs/ci/deploy-runbook.md. — citations: `['generated/projects/network-operations', 'https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/README.md#L1-L207']`
* Hyrule Web includes a /transparency route and a /llms.txt route in its public interface. — citations: `['generated/services/hyrule-web', 'https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/README.md#L1-L17']`
* The NOC Agent exposes webhook endpoints for both Alertmanager (/webhook/alertmanager) and Icinga (/webhook/icinga). — citations: `['generated/services/noc-agent', 'https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/README.md#L1-L240']`
* Hyrule Cloud exposes BGP pricing and lookup endpoints including GET /v1/bgp/pricing and POST /v1/bgp/lookup/quote. — citations: `['generated/services/hyrule-cloud', 'https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/README.md#L1-L180']`
* Hyrule Web uses WalletConnect as a frontend dependency, consistent with the x402 payment model used by Hyrule Cloud. — citations: `['generated/services/hyrule-web', 'generated/services/hyrule-cloud']`
