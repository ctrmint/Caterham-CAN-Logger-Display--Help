#!/usr/bin/env python3
"""Build the help site for GitHub Pages: every markdown file in the repository, as it
is, plus index.json listing them for the dash's HELP screen (Caterham-CAN-Logger-Display
#86, ADR 0008).

    python3 .github/scripts/build_site.py OUT_DIR

index.json: {"version": 1, "files": [{"path": "setup/wifi.md", "title": "...", "size": 1234}, ...]}
- every .md file in every folder (not .github, not OUT_DIR), sorted by path;
- title: the file's first heading ("# Title", or a line underlined with === or ---),
  with inline markers removed; "" if it has none (the dash then shows the path);
- size: bytes.
Only the standard library is used.
"""
import json
import re
import shutil
import sys
from pathlib import Path

ATX = re.compile(r"^ {0,3}(#{1,6})(?:[ \t]+(.*?))?[ \t]*$")
SETEXT = re.compile(r"^ {0,3}(=+|-+)[ \t]*$")


def plain(text):
    """Inline markers removed, escapes resolved, trimmed (as the dash does)."""
    out, i = [], 0
    while i < len(text):
        c = text[i]
        if c == "\\" and i + 1 < len(text):
            out.append(text[i + 1])
            i += 2
            continue
        if c not in "*_`[]":
            out.append(c)
        i += 1
    return "".join(out).strip()


def first_heading(text):
    prev = None
    for line in text.splitlines():
        m = ATX.match(line)
        if m:
            title = re.sub(r"[ \t]+#+$", "", m.group(2) or "").strip()
            title = plain(title)
            if title:
                return title
        elif prev and SETEXT.match(line):
            title = plain(prev)
            if title:
                return title
        prev = line if line.strip() else None
    return ""


def main():
    root = Path(".").resolve()
    out = Path(sys.argv[1]).resolve()
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    files = []
    for p in sorted(root.rglob("*")):
        rel = p.relative_to(root)
        if not p.is_file() or p.suffix.lower() != ".md" or rel.parts[0] in (".git", ".github") or out in p.parents:
            continue
        data = p.read_bytes()
        dest = out / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)   # served as written
        files.append({"path": rel.as_posix(), "title": first_heading(data.decode("utf-8", "replace")), "size": len(data)})
    files.sort(key=lambda f: f["path"])
    (out / "index.json").write_text(json.dumps({"version": 1, "files": files}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (out / ".nojekyll").write_text("")   # served as files, never converted to HTML
    print(f"{len(files)} help files indexed")


if __name__ == "__main__":
    main()
