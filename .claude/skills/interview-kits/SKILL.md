---
name: interview-kits
description: Build interview kits with scorecards and bias controls. Use for interview kits. Positive: Interview kit for PM. Negative: Deploy helm chart.
---

# Interview Kits

## Purpose
Build interview kits with scorecards and bias controls.

## Scope
In scope: Build interview kits with scorecards and bias controls.
Out of scope: work belonging to other departments unless explicitly coordinating.

## Preconditions
- Repository governance documents are readable (`CLAUDE.md`, `COMPANY_OS.md`, `PROJECT_TRUTH.md`).
- Required inputs for the task are available or explicitly marked missing.

## Required context
- Department: `human-resources`
- Capability ID: `skill.interview-kits`
- Related overlaps: none

## Required tools
- `Read`
- `Write`
- `Grep`
- `Glob`
- `Shell`

## Inputs
- Objective and constraints from the user
- Relevant repository files and prior decisions
- Success criteria or explicit ask

## Ordered workflow
1. Clarify objective, constraints, and success criteria
2. Gather required repository and stakeholder context
3. Execute the department workflow with evidence
4. Produce structured outputs and verification notes
5. Escalate risks and document residual uncertainty

## Decision points
- If evidence is missing, stop and request it or mark assumptions.
- If risk is high, escalate via risk-escalation / security-reviewer as appropriate.
- If another department owns the core work, route instead of diluting quality.

## Outputs
- Structured deliverable
- Assumptions list
- Verification notes

## Quality standard
- Evidence-backed claims only
- Explicit assumptions and unknowns
- Actionable next steps with owners when applicable
- No fabricated metrics, citations, or test results

## Safety restrictions
- Do not invent evidence
- Do not expose secrets
- Do not claim credentials work without testing

## Verification procedure
1. Confirm outputs match the requested objective.
2. Confirm no secrets or credentials were introduced.
3. Confirm overlaps were considered and duplicates avoided.
4. Update STATUS/PROJECT_TRUTH only with verified facts when asked.

## Failure handling
- If blocked on credentials: document as credential-blocked; continue unrelated work.
- If blocked on missing context: produce a partial brief listing gaps.
- If validation fails: do not claim success; file findings.

## Positive examples
- Interview kit for PM

## Negative examples
- Deploy helm chart
