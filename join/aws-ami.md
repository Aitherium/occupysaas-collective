# AWS: a node in the cloud

A cloud node is useful for the embed and runner lanes, and for a twin that
needs an always-on endpoint rather than a desktop that sleeps.

## Status: in progress

The AMI builder is not published yet, so there is no fixed AMI id to
quote here. Until it is, import the [awnix-ai-full ISO](spare-box.md) as
an EC2 image, or run the [Linux install](linux.md) on an instance you
already have. This page will carry the AMI id once it exists -- a guide
that named one now would be inventing it.

## After it boots

```bash
adk login
adk volunteer enroll --lane embed,twin --collective occupysaas \
  --invoke-url https://<your-node-host>/v1
```

The twin lane needs a URL the collective can actually reach; a loopback or
private address is refused. The embed lane needs no public address.
