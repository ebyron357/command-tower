# Integration workflow fixtures

These are **evaluation fixtures** for cross-department workflows.
They are not automatically executed Claude runtime tests.

| ID | Workflow | Departments | Expected routing |
|---|---|---|---|
| INT-01 | New repository onboarding | Engineering, Executive | `/repo-onboard`, repo-onboarding skill, repository-auditor |
| INT-02 | Feature planning + implementation | Product, Engineering | product-requirements → feature-implementation → code-review |
| INT-03 | Code + security review | Engineering, Quality-Security | `/code-review`, `/security-review` |
| INT-04 | Deep market research | Research, Marketing | `/research`, `/market-research`, source-verify |
| INT-05 | Competitive analysis | Research, Sales, Product | `/competitor-brief` |
| INT-06 | Brand + content campaign | Design, Marketing | brand-application, `/content-plan` |
| INT-07 | Sales meeting preparation | Sales | `/sales-brief`, discovery-prep |
| INT-08 | Customer onboarding | Customer Success | customer-onboarding, `/customer-health` |
| INT-09 | KPI investigation | Data | metric-diagnostics, data-analyst |
| INT-10 | Financial scenario analysis | Finance | `/financial-analysis` + disclaimer |
| INT-11 | Compliance research | Legal, Research | `/compliance-check`, regulatory-research |
| INT-12 | SOP creation | Operations | `/process-design`, sop-creation |
| INT-13 | Release readiness | Quality, Engineering, Product | `/release-readiness` |
| INT-14 | Project completion + handoff | Executive, Quality | `/completion-audit`, `/generate-handoff` |

See per-file JSON fixtures in this directory for positive/negative expectations.
