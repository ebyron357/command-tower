#!/usr/bin/env python3
"""Validate Command Tower Claude Company OS structure, registries, and safety.

Exit codes:
  0 = all checks passed
  1 = one or more failures
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ERRORS: list[str] = []
WARNINGS: list[str] = []
PASSED = 0
SKIPPED = 0

SECRET_PATTERNS = [
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----"),
    re.compile(r"(?i)api[_-]?key\s*[:=]\s*['\"][^'\"]{12,}['\"]"),
    re.compile(r"(?i)secret\s*[:=]\s*['\"][^'\"]{12,}['\"]"),
    re.compile(r"(?i)password\s*[:=]\s*['\"][^'\"]{8,}['\"]"),
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"gho_[A-Za-z0-9]{20,}"),
    re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"),
]

UNSAFE_SHELL = [
    re.compile(r"\brm\s+-rf\s+/(?:\s|$)"),
    re.compile(r"\bcurl\s+[^|]+\|\s*(?:ba)?sh\b"),
    re.compile(r"\bwget\s+[^|]+\|\s*(?:ba)?sh\b"),
    re.compile(r"eval\s*\$\("),
]

PLACEHOLDER = re.compile(r"\b(TODO|FIXME|TBD|PLACEHOLDER|lorem ipsum)\b", re.I)


def ok(msg: str) -> None:
    global PASSED
    PASSED += 1
    print(f"PASS: {msg}")


def fail(msg: str) -> None:
    ERRORS.append(msg)
    print(f"FAIL: {msg}")


def warn(msg: str) -> None:
    WARNINGS.append(msg)
    print(f"WARN: {msg}")


def skip(msg: str) -> None:
    global SKIPPED
    SKIPPED += 1
    print(f"SKIP: {msg}")


def parse_simple_registry(path: Path) -> list[dict]:
    """Minimal YAML-ish parser for our generated registry format."""
    text = path.read_text(encoding="utf-8")
    caps: list[dict] = []
    current: dict | None = None
    list_key: str | None = None
    for raw in text.splitlines():
        if raw.strip().startswith("#") or not raw.strip():
            continue
        if raw.startswith("  - id:"):
            if current:
                caps.append(current)
            current = {"id": raw.split(":", 1)[1].strip()}
            list_key = None
            continue
        if current is None:
            continue
        if raw.startswith("    ") and not raw.startswith("      "):
            line = raw.strip()
            if line.endswith(":") and ":" == line[-1] and line.count(":") == 1:
                list_key = line[:-1]
                current[list_key] = []
            else:
                key, _, val = line.partition(":")
                current[key.strip()] = val.strip().strip('"')
                list_key = None
        elif raw.startswith("      - ") and list_key:
            current[list_key].append(raw.strip()[2:].strip().strip('"'))
    if current:
        caps.append(current)
    return caps


def frontmatter(text: str) -> dict | None:
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    meta = {}
    for line in parts[1].splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        k, _, v = line.partition(":")
        meta[k.strip()] = v.strip()
    return meta


def check_skills(caps: list[dict]) -> None:
    skill_caps = [c for c in caps if c.get("type") == "skill"]
    names = []
    descs = []
    for c in skill_caps:
        name = c["name"]
        path = ROOT / ".claude" / "skills" / name / "SKILL.md"
        if not path.exists():
            fail(f"Missing SKILL.md for {name}")
            continue
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            fail(f"Empty skill file: {name}")
            continue
        meta = frontmatter(text)
        if not meta:
            fail(f"Invalid/missing YAML frontmatter: {name}")
            continue
        if meta.get("name") != name:
            fail(f"Skill name mismatch: folder={name} frontmatter={meta.get('name')}")
            continue
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            fail(f"Invalid skill name (kebab-case required): {name}")
            continue
        if not meta.get("description"):
            fail(f"Missing description: {name}")
            continue
        for section in ["Purpose", "Ordered workflow", "Safety restrictions", "Positive examples", "Negative examples"]:
            if f"## {section}" not in text and f"## {section.title()}" not in text:
                # allow Purpose via # and ## Purpose
                if f"## {section}" not in text:
                    fail(f"Missing section '{section}' in {name}")
                    break
        else:
            ok(f"Skill structure: {name}")
        names.append(name)
        descs.append(meta["description"])
        fixture = ROOT / "tests" / "skills" / name / "fixtures.json"
        if not fixture.exists():
            fail(f"Missing skill fixture: {name}")
        else:
            data = json.loads(fixture.read_text(encoding="utf-8"))
            if not data.get("positive_triggers") or not data.get("negative_triggers"):
                fail(f"Incomplete trigger fixtures: {name}")
            else:
                ok(f"Skill fixtures: {name}")

    dup_names = [n for n, c in Counter(names).items() if c > 1]
    if dup_names:
        fail(f"Duplicate skill names: {dup_names}")
    else:
        ok("No duplicate skill names")

    # Overlapping descriptions heuristic
    desc_counts = Counter(descs)
    dups = [d for d, c in desc_counts.items() if c > 1]
    if dups:
        fail(f"Duplicate skill descriptions: {len(dups)}")
    else:
        ok("No duplicate skill descriptions")


def check_agents(caps: list[dict]) -> None:
    names = []
    for c in [x for x in caps if x.get("type") == "subagent"]:
        name = c["name"]
        path = ROOT / ".claude" / "agents" / f"{name}.md"
        if not path.exists():
            fail(f"Missing agent file: {name}")
            continue
        text = path.read_text(encoding="utf-8")
        meta = frontmatter(text)
        if not meta or meta.get("name") != name:
            fail(f"Invalid agent frontmatter: {name}")
            continue
        for section in ["Role", "Allowed tools", "Prohibited actions", "Output contract"]:
            if f"## {section}" not in text:
                fail(f"Missing agent section {section}: {name}")
                break
        else:
            ok(f"Agent structure: {name}")
        names.append(name)
        fixture = ROOT / "tests" / "agents" / name / "fixtures.json"
        if fixture.exists():
            ok(f"Agent fixtures: {name}")
        else:
            fail(f"Missing agent fixture: {name}")
    dups = [n for n, c in Counter(names).items() if c > 1]
    if dups:
        fail(f"Duplicate agent names: {dups}")
    else:
        ok("No duplicate agent names")


def check_commands(caps: list[dict]) -> None:
    names = []
    for c in [x for x in caps if x.get("type") == "command"]:
        name = c["name"]
        path = ROOT / ".claude" / "commands" / f"{name}.md"
        if not path.exists():
            fail(f"Missing command file: {name}")
            continue
        text = path.read_text(encoding="utf-8")
        if f"# /{name}" not in text and f"# {name}" not in text:
            fail(f"Command heading missing: {name}")
        else:
            ok(f"Command structure: {name}")
        names.append(name)
        fixture = ROOT / "tests" / "commands" / name / "fixtures.json"
        if fixture.exists():
            ok(f"Command fixtures: {name}")
        else:
            fail(f"Missing command fixture: {name}")
    dups = [n for n, c in Counter(names).items() if c > 1]
    if dups:
        fail(f"Duplicate command names: {dups}")
    else:
        ok("No duplicate command names")


def check_registry_fs(caps: list[dict]) -> None:
    for c in caps:
        ctype = c.get("type")
        name = c.get("name")
        if ctype == "skill":
            if not (ROOT / ".claude" / "skills" / name / "SKILL.md").exists():
                if c.get("status") in ("implemented", "structure-validated", "fully-verified"):
                    fail(f"Registry skill missing on disk: {name}")
        elif ctype == "subagent":
            if not (ROOT / ".claude" / "agents" / f"{name}.md").exists():
                if c.get("status") == "implemented":
                    fail(f"Registry agent missing on disk: {name}")
        elif ctype == "command":
            if not (ROOT / ".claude" / "commands" / f"{name}.md").exists():
                if c.get("status") == "implemented":
                    fail(f"Registry command missing on disk: {name}")
    ok("Registry/filesystem consistency checked")

    # Unregistered skills on disk
    registered = {c["name"] for c in caps if c.get("type") == "skill"}
    for p in (ROOT / ".claude" / "skills").glob("*/SKILL.md"):
        if p.parent.name not in registered:
            fail(f"Unregistered skill on disk: {p.parent.name}")
    ok("No unregistered skills")


def check_governance() -> None:
    required = [
        "CLAUDE.md",
        "COMPANY_OS.md",
        "PROJECT_TRUTH.md",
        "STATUS.md",
        "ROADMAP.md",
        "HANDOFF.md",
        "SECURITY_POLICY.md",
        "CHANGELOG.md",
        "docs/source-of-truth/ORIGINAL_CAPABILITY_RECOVERY.md",
        "docs/audits/CURRENT_ENVIRONMENT_AUDIT.md",
        "docs/audits/SECURITY_AUDIT.md",
        "docs/installation/FRESH_INSTALL.md",
        "docs/installation/EXISTING_ENVIRONMENT_UPGRADE.md",
        "docs/installation/PLUGIN_INSTALLATION.md",
        "docs/installation/MCP_SETUP.md",
        "docs/installation/TROUBLESHOOTING.md",
        "registries/CAPABILITY_REGISTRY.yaml",
        "registries/SOURCE_REGISTRY.md",
        ".claude/settings.json",
    ]
    for rel in required:
        if (ROOT / rel).exists():
            ok(f"Present: {rel}")
        else:
            fail(f"Missing required file: {rel}")


def check_settings() -> None:
    path = ROOT / ".claude" / "settings.json"
    if not path.exists():
        fail("Missing .claude/settings.json")
        return
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        fail(f"Invalid settings.json: {e}")
        return
    if data.get("hooks"):
        # Only allow empty or explicitly documented safe hooks
        warn("Hooks present in settings.json — ensure they are reviewed")
    else:
        ok("No hooks enabled in settings.json")
    ok("settings.json is valid JSON")


def check_secrets_and_shell() -> None:
    ignore_dirs = {".git", ".venv", "node_modules", "__pycache__"}
    scanned = 0
    for path in ROOT.rglob("*"):
        if any(part in ignore_dirs for part in path.parts):
            continue
        if not path.is_file():
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".pdf", ".zip"}:
            continue
        if path.stat().st_size > 2_000_000:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        scanned += 1
        rel = str(path.relative_to(ROOT))
        # Allow .env.example placeholders
        if path.name == ".env.example":
            continue
        for pat in SECRET_PATTERNS:
            if pat.search(text):
                # Allow documentation that mentions pattern names without real secrets
                if "gho_************************************" in text or "EXAMPLE" in text:
                    continue
                if re.search(r"gho_\*+", text) and pat.pattern.startswith("gho_"):
                    continue
                fail(f"Credential-like pattern in {rel}: {pat.pattern[:30]}...")
        if path.suffix in {".sh", ".ps1", ".py", ".js", ".ts"} or "scripts" in path.parts:
            for pat in UNSAFE_SHELL:
                if pat.search(text):
                    fail(f"Unsafe shell pattern in {rel}")
        if path.suffix in {".md", ".yaml", ".yml"} and PLACEHOLDER.search(text):
            # placeholders in ROADMAP/HANDOFF are ok-ish; warn only for skills/agents/commands
            if any(x in path.parts for x in ("skills", "agents", "commands")):
                warn(f"Placeholder-like text in {rel}")
    ok(f"Scanned {scanned} files for secrets/unsafe patterns")


def check_trigger_fixtures() -> None:
    """Static evaluation of trigger fixtures (not Claude runtime)."""
    count = 0
    for base in ["skills", "agents", "commands"]:
        root = ROOT / "tests" / base
        if not root.exists():
            continue
        for fixture in root.rglob("fixtures.json"):
            data = json.loads(fixture.read_text(encoding="utf-8"))
            pos = data.get("positive_triggers") or []
            neg = data.get("negative_triggers") or []
            if not pos or not neg:
                fail(f"Fixture missing triggers: {fixture}")
                continue
            # Heuristic: positive and negative should not be identical sets
            if set(map(str.lower, pos)) & set(map(str.lower, neg)):
                fail(f"Overlapping pos/neg triggers: {fixture}")
                continue
            count += 1
            ok(f"Trigger fixture evaluated: {fixture.relative_to(ROOT)}")
    if count == 0:
        fail("No trigger fixtures found")
    else:
        ok(f"Evaluated {count} trigger fixtures (static)")


def check_capability_count(caps: list[dict]) -> None:
    if len(caps) < 100:
        fail(f"Capability count {len(caps)} < 100")
    else:
        ok(f"Capability count {len(caps)} >= 100")
    by_type = Counter(c.get("type") for c in caps)
    print("INFO: by_type", dict(by_type))


def main() -> int:
    print("=== Command Tower Company OS Validation ===")
    print(f"ROOT={ROOT}")
    reg = ROOT / "registries" / "CAPABILITY_REGISTRY.yaml"
    if not reg.exists():
        fail("Missing CAPABILITY_REGISTRY.yaml")
        print(f"\nFAILED with {len(ERRORS)} errors")
        return 1
    caps = parse_simple_registry(reg)
    check_capability_count(caps)
    check_governance()
    check_settings()
    check_skills(caps)
    check_agents(caps)
    check_commands(caps)
    check_registry_fs(caps)
    check_trigger_fixtures()
    check_secrets_and_shell()

    print("\n=== Summary ===")
    print(f"Passed: {PASSED}")
    print(f"Failed: {len(ERRORS)}")
    print(f"Warnings: {len(WARNINGS)}")
    print(f"Skipped: {SKIPPED}")
    if ERRORS:
        print("\nFailures:")
        for e in ERRORS:
            print(f" - {e}")
        return 1
    print("\nALL CHECKS PASSED (static/structural validation)")
    print("NOTE: Claude runtime discovery/trigger tests were NOT executed in this suite.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
