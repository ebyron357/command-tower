# TROUBLESHOOTING.md

## Validation fails

- Read the FAIL lines from `python scripts/validate/validate_company_os.py`
- Common causes: hand-edited registry drift, missing SKILL.md sections, duplicate names
- Regenerate only if intentional: `python scripts/install/generate_company_os.py`

## Skills not appearing in Claude Code

- Confirm files are under `.claude/skills/<name>/SKILL.md`
- Confirm YAML frontmatter `name` matches folder
- Restart Claude Code session
- Ensure you opened this repository as the project root

## Commands not found

- Confirm `.claude/commands/<name>.md` exists
- Invoke as `/name`

## False “fully verified” claims

- Static validation ≠ runtime tests
- Update STATUS honestly

## Secrets scanner false positives

- Avoid real-looking tokens in docs
- Use obvious placeholders like `YOUR_API_KEY_HERE`

## Uninstall leftover

- Run `python scripts/install/uninstall.py --dry-run` then without dry-run
- Does not modify user home Claude config
