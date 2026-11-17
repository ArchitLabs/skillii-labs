"""Refuse to commit anything shaped like an API key or an account id. Run by the pre-commit hook and in CI."""
import re
import subprocess
import sys

PATTERNS = [
    re.compile(r"sk-ant-[A-Za-z0-9_-]{8,}"),
    re.compile(r"sk-(?:proj-)?[A-Za-z0-9_-]{16,}"),
    re.compile(r"\b(?:org|proj|user|acct|ws|req|msg|toolu)[-_][A-Za-z0-9]{8,}"),
    re.compile(r"Bearer\s+[A-Za-z0-9._-]{12,}"),
]


def files(staged: bool) -> list[str]:
    cmd = ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"] if staged else ["git", "ls-files"]
    return [f for f in subprocess.run(cmd, capture_output=True, text=True).stdout.split() if f]


def main() -> int:
    bad = []
    for f in files("--staged" in sys.argv):
        try:
            text = open(f, encoding="utf-8").read()
        except (OSError, UnicodeDecodeError):
            continue
        for p in PATTERNS:
            for m in p.finditer(text):
                bad.append(f"{f}: {m.group(0)[:12]}…")
    for b in bad:
        print(f"secret-shaped text: {b}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
