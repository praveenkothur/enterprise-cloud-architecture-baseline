# AWS Availability and Disaster Recovery

## Availability design
- Deploy stateless application replicas across at least three AZs when region/service support and cost permit.
- Configure ALB health checks, graceful shutdown, readiness checks, and autoscaling limits.
- Use RDS/Aurora Multi-AZ and connection retry logic. Multi-AZ improves availability but is not a backup strategy.
- Use managed cache with replication/failover where cache availability is business-critical; ensure the app can degrade safely if cache is unavailable.
- Use SQS/EventBridge retry, dead-letter queues, idempotent consumers, and alarms on queue age/depth.
- Apply deployment health gates, canary/rolling releases, and rollback automation.

## Recovery objectives
Proposed baseline: RTO <= 4 hours and RPO <= 15 minutes for order metadata. Confirm achievable values with the selected database, replication mode, and operational team.

## Recovery tiers
1. **Backup-and-restore:** lowest steady-state cost; rebuild infrastructure in recovery region and restore data. RTO may exceed 4 hours.
2. **Pilot light:** network/security foundation and replicated data available; scale compute during incident.
3. **Warm standby:** reduced-capacity app and data services already running; faster recovery at higher cost.
4. **Multi-site active/active:** not baseline; requires explicit business justification, data conflict strategy, and much higher complexity.

## Baseline controls
- Copy database backups and object data to a separate recovery region/account as appropriate.
- Enable deletion protection, point-in-time recovery, backup retention, and restricted backup administration.
- Protect backup copies from production compromise with separate permissions and, where required, immutable retention.
- Maintain tested IaC and versioned runbooks.
- Exercise regional recovery at least annually and after material architecture changes; test restores more frequently.
- Record recovery time, data loss, unresolved issues, and action owners.
