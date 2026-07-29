# Quality Security Department

Capabilities owned by this department:

- `skill.security-review-skill` (skill) — Review changes for security defects and misuse cases.
- `skill.qa-review` (skill) — QA review for defects, coverage gaps, and release risk.
- `skill.red-team-review` (skill) — Adversarial review of plans/systems for abuse paths.
- `skill.release-readiness` (skill) — Assess release readiness across quality, security, ops.
- `skill.permission-audits` (skill) — Audit permissions for least privilege and drift.
- `skill.secrets-detection` (skill) — Detect credential-like strings and secret handling risks.
- `skill.supply-chain-review` (skill) — Review supply chain: deps, scripts, provenance.
- `skill.governance-enforcement` (skill) — Check governance docs/registries match implementation.
- `skill.completion-verification` (skill) — Verify completion claims with evidence gates.
- `agent.qa-lead` (subagent) — Lead QA strategy, test planning, and release quality gates.
- `agent.security-reviewer` (subagent) — Independent security review with severity ordering.
- `agent.completion-auditor` (subagent) — Audit completion claims against registries, tests, and docs.
- `cmd.security-review` (command) — Run security review workflow.
- `cmd.release-readiness` (command) — Assess release readiness with evidence.
- `cmd.capability-audit` (command) — Audit capability registry vs filesystem and statuses.
- `cmd.capability-search` (command) — Search capabilities by department, type, trigger, or status.
- `validation.validate-company-os` (validation) — Primary structural/security validation suite for Company OS.
- `validation.security-scan` (validation) — Scan for credential-like strings and unsafe shell patterns.
- `validation.registry-consistency` (validation) — Ensure registry entries match filesystem artifacts.
- `validation.trigger-fixture-runner` (validation) — Evaluate positive/negative trigger fixtures for skills/agents/commands.
- `hook.pre-commit-secrets-hint` (hook) — Optional documentation for secrets detection before commit.
- `hook.post-validate-registry` (hook) — Optional post-edit registry consistency check (disabled by default).
- `reference.testing-guide` (reference) — How structural vs runtime vs fixture tests are classified.
