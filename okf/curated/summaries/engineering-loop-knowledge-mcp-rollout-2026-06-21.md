---
type: Learning Summary
title: Engineering Loop and Knowledge MCP rollout evidence 2026-06-21
description: Source-cited rollout summary for Knowledge MCP deployment, Engineering Loop notification remediation, and canary verification.
tags:
- curated
- engineering-loop
- knowledge-mcp
- rollout
- summary
truth_owner: okf
authority: advisory
source_refs:
- repo: AS215932/knowledge
  path: src/hyrule_knowledge/mcp_server.py
  commit: ec09b7df21f9c08d155d5b4d63b3dba21d976e93
  url: https://github.com/AS215932/knowledge/blob/ec09b7df21f9c08d155d5b4d63b3dba21d976e93/src/hyrule_knowledge/mcp_server.py
- repo: AS215932/knowledge
  path: Dockerfile
  commit: ec09b7df21f9c08d155d5b4d63b3dba21d976e93
  url: https://github.com/AS215932/knowledge/blob/ec09b7df21f9c08d155d5b4d63b3dba21d976e93/Dockerfile
- repo: AS215932/engineering-loop
  path: src/hyrule_engineering_loop/knowledge_context.py
  commit: d4781edbef0cab9ca983f622b4aa2a960df16a97
  url: https://github.com/AS215932/engineering-loop/blob/d4781edbef0cab9ca983f622b4aa2a960df16a97/src/hyrule_engineering_loop/knowledge_context.py
- repo: AS215932/engineering-loop
  path: src/hyrule_engineering_loop/daemon.py
  commit: d4781edbef0cab9ca983f622b4aa2a960df16a97
  url: https://github.com/AS215932/engineering-loop/blob/d4781edbef0cab9ca983f622b4aa2a960df16a97/src/hyrule_engineering_loop/daemon.py
- repo: AS215932/engineering-loop
  path: src/hyrule_engineering_loop/gate_runner.py
  commit: d4781edbef0cab9ca983f622b4aa2a960df16a97
  url: https://github.com/AS215932/engineering-loop/blob/d4781edbef0cab9ca983f622b4aa2a960df16a97/src/hyrule_engineering_loop/gate_runner.py
- repo: AS215932/engineering-loop
  path: docs/engineering-loop/notification-smoke-path.md
  commit: 9396fab78e5dee97e86d005271bb374fa483ec68
  url: https://github.com/AS215932/engineering-loop/blob/9396fab78e5dee97e86d005271bb374fa483ec68/docs/engineering-loop/notification-smoke-path.md
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/loop.yml
  commit: 40c00a665e09bc1e7d739de8bde7eaf264e8e728
  url: https://github.com/AS215932/network-operations/blob/40c00a665e09bc1e7d739de8bde7eaf264e8e728/ansible/inventory/host_vars/loop.yml
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/mon.yml
  commit: 40c00a665e09bc1e7d739de8bde7eaf264e8e728
  url: https://github.com/AS215932/network-operations/blob/40c00a665e09bc1e7d739de8bde7eaf264e8e728/ansible/inventory/host_vars/mon.yml
- repo: AS215932/network-operations
  path: ansible/generated/loop/icinga_host.conf
  commit: 40c00a665e09bc1e7d739de8bde7eaf264e8e728
  url: https://github.com/AS215932/network-operations/blob/40c00a665e09bc1e7d739de8bde7eaf264e8e728/ansible/generated/loop/icinga_host.conf
- repo: AS215932/network-operations
  path: docs/runbooks/bootstrap-engineering-loop-vault.md
  commit: 40c00a665e09bc1e7d739de8bde7eaf264e8e728
  url: https://github.com/AS215932/network-operations/blob/40c00a665e09bc1e7d739de8bde7eaf264e8e728/docs/runbooks/bootstrap-engineering-loop-vault.md
- url: manual://loop/engineering-loop-knowledge-mcp-rollout/2026-06-21
last_verified_at: '2026-06-21T16:10:28Z'
confidence: medium
dispute_policy: adjudicate
review_status: proposed
authority_tier: A3
---

# Summary

On 2026-06-21 the `loop` VM rollout reached a working state for read-only Knowledge MCP context and Engineering Loop run-status notifications. This summary is a proposed OKF summary backed by source commits and by the observed evidence snapshot at [Engineering Loop / Knowledge MCP rollout live evidence](../../observed/latest/engineering-loop-knowledge-mcp-rollout-2026-06-21.md).

# Source-backed state

1. `AS215932/knowledge` PR #8 added the Dockerized read-only MCP server with HTTP transports and `/health`; the merged source commit is `ec09b7df21f9c08d155d5b4d63b3dba21d976e93`.
2. `AS215932/engineering-loop` consumes Knowledge MCP context over HTTP and includes the notification fixes and docs-only gate fix at deployed commit `d4781edbef0cab9ca983f622b4aa2a960df16a97`.
3. `AS215932/network-operations` PR #284 merged as `40c00a665e09bc1e7d739de8bde7eaf264e8e728` and records the production deployment pin, Icinga API path, Icinga CA install path, `mon` firewall allow, and the passive `loop!engineering-loop` service object.
4. The canary documentation PR `AS215932/engineering-loop#21` merged as `9396fab78e5dee97e86d005271bb374fa483ec68`, closing canary issue `#19`.

# Observed evidence

The sanitized live evidence snapshot recorded the following point-in-time results only:

* Knowledge MCP health on `loop` returned `status=ok`, `transport=streamable-http`, `read_only=true`, `tool_count=14`, `concept_count=865`, and `claim_count=4562`.
* `vault-agent-engineering-loop.service`, `hyrule-engineering-loop.timer`, `hyrule-knowledge-mcp.service`, and Docker were active.
* The passive Icinga object `loop!engineering-loop` existed and was OK with output `loop idle (approved queue is empty)` after a post-merge idle cycle.

# Caution

This summary must not be used to redefine intended state. Source repositories remain authoritative for deployment pins, firewall rules, service definitions, and runtime behavior. The linked observed evidence expires after 24 hours and is suitable only as A3 point-in-time evidence.
