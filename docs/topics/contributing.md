# How to contribute

This is the collective-wide guide. Each project's own `CONTRIBUTING.md` and
clean-room policy are authoritative for that project; read them first.

## Where a change goes

- **Project code, tests or docs** -> that project's repository (under
  `projects/` here, or on GitHub).
- **Knowledge-base pages** (this repository's `docs/`) -> this repository.
- **A decision that spans projects** -> an issue here, recorded as an
  [ADR](../adr/index.md) once agreed.

## Proposing work

1. **Open or find an issue.** State the change and why. Substantial work is
   agreed before it starts, because reviews take time and unmerged effort is
   wasted.
2. **Claim it.** In SalesCompel, comment `claiming` on the plan's `path` issue
   and say so in the community chat; the maintainer confirms or declines. In
   zeroauthy, open an issue or ask the maintainer.
3. **One plan or one bug per pull request.** Do not mix unrelated changes.
4. **Bring a test.** New behaviour comes with a test that fails without it.
5. **Sign off your commits** (`git commit -s`).

## The proposal that started this knowledge base

A shared wiki for the collective was proposed by **Chris** in the OccupySaaS
community. Rather than a separate wiki that drifts from the code, the knowledge
base lives in this repository beside the pinned projects, so a page and the code
it describes move together. Contributions to it follow the same rule as code:
open an issue, agree the change, then send a pull request.

## Clean room

Before contributing to a project, read its clean-room policy. In short:

- Compatibility is established from **public documentation, open standards and
  black-box testing** of public interfaces.
- Do **not** read, copy or derive from the original vendor's proprietary source.
- Where a project permits observing behaviour (for example a firewalled API
  observation against a tenant the observer owns), it records notes in the
  observer's own words, never verbatim vendor text or credentials.

Authoritative policies:

- zeroauthy: [CLEAN_ROOM.md](https://github.com/occupysaas/zeroauthy/blob/main/CLEAN_ROOM.md)
- salescompel: [CLEAN_ROOM.md](https://github.com/occupysaas/salescompel/blob/main/CLEAN_ROOM.md)

## Writing a knowledge-base page

- Link, do not restate: point at the project's own docs for detail that belongs
  there.
- Define a term once in the [glossary](../glossary.md) and link to it.
- Record a cross-project decision as a numbered [ADR](../adr/index.md);
  supersede a decision, never rewrite it.
- Every relative link must resolve; the docs workflow runs `scripts/check_kb.py`.

## Related

- [Governance](governance.md) -- how decisions are made
- [Glossary](../glossary.md) -- shared vocabulary
