---
title: "Border Gateway Protocol (part 2/2)"
source: https://en.wikipedia.org/wiki/BGP_confederation
domain: route-reflectors
license: CC-BY-SA-4.0
tags: route reflector, bgp scaling, internal bgp, autonomous system
fetched: 2026-07-02
part: 2/2
---

## Extensions

Multiprotocol Extensions for BGP (MBGP), sometimes referred to as Multiprotocol BGP or Multicast BGP and defined in RFC 4760, is an extension to BGP that allows different types of addresses (known as address families) to be distributed in parallel. Whereas standard BGP supports only IPv4 unicast addresses, Multiprotocol BGP supports IPv4 and IPv6 addresses and it supports unicast and multicast variants of each. Multiprotocol BGP allows information about the topology of IP multicast-capable routers to be exchanged separately from the topology of normal IPv4 unicast routers. Thus, it allows a multicast routing topology different from the unicast routing topology. Although MBGP enables the exchange of inter-domain multicast routing information, other protocols, such as the Protocol Independent Multicast family, are needed to build trees and forward multicast traffic. Multiprotocol BGP is also widely deployed in the case of MPLS L3 VPN, to exchange VPN labels learned for the routes from the customer sites over the MPLS network, in order to distinguish between different customer sites when the traffic from the other customer sites comes to the provider edge router for routing.

Another extension to BGP is multipath routing. This typically requires identical MED, weight, origin, and AS-path, although some implementations provide the ability to relax the AS-path checking to only expect an equal path length rather than the actual AS numbers in the path being expected to match too. This can then be extended further with features like Cisco's dmzlink-bw which enables a ratio of traffic sharing based on bandwidth values configured on individual links.

By default, BGP only supports the advertisement of a single locally selected best path to its neighbors through its Update messages. RFC 7911 defines the **ADD-PATH** extension, which allows a BGP speaker to advertise multiple paths for the same destination to peers. One application for this is when using route reflectors (RRs), because then the RR can advertise all known route paths to its clients, instead of sending only a single route it selected based on its local decision process, which is likely not the best path for all of its clients.


## Uses

BGP4 is standard for Internet routing and required of most Internet service providers (ISPs) to establish routing between one another. Very large private IP networks use BGP internally. An example use case is the joining of a number of large Open Shortest Path First (OSPF) networks when OSPF by itself does not scale to the size required. Another reason to use BGP is multihoming a network for better redundancy, either to multiple access points to a single ISP or to multiple ISPs.


## Implementations

Routers, especially small ones intended for small office/home office (SOHO) use, may not include BGP capability. Other commercial routers may need a specific software executable image that supports BGP, or a license that enables it. Devices marketed as layer-3 switches are less likely to support BGP than devices marketed as routers, but many high-end layer-3 switches can run BGP.

Products marketed as switches may have a size limitation on BGP tables that is far smaller than a full Internet table plus internal routes. These devices may be perfectly reasonable and useful when used for BGP routing of some smaller part of the network, such as a confederation-AS representing one of several smaller enterprises that are linked, by a BGP backbone of backbones, or a small enterprise that announces routes to an ISP but only accepts a default route and perhaps a small number of aggregated routes.

A BGP router used only for a network with a single point of entry to the Internet may have a much smaller routing table size (and hence RAM and CPU requirements) than a multihomed network. Even simple multihoming can have a modest routing table size. The actual amount of memory required in a BGP router depends on the amount of BGP information exchanged with other BGP speakers and the way in which the particular router stores BGP information. The router may have to keep more than one copy of a route, so it can manage different policies for route advertising and acceptance to a specific neighboring AS. The term *view* is often used for these different policy relationships on a running router.

If one router implementation takes more memory per route than another implementation, this may be a legitimate design choice, trading processing speed against memory. A full IPv4 BGP table as of September 2025 is in excess of one million prefixes. Large ISPs may add another 50% for internal and customer routes. Again, depending on implementation, separate tables may be kept for each view of a different peer AS.

Notable free and open-source implementations of BGP include:

- BIRD, a GPL routing package for Unix-like systems.
- FRRouting, a fork of Quagga for Unix-like systems; and its ancestors:
  - Quagga, a fork of GNU Zebra for Unix-like systems (no longer developed).
  - GNU Zebra, a GPL routing suite supporting BGP4 (decommissioned).
- OpenBGPD, a BSD-licensed implementation by the OpenBSD team.
- XORP, the eXtensible Open Router Platform, a BSD-licensed suite of routing protocols.

Systems for testing BGP conformance, load or stress performance come from vendors such as:

- Agilent Technologies
- GNS3 open source network simulator
- Ixia
- Spirent
