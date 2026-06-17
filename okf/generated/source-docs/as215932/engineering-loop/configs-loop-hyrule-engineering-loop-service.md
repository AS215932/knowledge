---
type: Source Document
title: /etc/systemd/system/hyrule-engineering-loop.service
description: '[Unit] Description=AS215932 Engineering Loop operations lane (one budgeted
  cycle) After=network-online.target Wants=network-online.target # Belt and braces:
  do not even attempt a cycle on a CI runner. ConditionEnvironment=!GITHUB_ACTIONS'
resource: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/configs/loop/hyrule-engineering-loop.service
tags:
- as215932
- engineering-loop
- source-document
timestamp: '2026-06-16T07:29:23Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/engineering-loop
  path: configs/loop/hyrule-engineering-loop.service
  commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
  lines: 1-60
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/configs/loop/hyrule-engineering-loop.service#L1-L60
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/engineering-loop
source_path: configs/loop/hyrule-engineering-loop.service
commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/engineering-loop` |
| Path | `configs/loop/hyrule-engineering-loop.service` |
| Commit | `768cde6c996e42f3f91d395347ba9809e2e020e5` |
| Lines | `60` |

# Detected headings

* `# /etc/systemd/system/hyrule-engineering-loop.service`
* `# Deploy to: an operator machine or a dedicated `loop` VM — NEVER the`
* `# privileged `ci` runner. The backend executes generated code; the daemon`
* `# refuses to run when GITHUB_ACTIONS is set, but do not schedule it there`
* `# regardless. A dedicated `loop` VM goes through the standard`
* `# docs/network-flows.md + firewall + monitoring onboarding three-steps.`
* `#`
* `# Oneshot, timer-driven: one cycle picks one loop:approved issue, runs the`
* `# full graph, and ends with a draft PR or a journaled failure, then exits.`
* `# Belt and braces: do not even attempt a cycle on a CI runner.`
* `# .env provides: HYRULE_DISCORD_WEBHOOK, HYRULE_ICINGA_URL/USER/PASSWORD,`
* `# the loop's GH token for `gh`, and any model/provider keys. It must NOT`
* `# contain production Vault tokens or fleet SSH material — the backend env`
* `# is scrubbed, but keep the surface minimal.`
* `# A run never blocks the next timer fire indefinitely; the daemon enforces`
* `# its own per-run wall-clock budget, this is the hard backstop.`
* `# Security hardening`

# Citations

[1] [configs/loop/hyrule-engineering-loop.service](https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/configs/loop/hyrule-engineering-loop.service)
