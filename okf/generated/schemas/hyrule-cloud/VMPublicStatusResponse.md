---
type: API Schema
title: VMPublicStatusResponse
description: Pydantic API schema `VMPublicStatusResponse` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L279-L302
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
  lines: 279-302
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L279-L302
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: VMPublicStatusResponse
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `VMPublicStatusResponse` |
| Source | `hyrule_cloud/models.py:279` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `vm_id` | `str` | `True` | `` |  |
| `status` | `VMStatus` | `True` | `` |  |
| `ipv6` | `str | None` | `False` | `None` |  |
| `hostname` | `str | None` | `False` | `None` |  |
| `expires_at` | `datetime | None` | `False` | `None` |  |
| `launch_proof_status` | `LaunchProofStatus | None` | `False` | `None` |  |
| `payment_status` | `PaymentStatus | None` | `False` | `None` |  |
| `dns_aaaa_verified` | `bool` | `False` | `False` |  |
| `ssh_smoke_status` | `SSHSmokeStatus` | `False` | `SSHSmokeStatus.NOT_RUN` |  |
| `rollback_available` | `bool` | `False` | `False` |  |
| `operator_message` | `str | None` | `False` | `None` |  |
| `customer_message` | `str | None` | `False` | `None` |  |

# Validators

No validators statically detected.

# Documentation

Sanitized public view returned by `GET /v1/vm/{id}/status`.

Block A0: any caller (no token, no account) can fetch this for any
vm_id. Reveals only the fields needed for an order-status page —
NO ssh string, NO firewall config, NO provisioning error detail.

Issue #28: enriched with launch-proof contract fields so a customer
can follow a VM from quote acceptance through provisioned/failed.

# Citations

[1] [hyrule_cloud/models.py:279-302](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L279-L302)
