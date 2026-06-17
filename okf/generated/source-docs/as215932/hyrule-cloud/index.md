# generated/source-docs/as215932/hyrule-cloud

* [--- VM status and size enums ---](alembic-versions-001-initial-schema-py.md) - """initial schema
* [002_security_hotfix.py](alembic-versions-002-security-hotfix-py.md) - """security hotfix: anon management token for VM management gating
* [005_provisioned_at.py](alembic-versions-005-provisioned-at-py.md) - """Block B: vms.provisioned_at column for live avg-provision metric
* [007_recovery_challenges.py](alembic-versions-007-recovery-challenges-py.md) - """Block F: server-side nonce store for wallet-signature recovery.
* [009_domain_launch_fields.py](alembic-versions-009-domain-launch-fields-py.md) - """domain launch ownership and pricing fields
* [010_network_intelligence_bgp_mx_mail.py](alembic-versions-010-network-intelligence-bgp-mx-mail-py.md) - """network intelligence, bgp, mx, and agent mail tables
* [011_diagnostic_job_primitives.py](alembic-versions-011-diagnostic-job-primitives-py.md) - """generic diagnostic job primitives
* [Account-based VM ownership. Existing rows get NULL (preserves anon-by-token flow).](alembic-versions-003-auth-and-ownership-py.md) - """auth subsystem + account-based VM ownership
* [Full crypto_intent_status value set: the legacy toy `pending`/`paid` plus the](alembic-versions-004-intent-engine-py.md) - """native crypto intent engine: state machine + idempotency + ownership link
* [Hyrule Agent Mail Skill](skill-mail.md) - Hyrule Agent Mail is the planned paid mailbox product for AI agents. The API contract is stable now; the backend adapter can be Stalwart, Postfix/Dovecot, Rspamd, or another mail backend hidden behind this API.
* [Hyrule Agentic ISP Support Skill](skill-agentic-support.md) - Hyrule Agentic ISP Support is the umbrella Skill for x402-paid network facts that LLMs cannot infer: live reachability, DNS, BGP, mail deliverability, routing/path evidence, TLS, reputation, VoIP, NAT hints, speedtests, and AS215932-back...
* [Hyrule BGP Data Skill](skill-bgp.md) - Hyrule BGP Data provides free AS215932 status plus paid public/global BGP intelligence for agents.
* [Hyrule Cloud](claude.md) - Agentic VPS hosting API on AS215932, paid via x402 (USDC on Base). Agents discover the service via x402 Bazaar or `/.well-known/x402.json`, pay per-request, and receive bare VMs with SSH access, automatic DNS subdomains, and IPv6-native...
* [Hyrule Cloud](readme.md) - Agentic VPS hosting on Hyrule Networks (AS215932) with x402 payments.
* [Hyrule Cloud Agent Guide](agents.md) - - `hyrule.host` is customer-facing Hyrule Cloud/product identity. Public API clients use `https://cloud.hyrule.host`; automatic VM hostnames live under `deploy.hyrule.host`. - `servify.network` is infrastructure identity for nameservers,...
* [Hyrule Cloud — Agentic VPS Hosting](skill.md) - Deploy bare VMs, register domains, and manage DNS zones — all paid via x402 (USDC on Base).
* [Hyrule DNS and Registry Skill](skill-dns-registry.md) - Use Hyrule Cloud when an AI agent needs read-only DNS, DNSSEC, propagation, RDAP, WHOIS, registrar/delegation, or record-publication guidance.
* [Hyrule Mail Deliverability Skill](skill-mail-deliverability.md) - Use Hyrule Cloud when an AI agent needs to diagnose missing, rejected, delayed, or spam-filtered email for any public domain. This Skill is a marketing/support wrapper over the canonical `/v1/mx` API.
* [Hyrule MX Diagnostics Skill](skill-mx.md) - Hyrule MX Diagnostics is a paid, MXToolbox-compatible troubleshooting API for AI agents and ISP support automation. Hyrule implements the checks internally; it is not affiliated with MXToolbox and does not scrape MXToolbox.
* [Hyrule NAT/CGNAT Skill](skill-nat-cgnat.md) - Use Hyrule Cloud when an AI agent needs server-side NAT or CGNAT hints for a customer. This MVP does not require browser/WebRTC/STUN participation.
* [Hyrule Network Intelligence Skill](skill-network-intel.md) - Use Hyrule Cloud for paid, agent-friendly network intelligence primitives.
* [Hyrule Port Reachability Skill](skill-port-reachability.md) - Use Hyrule Cloud when an AI agent needs to answer whether one declared public service is reachable from outside.
* [Hyrule Routing Path Skill](skill-routing-path.md) - Use Hyrule Cloud when an AI agent needs to decide whether an outage is likely customer LAN, AS215932, remote ISP, remote host, routing/BGP/RPKI, or inconclusive.
* [Hyrule Speedtest Skill](skill-speedtest.md) - Use Hyrule Cloud when an AI agent needs throughput, latency, jitter, and path evidence between a client and Hyrule/AS215932 endpoints.
* [Hyrule Threat Reputation Skill](skill-threat-reputation.md) - Use Hyrule Cloud when an AI agent needs open-source-first domain, IP, RBL, certificate transparency, RDAP/WHOIS, or reputation context.
* [Hyrule VoIP/SIP Skill](skill-voip-sip.md) - Use Hyrule Cloud when an AI agent needs SIP DNS, SIP TLS, SIP OPTIONS, STUN/TURN, number carrier, CNAM, number spam reputation, or E911 diagnostic context.
* [Hyrule Web Reachability Skill](skill-web-reachability.md) - Use Hyrule Cloud when an AI agent needs live, paid evidence for public website reachability, TLS/certificate failures, HTTP behavior, security headers, and CDN/WAF hints.
* [Values MATCH hyrule_cloud.models.QuoteStatus so an alembic-migrated DB and a](alembic-versions-008-vm-quotes-py.md) - """vm_quotes: durable order quotes (issue #14)
* [x402 official SDK (x402-foundation)](pyproject-toml.md) - [project] name = "hyrule-cloud" version = "0.1.0" description = "Agentic VPS hosting with x402 payments on AS215932" requires-python = ">=3.12" dependencies = [ "fastapi>=0.115", "uvicorn[standard]>=0.34", "pydantic>=2.10", "pydantic-set...
