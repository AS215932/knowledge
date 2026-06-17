# generated/workflows/network-operations

* [Advisory AI PR review (replaces hosted Sourcery). Runs on the UNPRIVILEGED](github-workflows-pr-agent-yml.md) - --- name: pr-agent
* [ci-pr lives on the customer-isolated segment and is managed from](github-workflows-drift-detection-yml.md) - --- name: drift-detection
* [Manual gated deployment. Run with:](github-workflows-apply-yml.md) - --- name: apply run-name: ${{ inputs.dry_run == true && 'Dry-run' || 'Apply' }} playbook ${{ inputs.playbook }} to target(s) ${{ inputs.limit }}
* [Nightly cadence for the heavy NetOps lab tiers (Wave 5, Stage 1: manual +](github-workflows-netops-nightly-yml.md) - --- name: netops-nightly
* [Ordering matters for NOC monitoring changes: install mon-side](github-workflows-app-promotion-deploy-yml.md) - --- name: app-promotion-deploy
* [promote-apps.yml](github-workflows-promote-apps-yml.md) - --- name: promote-apps
* [Renders every playbook in --tags validate --connection=local mode and](github-workflows-render-check-yml.md) - --- name: render-check
* [roles_path lives in ansible/ansible.cfg, which isn't picked up when lint](github-workflows-lint-yml.md) - --- name: lint
* [Tiered IaC test pipeline (Wave 5).](github-workflows-iac-tests-yml.md) - --- name: iac-tests
* [Token-less Semgrep SAST. Runs on the UNPRIVILEGED `hyrule-public-pr` runner,](github-workflows-semgrep-yml.md) - --- name: semgrep
