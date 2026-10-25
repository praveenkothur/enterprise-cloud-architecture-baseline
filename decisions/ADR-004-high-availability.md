# ADR-004: High Availability

- **Status:** Proposed
- **Date:** 2026-10-25

## Context
Checkout is revenue-impacting. An isolated instance or zone failure should not cause a full outage.

## Decision
Run multiple stateless application replicas across availability zones and use managed database HA. Add health checks, autoscaling, retry budgets, idempotency, and controlled deployment rollback.

## Consequences
- HA database configurations and multi-zone traffic may cost more.
- Zone redundancy does not protect against regional failure or logical data corruption.
- Applications must tolerate retries and duplicate asynchronous delivery.

## Alternatives considered
- Single-zone deployment: rejected for production baseline due to avoidable single-zone failure.
