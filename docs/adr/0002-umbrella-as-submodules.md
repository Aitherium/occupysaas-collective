# 2. The umbrella holds members as real git submodules

Date: 2026-11-22

## Status

Accepted

## Context

The collective's projects are separate repositories with separate maintainers,
histories and licences. Contributors and newcomers still need one place that
gathers them and explains how they fit together. Copying code into one
repository would fork it, duplicate review, and make it unclear which copy is
canonical; a folder of links is not a repository you can clone and build.

## Decision

This repository is an **umbrella** over the member projects:

- Every member is a **real git submodule** under `projects/`, pinned to an exact
  commit by a gitlink. `.gitmodules` records each project's URL.
- Each member keeps its own repository, history, licence and maintainers.
  Nothing is vendored or relicensed here.
- The umbrella hosts the **shared knowledge base** (`docs/`) that spans the
  projects.
- Pins are bumped deliberately (a reviewed commit, or the weekly bump pull
  request), not by tracking a moving branch.

## Consequences

- `git clone --recurse-submodules` gives a newcomer every project at a
  known-good commit plus the knowledge base.
- A member can evolve on its own; the umbrella only changes when a pin is bumped.
- The knowledge base has one home, so a topic page and the code it describes are
  reviewed together.
- The umbrella adds a pin to keep fresh; the scheduled workflow makes that a
  reviewable pull request rather than silent drift.
