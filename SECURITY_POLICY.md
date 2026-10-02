# SECURITY_POLICY.md

## Principles

1. No secrets in git, logs, reports, or fixtures.
2. Least privilege for agents and MCP servers.
3. Prefer internal reimplementation over unreviewed third-party installs.
4. Pin external sources when installed.
5. Prefer no hook over an unsafe hook.
6. Never disable security controls or use permission-bypass modes for convenience.
7. Do not execute unknown installation scripts without source review.

## Secrets

- Use `.env` locally only; never commit populated `.env`.
- `.env.example` may list variable names without values.
- Validation suite scans for credential-like patterns.
- If a secret is found: rotate, purge from history if committed, document incident.

## Permissions

- Subagents must declare allowed tools and prohibited actions.
- Do not grant blanket network or production deploy tools without need.
- Settings must not enable destructive hooks.

## Dependencies and supply chain

- Review package scripts, binaries, hooks, MCP declarations before install.
- Reject abandoned/suspicious packages used only to inflate capability counts.
- Record decisions in `registries/SOURCE_REGISTRY.md`.

## Plugins

- Source-review before install.
- Official Anthropic sources preferred.
- Community plugins: approved-with-restrictions or deferred.

## MCP

- Document required credentials.
- Mark credential-blocked when absent.
- Never embed tokens in repo files.
- Limit egress to required endpoints.

## Hooks

- Disabled by default in this repository.
- Any future hook must document lifecycle event, exact command, quoting, failure behavior, disable/uninstall steps, and tests.

## Legal / finance disclaimer

Skills in legal-compliance and finance are **not** licensed professional advice.

## Incident response (secrets)

1. Stop propagation.
2. Rotate credentials.
3. Remove from tree.
4. Assess git history exposure.
5. Record in CHANGELOG and security audit.
