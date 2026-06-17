---
type: Workflow
title: request-promotion
description: GitHub Actions workflow `request-promotion` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/.github/workflows/request-promotion.yml
tags:
- deploy
- github-actions
- noc-agent
- workflow
timestamp: '2026-06-17T07:49:45Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/noc-agent
  path: .github/workflows/request-promotion.yml
  commit: 98e5010648e34ac0ea6ad8e6a925fef76d0dbea9
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/.github/workflows/request-promotion.yml
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
source_path: .github/workflows/request-promotion.yml
triggers:
- workflow_dispatch
- workflow_run
---

# Workflow

| Field | Value |
| --- | --- |
| Name | `request-promotion` |
| Source | `.github/workflows/request-promotion.yml` |
| Triggers | `workflow_dispatch, workflow_run` |
| Deploy-like | `True` |
| Workflow permissions | `{"contents": "read"}` |

# Jobs

| Job | Runs on | Environment | Permissions |
| --- | --- | --- | --- |
| `request` | `self-hosted, linux, x64, hyrule-public-pr` | `` | `{}` |

# Secrets referenced by name

* `PROMOTION_APP_ID`
* `PROMOTION_APP_PRIVATE_KEY`

# Operational notes

This workflow summary is statically parsed from GitHub Actions YAML. It intentionally records secret names only, never values.

# Citations

[1] [.github/workflows/request-promotion.yml](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/.github/workflows/request-promotion.yml)
