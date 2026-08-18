# ROADMAP.md

## Incomplete / next

1. Operator opt-in install of Anthropic marketplace plugins after review
2. Configure Context7 MCP when API key available; run connectivity test
3. Optional CI workflow running `validate_company_os.py` on PRs
4. Interactive Claude Code runtime discovery tests for a sample of skills/commands
5. Tighten `.claude/settings.json` permissions per team preference
6. Consider curated extracts from deferred design packs (without violating licenses)
7. Security review of claude-mem before any enablement
8. Pin exact upstream commits when any external plugin is installed

## Deferred

- obra/superpowers (hooks policy)
- thedotmack/claude-mem (privacy/security)
- Context7 MCP (credentials)
- ui-ux-pro-max, taste-skill, transitions.dev (overlap/license/process)
- Enabled git hooks (prefer explicit validation command)

## Out of scope / rejected for inflation

- Empty placeholder skills
- Alias-only duplicates
- Credential theater marked as operational

## Future expansion

- Department-specific scorecards
- Multi-repo Company OS federation for BWA ecosystem
- Automated registry drift checks in CI
