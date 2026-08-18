# APPROVED_SOURCES.md

## Approved

| Source | Decision | Pin / method |
|---|---|---|
| Anthropic Skill Creator patterns | Approved | Reference patterns; internal skills |
| Anthropic MCP Builder | Approved | Reference only |
| Internal Command Tower skills/agents/commands | Approved | In-repo |

## Approved with restrictions

| Source | Restrictions |
|---|---|
| anthropics/skills | Review scripts; respect mixed licenses; don’t redistribute non-OSS docs skills |
| Claude plugin marketplace | Audit MCP/hooks per plugin; prefer Anthropic-maintained |
| Anthropic frontend-design / webapp-testing | Reimplemented internally; brand overrides apply |

## Wrapped / reimplemented internally

| Upstream | Internal capability |
|---|---|
| Anthropic frontend-design | `.claude/skills/frontend-design` |
| Anthropic webapp-testing | `.claude/skills/webapp-testing` |
| UI pack principles (selective) | Design department skills |

## Not auto-installed

Marketplace plugins and MCP servers require operator action after reading `PLUGIN_INSTALLATION.md` / `MCP_SETUP.md`.
