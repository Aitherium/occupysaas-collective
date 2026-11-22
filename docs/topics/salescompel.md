# salescompel

**An open-source, free-to-use Salesforce replacement.** An initial
tenant-isolated Go/PostgreSQL service with a Vue record workflow, aiming at a
Salesforce-compatible API that standard clients can use.

- Repository: <https://github.com/occupysaas/salescompel>
- Pinned here: `projects/salescompel`
- Licence: Apache-2.0
- Maintainer: Tom (`thomasmeadows`)

## What it is

SalesCompel is a clean-room, black-box reimplementation of Salesforce: the same
organisation, object, permission and API model, written from public interfaces
and documented behaviour rather than from Salesforce internals. The early
candidate is a tenant-isolated Go/PostgreSQL service; a Vue prototype explores
Account and Contact lists, details and create/edit flows with synthetic data.

## Status

The near-term goal is a **`0.x` early preview** for new teams and simple
Salesforce orgs: a working sales CRM with a Salesforce-compatible API and an
import with a dry-run report naming what will not carry over. Apex, Flow and
custom UI (LWC, Aura, Visualforce) are excluded from that first release.

The project tracks its longer-term certification milestones (M0-M10) in its
repository. Completed work includes the compatibility laboratory, a Go/PostgreSQL
walking slice, an accepted reference baseline, bounded metadata/catalog work, and
the early UI prototype. No full program milestone has a recorded exit-gate pass
yet.

## How work is organised

SalesCompel runs on **parallel work paths**: each remaining item is one-page
brief with an open GitHub issue labelled `path`. Two people never build the same
thing, and nothing starts before what it depends on has merged. The live status
is always the issue list.

- [Parallel work paths](https://github.com/occupysaas/salescompel/blob/main/docs/paths/README.md)
- [First-release roadmap](https://github.com/occupysaas/salescompel/blob/main/docs/superpowers/specs/2026-11-04-salescompel-first-release-roadmap-design.md)

## Clean room

SalesCompel uses **black-box testing**: compatibility comes from exercising
public interfaces and independently implementing observable behaviour. The
authoritative policy is the project's own
[CLEAN_ROOM.md](https://github.com/occupysaas/salescompel/blob/main/CLEAN_ROOM.md).
The umbrella's note is [here](../clean-room/salescompel.md).

## Contributing

Claim a plan's issue with a `claiming` comment before you start; one plan or one
bug per pull request; a test for new behaviour; sign off every commit. See the
project's
[CONTRIBUTING.md](https://github.com/occupysaas/salescompel/blob/main/CONTRIBUTING.md).

## Related decisions

- [ADR-0002](../adr/0002-umbrella-as-submodules.md) -- the umbrella and its
  submodules
