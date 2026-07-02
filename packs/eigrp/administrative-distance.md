---
title: "Administrative distance"
source: https://en.wikipedia.org/wiki/Administrative_distance
domain: eigrp
license: CC-BY-SA-4.0
tags: eigrp protocol, distance-vector routing, interior gateway protocol, route metric
fetched: 2026-07-02
---

# Administrative distance

**Administrative distance** (**AD**) or **route preference** is a number of arbitrary unit assigned to dynamic routes, static routes and directly connected routes. The value is used in routers to rank routes from most preferred (low AD value) to least preferred (high AD value). When multiple paths to the same destination are available in its routing table, the router uses the route with the lowest administrative distance.

Router vendors typically design their routers to assign a default administrative distance to each kind of route. For example, on Cisco routers, routes issued by the Open Shortest Path First routing protocol have a lower default administrative distance than routes issued by the Routing Information Protocol. This is because, by default on Cisco routers, OSPF has a default administrative distance of 110 and RIP has a default administrative distance of 120. Administrative distance values can, however, usually be adjusted manually by a network administrator.

## Overview

The administrative distance (AD) value is assigned by the router on a per-protocol basis. Routers, by design, should not install multiple routes into the routing table as this has the potential to cause routing loops. While a router may run multiple routing protocols on the same device, it is necessary for the router to implement a process to ensure that multiple routes, pointing to the same destination do not simultaneously exist in the routing table. Each process running on a router advertises its administrative distance value to the local router. The router uses this value to determine which route should be used. Once a route has been selected, the routing information database is updated. If two routes have the same administrative distance, the router uses its vendor-specific algorithm to determine which route should be installed. Cisco routers simply ignore the values and fall back to the default values, which are never the same.

The router will usually compare administrative distances to determine which protocol has the lowest value. The router prefers protocols that have a lower assigned administrative distance. For example, OSPF has a default distance of 110, so it is preferred by the router process, over RIP, which has a default distance of 120. The administrator can arbitrarily reconfigure the administrative distances, which affects the ranking of the preferred routes by the routing process. On Cisco routers, static routes have an administrative distance of 1, making them preferred over routes issued by a dynamic routing protocol. The administrative distance is a value that is always only referenced by the local router itself. The administrative distance is not advertised on the network.

## Default administrative distances

### Cisco

The following table lists the default administrative distances for various routing protocols used on Cisco routers.

| Routing protocol | Administrative distance |
|---|---|
| Directly connected interface | 0 |
| Static route | 1 |
| Dynamic Mobile Network Routing (DMNR) | 3 |
| EIGRP summary route | 5 |
| External BGP | 20 |
| EIGRP internal route | 90 |
| IGRP | 100 |
| Open Shortest Path First (OSPF) | 110 |
| Intermediate System to Intermediate System (IS-IS) | 115 |
| Routing Information Protocol (RIP) | 120 |
| Exterior Gateway Protocol (EGP) | 140 |
| ODR | 160 |
| EIGRP external route | 170 |
| Internal BGP | 200 |
| Next Hop Resolution Protocol (NHRP) | 250 |
| Default static route learned via DHCP | 254 |
| Unknown and unused | 255 |

1. Only the interface itself has an administrative distance of 0, since a route cannot have a distance of less than 1.
2. An administrative distance of 255 will cause the router to remove the route from the routing table and not use it.

### Juniper

The following table lists the default administrative distances for various routing protocols used on Juniper routers.

| Routing protocol | Administrative distance |
|---|---|
| Directly connected interface | 0 |
| Static routes | 5 |
| OSPF internal routes | 10 |
| IS-IS Level 1 Internal | 15 |
| IS-IS Level 2 Internal | 18 |
| RIP | 100 |
| Aggregate (route summary) | 130 |
| OSPF external routes | 150 |
| IS-IS Level 1 External | 160 |
| IS-IS Level 2 External | 165 |
| BGP | 170 |

### Extreme Networks

The following table lists the default administrative distances used on ExtremeXOS / Switch-Engine.

| Routing protocol | Administrative distance |
|---|---|
| Directly connected | 10 |
| MPLS | 20 |
| Blackhole | 50 |
| Static | 1100 |
| HostMobility | 1150 |
| ICMP-Redirect | 1200 |
| Fabric | 1699 |
| eBGP | 1700 |
| iBGP | 1900 |
| OSPFintra | 2200 |
| OSPFinter | 2300 |
| IS-IS | 2350 |
| IS-IS L1 | 2360 |
| IS-IS L2 | 2370 |
| RIP | 2400 |
| OSPF AS Ext | 3100 |
| OSPF Ext1 | 3200 |
| OSPF Ext2 | 3300 |
| IS-IS L1 Ext | 3400 |
| IS-IS L2 Ext | 3500 |
| Bootp | 5000 |

The following table lists the default administrative distances used on Extreme VOSS / Fabric-Engine.

| Routing Protocol | Administrative distance |
|---|---|
| Local | 0 |
| Static | 5 |
| SPBm L1 | 7 |
| OSPFintra | 20 |
| OSPFinter | 25 |
| eBGP | 45 |
| RIP | 100 |
| OSPF Ext1 | 120 |
| OSPF Ext2 | 125 |
| iBGP | 175 |

### FortiGate

The following table lists the default administrative distances for various routing protocols used on Fortinet FortiGate routers.

| Routing protocol | Administrative distance |
|---|---|
| Directly connected | 1 |
| Static routes | 10 |
| External BGP | 20 |
| Open Shortest Path First (OSPF) | 110 |
| Routing Information Protocol (RIP) | 120 |
| Internal & Local BGP | 200 |
| Kernel | 255 |

## Configuration

### Cisco IOS

The network administrator may modify the administrative distance to change the desired ranking of routing protocols. This may be necessary in cases where multiple routing protocols are in use. The Cisco Internetwork Operating System enables network administrators to modify the distance by changing the distance value in sub-router configuration mode. In the example below, RIP's administrative distance is changed to 89 so that it used in preference to OSPF.

```mw
R1#enable

R1#configure terminal

R1(config)#router rip

R1(config-router)#distance 89
```

Manually configuring the administrative distance is also required when configuring a floating static route. Floating static routes are used to provide an alternate path when a primary link fails. In order for static routes to be configured as a backup, the static route's administrative distance would need to be adjusted. Otherwise, it will take precedence over all routing protocols and routes issued from a routing protocol will not be inserted into the routing table. The example below shows how to configure the administrative distance to 254 to specify that it should only be used as a last resort.

`R1(config)# **ip route 10.0.0.0 255.0.0.0 backupLink 1 254**`

In the event that two routing protocols are configured with the same administrative distance, the Cisco router will ignore the configured values and instead use the default values.

Verifying the configuration of the administrative distance is done on Cisco equipment using the *show ip route* command in privileged exec mode on the console of the Cisco router. In the example shown below, the administrative distance is 1. The letter "S" indicates that the route is a static route that has, for all intents and purposes, been added manually to the router process by the administrator and installed into the routing table.

```mw
Router#enable

Router#configure terminal

Router(config)#ip route 1.1.1.0 255.255.255.0 fastEthernet 0/0

Router(config)#do show ip route
```

The *do show ip route* command will display the following, confirming that a static route has an administrative distance of 1.

`***S 1.1.1.0/0 [1/0] via 172.31.0.1***`
