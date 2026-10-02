# HANDOFF.md

## Continue from here

Branch: `agent/claude-company-os-complete`

1. Read `PROJECT_TRUTH.md`, `STATUS.md`, `SECURITY_POLICY.md`.
2. Run `python scripts/validate/validate_company_os.py` and keep the working tree green.
3. Do not mark capabilities `fully-verified` without runtime evidence.
4. For MCP: follow `docs/installation/MCP_SETUP.md` only with local secrets.
5. For plugins: follow `docs/installation/PLUGIN_INSTALLATION.md` and update `SOURCE_REGISTRY.md`.
6. Prefer editing registries via generator + validation rather than hand-drifting YAML.
7. Regeneration: `python scripts/install/generate_company_os.py` (overwrites generated skill/agent/command bodies — review diffs).

## Open blockers for humans

- Decide whether to allow SessionStart hooks (Superpowers).
- Provide Context7 API key locally if MCP docs access is required.
- Approve/deny memory plugin after security review.
- Review draft PR and merge policy for `main`.

## Exact next action for owner

Review the draft pull request on GitHub, run the validation command locally, then decide merge readiness.
