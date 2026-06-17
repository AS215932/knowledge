---
type: Workflow
title: ci
description: GitHub Actions workflow `ci` from AS215932/hyrule-network-proxy.
resource: https://github.com/AS215932/hyrule-network-proxy/blob/b82dc72bbf382167062bff272606ce84ec20538c/.github/workflows/ci.yml
tags:
- ci
- github-actions
- hyrule-network-proxy
- workflow
timestamp: '2026-06-13T21:03:25Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-network-proxy
  path: .github/workflows/ci.yml
  commit: b82dc72bbf382167062bff272606ce84ec20538c
  url: https://github.com/AS215932/hyrule-network-proxy/blob/b82dc72bbf382167062bff272606ce84ec20538c/.github/workflows/ci.yml
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-network-proxy
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
| Workflow permissions | `{}` |

# Jobs

| Job | Runs on | Environment | Permissions |
| --- | --- | --- | --- |
| `go` | `ubuntu-latest` | `` | `{}` |

# Secrets referenced by name

No `secrets.*` references detected.

# Operational notes

This workflow summary is statically parsed from GitHub Actions YAML. It intentionally records secret names only, never values.

# Citations

[1] [.github/workflows/ci.yml](https://github.com/AS215932/hyrule-network-proxy/blob/b82dc72bbf382167062bff272606ce84ec20538c/.github/workflows/ci.yml)
