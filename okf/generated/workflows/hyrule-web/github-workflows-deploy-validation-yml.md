---
type: Workflow
title: deploy-validation
description: GitHub Actions workflow `deploy-validation` from AS215932/hyrule-web.
resource: https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/.github/workflows/deploy-validation.yml
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
  path: .github/workflows/deploy-validation.yml
  commit: d94146e67f9eb05f8eeb5c57cab74cbe676f5c79
  url: https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/.github/workflows/deploy-validation.yml
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-web
source_path: .github/workflows/deploy-validation.yml
triggers:
- workflow_dispatch
---

# Workflow

| Field | Value |
| --- | --- |
| Name | `deploy-validation` |
| Source | `.github/workflows/deploy-validation.yml` |
| Triggers | `workflow_dispatch` |
| Deploy-like | `True` |
| Workflow permissions | `{"contents": "read"}` |

# Jobs

| Job | Runs on | Environment | Permissions |
| --- | --- | --- | --- |
| `validate` | `self-hosted, linux, x64, hyrule` | `` | `{}` |

# Secrets referenced by name

* `HYRULE_INFRA_DEPLOY_KEY`

# Operational notes

This workflow summary is statically parsed from GitHub Actions YAML. It intentionally records secret names only, never values.

# Citations

[1] [.github/workflows/deploy-validation.yml](https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/.github/workflows/deploy-validation.yml)
