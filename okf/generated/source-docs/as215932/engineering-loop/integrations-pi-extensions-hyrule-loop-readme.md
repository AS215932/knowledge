---
type: Source Document
title: Hyrule Loop Pi Extension
description: This directory contains the repo-owned source for the Pi `/loop` extension
  that fronts the Hyrule Engineering Loop.
resource: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/integrations/pi/extensions/hyrule-loop/README.md
tags:
- as215932
- engineering-loop
- source-document
timestamp: '2026-06-16T07:29:23Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/engineering-loop
  path: integrations/pi/extensions/hyrule-loop/README.md
  commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
  lines: 1-58
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/integrations/pi/extensions/hyrule-loop/README.md#L1-L58
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/engineering-loop
source_path: integrations/pi/extensions/hyrule-loop/README.md
commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/engineering-loop` |
| Path | `integrations/pi/extensions/hyrule-loop/README.md` |
| Commit | `768cde6c996e42f3f91d395347ba9809e2e020e5` |
| Lines | `58` |

# Detected headings

* `# Hyrule Loop Pi Extension`
* `## Install / Sync`
* `## Configuration`
* `## Source of Truth`

# Deterministic excerpt

```markdown
# Hyrule Loop Pi Extension

This directory contains the repo-owned source for the Pi `/loop` extension that
fronts the Hyrule Engineering Loop.

The extension is intentionally thin:

- turns a prompt or Plan Mode handoff into a request markdown file;
- calls `uv run hyrule-engineering-loop feature ...` from this repo;
- records state, trace, NOC handoff, model, diff, sign-off, and failure
  summaries in the Pi session;
- provides `/loop status`, `/loop trace`, `/loop cleanup`, and `/loop approve`
  helpers for the latest run.

## Install / Sync

Until Pi has a packaged extension installer for this repo, sync the source into
the local Pi extension directory:

```bash
mkdir -p ~/.pi/agent/extensions/hyrule-loop
cp integrations/pi/extensions/hyrule-loop/index.ts \
  ~/.pi/agent/extensions/hyrule-loop/index.ts
```

Run Pi from a `hyrule-*` checkout and invoke:

```text
/loop Add X in the order flow
/loop --repo hyrule-web Add X in the order flow
/loop --plan
/loop status
/loop trace
```

## Configuration

The extension currently autodetects the active `hyrule-*` repo from the current
working directory and falls back to `hyrule-cloud`.

Default paths are defined in `index.ts`:

```text
workspaceRoot: /home/svag/Dev
infraRepo: /home/svag/Dev/hyrule-infra
outputRoot: /tmp/hyrule-loop
defaultRepo: hyrule-cloud
defaultAllow: docs
defaultSources: README.md
```

A project-local override i
...
```

# Citations

[1] [integrations/pi/extensions/hyrule-loop/README.md](https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/integrations/pi/extensions/hyrule-loop/README.md)
