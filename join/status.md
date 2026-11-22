# See your node, your twin and your credit

## Your node

```bash
adk volunteer status
```

Prints your peer id, your trust state, the lanes you enrolled in, the
collective you registered with, whether the node and twin are recorded, and
the local model size.

## Your twin

If you enrolled the twin lane, the same command shows the twin name and
whether it was registered. A twin is only reachable when its invoke URL is
public (or on the mesh); the enrol step refuses a loopback address.

## Your credit

Work you complete is credited through the platform ledger; `adk wallet` shows
the balance. Credit is platform-driven from usage, never self-reported, so a
zero can also mean nothing has been measured yet rather than that you earned
nothing.

A Discord credit surface is not built yet; the balance lives in `adk wallet`
until it is.

## How work reaches you

The collective does not run your machine directly: a job is placed under a
lease by **awedgerunner**, which delegates to the adapter for the target (the
volunteer node, a CI runner, a mesh device) and ends on expiry or budget. Your
node is one of those targets.

Coordination is on **awrelay**: if enrolment gave a relay channel, the node
posts there and reads it with `awrelay inbox`. That is how the fleet talks to
it and how it reports status; `adk volunteer status` shows the channel.
