---
type: Workflow
title: ci
description: GitHub Actions workflow `ci` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/.github/workflows/ci.yml
tags:
- deploy
- github-actions
- hyrule-cloud
- workflow
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: .github/workflows/ci.yml
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/.github/workflows/ci.yml
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
source_path: .github/workflows/ci.yml
triggers:
- pull_request
- push
---

# Workflow

| Field | Value |
| --- | --- |
| Name | `ci` |
| Source | `.github/workflows/ci.yml` |
| Triggers | `pull_request, push` |
| Deploy-like | `True` |
| Workflow permissions | `{"contents": "read"}` |

# Jobs

| Job | Runs on | Environment | Permissions |
| --- | --- | --- | --- |
| `test` | `self-hosted, linux, x64, hyrule-public-pr` | `` | `{}` |

# Secrets referenced by name

No `secrets.*` references detected.

# Operational notes

This workflow summary is statically parsed from GitHub Actions YAML. It intentionally records secret names only, never values.

# Citations

[1] [.github/workflows/ci.yml](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/.github/workflows/ci.yml)
