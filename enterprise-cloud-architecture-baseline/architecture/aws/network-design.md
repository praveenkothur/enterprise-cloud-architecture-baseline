# AWS Network Design

## Topology
- One VPC per environment, with non-overlapping CIDRs and separate accounts for production and non-production.
- Three Availability Zones where available. Create public subnets for the internet-facing ALB and NAT gateways; private application subnets for compute; isolated data subnets for database/cache.
- Route tables are explicit. Data subnets have no direct internet route.
- Use VPC endpoints for S3, ECR, CloudWatch, Secrets Manager, and other supported services to reduce public egress exposure and potentially reduce NAT cost.
- Use AWS WAF on CloudFront and/or ALB according to edge and origin requirements. Restrict the ALB origin to the intended edge path where feasible.
- Use AWS Network Firewall or a vetted egress proxy if centralized inspection is required. Do not deploy inspection infrastructure without a clear requirement and operational owner.

## Traffic flows
1. Internet -> Route 53 -> CloudFront/WAF -> ALB over HTTPS.
2. ALB -> application target over TLS where supported and configured.
3. Application -> database/cache using private IPs and narrow security-group rules.
4. Application -> AWS APIs through VPC endpoints where available.
5. Outbound third-party calls use controlled NAT/egress and domain-aware controls where feasible.

## Controls
- Security groups are stateful and narrowly scoped; avoid broad `0.0.0.0/0` rules except required public ingress.
- Network ACLs are secondary guardrails, not a replacement for security groups.
- Enable VPC Flow Logs with centralized, access-controlled retention.
- Use AWS Transit Gateway only if multiple VPCs/accounts/on-premises connectivity justify it.
- Use AWS PrivateLink for private service-to-service exposure when applicable.
- Allocate CIDRs with growth, peering, VPN, and future regional connectivity in mind.

## Example CIDR plan
| Tier | Example CIDR | Notes |
|---|---|---|
| VPC | `10.40.0.0/16` | Per environment and region |
| Public subnets | `10.40.0.0/20`, `10.40.16.0/20`, `10.40.32.0/20` | ALB/NAT; split by AZ |
| App subnets | `10.40.64.0/20`, `10.40.80.0/20`, `10.40.96.0/20` | Private workloads |
| Data subnets | `10.40.128.0/20`, `10.40.144.0/20`, `10.40.160.0/20` | Isolated data tier |

CIDRs are examples only. Validate route capacity, reserved addresses, and organization-wide IPAM allocations before deployment.
