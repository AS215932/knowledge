---
type: Source Document
title: Hyrule MCP
description: '`hyrule-mcp` is the live diagnostic substrate for Hyrule Networks (AS215932).
  It exposes narrow, bounded Model Context Protocol tools for monitoring, routing,
  host, firewall, and packet-path inspection.'
resource: https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/README.md
tags:
- as215932
- hyrule-mcp
- source-document
timestamp: '2026-06-15T17:46:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-mcp
  path: README.md
  commit: 326bcc85e1c69f0d7c1839ebaa4abb73acd84185
  lines: 1-177
  url: https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/README.md#L1-L177
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-mcp
source_path: README.md
commit: 326bcc85e1c69f0d7c1839ebaa4abb73acd84185
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-mcp` |
| Path | `README.md` |
| Commit | `326bcc85e1c69f0d7c1839ebaa4abb73acd84185` |
| Lines | `177` |

# Detected headings

* `# Hyrule MCP`
* `## Runtime shape`
* `## Tool design`
* `## Core diagnostic families`
* `## Resource safety`
* `## Icinga behavior`
* `## Tests`
* `## Quick start`
* `### Run the daemon`
* `### Connect`
* `## Tool catalog`
* `## No-op rollback guards`
* `## Safety model`
* `## Related repositories`

# Deterministic excerpt

```markdown
# Hyrule MCP

`hyrule-mcp` is the live diagnostic substrate for Hyrule Networks (AS215932).
It exposes narrow, bounded Model Context Protocol tools for monitoring, routing,
host, firewall, and packet-path inspection.

## Runtime shape

- Runs as either the legacy stdio server or a supervised local daemon on `noc`.
- The daemon serves MCP over loopback streamable HTTP and exposes `/health`.
- Host-targeted tools short-circuit to local subprocess execution when the
  target resolves to the MCP host itself.
- Remote host work uses the configured noc MCP SSH key and host resolver.

The intended production daemon mode is:

```bash
HYRULE_MCP_TRANSPORT=http \
HYRULE_MCP_BIND=127.0.0.1 \
HYRULE_MCP_PORT=8765 \
python mcp_server.py
```

NOC Agent then connects to `http://127.0.0.1:8765/mcp`.

## Tool design

The server follows three layers:

1. Specialized read tools first.
2. Purpose-built diagnostic helpers for correlation-heavy checks.
3. Raw SSH only as a bounded escape hatch.

Command-style returns preserve:

- `stdout`
- `stderr`
- `exit_code`
- `duration_ms`
- `transport`
- `data.command`
- `data.argv`
- `data.resolved_target`

`data.resolved_target` reports the resolved target name, address, username, and
whether an SSH key is configured; it does not include private key paths.

## Core diagnostic families

- Monitoring:
  - `prometheus_query`
  - `prometheus_list_targets`
  - `icinga_get_host_state`
- Routing and path:
  - `frr_vtysh_cmd`
  - `path_explain`
  - `ecmp_path_select`
  - `multi_source_probe`
- Packet and firewall:
  - `tcpdump_capture`
  - `pf_log_tail`
  - `nft_log_tail`
  - `firewall_state`
  - `ndp_state`
  - `arp_state`
- Host/service:
  - `os_systemd_status`
  - `os_journalctl`
  - `dmesg_tail`
  - `service_restart_history`
  - `vault_agent_status`
- D
...
```

# Citations

[1] [README.md](https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/README.md)
