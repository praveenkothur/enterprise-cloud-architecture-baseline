# Threat Model

## System boundary
Customer traffic enters through a managed edge/WAF and load balancer. Stateless application workloads access a private relational database, cache, queue, object storage, secrets, and telemetry services. Administrators and CI/CD systems access cloud control planes through federated identity.

## Assets
- Customer and order metadata
- Checkout availability and integrity
- Cloud identities, tokens, and secrets
- Database backups and object versions
- Container images and deployment artifacts
- Audit logs and incident evidence
- Cloud account/subscription configuration

## Trust boundaries
1. Public internet to managed edge.
2. Edge/load balancer to private application tier.
3. Application tier to data and messaging services.
4. CI/CD identity to cloud control plane.
5. Production environment to recovery environment.
6. Runtime telemetry to centralized log/SIEM platform.

## Threats and mitigations
| Threat | Example | Mitigation | Detection / evidence |
|---|---|---|---|
| Credential theft | Leaked cloud key or token | OIDC/workload identity, short-lived credentials, MFA, least privilege | Audit logs, identity risk alerts |
| Public data exposure | Database/storage accidentally public | Private endpoints, public-access blocks, policy guardrails, config scans | CSPM findings and configuration history |
| Web attack | Injection, bot abuse, request flooding | WAF rules, input validation, rate limits, secure coding, DDoS controls | WAF logs, synthetic tests, app security logs |
| Lateral movement | Compromised app reaches unrelated workloads | Segmented subnets, narrow rules, least privilege, egress restrictions | Flow logs and workload telemetry |
| Supply-chain compromise | Malicious image or dependency | Signed/provenance-aware builds where available, scanning, protected branches, pinned dependencies | CI scan reports and artifact provenance |
| Data loss | Deletion or ransomware | Versioning, PITR, isolated backup copies, restricted delete rights, restore tests | Backup job alerts and restore evidence |
| Region outage | Primary region unavailable | Cross-region recovery design, tested runbooks, alternate-region quotas | DR exercise and replication metrics |
| Privilege escalation | Over-broad role assignment | PIM/time-bound elevation, policy guardrails, reviews | Cloud audit logs and access reviews |
| Sensitive logging | Tokens or personal data in logs | Structured logging standards, redaction, access controls, retention limits | Log scanning and periodic review |
| Denial of service | Traffic spike or dependency failure | Rate limiting, autoscaling, queue buffering, circuit breakers | SLO alerts and capacity dashboards |

## Risk ratings
Perform formal likelihood/impact scoring with the security team. Initial high-priority risks are identity compromise, public data exposure, destructive data loss, and untested recovery.

## Residual risks
- WAF does not replace secure application design.
- Cross-region replication may replicate corruption or malicious deletion.
- Managed services reduce operational burden but do not remove customer responsibility for configuration and access.
- Availability zones do not protect against regional failures or all control-plane incidents.
- Third-party payment-provider availability remains an external dependency.

## Review cadence
Review at design approval, before production launch, after major changes, and after security incidents or DR exercises.
