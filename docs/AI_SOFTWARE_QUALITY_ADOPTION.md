# AI Software Quality, Security & Production Readiness — Repository Adoption

**Canonical standard:** https://github.com/ebyron357/AI-Operating-Standards/blob/main/docs/AI_SOFTWARE_QUALITY_SECURITY_MASTER_STANDARD.md

This repository adopts the governing standard for all applicable functionality. This checklist is **NOT** an audit result or compliance certification.

## Verification checklist
- [ ] Visual integrity: consistent design tokens, typography, spacing, gradients, shadows, icons, cards, and responsive layout.
- [ ] Code quality: no unused imports, duplicate components, dead pages, conflicting CSS, unnecessary packages, hallucinated APIs, or abandoned code.
- [ ] Real UI: buttons, forms, settings, charts, data, notifications, testimonials and integrations are functional and truthful.
- [ ] Responsive and accessibility: mobile navigation, tables, dialogs, keyboard, screen readers, contrast, labels, WCAG 2.2 AA evaluation.
- [ ] Security: no exposed secrets, permissive endpoints, authorization bypass, tenant leakage, unsafe rendering, insecure uploads, vulnerable dependencies.
- [ ] Backend: real persistence, validation, migrations, recovery, data integrity, tenant separation, backups.
- [ ] Integrations: OAuth, webhooks, signature verification, retries, quotas, logging and recovery.
- [ ] AI agents where applicable: registered identity, supervisor, scoped tools, approval gates, activity traces, JEV, revocation and owner control.
- [ ] Performance and discovery: Core Web Vitals, SEO, GEO, AEO, structured data, no deceptive injections.
- [ ] Privacy/compliance: HIPAA/NIST/government requirements assessed only where applicable, with evidence and appropriate agreements.
- [ ] Tests and deployment: CI, E2E, visual regression, accessibility, security scans, rollback and production verification.
- [ ] Documentation: current architecture, ownership, inventory, runbooks, audit evidence, canonical standards.

## Required defect record
Issue ID | affected path | severity P0-P3 | reproduction | evidence | impact | corrective action | owner | tests | approval | status.

## Operating rules
Inspect before changing. Do not invent findings, blockers, compliance, passing tests or completed work. Preserve working code, data, branding and project intent. Use isolated reviewable PRs, least privilege, security checks and owner approval for release. Continue independently authorized work while reporting real constraints precisely.

**Current status: NOT INSPECTED.** Each item needs repository-specific evidence before completion.
