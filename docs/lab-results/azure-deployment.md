# Azure Checkout API — Hands-on Lab Results

- Test date: 2026-10-25
- Cloud provider: Microsoft Azure
- Hosting: Linux Azure App Service
- Plan: Free F1, if available
- Resource group: rg-ecab-46422
- Application: ecab-checkout-46422
- Application URL: https://ecab-checkout-46422.azurewebsites.net

## Scope

A demonstration FastAPI checkout API was deployed to Azure.
No database, payment processor, or persistent order store was used.

## Validation checklist

- [ ] Health endpoint returns HTTP 200.
- [ ] Readiness endpoint returns HTTP 200.
- [ ] Valid checkout returns an accepted simulation response.
- [ ] Simulated dependency failure returns HTTP 503.
- [ ] Invalid cart quantity is rejected with HTTP 422.
- [ ] Application logs were inspected.
- [ ] Deployment screenshots were captured.

## Architecture limitations

This is a portfolio lab, not a production deployment.
It does not yet implement private networking, managed identity,
persistent storage, multi-zone redundancy, or cross-region recovery.

## Cleanup

- Cleanup status: Pending
- Cleanup date: Not yet recorded

## Evidence

Add screenshots of the Azure resource, API documentation,
test results, and logs to the repository.
