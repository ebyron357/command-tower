# PLUGIN_INSTALLATION.md

## Policy

1. Read `registries/SOURCE_REGISTRY.md`.
2. Only install **Approved** or **Approved with restrictions** after understanding restrictions.
3. Never install deferred/rejected sources to inflate counts.
4. Pin versions/commits when practical.
5. Record the install in `CHANGELOG.md` and update registry status.

## Suggested official path (operator)

Inside Claude Code (examples — verify against current Claude Code docs):

```text
/plugin marketplace add anthropics/skills
```

Then install only specific reviewed plugins — not entire marketplaces blindly.

## Superpowers / claude-mem

Deferred. Do not install from bootstrap.

## Verification

- Plugin loads without error
- Hooks listed and acceptable
- MCP declarations reviewed
- Update `PLUGIN_REGISTRY.md` status fields
