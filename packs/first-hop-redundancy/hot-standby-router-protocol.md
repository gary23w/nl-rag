---
title: "Hot Standby Router Protocol"
source: https://en.wikipedia.org/wiki/Hot_Standby_Router_Protocol
domain: first-hop-redundancy
license: CC-BY-SA-4.0
tags: first hop redundancy, gateway redundancy, virtual router, hot standby
fetched: 2026-07-02
---

# Hot Standby Router Protocol

In computer networking, the **Hot Standby Router Protocol** (**HSRP**) is a Cisco proprietary redundancy protocol for establishing a fault-tolerant default gateway. Version 1 of the protocol was described in RFC 2281 in 1998. Version 2 of the protocol includes improvements and supports IPv6 but there is no corresponding RFC published for this version.

The protocol establishes an association between gateways in order to achieve default gateway failover if the primary gateway becomes inaccessible. HSRP gateways send multicast *hello* messages to other gateways to notify them of their priorities (which gateway is preferred) and current status (*active* or *standby*).

## Operation

The primary router with the highest configured priority will act as a *virtual* router with a pre-defined gateway IP address and will respond to the ARP or ND request from machines connected to the LAN with a virtual MAC address. If the primary router should fail, the router with the next-highest priority would take over the gateway IP address and answer ARP requests with the same MAC address, thus achieving transparent default gateway failover.

| HSRP version | IP protocol | Group address | UDP port | Virtual MAC address range |
|---|---|---|---|---|
| 1 | IPv4 | 224.0.0.2 (all routers) | 1985 | 00:00:0c:07:ac:XX |
| 2 | IPv4 | 224.0.0.102 (HSRP) | 1985 | 00:00:0c:9f:fX:XX |
| IPv6 | ff02::66 | 2029 | 00:05:73:a0:0X:XX |   |

In the virtual MAC address, Xs represent the group ID in hex.

HSRP is not a routing protocol as it does not advertise IP routes or affect the routing table in any way.

HSRP has the ability to trigger a failover if one or more interfaces on the router go down. This can be useful for dual branch routers each with a single link back to the gateway. If the link of the primary router goes down, the backup router will take over the primary functionality and thus retain connectivity to the gateway.

## Version 2

Version 2 of the protocol introduces stability, scalability and diagnostic improvements. It is not compatible with version 1 HSRP. There is no RFC for version 2 of the protocol.

- Provides IPv6 support
- Increases the number of HSRP groups from 256 to 4096
