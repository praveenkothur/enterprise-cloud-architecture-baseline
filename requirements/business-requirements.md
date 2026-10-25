# Business Requirements

## Business context
Northstar Commerce operates an online store. The checkout service validates carts, prices orders, authorizes payment through an external payment provider, and records order state. A checkout outage directly affects revenue and customer trust.

## Stakeholders
- Product owner: checkout journey and conversion
- Application team: service reliability and delivery
- Platform team: cloud foundations, deployment, and observability
- Security team: identity, data protection, and incident response
- Finance/FinOps: budgets, forecasts, and unit economics
- Business continuity owner: recovery priorities and exercises

## Functional scope
1. Serve HTTPS customer requests for checkout and order status.
2. Validate cart and pricing data using internal APIs.
3. Persist order metadata in a relational database.
4. Cache non-authoritative, frequently accessed data.
5. Publish order events to a managed queue/event service.
6. Store application artifacts and approved operational exports in object storage.
7. Expose health/readiness endpoints for orchestration and load balancing.
8. Produce structured logs, metrics, traces, and audit events.
9. Support controlled deployments and rollback.
10. Support backup restore and regional recovery procedures.

## Business requirements
| ID | Requirement | Acceptance evidence |
|---|---|---|
| BR-01 | Checkout must be available to customers over HTTPS. | External synthetic test succeeds |
| BR-02 | Application tiers must be independently scalable. | Load test and scaling event |
| BR-03 | Production data must be recoverable after accidental deletion or regional failure. | Restore/DR test report |
| BR-04 | Administrative actions must be attributable to an individual or workload identity. | Audit log review |
| BR-05 | Cloud costs must be attributable to environment, application, and owner. | Tag compliance report |
| BR-06 | Deployments must be repeatable and reversible. | CI/CD and rollback evidence |
| BR-07 | The design must support both AWS and Azure at reference-architecture level. | Provider comparison and ADRs |

## Out of scope
- Payment-card data storage; use a compliant payment provider and avoid storing PAN/CVV.
- Full application source code and production-grade Terraform modules.
- Exact vendor pricing or contractual discount modeling.
- Active-active multi-region writes unless separately justified.
- Compliance certification claims. Compliance applicability requires a formal assessment.
