# COMPANY_OS.md — Company Structure and Routing

## Mission

Operate Claude Code as a professional company: specialized departments, reusable skills, isolated subagents when needed, explicit commands, and evidence-based completion.

## Departments

| Department | Path | Primary jobs |
|---|---|---|
| Executive | `company/executive/` | Orchestration, status, prioritization, completion |
| Engineering | `company/engineering/` | Architecture, implementation, review, DevOps |
| Product | `company/product/` | PRDs, stories, prioritization, release planning |
| Design | `company/design/` | UX/UI, design systems, accessibility, brand |
| Marketing | `company/marketing/` | Research, positioning, campaigns, content |
| Content | `company/content/` | Editorial and repurposing (shared with marketing skills) |
| Sales | `company/sales/` | Account research, discovery, proposals, pipeline |
| Customer Success | `company/customer-success/` | Onboarding, health, renewals, CS reporting |
| Research | `company/research/` | Deep research, CI, source verification |
| Data & Analytics | `company/data-analytics/` | KPIs, diagnostics, forecasting, experiments |
| Finance | `company/finance/` | Budgeting, scenarios, unit economics (advisory) |
| Legal & Compliance | `company/legal-compliance/` | Issue spotting, checklists (not legal advice) |
| Operations | `company/operations/` | SOPs, workflows, incidents, handoffs |
| Human Resources | `company/human-resources/` | Roles, hiring, interview kits, onboarding |
| Training | `company/training/` | Curricula and internal knowledge systems |
| Quality & Security | `company/quality-security/` | Security, QA, release readiness, governance |

## Capability types

| Type | When to use |
|---|---|
| Governing instruction | Repo-wide rules (`CLAUDE.md`, policies) |
| Agent Skill | Reusable task instructions auto-loaded when relevant |
| Subagent | Isolated context / least-privilege specialty |
| User command | Explicit repeatable slash workflow |
| Plugin | Reviewed external package (install only when approved) |
| MCP connector | External system/data access |
| Hook | Deterministic lifecycle automation (prefer none unless safe) |
| Validation utility | Deterministic checks |
| External dependency | Reviewed third-party source |
| Reference resource | Registries, docs, inventories |

## Routing model

1. **Classify** the request (department + capability type).
2. **Search** `registries/CAPABILITY_REGISTRY.yaml` / `/capability-search`.
3. **Load** the matching skill(s).
4. **Delegate** to a subagent only when isolation or restricted tools help.
5. **Orchestrate** multi-department work via `chief-of-staff`.
6. **Verify** with validation utilities and evidence.
7. **Escalate** security, legal, and finance-certified needs to humans.

## Orchestration rules

- Chief-of-staff aggregates status; it does not silently rewrite department ownership.
- Engineering owns code changes; Product owns requirements clarity; Security owns high-severity findings disposition.
- Marketing/Sales must not fabricate metrics or customer quotes.
- Finance/Legal skills must include professional disclaimers.
- Quality & Security can veto false-done claims.

## Completion standard

A capability is **fully-verified** only when source, license, structure, registration, discovery, positive/negative triggers, output quality, safety, dependencies, credentials status, overlap review, and docs are evidenced. Use lower statuses when any gate is incomplete.
