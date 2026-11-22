# Contributing to OccupySaaS

## Adding a member project

Members are declared in `AitherOS/config/horizontal_repos/occupysaas.yaml` and appear here as git submodules under `projects/`. Add one with:

```bash
python AitherOS/dev/tools/horizontal_repo_gen.py add AitherOS/config/horizontal_repos/occupysaas.yaml <repo-url> --write
```

Never add a member as a plain directory or a vendored copy. A submodule is what makes the pin auditable: `git submodule status` shows the exact commit each project is at.

## Keeping pins fresh

`sync` resolves each member's configured ref and stages the new gitlink. Review the staged change, run `check`, then commit. The scheduled CI job opens the same change as a pull request.

## Knowledge base conventions

- A topic page per member under `docs/topics/`, linked from its index.
- One architectural decision per ADR under `docs/adr/`, numbered and never rewritten.
- Shared vocabulary in `docs/glossary.md`; a term is defined once and linked thereafter.

## Clean room

Where a member is read as reference for independent work, its clean-room note under `docs/clean-room/` states the boundary. Do not copy code across it.
