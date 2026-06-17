---
type: Source Document
title: Implementation Writer
description: '- Producing the smallest useful implementation tranche for the active
  feature request. - Returning structured file mutations only. - Respecting the target
  repository, allowed paths, source context, senior role approvals, and current Grap...'
resource: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/docs/agent-loops/implementation-writer.md
tags:
- as215932
- engineering-loop
- source-document
timestamp: '2026-06-16T07:29:23Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/engineering-loop
  path: docs/agent-loops/implementation-writer.md
  commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
  lines: 1-48
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/docs/agent-loops/implementation-writer.md#L1-L48
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/engineering-loop
source_path: docs/agent-loops/implementation-writer.md
commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/engineering-loop` |
| Path | `docs/agent-loops/implementation-writer.md` |
| Commit | `768cde6c996e42f3f91d395347ba9809e2e020e5` |
| Lines | `48` |

# Detected headings

* `# Implementation Writer`
* `## Owns`
* `## Input Contract`
* `## Output Contract`
* `## Must Reject`

# Deterministic excerpt

```markdown
# Implementation Writer

## Owns

- Producing the smallest useful implementation tranche for the active feature
  request.
- Returning structured file mutations only.
- Respecting the target repository, allowed paths, source context, senior role
  approvals, and current GraphState.
- Keeping generated changes reviewable by humans before commit or PR creation.

## Input Contract

Use the active GraphState plus repository context bundle. Treat
`repo_context_bundle.repos[].allowed_paths` as the mutation boundary. Source
files are partial context and may be truncated.

## Output Contract

Return JSON matching the structured role output schema:

```json
{
  "approved": true,
  "validation_errors": [],
  "proposed_mutations": [
    {
      "path": "repo-name:relative/path",
      "content": "complete target file content",
      "operation": "create"
    }
  ],
  "notes": "short implementation note"
}
```

Allowed operations:

- `create`: only for files that should not already exist.
- `replace`: only for files that must already exist.

## Must Reject

- Mutations outside allowed paths.
- Partial patches or diff hunks instead of complete file content.
- Secret material, credentials, or environment-specific tokens.
- Changes that require live production credentials by default.
- Broad rewrites when a smaller file tranche satisfies the request.
```

# Citations

[1] [docs/agent-loops/implementation-writer.md](https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/docs/agent-loops/implementation-writer.md)
