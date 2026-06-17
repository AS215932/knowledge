---
type: Workflow
title: ci
description: GitHub Actions workflow `ci` from AS215932/engineering-loop.
resource: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/.github/workflows/ci.yml
tags:
- ci
- engineering-loop
- github-actions
- workflow
timestamp: '2026-06-16T07:29:23Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/engineering-loop
  path: .github/workflows/ci.yml
  commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/.github/workflows/ci.yml
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/engineering-loop
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
| Deploy-like | `False` |
| Workflow permissions | `{"contents": "read"}` |

# Jobs

| Job | Runs on | Environment | Permissions |
| --- | --- | --- | --- |
| `ruff` | `self-hosted, linux, x64, hyrule-public-pr` | `` | `{}` |
| `mypy` | `self-hosted, linux, x64, hyrule-public-pr` | `` | `{}` |
| `pytest` | `self-hosted, linux, x64, hyrule-public-pr` | `` | `{}` |
| `evals` | `self-hosted, linux, x64, hyrule-public-pr` | `` | `{}` |

# Secrets referenced by name

No `secrets.*` references detected.

# Operational notes

This workflow summary is statically parsed from GitHub Actions YAML. It intentionally records secret names only, never values.

# Citations

[1] [.github/workflows/ci.yml](https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/.github/workflows/ci.yml)
