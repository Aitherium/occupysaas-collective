# No spare box: the browser tier

A machine that can run a modern browser can run Bonsai, on the tab's own GPU,
with no install and no account. This is the lightest tier, and it is real: the
model loads once and answers locally.

```bash
npm install @aitherium/awbonsai
```

```js
import { isSupported, grantBonsaiConsent, loadModel } from '@aitherium/awbonsai'
const report = await isSupported()   // downloads nothing
if (report.supported) grantBonsaiConsent(false)  // your UI asks first
const model = await loadModel('bonsai-1.7b')
```

The model sizes are the same table as the machine tiers, but the browser
engine supports the 1.7B, the 4B, the 27B and Bonsai 2 27B; the Bonsai 2
2B/4B/9B are self-host only.

## What this tier does not do yet

Awbonsai is an inference library, not a work queue: it has no hook that lets
the collective push a job into a tab. It serves YOUR use in that tab, and it
is registered as a node, but it does not accept collective work. That is why
the lane is marked non-dispatching. Claiming otherwise would be the kind of
silent lie the fail-closed gates exist to prevent.

If you do have a spare box, use a machine tier: it can accept work today.
