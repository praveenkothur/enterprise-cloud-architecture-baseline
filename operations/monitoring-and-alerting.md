# Monitoring and Alerting Standard

## Golden signals
- **Latency:** p50/p95/p99 request duration and dependency duration.
- **Traffic:** request rate, queue throughput, and concurrent sessions.
- **Errors:** HTTP 5xx, failed transactions, payment-provider errors, and retry exhaustion.
- **Saturation:** CPU, memory, throttling, database connections, storage, queue age, and connection pool usage.

## Recommended alerts
| Alert | Initial condition | Severity | Response |
|---|---|---|---|
| Checkout availability | Synthetic checkout fails repeatedly from multiple probes | Critical | Page on-call; validate edge, app, database, dependencies |
| API errors | 5xx > 2% for 5 minutes with meaningful traffic | Critical/Warning by impact | Check release, dependency, saturation |
| API latency | p95 > 300 ms for 10 minutes | Warning | Inspect traces, database, and downstream calls |
| Database connections | > 80% of configured limit for 10 minutes | Warning | Inspect pool sizing and slow queries |
| Queue age | Oldest message exceeds business threshold | Warning/Critical | Check consumer health and DLQ |
| Pod/task restart rate | Sustained restarts or replicas below desired count | Warning | Inspect health checks, memory, image/config changes |
| Backup failure | Any critical database backup job fails | Critical | Retry/repair and confirm last valid recovery point |
| DR replication lag | Lag threatens RPO | Critical | Escalate to platform and data owner |
| Budget anomaly | Spend deviates materially from baseline | Warning | Check usage changes, egress, logs, and scaling |

Thresholds are starting points. Tune from SLOs and real workload behavior. Avoid paging on a metric unless the response is actionable.

## Logging and tracing
- Use structured JSON logs with request/correlation IDs.
- Do not log credentials, access tokens, payment details, or unnecessary personal data.
- Propagate trace context across services.
- Centralize cloud audit logs separately from application logs.
- Define retention, access controls, and deletion policy by classification.
- Monitor ingestion volume and cost.

## Alert lifecycle
1. Every alert has an owner, severity, runbook link, and expected action.
2. Test alert delivery and deduplication before launch.
3. Review false positives and missed incidents monthly.
4. Use maintenance windows/silences for approved changes, not to suppress unknown issues.
5. Record incident timeline, impact, contributing factors, and corrective actions.
