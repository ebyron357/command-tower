# PROJECT_TRUTH.md — Verified Current State

> Only verified facts. Last updated from repository inspection during Company OS build.

## Repository

| Field | Value |
|---|---|
| Remote | `https://github.com/ebyron357/command-tower.git` |
| Default branch | `main` |
| Starting commit | `6ffcb7b4999d4c34ba750094fd074ec6b4c80be0` (Initial commit: README only) |
| Working branch | `agent/claude-company-os-complete` |
| Pre-build contents | `README.md` only; no prior `.claude/` skills/agents/commands |
| Claude Code CLI | `2.1.220` (detected on builder machine) |
| Python | `3.13.14` |
| Node | `v24.18.0` |
| GitHub auth | Available as `ebyron357` with `repo` scope (at build time) |

## What exists now (implementation)

- Canonical governance documents at repo root
- `.claude/skills/`, `.claude/agents/`, `.claude/commands/`, `.claude/settings.json`
- `company/` department READMEs
- `registries/CAPABILITY_REGISTRY.yaml` and human-readable registries
- Validation suite at `scripts/validate/validate_company_os.py`
- Generator at `scripts/install/generate_company_os.py`
- Installation and audit docs under `docs/`
- Behavioral fixtures under `tests/`

## Capability counts (from generator summary)

See `registries/GENERATION_SUMMARY.json` for exact numbers produced at generation time.

Approximate taxonomy after generation:

- 100+ total registered capabilities across types
- Skills implemented under `.claude/skills/`
- Subagents under `.claude/agents/`
- Commands under `.claude/commands/`
- Plugins/MCP/hooks largely **deferred** or **documented**, not silently marked operational

## Original intent recovery

No prior “128 skills” inventory existed in git history (single initial commit). Inventory was **reconstructed** from the assignment’s department objectives plus recovered external source list. See `docs/source-of-truth/ORIGINAL_CAPABILITY_RECOVERY.md`.

## Explicit non-claims

- Context7 MCP is **not** configured with credentials in-repo.
- External plugins (superpowers, claude-mem, UI packs) are **not** auto-installed.
- No hooks are enabled in `.claude/settings.json`.
- Claude runtime discovery/trigger tests require Claude Code interactive sessions; static fixtures ≠ runtime proof.
- Legal/finance capabilities are advisory support only.
