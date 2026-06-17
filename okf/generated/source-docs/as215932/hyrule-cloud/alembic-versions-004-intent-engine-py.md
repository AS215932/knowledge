---
type: Source Document
title: 'Full crypto_intent_status value set: the legacy toy `pending`/`paid` plus
  the'
description: '"""native crypto intent engine: state machine + idempotency + ownership
  link'
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/alembic/versions/004_intent_engine.py
tags:
- as215932
- hyrule-cloud
- source-document
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: alembic/versions/004_intent_engine.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1-156
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/alembic/versions/004_intent_engine.py#L1-L156
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
source_path: alembic/versions/004_intent_engine.py
commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-cloud` |
| Path | `alembic/versions/004_intent_engine.py` |
| Commit | `81e4316f3d1f4e7f770bc2589bd84a2c7972aad5` |
| Lines | `156` |

# Detected headings

* `# Full crypto_intent_status value set: the legacy toy `pending`/`paid` plus the`
* `# Block E state machine. Order MATCHES hyrule_cloud.models.CryptoIntentStatus so`
* `# an alembic-migrated DB and a create_all() DB (tests) produce the same enum.`
* `# Fail fast with an actionable message if the legacy toy schema is still`
* `# present, rather than a cryptic "relation/type already exists". The only`
* `# environment that ever had it is `api`; playbooks/cloud_toy_cleanup.yml`
* `# drops the empty toy accounts + crypto_intents + crypto_intent_status and`
* `# is the documented pre-migration step.`
* `# The crypto_intents table + crypto_intent_status enum are CREATED here,`
* `# not extended. Earlier revisions of this migration assumed both already`
* `# existed from the hand-applied db_patch toy scripts on `api`; that made the`
* `# chain unappliable on a clean DB (disaster recovery, new env, alembic CI).`
* `# We now create the full Block E shape from scratch so 001→006 applies on`
* `# any empty database. This is dead schema until Wave 4 flips`
* `# HYR_FEATURES_INTENT_ENGINE; no code reads it before then.`
* `#`
* `# JSONB on Postgres, generic JSON on SQLite (tests use create_all, not this`
* `# migration, but keep the variant for parity).`
* `# sa.Enum inside create_table emits CREATE TYPE before CREATE TABLE on`
* `# Postgres and a CHECK constraint on SQLite — matching the model's`
* `# Enum(..., name="crypto_intent_status"). Listing literal values (not user`
* `# input) sidesteps the ALTER TYPE string-interpolation the old revision`
* `# needed (and the Sourcery SQL-injection finding it carried).`
* `# --- Block E additions ---`

# Citations

[1] [alembic/versions/004_intent_engine.py](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/alembic/versions/004_intent_engine.py)
