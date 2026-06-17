---
type: Source Document
title: Semgrep (token-less SAST)
description: Semgrep is the real security gate (PR-Agent is advisory). It runs token-less
  — no `SEMGREP_APP_TOKEN`, no dashboard — and uploads SARIF to GitHub Code Scanning
  (free for public repos).
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/semgrep.md
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: docs/ci/semgrep.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-47
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/semgrep.md#L1-L47
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: docs/ci/semgrep.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `docs/ci/semgrep.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `47` |

# Detected headings

* `# Semgrep (token-less SAST)`
* `## Reporting-only baseline → gate`
* `## Packs`
* `## Fork note`
* `## Triage`

# Deterministic excerpt

```markdown
# Semgrep (token-less SAST)

Semgrep is the real security gate (PR-Agent is advisory). It runs token-less —
no `SEMGREP_APP_TOKEN`, no dashboard — and uploads SARIF to GitHub Code Scanning
(free for public repos).

- Image: `semgrep/semgrep@sha256:bc8b15e245d7bd392bcadce7ef4db36601b375fab35bfd8070ed8ae3d7824c74`, pinned by digest, run via `docker run` (not a job `container:`, so the Node-based upload-sarif action runs in the normal runner env).
- Upload: `github/codeql-action/upload-sarif@84498526a009a99c875e83ef4821a8ba52de7c22`.
- Runner: `hyrule-public-pr` (unprivileged).
- Triggers: every PR, `workflow_dispatch`, push on workflow/rule changes, nightly cron.

## Reporting-only baseline → gate

The `Run Semgrep` step is `continue-on-error: true` during the baseline, so
findings land in the Security tab without failing the job. The `semgrep` job
itself therefore (almost) always reports success — which is why it is safe to
require as a status check now: it guarantees the scan *runs* on every PR.

To turn Semgrep into a true blocking gate once the baseline is triaged: drop
`continue-on-error` from the scan step (or use `semgrep ci --error`). Do this
per repo only after the existing findings are reviewed — don't block on
historical findings. Recommended progression: baseline (reporting-only) → block
new high-severity → high-confidence medium+ on the security-sensitive repos
(`hyrule-cloud`, `noc-agent`, `hyrule-mcp`).

## Packs

Curated `p/` rulesets per stack (`p/ci`, `p/github-actions`, `p/secrets`, plus
`p/python` / `p/javascript` / `p/typescript` as relevant). The Actions rules are
the security-critical ones for this org: they flag `pull_request_target`,
`permissions: write-all`, unpinned third-party actions, `curl | sh`, secrets
echoed to logs, and self-hosted-runner
...
```

# Citations

[1] [docs/ci/semgrep.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/semgrep.md)
