# Clean-room note: salescompel

SalesCompel is an independent implementation intended to be compatible with
Salesforce clients, data and customisations. This umbrella links it as the
submodule `projects/salescompel` under Apache-2.0; it never copies, vendors or
relicenses any of its code.

## The boundary

SalesCompel uses **black-box testing** rather than a personnel-separated
clean-room process:

- **Test only what you are authorised to test.** Use Salesforce organisations the
  maintainer owns or authorises -- disposable trials, Developer Edition orgs and
  sandboxes -- with synthetic data and unmodified public clients.
- **Do not inspect or derive from proprietary Salesforce internals.** Describe
  observed behaviour independently: inputs, status and error codes, field types,
  defaults, ordering, pagination, permissions and effects.
- **Record provenance.** Note the profile, API and client versions, capture
  dates and reproduction steps; distinguish observed behaviour from assumptions.
- **Keep secrets and personal data out** of published notes and reports.

The operator defines the policy; the project's own file is authoritative:

- [salescompel CLEAN_ROOM.md](https://github.com/occupysaas/salescompel/blob/main/CLEAN_ROOM.md)

## In this umbrella

- Topic page: [salescompel](../topics/salescompel.md)
- Entry: [glossary](../glossary.md)
