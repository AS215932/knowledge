---
type: Source Document
title: Values MATCH hyrule_cloud.models.QuoteStatus so an alembic-migrated DB and
  a
description: '"""vm_quotes: durable order quotes (issue #14)'
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/alembic/versions/008_vm_quotes.py
tags:
- as215932
- hyrule-cloud
- source-document
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: alembic/versions/008_vm_quotes.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1-79
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/alembic/versions/008_vm_quotes.py#L1-L79
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
source_path: alembic/versions/008_vm_quotes.py
commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-cloud` |
| Path | `alembic/versions/008_vm_quotes.py` |
| Commit | `81e4316f3d1f4e7f770bc2589bd84a2c7972aad5` |
| Lines | `79` |

# Detected headings

* `# Values MATCH hyrule_cloud.models.QuoteStatus so an alembic-migrated DB and a`
* `# create_all() DB (tests) produce the same enum.`
* `# JSONB on Postgres, generic JSON on SQLite (tests use create_all, not this`
* `# migration, but keep the variant for parity).`
* `# sa.Enum inside create_table emits CREATE TYPE before CREATE TABLE on`
* `# Postgres and a CHECK constraint on SQLite — matching the model's`
* `# Enum(..., name="vm_quote_status").`
* `# Model declares client_order_id unique=True+index=True → create_all renders`
* `# a unique index of this name. Match it so autogenerate stays quiet.`
* `# create_table auto-created the enum on Postgres; drop it explicitly so a`
* `# downgrade leaves no orphan type behind. checkfirst keeps SQLite happy.`

# Citations

[1] [alembic/versions/008_vm_quotes.py](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/alembic/versions/008_vm_quotes.py)
