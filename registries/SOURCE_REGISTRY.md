# SOURCE_REGISTRY.md

## Decision legend

Approved · Approved with restrictions · Wrapped internally · Reimplemented internally · Deferred pending credentials · Deferred pending review · Rejected · Superseded

## Sources

### anthropics/skills
- **URL:** https://github.com/anthropics/skills
- **Owner:** Anthropic
- **Purpose:** Official Agent Skills examples and patterns
- **Type:** External dependency / marketplace content
- **License:** Mixed (Apache-2.0 examples; document skills source-available)
- **Reviewed:** Public docs + repository structure (2026-07-29)
- **Maintenance:** Active
- **Install method:** Optional `/plugin marketplace add anthropics/skills` (operator)
- **Scripts/hooks/MCP/binaries:** Skills may include scripts — review before enable
- **Network/credentials:** None required for reading patterns
- **Overlap:** Skill creator, frontend-design, webapp-testing, mcp-builder
- **Security:** Prefer copying patterns; do not redistribute non-OSS document skills
- **Recommendation:** **Approved with restrictions**
- **Pin:** Track upstream main thoughtfully; prefer commit pin when installing

### anthropics/claude-plugins-official (marketplace)
- **URL:** https://github.com/anthropics/claude-plugins-official
- **Purpose:** Official plugin catalog
- **License:** Apache-2.0 (repo); plugins vary
- **Recommendation:** **Approved with restrictions**
- **Notes:** Audit MCP scopes inside plugins

### obra/superpowers
- **URL:** https://github.com/obra/superpowers
- **License:** MIT
- **Purpose:** SDLC methodology plugin
- **Security:** SessionStart hooks reshape behavior
- **Recommendation:** **Deferred pending review** (org policy on hooks)

### upstash/context7
- **URL:** https://github.com/upstash/context7
- **License:** MIT (client); SaaS backend proprietary
- **Credentials:** `CONTEXT7_API_KEY`
- **Recommendation:** **Deferred pending credentials**
- **Security:** Third-party egress for doc queries

### Anthropic Skill Creator
- **URL:** https://github.com/anthropics/skills (skill-creator) / official plugins
- **License:** Apache-2.0 (example lineage)
- **Recommendation:** **Approved**
- **Use:** Patterns applied to internal skill quality bar

### Anthropic MCP Builder
- **URL:** https://github.com/anthropics/skills/tree/main/skills/mcp-builder
- **License:** Apache-2.0
- **Recommendation:** **Approved** (reference)

### Anthropic Webapp Testing
- **URL:** https://github.com/anthropics/skills (webapp-testing)
- **Recommendation:** **Reimplemented internally** as `.claude/skills/webapp-testing`

### Anthropic Frontend Design
- **URL:** https://github.com/anthropics/skills (frontend-design)
- **Recommendation:** **Reimplemented internally** as `.claude/skills/frontend-design`

### thedotmack/claude-mem
- **URL:** https://github.com/thedotmack/claude-mem
- **License:** Apache-2.0
- **Security:** Captures tool output; local worker
- **Recommendation:** **Deferred pending review**

### nextlevelbuilder/ui-ux-pro-max-skill
- **URL:** https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- **License:** MIT
- **Recommendation:** **Deferred pending review** / principles wrapped into design skills

### Leonxlnx/taste-skill
- **URL:** https://github.com/Leonxlnx/taste-skill
- **License:** MIT
- **Recommendation:** **Deferred pending review**

### Jakubantalik/transitions.dev
- **URL:** https://github.com/Jakubantalik/transitions.dev
- **License:** Custom (no redistributing collection as competing library)
- **Recommendation:** **Deferred pending review**

## Rejected

None rejected solely on public documentation. Closest gate: claude-mem deferred for privacy/security rather than malice.

## Deferred / rejected reports

See also `docs/security/DEFERRED_AND_REJECTED_SOURCES.md`.
