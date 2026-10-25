# Azure Illustrative Monthly Estimate

**Planning placeholder only.** These are rounded estimates, not live quotes. Replace every line with Azure Pricing Calculator output for the selected region and SKU.

| Component | Illustrative monthly USD | Assumption |
|---|---:|---|
| Container compute | 950 | AKS node pools or managed container capacity |
| Front Door / Application Gateway / WAF | 500 | Edge and regional ingress, moderate request volume |
| Managed relational database HA | 1,350 | Production-sized database and storage |
| Cache | 250 | Managed cache option with required availability |
| Service Bus / event services | 100 | Moderate asynchronous traffic |
| Blob storage + requests | 120 | Application artifacts/exports and lifecycle |
| NAT / Firewall / private endpoints / bandwidth | 700 | Controlled egress; actual traffic is a key variable |
| Azure Monitor / Log Analytics / security | 750 | Moderate ingestion and retention |
| Cross-region backup/replication | 450 | Protected backup copies and limited replication |
| **Illustrative total** | **5,170** | Excludes taxes, support, discounts, and licensing |

## Sensitivity
- SKU selection, database HA mode, log ingestion, bandwidth, and firewall design drive variance.
- Warm standby DR can increase cost significantly.
- Compare equivalent availability and retention assumptions across providers.
- Use current pricing and enterprise discount terms before making a provider decision.

## Approval
Export a dated Azure Pricing Calculator estimate and attach SKU, region, usage, and discount assumptions.
