# The tools

| tool | what it is | how to get it |
|---|---|---|
| **awnix** | the immutable base: the aw* tools and, in the ai-full image, a local model sized to the machine. | the WSL one-liner, the ISO, or the AMI builder |
| **awdk** | the agent runtime; provides the `adk` command. | `pip install awdk` |
| **awsh** | the agent shell you type at. | `npm install -g @aitherium/awsh` |
| **awconnect** | the browser extension that puts the collective's assistant in your browser. | Chrome Web Store: https://chromewebstore.google.com/detail/awconnect/peeojgjhjficedkncdejbfnacooodbak |
| **awbonsai** | runs a Bonsai in the visitor's browser on its own GPU; the lightest tier, for a member with no spare box. It does not accept collective work yet. | `npm install @aitherium/awbonsai` |
| **awrelay** | the collective's channel: findings, alerts and work coordination between the fleet's nodes and twins. | `pip install awrelay` |
| **awedgerunner** | the lease and router that runs agent and CI work on edge runners (volunteer GPUs, CI minutes, mesh devices) under a hard budget cap. | bundled with awnix/awdk; it is not yet published as its own package |

awnix also carries the rest of the aw* tools (`awgit`, `awrelay`, `awm`,
`awgraph`, `awembed`, `awdesk` and more). `awkno -k <verb>` lists what is
installed and what each one does.
