# MCP_SETUP.md

## Context7 (deferred / credential-blocked)

| Field | Value |
|---|---|
| Purpose | Up-to-date public library documentation |
| Credential | `CONTEXT7_API_KEY` |
| Config location | User-level Claude MCP config (not committed) |
| Status | Credential-blocked in this repository |

### Setup procedure (operator)

1. Obtain an API key from Context7/Upstash per their docs.
2. Store in local environment or user secrets — **not** in git.
3. Add MCP server config in user Claude settings pointing at the official Context7 server package/endpoint.
4. Restrict to public library docs; do not send private/internal documentation unless policy allows.

### Verification command

In Claude Code, run a docs query for a public library (for example React). Success = retrieved docs. Failure = leave status credential-blocked.

### Repository stance

No MCP secrets are stored in this repo. `.env.example` lists the variable name only.
