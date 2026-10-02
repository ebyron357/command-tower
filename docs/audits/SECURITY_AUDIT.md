# SECURITY_AUDIT.md

## Audit metadata

| Field | Value |
|---|---|
| Date | 2026-07-29 |
| Scope | Repository contents, scripts, settings, external source decisions |
| Method | Manual inspection + `scripts/validate/validate_company_os.py` secret/unsafe-pattern scan |

## Findings

| ID | Finding | Severity | Evidence | Disposition |
|---|---|---|---|---|
| SEC-001 | No secrets in initial README-only tree | Info | Pre-build file listing | OK |
| SEC-002 | Risk of future secret commits | Medium | No pre-commit hook historically | Mitigated by validation scanner + SECURITY_POLICY; hooks remain disabled by choice |
| SEC-003 | External plugin install scripts not executed | Info | Policy: review before install | Deferred plugins not installed |
| SEC-004 | claude-mem capture surface | High (if installed) | Source review | Deferred; not installed |
| SEC-005 | Context7 data egress | Medium (if configured) | Requires API key | Credential-blocked; docs only |
| SEC-006 | Community UI skill packs unpinned if blindly installed | Medium | Source review | Deferred; internal skills used instead |
| SEC-007 | No destructive hooks enabled | Info | `.claude/settings.json` hooks `{}` | OK |
| SEC-008 | Finance/legal misuse risk | Medium | Advisory skills could be over-trusted | Disclaimers in skills + policy |
| SEC-009 | Generator/validation scripts are local Python | Low | `scripts/**` | Reviewed; no curl\|sh |
| SEC-010 | Settings allow broad Write in project | Medium | Least-privilege vs usability tradeoff | Documented; agents still declare tighter tool lists |

## Embedded secrets check

Run:

```bash
python scripts/validate/validate_company_os.py
```

Expect: no credential-like matches in tracked files (excluding documented placeholders).

## Unsafe scripts

No `curl | sh` / `wget | sh` / `rm -rf /` patterns are permitted by validation.

## MCP / plugins

| Item | Status |
|---|---|
| Context7 | Deferred / credential-blocked |
| Superpowers | Deferred |
| claude-mem | Deferred (security) |
| Anthropic marketplaces | Approved with restrictions; not auto-installed |

## Remaining risks

1. Operator may install deferred plugins without reading SOURCE_REGISTRY.
2. Broad Write permission in project settings can be tightened further per team preference.
3. Runtime Claude behavior cannot be fully proven by static validation alone.

## Resolved in this build

- Established security policy
- Disabled hooks by default
- Deferred high-risk externals
- Added secrets/unsafe-pattern scanner
- Documented credential handling
