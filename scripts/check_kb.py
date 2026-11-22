#!/usr/bin/env python3
"""Fail when a relative markdown link under docs/ does not resolve."""
import re
import sys
from pathlib import Path

LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
SKIP = ("http://", "https://", "mailto:", "#")


def main(root=Path("docs")) -> int:
    bad = 0
    for md in sorted(root.rglob("*.md")):
        for raw in LINK.findall(md.read_text(encoding="utf-8")):
            if raw.startswith(SKIP):
                continue
            target = raw.split("#", 1)[0]
            if not target:
                continue
            if not (md.parent / target).resolve().exists():
                print("%s: broken link -> %s" % (md, raw))
                bad += 1
    if bad:
        print("%d broken link(s)" % bad)
        return 1
    print("knowledge base links resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main())
