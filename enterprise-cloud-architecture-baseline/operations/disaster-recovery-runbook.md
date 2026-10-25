# Disaster Recovery Runbook

## Activation criteria
Activate DR when the primary region is unavailable or expected to remain unavailable beyond the approved recovery threshold, or when a security/destructive incident requires isolation. The incident commander makes the activation decision with business and platform owners.

## Roles
- Incident commander: coordinates decisions and timeline.
- Cloud/platform lead: recovery infrastructure, routing, and identity.
- Data owner: recovery point, integrity, and consistency.
- Application lead: application deployment and validation.
- Security lead: incident containment, access review, and evidence.
- Business owner: customer communications and acceptance.

## Recovery sequence
1. **Declare and communicate**
   - Open incident, assign roles, record UTC timestamps, and use the approved communications plan.
   - Determine whether the primary is an outage or a security compromise. Do not blindly fail over a compromised environment.
2. **Assess recovery point**
   - Check database replication/backup timestamp, object data, queue state, and known corruption window.
   - Compare the achievable recovery point with the approved RPO.
3. **Prepare recovery region**
   - Confirm access, quotas, networking, private DNS, secrets, keys, registry images, and monitoring.
   - Apply reviewed infrastructure definitions. Do not make undocumented emergency changes unless necessary and recorded.
4. **Recover data**
   - Promote a supported replica or restore a protected backup according to the selected service design.
   - Confirm data integrity and application schema compatibility.
5. **Deploy application**
   - Deploy approved artifacts and configuration.
   - Validate health/readiness, database access, cache behavior, messaging, and external dependencies.
6. **Route traffic**
   - Update global/regional routing only after smoke tests and owner approval.
   - Consider DNS TTL, cache behavior, certificate validity, and client retry behavior.
7. **Validate service**
   - Run synthetic checkout and order-status tests.
   - Monitor error rate, p95 latency, queue age, database connections, and security alerts.
8. **Stabilize**
   - Keep increased monitoring for at least the agreed stabilization period.
   - Do not fail back until primary health, data reconciliation, and a controlled plan are approved.
9. **Close and learn**
   - Report actual RTO/RPO, customer impact, data reconciliation, and residual risks.
   - Schedule a blameless post-incident review and assign corrective actions.

## Recovery checklist
- [ ] Incident commander has declared DR
- [ ] Recovery region access and quotas verified
- [ ] Network, private DNS, and certificates verified
- [ ] Secrets and encryption keys available
- [ ] Database recovery point selected and integrity checked
- [ ] Object data and queues handled
- [ ] Application version and configuration validated
- [ ] Synthetic checkout succeeds
- [ ] Traffic cutover approved
- [ ] Security controls and monitoring active
- [ ] Business owner accepts service
- [ ] RTO/RPO and follow-up actions recorded

## Important
This runbook is a framework. Before production, replace generic steps with service-specific commands, resource names, approval contacts, and escalation paths. Conduct a timed exercise.
