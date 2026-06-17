---
type: Source Document
title: PR-Agent (advisory AI review)
description: PR-Agent replaces the hosted Sourcery app with a self-controlled reviewer
  that uses **our own OpenRouter key**. It is advisory only — read + PR/issue-comment
  permissions, never deploys, never writes code, never auto-merges, and is **not*...
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/pr-agent.md
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: docs/ci/pr-agent.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-60
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/pr-agent.md#L1-L60
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: docs/ci/pr-agent.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `docs/ci/pr-agent.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `60` |

# Detected headings

* `# PR-Agent (advisory AI review)`
* `## The model-pin gotcha (important)`
* `## Fork / trust policy`
* `## Triage`

# Deterministic excerpt

```markdown
# PR-Agent (advisory AI review)

PR-Agent replaces the hosted Sourcery app with a self-controlled reviewer that
uses **our own OpenRouter key**. It is advisory only — read + PR/issue-comment
permissions, never deploys, never writes code, never auto-merges, and is **not**
a required check.

- Action: `The-PR-Agent/pr-agent@0bd56c0508504c718cc03d504cd4ceb6725ba3c7` (v0.35.0, Docker-based), SHA-pinned.
- Runner: `hyrule-public-pr` (unprivileged `ci-pr`) only.
- Model: primary `openrouter/deepseek/deepseek-v4-flash`, fallback `openrouter/minimax/minimax-m2.7`.
- Key: `OPENROUTER_API_KEY` org secret (visibility = the six repos), delivered per-job as `OPENROUTER__KEY`.
- Config: `.pr_agent.toml` per repo (model, fallback, `extra_instructions`).

## The model-pin gotcha (important)

PR-Agent reads `.pr_agent.toml` from the **default branch**, not the PR head
(its action has no checkout step; "Applying repo settings" loads from the
default branch). So until a new repo's `.pr_agent.toml` is merged to `main`,
PR-Agent silently falls back to its packaged default (`gpt-5.5…` → `gpt-5.4-mini`)
and the gpt-5.5 call errors "not a valid model ID".

Fix = pin via dynaconf env in `pr-agent.yml` `env:` (double-underscore, same path
that delivers `OPENROUTER__KEY`), which is honoured immediately:

```yaml
CONFIG__MODEL: openrouter/deepseek/deepseek-v4-flash
CONFIG__FALLBACK_MODELS: '["openrouter/minimax/minimax-m2.7"]'
CONFIG__CUSTOM_MODEL_MAX_TOKENS: "128000"
```

Both models are *custom* (litellm) models → `custom_model_max_tokens` is
required. Keep the env pin even after `.pr_agent.toml` lands (belt and braces).

## Fork / trust policy

```yaml
if: >
  (github.event_name == 'pull_request' &&
   github.event.pull_request.head.repo.full_name == github.repository) ||
  (github.event_name =
...
```

# Citations

[1] [docs/ci/pr-agent.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/pr-agent.md)
