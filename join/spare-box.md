# A spare box: boot the ISO

Use this when you have a whole machine to give the collective, or when you
want an image that cannot drift from the one everyone else runs.

## 1. Write the image

Download [awnix-ai-full](https://artifact.aitherium.com/awnix-ai-full-x86_64.iso) (~the current ai-full build). Write it to a USB stick with your usual
tool, then boot the machine from it.

## 2. First boot

`awnix-setup` asks for a hostname, an administrator account, optional extra
components, and whether to link the box to your fleet. Choose the ai-full
image if you want the local model; it is sized to the hardware on first boot.

## 3. Join the collective

On the box:

```bash
adk login
adk volunteer enroll --lane embed,bonsai --collective occupysaas
adk volunteer serve --lane bonsai
adk volunteer start --lane embed
```

The same image can be imported as a cloud image; see [AWS](aws-ami.md).
