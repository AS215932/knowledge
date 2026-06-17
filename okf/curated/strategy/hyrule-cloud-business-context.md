---
type: Strategy
title: Hyrule Cloud Business Context
description: Business and pricing context for Hyrule Cloud hosting economics.
tags:
- curated
- proposed
- strategy
truth_owner: okf
authority: advisory
source_refs:
- repo: AS215932/hyrule-business
  path: hosting-cost-analysis.md
  commit: 89febc9c95fb6766df071e054cb44fba0b1ec8e4
  url: https://github.com/AS215932/hyrule-business/blob/89febc9c95fb6766df071e054cb44fba0b1ec8e4/hosting-cost-analysis.md
- repo: AS215932/hyrule-cloud
  path: README.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/README.md
last_verified_at: '2026-06-17T10:18:30Z'
confidence: medium
dispute_policy: adjudicate
review_status: proposed
---

# Business context

Hyrule Cloud targets AI agents and builders that need deployable VPS capacity with x402 payment flows. The business notes model OVH/XCP-ng hosting economics, IPv6-only margins, optional IPv4 lease costs, and small/medium/large VM pricing.

# Strategy signals

- IPv6-only capacity materially improves early economics.
- A leased IPv4 /24 is a fixed cost that becomes efficient only at higher density.
- RISE-S class servers are modeled as cost-efficient launch capacity.
- Product simplicity matters: bare VMs reduce PaaS support burden while preserving agent autonomy.

# Review status

This page is proposed strategy synthesis. Treat the business repo as canonical for numeric assumptions.

# Citations

[1] [AS215932/hyrule-business:hosting-cost-analysis.md](https://github.com/AS215932/hyrule-business/blob/89febc9c95fb6766df071e054cb44fba0b1ec8e4/hosting-cost-analysis.md)
[2] [AS215932/hyrule-cloud:README.md](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/README.md)
