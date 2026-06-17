---
type: Workflow
title: app-promotion-deploy
description: GitHub Actions workflow `app-promotion-deploy` from AS215932/network-operations.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/app-promotion-deploy.yml
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
  path: .github/workflows/app-promotion-deploy.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/app-promotion-deploy.yml
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: .github/workflows/app-promotion-deploy.yml
triggers:
- push
---

# Workflow

| Field | Value |
| --- | --- |
| Name | `app-promotion-deploy` |
| Source | `.github/workflows/app-promotion-deploy.yml` |
| Triggers | `push` |
| Deploy-like | `True` |
| Workflow permissions | `{"contents": "read", "pull-requests": "write"}` |

# Jobs

| Job | Runs on | Environment | Permissions |
| --- | --- | --- | --- |
| `detect` | `self-hosted, linux, x64, hyrule-public-pr` | `` | `{}` |
| `apply` | `unspecified` | `` | `{}` |

# Secrets referenced by name

No `secrets.*` references detected.

# Operational notes

This workflow summary is statically parsed from GitHub Actions YAML. It intentionally records secret names only, never values.

# Citations

[1] [.github/workflows/app-promotion-deploy.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/app-promotion-deploy.yml)
