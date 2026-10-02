# Deferred and Rejected Sources

## Deferred pending credentials

| Source | Reason | Unblock |
|---|---|---|
| Context7 MCP | Requires `CONTEXT7_API_KEY`; not present in repo | Configure locally per `docs/installation/MCP_SETUP.md`, test connectivity, update registry status |

## Deferred pending review / policy

| Source | Reason | Unblock |
|---|---|---|
| obra/superpowers | SessionStart hooks change agent behavior org-wide | Security + workflow review; opt-in only |
| thedotmack/claude-mem | Captures tool output; local worker attack/privacy surface | Formal security review; loopback-only; pin version |
| ui-ux-pro-max-skill | Large surface; brand conflict risk | Curate extracts into internal skills if needed |
| taste-skill | Aesthetic conflicts with brand/frontend-design | Team design director decision |
| transitions.dev | Custom no-redistribute constraints; Pro auth for tooling | Legal/license review for intended use |
| Enabled git hooks | Prefer explicit validation over silent hooks | Add only with quoted commands + tests |

## Rejected

None formally rejected on public evidence alone.

## Explicitly not installed by this repository bootstrap

All deferred items above. Bootstrap installs project files only.
