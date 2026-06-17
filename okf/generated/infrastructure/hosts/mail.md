---
type: Infrastructure Host
title: mail
description: Infrastructure Host `mail` with address `2a0c:b641:b50:2::90` and groups
  `infra_vms, openbsd, public_facing`.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml
tags:
- host
- infra_vms
- infrastructure
- openbsd
- public_facing
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
  path: ansible/inventory/host_vars/mail.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/mail.yml
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
host: mail
address: 2a0c:b641:b50:2::90
groups:
- infra_vms
- openbsd
- public_facing
---

# Host

| Field | Value |
| --- | --- |
| Host | `mail` |
| Type | `Infrastructure Host` |
| Address | `2a0c:b641:b50:2::90` |
| Groups | `infra_vms, openbsd, public_facing` |
| Role comment | `mail — OpenBSD mail server for as215932.net.` |
| Monitoring role | `mail` |
| Logs role | `not set` |

# Deployed version pins

No app version pins found in host vars.

# Inbound firewall rules

* `tcp` port `25` from `any` — SMTP inbound (OpenSMTPD)
* `tcp` port `465` from `any` — SMTPS submission (OpenSMTPD)
* `tcp` port `587` from `any` — Submission STARTTLS (OpenSMTPD)
* `tcp` port `80` from `any` — ACME HTTP-01 (httpd)
* `tcp` port `993` from `['{{ ops_prefix_v6 }}', '{{ vpn_clients_subnet }}', '{{ peers.mon.ipv6 }}', '{{ peers.noc.ipv6 }}']` — IMAPS from ops/VPN/mon/noc
* `tcp` port `4190` from `['{{ ops_prefix_v6 }}', '{{ vpn_clients_subnet }}']` — ManageSieve from ops/VPN
* `tcp` port `9100` from `{{ peers.mon.ipv6 }}` — node_exporter scrape

# Monitoring services

* `smtp-tcp` (tcp) — OpenSMTPD public SMTP listener on tcp/25
* `smtps-cert-validity` (ssl) — TLS certificate days-until-expiry on tcp/465
* `submission-tcp` (tcp) — OpenSMTPD submission listener on tcp/587
* `imaps-cert-validity` (ssl) — Dovecot IMAPS certificate days-until-expiry on tcp/993

# Peer registry values

| Key | Value |
| --- | --- |
| `ipv6` | `2a0c:b641:b50:2::90` |

# Host variables summary

| Key | Value |
| --- | --- |
| `firewall_log_only` | `False` |
| `mail_dkim_extra_domains` | `["hyrule.host"]` |
| `mail_domain` | `as215932.net` |
| `mail_dovecot_listen` | `*, ::` |
| `mail_extra_domains` | `["hyrule.host"]` |
| `mail_hostname` | `mail.as215932.net` |
| `mail_ipv4` | `{{ mail_failover_ipv4 | default('') }}` |
| `mail_ipv4_gw` | `{{ mail_failover_ipv4_gateway | default('') }}` |
| `mail_ipv6` | `{{ peers.mail.ipv6 }}` |
| `mail_role_addresses` | `["noc", "abuse", "peering", "dh", "support"]` |
| `mail_shared_user` | `noc` |
| `monitoring_display_name` | `mail (OpenBSD mail server)` |
| `monitoring_node_listen` | `[{{ peers.mail.ipv6 }}]:9100` |
| `monitoring_register` | `True` |
| `monitoring_role` | `mail` |
| `pf_ext_if` | `xnf0` |
| `pf_ext_ifs` | `["xnf0", "xnf1"]` |
| `ssh_allow_sources_v6` | `["{{ ops_prefix_v6 }}", "{{ vpn_clients_subnet }}", "{{ peers.ci.ipv6 }}", "{{ peers.mon.ipv6 }}"]` |

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/mail.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/mail.yml)
