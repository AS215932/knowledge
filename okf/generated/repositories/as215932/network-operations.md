---
type: Repository
title: AS215932 Network Operations
description: Network operations and infrastructure tracking for AS215932 (Hyrule).
  Building a complete ISP from scratch - BGP/OSPFv3 routing, IXP peering, automation.
  Working in public.
resource: https://github.com/AS215932/network-operations
tags:
- ansible
- as215932
- autonomous-system
- bgp
- devops
- frrouting
- infrastructure
- infrastructure-as-code
- ipv6
- irr
- isp
- ixp
- jinja2
- looking-glass
- network-automation
- network-operations
- ospf
- ospf-v3
- peering
- repository
- ripe
- rpki
- wireguard
- xcp-ng
timestamp: '2026-06-17T08:13:24Z'
truth_owner: external
authority: evidence
source_refs:
- repo: AS215932/network-operations
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: evidence_only
repo: AS215932/network-operations
default_branch: main
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Repository

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Default branch | `main` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Visibility | `public` |
| Primary language | `Python` |
| Topics | ansible, autonomous-system, bgp, devops, frrouting, infrastructure-as-code, ipv6, irr, isp, ixp, jinja2, looking-glass, network-automation, ospf, ospf-v3, peering, ripe, rpki, wireguard, xcp-ng |
| GitHub URL | https://github.com/AS215932/network-operations |

# Description

Network operations and infrastructure tracking for AS215932 (Hyrule). Building a complete ISP from scratch - BGP/OSPFv3 routing, IXP peering, automation. Working in public.

# Indexed source material

* [.github/workflows/app-promotion-deploy.yml](/generated/workflows/network-operations/github-workflows-app-promotion-deploy-yml.md)
* [.github/workflows/apply.yml](/generated/workflows/network-operations/github-workflows-apply-yml.md)
* [.github/workflows/drift-detection.yml](/generated/workflows/network-operations/github-workflows-drift-detection-yml.md)
* [.github/workflows/iac-tests.yml](/generated/workflows/network-operations/github-workflows-iac-tests-yml.md)
* [.github/workflows/lint.yml](/generated/workflows/network-operations/github-workflows-lint-yml.md)
* [.github/workflows/netops-nightly.yml](/generated/workflows/network-operations/github-workflows-netops-nightly-yml.md)
* [.github/workflows/pr-agent.yml](/generated/workflows/network-operations/github-workflows-pr-agent-yml.md)
* [.github/workflows/promote-apps.yml](/generated/workflows/network-operations/github-workflows-promote-apps-yml.md)
* [.github/workflows/render-check.yml](/generated/workflows/network-operations/github-workflows-render-check-yml.md)
* [.github/workflows/semgrep.yml](/generated/workflows/network-operations/github-workflows-semgrep-yml.md)
* [AGENTS.md](/generated/source-docs/as215932/network-operations/agents.md)
* [CHANGELOG.md](/generated/source-docs/as215932/network-operations/changelog.md)
* [CLAUDE.md](/generated/source-docs/as215932/network-operations/claude.md)
* [CONTRIBUTING.md](/generated/source-docs/as215932/network-operations/contributing.md)
* [README.md](/generated/source-docs/as215932/network-operations/readme.md)
* [ansible/inventory/group_vars/all.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-group-vars-all-yml.md)
* [ansible/inventory/group_vars/freebsd.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-group-vars-freebsd-yml.md)
* [ansible/inventory/group_vars/infra_vms.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-group-vars-infra-vms-yml.md)
* [ansible/inventory/group_vars/linux.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-group-vars-linux-yml.md)
* [ansible/inventory/group_vars/nameservers.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-group-vars-nameservers-yml.md)
* [ansible/inventory/group_vars/openbsd.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-group-vars-openbsd-yml.md)
* [ansible/inventory/group_vars/public_facing.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-group-vars-public-facing-yml.md)
* [ansible/inventory/group_vars/routers.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-group-vars-routers-yml.md)
* [ansible/inventory/host_vars/api.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-host-vars-api-yml.md)
* [ansible/inventory/host_vars/ci-pr.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-host-vars-ci-pr-yml.md)
* [ansible/inventory/host_vars/ci.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-host-vars-ci-yml.md)
* [ansible/inventory/host_vars/cr1-ch1.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-host-vars-cr1-ch1-yml.md)
* [ansible/inventory/host_vars/cr1-de1.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-host-vars-cr1-de1-yml.md)
* [ansible/inventory/host_vars/cr1-nl1.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-host-vars-cr1-nl1-yml.md)
* [ansible/inventory/host_vars/dns.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-host-vars-dns-yml.md)
* [ansible/inventory/host_vars/dom0.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-host-vars-dom0-yml.md)
* [ansible/inventory/host_vars/extmon.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-host-vars-extmon-yml.md)
* [ansible/inventory/host_vars/irc.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-host-vars-irc-yml.md)
* [ansible/inventory/host_vars/log.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-host-vars-log-yml.md)
* [ansible/inventory/host_vars/loop.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-host-vars-loop-yml.md)
* [ansible/inventory/host_vars/mail.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-host-vars-mail-yml.md)
* [ansible/inventory/host_vars/mon.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-host-vars-mon-yml.md)
* [ansible/inventory/host_vars/netproxy.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-host-vars-netproxy-yml.md)
* [ansible/inventory/host_vars/noc.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-host-vars-noc-yml.md)
* [ansible/inventory/host_vars/ns2.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-host-vars-ns2-yml.md)
* [ansible/inventory/host_vars/proxy.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-host-vars-proxy-yml.md)
* [ansible/inventory/host_vars/rtr.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-host-vars-rtr-yml.md)
* [ansible/inventory/host_vars/vault.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-host-vars-vault-yml.md)
* [ansible/inventory/host_vars/vpn.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-host-vars-vpn-yml.md)
* [ansible/inventory/host_vars/web.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-host-vars-web-yml.md)
* [ansible/inventory/host_vars/xoa.yml](/generated/source-docs/as215932/network-operations/ansible-inventory-host-vars-xoa-yml.md)
* [ansible/roles/frr/README.md](/generated/source-docs/as215932/network-operations/ansible-roles-frr-readme.md)
* [autoinstall/README.md](/generated/source-docs/as215932/network-operations/autoinstall-readme.md)
* [configs/rtr/jool/nat64-vrf-leak.service](/generated/source-docs/as215932/network-operations/configs-rtr-jool-nat64-vrf-leak-service.md)
* [configs/web/nginx/README.md](/generated/source-docs/as215932/network-operations/configs-web-nginx-readme.md)
* [docs/agent-loops/acceptance-gates.md](/generated/source-docs/as215932/network-operations/docs-agent-loops-acceptance-gates.md)
* [docs/agent-loops/change-orchestrator.md](/generated/source-docs/as215932/network-operations/docs-agent-loops-change-orchestrator.md)
* [docs/agent-loops/finops-billing-integrity-engineer.md](/generated/source-docs/as215932/network-operations/docs-agent-loops-finops-billing-integrity-engineer.md)
* [docs/agent-loops/implementation-writer.md](/generated/source-docs/as215932/network-operations/docs-agent-loops-implementation-writer.md)
* [docs/agent-loops/repo-map.md](/generated/source-docs/as215932/network-operations/docs-agent-loops-repo-map.md)
* [docs/agent-loops/senior-devops-netops-engineer.md](/generated/source-docs/as215932/network-operations/docs-agent-loops-senior-devops-netops-engineer.md)
* [docs/agent-loops/senior-network-architect.md](/generated/source-docs/as215932/network-operations/docs-agent-loops-senior-network-architect.md)
* [docs/agent-loops/senior-security-cryptographic-auditor.md](/generated/source-docs/as215932/network-operations/docs-agent-loops-senior-security-cryptographic-auditor.md)
* [docs/agent-loops/senior-systems-engineer.md](/generated/source-docs/as215932/network-operations/docs-agent-loops-senior-systems-engineer.md)
* [docs/agent-loops/virtual-lab-chaos-simulation-engineer.md](/generated/source-docs/as215932/network-operations/docs-agent-loops-virtual-lab-chaos-simulation-engineer.md)
* [docs/ci/branch-protection.md](/generated/source-docs/as215932/network-operations/docs-ci-branch-protection.md)
* [docs/ci/deploy-runbook.md](/generated/source-docs/as215932/network-operations/docs-ci-deploy-runbook.md)
* [docs/ci/org-cicd-inventory.md](/generated/source-docs/as215932/network-operations/docs-ci-org-cicd-inventory.md)
* [docs/ci/pr-agent.md](/generated/source-docs/as215932/network-operations/docs-ci-pr-agent.md)
* [docs/ci/provision-ci-pr.md](/generated/source-docs/as215932/network-operations/docs-ci-provision-ci-pr.md)
* [docs/ci/provision.md](/generated/source-docs/as215932/network-operations/docs-ci-provision.md)
* [docs/ci/security-model.md](/generated/source-docs/as215932/network-operations/docs-ci-security-model.md)
* [docs/ci/semgrep.md](/generated/source-docs/as215932/network-operations/docs-ci-semgrep.md)
* [docs/ci/workflows.md](/generated/source-docs/as215932/network-operations/docs-ci-workflows.md)
* [docs/engineering-loop/templates/pr-contract.md](/generated/source-docs/as215932/network-operations/docs-engineering-loop-templates-pr-contract.md)
* [docs/engineering-loop/templates/task-spec.md](/generated/source-docs/as215932/network-operations/docs-engineering-loop-templates-task-spec.md)
* [docs/engineering-loop/v2-architecture.md](/generated/source-docs/as215932/network-operations/docs-engineering-loop-v2-architecture.md)
* [docs/engineering-loop/v2-roadmap.md](/generated/source-docs/as215932/network-operations/docs-engineering-loop-v2-roadmap.md)
* [docs/netops/testing-strategy.md](/generated/source-docs/as215932/network-operations/docs-netops-testing-strategy.md)
* [docs/runbooks/bootstrap-engineering-loop-vault.md](/generated/source-docs/as215932/network-operations/docs-runbooks-bootstrap-engineering-loop-vault.md)
* [docs/runbooks/bootstrap-hyrule-cloud-vault.md](/generated/source-docs/as215932/network-operations/docs-runbooks-bootstrap-hyrule-cloud-vault.md)
* [docs/runbooks/bootstrap-runner-vault.md](/generated/source-docs/as215932/network-operations/docs-runbooks-bootstrap-runner-vault.md)
* [docs/runbooks/rotate-icinga-api-user.md](/generated/source-docs/as215932/network-operations/docs-runbooks-rotate-icinga-api-user.md)
* [docs/runbooks/vps-launch-proof-smoke.md](/generated/source-docs/as215932/network-operations/docs-runbooks-vps-launch-proof-smoke.md)
* [integrations/pi/extensions/hyrule-loop/README.md](/generated/source-docs/as215932/network-operations/integrations-pi-extensions-hyrule-loop-readme.md)
* ... 11 additional indexed files omitted from this glance list.

# Citations

[1] [AS215932/network-operations](https://github.com/AS215932/network-operations)
