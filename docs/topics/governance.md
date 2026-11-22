# Governance

OccupySaaS is a small, maintainer-led open-source collective. This page states
how decisions are made, so contributors know where to take a proposal and who
decides.

## Who decides

- **Each project has a maintainer.** Tom (`thomasmeadows`) maintains zeroauthy
  and salescompel upstream and is the only person who merges there. A project's
  direction and its merges are his call.
- **Cross-project decisions** are recorded in this repository as
  [architecture decision records](../adr/index.md). They exist so that one
  project does not grow half of a rule that contradicts another project.
- **Knowledge-base changes** are ordinary pull requests to this repository: an
  issue, a reviewed change, a merge.

## How to raise something

1. **A bug or a small improvement in one project** -> that project's issue
   tracker.
2. **A larger change in one project** -> an issue there first; claim it if the
   project organises work as claimable plans (SalesCompel does).
3. **A decision that touches more than one project** -> an issue here. When it
   is agreed, write it as an ADR and link it from the projects it affects.
4. **A new project for the collective** -> an issue here proposing it, with its
   licence and maintainer. It is added as a submodule once accepted; see
   [How to contribute](contributing.md).

## What an agreement looks like

- **Silence is not agreement.** A change is agreed when the maintainer says so on
  the issue or pull request, or when a review approves it.
- **Tests and a clean-room check are part of agreement**, not an afterthought: a
  change that cannot demonstrate its behaviour, or that breaks a project's
  clean-room policy, is not ready.
- **Decisions that span projects are written down.** An unwritten decision is a
  conversation; an ADR is the record later contributors can rely on.

## Changing these rules

This page and the [decision records](../adr/index.md) change by pull request,
like everything else. If a rule is wrong, open an issue and propose the change.
