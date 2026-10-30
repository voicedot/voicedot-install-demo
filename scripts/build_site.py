"""Build the tiny static site without third-party dependencies."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import shutil


def build(commit: str) -> Path:
    if not re.fullmatch(r"[a-f0-9]{40}", commit):
        raise ValueError("Expected an exact lowercase 40-character Git commit")
    root = Path(__file__).resolve().parents[1]
    source = root / "site"
    output = root / "dist"
    if not (source / "index.html").is_file():
        raise ValueError("Missing site/index.html")
    # Only this script's generated output directory is replaced.
    if output.is_symlink():
        raise ValueError("Refusing a symlink output directory")
    if output.exists():
        shutil.rmtree(output)
    shutil.copytree(source, output)
    (output / ".nojekyll").touch()
    (output / "deployment.json").write_text(json.dumps({
        "commit": commit,
        "branch": "main",
        "builtAt": datetime.now(timezone.utc).isoformat(),
    }, indent=2) + "\n")
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit", required=True)
    args = parser.parse_args()
    print(build(args.commit))
