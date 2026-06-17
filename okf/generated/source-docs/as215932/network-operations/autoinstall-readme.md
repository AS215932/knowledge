---
type: Source Document
title: Autoinstall Configurations
description: Templates and tools for automated VM provisioning on XCP-NG.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/autoinstall/README.md
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: autoinstall/README.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-91
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/autoinstall/README.md#L1-L91
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: autoinstall/README.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `autoinstall/README.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `91` |

# Detected headings

* `# Autoinstall Configurations`
* `## OpenBSD (cloud-init template)`
* `## OpenBSD autoinstall fallback`
* `# On dom0: start DHCP + HTTP for autoinstall`
* `# Boot VM from ISO, type 'a' at prompt, select mgmt NIC, confirm URL`
* `## Debian (cloud-init)`
* `## QMP Tools`

# Deterministic excerpt

```markdown
# Autoinstall Configurations

Templates and tools for automated VM provisioning on XCP-NG.

## OpenBSD (cloud-init template)

OpenBSD is supported by cloud-init, and the preferred provisioning path for
service VMs is an XO template with cloud-init preinstalled. Build the template
once:

```sh
doas pkg_add -u
doas pkg_add cloud-init
doas rcctl enable cloudinit_local
doas rcctl enable cloudinit
```

Set the datasource order in `/etc/cloud/cloud.cfg.d/99_datasource.cfg`:

```yaml
datasource_list: [ ConfigDrive, NoCloud, OpenStack, None ]
```

Then clean the template before converting it in XO:

```sh
doas cloud-init clean --logs --seed
doas rm -f /etc/ssh/ssh_host_*
```

Templates:

- `openbsd-cloud-init.yaml.j2` — user-data for OpenBSD service VMs. It writes
  native `/etc/hostname.xnf*` files, installs `python3`, configures `doas`,
  and restarts networking/SSH.
- `openbsd-meta-data.j2` — instance metadata for ConfigDrive/NoCloud.

OpenBSD NICs on XCP-NG should use the Xen PV driver names `xnf0`, `xnf1`,
`xnf2` (not emulated-device names and not MAC-address hostname files). For
`mail`, attach the infra VIF first as `xnf0`; attach the OVH failover IPv4 VIF
second as `xnf1`. Use the router resolver `2a0c:b641:b50:2::1` for
`dns_server`; `dns`/`ns1` is authoritative and is not a general recursor.

## OpenBSD autoinstall fallback

`openbsd-fw.conf` — autoinstall response file. Serve via HTTP on the mgmt bridge:
`openbsd-mail.conf` is the equivalent response file for the `mail` VM on
xenbr-infra with static IPv6 `2a0c:b641:b50:2::90`. Use this path to build the
first cloud-init template or when ConfigDrive provisioning is unavailable.

```bash
# On dom0: start DHCP + HTTP for autoinstall
dhcpd -cf /etc/dhcp/dhcpd.conf xapi0
cd /path/to/autoinstall && python3 -m http.server 80
...
```

# Citations

[1] [autoinstall/README.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/autoinstall/README.md)
