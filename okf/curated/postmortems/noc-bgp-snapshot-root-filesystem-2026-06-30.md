---
type: Postmortem
title: NOC BGP snapshots filled root filesystem
description: Reviewed operator context for the low root filesystem handoff on noc caused by unbounded BGP router snapshots.
tags:
- noc
- bgp
- disk
- retention
- engineering-handoff
truth_owner: okf
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: docs/runbooks/noc-bgp-snapshot-retention.md
  commit: e0e643a1f5e1fefdb458478e468fbf6b3bca13b2
  url: https://github.com/AS215932/network-operations/blob/e0e643a1f5e1fefdb458478e468fbf6b3bca13b2/docs/runbooks/noc-bgp-snapshot-retention.md
- url: https://github.com/AS215932/network-operations/issues/321
last_verified_at: '2026-07-01T02:42:42Z'
confidence: high
dispute_policy: adjudicate
review_status: reviewed
---

# NOC BGP snapshot root filesystem incident

The `noc` host stores Hyrule MCP BGP router table snapshots under
`/var/lib/hyrule-mcp/bgp-snapshots`. On 2026-06-30, hourly snapshots filled the
root filesystem because snapshot metadata contained a 7 day `expires_at` but no
host-local retention mechanism enforced that horizon.

# Impact

The root filesystem reached 100 percent usage. `apt-get update` failed with
`No space left on device`, which caused unrelated Ansible applies against `noc`
to fail.

# Immediate mitigation

Operators stopped and disabled `bgp-router-snapshot.timer`, cleaned apt cache
and journals, verified `apt-get update` succeeded, and left `/` with healthy
free space. This is a temporary mitigation only.

# Permanent fix

Engineering work for low root filesystem NOC handoffs should implement the
`noc` Ansible fix:

- manage `bgp-router-snapshot.service` and `bgp-router-snapshot.timer`, or
  explicitly remove unmanaged copies;
- enforce retention on `/var/lib/hyrule-mcp/bgp-snapshots` before enabling the
  timer;
- default retention to 7 days to match snapshot metadata;
- prefer `systemd-tmpfiles` unless a dedicated cleanup timer is required;
- re-enable `bgp-router-snapshot.timer` only after retention is active.

# Verification

The remediation is complete when `bgp-router-snapshot.timer` is active, cleanup
policy exists and can run, `/` has healthy free space, `apt-get update`
succeeds, and the NOC CaseService health endpoints remain healthy.

# Handoff mapping

NOC CaseService handoffs with the objective "resolve low root filesystem
condition" on `noc` should retrieve this context and route to Engineering Loop
for an Ansible retention fix, not to suppression or a NOC-only disk cleanup.

# Citations

[1] [NOC BGP router snapshot retention](https://github.com/AS215932/network-operations/blob/e0e643a1f5e1fefdb458478e468fbf6b3bca13b2/docs/runbooks/noc-bgp-snapshot-retention.md)
[2] [network-operations issue #321](https://github.com/AS215932/network-operations/issues/321)
