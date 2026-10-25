# Azure Identity and Security

## Identity
- Use Microsoft Entra ID for workforce authentication and centralized conditional access.
- Require MFA and privileged identity management / time-bound elevation for administrative roles.
- Use managed identities for supported Azure workloads; for AKS, configure Microsoft Entra Workload ID for pod-to-Azure authentication.
- Use GitHub Actions OIDC federation to Azure rather than client secrets.
- Separate production and non-production subscriptions and apply management-group governance where appropriate.

## Authorization
- Assign least-privilege Azure RBAC at the narrowest practical scope.
- Separate platform deployment, runtime identity, security operations, and emergency access.
- Use Azure Policy initiatives for required tags, allowed regions/SKUs, secure configurations, and diagnostic settings.
- Review privileged role assignments and service-principal federations regularly.

## Data protection
- Use Key Vault for secrets, keys, and certificates. Prefer managed identity access and rotation.
- Encrypt managed databases, disks, storage, and backups. Use customer-managed keys when policy requires them.
- Require HTTPS/TLS and validate private connectivity for data services.
- Disable anonymous/public blob access unless explicitly approved.
- Minimize sensitive data in logs and define retention by classification.

## Detection and governance
- Enable Defender for Cloud according to risk and budget, Azure Activity Logs, resource diagnostic settings, and Microsoft Sentinel if a SIEM is required.
- Enable container registry image scanning and CI dependency scanning.
- Send audit/security logs to a protected central workspace or storage account.
- Apply resource locks only where operationally appropriate; document removal authority.
- Require tags such as `application`, `environment`, `owner`, `costCenter`, and `dataClassification`.

## Required safeguards
- No secrets in Git, images, pipeline output, or plaintext app settings.
- No public database endpoints for this workload.
- Use private admin access and just-in-time elevation.
- Test identity revocation, credential rotation, and emergency access procedures.
