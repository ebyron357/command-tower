# EXISTING_ENVIRONMENT_UPGRADE.md

## Goals

Upgrade an existing checkout to the Company OS layout without destroying unrelated user Claude configuration in the home directory.

## Steps

1. Commit or stash local work.
2. Fetch and checkout the Company OS branch (or merge once approved).
3. Diff governance documents carefully (`CLAUDE.md`, settings).
4. Run:

```bash
python scripts/install/bootstrap.py --upgrade
python scripts/validate/validate_company_os.py
```

5. Review `registries/` changes for new capabilities.
6. Re-apply any local MCP config only in user-level Claude settings — never commit secrets.

## Backup

Bootstrap creates `backups/claude-settings-*.json` if it would modify `.claude/settings.json`.
