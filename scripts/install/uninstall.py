#!/usr/bin/env python3
"""Uninstall components installed by this repository's Company OS layout.

Preserves unrelated user configuration (~/.claude).
By default only removes generated Company OS paths when --confirm is passed.
"""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# Paths owned by this Company OS implementation (project-level only)
OWNED = [
    ".claude/skills",
    ".claude/agents",
    ".claude/commands",
    ".claude/settings.json",
    "company",
    "registries",
    "docs/audits",
    "docs/architecture",
    "docs/installation",
    "docs/security",
    "docs/source-of-truth",
    "docs/testing",
    "scripts/audit",
    "scripts/install",
    "scripts/validate",
    "scripts/test",
    "tests",
    "CLAUDE.md",
    "COMPANY_OS.md",
    "PROJECT_TRUTH.md",
    "STATUS.md",
    "ROADMAP.md",
    "HANDOFF.md",
    "SECURITY_POLICY.md",
    "CHANGELOG.md",
    "backups",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--confirm", action="store_true", help="Required to delete")
    args = parser.parse_args()

    if not args.dry_run and not args.confirm:
        print("Refusing to delete without --confirm (or use --dry-run).")
        return 2

    for rel in OWNED:
        path = ROOT / rel
        exists = path.exists()
        action = "WOULD_REMOVE" if args.dry_run else "REMOVE"
        print(f"{action if exists else 'MISSING'}: {rel}")
        if exists and not args.dry_run:
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()
    print("Done. User home Claude config was not modified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
