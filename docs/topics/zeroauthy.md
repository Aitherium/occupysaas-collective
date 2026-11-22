# zeroauthy

**A clean-room, Auth0-compatible identity server you can self-host.** Point an
existing Auth0 SDK at a zeroauthy tenant and it works with no code changes.

- Repository: <https://github.com/occupysaas/zeroauthy>
- Pinned here: `projects/zeroauthy`
- Licence: Apache-2.0
- Maintainer: Tom (`thomasmeadows`)

## What it is

zeroauthy is an open-source, self-hostable identity server that speaks the Auth0
Authentication API and Management API. It is an independent implementation built
from public documentation and open standards, not affiliated with Auth0 or Okta.
It also serves as a disposable, Auth0-compatible login server for end-to-end
tests.

## Status

- **1.0 early preview.** It covers what most Auth0 tenants use, but not
  everything. Check the project's
  [compatibility page](https://github.com/occupysaas/zeroauthy/blob/main/docs/compatibility.md)
  for the gaps (WebAuthn and passkeys, SAML, enterprise directories and more)
  before relying on it.
- **OpenID Certified** by the OpenID Foundation (Basic OP, Config OP and Form
  Post OP profiles, October 2026).

## What works in 1.0

- The Authentication API and hosted login: authorization code with PKCE,
  refresh-token rotation, client credentials, password grants, PAR, device flow,
  logout, consent, signup and password reset.
- MFA (one-time passwords, email, SMS, voice, recovery codes) and passwordless
  email and SMS.
- Database, custom database, Google, Microsoft and generic OAuth 2 / OIDC
  connections.
- A Management API for applications, APIs, connections, users, roles,
  organisations, Actions, branding and more.
- An admin console; SQLite, PostgreSQL, MySQL and gRPC storage; verified against
  the common Auth0 SDKs and CLIs.

## Clean room

zeroauthy is a clean-room implementation: it follows the Auth0 public contract
and OpenID standards, never Auth0's source. The authoritative policy is the
project's own
[CLEAN_ROOM.md](https://github.com/occupysaas/zeroauthy/blob/main/CLEAN_ROOM.md).
The umbrella's note is [here](../clean-room/zeroauthy.md).

## Getting started

- [Quickstart](https://github.com/occupysaas/zeroauthy/blob/main/docs/quickstart.md)
  -- container to SDK login
- [Migrating from Auth0](https://github.com/occupysaas/zeroauthy/blob/main/docs/migrating-from-auth0.md)
- [Deployment](https://github.com/occupysaas/zeroauthy/blob/main/docs/deployment.md)
- [Contributing](https://github.com/occupysaas/zeroauthy/blob/main/CONTRIBUTING.md)

## Related decisions

- [ADR-0001](../adr/0001-record-architecture-decisions.md) -- record
  architecture decisions
- [ADR-0002](../adr/0002-umbrella-as-submodules.md) -- the umbrella and its
  submodules
