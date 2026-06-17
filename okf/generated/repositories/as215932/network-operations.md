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
last_verified_at: '2026-06-17T10:33:31Z'
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

# Extracted inventory

| Asset | Count |
| --- | ---: |
| Indexed source files | 91 |
| API endpoints | 0 |
| API schemas | 2 |
| Workflows | 10 |
| Open issues | 51 |
| Open pull requests | 6 |
| Releases | 0 |

# Related concepts

* Top-level concept: [AS215932 Network Operations](../../projects/network-operations.md)

# Indexed source material

* [.github/workflows/app-promotion-deploy.yml](../../workflows/network-operations/github-workflows-app-promotion-deploy-yml.md)
* [.github/workflows/apply.yml](../../workflows/network-operations/github-workflows-apply-yml.md)
* [.github/workflows/drift-detection.yml](../../workflows/network-operations/github-workflows-drift-detection-yml.md)
* [.github/workflows/iac-tests.yml](../../workflows/network-operations/github-workflows-iac-tests-yml.md)
* [.github/workflows/lint.yml](../../workflows/network-operations/github-workflows-lint-yml.md)
* [.github/workflows/netops-nightly.yml](../../workflows/network-operations/github-workflows-netops-nightly-yml.md)
* [.github/workflows/pr-agent.yml](../../workflows/network-operations/github-workflows-pr-agent-yml.md)
* [.github/workflows/promote-apps.yml](../../workflows/network-operations/github-workflows-promote-apps-yml.md)
* [.github/workflows/render-check.yml](../../workflows/network-operations/github-workflows-render-check-yml.md)
* [.github/workflows/semgrep.yml](../../workflows/network-operations/github-workflows-semgrep-yml.md)
* [AGENTS.md](../../source-docs/as215932/network-operations/agents.md)
* [CHANGELOG.md](../../source-docs/as215932/network-operations/changelog.md)
* [CLAUDE.md](../../source-docs/as215932/network-operations/claude.md)
* [CONTRIBUTING.md](../../source-docs/as215932/network-operations/contributing.md)
* [README.md](../../source-docs/as215932/network-operations/readme.md)
* [ansible/inventory/group_vars/all.yml](../../source-docs/as215932/network-operations/ansible-inventory-group-vars-all-yml.md)
* [ansible/inventory/group_vars/freebsd.yml](../../source-docs/as215932/network-operations/ansible-inventory-group-vars-freebsd-yml.md)
* [ansible/inventory/group_vars/infra_vms.yml](../../source-docs/as215932/network-operations/ansible-inventory-group-vars-infra-vms-yml.md)
* [ansible/inventory/group_vars/linux.yml](../../source-docs/as215932/network-operations/ansible-inventory-group-vars-linux-yml.md)
* [ansible/inventory/group_vars/nameservers.yml](../../source-docs/as215932/network-operations/ansible-inventory-group-vars-nameservers-yml.md)
* [ansible/inventory/group_vars/openbsd.yml](../../source-docs/as215932/network-operations/ansible-inventory-group-vars-openbsd-yml.md)
* [ansible/inventory/group_vars/public_facing.yml](../../source-docs/as215932/network-operations/ansible-inventory-group-vars-public-facing-yml.md)
* [ansible/inventory/group_vars/routers.yml](../../source-docs/as215932/network-operations/ansible-inventory-group-vars-routers-yml.md)
* [ansible/inventory/host_vars/api.yml](../../source-docs/as215932/network-operations/ansible-inventory-host-vars-api-yml.md)
* [ansible/inventory/host_vars/ci-pr.yml](../../source-docs/as215932/network-operations/ansible-inventory-host-vars-ci-pr-yml.md)
* [ansible/inventory/host_vars/ci.yml](../../source-docs/as215932/network-operations/ansible-inventory-host-vars-ci-yml.md)
* [ansible/inventory/host_vars/cr1-ch1.yml](../../source-docs/as215932/network-operations/ansible-inventory-host-vars-cr1-ch1-yml.md)
* [ansible/inventory/host_vars/cr1-de1.yml](../../source-docs/as215932/network-operations/ansible-inventory-host-vars-cr1-de1-yml.md)
* [ansible/inventory/host_vars/cr1-nl1.yml](../../source-docs/as215932/network-operations/ansible-inventory-host-vars-cr1-nl1-yml.md)
* [ansible/inventory/host_vars/dns.yml](../../source-docs/as215932/network-operations/ansible-inventory-host-vars-dns-yml.md)
* [ansible/inventory/host_vars/dom0.yml](../../source-docs/as215932/network-operations/ansible-inventory-host-vars-dom0-yml.md)
* [ansible/inventory/host_vars/extmon.yml](../../source-docs/as215932/network-operations/ansible-inventory-host-vars-extmon-yml.md)
* [ansible/inventory/host_vars/irc.yml](../../source-docs/as215932/network-operations/ansible-inventory-host-vars-irc-yml.md)
* [ansible/inventory/host_vars/log.yml](../../source-docs/as215932/network-operations/ansible-inventory-host-vars-log-yml.md)
* [ansible/inventory/host_vars/loop.yml](../../source-docs/as215932/network-operations/ansible-inventory-host-vars-loop-yml.md)
* [ansible/inventory/host_vars/mail.yml](../../source-docs/as215932/network-operations/ansible-inventory-host-vars-mail-yml.md)
* [ansible/inventory/host_vars/mon.yml](../../source-docs/as215932/network-operations/ansible-inventory-host-vars-mon-yml.md)
* [ansible/inventory/host_vars/netproxy.yml](../../source-docs/as215932/network-operations/ansible-inventory-host-vars-netproxy-yml.md)
* [ansible/inventory/host_vars/noc.yml](../../source-docs/as215932/network-operations/ansible-inventory-host-vars-noc-yml.md)
* [ansible/inventory/host_vars/ns2.yml](../../source-docs/as215932/network-operations/ansible-inventory-host-vars-ns2-yml.md)
* [ansible/inventory/host_vars/proxy.yml](../../source-docs/as215932/network-operations/ansible-inventory-host-vars-proxy-yml.md)
* [ansible/inventory/host_vars/rtr.yml](../../source-docs/as215932/network-operations/ansible-inventory-host-vars-rtr-yml.md)
* [ansible/inventory/host_vars/vault.yml](../../source-docs/as215932/network-operations/ansible-inventory-host-vars-vault-yml.md)
* [ansible/inventory/host_vars/vpn.yml](../../source-docs/as215932/network-operations/ansible-inventory-host-vars-vpn-yml.md)
* [ansible/inventory/host_vars/web.yml](../../source-docs/as215932/network-operations/ansible-inventory-host-vars-web-yml.md)
* [ansible/inventory/host_vars/xoa.yml](../../source-docs/as215932/network-operations/ansible-inventory-host-vars-xoa-yml.md)
* [ansible/roles/frr/README.md](../../source-docs/as215932/network-operations/ansible-roles-frr-readme.md)
* [autoinstall/README.md](../../source-docs/as215932/network-operations/autoinstall-readme.md)
* [configs/rtr/jool/nat64-vrf-leak.service](../../source-docs/as215932/network-operations/configs-rtr-jool-nat64-vrf-leak-service.md)
* [configs/web/nginx/README.md](../../source-docs/as215932/network-operations/configs-web-nginx-readme.md)
* [docs/agent-loops/acceptance-gates.md](../../source-docs/as215932/network-operations/docs-agent-loops-acceptance-gates.md)
* [docs/agent-loops/change-orchestrator.md](../../source-docs/as215932/network-operations/docs-agent-loops-change-orchestrator.md)
* [docs/agent-loops/finops-billing-integrity-engineer.md](../../source-docs/as215932/network-operations/docs-agent-loops-finops-billing-integrity-engineer.md)
* [docs/agent-loops/implementation-writer.md](../../source-docs/as215932/network-operations/docs-agent-loops-implementation-writer.md)
* [docs/agent-loops/repo-map.md](../../source-docs/as215932/network-operations/docs-agent-loops-repo-map.md)
* [docs/agent-loops/senior-devops-netops-engineer.md](../../source-docs/as215932/network-operations/docs-agent-loops-senior-devops-netops-engineer.md)
* [docs/agent-loops/senior-network-architect.md](../../source-docs/as215932/network-operations/docs-agent-loops-senior-network-architect.md)
* [docs/agent-loops/senior-security-cryptographic-auditor.md](../../source-docs/as215932/network-operations/docs-agent-loops-senior-security-cryptographic-auditor.md)
* [docs/agent-loops/senior-systems-engineer.md](../../source-docs/as215932/network-operations/docs-agent-loops-senior-systems-engineer.md)
* [docs/agent-loops/virtual-lab-chaos-simulation-engineer.md](../../source-docs/as215932/network-operations/docs-agent-loops-virtual-lab-chaos-simulation-engineer.md)
* [docs/ci/branch-protection.md](../../source-docs/as215932/network-operations/docs-ci-branch-protection.md)
* [docs/ci/deploy-runbook.md](../../source-docs/as215932/network-operations/docs-ci-deploy-runbook.md)
* [docs/ci/org-cicd-inventory.md](../../source-docs/as215932/network-operations/docs-ci-org-cicd-inventory.md)
* [docs/ci/pr-agent.md](../../source-docs/as215932/network-operations/docs-ci-pr-agent.md)
* [docs/ci/provision-ci-pr.md](../../source-docs/as215932/network-operations/docs-ci-provision-ci-pr.md)
* [docs/ci/provision.md](../../source-docs/as215932/network-operations/docs-ci-provision.md)
* [docs/ci/security-model.md](../../source-docs/as215932/network-operations/docs-ci-security-model.md)
* [docs/ci/semgrep.md](../../source-docs/as215932/network-operations/docs-ci-semgrep.md)
* [docs/ci/workflows.md](../../source-docs/as215932/network-operations/docs-ci-workflows.md)
* [docs/engineering-loop/templates/pr-contract.md](../../source-docs/as215932/network-operations/docs-engineering-loop-templates-pr-contract.md)
* [docs/engineering-loop/templates/task-spec.md](../../source-docs/as215932/network-operations/docs-engineering-loop-templates-task-spec.md)
* [docs/engineering-loop/v2-architecture.md](../../source-docs/as215932/network-operations/docs-engineering-loop-v2-architecture.md)
* [docs/engineering-loop/v2-roadmap.md](../../source-docs/as215932/network-operations/docs-engineering-loop-v2-roadmap.md)
* [docs/netops/testing-strategy.md](../../source-docs/as215932/network-operations/docs-netops-testing-strategy.md)
* [docs/runbooks/bootstrap-engineering-loop-vault.md](../../source-docs/as215932/network-operations/docs-runbooks-bootstrap-engineering-loop-vault.md)
* [docs/runbooks/bootstrap-hyrule-cloud-vault.md](../../source-docs/as215932/network-operations/docs-runbooks-bootstrap-hyrule-cloud-vault.md)
* [docs/runbooks/bootstrap-runner-vault.md](../../source-docs/as215932/network-operations/docs-runbooks-bootstrap-runner-vault.md)
* [docs/runbooks/rotate-icinga-api-user.md](../../source-docs/as215932/network-operations/docs-runbooks-rotate-icinga-api-user.md)
* [docs/runbooks/vps-launch-proof-smoke.md](../../source-docs/as215932/network-operations/docs-runbooks-vps-launch-proof-smoke.md)
* [integrations/pi/extensions/hyrule-loop/README.md](../../source-docs/as215932/network-operations/integrations-pi-extensions-hyrule-loop-readme.md)
* [pyproject.toml](../../source-docs/as215932/network-operations/pyproject-toml.md)
* [skills/README.md](../../source-docs/as215932/network-operations/skills-readme.md)
* [skills/firewall-change/SKILL.md](../../source-docs/as215932/network-operations/skills-firewall-change-skill.md)
* [skills/implementation-tranche/SKILL.md](../../source-docs/as215932/network-operations/skills-implementation-tranche-skill.md)
* [skills/monitoring-onboarding/SKILL.md](../../source-docs/as215932/network-operations/skills-monitoring-onboarding-skill.md)
* [skills/role-devops-netops/SKILL.md](../../source-docs/as215932/network-operations/skills-role-devops-netops-skill.md)
* [skills/role-finops-integrity/SKILL.md](../../source-docs/as215932/network-operations/skills-role-finops-integrity-skill.md)
* [skills/role-network-architect/SKILL.md](../../source-docs/as215932/network-operations/skills-role-network-architect-skill.md)
* [skills/role-security-auditor/SKILL.md](../../source-docs/as215932/network-operations/skills-role-security-auditor-skill.md)
* [skills/role-systems-engineer/SKILL.md](../../source-docs/as215932/network-operations/skills-role-systems-engineer-skill.md)
* [skills/role-virtual-lab-chaos/SKILL.md](../../source-docs/as215932/network-operations/skills-role-virtual-lab-chaos-skill.md)

# Citations

[1] [AS215932/network-operations](https://github.com/AS215932/network-operations)
