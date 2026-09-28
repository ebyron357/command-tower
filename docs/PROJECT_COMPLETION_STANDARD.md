# Universal Project Completion Standard

> NON-NEGOTIABLE: A project is not complete because the code works. It is complete only when an authorized person can access it, understand it, operate it, administer it, support it, recover it, secure it, transfer it, and shut it down safely without guessing.

## Hard blocker rule
Only failures that prevent safe production access, core operation, authentication/authorization, required persistence, tenant isolation where applicable, administration, security, data integrity, required recovery, or responsible client handoff may block closeout. Redesigns, polish, speculative enhancements, experimental features, optional integrations, future automation, research, and nonessential modernization are NON-BLOCKING FOLLOW-UP.

## Required completion baseline
Every applicable project must document and verify: project identity/repo/default branch/production+login URLs/deployed SHA; environment map; account creation/login/logout/password requirements/temporary credentials/first-login rotation/password recovery/MFA where supported/lockout recovery; client provisioning/workspace/admin/invites/roles/ownership transfer/offboarding; complete user manual; complete admin/operator manual; roles/permissions matrix; security baseline; secrets register by name only; ownership register; billing/subscription and cost controls; integration truth; architecture/dependency map; API/integration contracts; deployment runbook; release/change control; testing; performance/capacity where applicable; monitoring/alerts/logs/auditability; incident response; backup/restore; disaster recovery/business continuity; data classification/lifecycle/export/retention/deletion/offboarding; privacy/compliance where applicable; browser/device/accessibility support; email/notification reliability; support/troubleshooting; training/knowledge transfer; source/IP/assets/licenses; domain/DNS/certificates; vendor register; software supply chain; AI agent/automation controls; known limitations; production acceptance; client acceptance; ownership transfer; decommissioning.

## Integration truth statuses
Every integration must be labeled one of: LIVE + VERIFIED, CONFIGURATION REQUIRED, AVAILABLE BUT NOT CERTIFIED, DEGRADED, NOT IMPLEMENTED, DEFERRED, DEPRECATED.

## Required repo handoff files
Each applicable production repository should contain or link to:
- docs/PROJECT_COMPLETION_STANDARD.md
- docs/PROJECT_CLOSEOUT_STATUS.md
- docs/CLIENT_USER_MANUAL.md
- docs/ADMIN_OPERATIONS_MANUAL.md
- docs/SECURITY_AND_ACCESS_HANDOFF.md
- docs/DEPLOYMENT_AND_RECOVERY_RUNBOOK.md
- docs/DATA_LIFECYCLE_AND_OFFBOARDING.md
- docs/TROUBLESHOOTING_AND_SUPPORT.md
- docs/CLIENT_ACCESS_HANDOFF_TEMPLATE.md
- docs/FINAL_CLIENT_ACCEPTANCE.md

If a document is not applicable, mark it NOT APPLICABLE with a reason in PROJECT_CLOSEOUT_STATUS.md.

## Closeout statuses
Every applicable requirement must be PASS, FAIL, BLOCKED, NOT APPLICABLE, or NON-BLOCKING FOLLOW-UP. PASS should include evidence where available.

## Agent rule
Any agent working in this repository must read this standard before declaring completion, use current code and production state rather than stale docs, avoid reopening completed work, resolve agent-doable blockers, stop only at genuine owner/external boundaries, provide evidence, and never let optional work delay closeout.

## Final closure states
Use only READY FOR CLIENT HANDOFF, READY FOR INTERNAL OPERATION, BLOCKED - OWNER ACTION REQUIRED, or BLOCKED - TECHNICAL OPERATING FAILURE.

## Final test
If an authorized person still has to guess where to log in, how to create/reset an account, how to add a user, who owns or pays for the system, how to deploy/rollback/restore it, where data lives, which integrations are truly live, how to export/delete data, how to offboard, how to get support, or how to shut the system down safely, the operational handoff is incomplete.
