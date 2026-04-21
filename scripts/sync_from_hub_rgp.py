"""Sync skills/ + .claude-plugin/ from the private hub-rgp repo.

Authoritative content for the 13 RGP skills lives in the private
`eldeebbomar/hub-rgp` repo at `skills/<slug>/SKILL.md`. This public
`rgp-skills` repo mirrors those files so the team can install via
`/plugin marketplace add eldeebbomar/rgp-skills`.

This script:
  1. Shallow-clones hub-rgp into a temp directory.
  2. Rsync-copies `skills/` and `.claude-plugin/` into this repo.
  3. Deletes `skills/_build_migration.py` (hub-rgp infra, not needed here).

Run locally:
    GITHUB_TOKEN=<pat> python scripts/sync_from_hub_rgp.py

GITHUB_TOKEN must be a PAT with read access to eldeebbomar/hub-rgp.
Inside the sync GitHub Action the token is passed as HUB_RGP_READ_TOKEN.

After running, commit and push:
    git add skills/ .claude-plugin/
    git commit -m "sync: pull latest skills from hub-rgp"
    git push origin main
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
HUB_RGP = "eldeebbomar/hub-rgp"
FOLDERS_TO_SYNC = ("skills", ".claude-plugin")
FILES_TO_REMOVE_POST_SYNC = ("skills/_build_migration.py",)


def run(cmd: list[str], cwd: Path | None = None, env: dict | None = None) -> None:
    print(f"$ {' '.join(cmd)}")
    subprocess.run(cmd, cwd=cwd, env=env, check=True)


def main() -> int:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("HUB_RGP_READ_TOKEN")
    if not token:
        print(
            "ERROR: set GITHUB_TOKEN (or HUB_RGP_READ_TOKEN) to a PAT with\n"
            f"       read access to the private {HUB_RGP} repo.",
            file=sys.stderr,
        )
        return 2

    clone_url = f"https://x-access-token:{token}@github.com/{HUB_RGP}.git"

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp) / "hub-rgp"
        run(
            ["git", "clone", "--depth", "1", clone_url, str(tmp_path)],
            env={**os.environ, "GIT_TERMINAL_PROMPT": "0"},
        )

        for folder in FOLDERS_TO_SYNC:
            src = tmp_path / folder
            dst = REPO / folder
            if not src.exists():
                print(f"WARN: {folder} missing in hub-rgp, skipping", file=sys.stderr)
                continue
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
            print(f"  ← {folder}/ ({sum(1 for _ in dst.rglob('*'))} entries)")

    for rel in FILES_TO_REMOVE_POST_SYNC:
        target = REPO / rel
        if target.exists():
            target.unlink()
            print(f"  - removed {rel} (hub-rgp-only infra)")

    print("\nDone. Review with `git status`, then:")
    print("  git add skills/ .claude-plugin/")
    print("  git commit -m 'sync: pull latest skills from hub-rgp'")
    print("  git push origin main")
    return 0


if __name__ == "__main__":
    sys.exit(main())
