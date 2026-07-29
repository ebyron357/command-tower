# ORIGINAL_CAPABILITY_RECOVERY.md

## Recovery method

| Step | Evidence |
|---|---|
| Git history search | Only commit on `main`: `6ffcb7b` — `README.md` (“central command platform for AI engineering… BWA ecosystem”) |
| Branch search | No historical feature branches with skill inventories |
| Docs/search for “128 skills”, “100 skills”, “company OS”, “org chart” | Not present in repository before this build |
| Claude environment | No prior project `.claude/` skills/agents/commands |
| Assignment text | Provided explicit departments, candidate agents/commands, and external repositories |

**Conclusion:** The complete original numbered skill list could not be recovered from git. The inventory was **reconstructed** from (a) recovered external sources named in the assignment, (b) department capability objectives in the assignment, and (c) newly designed internal capabilities required to operate a Company OS.

## Distinction legend

- **Recovered** — Named in assignment external-source list or clearly implied by README mission + assignment text as a known upstream.
- **Newly designed** — Created to fulfill department coverage and Company OS operating model.

## Recovered external / reference items

| Original name | Source | Intended department | Intended purpose | Actually a Claude skill? | Classification | Duplicate/overlap | Security | Canonical interpretation | Disposition |
|---|---|---|---|---|---|---|---|---|---|
| anthropics/skills | GitHub Anthropic | Engineering | Official skill patterns + examples | Mixed (skills + marketplace) | External dependency / Plugin marketplace | Overlaps internal skill authoring | Review scripts; mixed licenses | Canonical pattern source | Approved with restrictions |
| Claude Code plugin marketplace | Anthropic | Engineering | Discover/install plugins | No (marketplace) | Plugin | — | Audit MCP inside plugins | Official install path | Approved with restrictions |
| obra/superpowers | GitHub + marketplace | Engineering | SDLC methodology | Plugin with skills/hooks | Plugin | Overlaps internal planning/debug skills | SessionStart hooks | Optional methodology pack | Deferred pending org policy |
| upstash/context7 | GitHub / SaaS | Engineering | Live library docs | MCP | MCP connector | Overlaps static docs | API key; data egress | Public-docs MCP | Deferred pending credentials |
| Skill Creator | Anthropic | Engineering | Author/eval skills | Skill/plugin | External dependency | — | Eval may run scripts | Authoring standard | Approved (patterns applied) |
| MCP Builder | anthropics/skills | Engineering | Build MCP servers | Skill | External / Reference | — | Built MCPs need auth | Authoring standard | Approved |
| Webapp Testing | anthropics/skills | Engineering | Playwright local testing | Skill | Agent Skill (reimplemented) | Overlaps QA | Local browser/server | Internal `webapp-testing` | Reimplemented internally |
| Frontend Design | anthropics/skills | Design/Engineering | Anti-generic UI | Skill | Agent Skill (reimplemented) | Overlaps brand skills | Prompt-only | Internal `frontend-design` | Reimplemented internally |
| thedotmack/claude-mem | GitHub | Engineering/Ops | Persistent memory | Plugin + local worker | Plugin | — | High: captures tool output | Optional memory | Deferred pending security review |
| ui-ux-pro-max-skill | GitHub | Design | Design intelligence pack | Skill pack | External dependency | Overlaps design skills | Review scripts | Optional reference | Deferred; principles wrapped |
| taste-skill | GitHub | Design | Anti-slop taste | Skill | External dependency | Conflicts with brand/frontend-design | Prompt/assets | Optional | Deferred |
| transitions.dev | GitHub | Design | CSS transitions | Skill + snippets | External dependency | Motion guidance | Custom license no-redistribute | Snippet reference only | Deferred |

## Recovered organizational intent (from assignment)

Departments and capability themes listed in the assignment (executive through quality-security) are treated as **recovered requirements**, even where individual skill names were not present in git.

Candidate subagents recovered from assignment text (implemented):

`chief-of-staff`, `repository-auditor`, `software-architect`, `implementation-engineer`, `code-reviewer`, `qa-lead`, `security-reviewer`, `research-director`, `competitive-intelligence-analyst`, `product-manager`, `design-director`, `marketing-strategist`, `sales-strategist`, `customer-success-manager`, `data-analyst`, `finance-analyst`, `compliance-reviewer`, `operations-manager`, `completion-auditor`

Candidate commands recovered from assignment text (implemented under `.claude/commands/`).

## Newly designed items

All department skills not listed as upstream Anthropic/community packages were newly designed as internal project skills. Full machine-readable list: `registries/CAPABILITY_REGISTRY.yaml` (`origin: newly-designed` vs `recovered`).

## Consolidation decisions

| Overlap | Decision |
|---|---|
| Anthropic frontend-design vs community UI packs | Reimplement official patterns internally; defer community packs |
| Superpowers vs internal engineering skills | Keep internal skills; defer Superpowers plugin |
| Multiple “status” docs | Single `STATUS.md` + `PROJECT_TRUTH.md` roles |
| Marketing vs Content | Content capabilities live primarily under marketing skills; `company/content/` points to shared ownership |
| Completion-review skill vs completion-auditor agent | Skill = workflow; agent = isolated audit pass |

## Security concerns from recovery

- Memory plugins and install-script-heavy community packs are highest risk.
- Credentialed MCP must not be marked operational without keys.
- Mixed licenses in anthropics/skills document skills (not redistributed here).

## Final disposition summary

- Reconstruct full Company OS inventory (≥100 useful capabilities).
- Implement internal skills/agents/commands.
- Source-review externals; install none automatically that are deferred/rejected.
- Register everything with honest statuses.
