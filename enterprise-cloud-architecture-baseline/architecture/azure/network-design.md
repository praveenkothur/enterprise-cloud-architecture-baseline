# Azure Network Design

## Topology
- Use a dedicated VNet per environment/region with centrally governed address space.
- Use separate subnets for Application Gateway, application workloads, private endpoints, and any required platform integrations. Delegate subnets only where required by the chosen service.
- Keep database and cache access private. Use Private Link/private endpoints and Private DNS zones where supported.
- Use Azure Front Door with WAF for global edge routing and Application Gateway WAF for regional ingress when the extra layer is justified. Avoid duplicative WAF layers without a clear threat/traffic requirement.
- Use NAT Gateway for predictable outbound connectivity from eligible subnets; use Azure Firewall when centralized inspection, FQDN rules, or hub-spoke egress governance is required.

## Traffic flows
1. Internet -> Azure DNS -> Front Door/WAF -> regional Application Gateway -> private app workload.
2. App -> database/cache via private connectivity.
3. App -> Azure services through managed identity and private endpoints where supported.
4. Outbound third-party calls use controlled egress and logging.

## Controls
- Use NSGs for subnet/NIC-level segmentation and Azure Firewall policies where centralized inspection is required.
- Enable VNet flow logs / supported network monitoring and route logs to a controlled workspace.
- Use hub-spoke networking for shared services, on-premises connectivity, and centralized egress when complexity warrants it.
- Use Azure Virtual WAN only when global connectivity and operational scale justify it.
- Plan IP ranges to avoid overlap with corporate networks and future peering/VPN/ExpressRoute.
- Restrict private endpoint DNS changes to authorized platform administrators.

## Example address plan
| Tier | Example CIDR | Notes |
|---|---|---|
| VNet | `10.50.0.0/16` | Per environment and region |
| Ingress | `10.50.0.0/24` | Application Gateway subnet |
| App | `10.50.16.0/20` | Private application workloads |
| Private endpoints | `10.50.32.0/20` | Private Link endpoints |
| Platform/egress | `10.50.48.0/20` | Only if required by service design |

These CIDRs are examples. Confirm subnet delegation and sizing against the chosen compute service.
