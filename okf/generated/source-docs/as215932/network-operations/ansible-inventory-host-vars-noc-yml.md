---
type: Source Document
title: noc — autonomous NOC agent + hyrule-mcp tool server.
description: '--- # noc — autonomous NOC agent + hyrule-mcp tool server. # # noc-agent
  (FastAPI on :8000) receives webhooks from Alertmanager and Icinga2 # on mon, runs
  an LLM-driven investigation against hyrule-mcp tools, and # notifies a Discord cha...'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/noc.yml
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/noc.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-100
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/noc.yml#L1-L100
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: ansible/inventory/host_vars/noc.yml
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `ansible/inventory/host_vars/noc.yml` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `100` |

# Detected headings

* `# noc — autonomous NOC agent + hyrule-mcp tool server.`
* `#`
* `# noc-agent (FastAPI on :8000) receives webhooks from Alertmanager and Icinga2`
* `# on mon, runs an LLM-driven investigation against hyrule-mcp tools, and`
* `# notifies a Discord channel. hyrule-mcp is a stdio child of noc-agent.`
* `# XO MCP occasionally takes >5s to answer tools/list via supergateway during`
* `# streamable-HTTP session churn. Keep Icinga + app health probes below their`
* `# 15s HTTP wrapper timeout while avoiding false 5s flaps.`
* `# Webhooks from Alertmanager + Icinga2 on mon.`
* `# Operator dashboard via Caddy on proxy (noc.servify.network -> /control + /health).`
* `# Monitoring scrapes.`
* `# Monitoring — register on mon (new host, not in legacy infra-vms.conf).`
* `# Custom check: surfaces /health/mcp's per-source JSON state instead of`
* `# the generic check_http "503 + pattern not found" output.`
* `# CheckCommand defined in configs/mon/icinga2/services/noc-agent-mcp-health.conf.`
* `# Require ~2 minutes of consistent failure before a HARD CRITICAL so a`
* `# single 1/3 soft flap does not page. Flapping detection surfaces the`
* `# pattern when it repeatedly fails on one attempt and recovers.`
* `# Custom check: surfaces /health/mail's JSON body (IMAP reason / error) in`
* `# the alert instead of just the HTTP code.`
* `# CheckCommand defined in configs/mon/icinga2/services/noc-agent-mail-health.conf.`
* `# Custom check: surfaces /health/model's JSON body in the alert.`
* `# CheckCommand defined in configs/mon/icinga2/services/noc-agent-model-health.conf.`
* `# --- Logs --- (ships journald to log VM via Vector)`

# Citations

[1] [ansible/inventory/host_vars/noc.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/noc.yml)
