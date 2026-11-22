# OccupySaaS knowledge base

The shared knowledge base for the OccupySaaS collective. It is one umbrella over
three independently maintained projects, each pinned here as a git submodule.

The idea of a shared wiki for the collective came from Chris in the OccupySaaS
community; this repository is that wiki, kept next to the code instead of beside
it.

## Start here

- [About OccupySaaS](about.md) -- what the collective is, what it builds, how it
  is funded
- [Topics](topics/index.md) -- one page per project, plus how to contribute and
  how decisions are made
- [Decisions](adr/index.md) -- architecture decision records, numbered and never
  rewritten
- [Glossary](glossary.md) -- shared vocabulary, defined once
- [Contributing](../CONTRIBUTING.md) -- where a change goes and how to propose it

## The projects

| project | what it is | status |
|---|---|---|
| [zeroauthy](topics/zeroauthy.md) | Auth0-compatible identity server | 1.0 early preview; OpenID Certified |
| [salescompel](topics/salescompel.md) | Salesforce-compatible CRM | 0.x early preview in progress |
| [website](topics/website.md) | The public site at occupysaas.com | Live |

## How this repository is organised

```
projects/          each member project as a pinned git submodule
docs/index.md      this page
docs/about.md      what the collective is
docs/topics/       one page per project, plus contributing and governance
docs/adr/          architecture decision records
docs/glossary.md   shared vocabulary
docs/clean-room/   the clean-room boundary per project
scripts/check_kb.py  link checker run by the docs workflow
```

Every claim here is drawn from the projects' public repositories and public
sites. If something drifts, fix the page and link the source.
