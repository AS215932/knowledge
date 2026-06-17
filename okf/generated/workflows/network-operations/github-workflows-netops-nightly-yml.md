---
type: Workflow
title: netops-nightly
description: GitHub Actions workflow `netops-nightly` from AS215932/network-operations.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/netops-nightly.yml
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
  path: .github/workflows/netops-nightly.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/netops-nightly.yml
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: .github/workflows/netops-nightly.yml
triggers:
- schedule
- workflow_dispatch
---

# Workflow

| Field | Value |
| --- | --- |
| Name | `netops-nightly` |
| Source | `.github/workflows/netops-nightly.yml` |
| Triggers | `schedule, workflow_dispatch` |
| Deploy-like | `True` |
| Workflow permissions | `{"contents": "read"}` |

# Jobs

| Job | Runs on | Environment | Permissions |
| --- | --- | --- | --- |
| `batfish-full` | `self-hosted, linux, x64, hyrule-infra` | `` | `{}` |
| `containerlab-full` | `self-hosted, linux, x64, hyrule-infra` | `` | `{}` |
| `notify-failure` | `self-hosted, linux, x64, hyrule-infra` | `` | `{}` |

# Secrets referenced by name

* `env`

# Operational notes

This workflow summary is statically parsed from GitHub Actions YAML. It intentionally records secret names only, never values.

# Citations

[1] [.github/workflows/netops-nightly.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/netops-nightly.yml)
