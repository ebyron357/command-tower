# FRESH_INSTALL.md

## Prerequisites

- Git
- Python 3.11+ (3.13 tested)
- Claude Code CLI (optional for runtime; required for interactive skill use)
- GitHub access if pushing

## Steps

1. Clone the repository and checkout the Company OS branch or merged main.
2. Read `SECURITY_POLICY.md` and `PROJECT_TRUTH.md`.
3. Run post-install validation:

```bash
python scripts/validate/validate_company_os.py
```

4. (Optional) Run bootstrap (copies nothing outside repo; verifies structure):

```bash
python scripts/install/bootstrap.py
```

5. Open the repo in Claude Code. Project skills/agents/commands load from `.claude/`.

6. Do **not** expect deferred MCP/plugins to work until configured.

## Skipped components

- External plugins
- MCP servers requiring credentials
- Git hooks

## Installation report

Bootstrap writes `docs/installation/LAST_INSTALL_REPORT.md` when run.
