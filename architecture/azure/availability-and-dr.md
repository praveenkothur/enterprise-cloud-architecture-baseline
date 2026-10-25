# Azure Availability and Disaster Recovery

## Availability design
- Use availability zones for supported compute and data services; verify regional/SKU support at deployment time.
- Run multiple application replicas with probes, autoscaling, and graceful shutdown.
- Configure database HA and backups using the selected engine's supported zone-redundant and geo-recovery features.
- Use Service Bus retries, dead-letter queues, duplicate detection/idempotency as appropriate, and queue-age alerts.
- Use deployment slots, canary, rolling deployment, or blue/green patterns according to the hosting platform.
- Ensure app behavior is defined for cache and dependency failure.

## Recovery objectives
Proposed baseline: RTO <= 4 hours and RPO <= 15 minutes for order metadata. Validate with the chosen database replication and restore strategy.

## Recovery tiers
1. **Backup-and-restore:** lowest standing cost, potentially longer RTO.
2. **Pilot light:** recovery network and data replication ready; app capacity added during incident.
3. **Warm standby:** scaled-down app and data resources already available.
4. **Active/active:** not baseline; requires explicit justification, conflict handling, and operational maturity.

## Baseline controls
- Configure database geo-backups/replication and object storage redundancy appropriate to data requirements.
- Keep recovery permissions separate from normal production permissions.
- Enable soft delete/versioning/immutability where suitable and test restore paths.
- Keep infrastructure definitions and recovery instructions version-controlled.
- Run annual DR exercises and regular component restore tests.
- Document regional service dependencies and known recovery limitations.
