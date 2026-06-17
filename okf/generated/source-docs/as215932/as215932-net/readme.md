---
type: Source Document
title: as215932.net
description: Informational website for AS215932 (Hyrule Networks). ASN facts, peering
  policy, network weathermap, prefix allocations, and a stub for the upcoming Looking
  Glass.
resource: https://github.com/AS215932/as215932.net/blob/9c0ee2d8f2bb793ea799589ca0fe4f77571b2572/README.md
tags:
- as215932
- as215932.net
- source-document
timestamp: '2026-06-13T17:48:17Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/as215932.net
  path: README.md
  commit: 9c0ee2d8f2bb793ea799589ca0fe4f77571b2572
  lines: 1-54
  url: https://github.com/AS215932/as215932.net/blob/9c0ee2d8f2bb793ea799589ca0fe4f77571b2572/README.md#L1-L54
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/as215932.net
source_path: README.md
commit: 9c0ee2d8f2bb793ea799589ca0fe4f77571b2572
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/as215932.net` |
| Path | `README.md` |
| Commit | `9c0ee2d8f2bb793ea799589ca0fe4f77571b2572` |
| Lines | `54` |

# Detected headings

* `# as215932.net`
* `## Layout`
* `## Deploy`
* `## Editing`
* `## License`

# Deterministic excerpt

```markdown
# as215932.net

Informational website for [AS215932](https://www.peeringdb.com/asn/215932)
(Hyrule Networks). ASN facts, peering policy, network weathermap, prefix
allocations, and a stub for the upcoming Looking Glass.

Deliberately primitive: plain static HTML, one CSS file, no JavaScript,
no webfonts, no remote assets. Renders under Tor Browser "Safest" mode.
Soft 80-column target for the hacker/builder aesthetic.

## Layout

| file | purpose |
|------|---------|
| `index.html`    | Home — ASN facts + weathermap |
| `network.html`  | Full topology and routing stack |
| `peering.html`  | Peering policy, requirements, NOC contact |
| `prefixes.html` | IPv6 allocation, RPKI/IRR, external records |
| `lg.html`       | Looking Glass stub — real LG coming later |
| `style.css`     | Black background, white text, monospace, ~80ch |

## Deploy

The site is served by `nginx` on the `web` VM
(`2a0c:b641:b50:2::30`) on port `8081`, fronted by Caddy on the `proxy`
VM which terminates TLS for `as215932.net`. All nginx / Caddy / Knot /
Icinga configuration lives in the
[hyrule-infra](https://github.com/AS215932/network-operations)
repository — this repo only contains the site content.

```sh
./deploy.sh            # rsync + reload nginx on the web VM
```

`deploy.sh` is a thin wrapper around `rsync` — it touches only
`/var/www/as215932.net/` and reloads nginx. No other state is changed.

## Editing

Since pages share a nav / header / footer, changes to the menu must be
applied to all five HTML files. There is no template engine — that's
intentional, to keep the site buildable with nothing but a text editor.

When adding content, keep rendered lines at or under 80 columns where
possible (CSS wraps longer lines, but breaking manually keeps the
aesthetic).

## License

Same as the re
...
```

# Citations

[1] [README.md](https://github.com/AS215932/as215932.net/blob/9c0ee2d8f2bb793ea799589ca0fe4f77571b2572/README.md)
