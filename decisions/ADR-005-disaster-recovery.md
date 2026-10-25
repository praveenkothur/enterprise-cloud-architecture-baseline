# ADR-005: Disaster Recovery Strategy

- **Status:** Proposed
- **Date:** 2026-10-25

## Context
A regional outage or destructive incident can make the primary region unavailable.

## Decision
Use cross-region protected backups as the minimum baseline. Design for RTO <= 4 hours and RPO <= 15 minutes as proposed targets. Select pilot-light or warm-standby DR only after business owners approve targets and budget.

## Consequences
- Backup-and-restore alone may not meet the proposed RTO; validate through timed exercises.
- Replication can reproduce logical corruption or deletion, so point-in-time recovery and isolated copies remain necessary.
- DR must include identity, DNS, secrets, network, observability, and dependencies, not only compute.

## Alternatives considered
- Active/active multi-region: deferred due to complexity and cost.
- Backups only with no tested recovery: rejected as insufficient operational practice.
