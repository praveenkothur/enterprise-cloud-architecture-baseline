# Nonfunctional Requirements

Targets below are proposed design objectives, not a contractual SLA. Business owners must approve them.

| ID | Attribute | Initial target | Verification |
|---|---|---|---|
| NFR-01 | Availability | 99.9% monthly service availability | SLI dashboard and monthly report |
| NFR-02 | Latency | Checkout API p95 under 300 ms at agreed load, excluding payment-provider latency | Load test and production telemetry |
| NFR-03 | Regional recovery | RTO <= 4 hours for baseline DR tier | Timed DR exercise |
| NFR-04 | Data loss | RPO <= 15 minutes for order metadata, subject to database replication/backup design | Recovery-point evidence |
| NFR-05 | Security | TLS in transit; encryption at rest; least privilege | Configuration and policy scans |
| NFR-06 | Scalability | Horizontal scaling for stateless compute | Load test and scaling evidence |
| NFR-07 | Resilience | No single application instance or availability zone is a planned single point of failure | Failure-injection test |
| NFR-08 | Operability | Actionable alerting, documented runbooks, named service owner | Alert test and runbook review |
| NFR-09 | Auditability | Centralized, access-controlled audit logs | Periodic audit review |
| NFR-10 | Backup | Automated backups and periodic restore tests | Restore evidence |
| NFR-11 | Cost | Budget alerts and monthly forecast variance review | FinOps report |
| NFR-12 | Maintainability | Infrastructure changes reviewed and version-controlled | Pull request history |

## Service-level indicators
- Availability: successful valid requests / total valid requests.
- Latency: p50, p95, and p99 server-side request duration.
- Errors: HTTP 5xx percentage and dependency failures.
- Saturation: CPU, memory, database connections, queue age, and connection pool utilization.
- Recovery: time from declared incident to service restoration; data recovery point achieved.

## Alerting principles
Alert on customer impact and actionable symptoms. Use warning and critical thresholds, multi-window burn-rate alerts where practical, and deduplication. Avoid paging on isolated noisy infrastructure metrics without impact context.
