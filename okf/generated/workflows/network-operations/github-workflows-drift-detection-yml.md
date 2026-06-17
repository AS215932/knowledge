---
type: Workflow
title: drift-detection
description: GitHub Actions workflow `drift-detection` from AS215932/network-operations.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/drift-detection.yml
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
  path: .github/workflows/drift-detection.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/drift-detection.yml
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: .github/workflows/drift-detection.yml
triggers:
- schedule
- workflow_dispatch
---

# Workflow

| Field | Value |
| --- | --- |
| Name | `drift-detection` |
| Source | `.github/workflows/drift-detection.yml` |
| Triggers | `schedule, workflow_dispatch` |
| Deploy-like | `True` |
| Workflow permissions | `{"contents": "read"}` |

# Jobs

| Job | Runs on | Environment | Permissions |
| --- | --- | --- | --- |
| `check-drift` | `self-hosted, linux, x64, hyrule-infra` | `` | `{}` |

# Secrets referenced by name

* `env`

# Operational notes

This workflow summary is statically parsed from GitHub Actions YAML. It intentionally records secret names only, never values.

# Citations

[1] [.github/workflows/drift-detection.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/drift-detection.yml)
