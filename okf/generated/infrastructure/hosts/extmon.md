---
type: Infrastructure Host
title: extmon
description: Infrastructure Host `extmon` with address `0.0.0.0` and groups `external`.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml
tags:
- external
- host
- infrastructure
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
  path: ansible/inventory/host_vars/extmon.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/extmon.yml
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
host: extmon
address: 0.0.0.0
groups:
- external
---

# Host

| Field | Value |
| --- | --- |
| Host | `extmon` |
| Type | `Infrastructure Host` |
| Address | `0.0.0.0` |
| Groups | `external` |
| Role comment | `extmon — external monitoring host (Vultr / DigitalOcean / Hetzner Cloud).` |
| Monitoring role | `not set` |
| Logs role | `not set` |

# Deployed version pins

No app version pins found in host vars.

# Inbound firewall rules

No `firewall_extra_rules` found in host vars.

# Monitoring services

No host-local `monitoring_extra_services` found in host vars.

# Peer registry values

| Key | Value |
| --- | --- |
| `ipv4` | `0.0.0.0` |
| `ipv6` | `::` |

# Host variables summary

| Key | Value |
| --- | --- |
| `ansible_distribution` | `Debian` |
| `ansible_os_family` | `Debian` |
| `extmon_apply` | `False` |
| `extmon_discord_webhook_url` | `{{ lookup('ansible.builtin.env', 'EXTMON_DISCORD_WEBHOOK_URL') | default('') }}` |
| `extmon_ovh_application_key` | `{{ lookup('ansible.builtin.env', 'OVH_APPLICATION_KEY') | default('') }}` |
| `extmon_ovh_application_secret` | `{{ lookup('ansible.builtin.env', 'OVH_APPLICATION_SECRET') | default('') }}` |
| `extmon_ovh_consumer_key` | `{{ lookup('ansible.builtin.env', 'OVH_CONSUMER_KEY') | default('') }}` |
| `extmon_ovh_endpoint` | `{{ lookup('ansible.builtin.env', 'OVH_ENDPOINT') | default('ovh-eu') }}` |
| `extmon_ovh_failover_ips` | `["46.105.40.223", "51.91.236.215", "54.38.14.218"]` |
| `extmon_ovh_server_name` | `ns3526203.ip-193-70-32.eu` |
| `extmon_ssh_allow_v4` | `["{{ ops_prefix_v4 }}"]` |
| `extmon_ssh_allow_v6` | `["{{ ops_prefix_v6 }}", "{{ as215932_prefix }}"]` |

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/extmon.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/extmon.yml)
