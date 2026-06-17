---
type: Workflow
title: apply
description: GitHub Actions workflow `apply` from AS215932/network-operations.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/apply.yml
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
  path: .github/workflows/apply.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/apply.yml
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: .github/workflows/apply.yml
triggers:
- workflow_dispatch
- workflow_call
---

# Workflow

| Field | Value |
| --- | --- |
| Name | `apply` |
| Source | `.github/workflows/apply.yml` |
| Triggers | `workflow_dispatch, workflow_call` |
| Deploy-like | `True` |
| Workflow permissions | `{"contents": "read", "pull-requests": "write"}` |

# Jobs

| Job | Runs on | Environment | Permissions |
| --- | --- | --- | --- |
| `apply` | `self-hosted, linux, x64, hyrule-infra` | `${{ inputs.dry_run && 'dry-run' || 'production' }}` | `{}` |

# Secrets referenced by name

* `GITHUB_TOKEN`
* `env`

# Operational notes

This workflow summary is statically parsed from GitHub Actions YAML. It intentionally records secret names only, never values.

# Citations

[1] [.github/workflows/apply.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/apply.yml)
