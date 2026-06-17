---
type: API Schema
title: VMCreateRequest
description: Pydantic API schema `VMCreateRequest` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L186-L213
tags:
- api-schema
- hyrule-cloud
- pydantic
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/models.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 186-213
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L186-L213
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: VMCreateRequest
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `VMCreateRequest` |
| Source | `hyrule_cloud/models.py:186` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `duration_days` | `int` | `False` | `Field(ge=1, le=365, description='Hosting duration in days')` | Hosting duration in days |
| `size` | `VMSize` | `False` | `Field(default=VMSize.XS, description='VM size tier')` | VM size tier |
| `os` | `str` | `False` | `Field(default='debian-13', description='OS template name')` | OS template name |
| `ssh_pubkey` | `str` | `False` | `Field(description='SSH public key for root access (ed25519 or rsa)')` | SSH public key for root access (ed25519 or rsa) |
| `domain_mode` | `DomainMode` | `False` | `Field(default=DomainMode.AUTO)` |  |
| `domain` | `str | None` | `False` | `Field(default=None, description='Domain to register (required when domain_mod...` | Domain to register (required when domain_mode=custom) |
| `open_ports` | `list[int]` | `False` | `Field(default_factory=lambda: [80, 443], description='Inbound TCP ports to al...` | Inbound TCP ports to allow (22 always included) |
| `setup_script` | `str | None` | `False` | `Field(default=None, description='Optional shell script to execute after boot ...` | Optional shell script to execute after boot via cloud-init |
| `quote_id` | `str | None` | `False` | `Field(default=None, max_length=36, description='Optional durable quote id fro...` | Optional durable quote id from POST /v1/vm/quote. When set, the server provisions the spec stored on the quote at the quote-locked price; the rest of this body must match that stored spec. Omit for the legacy compute-price-from-body flow. |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:186-213](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L186-L213)
