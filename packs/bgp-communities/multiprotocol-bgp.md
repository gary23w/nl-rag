---
title: "Multiprotocol BGP"
source: https://en.wikipedia.org/wiki/Multiprotocol_BGP
domain: bgp-communities
license: CC-BY-SA-4.0
tags: bgp communities, bgp policy, path attributes, route tagging
fetched: 2026-07-02
---

# Multiprotocol BGP

**Multiprotocol Extensions for BGP** (**MBGP** or **MP-BGP**), sometimes referred to as **Multiprotocol BGP** or **Multicast BGP** is an extension to Border Gateway Protocol (BGP) that allows different types of addresses (known as address families) to be distributed in parallel. It is defined in RFC 4760.

Whereas standard BGP supports only IPv4 unicast addresses, Multiprotocol BGP supports IPv4 and IPv6 addresses and it supports unicast and multicast variants of each. Multiprotocol BGP allows information about the topology of IP multicast-capable routers to be exchanged separately from the topology of normal IPv4 unicast routers. Thus, it allows a multicast routing topology different from the unicast routing topology. Although MBGP enables the exchange of inter-domain multicast routing information, other protocols such as the Protocol Independent Multicast family are needed to build trees and forward multicast traffic. As an enhancement of BGP-4, MP-BGP provides routing information for various protocols, such as IPv6 (BGP4+) and multicast:

- MP-BGP maintains unicast and multicast routing information, and stores both types in different routing tables to ensure their separation.
- MP-BGP supports unicast and multicast, and constructs different network topologies for each.
- MP-BGP can maintain unicast and multicast routes based on routing policies. The unicast routing policies and configurations supported by BGP-4 can mostly be applied to multicast.

Multiprotocol BGP is also widely deployed in case of MPLS L3 VPN, to exchange VPN labels learned for the routes from the customer sites over the MPLS network, in order to distinguish between different customer sites when the traffic from the other customer sites comes to the provider edge router (PE router) for routing.
