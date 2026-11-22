# Join the OccupySaaS fleet

Turn a machine you control into a node the collective can use. Pick the
path that matches what you have; every path ends in the same commands.

| you have | start here |
|---|---|
| Windows 10/11 | [Windows (WSL)](windows-wsl.md) |
| a Linux box | [Linux](linux.md) |
| a spare PC | [Boot the ISO](spare-box.md) |
| an AWS account | [AWS](aws-ami.md) |

## The path is the same everywhere

1. Install **awnix** -- the base OS with the aw* tools and, in the ai-full
   image, a local model sized to your machine.
2. Sign in: `adk login`.
3. Enrol and register with the collective:
   ```bash
   adk volunteer enroll --lane embed,bonsai --collective occupysaas
   ```
4. Serve what you chose:
   ```bash
   adk volunteer serve --lane bonsai   # 127.0.0.1:8199
   adk volunteer start --lane embed
   ```

Enrolment is fail-closed. Nothing is routed until you record consent and an
operator raises your peer's trust tier; a lane that needs trust says so
instead of pretending to serve. `adk volunteer lanes` prints the menu.

The bootstrap scripts print a plan first and run nothing until you pass
`-Yes` (Windows) or `--yes` (Linux).

More: [hardware and model sizes](hardware.md) - [see your node, twin and credit](status.md) - [the tools](tools.md)
