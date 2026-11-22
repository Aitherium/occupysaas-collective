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

## Get it working

```bash
git clone --recurse-submodules https://github.com/Aitherium/occupysaas-collective.git
cd occupysaas-collective
git submodule status --recursive
```

Without `--recurse-submodules`, run `git submodule update --init --recursive`
after cloning.

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
