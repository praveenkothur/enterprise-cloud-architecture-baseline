# Backup and Restore Runbook

## Purpose
Restore application data after accidental deletion, corruption, or a service failure. Follow approved change and incident procedures.

## Preconditions
- Incident commander or service owner has authorized restore.
- Confirm target environment, database, recovery point, and business impact.
- Identify the last known good backup / point-in-time recovery timestamp.
- Ensure restore target is isolated from production writes until validated.
- Capture relevant logs and preserve evidence if compromise is suspected.

## Procedure
1. **Declare and scope**
   - Record incident ID, affected resources, timeline, and data-loss estimate.
   - Determine whether this is logical corruption, operator error, infrastructure failure, or suspected malicious activity.
2. **Select recovery point**
   - Consult backup catalog, database PITR range, object versioning, and replication status.
   - Prefer a point before the corruption/deletion was introduced.
3. **Restore to an isolated target**
   - Use provider-native restore workflow into a separate instance/account/subscription or isolated network.
   - Do not overwrite the original data before validation.
4. **Validate**
   - Check database integrity, row counts/business invariants, schema version, and application compatibility.
   - Run smoke tests against the isolated environment.
   - Security team validates the restored environment if compromise is suspected.
5. **Approve cutover**
   - Obtain application owner and incident commander approval.
   - Pause or drain writes as required; document consistency handling.
   - Update connection configuration/secret references through approved change process.
6. **Monitor**
   - Watch errors, latency, replication, queue backlog, and data consistency.
   - Keep the original resources protected until the retention/evidence decision is made.
7. **Close**
   - Record actual RTO/RPO, data loss, validation results, and follow-up actions.

## Safety checks
- Never restore untrusted backups directly into production without validation.
- Never delete the original source as part of an unverified restore.
- Verify encryption keys and permissions are available in the recovery environment.
- Ensure asynchronous queues are replayed safely and consumers are idempotent.
- For suspected compromise, rotate credentials and review audit trails before cutover.

## Exercise cadence
- Test critical database restore at least quarterly.
- Test object-level restore and secret/config recovery at least semiannually.
- Record evidence, duration, failures, and action owners.
