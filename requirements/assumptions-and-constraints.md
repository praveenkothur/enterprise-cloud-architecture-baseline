# Assumptions and Constraints

## Assumptions
- The workload is a medium-sized, customer-facing web/API application.
- The initial footprint is one primary region with at least three availability zones where supported.
- A second region is reserved for recovery, not continuous active-active serving.
- The application is stateless at the compute tier.
- Order data resides in a managed relational database.
- Payment processing is delegated to a third-party provider; sensitive payment credentials are not stored.
- Traffic averages 2 million API requests per day with seasonal peaks; validate using real telemetry.
- A production baseline uses multiple application replicas and a managed database HA configuration.
- Data classification and applicable regulatory obligations will be confirmed by legal/security teams.

## Constraints
- Region choice must satisfy data residency, latency, and service availability requirements.
- All public endpoints require TLS; admin interfaces are not publicly exposed.
- Production secrets cannot be committed to source control or embedded in container images.
- Private workload tiers must use controlled egress and private endpoints where supported.
- Cost estimates are illustrative and must be replaced with calculator output before approval.
- Managed service features and exact names differ between AWS and Azure; do not assume one-to-one equivalence.
- Kubernetes is not mandatory. Prefer a simpler managed container service if the team cannot operate Kubernetes safely.

## Open questions
1. What are the approved RTO and RPO for checkout and order history?
2. Is customer data residency restricted to a specific country or region?
3. What is the expected peak request rate and payload size?
4. Which database engine and compatibility requirements are mandatory?
5. What are log retention and audit retention requirements?
6. Is cross-region warm standby required, or is backup-and-rebuild acceptable?
7. Are private corporate connectivity and on-premises integration required?
8. Which support plan and enterprise discounts apply?
