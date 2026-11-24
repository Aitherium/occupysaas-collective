# OccupySaaS

**Reclaiming the software ecosystem, one open-source project at a time.**

OccupySaaS builds clean-room, open-source, drop-in replacements for the SaaS
giants. This repository is the collective's umbrella: it gathers each project as a
real git submodule and hosts the shared knowledge base for all of them. Every
project stays its own repository with its own history, licence and maintainers;
this repository pins an exact commit of each.

## Members

| project | what it is | path | licence |
|---|---|---|---|
| [zeroauthy](https://github.com/occupysaas/zeroauthy) | Self-hostable, Auth0-compatible identity server (OpenID Certified) | `projects/zeroauthy` | Apache-2.0 |
| [salescompel](https://github.com/occupysaas/salescompel) | Salesforce-compatible CRM, built as a Go/PostgreSQL service with a Vue UI | `projects/salescompel` | Apache-2.0 |
| [website](https://github.com/occupysaas/website) | The public site at occupysaas.com (static HTML/CSS/JS) | `projects/website` | Apache-2.0 |

Pinned commits are recorded in `.gitmodules` and the gitlinks under `projects/`.

## Knowledge base

Start at [docs/index.md](docs/index.md). It links every topic, the decision
records and the shared glossary:

- [About OccupySaaS](docs/about.md) -- what the collective is and how it works
- [Topics](docs/topics/index.md) -- one page per project, plus how to contribute
- [Decisions](docs/adr/index.md) -- architecture decision records
- [Glossary](docs/glossary.md) -- shared vocabulary
- [The wiki](https://occupysaas.miraheze.org/) -- where people browse and edit; [wiki/README.md](wiki/README.md) says how it and this repository stay in step

## Get it working

```bash
git clone --recurse-submodules https://github.com/Aitherium/occupysaas-collective.git
cd occupysaas-collective
git submodule status --recursive
```

Without `--recurse-submodules`, run `git submodule update --init --recursive`
after cloning.

## Run an agent for the collective

A machine you control can serve this collective as a node: embeddings, a local
Bonsai model, a managed twin the collective can dispatch work to, or CI for
public repositories. Start at **[join/index.md](join/index.md)**. It has one guide
per platform (Windows WSL, Linux, a spare box via the ISO, AWS, or the browser for a
member with no spare box), a hardware-to-model table, a status page for your node,
twin and credit, and a bootstrap script per OS that prints its plan and runs nothing
until you say yes.

The tools it uses:

- **awnix** -- the immutable base OS with the aw* tools and a model sized to your
  machine (the WSL one-liner, the ISO, or the AMI builder).
- **awdk** -- the agent runtime, which provides the `adk` command: `pip install awdk`.
- **awsh** -- the agent shell: `npm install -g @aitherium/awsh`.
- **awconnect** -- the browser extension that puts the assistant in your browser,
  from the [Chrome Web Store](https://chromewebstore.google.com/detail/awconnect/peeojgjhjficedkncdejbfnacooodbak).
- **awbonsai** -- runs a Bonsai in the visitor's browser on its own GPU; the lightest
  tier, for a member with no spare box (`npm install @aitherium/awbonsai`). It is an
  inference library, not a work queue: it does not accept collective work yet.
- **awrelay** -- the collective's channel for findings, alerts and work coordination
  (`pip install awrelay`). Enrolment subscribes the node to it.
- **awedgerunner** -- the lease and router that runs agent and CI work on edge
  runners (volunteer GPUs, CI minutes, mesh devices) under a hard budget cap. It
  ships in-tree with awnix/awdk and is not yet its own published package.

Enrolment is fail-closed: the node records your consent, an operator raises its
trust tier, and nothing is routed before both are true.

## Keeping pins fresh

A member is pinned to a commit, not to a moving branch, so a build is
reproducible. Bump every pin to the current upstream head with:

```bash
git submodule update --remote --checkout
```

Review the staged gitlinks, commit them and open a pull request. A scheduled
workflow opens the same bump as a pull request each week.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) and each project's own contribution
rules before opening a pull request. Each project carries a clean-room policy
that every contribution must follow.

## Licence

Apache-2.0. Each member keeps its own licence; this repository never relicenses
a submodule's code. Homepage: <https://occupysaas.com>.
