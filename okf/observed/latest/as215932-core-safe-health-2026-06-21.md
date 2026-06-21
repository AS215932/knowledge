---
type: Observation
title: AS215932 core automation safe-health snapshot 2026-06-21
description: Sanitized point-in-time evidence for loop automation, Knowledge MCP, NOC Agent, Hyrule MCP, Docker IPv6, Prometheus, and Icinga.
tags:
- docker-ipv6
- engineering-loop
- hyrule-mcp
- icinga
- knowledge-mcp
- noc-agent
- observed
- prometheus
- safe-health
truth_owner: observed
authority: evidence
source_refs:
- url: manual://as215932-core-safe-health/2026-06-21
- url: manual://loop/as215932-core-safe-health/2026-06-21
- url: manual://noc/as215932-core-safe-health/2026-06-21
- url: manual://mon/as215932-core-safe-health/2026-06-21
last_verified_at: '2026-06-21T17:58:26Z'
confidence: medium
dispute_policy: evidence_only
observed_at: '2026-06-21T17:58:26Z'
expires_at: '2026-06-22T17:58:26Z'
collection_profile: as215932-core-safe-health
observation_source: manual-local-readonly
observation_status: degraded
payload_json: '{"collection_window":{"ended_at":"2026-06-21T17:58:26Z","started_at":"2026-06-21T17:52:31Z"},"expires_at":"2026-06-22T17:58:26Z","observed_at":"2026-06-21T17:58:26Z","profile":"as215932-core-safe-health","sources":{"docker_ipv6":{"bridge_has_fixed_subnet":true,"daemon_ipv6":true,"default_bridge_ipv6_ping_dns":"ok","dns_count":1,"fixed_cidr_v6":"2a0c:b641:b50:f0::/64","ip6tables":false,"ip_masq":false,"status":"ok"},"engineering_loop":{"runtime_head":"d4781edbef0cab9ca983f622b4aa2a960df16a97","status":"ok","timer_state":"active","vault_agent_state":"active"},"hyrule_mcp":{"health_http_status":200,"health_status":"ok","runtime_head":"05b1245710e6a67ad40ccd62c033755f48ad4958","service_state":"active","status":"ok","transport":"streamable-http"},"icinga":{"selected_services":[{"host":"loop","output":"loop idle (approved queue is empty)","service":"engineering-loop","state":0},{"host":"loop","output":"UNKNOWN: query returned no data","service":"knowledge-mcp-service","state":3},{"host":"noc","output":"HTTP OK","service":"noc-agent-config-health","state":0},{"host":"noc","output":"HTTP OK","service":"noc-agent-health","state":0},{"host":"noc","output":"OK - status=ok mailbox=INBOX count=106","service":"noc-agent-mail-health","state":0},{"host":"noc","output":"OK - status=ok hyrule_ready=true xo_ready=true","service":"noc-agent-mcp-health","state":0},{"host":"noc","output":"OK - primary=openrouter:deepseek/deepseek-v4-pro status=ok quota=ok","service":"noc-agent-model-health","state":0}],"service_count":149,"service_state":"active","service_states":{"ok":144,"unknown":4,"warning":1},"status":"degraded","unhandled_problem_services":4},"knowledge_mcp":{"claim_count":4569,"concept_count":867,"container_revision":"69e9a30bcb11a6242f6d4adc4587e48ce20e5754","health_status":"ok","observation_count_before_ingest":1,"read_only":true,"run_id":"local-20260621165518","runtime_head":"69e9a30bcb11a6242f6d4adc4587e48ce20e5754","service_state":"active","status":"ok","tool_count":14,"transport":"streamable-http"},"noc_agent":{"config_disabled_count":0,"config_missing_count":0,"config_status":"ok","configured_model_count":2,"health_http_status":200,"health_status":"ok","mail_message_count":106,"mail_status":"ok","missing_credentials_count":0,"model_status":"ok","provider_status":{"openrouter":"ok"},"quota_monitoring":"ok","runtime_head":"2ba3fab7af61ad51a125fb8c85f021bb82555bf3","service_state":"active","status":"ok","vault_agent_state":"active"},"prometheus":{"down_series":2,"query_status":"success","ready_http_status":200,"service_state":"active","status":"degraded","up_series":54}}}'
---

# AS215932 core automation safe-health snapshot

This file is sanitized observed evidence only. It does not define intended state and must lose to source repositories when facts conflict.

Collection window: `2026-06-21T17:52:31Z` to `2026-06-21T17:58:26Z`. Evidence expires at `2026-06-22T17:58:26Z`.

# Source summary

| Source | Status | Sanitized evidence |
| --- | --- | --- |
| `engineering_loop` | `ok` | timer `active`; Vault Agent `active`; runtime `d4781edbef0cab9ca983f622b4aa2a960df16a97` |
| `knowledge_mcp` | `ok` | service `active`; HTTP health `ok`; `streamable-http`; read-only; 14 tools; 867 concepts; 4569 claims |
| `docker_ipv6` | `ok` | Docker IPv6 enabled; routed bridge `2a0c:b641:b50:f0::/64`; IPv6 ping from default bridge to AS215932 resolver `ok` |
| `noc_agent` | `ok` | service `active`; config `ok`; mail `ok`; model/quota health `ok`; no missing credentials reported by health endpoint |
| `hyrule_mcp` | `ok` | service `active`; loopback health `ok`; `streamable-http` |
| `prometheus` | `degraded` | service `active`; ready endpoint HTTP 200; `up` query succeeded with 54 series and 2 down series |
| `icinga` | `degraded` | service `active`; 149 services; 144 OK, 1 WARNING, 4 UNKNOWN; selected NOC Agent checks OK; `loop!knowledge-mcp-service` UNKNOWN at collection time |

# Interpretation boundaries

- `prometheus` and `icinga` degraded statuses are observed monitoring evidence only; they do not prove intended state drift by themselves.
- Direct Knowledge MCP and Docker IPv6 checks were OK during the same window even though the selected Icinga Knowledge MCP service was UNKNOWN.
- Provider model health is summarized without token values, authorization headers, raw logs, or raw API responses.

# Sanitized payload

```json
{
  "collection_window": {
    "ended_at": "2026-06-21T17:58:26Z",
    "started_at": "2026-06-21T17:52:31Z"
  },
  "expires_at": "2026-06-22T17:58:26Z",
  "observed_at": "2026-06-21T17:58:26Z",
  "profile": "as215932-core-safe-health",
  "sources": {
    "docker_ipv6": {
      "bridge_has_fixed_subnet": true,
      "daemon_ipv6": true,
      "default_bridge_ipv6_ping_dns": "ok",
      "dns_count": 1,
      "fixed_cidr_v6": "2a0c:b641:b50:f0::/64",
      "ip6tables": false,
      "ip_masq": false,
      "status": "ok"
    },
    "engineering_loop": {
      "runtime_head": "d4781edbef0cab9ca983f622b4aa2a960df16a97",
      "status": "ok",
      "timer_state": "active",
      "vault_agent_state": "active"
    },
    "hyrule_mcp": {
      "health_http_status": 200,
      "health_status": "ok",
      "runtime_head": "05b1245710e6a67ad40ccd62c033755f48ad4958",
      "service_state": "active",
      "status": "ok",
      "transport": "streamable-http"
    },
    "icinga": {
      "selected_services": [
        {
          "host": "loop",
          "output": "loop idle (approved queue is empty)",
          "service": "engineering-loop",
          "state": 0
        },
        {
          "host": "loop",
          "output": "UNKNOWN: query returned no data",
          "service": "knowledge-mcp-service",
          "state": 3
        },
        {
          "host": "noc",
          "output": "HTTP OK",
          "service": "noc-agent-config-health",
          "state": 0
        },
        {
          "host": "noc",
          "output": "HTTP OK",
          "service": "noc-agent-health",
          "state": 0
        },
        {
          "host": "noc",
          "output": "OK - status=ok mailbox=INBOX count=106",
          "service": "noc-agent-mail-health",
          "state": 0
        },
        {
          "host": "noc",
          "output": "OK - status=ok hyrule_ready=true xo_ready=true",
          "service": "noc-agent-mcp-health",
          "state": 0
        },
        {
          "host": "noc",
          "output": "OK - primary=openrouter:deepseek/deepseek-v4-pro status=ok quota=ok",
          "service": "noc-agent-model-health",
          "state": 0
        }
      ],
      "service_count": 149,
      "service_state": "active",
      "service_states": {
        "ok": 144,
        "unknown": 4,
        "warning": 1
      },
      "status": "degraded",
      "unhandled_problem_services": 4
    },
    "knowledge_mcp": {
      "claim_count": 4569,
      "concept_count": 867,
      "container_revision": "69e9a30bcb11a6242f6d4adc4587e48ce20e5754",
      "health_status": "ok",
      "observation_count_before_ingest": 1,
      "read_only": true,
      "run_id": "local-20260621165518",
      "runtime_head": "69e9a30bcb11a6242f6d4adc4587e48ce20e5754",
      "service_state": "active",
      "status": "ok",
      "tool_count": 14,
      "transport": "streamable-http"
    },
    "noc_agent": {
      "config_disabled_count": 0,
      "config_missing_count": 0,
      "config_status": "ok",
      "configured_model_count": 2,
      "health_http_status": 200,
      "health_status": "ok",
      "mail_message_count": 106,
      "mail_status": "ok",
      "missing_credentials_count": 0,
      "model_status": "ok",
      "provider_status": {
        "openrouter": "ok"
      },
      "quota_monitoring": "ok",
      "runtime_head": "2ba3fab7af61ad51a125fb8c85f021bb82555bf3",
      "service_state": "active",
      "status": "ok",
      "vault_agent_state": "active"
    },
    "prometheus": {
      "down_series": 2,
      "query_status": "success",
      "ready_http_status": 200,
      "service_state": "active",
      "status": "degraded",
      "up_series": 54
    }
  }
}
```
