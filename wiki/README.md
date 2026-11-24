# The wiki and this repository

The collective's wiki is <https://occupysaas.miraheze.org/>. It is where people
browse and edit. This repository is where the same knowledge is versioned,
reviewed and read by the company brain. `scripts/wiki_sync.py` keeps the two in
step, one direction at a time.

| direction | what moves | credentials | when |
|---|---|---|---|
| wiki -> repo (`mirror`) | every page's wikitext into `wiki/mirror/`, plus `index.json` (last editor, timestamp) | none: the wiki is public | daily from the collective's host (`scripts/wiki_mirror_pr.sh`), as a pull request |
| repo -> wiki (`publish`) | only the markdown files listed in `publish.json` | a bot password | on every push to `main`; dry run on pull requests |

Rules the script enforces:

- `publish` never overwrites a page whose latest revision was made by a person.
  Move the edit into the markdown source, or rerun once with `--force`.
- Published pages start with a comment naming their source file, so an editor
  on the wiki can see where the page really lives.
- Nothing secret goes on the wiki or in this repository. Both are public.

## Turning on publish

1. On the wiki, an administrator opens `Special:BotPasswords`, creates a bot
   named `sync` with the grant "Edit existing pages" and "Create, edit, and move
   pages", and copies the `User@sync` name and the generated password.
2. In this repository's settings, add them as Actions secrets
   `WIKI_BOT_USER` and `WIKI_BOT_PASSWORD`.
3. The next push to `main` publishes. Until then the workflow runs as a dry run.

## Where it runs

Miraheze answers HTTP 403 to GitHub-hosted runners, so the scripts exit 2
(could not judge) there and the workflow reports a warning, never a pass. The
daily mirror and the real publish run on the collective's own host, which the
wiki answers. Any member's machine works the same way:
`bash scripts/wiki_mirror_pr.sh`.

## Run it yourself

```bash
python3 scripts/wiki_sync.py mirror            # refresh wiki/mirror/ locally
python3 scripts/wiki_sync.py publish           # print what would change
python3 -m unittest discover -s scripts -p "test_*.py"  # the tests
```
