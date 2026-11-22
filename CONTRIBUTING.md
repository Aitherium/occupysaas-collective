# Contributing to OccupySaaS

Thanks for helping reclaim the software ecosystem. This repository is the
collective's umbrella and shared knowledge base. Code changes usually belong in
a member project, not here; this page covers both.

## Where a change goes

| you want to | open it in |
|---|---|
| change a project's code, tests or docs | that project's own repository under `projects/` |
| fix or add a knowledge-base page (this repository's `docs/`) | this repository |
| propose a decision that spans projects | an issue here, then an [ADR](docs/adr/index.md) |
| add a project to the collective | an issue here, then a member addition (below) |

Each member project has its own `CONTRIBUTING.md` and its own clean-room policy.
Read them first; they win over anything here.

## Proposing work

1. **Open or find an issue first.** Say what you intend to change and why, so
   effort is not spent on something that cannot merge.
2. **Claim it.** For SalesCompel, comment `claiming` on the plan's `path`
   issue and say so in the community chat; the maintainer confirms or declines.
   For zeroauthy, open an issue or ask the maintainer before a substantial
   change.
3. **One change per pull request.** Keep a plan or a bug in its own PR, with a
   test that fails without the change.
4. **Sign off your commits** (`git commit -s`) and follow the project's
   contribution rules.

The fuller guide is [How to contribute](docs/topics/contributing.md). How the
collective makes decisions is in [Governance](docs/topics/governance.md).

## Adding a member project

A member is a real git submodule pinned to a commit, never a copied directory or
a vendored snapshot. Add one with:

```bash
git submodule add https://github.com/occupysaas/<project>.git projects/<project>
git -C projects/<project> checkout <commit-sha>
git add .gitmodules projects/<project>
git commit
```

Then add a topic page under `docs/topics/`, link it from
[the topics index](docs/topics/index.md), add a clean-room note under
`docs/clean-room/`, and record the project's licence. A member without a
recorded licence cannot be added: the umbrella must be able to honour every
project's terms.

## Keeping pins fresh

A pin is a commit, so it does not move on its own. Bump every pin to its
upstream head, review the staged gitlinks, then commit:

```bash
git submodule update --remote --checkout
git submodule status --recursive
git diff
```

A scheduled workflow opens the same bump as a pull request each week.

## Knowledge-base conventions

- A topic page per member under `docs/topics/`, linked from its index.
- One architectural decision per ADR under `docs/adr/`, numbered and never
  rewritten; supersede, do not edit.
- Shared vocabulary in `docs/glossary.md`; define a term once and link to it.
- Every relative link must resolve. The docs workflow runs
  `scripts/check_kb.py` and fails on a broken link.

## Clean room

Where a project is read as a reference for independent work, its clean-room note
under `docs/clean-room/` states the boundary. Do not copy code across it. The
members' own policies are authoritative:

- zeroauthy: [CLEAN_ROOM.md](https://github.com/occupysaas/zeroauthy/blob/main/CLEAN_ROOM.md)
- salescompel: [CLEAN_ROOM.md](https://github.com/occupysaas/salescompel/blob/main/CLEAN_ROOM.md)
