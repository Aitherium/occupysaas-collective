# Glossary

Define a term once, here, and link to it everywhere else.

| term | meaning |
|---|---|
| umbrella | this repository: several projects as submodules plus their shared knowledge base |
| member | one upstream project pinned here as a git submodule |
| pin | the exact commit a submodule gitlink records; it does not move on its own |
| submodule | a git repository embedded at a path in another repository, recorded as a gitlink to one commit |
| clean room | building compatible software from public documentation and standards, without reading or copying the original vendor's source |
| black-box testing | establishing behaviour only by exercising public interfaces and observing results, not by inspecting an implementation |
| drop-in replacement | software that existing clients can switch to by changing configuration, not code |
| compatibility / parity | how much of the original service's observable behaviour a replacement reproduces |
| tenant | one isolated customer space inside a multi-tenant service |
| OIDC | OpenID Connect, an identity layer on OAuth 2.0; zeroauthy is an OpenID Certified provider |
| SOQL | Salesforce Object Query Language, the query language salescompel reimplements |
| ADR | architecture decision record: a numbered, never-rewritten note of a cross-project decision |

## See also

- [Topics](topics/index.md) -- one page per project
- [Decision records](adr/index.md)
