---
title: "Warning: Terraform Provider Moved"
date: 2020-12-08T15:32:05-08:00
tags:
    - terraform
    - devops
---

Recently I had an issue where Terraform did not seem to be loading the correct provider. I was getting the following result from a `terraform init -upgrade` even though I had updated the provider name in `versions.tf`

```
Warning: Additional provider information from registry

The remote registry returned warnings for
registry.terraform.io/terraform-providers/cloudflare:
- For users on Terraform 0.13 or greater, this provider has moved to
cloudflare/cloudflare. Please update your source in required_providers.

Terraform has been successfully initialized!
```

What appeared to be the issue is that changing the provider source in `versions.tf` like below did not result in the underlying resources using the new provider.

```diff
- source = "terraform-providers/cloudflare"
+ source = "cloudflare/cloudflare"
```

This makes sense once you realize what Terraform is doing. You wouldn't want someone to accidentally swap the source of a provider to something different entirely.

You can see this in Terraform's state. Go ahead and pull your state to `stdout` by running `terraform state pull` and you will find that each resource includes a provider.

```json
{
  "module": "module.cloudflare",
  "mode": "managed",
  "type": "cloudflare_zone",
  "name": "main",
  "provider": "provider[\"registry.terraform.io/terraform-providers/cloudflare\"]",
  "instances": [
    {
      ...
    }
  ]
},
```

Now you can go through the trouble of pulling your state file and manually making the changes and pushing it again, but the correct way to update it is to use the following command:

```bash
terraform state replace-provider OLD_PROVIDER NEW_PROVIDER
```

Or for my cloudflare example:

```bash
terraform state replace-provider terraform-providers/cloudflare cloudflare/cloudflare
```

Terraform will show you what resources you will be changing with this command and ask you to confirm.
