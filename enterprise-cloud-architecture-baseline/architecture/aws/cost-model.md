# AWS Cost Model

## Model boundaries
The sample monthly estimate in `../../cost/aws-estimate.md` represents a moderate production environment. It excludes taxes, support, enterprise discounts, and application licensing. Actual spend depends heavily on region, utilization, logs, egress, database sizing, and DR mode.

## Cost drivers
- Compute: task/node count, vCPU/memory, hours, scaling headroom.
- Database: instance class, storage, IOPS, backups, Multi-AZ, cross-region replication.
- Network: NAT gateways, data processing, internet egress, cross-AZ traffic, load balancers.
- Edge/security: CDN requests, WAF rules/requests, threat detection.
- Observability: metric cardinality, log ingestion/retention, tracing volume.
- DR: replicated data, standby compute, backup copies, and test runs.

## Optimization controls
- Use budgets and anomaly detection, with notifications to owners.
- Apply mandatory tags and review untagged spend.
- Right-size based on utilization and load tests; set autoscaling minimums and maximums.
- Set log retention by data class and operational need.
- Prefer private endpoints where appropriate, but compare endpoint costs with NAT processing costs.
- Use Savings Plans/Reserved Instances only after stable usage is demonstrated.
- Review cross-region and cross-AZ data transfer assumptions.
- Model warm standby separately; do not bury DR cost in the baseline.

## Approval gate
Export a current estimate from https://calculator.aws/ and attach assumptions, date, region, and pricing options to the project before budget approval.
