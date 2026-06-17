---
type: Workflow
title: request-promotion
description: GitHub Actions workflow `request-promotion` from AS215932/hyrule-web.
resource: https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/.github/workflows/request-promotion.yml
tags:
- deploy
- github-actions
- hyrule-web
- workflow
timestamp: '2026-06-16T15:09:49Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-web
  path: .github/workflows/request-promotion.yml
  commit: d94146e67f9eb05f8eeb5c57cab74cbe676f5c79
  url: https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/.github/workflows/request-promotion.yml
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-web
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

[1] [.github/workflows/request-promotion.yml](https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/.github/workflows/request-promotion.yml)
