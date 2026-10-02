# /release-readiness

## Purpose
Assess release readiness with evidence.

## Business value
Go/no-go support.

## Invocation
`/release-readiness`

## Required inputs
- Clear objective (or accept defaults from PROJECT_TRUTH/STATUS when appropriate)
- Any entity names (account, competitor, release) when relevant

## Missing-input behavior
If required inputs are absent, ask for them. If defaults exist in governance docs, state the defaults used.

## Routing
1. Read `PROJECT_TRUTH.md`, `STATUS.md`, and relevant registry entries.
2. Load the matching department skill(s) and/or subagent.
3. Execute the workflow.
4. Write or update only requested artifacts.
5. Report evidence and residual risks.

## Expected output
- Concise result matching the command purpose
- Evidence references
- Next actions
- Explicit status of verification (static / fixture / runtime / credential-blocked)

## Failure handling
- Do not fabricate success
- Document blockers
- Preserve working tree safety (no secrets, no force push, no merge)

## Safety behavior
- Follow SECURITY_POLICY.md
- Least privilege
- No credential printing

## Positive trigger examples
- /release-readiness

## Negative trigger examples
- Ignore open blockers

## Related capabilities
See CAPABILITY_REGISTRY.yaml
