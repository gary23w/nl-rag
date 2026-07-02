---
title: "Virtual Router Redundancy Protocol"
source: https://en.wikipedia.org/wiki/Virtual_Router_Redundancy_Protocol
domain: first-hop-redundancy
license: CC-BY-SA-4.0
tags: first hop redundancy, gateway redundancy, virtual router, hot standby
fetched: 2026-07-02
---

# Virtual Router Redundancy Protocol

The **Virtual Router Redundancy Protocol** (**VRRP**) is a computer networking protocol that provides for automatic assignment of available Internet Protocol (IP) routers to participating hosts. This increases the availability and reliability of routing paths via automatic default gateway selections on an IP subnetwork.

The protocol achieves this by the creation of virtual routers, which are an abstract representation of multiple routers, i.e. primary/active and secondary/Standby routers, acting as a group. The virtual router is assigned to act as a default gateway of participating hosts, instead of a physical router. If the physical router that is routing packets on behalf of the virtual router fails, another physical router is selected to automatically replace it. The physical router that is forwarding packets at any given time is called the primary/active router.

VRRP provides information on the state of a router, not the routes processed and exchanged by that router. Each VRRP instance is limited, in scope, to a single subnet. It does not advertise IP routes beyond that subnet or affect the routing table in any way. VRRP can be used in Ethernet, MPLS and Token Ring networks with Internet Protocol Version 4 (IPv4), as well as IPv6.

## Implementation

A virtual router must use *00-00-5E-00-01-XX* as its media access control (MAC) address. The last byte of the address (XX) is the virtual router identifier (VRID), which is different for each virtual router in the network. This address is used by only one physical router at a time, and it will reply with this MAC address when an ARP request is sent for the virtual router's IP address.

Physical routers within the virtual router must communicate within themselves using packets with multicast IP address *224.0.0.18* and IP protocol number 112 for IPv4, or *ff02::12* and IP protocol number 112 for IPv6.

Routers backing up a virtual router have a priority between 1 and 254, and the router with the highest priority will become the primary/active. The default priority is 100; for the MAC address owner, the priority is always 255.

## Elections of primary/active routers

A failure to receive a multicast packet from the primary/active router for a period longer than three times the advertisement timer causes the secondary/standby routers to assume that the primary/active router is dead. The virtual router then transitions into an unsteady state and an election process is initiated to select the next primary/active router from the secondary/standby routers. This is fulfilled through the use of multicast packets.

Secondary/standby router(s) are only supposed to send multicast packets during an election process. One exception to this rule is when a physical router is configured with a higher priority than the current primary/active, which means that on connection to the network it will pre-empt the primary/active status. This allows a system administrator to force a physical router to the primary/active state immediately after booting, for example when that particular router is more powerful than others within the virtual router. The secondary/standby router with the highest priority becomes the primary/active router by raising its priority above that of the current primary/active. It will then take responsibility for routing packets sent to the virtual gateway's MAC address. In cases where secondary/standby routers all have the same priority, the secondary/standby router with the highest IP address becomes the primary/active router.

All physical routers acting as a virtual router must be in the same local area network (LAN) segment. Communication within the virtual router takes place periodically. This period can be adjusted by changing advertisement interval timers. The shorter the advertisement interval, the shorter the black hole period, though at the expense of more traffic in the network. Security is achieved by responding only to first hop packets, though other mechanisms are provided to reinforce this, particularly against local attacks. The election process is made orderly through the use of skew time, derived from a router's priority, and used to reduce the chance of the thundering herd problem occurring during the election. The skew time is given by the formula (256 − *Priority*) / 256 (expressed in milliseconds).

Secondary/standby router utilization can be improved by load sharing.

## History

Work on VRRP started in 1997 with a first draft published by the Internet Engineering Task Force (IETF). In 1998, the protocol was officially defined. VRRP is an open standard, but Cisco claimed that their Hot Standby Router Protocol (HSRP), a similar but proprietary protocol with essentially the same facility, is patented and licensed. However, in 2001, in reply to a direct request, Robert Barr of Cisco replied that they will not assert any patent claims unless someone tried to assert a claim against Cisco. IBM also claims covering patents and their statement is readable on the IETF webpage. All patents in question have expired.

The protocol was refined in 2004 as version 2. VRRP version 3, the current version, was published in 2010.

## Derivatives

Mellanox offers MAGP, a proprietary protocol based on VRRP that allows active-active operation.

Foundry Networks developed VRRP-E(Extended), a proprietary version of VRRP that avoids a few limitations of RFC 3768
