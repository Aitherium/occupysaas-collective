# Linux: install awnix

Your distribution should be a current, systemd-based one. awnix is immutable
and adds the aw* tools; your own packages stay where they are.

## 1. Install awnix

```bash
curl -fsSL https://raw.githubusercontent.com/Aitherium/awnix/main/install.sh | sudo sh
```

Prefer a sealed image? Use the [spare-box ISO path](spare-box.md).

## 2. Sign in and enrol

```bash
adk login
adk volunteer enroll --lane embed,bonsai --collective occupysaas --relay-channel '#occupysaas'
```

## 3. Serve

```bash
adk volunteer serve --lane bonsai
adk volunteer start --lane embed
```

## Or run the bootstrap script

```bash
./bootstrap.sh           # prints the plan; runs nothing
./bootstrap.sh --yes     # runs the published installers and adk
```
