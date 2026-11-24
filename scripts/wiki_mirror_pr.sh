#!/usr/bin/env bash
# Mirror the wiki into wiki/mirror/ and open or update the `wiki-mirror` pull request.
# Needs git push rights and an authenticated `gh`. Run from a clone of this repo on a
# machine the wiki answers (Miraheze returns 403 to GitHub-hosted runners).
set -euo pipefail
cd "$(dirname "$0")/.."
# python3 on Windows is often the Store stub; fall back to python.
PY="${PYTHON:-}"
if [ -z "$PY" ]; then if python3 -c "" 2>/dev/null; then PY=python3; else PY=python; fi; fi
git fetch -q origin main
git checkout -q -B wiki-mirror origin/main
"$PY" scripts/wiki_sync.py mirror
git add -A wiki/mirror
if git diff --cached --quiet; then echo "wiki unchanged"; exit 0; fi
git -c user.name=wiki-mirror -c user.email=wiki-mirror@users.noreply.github.com \
  commit -q -m "wiki: mirror pages from occupysaas.miraheze.org"
git fetch -q origin wiki-mirror 2>/dev/null || true
git push -q --force-with-lease origin wiki-mirror
gh pr view wiki-mirror >/dev/null 2>&1 || gh pr create --head wiki-mirror --base main \
  --title "wiki: mirror pages from the wiki" \
  --body "Daily copy of https://occupysaas.miraheze.org/ (scripts/wiki_mirror_pr.sh). The diff is what changed on the wiki."
