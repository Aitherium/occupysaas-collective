# AWS: a node in the cloud

A cloud node is useful for the embed and runner lanes, and for a twin that
needs an always-on endpoint rather than a desktop that sleeps.

## Build an AMI in your own account

```bash
curl -fsSL https://raw.githubusercontent.com/Aitherium/awnix/main/awnix-aws-ami.sh | sh -s -- --region us-east-1 --dry-run
# drop --dry-run to build it
```

The builder runs bootc-image-builder against the public awnix image and
creates the bucket, the import role, the AMI and an SSH-only security
group in YOUR account, with YOUR credentials. `--dry-run` prints every
step and calls neither AWS nor a container engine. It prints a ready
`aws ec2 run-instances` command when it finishes.

## After it boots

```bash
adk login
adk volunteer enroll --lane embed,twin --collective occupysaas \
  --invoke-url https://<your-node-host>/v1
```

The twin lane needs a URL the collective can actually reach; a loopback or
private address is refused. The embed lane needs no public address.
