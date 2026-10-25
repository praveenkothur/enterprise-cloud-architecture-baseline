# Azure Cost Model

## Model boundaries
The sample estimate in `../../cost/azure-estimate.md` is an illustrative monthly planning model. It excludes taxes, support, enterprise discounts, licensing, and negotiated rates. Validate all selected SKUs and regional prices.

## Cost drivers
- Compute: AKS system/user nodes or Container Apps consumption, replicas, uptime, and autoscaling.
- Database: vCores/DTUs, storage, HA, backup retention, geo-replication, and I/O.
- Network: NAT Gateway, Azure Firewall, Application Gateway, Front Door, bandwidth, and private endpoints.
- Observability: Log Analytics ingestion/retention, metrics, tracing, and security analytics.
- DR: replicated storage/database, warm standby, and recovery testing.

## Optimization controls
- Configure budgets, alerts, tags, and Cost Management exports.
- Use Azure Advisor recommendations after validating performance and resilience impact.
- Right-size after load tests and use autoscaling with safe limits.
- Set workspace retention and avoid excessive high-cardinality telemetry.
- Compare NAT Gateway with Azure Firewall based on actual security requirements, not cost alone.
- Review egress and cross-region transfer costs.
- Use reservations/savings plans only after usage patterns are stable.

## Approval gate
Create a dated estimate using https://azure.microsoft.com/pricing/calculator/ and preserve region, SKU, usage, and discount assumptions.
