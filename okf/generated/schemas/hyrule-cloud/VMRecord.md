---
type: API Schema
title: VMRecord
description: Pydantic API schema `VMRecord` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L423-L444
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
  lines: 423-444
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L423-L444
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: VMRecord
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `VMRecord` |
| Source | `hyrule_cloud/models.py:423` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `vm_id` | `str` | `False` | `Field(default_factory=generate_vm_id)` |  |
| `xcpng_uuid` | `str | None` | `False` | `None` |  |
| `owner_wallet` | `str` | `False` | `<string>` |  |
| `status` | `VMStatus` | `False` | `VMStatus.PROVISIONING` |  |
| `size` | `VMSize` | `False` | `VMSize.XS` |  |
| `os` | `str` | `False` | `<string>` |  |
| `ipv6` | `str | None` | `False` | `None` |  |
| `hostname` | `str | None` | `False` | `None` |  |
| `ssh_pubkey` | `str` | `False` | `<string>` |  |
| `open_ports` | `list[int]` | `False` | `Field(default_factory=lambda: [22, 80, 443])` |  |
| `setup_script` | `str | None` | `False` | `None` |  |
| `domain_mode` | `DomainMode` | `False` | `DomainMode.AUTO` |  |
| `domain` | `str | None` | `False` | `None` |  |
| `created_at` | `datetime` | `False` | `Field(default_factory=datetime.utcnow)` |  |
| `expires_at` | `datetime | None` | `False` | `None` |  |
| `destroyed_at` | `datetime | None` | `False` | `None` |  |
| `error` | `str | None` | `False` | `None` |  |
| `payment_tx` | `str | None` | `False` | `None` |  |
| `cost_total` | `Decimal` | `False` | `Decimal('0')` |  |

# Validators

No validators statically detected.

# Documentation

Internal record tracking a VM through its lifecycle.

# Citations

[1] [hyrule_cloud/models.py:423-444](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L423-L444)
