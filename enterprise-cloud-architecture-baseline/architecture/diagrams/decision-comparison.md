# AWS vs Azure: Decision Comparison

| Concern | AWS reference | Azure reference | Decision guidance |
|---|---|---|---|
| Edge / WAF | CloudFront + AWS WAF | Front Door + WAF; optionally Application Gateway WAF | Use one or two layers only when each has a defined role |
| DNS | Route 53 | Azure DNS | Align with existing DNS ownership and operations |
| Network | VPC, subnets, security groups, endpoints | VNet, subnets, NSGs, private endpoints | Both support private-tier segmentation; implementation differs |
| Container runtime | ECS Fargate or EKS | Azure Container Apps or AKS | Prefer simpler managed container platform unless Kubernetes capabilities are needed |
| Workload identity | IAM roles, task role, EKS Pod Identity/IRSA | Managed identity, Entra Workload ID for AKS | Avoid long-lived cloud credentials |
| Secrets / keys | Secrets Manager, KMS | Key Vault, managed keys | Define rotation, access logging, and separation of duties |
| Relational data | RDS/Aurora | Azure SQL or Azure Database for PostgreSQL | Choose based on engine compatibility, HA, recovery, and team expertise |
| Messaging | SQS / EventBridge | Service Bus / Event Grid | Map delivery semantics and ordering needs explicitly |
| Object storage | S3 | Blob Storage | Validate redundancy, versioning, lifecycle, and immutability |
| Observability | CloudWatch, CloudTrail, X-Ray/OTel | Azure Monitor, Activity Logs, Application Insights | Standardize OpenTelemetry where useful; avoid duplicative ingestion |
| Governance | Organizations, SCPs, Config | Management Groups, Azure Policy | Enforce baseline controls as code |
| Cost control | Budgets, Cost Explorer, anomaly detection | Cost Management, budgets, Advisor | Tie spend to owner and environment tags |

## Recommendation
Choose the provider based on enterprise identity, existing landing zone, staff skills, data platform, regional requirements, and negotiated commercial terms. The architecture principles are portable; the managed service configurations and failure modes are not identical.

## Important differences
- AWS and Azure service names do not imply feature parity.
- Zone support, database failover behavior, quotas, private endpoint behavior, and regional recovery features must be validated for the exact SKU/region.
- Kubernetes increases operational burden. Do not select EKS/AKS solely because it is common in architecture diagrams.
