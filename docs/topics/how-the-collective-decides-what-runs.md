# How the collective decides what runs

Collective jobs run on hardware that members volunteer: CPU, GPU, RAM and
storage lent by people, not bought by the hub. Because a collective job
spends someone else's machine, it is not enough for one person to want it
run. Two independent gates must both pass before any collective job starts.

## Gate 1: council review

A named council reviews the job specification. The council has a fixed set
of seats, and a job needs a configured minimum number of approving seats
(K of N). Each seat records its own approval or rejection with a reason.
A council that falls short of K cannot approve a job, no matter how popular
it is.

## Gate 2: community vote

Enrolled members then vote yes, no, or abstain. The vote must reach a
turnout quorum: a minimum number of members must actually show up, scaled
to the size of the enrolled membership. Among the votes cast, the yes share
must reach a passing threshold.

Votes are weighted, with a one-member base vote plus capped weight from
contribution credit and reputation. The base vote means every enrolled
member counts. The caps mean contribution cannot buy the outcome. Every
weight and cap is configuration set by the operator, not a constant in the
code.

## The approval becomes a permit

Passing both gates does not leave a job "approved" in a database that any
script can claim. It mints a signed permit. The permit names the exact job
specification by hash, its resource and cost ceilings, and an expiry. A
permit for one specification cannot run a different one, cannot run past
its expiry, and cannot exceed its caps.

## Admission

The compute queue and the edge-runner dispatcher check the permit before a
collective job is queued or charged. A collective job without a valid
permit is refused, and the refusal names the specification hash and where
to propose it. Hub-internal work, which does not use member resources, is
not subject to this gate.

## Bad actors and broken workers

Members lend hardware, so the collective assumes some workers can be wrong
or hostile. Two rules bound that.

Enrolment is attested. A node may join only while it runs a signed image:
the hub verifies the image digest with cosign against the known signer,
and requires the agent tools at pinned versions. The check is repeated on
a schedule. A modified worker does not have a verified digest to show.

Work is replicated. Deterministic jobs (builds, embeddings with a fixed
model, quantisation, seeded runs) go to at least 3f+1 independent nodes
run by different operators. A result is accepted only when 2f+1 nodes
agree on the same signed output hash. A node that disagrees is
quarantined, loses reputation and the credit for that unit, and is
revoked if it repeats. Non-deterministic model work cannot agree on a
hash, so the hub re-executes a sample of it and a judge decides whether
the outputs are equivalent.

Redundancy costs compute: deterministic work is multiplied by the
replication factor, and judged work by one plus the sampling rate. The
proposal records that trade-off. The fault tolerance, replication and
sampling numbers are set by the operator in the governance
configuration.

## Bootstrap and audit

While the collective is bootstrapping, a founder veto can stop a proposal
until a fixed expiry date. After that date the veto has no effect. Every
proposal, council vote, community vote, tally, veto and permit is appended
to a tamper-evident audit log.

## Proposing a job

A proposal states what the job does, which public repository it uses, the
CPU/GPU/RAM/duration it needs, and how it handles data. Repositories used on
member runners must be public. Proposals are opened at the collective
proposal page; the same page shows the current council, quorum and caps.

