# CLAUDE.md — Command Tower Company Operating System

This repository is the **Command Tower Claude Company Operating System** for the BWA ecosystem: a professional, department-organized Claude Code environment with skills, subagents, commands, registries, validation, and governance.

## Operating rules

1. Treat `PROJECT_TRUTH.md` as the only verified current-state document. Do not invent progress.
2. Treat `registries/CAPABILITY_REGISTRY.yaml` as the machine-readable inventory of capabilities.
3. Prefer existing registered capabilities over inventing parallel workflows.
4. Route cross-department work through the executive orchestration model in `COMPANY_OS.md`.
5. Follow `SECURITY_POLICY.md` at all times. Never commit secrets, disable security controls, or use permission-bypass modes.
6. Distinguish clearly between: proposed, implemented, structure-validated, runtime-tested, fully-verified, credential-blocked, deferred, rejected.
7. Do not claim credential-dependent integrations work without tested credentials.
8. Do not present legal or financial capabilities as substitutes for licensed professionals.
9. Prefer least-privilege tools for subagents.
10. Before major commits, run: `python scripts/validate/validate_company_os.py`

## Project layout (canonical)

- `.claude/skills/` — project skills (`SKILL.md`)
- `.claude/agents/` — subagents
- `.claude/commands/` — user commands
- `.claude/settings.json` — project Claude Code settings (no destructive hooks enabled)
- `company/` — department overviews
- `registries/` — capability and source registries
- `docs/` — audits, installation, architecture, testing, security, source-of-truth
- `scripts/` — audit, install, validate, test utilities
- `tests/` — structural fixtures and evaluation cases

## Default branch protection

- Do not work directly on `main`.
- Do not merge pull requests unless a human explicitly requests it outside this agent assignment.
- Prefer dedicated branches such as `agent/claude-company-os-complete`.

## Validation

Primary suite:

```bash
python scripts/validate/validate_company_os.py
```

Static validation success is not runtime Claude discovery success. Report both honestly.

## Credentials

Credential-dependent items (for example Context7) are documented in `docs/installation/MCP_SETUP.md` and marked deferred/credential-blocked until configured locally by the operator. Never place real keys in the repository.
