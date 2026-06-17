---
type: Monitoring Inventory
title: Network Operations Monitoring Inventory
description: Tracked Prometheus/Icinga/blackbox monitoring configuration files from
  network-operations.
tags:
- icinga
- monitoring
- network-operations
- prometheus
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: configs/mon/10-enX0.network
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/mon/10-enX0.network
- repo: AS215932/network-operations
  path: configs/mon/10-enX1.network
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/mon/10-enX1.network
- repo: AS215932/network-operations
  path: configs/mon/alertmanager.yml.j2
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/mon/alertmanager.yml.j2
- repo: AS215932/network-operations
  path: configs/mon/blackbox.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/mon/blackbox.yml
- repo: AS215932/network-operations
  path: configs/mon/icinga2/hosts/dom0.conf
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/mon/icinga2/hosts/dom0.conf
- repo: AS215932/network-operations
  path: configs/mon/icinga2/hosts/infra-vms.conf
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/mon/icinga2/hosts/infra-vms.conf
- repo: AS215932/network-operations
  path: configs/mon/icinga2/hosts/routers.conf
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/mon/icinga2/hosts/routers.conf
- repo: AS215932/network-operations
  path: configs/mon/icinga2/scripts/check_dns_soa_ecmp.py
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/mon/icinga2/scripts/check_dns_soa_ecmp.py
- repo: AS215932/network-operations
  path: configs/mon/icinga2/scripts/check_jool_success_delta.sh
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/mon/icinga2/scripts/check_jool_success_delta.sh
- repo: AS215932/network-operations
  path: configs/mon/icinga2/scripts/check_noc_agent_mail_health.sh
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/mon/icinga2/scripts/check_noc_agent_mail_health.sh
- repo: AS215932/network-operations
  path: configs/mon/icinga2/scripts/check_noc_agent_mcp_health.sh
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/mon/icinga2/scripts/check_noc_agent_mcp_health.sh
- repo: AS215932/network-operations
  path: configs/mon/icinga2/scripts/check_noc_agent_model_health.sh
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/mon/icinga2/scripts/check_noc_agent_model_health.sh
last_verified_at: '2026-06-17T10:33:31Z'
confidence: medium
dispute_policy: repo_wins
---

# Monitoring configuration

This concept summarizes tracked monitoring source files under `configs/mon/`.

# Files

* `configs/mon/10-enX0.network`
* `configs/mon/10-enX1.network`
* `configs/mon/alertmanager.yml.j2`
* `configs/mon/blackbox.yml`
* `configs/mon/icinga2/hosts/dom0.conf`
* `configs/mon/icinga2/hosts/infra-vms.conf`
* `configs/mon/icinga2/hosts/routers.conf`
* `configs/mon/icinga2/scripts/check_dns_soa_ecmp.py`
* `configs/mon/icinga2/scripts/check_jool_success_delta.sh`
* `configs/mon/icinga2/scripts/check_noc_agent_mail_health.sh`
* `configs/mon/icinga2/scripts/check_noc_agent_mcp_health.sh`
* `configs/mon/icinga2/scripts/check_noc_agent_model_health.sh`
* `configs/mon/icinga2/scripts/icinga-snapshot`
* `configs/mon/icinga2/scripts/notify-discord.sh`
* `configs/mon/icinga2/scripts/notify-noc-agent.sh`
* `configs/mon/icinga2/services/bgp.conf`
* `configs/mon/icinga2/services/cr-bogon-egress.conf`
* `configs/mon/icinga2/services/disk.conf`
* `configs/mon/icinga2/services/dns-soa-ecmp.conf`
* `configs/mon/icinga2/services/dns.conf`
* `configs/mon/icinga2/services/github-runner.conf`
* `configs/mon/icinga2/services/host-ping6.conf`
* `configs/mon/icinga2/services/http.conf`
* `configs/mon/icinga2/services/nat64.conf`
* `configs/mon/icinga2/services/noc-agent-mail-health.conf`
* `configs/mon/icinga2/services/noc-agent-mcp-health.conf`
* `configs/mon/icinga2/services/noc-agent-model-health.conf`
* `configs/mon/icinga2/services/noc-agent-uptime.conf`
* `configs/mon/icinga2/services/node-up.conf`
* `configs/mon/icinga2/services/postgres.conf`
* `configs/mon/icinga2/services/rtr-checks.conf`
* `configs/mon/icinga2/services/ssh.conf`
* `configs/mon/icinga2/services/ssl.conf`
* `configs/mon/icinga2/services/underlay.conf`
* `configs/mon/icinga2/services/wireguard.conf`
* `configs/mon/icinga2/zones.conf`
* `configs/mon/plugins/check_prom_query`
* `configs/mon/prometheus-rules/logs-pipeline.yml`
* `configs/mon/prometheus-rules/noc-tripwire.yml`
* `configs/mon/prometheus.yml`

# Check/service names

* `bgp`
* `cr-bogon-egress`
* `disk`
* `dns`
* `dns-soa-ecmp`
* `github-runner`
* `host-ping6`
* `http`
* `nat64`
* `noc-agent-mail-health`
* `noc-agent-mcp-health`
* `noc-agent-model-health`
* `noc-agent-uptime`
* `node-up`
* `postgres`
* `prometheus`
* `rtr-checks`
* `ssh`
* `ssl`
* `underlay`
* `wireguard`

# Citations

[1] [configs/mon/10-enX0.network](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/mon/10-enX0.network)
[2] [configs/mon/10-enX1.network](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/mon/10-enX1.network)
[3] [configs/mon/alertmanager.yml.j2](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/mon/alertmanager.yml.j2)
[4] [configs/mon/blackbox.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/mon/blackbox.yml)
[5] [configs/mon/icinga2/hosts/dom0.conf](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/mon/icinga2/hosts/dom0.conf)
[6] [configs/mon/icinga2/hosts/infra-vms.conf](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/mon/icinga2/hosts/infra-vms.conf)
[7] [configs/mon/icinga2/hosts/routers.conf](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/mon/icinga2/hosts/routers.conf)
[8] [configs/mon/icinga2/scripts/check_dns_soa_ecmp.py](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/mon/icinga2/scripts/check_dns_soa_ecmp.py)
[9] [configs/mon/icinga2/scripts/check_jool_success_delta.sh](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/mon/icinga2/scripts/check_jool_success_delta.sh)
[10] [configs/mon/icinga2/scripts/check_noc_agent_mail_health.sh](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/mon/icinga2/scripts/check_noc_agent_mail_health.sh)
[11] [configs/mon/icinga2/scripts/check_noc_agent_mcp_health.sh](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/mon/icinga2/scripts/check_noc_agent_mcp_health.sh)
[12] [configs/mon/icinga2/scripts/check_noc_agent_model_health.sh](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/mon/icinga2/scripts/check_noc_agent_model_health.sh)
