# Testing Guide

## Classes of tests (do not conflate)

| Class | What it proves | Location |
|---|---|---|
| Static / structural | Files, frontmatter, registry consistency, secret patterns | `scripts/validate/validate_company_os.py` |
| Trigger fixtures | Positive/negative examples exist and don’t overlap | `tests/**/fixtures.json` |
| Runtime Claude tests | Discovery/triggering inside Claude Code | Manual / interactive (not auto in CI yet) |
| Credential-blocked | MCP/plugin connectivity | Skipped without secrets |
| Integration scenarios | Cross-department workflows (documented fixtures) | `tests/integration/` |

## Running

```bash
python scripts/validate/validate_company_os.py
```

## Honesty rule

Never mark a test successful unless executed and passed. Static PASS ≠ runtime PASS.
