---
title: "Supernetwork"
source: https://en.wikipedia.org/wiki/Supernetwork
domain: cidr-subnetting
license: CC-BY-SA-4.0
tags: cidr, subnetting, classless inter-domain routing, supernetwork
fetched: 2026-07-02
---

# Supernetwork

A **supernetwork**, or **supernet**, is an Internet Protocol (IP) network that is formed by aggregation of multiple networks (or subnets) into a larger network. The new routing prefix for the aggregate network represents the constituent networks in a single routing table entry. The process of forming a supernet is called **supernetting**, **prefix aggregation**, **route aggregation**, or **route summarization**.

Supernetting within the Internet serves as a strategy to avoid fragmentation of the IP address space by using a hierarchical allocation system that delegates control of segments of address space to regional Internet registries. This method facilitates regional route aggregation.

The benefits of supernetting are efficiencies gained in routers in terms of memory storage of route information and processing overhead when matching routes. Supernetting, however, can introduce interoperability issues and other risks.

## Overview

In IP networking terminology, a supernet is a block of contiguous subnetworks addressed as a single subnet from the perspective of the larger network. Supernets are always larger than their component networks. Supernetting is the process of aggregating routes to multiple smaller networks, thus saving storage space in the routing table, simplifying routing decisions and reducing route advertisements to neighboring gateways. Supernetting has helped address the increasing size of routing tables as the Internet has expanded.

Supernetting in large, complex networks can isolate topology changes from other routers. This can improve the stability of the network by limiting the propagation of routing changes in the event of a network link failure. If a router only advertises a summary route to the next router, then it does not need to advertise any changes to specific subnets within the summarized range. This can significantly reduce any unnecessary routing updates following a topology change. Hence, it increases the speed of convergence resulting in a more stable environment.

## Protocol requirements

Supernetting requires the use of routing protocols that support Classless Inter-Domain Routing (CIDR). Interior Gateway Routing Protocol, Exterior Gateway Protocol and version 1 of the Routing Information Protocol (RIPv1) assume classful addressing, and therefore cannot transmit the subnet mask information required for supernetting.

Enhanced Interior Gateway Routing Protocol (EIGRP) supports CIDR. By default, EIGRP summarizes the routes within the routing table and forwards these summarized routes to its peers. Other routing protocols with CIDR support include RIPv2, Open Shortest Path First, IS-IS and Border Gateway Protocol.

## Examples

A company that operates 150 accounting services in each of 50 districts has a router in each office connected with a Frame Relay link to its corporate headquarters. Without supernetting, the routing table on any given router might have to account for 150 routers in each of the 50 districts, or 7500 different networks. However, if a hierarchical addressing system is implemented with supernetting, then each district has a centralized site as an interconnection point. Each route is summarized before being advertised to other districts. Each router now only recognizes its own subnet and the other 49 summarized routes.

The determination of the summary route on a router involves the recognition of the number of highest-order bits that match all addresses. The summary route is calculated as follows. A router has the following networks in its routing table:

```
 192.168.98.0
 192.168.99.0
 192.168.100.0
 192.168.101.0
 192.168.102.0
 192.168.105.0
```

Firstly, the addresses are converted to binary format and aligned in a list:

| Address | First Octet | Second Octet | Third Octet | Fourth Octet |
|---|---|---|---|---|
| 192.168.98.0 | 11000000 | 10101000 | 01100010 | 00000000 |
| 192.168.99.0 | 11000000 | 10101000 | 01100011 | 00000000 |
| 192.168.100.0 | 11000000 | 10101000 | 01100100 | 00000000 |
| 192.168.101.0 | 11000000 | 10101000 | 01100101 | 00000000 |
| 192.168.102.0 | 11000000 | 10101000 | 01100110 | 00000000 |
| 192.168.105.0 | 11000000 | 10101000 | 01101001 | 00000000 |

Secondly, the bits at which the common pattern of digits ends are located. These common bits are shown in red. Lastly, the number of common bits is counted. The summary route is found by setting the remaining bits to zero, as shown below. It is followed by a slash and then the number of common bits.

| First Octet | Second Octet | Third Octet | Fourth Octet | Address | Netmask |
|---|---|---|---|---|---|
| 11000000 | 10101000 | 01100000 | 00000000 | 192.168.96.0 | /20 |

The summarized route is 192.168.96.0/20. The subnet mask is 255.255.240.0. This summarized route also contains networks that were not in the summarized group, namely, 192.168.96.0, 192.168.97.0, 192.168.103.0, 192.168.104.0, 192.168.106.0, 192.168.107.0, 192.168.108.0, 192.168.109.0, 192.168.110.0, and 192.168.111.0. It must be assured that the missing networks do not exist outside of this route.

In another example, an ISP is assigned a block of IP addresses by a regional Internet registry (RIR) of 172.1.0.0 to 172.1.255.255. The ISP might then assign subnetworks to each of their downstream clients, e.g., *Customer A* will have the range 172.1.1.0 to 172.1.1.255, *Customer B* would receive the range 172.1.2.0 to 172.1.2.255 and *Customer C* would receive the range 172.1.3.0 to 172.1.3.255, and so on. Instead of an entry for each of the subnets 172.1.1.x and 172.1.2.x, etc., the ISP could aggregate the entire 172.1.x.x address range and advertise the network 172.1.0.0/16, which would reduce the number of entries in the global routing table.

## Risks

The following supernetting risks have been identified:

- Supernetting is implemented in different ways on different routers.
- Supernetting on one router interface can influence how routes are advertised on other interfaces of the same router.
- In the presence of supernetting, detecting a persistent routing loop becomes a difficult problem.
- Adverse impact in heterogeneous routing environments with discontiguous subnets
