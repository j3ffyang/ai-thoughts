#!/usr/bin/env python3
"""Publish skills in .opencode/skills/ to ClawHub via the pinned ClawHub CLI.

Run from the repo root inside GitHub Actions. The workflow sets up:
    <workspace>/clawhub-source/...  openclaw/clawhub checkout (ref: v0.23.3)
    CLAWHUB_CONFIG_PATH             config file with registry + token (real publish only)

The CLI returns one of five statuses — unchanged, would-publish, submitted,
published, pending-publication. All five mean the run succeeded; anything else
is a real failure. (The upstream skill-publish workflow only maps three of the
five, so a successful async publish shows up as a false failure there.)

Usage:
    python scripts/clawhub_publish.py            # publish all skills
    python scripts/clawhub_publish.py --dry-run  # preview without publishing
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

SKILLS_ROOT = ".opencode/skills"
SITE = "https://clawhub.ai"
REGISTRY = "https://clawhub.ai"
OK_STATUSES = {"unchanged", "would-publish", "submitted", "published", "pending-publication"}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dry-run", action="store_true", help="preview without publishing")
    args = ap.parse_args()

    workspace = Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    cli_entry = workspace / "clawhub-source" / "packages" / "clawhub" / "src" / "cli.ts"
    if not cli_entry.is_file():
        print(f"Missing ClawHub CLI entrypoint at {cli_entry}", file=sys.stderr)
        return 1

    root = workspace / SKILLS_ROOT
    targets = sorted(
        (p for p in root.iterdir() if p.is_dir() and (p / "SKILL.md").is_file()),
        key=lambda p: p.name.lower(),
    )
    if not targets:
        print(f"No skill folders found under {SKILLS_ROOT}", file=sys.stderr)
        return 1

    source_commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=workspace, text=True).strip()
    source_repo = os.environ["SOURCE_REPOSITORY"]
    source_ref = os.environ["SOURCE_REF"]

    ok, failed = [], []
    for target in targets:
        rel = target.relative_to(workspace).as_posix()
        cmd = [
            "bun",
            str(cli_entry),
            "--workdir", str(workspace),
            "--site", SITE,
            "--registry", REGISTRY,
            "skill", "publish", rel,
            "--json",
            "--tags", "latest",
            "--source-repo", source_repo,
            "--source-commit", source_commit,
            "--source-ref", source_ref,
            "--source-path", rel,
        ]
        if args.dry_run:
            cmd.append("--dry-run")
        completed = subprocess.run(cmd, cwd=workspace, capture_output=True, text=True)
        if completed.returncode != 0:
            message = completed.stderr.strip() or completed.stdout.strip() or f"exit {completed.returncode}"
            failed.append({"slug": target.name, "status": "cli-error", "message": message})
            continue
        try:
            status = json.loads(completed.stdout).get("status")
            if status in OK_STATUSES:
                ok.append({"slug": target.name, "status": status})
            else:
                failed.append({"slug": target.name, "status": status, "message": f"Unknown publish status: {status}"})
        except json.JSONDecodeError as exc:
            failed.append({"slug": target.name, "status": "invalid-output", "message": f"Invalid publish output: {exc}"})

    print(json.dumps({"dryRun": args.dry_run, "ok": ok, "failed": failed}, indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
