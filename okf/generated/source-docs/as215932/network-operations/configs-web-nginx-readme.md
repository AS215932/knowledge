---
type: Source Document
title: nginx on the web VM
description: The `web` VM (`2a0c:b641:b50:2::30`) runs `hyrule-web` (uvicorn) on `[::]:8080`
  and nginx on `[::]:8081` for the static `as215932.net` info site. Caddy on the `proxy`
  VM reverse-proxies both.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/web/nginx/README.md
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: configs/web/nginx/README.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-39
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/web/nginx/README.md#L1-L39
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: configs/web/nginx/README.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `configs/web/nginx/README.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `39` |

# Detected headings

* `# nginx on the web VM`
* `## Install`
* `## Deploy `as215932.net``

# Deterministic excerpt

```markdown
# nginx on the web VM

The `web` VM (`2a0c:b641:b50:2::30`) runs `hyrule-web` (uvicorn) on
`[::]:8080` and nginx on `[::]:8081` for the static `as215932.net`
info site. Caddy on the `proxy` VM reverse-proxies both.

## Install

```
apt install nginx-light
```

## Deploy `as215932.net`

1. Copy the site content:

   ```
   rsync -av configs/as215932-net/html/ \
       root@[2a0c:b641:b50:2::30]:/var/www/as215932.net/
   ```

2. Drop the server block and enable it:

   ```
   scp configs/web/nginx/as215932.net.conf \
       root@[2a0c:b641:b50:2::30]:/etc/nginx/sites-available/as215932.net.conf
   ssh root@[2a0c:b641:b50:2::30] \
       'ln -sf /etc/nginx/sites-available/as215932.net.conf \
               /etc/nginx/sites-enabled/as215932.net.conf \
        && nginx -t && systemctl reload nginx'
   ```

3. Smoke-test from `proxy` (infra network):

   ```
   curl -6 -H "Host: as215932.net" http://[2a0c:b641:b50:2::30]:8081/ | head
   curl -6 -sI -H "Host: as215932.net" \
       http://[2a0c:b641:b50:2::30]:8081/peering
   ```
```

# Citations

[1] [configs/web/nginx/README.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/configs/web/nginx/README.md)
