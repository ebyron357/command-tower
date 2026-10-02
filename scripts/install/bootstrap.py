#!/usr/bin/env python3
"""Bootstrap / verify Command Tower Company OS project files.

Does not install external plugins or MCP credentials.
Does not modify ~/.claude user configuration.
"""
from __future__ import annotations

import argparse
import json
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def detect_prereqs() -> dict:
    info = {
        "os": platform.platform(),
        "python": sys.version.split()[0],
        "claude_cli": None,
        "git": None,
    }
    try:
        info["claude_cli"] = subprocess.check_output(["claude", "--version"], text=True, stderr=subprocess.STDOUT).strip()
    except Exception:
        info["claude_cli"] = "not-found"
    try:
        info["git"] = subprocess.check_output(["git", "--version"], text=True).strip()
    except Exception:
        info["git"] = "not-found"
    return info


def backup_settings() -> str | None:
    settings = ROOT / ".claude" / "settings.json"
    if not settings.exists():
        return None
    backup_dir = ROOT / "backups"
    backup_dir.mkdir(exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    dest = backup_dir / f"claude-settings-{stamp}.json"
    dest.write_text(settings.read_text(encoding="utf-8"), encoding="utf-8")
    return str(dest.relative_to(ROOT))


def required_paths() -> list[Path]:
    return [
        ROOT / "CLAUDE.md",
        ROOT / "COMPANY_OS.md",
        ROOT / "registries" / "CAPABILITY_REGISTRY.yaml",
        ROOT / ".claude" / "settings.json",
        ROOT / "scripts" / "validate" / "validate_company_os.py",
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--upgrade", action="store_true", help="Backup settings before verify")
    args = parser.parse_args()

    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "mode": "upgrade" if args.upgrade else "fresh-verify",
        "prereqs": detect_prereqs(),
        "backup": None,
        "missing": [],
        "skipped": [
            "external-plugins",
            "mcp-servers",
            "git-hooks",
            "credential-dependent-integrations",
        ],
        "credential_requirements": ["CONTEXT7_API_KEY (optional, for Context7 MCP)"],
        "validation": None,
    }

    if args.upgrade:
        report["backup"] = backup_settings()

    for p in required_paths():
        if not p.exists():
            report["missing"].append(str(p.relative_to(ROOT)))

    # Ensure settings exists with safe defaults
    settings = ROOT / ".claude" / "settings.json"
    settings.parent.mkdir(parents=True, exist_ok=True)
    if not settings.exists():
        settings.write_text(json.dumps({"permissions": {"allow": [], "deny": []}, "hooks": {}}, indent=2) + "\n", encoding="utf-8")

    # Run validation
    val = ROOT / "scripts" / "validate" / "validate_company_os.py"
    if val.exists():
        proc = subprocess.run([sys.executable, str(val)], cwd=str(ROOT), capture_output=True, text=True)
        report["validation"] = {
            "exit_code": proc.returncode,
            "stdout_tail": "\n".join(proc.stdout.splitlines()[-40:]),
            "stderr_tail": "\n".join(proc.stderr.splitlines()[-20:]),
        }
    else:
        report["validation"] = {"exit_code": 2, "error": "validator missing"}

    out = ROOT / "docs" / "installation" / "LAST_INSTALL_REPORT.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# LAST_INSTALL_REPORT",
        "",
        f"Generated: {report['timestamp']}",
        f"Mode: {report['mode']}",
        "",
        "## Prerequisites",
        "```json",
        json.dumps(report["prereqs"], indent=2),
        "```",
        "",
        f"Backup: {report['backup'] or 'none'}",
        "",
        "## Missing required paths",
        *(f"- {m}" for m in report["missing"] or ["none"]),
        "",
        "## Skipped components",
        *(f"- {s}" for s in report["skipped"]),
        "",
        "## Credential requirements",
        *(f"- {c}" for c in report["credential_requirements"]),
        "",
        "## Validation",
        f"Exit code: {report['validation'].get('exit_code')}",
        "```",
        report["validation"].get("stdout_tail") or report["validation"].get("error") or "",
        "```",
        "",
    ]
    out.write_text("\n".join(lines), encoding="utf-8")
    print(out.read_text(encoding="utf-8"))
    return int(report["validation"].get("exit_code") or 1)


if __name__ == "__main__":
    sys.exit(main())
