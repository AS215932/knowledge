---
type: Infrastructure Host
title: ci-pr
description: Infrastructure Host `ci-pr` with address `2a0c:b641:b51::c1` and groups
  `linux`.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml
tags:
- host
- infrastructure
- linux
- vm
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: ansible/inventory/hosts.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/ci-pr.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/ci-pr.yml
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
host: ci-pr
address: 2a0c:b641:b51::c1
groups:
- linux
---

# Host

| Field | Value |
| --- | --- |
| Host | `ci-pr` |
| Type | `Infrastructure Host` |
| Address | `2a0c:b641:b51::c1` |
| Groups | `linux` |
| Role comment | `ci-pr — UNPRIVILEGED self-hosted GitHub Actions runner for untrusted PR code` |
| Monitoring role | `ci` |
| Logs role | `not set` |

# Deployed version pins

No app version pins found in host vars.

# Inbound firewall rules

* `tcp` port `9100` from `{{ peers.mon.ipv6 }}` — node_exporter scrape (mon, pull-only)

# Monitoring services

No host-local `monitoring_extra_services` found in host vars.

# Peer registry values

| Key | Value |
| --- | --- |
| `ipv6` | `2a0c:b641:b51::c1` |

# Host variables summary

| Key | Value |
| --- | --- |
| `firewall_forward_extra_raw_nft` | `iifname docker0 ip6 saddr {{ github_runner_docker_fixed_cidr_v6 }} counter accept comment "ci-pr Docker IPv6 egress"
` |
| `github_runner_caddy_rfc2136_enabled` | `False` |
| `github_runner_containerlab_enabled` | `False` |
| `github_runner_docker_dns` | `["2a0c:b641:b50:2::1"]` |
| `github_runner_docker_fixed_cidr_v6` | `2a0c:b641:b51:c1::/64` |
| `github_runner_docker_ipv6_enabled` | `True` |
| `github_runner_group_name` | `public-pr` |
| `github_runner_labels` | `["self-hosted", "linux", "{{ github_runner_arch }}", "hyrule-public-pr"]` |
| `github_runner_ssh_key_path` | `` |
| `github_runner_storage_enabled` | `False` |
| `github_runner_vault_enabled` | `False` |
| `logs_register` | `False` |
| `monitoring_check_vars` | `{"github_runner": true}` |
| `monitoring_register` | `True` |
| `monitoring_role` | `ci` |

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/ci-pr.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/ci-pr.yml)
