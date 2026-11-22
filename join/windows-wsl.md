# Windows: run awnix in WSL

## 1. Install awnix

```powershell
irm https://raw.githubusercontent.com/Aitherium/awnix/main/.DEPLOYMENT/standalone/bootc/install-awnix-wsl.ps1 | iex
```

The image is pulled anonymously. Expect about 2 GB of download and 10 GB of
free disk. First boot runs `awnix-setup` (hostname, an administrator account,
optional extras, an optional link to your fleet); every question is
skippable and the box is fully usable without linking.

## 2. Sign in

```bash
adk login
```

This is the account the collective sees. Consent and trust are
authenticated, so there is no anonymous path.

## 3. Enrol

```bash
adk volunteer enroll --lane embed,bonsai --collective occupysaas
```

A lane that needs operator trust records the request and tells you it is
pending; it does not claim the node is serving.

## 4. Serve

```bash
adk volunteer serve --lane bonsai   # sized and served on 127.0.0.1:8199
adk volunteer start --lane embed
```

## Or run the bootstrap script

```powershell
./bootstrap.ps1          # prints the plan; runs nothing
./bootstrap.ps1 -Yes     # runs the published installers and adk
```

## Check it

`adk volunteer status` prints your peer, trust, lanes, collective and twin.
