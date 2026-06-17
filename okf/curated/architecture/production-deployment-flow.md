---
type: Architecture
title: Production Deployment Flow
description: How app repositories promote reviewed commits into production through
  network-operations.
tags:
- architecture
- curated
- proposed
truth_owner: okf
authority: advisory
source_refs:
- repo: AS215932/network-operations
  path: README.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/README.md
- repo: AS215932/network-operations
  path: docs/ci/deploy-runbook.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/deploy-runbook.md
- repo: AS215932/network-operations
  path: AGENTS.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/AGENTS.md
last_verified_at: '2026-06-17T10:33:31Z'
confidence: medium
dispute_policy: adjudicate
review_status: proposed
---

# Production deployment flow

App repositories do not directly define production state. They produce reviewed commits and request promotion. `network-operations` pins exact app SHAs in Ansible inventory, renders intended state, and runs production applies behind human approval.

# Normal path

1. App CI succeeds on the app repository's `main` branch.
2. The app requests promotion or an operator runs `promote-apps`.
3. A promotion PR updates exact 40-character SHAs in `network-operations` host vars.
4. Reviewers merge the promotion PR after render/CI checks.
5. `app-promotion-deploy` calls `apply.yml` for affected playbooks.
6. A human approves the GitHub `production` environment gate.
7. Operators review Icinga pre/post snapshot diffs.

# Safety lessons

The deployment record lives in one repo; app repos remain implementation sources. This avoids accidental production deploys on application merge.

# Citations

[1] [AS215932/network-operations:README.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/README.md)
[2] [AS215932/network-operations:docs/ci/deploy-runbook.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/deploy-runbook.md)
[3] [AS215932/network-operations:AGENTS.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/AGENTS.md)
