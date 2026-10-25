# ADR-002: Network Segmentation

- **Status:** Accepted for baseline
- **Date:** 2026-10-25

## Context
A public-facing checkout workload must minimize attack surface and limit lateral movement.

## Decision
Separate public ingress, private application workloads, and private data services. Use managed edge protection, narrow security rules, private service access, controlled egress, and centralized network logging.

## Reasons
- Prevents direct internet access to compute and data tiers.
- Limits the blast radius of compromised components.
- Makes allowed traffic paths reviewable.

## Consequences
- Private connectivity and egress controls add configuration and cost.
- DNS, routing, and endpoint policies require operational ownership.
- Emergency troubleshooting must use documented private admin paths.

## Alternatives considered
- Single flat network: rejected due to excessive lateral movement risk.
- Fully centralized hub-spoke from day one: deferred until connectivity scale requires it.
