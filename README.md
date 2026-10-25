# Enterprise Cloud Architecture Baseline

A portfolio-ready reference architecture for a fictional enterprise checkout platform, designed in parallel for AWS and Microsoft Azure. The project documents business and nonfunctional requirements, network segmentation, identity and security, high availability, disaster recovery, operational runbooks, cost assumptions, threat modeling, and architecture decision records.

> **Scope:** architecture baseline and planning artifacts, not a production deployment. Cost figures are illustrative planning estimates in USD, not vendor quotes. Validate service availability, quotas, pricing, and regional capabilities before implementation.

## Scenario

**Fictional company:** Northstar Commerce  
**Application:** `checkout-api`, a customer-facing e-commerce checkout service  
**Workload:** containerized API, web frontend, relational database, cache, object storage, asynchronous messaging, and centralized observability  
**Cloud strategy:** compare AWS and Azure without assuming that either provider is universally better.

## Architecture goals

- Public traffic enters through managed edge protection and a load-balancing layer.
- Application workloads run in private subnets/subnets with no direct inbound internet access.
- Workload identity is preferred over long-lived credentials.
- Data is encrypted in transit and at rest.
- Production workloads span multiple availability zones/zones.
- Backups are isolated from the primary workload and restore-tested.
- Disaster recovery targets are explicit and subject to business approval.
- Monitoring, audit logs, and actionable alerts are designed in from the start.
- Costs are visible, tagged, reviewed, and tied to stated assumptions.

## Repository map

```text
requirements/       Business, nonfunctional, assumptions and constraints
architecture/aws/   AWS reference architecture and design details
architecture/azure/ Azure reference architecture and design details
architecture/diagrams/ SVG diagrams and provider comparison
decisions/          Architecture Decision Records (ADRs)
operations/         Monitoring, backup/restore, and DR runbooks
cost/               Illustrative estimates and editable assumptions CSV
security/           Threat model and mitigations
```

## Key design baseline

| Concern | Baseline |
|---|---|
| Primary region | AWS `us-east-2` or Azure `East US 2`, subject to data residency and service validation |
| Availability | Multi-zone application and database deployment |
| Ingress | Managed WAF + HTTPS load balancer |
| Compute | Managed Kubernetes or managed container service; choose based on operational capability |
| Database | Managed relational database with Multi-AZ / zone-redundant HA |
| Cache | Managed Redis-compatible cache, private access only |
| Secrets | Native secret manager / Key Vault, with rotation |
| Identity | Federated workforce identity and workload identity |
| Recovery | Cross-region backup copy; warm-standby DR is an optional higher-cost tier |
| Observability | Metrics, logs, traces, audit logs, SLO-based alerts |
| Cost control | Mandatory tags, budgets, anomaly alerts, monthly review |

## Suggested implementation sequence

1. Review `requirements/` and confirm RTO/RPO with business owners.
2. Review the provider diagrams and ADRs. Record any deviations.
3. Build a non-production landing zone using infrastructure as code.
4. Add policy-as-code, secret scanning, image scanning, and CI checks.
5. Deploy a minimal application and test health checks, scaling, and failure behavior.
6. Run restore tests and a controlled DR exercise before production approval.
7. Compare actual cloud bills with the estimates in `cost/`.

## Validation checklist

- [ ] Confirm region and data residency requirements.
- [ ] Confirm workload sizing, traffic profile, and peak concurrency.
- [ ] Confirm database engine, storage, IOPS, and retention requirements.
- [ ] Confirm RTO/RPO with business and compliance owners.
- [ ] Validate service SKUs, quotas, private connectivity, and regional support.
- [ ] Replace illustrative cost assumptions with current pricing-calculator exports.
- [ ] Threat-model review completed and risks assigned owners.
- [ ] Backup restore and DR exercises completed with evidence.
- [ ] Alerts tested using simulated failures.
- [ ] Security, platform, application, and business owners sign off.

## Cost disclaimer

The example estimates are deliberately transparent and editable. They are not guaranteed current prices. Egress, support plans, taxes, discounts, licensing, log ingestion, data growth, and enterprise agreements can materially change the total. Use the official calculators before committing spend:
- AWS Pricing Calculator: https://calculator.aws/
- Azure Pricing Calculator: https://azure.microsoft.com/pricing/calculator/

## How to publish

```bash
git init
git add .
git commit -m "Add enterprise cloud architecture baseline"
git branch -M main
git remote add origin https://github.com/<YOUR-USERNAME>/enterprise-cloud-architecture-baseline.git
git push -u origin main
```

For GitHub rendering, Mermaid files use `.mmd`; preview them locally with Mermaid CLI or a Mermaid-compatible editor. SVG diagrams are included for quick viewing.
