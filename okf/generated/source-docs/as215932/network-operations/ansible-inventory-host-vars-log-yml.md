---
type: Source Document
title: log — centralized log aggregation host.
description: '--- # log — centralized log aggregation host. # # Vector aggregator
  on :6000 (vector-native ingest from agents) and :6514 # (TCP syslog from OpenBSD
  mail). Loki on :3100 (HTTP query, only reachable # from mon''s Grafana). Disk: 50
  GB on /...'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/log.yml
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/log.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-74
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/log.yml#L1-L74
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: ansible/inventory/host_vars/log.yml
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `ansible/inventory/host_vars/log.yml` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `74` |

# Detected headings

* `# log — centralized log aggregation host.`
* `#`
* `# Vector aggregator on :6000 (vector-native ingest from agents) and :6514`
* `# (TCP syslog from OpenBSD mail). Loki on :3100 (HTTP query, only reachable`
* `# from mon's Grafana). Disk: 50 GB on /var/lib/loki.`
* `# Mgmt v4 NIC mirrors xoa so dom0 can ship logs without overlay routing.`
* `#`
* `# See docs/network-flows.md → "### log" for the canonical inbound matrix and`
* `# docs/application-logging.md for the contract that fills these streams.`
* `# Vector→Vector ingest from agents.`
* `# Off-net ns2 over public IPv6 (different ASN, transits via rtr).`
* `# XCP-NG dom0 over mgmt v4 (no AS215932 address). Mgmt subnet matches xoa pattern.`
* `# OpenBSD mail's native syslogd `@@host` forward — TCP only, no UDP.`
* `# FreeBSD core routers' native syslogd `@@host` forward (issue #17).`
* `# Grafana on mon queries Loki; also scrapes Vector's internal metrics.`
* `# Standard monitoring scrape.`
* `# Monitoring — register on mon (new host).`
* `# Logging role knobs.`
* `# Aggregator host doesn't ship to itself externally — sources land in the`
* `# in-process Vector pipeline. Buffer cap on the loki sink instead, sized`
* `# generously since /var/lib/loki has 50 GB.`

# Citations

[1] [ansible/inventory/host_vars/log.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/log.yml)
