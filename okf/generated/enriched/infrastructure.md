---
type: Reference
title: AS215932 Infrastructure Knowledge Base
description: A comprehensive OKF enrichment of AS215932's network infrastructure,
  covering all Ansible-managed hosts, routers, network prefixes, DNS zones, deployment
  pins, monitoring configuration, and CI/CD workflows as derived from the AS215932/network-operations
  repository and associated service repositories.
tags:
- enriched
- infrastructure
- llm
truth_owner: derived
authority: advisory
source_refs:
- repo: AS215932/network-operations
  path: ansible/inventory/hosts.yml
  commit: fe46c3c3580ff79e8009ca839ab579f0691b55b8
  url: https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/hosts.yml
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/loop.yml
  commit: fe46c3c3580ff79e8009ca839ab579f0691b55b8
  url: https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/host_vars/loop.yml
- repo: AS215932/network-operations
  path: ansible/inventory/hosts.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/api.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/api.yml
- repo: AS215932/network-operations
  path: ansible/inventory/hosts.yml
  commit: fe46c3c3580ff79e8009ca839ab579f0691b55b8
  url: https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/hosts.yml
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/noc.yml
  commit: fe46c3c3580ff79e8009ca839ab579f0691b55b8
  url: https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/host_vars/noc.yml
- repo: AS215932/network-operations
  path: ansible/inventory/hosts.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/netproxy.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/netproxy.yml
- repo: AS215932/network-operations
  path: ansible/inventory/hosts.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/web.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/web.yml
- repo: AS215932/network-operations
  path: ansible/inventory/hosts.yml
  commit: fe46c3c3580ff79e8009ca839ab579f0691b55b8
  url: https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/hosts.yml
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/noc.yml
  commit: fe46c3c3580ff79e8009ca839ab579f0691b55b8
  url: https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/host_vars/noc.yml
- repo: AS215932/network-operations
  path: configs/0.5.b.0.1.4.6.b.c.0.a.2.ip6.arpa.zone
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/0.5.b.0.1.4.6.b.c.0.a.2.ip6.arpa.zone
- repo: AS215932/network-operations
  path: configs/as215932.net.zone
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/as215932.net.zone
- repo: AS215932/network-operations
  path: configs/deploy.hyrule.host.zone
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/deploy.hyrule.host.zone
- repo: AS215932/network-operations
  path: configs/hyrule.host.zone
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/hyrule.host.zone
- repo: AS215932/network-operations
  path: configs/servify.network.zone
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/servify.network.zone
- repo: AS215932/network-operations
  path: ansible/inventory/hosts.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/api.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/api.yml
- repo: AS215932/network-operations
  path: ansible/inventory/hosts.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/ci-pr.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/ci-pr.yml
- repo: AS215932/network-operations
  path: ansible/inventory/hosts.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/ci.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/ci.yml
- repo: AS215932/network-operations
  path: ansible/inventory/hosts.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/cr1-ch1.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/cr1-ch1.yml
- repo: AS215932/network-operations
  path: ansible/inventory/hosts.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/cr1-de1.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/cr1-de1.yml
- repo: AS215932/network-operations
  path: ansible/inventory/hosts.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/cr1-nl1.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/cr1-nl1.yml
- repo: AS215932/network-operations
  path: ansible/inventory/hosts.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml
last_verified_at: '2026-06-23T11:19:14Z'
confidence: medium
dispute_policy: repo_wins
review_status: reviewed
reviewed_by: svag
reviewed_at: '2026-06-23T14:05:00Z'
review_note: Human-approved as useful advisory synthesis; repo source truth continues to win on conflict.
enrichment:
  mode: llm
  provider: openrouter
  model: anthropic/claude-sonnet-4.6
  prompt_version: useful-v1
  input_hash: 8617ebda3c108d064f3a32775328cc39164fa9df4d0d8c86156d6f2232fc36c4
  output_hash: dac80f21907d64c9cdccaaad290e2006a1850eacf4579303601baa5507e9cf5b
  generated_at: '2026-06-23T11:19:14Z'
enrichment_json: '{"generated_at":"2026-06-23T11:19:14Z","input_hash":"8617ebda3c108d064f3a32775328cc39164fa9df4d0d8c86156d6f2232fc36c4","mode":"llm","model":"anthropic/claude-sonnet-4.6","output_hash":"dac80f21907d64c9cdccaaad290e2006a1850eacf4579303601baa5507e9cf5b","prompt_version":"useful-v1","provider":"openrouter"}'
---

# LLM enrichment

Review status: proposed. Treat this as advisory until human-reviewed.

# Network Prefixes and Addressing

AS215932 operates under the aggregate prefix 2a0c:b641:b50::/44 (variable `as215932_prefix`). The infrastructure VM subnet is 2a0c:b641:b50:2::/64 (`infra_subnet`), router loopbacks occupy 2a0c:b641:b50::/64 (`router_loopback_subnet`), VPN clients are assigned from 2a0c:b641:b50:3::/64 (`vpn_clients_subnet`), the Engineering Loop Docker subnet is 2a0c:b641:b50:f0::/64 (`loop_docker_subnet`), WireGuard point-to-point links use 2a0c:b641:b50:ff00::/56 (`wg_link_prefix`), and customer allocations fall within 2a0c:b641:b51::/48 (`customer_subnet`). All prefix values are sourced from the Ansible group_vars.

Citations: `generated/infrastructure/prefixes/as215932-prefix`, `generated/infrastructure/prefixes/infra-subnet`, `generated/infrastructure/prefixes/router-loopback-subnet`, `generated/infrastructure/prefixes/vpn-clients-subnet`, `generated/infrastructure/prefixes/loop-docker-subnet`, `generated/infrastructure/prefixes/wg-link-prefix`, `generated/infrastructure/prefixes/customer-subnet`

# Infrastructure Hosts — VM Fleet

The core infrastructure VM fleet runs on the 2a0c:b641:b50:2::/64 subnet and is managed via Ansible (groups `infra_vms, linux` unless noted). Key hosts and their IPv6 addresses are: `rtr` (2a0c:b641:b50:2::1, Debian 13 + FRRouting, public-facing router/gateway), `dns` (2a0c:b641:b50:2::10, Knot primary authoritative DNS / ns1), `api` (2a0c:b641:b50:2::20, Hyrule Cloud FastAPI + PostgreSQL), `web` (2a0c:b641:b50:2::30, hyrule-web uvicorn + nginx), `proxy` (2a0c:b641:b50:2::40, Caddy TLS reverse proxy), `mon` (2a0c:b641:b50:2::50, Prometheus + Grafana + Icinga2), `vpn` (2a0c:b641:b50:2::60, WireGuard server), `xoa` (2a0c:b641:b50:2::70, Xen Orchestra), `irc` (2a0c:b641:b50:2::80, Soju IRC bouncer), `mail` (2a0c:b641:b50:2::90, OpenBSD OpenSMTPD + Dovecot), `noc` (2a0c:b641:b50:2::a0, NOC agent + hyrule-mcp), `log` (2a0c:b641:b50:2::b0, centralized log aggregation via Vector + Loki), `vault` (2a0c:b641:b50:2::c0, HashiCorp Vault secret plane), `ci` (2a0c:b641:b50:2::d0, self-hosted GitHub Actions runner), `netproxy` (2a0c:b641:b50:2::e0, Hyrule Network Proxy sidecar), and `loop` (2a0c:b641:b50:2::f0, Engineering Loop dedicated VM). Additional hosts include `dom0` (193.70.32.138, XCP-NG hypervisor on OVH RISE-S), `ns2` (2001:41d0:304:300::7bfb, secondary nameserver at OVH GRA11), `ci-pr` (2a0c:b641:b51::c1, unprivileged GitHub Actions runner for untrusted PR code), and `extmon` (external monitoring host).

Citations: `generated/infrastructure/hosts/rtr`, `generated/infrastructure/hosts/dns`, `generated/infrastructure/hosts/api`, `generated/infrastructure/hosts/web`, `generated/infrastructure/hosts/proxy`, `generated/infrastructure/hosts/mon`, `generated/infrastructure/hosts/vpn`, `generated/infrastructure/hosts/xoa`, `generated/infrastructure/hosts/irc`, `generated/infrastructure/hosts/mail`, `generated/infrastructure/hosts/noc`, `generated/infrastructure/hosts/host-log`, `generated/infrastructure/hosts/vault`, `generated/infrastructure/hosts/ci`, `generated/infrastructure/hosts/netproxy`, `generated/infrastructure/hosts/loop`, `generated/infrastructure/hosts/dom0`, `generated/infrastructure/hosts/ns2`, `generated/infrastructure/hosts/ci-pr`, `generated/infrastructure/hosts/extmon`

# Router Fleet

AS215932 operates four routers running FRRouting. `rtr` (loopback 2a0c:b641:b50::d, underlay 2001:41d0:303:48a::2) is a Debian 13 + FRRouting VM hosted at OVH FR, serving as the primary gateway with iBGP peering to the three core routers over WireGuard. `cr1-nl1` (loopback 2a0c:b641:b50::a, underlay 2a0c:b640:8:69::1) runs FreeBSD 14.3 + FRRouting at Servperso NL with IXP connectivity (`ixp_nl`). `cr1-de1` (loopback 2a0c:b641:b50::b, underlay 2a0c:b640:10::213) runs FreeBSD 15.0 + FRRouting at Servperso DE with transit and IXP interfaces (`transit2_if`, `ixp_dus`, `ixp_fra`). `cr1-ch1` (loopback 2a0c:b641:b50::c, underlay 2a09:4c0:100:2d88::8898) runs FreeBSD 14.4 + FRRouting at Securebit CH with IXP connectivity (`ixp_4ixp`, `ixp_sbix`). All routers expose node_exporter (tcp/9100) and frr_exporter (tcp/9342) to the `mon` host, and use pf (FreeBSD) or nftables (Linux) firewalls.

Citations: `generated/infrastructure/hosts/rtr`, `generated/infrastructure/hosts/cr1-nl1`, `generated/infrastructure/hosts/cr1-de1`, `generated/infrastructure/hosts/cr1-ch1`

# DNS Zones

AS215932 manages five DNS zones via Knot authoritative DNS (primary on `dns`, secondary on `ns2`). The `as215932.net` zone (TTL 3600) contains 30 records including AAAA records for all infrastructure hosts, MX pointing to mail.as215932.net, SPF/DMARC/DKIM TXT records, and an A record. The `hyrule.host` zone (TTL 3600) contains 18 records with dual-stack A/AAAA, MX, SPF/DMARC/DKIM, and a Google site verification TXT. The `servify.network` zone (TTL 3600) contains 34 records including ns1/ns2 A and AAAA glue records. The `deploy.hyrule.host` zone (TTL 300) contains only NS and SOA records. The reverse zone `0.5.b.0.1.4.6.b.c.0.a.2.ip6.arpa` contains 19 PTR records mapping infrastructure IPv6 addresses to hostnames (e.g., rtr, dns, api, web, proxy, mon, vpn, xoa, irc). All zones use ns1.servify.network and ns2.servify.network as authoritative nameservers.

Citations: `generated/infrastructure/dns-zones/as215932-net`, `generated/infrastructure/dns-zones/hyrule-host`, `generated/infrastructure/dns-zones/servify-network`, `generated/infrastructure/dns-zones/deploy-hyrule-host`, `generated/infrastructure/dns-zones/0-5-b-0-1-4-6-b-c-0-a-2-ip6-arpa`

# Service Deployment Pins

Application versions are pinned via Ansible host_vars variables. The intended deployment state (not confirmed runtime state) is as follows: Hyrule Cloud (`hyrule_cloud_version`) is pinned to commit `81e4316f3d1f4e7f770bc2589bd84a2c7972aad5` on host `api`. Hyrule Web (`hyrule_web_version`) is pinned to `d94146e67f9eb05f8eeb5c57cab74cbe676f5c79` on host `web`. Hyrule Network Proxy (`hyrule_network_proxy_version`) is pinned to `b82dc72bbf382167062bff272606ce84ec20538c` on host `netproxy`. Hyrule MCP (`hyrule_mcp_version`) is pinned to `05b1245710e6a67ad40ccd62c033755f48ad4958` on host `noc`. Hyrule NOC Agent (`noc_agent_version`) is pinned to `be0924a2903568558f0ce81370d6e1a099fc1bee` on host `noc`. Engineering Loop (`engineering_loop_version`) is pinned to `eb37b1c4d1d7c3f349c8c6cdb3bd890f168c2755` on host `loop`. The `loop` host also pins `knowledge_mcp_version` to `5a6666cbb9d290868db3fb854ffed39099515b91`, and `noc` pins `noc_knowledge_version` to the same commit. Runtime state requires observed evidence from `okf/observed/` to confirm.

Citations: `generated/deployments/hyrule-cloud-on-api`, `generated/deployments/hyrule-web-on-web`, `generated/deployments/hyrule-network-proxy-on-netproxy`, `generated/deployments/hyrule-mcp-on-noc`, `generated/deployments/noc-agent-on-noc`, `generated/deployments/engineering-loop-on-loop`, `generated/infrastructure/hosts/loop`, `generated/infrastructure/hosts/noc`

# Monitoring Architecture

The `mon` host (2a0c:b641:b50:2::50) runs Prometheus, Grafana, Icinga2, and blackbox_exporter. All infrastructure hosts expose node_exporter on tcp/9100 to `mon`. Routers additionally expose frr_exporter on tcp/9342. The `api` host exposes postgres_exporter on tcp/9187. Icinga2 service checks cover: bgp, cr-bogon-egress, disk, dns, dns-soa-ecmp, github-runner, host-ping6, http, nat64, noc-agent-mail-health, noc-agent-mcp-health, noc-agent-model-health, noc-agent-uptime, node-up, postgres, prometheus, rtr-checks, ssh, ssl, underlay, and wireguard. Custom check scripts include check_dns_soa_ecmp.py, check_jool_success_delta.sh, check_noc_agent_mail_health.sh, check_noc_agent_mcp_health.sh, and check_noc_agent_model_health.sh. Alertmanager and Discord webhook notifications are configured. The `mon` host accepts Icinga2 API connections from `noc` (tcp/5665) and passive check submissions from `loop` (tcp/5665), and Prometheus API queries from `noc` (tcp/9090).

Citations: `generated/monitoring/network-operations-monitoring`, `generated/infrastructure/hosts/mon`, `generated/infrastructure/hosts/noc`, `generated/infrastructure/hosts/loop`

# Log Aggregation

The `log` host (2a0c:b641:b50:2::b0) serves as the centralized log aggregation point running Vector (aggregator) and Loki. It accepts Vector native protocol on tcp/6000 from all infrastructure hosts (rtr, dns, api, web, proxy, mon, vpn, xoa, irc, noc, ci, loop, cr1-nl1, cr1-de1, ns2, dom0 via mgmt v4), syslog over TCP on tcp/6514 from mail and the cr1-* routers, Loki HTTP API on tcp/3100 from mon (Grafana), and Vector internal metrics scrape on tcp/8686 from mon. The `log` host has a 4 GiB disk buffer (`logs_agent_disk_buffer_bytes: 4294967296`). Monitoring checks include `vector-aggregator` (tcp) and `loki-ready` (http).

Citations: `generated/infrastructure/hosts/host-log`

# NOC Agent and Engineering Loop

The `noc` host (2a0c:b641:b50:2::a0) runs the autonomous NOC agent (`noc_agent_version: be0924a2903568558f0ce81370d6e1a099fc1bee`), hyrule-mcp tool server (`hyrule_mcp_version: 05b1245710e6a67ad40ccd62c033755f48ad4958`), and noc-knowledge (`noc_knowledge_version: 5a6666cbb9d290868db3fb854ffed39099515b91`). The NOC agent listens on tcp/8000 and accepts connections from `mon` (Alertmanager/Icinga webhooks), `proxy` (control dashboard), and `loop` (LHP-v1 Engineering Loop fetch/callback). Case auto-resolve is disabled; case verification is enabled in non-dry-run mode; disk alert handoff and engineering handoff delivery are enabled. The `loop` host (2a0c:b641:b50:2::f0) is a dedicated Engineering Loop VM running `engineering_loop_version: eb37b1c4d1d7c3f349c8c6cdb3bd890f168c2755` and `knowledge_mcp_version: 5a6666cbb9d290868db3fb854ffed39099515b91`. The loop timer is enabled and the LHP callback to noc-agent is active. Allowed repository paths for the loop are `hyrule-cloud` (hyrule_cloud, tests, scripts, docs) and `hyrule-web` (frontend, hyrule_web, tests). The Knowledge MCP server listens on 127.0.0.1:8767 using streamable-http transport.

Citations: `generated/infrastructure/hosts/noc`, `generated/infrastructure/hosts/loop`, `generated/deployments/noc-agent-on-noc`, `generated/deployments/hyrule-mcp-on-noc`, `generated/deployments/engineering-loop-on-loop`

# CI/CD Workflows and Promotion Pipeline

AS215932 uses a GitOps promotion pipeline across multiple repositories. Application repositories (hyrule-cloud, hyrule-web, hyrule-mcp, noc-agent) each have a `request-promotion` workflow (triggered on workflow_dispatch/workflow_run) that uses `PROMOTION_APP_ID` and `PROMOTION_APP_PRIVATE_KEY` secrets to request promotion. The `network-operations` repository has a `promote-apps` workflow (triggered on repository_dispatch/workflow_dispatch, requires `contents: write`) that updates version pins, and an `app-promotion-deploy` workflow that detects and applies promotions. The `apply` workflow (workflow_dispatch/workflow_call) runs Ansible against the `hyrule-infra` runner in either `dry-run` or `production` environment. A `drift-detection` workflow runs on schedule to detect configuration drift. IaC tests (`iac-tests`) run Batfish network analysis, ContainerLab FRR tests, and Ansible idempotency checks. A `netops-nightly` workflow runs full Batfish and ContainerLab suites nightly. All repositories also run `semgrep` for SAST and `pr-agent` for AI-assisted PR review using `OPENROUTER_API_KEY`. The `hyrule-network-proxy` CI runs on `ubuntu-latest` (not self-hosted). The `ci-pr` host provides the `hyrule-public-pr` runner label for untrusted PR code; the `ci` host provides the `hyrule-infra` runner for privileged operations.

Citations: `generated/workflows/network-operations/github-workflows-promote-apps-yml`, `generated/workflows/network-operations/github-workflows-app-promotion-deploy-yml`, `generated/workflows/network-operations/github-workflows-apply-yml`, `generated/workflows/network-operations/github-workflows-drift-detection-yml`, `generated/workflows/network-operations/github-workflows-iac-tests-yml`, `generated/workflows/network-operations/github-workflows-netops-nightly-yml`, `generated/workflows/hyrule-cloud/github-workflows-request-promotion-yml`, `generated/workflows/hyrule-web/github-workflows-request-promotion-yml`, `generated/workflows/hyrule-mcp/github-workflows-request-promotion-yml`, `generated/workflows/noc-agent/github-workflows-request-promotion-yml`, `generated/workflows/hyrule-network-proxy/github-workflows-ci-yml`, `generated/infrastructure/hosts/ci`, `generated/infrastructure/hosts/ci-pr`

# Hypervisor and Secret Management

The `dom0` host (193.70.32.138) is an XCP-NG hypervisor running on an OVH RISE-S server, hosting the majority of the infrastructure VMs. It is managed via Ansible in the `xcpng` group. Xen Orchestra (`xoa`, 2a0c:b641:b50:2::70) provides the management UI, with its management NIC reaching dom0 XAPI and its infra NIC serving the UI via the `proxy` host. The `vault` host (2a0c:b641:b50:2::c0) provides the machine secret plane using HashiCorp Vault, accessible on tcp/8200 from proxy, internal agents (noc, mon, api, web, ci, loop), VPN operators, and the ops prefix. A `vault-health` monitoring check verifies the seal/standby health endpoint.

Citations: `generated/infrastructure/hosts/dom0`, `generated/infrastructure/hosts/xoa`, `generated/infrastructure/hosts/vault`

# Mail and IRC Services

The `mail` host (2a0c:b641:b50:2::90) runs OpenBSD with OpenSMTPD and Dovecot, serving as the mail server for as215932.net and hyrule.host. It accepts SMTP (tcp/25), SMTPS (tcp/465), and submission STARTTLS (tcp/587) from any source, and IMAPS (tcp/993) restricted to ops prefix, VPN clients, mon, and noc. ManageSieve (tcp/4190) is restricted to ops prefix and VPN clients. DKIM is configured for both as215932.net and hyrule.host. Role addresses include noc, abuse, peering, dh, and support. The `irc` host (2a0c:b641:b50:2::80) runs Soju IRC bouncer, accepting IRCS connections on tcp/6697 from any source. Both hosts are monitored for TLS certificate validity.

Citations: `generated/infrastructure/hosts/mail`, `generated/infrastructure/hosts/irc`

# Claims

* AS215932's aggregate IPv6 prefix is 2a0c:b641:b50::/44, as defined by the `as215932_prefix` variable in Ansible group_vars. — citations: `['generated/infrastructure/prefixes/as215932-prefix']`
* The infrastructure VM subnet is 2a0c:b641:b50:2::/64 (`infra_subnet`). — citations: `['generated/infrastructure/prefixes/infra-subnet']`
* Customer allocations are served from 2a0c:b641:b51::/48 (`customer_subnet`). — citations: `['generated/infrastructure/prefixes/customer-subnet']`
* VPN clients are assigned addresses from 2a0c:b641:b50:3::/64 (`vpn_clients_subnet`). — citations: `['generated/infrastructure/prefixes/vpn-clients-subnet']`
* The Engineering Loop Docker subnet is 2a0c:b641:b50:f0::/64 (`loop_docker_subnet`). — citations: `['generated/infrastructure/prefixes/loop-docker-subnet']`
* WireGuard point-to-point link addresses are drawn from 2a0c:b641:b50:ff00::/56 (`wg_link_prefix`). — citations: `['generated/infrastructure/prefixes/wg-link-prefix']`
* Router loopback addresses occupy 2a0c:b641:b50::/64 (`router_loopback_subnet`). — citations: `['generated/infrastructure/prefixes/router-loopback-subnet']`
* The `rtr` host is a Debian 13 + FRRouting VM at OVH FR with IPv6 address 2a0c:b641:b50:2::1, loopback 2a0c:b641:b50::d, and WAN IP 46.105.40.223. — citations: `['generated/infrastructure/hosts/rtr']`
* The `dns` host (2a0c:b641:b50:2::10) runs Knot authoritative DNS as the primary nameserver (ns1.servify.network) and accepts RFC 2136 dynamic DNS updates from api, proxy, and irc. — citations: `['generated/infrastructure/hosts/dns']`
* The `api` host (2a0c:b641:b50:2::20) runs Hyrule Cloud (FastAPI on tcp/8402) and PostgreSQL, with postgres_exporter exposed on tcp/9187 to mon. — citations: `['generated/infrastructure/hosts/api']`
* The `api` host has `hyrule_cloud_monero_wallet_rpc_enabled` set to True. — citations: `['generated/infrastructure/hosts/api']`
* The `web` host (2a0c:b641:b50:2::30) runs hyrule-web (uvicorn on tcp/8080) and nginx serving as215932.net (tcp/8081), both accessible only from proxy and mon. — citations: `['generated/infrastructure/hosts/web']`
* The `proxy` host (2a0c:b641:b50:2::40) runs Caddy as a TLS reverse proxy with ACME DNS-01 via RFC 2136 to the dns host, accepting HTTP (tcp/80) and HTTPS (tcp/443) from any source. — citations: `['generated/infrastructure/hosts/proxy']`
* The `mon` host (2a0c:b641:b50:2::50) runs Prometheus, Grafana, Icinga2, and blackbox_exporter. — citations: `['generated/infrastructure/hosts/mon']`
* The `vpn` host (2a0c:b641:b50:2::60) runs WireGuard for client tunnels, accepting UDP/51820 from any source, with clients in 2a0c:b641:b50:3::/64. — citations: `['generated/infrastructure/hosts/vpn']`
* The `xoa` host (2a0c:b641:b50:2::70) runs Xen Orchestra, with its management NIC reaching dom0 XAPI and its infra NIC serving the UI via proxy. — citations: `['generated/infrastructure/hosts/xoa']`
* The `irc` host (2a0c:b641:b50:2::80) runs Soju IRC bouncer, accepting IRCS connections on tcp/6697 from any source. — citations: `['generated/infrastructure/hosts/irc']`
* The `mail` host (2a0c:b641:b50:2::90) runs OpenBSD with OpenSMTPD and Dovecot, serving as215932.net and hyrule.host with DKIM configured for both domains. — citations: `['generated/infrastructure/hosts/mail']`
* The `noc` host (2a0c:b641:b50:2::a0) runs the autonomous NOC agent, hyrule-mcp tool server, and noc-knowledge, with noc_case_auto_resolve_enabled set to False and noc_case_verification_enabled set to True. — citations: `['generated/infrastructure/hosts/noc']`
* The `log` host (2a0c:b641:b50:2::b0) is the centralized log aggregation host running Vector and Loki, with a 4 GiB disk buffer, accepting Vector native protocol on tcp/6000 from all infrastructure hosts. — citations: `['generated/infrastructure/hosts/host-log']`
* The `vault` host (2a0c:b641:b50:2::c0) provides the machine secret plane using HashiCorp Vault, accessible on tcp/8200 from proxy, noc, mon, api, web, ci, loop, VPN operators, and the ops prefix. — citations: `['generated/infrastructure/hosts/vault']`
* The `ci` host (2a0c:b641:b50:2::d0) is a self-hosted GitHub Actions runner for AS215932/network-operations with a dedicated data disk at /dev/xvdi. — citations: `['generated/infrastructure/hosts/ci']`
* The `netproxy` host (2a0c:b641:b50:2::e0) is an internal Hyrule Network Proxy sidecar target, accepting connections from api on tcp/8450 and Prometheus scrape from mon on tcp/8451. — citations: `['generated/infrastructure/hosts/netproxy']`
* The `loop` host (2a0c:b641:b50:2::f0) is a dedicated Engineering Loop VM with the loop timer enabled, LHP callback to noc-agent active, and Knowledge MCP server listening on 127.0.0.1:8767 using streamable-http transport. — citations: `['generated/infrastructure/hosts/loop']`
* The `dom0` host (193.70.32.138) is an XCP-NG hypervisor on an OVH RISE-S server. — citations: `['generated/infrastructure/hosts/dom0']`
* The `ns2` host (2001:41d0:304:300::7bfb, IPv4 54.38.14.218) is the secondary authoritative nameserver at OVH GRA11, configured as a Knot secondary receiving zone transfers from the primary dns host. — citations: `['generated/infrastructure/hosts/ns2']`
* The `ci-pr` host (2a0c:b641:b51::c1) is an unprivileged self-hosted GitHub Actions runner for untrusted PR code, with the runner group `public-pr` and label `hyrule-public-pr`. Caddy RFC 2136 and ContainerLab are disabled on this host. — citations: `['generated/infrastructure/hosts/ci-pr']`
* The `extmon` host is an external monitoring host (Vultr/DigitalOcean/Hetzner Cloud) managing OVH failover IPs 46.105.40.223, 51.91.236.215, and 54.38.14.218. — citations: `['generated/infrastructure/hosts/extmon']`
* cr1-nl1 (loopback 2a0c:b641:b50::a) runs FreeBSD 14.3 + FRRouting at Servperso NL with IXP interface `ixp_nl` and WireGuard ports 1337, 1338, 1340, 1341. — citations: `['generated/infrastructure/hosts/cr1-nl1']`
* cr1-de1 (loopback 2a0c:b641:b50::b) runs FreeBSD 15.0 + FRRouting at Servperso DE with transit and IXP interfaces (transit2_if, ixp_dus, ixp_fra) and WireGuard ports 1337, 1338, 1342. — citations: `['generated/infrastructure/hosts/cr1-de1']`
* cr1-ch1 (loopback 2a0c:b641:b50::c) runs FreeBSD 14.4 + FRRouting at Securebit CH with IXP interfaces (ixp_4ixp, ixp_sbix) and WireGuard ports 1339, 1341, 1342. — citations: `['generated/infrastructure/hosts/cr1-ch1']`
* Hyrule Cloud is pinned to commit 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5 on host `api` via the `hyrule_cloud_version` Ansible variable. This is intended deployment state only. — citations: `['generated/deployments/hyrule-cloud-on-api']`
* Hyrule Web is pinned to commit d94146e67f9eb05f8eeb5c57cab74cbe676f5c79 on host `web` via the `hyrule_web_version` Ansible variable. This is intended deployment state only. — citations: `['generated/deployments/hyrule-web-on-web']`
* Hyrule Network Proxy is pinned to commit b82dc72bbf382167062bff272606ce84ec20538c on host `netproxy` via the `hyrule_network_proxy_version` Ansible variable. This is intended deployment state only. — citations: `['generated/deployments/hyrule-network-proxy-on-netproxy']`
* Hyrule MCP is pinned to commit 05b1245710e6a67ad40ccd62c033755f48ad4958 on host `noc` via the `hyrule_mcp_version` Ansible variable. This is intended deployment state only. — citations: `['generated/deployments/hyrule-mcp-on-noc']`
* Hyrule NOC Agent is pinned to commit be0924a2903568558f0ce81370d6e1a099fc1bee on host `noc` via the `noc_agent_version` Ansible variable. This is intended deployment state only. — citations: `['generated/deployments/noc-agent-on-noc']`
* The Engineering Loop is pinned to commit eb37b1c4d1d7c3f349c8c6cdb3bd890f168c2755 on host `loop` via the `engineering_loop_version` Ansible variable. This is intended deployment state only. — citations: `['generated/deployments/engineering-loop-on-loop']`
* The as215932.net DNS zone contains 30 parsed records including AAAA records for all infrastructure hosts, MX, SPF, DMARC, and DKIM TXT records, with a default TTL of 3600. — citations: `['generated/infrastructure/dns-zones/as215932-net']`
* The hyrule.host DNS zone contains 18 parsed records with dual-stack A/AAAA, MX, SPF/DMARC/DKIM TXT, and a Google site verification TXT record. — citations: `['generated/infrastructure/dns-zones/hyrule-host']`
* The servify.network DNS zone contains 34 parsed records including ns1 (46.105.40.223 / 2a0c:b641:b50:2::10) and ns2 (54.38.14.218 / 2001:41d0:304:300::7bfb) glue records. — citations: `['generated/infrastructure/dns-zones/servify-network']`
* The reverse zone 0.5.b.0.1.4.6.b.c.0.a.2.ip6.arpa contains 19 PTR records mapping infrastructure IPv6 addresses to hostnames including rtr, dns, api, web, proxy, mon, vpn, xoa, and irc. — citations: `['generated/infrastructure/dns-zones/0-5-b-0-1-4-6-b-c-0-a-2-ip6-arpa']`
* The deploy.hyrule.host DNS zone has a TTL of 300 and contains only NS and SOA records (3 total). — citations: `['generated/infrastructure/dns-zones/deploy-hyrule-host']`
* The monitoring stack on `mon` includes 21 Icinga2 service check types and custom scripts for DNS SOA ECMP, Jool NAT64 success delta, and NOC agent health checks (mail, MCP, model). — citations: `['generated/monitoring/network-operations-monitoring']`
* The `network-operations` repository has a `promote-apps` workflow with `contents: write` permission that handles version pin updates, triggered by repository_dispatch or workflow_dispatch. — citations: `['generated/workflows/network-operations/github-workflows-promote-apps-yml']`
* The `apply` workflow in network-operations runs Ansible on the `hyrule-infra` self-hosted runner and deploys to either `dry-run` or `production` GitHub environment based on the `dry_run` input. — citations: `['generated/workflows/network-operations/github-workflows-apply-yml']`
* The `drift-detection` workflow in network-operations runs on a schedule on the `hyrule-infra` runner to detect configuration drift. — citations: `['generated/workflows/network-operations/github-workflows-drift-detection-yml']`
* The `iac-tests` workflow runs Batfish network analysis, ContainerLab FRR tests, and Ansible idempotency checks across multiple runner types including `hyrule-public-pr` and `hyrule-infra`. — citations: `['generated/workflows/network-operations/github-workflows-iac-tests-yml']`
* The `netops-nightly` workflow runs full Batfish and ContainerLab test suites nightly on the `hyrule-infra` runner. — citations: `['generated/workflows/network-operations/github-workflows-netops-nightly-yml']`
* The hyrule-network-proxy CI workflow runs on `ubuntu-latest` (GitHub-hosted), unlike other AS215932 service CI workflows which use self-hosted runners. — citations: `['generated/workflows/hyrule-network-proxy/github-workflows-ci-yml']`
* The hyrule-cloud `deploy-validation` workflow uses the `HYRULE_INFRA_DEPLOY_KEY` secret and runs on the `hyrule` self-hosted runner label. — citations: `['generated/workflows/hyrule-cloud/github-workflows-deploy-yml']`
* The hyrule-web CI workflow includes both `test` and `frontend` jobs, both running on the `hyrule-public-pr` self-hosted runner. — citations: `['generated/workflows/hyrule-web/github-workflows-ci-yml']`
* The engineering-loop CI workflow includes ruff, mypy, pytest, and evals jobs, all running on the `hyrule-public-pr` self-hosted runner. — citations: `['generated/workflows/engineering-loop/github-workflows-ci-yml']`
* The `render-check` workflow in network-operations validates rendered configuration output on pull_request and push events. — citations: `['generated/workflows/network-operations/github-workflows-render-check-yml']`
* The `app-promotion-deploy` workflow in network-operations has a `detect` job on `hyrule-public-pr` and an `apply` job with unspecified runner, triggered on push. — citations: `['generated/workflows/network-operations/github-workflows-app-promotion-deploy-yml']`
