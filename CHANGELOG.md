# CHANGELOG.md

## Unreleased — Company OS foundation (branch `agent/claude-company-os-complete`)

### Added

- Canonical governance: `CLAUDE.md`, `COMPANY_OS.md`, `PROJECT_TRUTH.md`, `STATUS.md`, `ROADMAP.md`, `HANDOFF.md`, `SECURITY_POLICY.md`
- `.claude/skills/`, `.claude/agents/`, `.claude/commands/`, `.claude/settings.json`
- Department overviews under `company/`
- Machine-readable `registries/CAPABILITY_REGISTRY.yaml` and human registries
- Source registry and deferred/rejected source report
- Audits: environment + security
- Installation docs and bootstrap/uninstall scripts
- Validation suite `scripts/validate/validate_company_os.py`
- Trigger fixtures under `tests/`
- Capability generator `scripts/install/generate_company_os.py`

### Security

- No hooks enabled by default
- Deferred high-risk externals
- Secrets/unsafe-pattern scanning in validator

### Notes

- Original 100+/128 inventory not present in git history; reconstructed per recovery doc
- External plugins/MCP not auto-installed
