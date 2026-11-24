#!/usr/bin/env python3
"""Keep the OccupySaaS wiki and this repository in step.

Two directions, each one safe on its own:

  mirror   wiki -> repo. Reads every page of the public wiki (no credentials) and
           writes its wikitext under wiki/mirror/. A scheduled workflow commits the
           result, so the repo holds a reviewable, diffable copy of the wiki and the
           company brain can read the knowledge base from one place.

  publish  repo -> wiki. Publishes the markdown files listed in wiki/publish.json to
           the wiki pages they name, through a bot account. Dry run unless --apply.
           It refuses to overwrite a page whose latest revision was made by anyone
           but the bot, so hand edits on the wiki are never clobbered: either move
           the edit into the markdown file or pass --force for that run.

Standard library only, plus pandoc on PATH for publish (markdown -> wikitext).

  python3 scripts/wiki_sync.py mirror
  python3 scripts/wiki_sync.py publish                # dry run, prints the plan
  WIKI_BOT_USER=... WIKI_BOT_PASSWORD=... python3 scripts/wiki_sync.py publish --apply
"""
from __future__ import annotations

import argparse
import http.cookiejar
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API = os.environ.get("WIKI_API", "https://occupysaas.miraheze.org/w/api.php")
USER_AGENT = (
    "occupysaas-collective-wiki-sync/0.1 "
    "(https://github.com/Aitherium/occupysaas-collective)"
)
ROOT = Path(__file__).resolve().parent.parent
MIRROR_DIR = ROOT / "wiki" / "mirror"
PUBLISH_MAP = ROOT / "wiki" / "publish.json"
# Namespaces mirrored: main (0), Project (4), Template (10), Help (12), Category (14).
MIRROR_NAMESPACES = (0, 4, 10, 12, 14)
MARKER = "<!-- generated from the occupysaas-collective repo; edit {src} there -->"
UNSAFE = re.compile(r'[<>:"\\|?*\x00-\x1f]')


class WikiRefused(RuntimeError):
    """The wiki answered 403 to this machine (Miraheze refuses some cloud ranges, e.g. CI)."""


class Wiki:
    def __init__(self, api: str = API) -> None:
        self.api = api
        jar = http.cookiejar.CookieJar()
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))

    def call(self, params: dict, post: bool = False) -> dict:
        params = dict(params, format="json", formatversion="2")
        data = urllib.parse.urlencode(params).encode()
        if post:
            req = urllib.request.Request(self.api, data=data)
        else:
            req = urllib.request.Request(self.api + "?" + data.decode())
        req.add_header("User-Agent", USER_AGENT)
        try:
            with self.opener.open(req, timeout=60) as resp:
                body = json.load(resp)
        except urllib.error.HTTPError as exc:
            if exc.code == 403:
                raise WikiRefused("the wiki refused this machine (HTTP 403)") from exc
            raise
        if "error" in body:
            raise RuntimeError("wiki API error: %s" % body["error"])
        return body

    def all_titles(self, namespace: int) -> list[str]:
        titles, cont = [], {}
        while True:
            body = self.call(dict(action="query", list="allpages", apnamespace=namespace,
                                  aplimit="max", **cont))
            titles += [p["title"] for p in body["query"]["allpages"]]
            if "continue" not in body:
                return titles
            cont = body["continue"]

    def latest(self, titles: list[str]) -> dict[str, dict]:
        """title -> {text, user, timestamp}; a missing page maps to {}."""
        out: dict[str, dict] = {}
        for i in range(0, len(titles), 50):
            body = self.call(dict(action="query", prop="revisions", titles="|".join(titles[i:i + 50]),
                                  rvprop="content|user|timestamp", rvslots="main"))
            for page in body["query"]["pages"]:
                if page.get("missing") or not page.get("revisions"):
                    out[page["title"]] = {}
                    continue
                rev = page["revisions"][0]
                out[page["title"]] = {"text": rev["slots"]["main"]["content"],
                                      "user": rev["user"], "timestamp": rev["timestamp"]}
        return out

    def login(self, user: str, password: str) -> None:
        token = self.call(dict(action="query", meta="tokens", type="login"))["query"]["tokens"]["logintoken"]
        body = self.call(dict(action="login", lgname=user, lgpassword=password, lgtoken=token), post=True)
        if body.get("login", {}).get("result") != "Success":
            raise RuntimeError("bot login failed: %s" % body.get("login", {}).get("reason", body))

    def edit(self, title: str, text: str, summary: str) -> dict:
        token = self.call(dict(action="query", meta="tokens"))["query"]["tokens"]["csrftoken"]
        return self.call(dict(action="edit", title=title, text=text, summary=summary,
                              bot="1", token=token), post=True)


def title_to_path(title: str) -> Path:
    """'Company Brain/Approvals' -> wiki/mirror/Company Brain/Approvals.wiki (Windows-safe)."""
    parts = [UNSAFE.sub(lambda m: "%%%02X" % ord(m.group()), p).rstrip(" .") or "_"
             for p in title.split("/")]
    return MIRROR_DIR.joinpath(*parts).with_suffix(".wiki")


def mirror(wiki: Wiki) -> int:
    titles = [t for ns in MIRROR_NAMESPACES for t in wiki.all_titles(ns)]
    pages = wiki.latest(titles)
    written = set()
    for title, rev in sorted(pages.items()):
        if not rev:
            continue
        path = title_to_path(title)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(rev["text"].rstrip("\n") + "\n", encoding="utf-8", newline="\n")
        written.add(path)
    stale = [p for p in MIRROR_DIR.rglob("*.wiki") if p not in written]
    for p in stale:
        p.unlink()
    index = {t: {"file": title_to_path(t).relative_to(ROOT).as_posix(),
                 "user": r["user"], "timestamp": r["timestamp"]}
             for t, r in sorted(pages.items()) if r}
    (MIRROR_DIR / "index.json").write_text(json.dumps(index, indent=1) + "\n",
                                           encoding="utf-8", newline="\n")
    print("mirrored %d page(s), removed %d stale file(s)" % (len(index), len(stale)))
    return 0 if index else 2


def to_wikitext(md_path: Path) -> str:
    try:
        out = subprocess.run(["pandoc", "--from=gfm", "--to=mediawiki", str(md_path)],
                             check=True, capture_output=True, text=True)
    except FileNotFoundError:
        raise SystemExit("pandoc is not on PATH (publish needs it; mirror does not)")
    src = md_path.relative_to(ROOT).as_posix()
    return MARKER.format(src=src) + "\n" + out.stdout


def plan_publish(entries: list[dict], current: dict[str, dict], bot: str) -> list[tuple[str, str, str]]:
    """Return (title, source, verdict) per entry. verdict: create | update | same | refuse."""
    plan = []
    for e in entries:
        rev = current.get(e["title"], {})
        if not rev:
            verdict = "create"
        elif rev["text"].strip() == e["text"].strip():
            verdict = "same"
        elif bot and rev["user"].split("@")[0] == bot.split("@")[0]:
            verdict = "update"
        else:
            verdict = "refuse"
        plan.append((e["title"], e["source"], verdict))
    return plan


def publish(wiki: Wiki, apply: bool, force: bool) -> int:
    mapping = json.loads(PUBLISH_MAP.read_text(encoding="utf-8"))
    entries = []
    for item in mapping["pages"]:
        src = ROOT / item["source"]
        if not src.is_file():
            print("missing source: %s" % item["source"])
            return 1
        entries.append({"title": item["title"], "source": item["source"], "text": to_wikitext(src)})
    bot = os.environ.get("WIKI_BOT_USER", "")
    current = wiki.latest([e["title"] for e in entries])
    plan = plan_publish(entries, current, bot)
    for title, src, verdict in plan:
        print("%-8s %s <- %s" % (verdict, title, src))
    refused = [p for p in plan if p[2] == "refuse"]
    if refused and not force:
        print("%d page(s) were last edited by a person on the wiki; move those edits into the "
              "markdown source, or rerun with --force" % len(refused))
    if not apply:
        print("dry run: nothing written (pass --apply with WIKI_BOT_USER/WIKI_BOT_PASSWORD set)")
        return 1 if refused and not force else 0
    password = os.environ.get("WIKI_BOT_PASSWORD", "")
    if not bot or not password:
        print("--apply needs WIKI_BOT_USER and WIKI_BOT_PASSWORD (a Special:BotPasswords pair)")
        return 2
    wiki.login(bot, password)
    texts = {e["title"]: e["text"] for e in entries}
    for title, src, verdict in plan:
        if verdict in ("create", "update") or (verdict == "refuse" and force):
            wiki.edit(title, texts[title], "sync from occupysaas-collective: %s" % src)
            print("wrote    %s" % title)
    return 1 if refused and not force else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("mirror", help="wiki -> wiki/mirror/ (read-only, no credentials)")
    pub = sub.add_parser("publish", help="wiki/publish.json markdown -> wiki pages")
    pub.add_argument("--apply", action="store_true", help="write to the wiki (default: dry run)")
    pub.add_argument("--force", action="store_true", help="overwrite pages a person edited last")
    args = ap.parse_args(argv)
    wiki = Wiki()
    try:
        if args.cmd == "mirror":
            return mirror(wiki)
        return publish(wiki, args.apply, args.force)
    except WikiRefused as exc:
        # 2 = could not judge: not a pass, not a content failure.
        print("%s; run this from a machine the wiki answers (see wiki/README.md)" % exc)
        return 2


if __name__ == "__main__":
    sys.exit(main())
