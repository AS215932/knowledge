---
type: Workflow
title: Cancel superseded runs on the same ref. Per-branch grouping so a push to main
description: 'name: ci'
resource: https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/.github/workflows/ci.yml
tags:
- as215932
- hyrule-web
- workflow
timestamp: '2026-06-16T15:09:49Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-web
  path: .github/workflows/ci.yml
  commit: d94146e67f9eb05f8eeb5c57cab74cbe676f5c79
  lines: 1-106
  url: https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/.github/workflows/ci.yml#L1-L106
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-web
source_path: .github/workflows/ci.yml
commit: d94146e67f9eb05f8eeb5c57cab74cbe676f5c79
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-web` |
| Path | `.github/workflows/ci.yml` |
| Commit | `d94146e67f9eb05f8eeb5c57cab74cbe676f5c79` |
| Lines | `106` |

# Detected headings

* `# Cancel superseded runs on the same ref. Per-branch grouping so a push to main`
* `# doesn't kill an open PR's CI on a different branch.`
* `# Branch protection requires this exact check name. Don't rename without`
* `# updating the rule in repo settings.`
* `# actions/setup-python has no Debian 13 build for 3.12; the runner`
* `# ships system Python 3.13 which satisfies the project's`
* `# requires-python = ">=3.12" and matches the web VM in production.`
* `# Issue #14: TypeScript/Vite/Tailwind frontend bundle. Add this check name to`
* `# branch protection alongside `test`. Don't rename without updating the rule.`
* `# npm 11 — must match the npm that generated package-lock.json, else`
* `# `npm ci` rejects the lock (npm 10 mis-reads npm-11 nested deps). node`
* `# 24 LTS ships npm 11.`
* `# The built bundle is committed (the web host has no Node; the deploy`
* `# git-checks-out the repo). Fail if the committed dist drifts from a fresh`
* `# build so an SHA-pinned rollback always ships matching assets.`

# Citations

[1] [.github/workflows/ci.yml](https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/.github/workflows/ci.yml)
