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
- url: https://github.com/AS215932/network-operations/commit/153a7055ff6a39b976571bc5f2ba6dc9ba861866
- url: https://github.com/AS215932/network-operations/issues/214
last_verified_at: '2026-06-21T21:12:38Z'
confidence: medium
dispute_policy: evidence_only
observed_at: '2026-06-21T21:12:38Z'
expires_at: '2026-06-22T21:12:38Z'
collection_profile: as215932-core-safe-health
observation_source: manual-local-readonly
observation_status: ok
payload_json: '{"collection_window":{"ended_at":"2026-06-21T21:12:38Z","started_at":"2026-06-21T21:05:54Z"},"expires_at":"2026-06-22T21:12:38Z","observed_at":"2026-06-21T21:12:38Z","profile":"as215932-core-safe-health","sources":{"docker_ipv6":{"bridge_has_fixed_subnet":true,"daemon_ipv6":true,"default_bridge_ipv6_ping_dns":"ok","dns_count":1,"fixed_cidr_v6":"2a0c:b641:b50:f0::/64","ip6tables":false,"ip_masq":false,"status":"ok"},"engineering_loop":{"runtime_head":"d4781edbef0cab9ca983f622b4aa2a960df16a97","status":"ok","timer_state":"active","vault_agent_state":"active"},"hyrule_mcp":{"health_http_status":200,"health_status":"ok","runtime_head":"05b1245710e6a67ad40ccd62c033755f48ad4958","service_state":"active","status":"ok","tool_count":34,"transport":"streamable-http"},"icinga":{"selected_services":[{"host":"loop","output":"OK: up=1","service":"node-up","state":0},{"host":"loop","output":"OK: free_ratio=0.827","service":"disk disk /","state":0},{"host":"loop","output":"loop idle (approved queue is empty)","service":"engineering-loop","state":0},{"host":"loop","output":"OK: active=1","service":"engineering-loop-timer","state":0},{"host":"loop","output":"OK: active=1","service":"knowledge-mcp-service","state":0},{"host":"noc","output":"HTTP OK","service":"noc-agent-health","state":0},{"host":"noc","output":"OK - status=ok hyrule_ready=true hyrule_tools=34 xo_ready=true xo_tools=40","service":"noc-agent-mcp-health","state":0},{"host":"noc","output":"OK - primary=openrouter:deepseek/deepseek-v4-pro status=ok quota=ok","service":"noc-agent-model-health","state":0},{"acknowledged":true,"handled":true,"host":"rtr","output":"WARNING: free_ratio=0.113 (< 0.2)","service":"disk disk /","state":1}],"service_count":149,"service_state":"active","service_states":{"critical":0,"ok":148,"unknown":0,"warning":1},"status":"ok","unhandled_problem_services":0},"knowledge_mcp":{"claim_count":4584,"concept_count":868,"container_revision":"67b338757efe9b496c4e154fbb0212563b1b96e8","health_status":"ok","observation_count_before_ingest":2,"read_only":true,"run_id":"local-20260621180213","runtime_head":"67b338757efe9b496c4e154fbb0212563b1b96e8","service_state":"active","status":"ok","tool_count":14,"transport":"streamable-http"},"noc_agent":{"bot_service_state":"active","config_disabled_count":0,"config_missing_count":0,"config_status":"ok","configured_model_count":2,"health_http_status":200,"health_status":"ok","mail_message_count":106,"mail_status":"ok","missing_credentials_count":0,"model_status":"ok","provider_status":{"openrouter":"ok"},"quota_monitoring":"ok","runtime_head":"2ba3fab7af61ad51a125fb8c85f021bb82555bf3","service_state":"active","status":"ok","vault_agent_state":"active"},"prometheus":{"down_series":0,"loop_node_up":true,"query_status":"success","ready_http_status":200,"service_state":"active","status":"ok","up_series":55,"vault_internal_success":true,"vector_up":true}}}'
---

# AS215932 core automation safe-health snapshot

This file is sanitized observed evidence only. It does not define intended state and must lose to source repositories when facts conflict.

Collection window: `2026-06-21T21:05:54Z` to `2026-06-21T21:12:38Z`. Evidence expires at `2026-06-22T21:12:38Z`.

# Source summary

| Source | Status | Sanitized evidence |
| --- | --- | --- |
| `engineering_loop` | `ok` | timer `active`; Vault Agent `active`; runtime `d4781edbef0cab9ca983f622b4aa2a960df16a97` |
| `knowledge_mcp` | `ok` | service `active`; HTTP health `ok`; `streamable-http`; read-only; 14 tools; 868 concepts; 4584 claims |
| `docker_ipv6` | `ok` | Docker IPv6 enabled; routed bridge `2a0c:b641:b50:f0::/64`; IPv6 ping from default bridge to AS215932 resolver `ok` |
| `noc_agent` | `ok` | service `active`; config `ok`; mail `ok`; model/quota health `ok`; no missing credentials reported by health endpoint |
| `hyrule_mcp` | `ok` | service `active`; loopback health `ok`; `streamable-http`; 34 tools via NOC Agent MCP health |
| `prometheus` | `ok` | service `active`; ready endpoint HTTP 200; `up` query succeeded with 55 series and 0 down series; Vector and Vault internal probes healthy |
| `icinga` | `ok` | service `active`; 149 services; 148 OK, 1 acknowledged/handled WARNING, 0 UNKNOWN/CRITICAL; loop and selected NOC Agent checks OK |

# Interpretation boundaries

- Monitoring remediation after NetOps #288 is reflected here as observed evidence only; source repositories still define intended state.
- `netproxy` monitoring targets are intentionally disabled because that VM is not live yet and remains tracked for rollout separately.
- The remaining `rtr!disk /` warning was acknowledged/handled at collection time and is not a current unhandled core automation blocker.
- Provider model health is summarized without token values, authorization headers, raw logs, or raw API responses.

# Sanitized payload

```json
{
  "collection_window": {
    "ended_at": "2026-06-21T21:12:38Z",
    "started_at": "2026-06-21T21:05:54Z"
  },
  "expires_at": "2026-06-22T21:12:38Z",
  "observed_at": "2026-06-21T21:12:38Z",
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
      "tool_count": 34,
      "transport": "streamable-http"
    },
    "icinga": {
      "selected_services": [
        {
          "host": "loop",
          "output": "OK: up=1",
          "service": "node-up",
          "state": 0
        },
        {
          "host": "loop",
          "output": "OK: free_ratio=0.827",
          "service": "disk disk /",
          "state": 0
        },
        {
          "host": "loop",
          "output": "loop idle (approved queue is empty)",
          "service": "engineering-loop",
          "state": 0
        },
        {
          "host": "loop",
          "output": "OK: active=1",
          "service": "engineering-loop-timer",
          "state": 0
        },
        {
          "host": "loop",
          "output": "OK: active=1",
          "service": "knowledge-mcp-service",
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
          "output": "OK - status=ok hyrule_ready=true hyrule_tools=34 xo_ready=true xo_tools=40",
          "service": "noc-agent-mcp-health",
          "state": 0
        },
        {
          "host": "noc",
          "output": "OK - primary=openrouter:deepseek/deepseek-v4-pro status=ok quota=ok",
          "service": "noc-agent-model-health",
          "state": 0
        },
        {
          "acknowledged": true,
          "handled": true,
          "host": "rtr",
          "output": "WARNING: free_ratio=0.113 (< 0.2)",
          "service": "disk disk /",
          "state": 1
        }
      ],
      "service_count": 149,
      "service_state": "active",
      "service_states": {
        "critical": 0,
        "ok": 148,
        "unknown": 0,
        "warning": 1
      },
      "status": "ok",
      "unhandled_problem_services": 0
    },
    "knowledge_mcp": {
      "claim_count": 4584,
      "concept_count": 868,
      "container_revision": "67b338757efe9b496c4e154fbb0212563b1b96e8",
      "health_status": "ok",
      "observation_count_before_ingest": 2,
      "read_only": true,
      "run_id": "local-20260621180213",
      "runtime_head": "67b338757efe9b496c4e154fbb0212563b1b96e8",
      "service_state": "active",
      "status": "ok",
      "tool_count": 14,
      "transport": "streamable-http"
    },
    "noc_agent": {
      "bot_service_state": "active",
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
      "down_series": 0,
      "loop_node_up": true,
      "query_status": "success",
      "ready_http_status": 200,
      "service_state": "active",
      "status": "ok",
      "up_series": 55,
      "vault_internal_success": true,
      "vector_up": true
    }
  }
}
```
