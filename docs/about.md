# About OccupySaaS

**OccupySaaS** ("Reclaiming the software ecosystem, one open-source project at a
time") is an open-source collective building clean-room, drop-in replacements
for the SaaS giants: software you can self-host, read, and keep.

The premise is compatibility by contract rather than by copy. Each project
re-implements a widely used proprietary service so that existing clients, SDKs
and data continue to work, while the implementation is independently written
from public documentation, open standards, and black-box testing of public
interfaces. Nothing is derived from the original vendor's source.

## What the collective builds

The collective's public projects are listed in the [topics index](topics/index.md):

- **[zeroauthy](topics/zeroauthy.md)** -- an Auth0-compatible, OpenID Certified
  identity server.
- **[salescompel](topics/salescompel.md)** -- a Salesforce-compatible CRM.
- **[website](topics/website.md)** -- the public site at occupysaas.com.

Each is its own repository, its own community, and its own release cadence. This
umbrella pins a commit of each and hosts the knowledge they share.

## How it works

- **Clean room, not a fork.** Compatibility comes from standards and public
  documentation; see each project's clean-room note under
  [`docs/clean-room/`](clean-room/) and its own policy.
- **Maintainers decide their project.** Tom (`thomasmeadows`) maintains the
  projects upstream and is the only person who merges there. A change to a
  project is agreed in that project, not here.
- **The knowledge base is shared.** Cross-project vocabulary and decisions live
  here, so each project does not grow a contradictory half of the same rule. See
  [Governance](topics/governance.md) and the [decision records](adr/index.md).
- **Contributors claim work before starting.** Every substantial change starts
  from an issue; see [How to contribute](topics/contributing.md).

## Where the code is

The projects are hosted under the
[occupysaas](https://github.com/occupysaas) GitHub organisation. This umbrella
mirrors them as submodules under `projects/` so one clone gives you all of them
at known-good commits, plus this knowledge base.

## Licence

Every member project is Apache-2.0 unless its own repository says otherwise.
This umbrella never relicenses a member's code.
