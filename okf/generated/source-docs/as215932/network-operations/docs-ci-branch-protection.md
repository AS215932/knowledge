---
type: Source Document
title: Branch protection — required checks per repo
description: Current `main` protection across the org (set in Wave 6). PR-Agent is
  **never** required (advisory, same-repo-only — requiring it would wedge fork/dependabot
  PRs). Semgrep is required as a *presence* gate while reporting-only; flip it to...
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/branch-protection.md
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: docs/ci/branch-protection.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-79
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/branch-protection.md#L1-L79
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: docs/ci/branch-protection.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `docs/ci/branch-protection.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `79` |

# Detected headings

* `# Branch protection — required checks per repo`
* `## Why these settings`
* `## The `iac-gate` deadlock guard (acceptance #7)`
* `## Reproducing the protection`
* `# Four repos protected on existing green contexts (no required reviews):`
* `# Add a context to an already-protected repo without disturbing the rest:`
* `## admin:org token — revoke when done`

# Deterministic excerpt

```markdown
# Branch protection — required checks per repo

Current `main` protection across the org (set in Wave 6). PR-Agent is **never**
required (advisory, same-repo-only — requiring it would wedge fork/dependabot
PRs). Semgrep is required as a *presence* gate while reporting-only; flip it to
a blocking gate per `docs/ci/semgrep.md` once each repo's baseline is triaged.

| Repo | Required checks | strict | reviews | enforce_admins |
|------|-----------------|:------:|:-------:|:--------------:|
| `network-operations` | `lint, render, iac-gate, semgrep` | ✓ | 1 | off |
| `hyrule-web` | `test, frontend` | ✓ | 1 | off |
| `hyrule-cloud` | `test, semgrep` | ✓ | 0 | off |
| `noc-agent` | `semgrep` | ✓ | 0 | off |
| `hyrule-mcp` | `semgrep` | ✓ | 0 | off |
| `as215932.net` | `semgrep` | ✓ | 0 | off |

`Sourcery review` was removed from `network-operations` **before** the
`sourcery-ai` app was uninstalled (no window where merges blocked on a check
that could never report). The app is gone (`gh api orgs/AS215932/installations`
lists only `claude-for-github`, `claude`).

## Why these settings

- **No required reviews on the four newly-protected repos** (and `enforce_admins`
  off everywhere): this is a solo-maintainer org. Requiring an approval with no
  second maintainer forces an `--admin` bypass on every merge (self-approval is
  forbidden) and risks a merge lockout. `network-operations`/`hyrule-web` keep
  their pre-existing 1-review rule; the rest protect via status checks + no
  force-push/deletion. Tighten later when there's a second reviewer. The
  `@AS215932/ops` team exists and backs `.github/CODEOWNERS`, but
  `require_code_owner_reviews` is intentionally left **off** for now.
- **`semgrep`-only on `noc-agent`/`hyrule-mcp`/`as215932.net`**: those repos have
  no test/lint wor
...
```

# Citations

[1] [docs/ci/branch-protection.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/branch-protection.md)
