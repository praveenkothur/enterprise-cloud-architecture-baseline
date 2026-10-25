# ADR-003: Workforce and Workload Identity

- **Status:** Accepted for baseline
- **Date:** 2026-10-25

## Context
Static credentials create rotation burden and increase exposure risk.

## Decision
Federate workforce access through the enterprise identity provider, require MFA and privileged elevation, and use short-lived role/managed identities for workloads and CI/CD. Store unavoidable secrets in native secret stores.

## Consequences
- Federation and trust policies need careful setup and monitoring.
- Local emergency access must be restricted, monitored, and tested.
- Applications must support identity-based access to cloud services.

## Alternatives considered
- Long-lived user access keys or pipeline secrets: rejected except documented exception.
