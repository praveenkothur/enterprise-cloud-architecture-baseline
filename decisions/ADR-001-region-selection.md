# ADR-001: Primary and Recovery Region Selection

- **Status:** Proposed
- **Date:** 2026-10-25

## Context
The checkout platform requires low latency, regional service availability, recovery capability, and compliance with data residency requirements.

## Decision
Use AWS `us-east-2` or Azure `East US 2` as a candidate primary region, with a separate supported US recovery region selected after service and policy validation. This is a candidate baseline, not a final regional approval.

## Reasons
- Establishes a concrete region for initial diagrams and cost modeling.
- Supports a US-based workload assumption.
- Keeps primary and recovery region selection explicit.

## Consequences
- Confirm data residency and user latency requirements before production.
- Verify zone and DR feature availability for every selected SKU.
- Cross-region replication and egress add cost.
- Region names are not equivalent between providers and should not be treated as interchangeable.

## Alternatives considered
- Choose regions only after a formal latency/data residency assessment.
- Multi-region active/active, rejected for baseline due to complexity and cost.
