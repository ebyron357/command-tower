#!/usr/bin/env python3
"""Quick audit helpers for Company OS."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main() -> None:
    summary = json.loads((ROOT / "registries" / "GENERATION_SUMMARY.json").read_text(encoding="utf-8"))
    print(json.dumps(summary, indent=2))
    skills = len(list((ROOT / ".claude" / "skills").glob("*/SKILL.md")))
    agents = len(list((ROOT / ".claude" / "agents").glob("*.md")))
    commands = len(list((ROOT / ".claude" / "commands").glob("*.md")))
    print(f"disk_skills={skills} disk_agents={agents} disk_commands={commands}")


if __name__ == "__main__":
    main()
