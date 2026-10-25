# AWS Illustrative Monthly Estimate

**Planning placeholder only.** These are rounded estimates for a moderate production workload, not live quotes. Replace every line with AWS Pricing Calculator output for the chosen region and SKU.

| Component | Illustrative monthly USD | Assumption |
|---|---:|---|
| Container compute | 900 | Managed containers, multiple replicas, variable load |
| Load balancing + edge/WAF | 350 | ALB, CDN/WAF usage, moderate request volume |
| Managed relational database HA | 1,400 | Production-sized Multi-AZ database and storage |
| Cache | 250 | Small managed replicated cache |
| Queue/event services | 100 | Moderate asynchronous traffic |
| Object storage + requests | 120 | Application artifacts/exports, lifecycle policy |
| NAT, endpoints, data transfer | 650 | Controlled egress; egress volume is uncertain |
| Logs, metrics, traces, audit/security | 700 | Moderate ingestion and retention |
| Cross-region backup/replication | 450 | Protected backup copies and limited replication |
| **Illustrative total** | **4,920** | Excludes taxes, support, discounts, and licensing |

## Sensitivity
- Egress and log ingestion can materially exceed the placeholder.
- Warm standby DR may add significant compute/database spend.
- Development environments should have separate, lower-cost schedules and budgets.
- Run the calculator with at least baseline, peak, and warm-standby scenarios.

## Approval
Do not use this total as a purchase commitment. Export a dated AWS Pricing Calculator estimate and record the input assumptions.
