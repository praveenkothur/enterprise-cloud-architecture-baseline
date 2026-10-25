# AWS IAM and Security

## Identity
- Federate workforce access through the corporate identity provider using IAM Identity Center and SSO.
- Require MFA for privileged access and use time-bound elevation where available.
- Use separate AWS accounts for production, non-production, security/log archive, and shared networking as organizational scale requires.
- Prefer ECS task roles or EKS Pod Identity / IRSA over static access keys.
- Use roles for CI/CD via OIDC federation. Do not store AWS access keys in GitHub secrets unless federation is unavailable and a documented exception is approved.

## Authorization
- Apply least privilege and resource-level restrictions where supported.
- Separate deployment, runtime, security audit, and break-glass roles.
- Deny public database access through policy and network controls.
- Require approvals for production changes and protect main branch.
- Review role trust policies and unused permissions periodically.

## Data protection
- Encrypt RDS, S3, EBS, logs, and backups using KMS-managed keys; use customer-managed keys where separation of duties or policy requires it.
- Require TLS for public and internal sensitive connections.
- Enable S3 Block Public Access, versioning, and appropriate lifecycle policies.
- Store credentials in Secrets Manager and rotate them on a defined schedule.
- Classify data and minimize sensitive fields in logs.

## Detection and governance
- Enable CloudTrail organization trails, AWS Config, GuardDuty, Security Hub, and centralized log storage according to budget and security requirements.
- Scan container images and dependencies before release.
- Apply SCPs and AWS Config rules for preventive/detective guardrails.
- Use tags for owner, environment, application, data classification, and cost center.
- Run incident response exercises and document evidence retention.

## Required safeguards
- No secrets in Git, images, build logs, or plaintext configuration.
- No direct SSH/RDP exposure from the internet.
- Use Systems Manager Session Manager or a controlled bastion pattern for administration.
- Test key rotation and revocation procedures.
