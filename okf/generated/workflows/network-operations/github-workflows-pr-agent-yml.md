---
type: Workflow
title: Advisory AI PR review (replaces hosted Sourcery). Runs on the UNPRIVILEGED
description: '--- name: pr-agent'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/pr-agent.yml
tags:
- as215932
- network-operations
- workflow
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: .github/workflows/pr-agent.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-60
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/pr-agent.yml#L1-L60
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: .github/workflows/pr-agent.yml
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `.github/workflows/pr-agent.yml` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `60` |

# Detected headings

* `# Advisory AI PR review (replaces hosted Sourcery). Runs on the UNPRIVILEGED`
* `# `hyrule-public-pr` runner only, with read + PR/issue-comment permissions and`
* `# our own OpenRouter key. Never deploys, never writes code, never auto-merges.`
* `# Config (model/fallback/instructions): .pr_agent.toml. Design: docs/ci/pr-agent.md.`
* `# Public-fork policy: auto-review ONLY for same-repo (internal) PRs, and`
* `# slash commands ONLY from trusted authors. This keeps OPENROUTER_API_KEY`
* `# off untrusted fork PRs and stops anyone from burning the OpenRouter`
* `# budget via /ask, /improve, etc.`
* `# PR-Agent reads the OpenRouter key from openrouter__key; litellm also`
* `# honours OPENROUTER_API_KEY. Set both from the org secret.`
* `# Force our models via dynaconf env (SECTION__KEY, double underscore —`
* `# the same mechanism OPENROUTER__KEY uses, and proven to reach the`
* `# action's container). .pr_agent.toml alone is NOT honoured here: it`
* `# only lives on this pilot branch (not the default branch) and there is`
* `# no checkout step, so PR-Agent's "repo settings" load misses it and`
* `# falls back to its packaged default (gpt-5.5 → gpt-5.4-mini). These`
* `# env vars override that regardless. Once .pr_agent.toml lands on main`
* `# (Wave 3) it becomes the durable source; these stay as a belt-and-`
* `# suspenders pin. deepseek-v4-flash/minimax-m2.7 are custom (non-listed)`
* `# models, so custom_model_max_tokens is required.`

# Citations

[1] [.github/workflows/pr-agent.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/pr-agent.yml)
