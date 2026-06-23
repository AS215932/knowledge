---
type: Workflow
title: iac-tests
description: GitHub Actions workflow `iac-tests` from AS215932/network-operations.
resource: https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/.github/workflows/iac-tests.yml
tags:
- ci
- github-actions
- network-operations
- workflow
timestamp: '2026-06-23T09:21:09Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: .github/workflows/iac-tests.yml
  commit: fe46c3c3580ff79e8009ca839ab579f0691b55b8
  url: https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/.github/workflows/iac-tests.yml
last_verified_at: '2026-06-23T10:06:29Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: .github/workflows/iac-tests.yml
triggers:
- pull_request
- push
- workflow_dispatch
---

# Workflow

| Field | Value |
| --- | --- |
| Name | `iac-tests` |
| Source | `.github/workflows/iac-tests.yml` |
| Triggers | `pull_request, push, workflow_dispatch` |
| Deploy-like | `False` |
| Workflow permissions | `{"contents": "read", "pull-requests": "read"}` |

# Jobs

| Job | Runs on | Environment | Permissions |
| --- | --- | --- | --- |
| `changes` | `self-hosted, linux, x64, hyrule-public-pr` | `` | `{}` |
| `static-iac` | `self-hosted, linux, x64, hyrule-public-pr` | `` | `{}` |
| `ansible-idempotency` | `self-hosted, linux, x64, hyrule-public-pr` | `` | `{}` |
| `batfish` | `self-hosted, linux, x64, hyrule-infra` | `` | `{}` |
| `containerlab-frr` | `self-hosted, linux, x64, hyrule-infra` | `` | `{}` |
| `iac-gate` | `self-hosted, linux, x64, hyrule-public-pr` | `` | `{}` |

# Secrets referenced by name

No `secrets.*` references detected.

# Operational notes

This workflow summary is statically parsed from GitHub Actions YAML. It intentionally records secret names only, never values.

# Citations

[1] [.github/workflows/iac-tests.yml](https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/.github/workflows/iac-tests.yml)
