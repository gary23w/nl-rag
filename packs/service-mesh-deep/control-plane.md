---
title: "Control plane"
source: https://en.wikipedia.org/wiki/Control_plane
domain: service-mesh-deep
license: CC-BY-SA-4.0
tags: service mesh data plane, mesh control plane, mutual tls mesh, east west traffic
fetched: 2026-07-02
---

# Control plane

In network routing, the **control plane** is the part of the router architecture that is concerned with establishing the network topology, or the information in a routing table that defines what to do with incoming packets. Control plane functions, such as participating in routing protocols, run in the architectural control element. In most cases, the routing table contains a list of destination addresses and the outgoing interface or interfaces associated with each. Control plane logic can also identify certain packets to be discarded, as well as preferential treatment of certain packets for which a high quality of service is defined by such mechanisms as differentiated services.

Depending on the specific router implementation, there may be a separate forwarding information base that is populated by the control plane, but used by the high-speed forwarding plane to look up packets and decide how to handle them.

In computing, the control plane is the part of the software that configures and shuts down the data plane. By contrast, the data plane is the part of the software that processes the data requests. The data plane is also sometimes referred to as the forwarding plane.

The distinction has proven useful in the networking field where it originated, as it separates the concerns: the data plane is optimized for speed of processing, and for simplicity and regularity. The control plane is optimized for customizability, handling policies, handling exceptional situations, and in general facilitating and simplifying the data plane processing.

## Building the unicast routing table

A major function of the control plane is deciding which routes go into the main routing table. "Main" refers to the table that holds the unicast routes that are active. Multicast routing may require an additional routing table for multicast routes. Several routing protocols e.g., IS-IS, OSPF and BGP maintain internal databases of candidate routes which are promoted when a route fails or when a routing policy is changed.

Several different information sources may provide information about a route to a given destination, but the router must select the "best" route to install into the routing table. In some cases, there may be multiple routes of equal "quality", and the router may install all of them and load-share across them.

### Sources of routing information

There are three general sources of routing information:

- Information on the status of directly connected hardware and software-defined interfaces
- Manually configured static routes
- Information from (dynamic) routing protocols

#### Local interface information

Routers forward traffic that enters on an input interface and leaves on an output interface, subject to filtering and other local rules. While routers usually forward from one physical (e.g., Ethernet, serial) to another physical interface, it is also possible to define multiple logical interfaces on a physical interface. A physical Ethernet interface, for example, can have logical interfaces in several virtual LANs defined by IEEE 802.1Q VLAN headers.

When an interface has an address configured in a subnet, such as 192.0.2.1 in the 192.0.2.0/24 (i.e., subnet mask 255.255.255.0) subnet, and that interface is considered "up" by the router, the router thus has a directly connected route to 192.0.2.0/24. If a routing protocol offered another router's route to that same subnet, the routing table installation software will normally ignore the dynamic route and prefer the directly connected route.

There also may be software-only interfaces on the router, which it treats as if they were locally connected. For example, most implementations have a "null" software-defined interface. Packets having this interface as a next hop will be discarded, which can be a very efficient way to filter traffic. Routers usually can route traffic faster than they can examine it and compare it to filters, so, if the criterion for discarding is the packet's destination address, "blackholing" the traffic will be more efficient than explicit filters.

Other software-defined interfaces that are treated as directly connected, as long as they are active, are interfaces associated with tunneling protocols such as Generic Routing Encapsulation (GRE) or Multiprotocol Label Switching (MPLS). Loopback interfaces are virtual interfaces that are considered directly connected interfaces.

#### Static routes

Router configuration rules may contain static routes. A static route minimally has a destination address, a prefix length or subnet mask, and a definition of where to send packets for the route. That definition can refer to a local interface on the router, or a next-hop address that could be on the far end of a subnet to which the router is connected. The next-hop address could also be on a subnet that is directly connected, and, before the router can determine if the static route is usable, it must do a **recursive lookup** of the next hop address in the local routing table. If the next-hop address is reachable, the static route is usable, but if the next-hop is unreachable, the route is ignored.

Static routes also may have preference factors used to select the best static route to the same destination. One application is called a **floating static route**, where the static route is less preferred than a route from any routing protocol. The static route, which might use a dial-up link or other slow medium, activates only when the dynamic routing protocol(s) cannot provide a route to the destination.

Static routes that are more preferred than any dynamic route can also be very useful, especially when using traffic engineering principles to make certain traffic go over a specific path with an engineered quality of service.

#### Dynamic routing protocols

See routing protocols. The routing table manager, according to implementation and configuration rules, may select a particular route or routes from those advertised by various routing protocols.

### Installing unicast routes

Different implementations have different sets of preferences for routing information, and these are not standardized among IP routers. It is fair to say that subnets on directly connected active interfaces are always preferred. Beyond that, however, there will be differences.

Implementers generally have a numerical preference, which Cisco calls an "administrative distance", for route selection. The lower the preference, the more desirable the route. Cisco's IOS implementation makes exterior BGP the most preferred source of dynamic routing information, while Nortel RS makes intra-area OSPF most preferred.

The general order of selecting routes to install is:

1. If the route is not in the routing table, install it.
2. If the route is "more specific" than an existing route, install it in addition to the existing routes. "More specific" means that it has a longer prefix. A /28 route, with a subnet mask of 255.255.255.240, is more specific than a /24 route, with a subnet mask of 255.255.255.0.
3. If the route is of equal specificity to a route already in the routing table, but comes from a more preferred source of routing information, replace the route in the table.
4. If the route is of equal specificity to a route in the routing table, yet comes from a source of the same preference,
  1. Discard it if the route has a higher metric than the existing route
  2. Replace the existing route if the new route has a lower metric
  3. If the routes are of equal metric and the router supports load-sharing, add the new route and designate it as part of a load-sharing group. Typically, implementations will support a maximum number of routes that load-share to the same destination. If that maximum is already in the table, the new route is usually dropped.

## Routing table vs. forwarding information base

See forwarding plane for more detail, but each implementation has its own means of updating the forwarding information base (FIB) with new routes installed in the routing table. If the FIB is in one-to-one correspondence with the RIB, the new route is installed in the FIB after it is in the RIB. If the FIB is smaller than the RIB, and the FIB uses a hash table or other data structure that does not easily update, the existing FIB might be invalidated and replaced with a new one computed from the updated RIB.

## Multicast routing tables

Multicast routing builds on unicast routing. Each multicast group to which the local router can route has a multicast routing table entry with a next hop for the group, rather than for a specific destination as in unicast routing.

There can be multicast static routes as well as learning dynamic multicast routes from a protocol such as Protocol Independent Multicast (PIM).
