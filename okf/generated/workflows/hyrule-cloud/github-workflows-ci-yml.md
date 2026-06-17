---
type: Workflow
title: Cancel superseded runs on the same ref. Per-branch grouping so a push to main
description: 'name: ci'
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/.github/workflows/ci.yml
tags:
- as215932
- hyrule-cloud
- workflow
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: .github/workflows/ci.yml
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1-80
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/.github/workflows/ci.yml#L1-L80
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
source_path: .github/workflows/ci.yml
commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-cloud` |
| Path | `.github/workflows/ci.yml` |
| Commit | `81e4316f3d1f4e7f770bc2589bd84a2c7972aad5` |
| Lines | `80` |

# Detected headings

* `# Cancel superseded runs on the same ref. Per-branch grouping so a push to main`
* `# doesn't kill an open PR's CI on a different branch.`
* `# Branch protection requires this exact check name. Don't rename without`
* `# updating the rule in repo settings.`
* `# ruff-on-touched-files needs the base ref for `git diff`. Fetch`
* `# depth 0 is cheaper than fetching just the base — self-hosted`
* `# runner caches the .git anyway.`
* `# actions/setup-python has no Debian 13 build for 3.12; the runner`
* `# ships system Python 3.13 which satisfies requires-python = ">=3.12"`
* `# and matches the api VM in production.`
* `# `--extra dev` pulls in pytest/pytest-asyncio/ruff/mypy from`
* `# `[project.optional-dependencies].dev` in pyproject.toml.`
* `# hyrule-web uses `--group dev` because it declares deps under`
* `# `[dependency-groups]`; the flag differs by where the group lives.`
* `# verify_facilitator.py is the CI gate per feedback_verified_payment_chains.md.`
* `# Triggers only when PaymentConfig itself changes (not unrelated feature`
* `# flags or other config edits) to avoid burning facilitator-side quota`
* `# on every PR. Failure here blocks merge.`

# Citations

[1] [.github/workflows/ci.yml](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/.github/workflows/ci.yml)
