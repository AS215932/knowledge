---
type: Observation
title: Engineering Loop / Knowledge MCP rollout live evidence 2026-06-21
description: Sanitized point-in-time evidence for the loop VM Engineering Loop and Knowledge MCP rollout.
tags:
- engineering-loop
- knowledge-mcp
- observed
- rollout
- safe-health
truth_owner: observed
authority: evidence
source_refs:
- url: manual://loop/engineering-loop-knowledge-mcp-rollout/2026-06-21
last_verified_at: '2026-06-21T16:10:28Z'
confidence: medium
dispute_policy: evidence_only
observed_at: '2026-06-21T16:10:28Z'
expires_at: '2026-06-22T16:10:28Z'
collection_profile: rollout-safe-health
observation_source: manual-local
observation_status: ok
payload_json: '{"observed_at":"2026-06-21T16:10:28Z","profile":"rollout-safe-health","sources":{"engineering_loop":{"runtime_head":"d4781edbef0cab9ca983f622b4aa2a960df16a97","status":"ok","timer_state":"active","vault_agent_state":"active"},"icinga":{"check":"loop!engineering-loop","output":"loop idle (approved queue is empty)","state":0,"status":"ok"},"knowledge_mcp":{"claim_count":4562,"concept_count":865,"read_only":true,"status":"ok","tool_count":14,"transport":"streamable-http"}}}'
---

# Engineering Loop / Knowledge MCP rollout live evidence

This file is sanitized observed evidence only. It does not define intended state and must lose to source repositories when facts conflict.

# Sanitized observations

| Check | Observed result |
| --- | --- |
| `loop` Engineering Loop runtime revision | `d4781edbef0cab9ca983f622b4aa2a960df16a97` |
| `vault-agent-engineering-loop.service` | `active` |
| `hyrule-engineering-loop.timer` | `active` |
| `hyrule-knowledge-mcp.service` | `active` |
| Docker daemon on `loop` | `active` |
| Knowledge MCP `/health` | `status=ok`, `transport=streamable-http`, `read_only=true`, `tool_count=14`, `concept_count=865`, `claim_count=4562` |
| Engineering Loop passive Icinga service | `loop!engineering-loop state=0`, output `loop idle (approved queue is empty)` |
| Canary issue/PR | `AS215932/engineering-loop#19` closed after draft PR `#21` merged |

# Sanitized payload

```json
{
  "observed_at": "2026-06-21T16:10:28Z",
  "profile": "rollout-safe-health",
  "sources": {
    "engineering_loop": {
      "runtime_head": "d4781edbef0cab9ca983f622b4aa2a960df16a97",
      "status": "ok",
      "timer_state": "active",
      "vault_agent_state": "active"
    },
    "icinga": {
      "check": "loop!engineering-loop",
      "output": "loop idle (approved queue is empty)",
      "state": 0,
      "status": "ok"
    },
    "knowledge_mcp": {
      "claim_count": 4562,
      "concept_count": 865,
      "read_only": true,
      "status": "ok",
      "tool_count": 14,
      "transport": "streamable-http"
    }
  }
}
```
