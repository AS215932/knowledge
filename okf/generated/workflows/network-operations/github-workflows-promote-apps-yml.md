---
type: Workflow
title: promote-apps
description: GitHub Actions workflow `promote-apps` from AS215932/network-operations.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/promote-apps.yml
tags:
- deploy
- github-actions
- network-operations
- workflow
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: .github/workflows/promote-apps.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/promote-apps.yml
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: .github/workflows/promote-apps.yml
triggers:
- repository_dispatch
- workflow_dispatch
---

# Workflow

| Field | Value |
| --- | --- |
| Name | `promote-apps` |
| Source | `.github/workflows/promote-apps.yml` |
| Triggers | `repository_dispatch, workflow_dispatch` |
| Deploy-like | `True` |
| Workflow permissions | `{"contents": "write", "pull-requests": "write"}` |

# Jobs

| Job | Runs on | Environment | Permissions |
| --- | --- | --- | --- |
| `promote` | `self-hosted, linux, x64, hyrule-public-pr` | `` | `{}` |

# Secrets referenced by name

* `PROMOTION_APP_ID`
* `PROMOTION_APP_PRIVATE_KEY`

# Operational notes

This workflow summary is statically parsed from GitHub Actions YAML. It intentionally records secret names only, never values.

# Citations

[1] [.github/workflows/promote-apps.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/promote-apps.yml)
