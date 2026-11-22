# OccupySaaS

OccupySaaS -- one umbrella repository that gathers its member projects as REAL git submodules and hosts the shared knowledge base for all of them. Every member stays its own repository with its own history, licence and maintainers; this repository pins a commit of each.

## Members

| project | path | ref | licence |
|---|---|---|---|
| [zeroauthy](https://github.com/occupysaas/zeroauthy) | `projects/zeroauthy` | `5cf04cfac9f47d3fc2993c3ce2e14f0d2bf54c56` | Apache-2.0 |
| [salescompel](https://github.com/occupysaas/salescompel) | `projects/salescompel` | `9a8a8cec74e9da75f95a906016df84696b8fd9b4` | Apache-2.0 |
| [website](https://github.com/occupysaas/website) | `projects/website` | `5ba0a2db0a09f0100f6bbbcd8a11373cc74b9d40` | Apache-2.0 |

## Knowledge base

Start at [docs/index.md](docs/index.md). Topics live in [`docs/topics`](docs/topics/), decisions in [`docs/adr`](docs/adr/) and shared vocabulary in [`docs/glossary.md`](docs/glossary.md).

## Get it working

```bash
git clone --recurse-submodules https://github.com/Aitherium/occupysaas.git
cd occupysaas
git submodule status --recursive
```

Bump every submodule to its configured ref with `python AitherOS/dev/tools/horizontal_repo_gen.py sync occupysaas.yaml --write` from the AitherOS monorepo, or `git submodule update --remote --checkout` by hand.

## Licence

Apache-2.0. Each member keeps its own licence; this repository never relicenses a submodule's code. Homepage: https://occupysaas.com.
