---
type: Source Document
title: irc — Soju IRC bouncer.
description: '--- # irc — Soju IRC bouncer. # TLS termination is handled by Caddy
  on proxy; soju listens plaintext on :6697 # and is reachable only from proxy (and
  the ops-prefix/vpn-clients SSH set).'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/irc.yml
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/irc.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-36
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/irc.yml#L1-L36
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: ansible/inventory/host_vars/irc.yml
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `ansible/inventory/host_vars/irc.yml` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `36` |

# Detected headings

* `# irc — Soju IRC bouncer.`
* `# TLS termination is handled by Caddy on proxy; soju listens plaintext on :6697`
* `# and is reachable only from proxy (and the ops-prefix/vpn-clients SSH set).`
* `# Soju bouncer — TLS terminated by Soju itself.`
* `# ACME HTTP-01 challenge — certbot --standalone briefly binds tcp/80 during issuance/renewal.`
* `# We're using HTTP-01 instead of DNS-01 because Openprovider secondaries don't refresh`
* `# in time for the ACME check (project_openprovider_notify memory).`
* `# Monitoring.`
* `# --- Monitoring ---`
* `# --- Logs --- (ships journald to log VM via Vector)`

# Citations

[1] [ansible/inventory/host_vars/irc.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/irc.yml)
