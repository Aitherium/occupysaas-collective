# Clean-room note: zeroauthy

zeroauthy is an independent, clean-room implementation of an identity server
that is wire-compatible with Auth0. This umbrella links it as the submodule
`projects/zeroauthy` under Apache-2.0; it never copies, vendors or relicenses
any of its code.

## The boundary

- **Permitted sources** include Auth0's public documentation, its public
  changelog (used to plan parity, summarised in the project's own words), open
  standards (IETF RFCs, OpenID specifications), and open-source Auth0 SDKs and
  tools under their own licences.
- **The original proprietary source is never read, copied or derived from.**
- **Firewalled observation** of the Management API is permitted only against a
  tenant the observer owns, with separate observer and implementer roles, and
  notes written in the observer's own words without credentials, tenant
  identifiers or personal data.

The operator defines the policy; the project's own file is authoritative:

- [zeroauthy CLEAN_ROOM.md](https://github.com/occupysaas/zeroauthy/blob/main/CLEAN_ROOM.md)

## In this umbrella

- Topic page: [zeroauthy](../topics/zeroauthy.md)
- Entry: [glossary](../glossary.md)
