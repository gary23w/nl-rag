---
title: "IP routing"
source: https://en.wikipedia.org/wiki/IP_routing
domain: anycast-routing
license: CC-BY-SA-4.0
tags: anycast routing, anycast addressing, content delivery, route selection
fetched: 2026-07-02
---

# IP routing

**IP routing** is the application of traffic routing methodologies to IP networks. This involves technologies, protocols, structure, administrations, and policies of the worldwide Internet infrastructure. In each IP network node, IP routing involves the determination of a suitable path for a network packet from a source to its destination. The process uses rules, obtained from either static configuration or dynamically with routing protocols, to select specific packet forwarding methods to direct traffic to the next available intermediate network node one *hop* closer to the desired final destination. The total path potentially spans multiple computer networks.

Networks are separated from each other by specialized hosts, called gateways or routers with specialized software support optimized for routing. **IP forwarding** algorithms in most routing software determine a route through a shortest path algorithm. In routers, packets arriving at an interface are examined for source and destination addressing and queued to the appropriate outgoing interface according to their destination address and a set of rules and performance metrics. Rules are encoded in a routing table that contains entries for all interfaces and their connected networks. If no rule satisfies the requirements for a network packet, it is forwarded to a default route. Routing tables are maintained either manually by a network administrator, or updated dynamically by a routing protocol.

A routing protocol specifies how routers communicate and share information about the topology of the network, and the capabilities of each routing node. Different protocols are often used for different topologies or different application areas. For example, the Open Shortest Path First (OSPF) protocol is generally used within an enterprise and the Border Gateway Protocol (BGP) is used on a global scale. BGP is the de facto standard for worldwide Internet routing.

## Protocol classification

Routing protocols may be broadly distinguished by their realm of operation in terms of network scope. Interior gateway protocols are used for routing within autonomous systems, while exterior gateway protocols route traffic between them. The former group is exemplified by the Routing Information Protocol (RIP) and Open Shortest Path First (OSPF), while the Exterior Gateway Protocol (EGP) and the Border Gateway Protocol (BGP) are examples of the exterior type. BGP is the dominant route distribution protocol used on the Internet.

## Routing algorithm

The IP forwarding algorithm is a specific implementation of routing for IP networks. In order to achieve a successful transfer of data, the algorithm uses a routing table to select a next-hop router as the next destination for a datagram. The IP address of the selected router is known as the *next-hop address.*

The IP forwarding algorithm states:

Given a destination IP address,

D

, and network prefix,

N

:

if

(

N

matches a directly connected network address

)

Deliver datagram to

D

over that network link

;

else if

(

The routing table contains a route for

N

)

Send datagram to the next-hop address listed in the routing table;

else if

(

a default route exists

)

Send datagram to the default route

;

else

Send a forwarding error message to the originator

;

When multiple route table entries match, the entry with the longest subnet mask is chosen as it is the most specific one. If there are multiple routes with the same subnet mask, the route with the lowest metric is used. If there are multiple default routes, the metric is also used to determine which to use. If there are multiple routes with the same subnet mask and metric, the system may use equal-cost multi-path routing as a forwarding strategy.

When no route is available, an ICMP error message is sent to the originator of the packet, to inform that host that the packet could not be delivered. To avoid unnecessary retransmission to avoid network congestion, the sending host should either stop transmitting or choose another address or route.

## Routing table

The following presents a typical routing table in a Unix-like operating system:

```
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         71.46.14.1      0.0.0.0         UG    0      0        0 ppp0
10.0.0.0        0.0.0.0         255.0.0.0       U     0      0        0 eth0
71.46.14.1      0.0.0.0         255.255.255.255 UH    0      0        0 ppp0
169.254.0.0     0.0.0.0         255.255.0.0     U     0      0        0 eth0
172.16.0.0      0.0.0.0         255.240.0.0     U     0      0        0 eth0
192.168.0.0     0.0.0.0         255.255.0.0     U     0      0        0 eth0
192.168.1.0     192.168.96.1    255.255.255.0   UG    0      0        0 eth0
192.168.96.0    0.0.0.0         255.255.255.0   U     0      0        0 eth0
```

The host has several network interfaces. *eth0* is the interface name of the network interface card representing an Ethernet port. *ppp0* is a PPPoE interface, which is configured as the default route in this example.

A default route is recognized by the destination *0.0.0.0* and the flag *G*. A network router is identified by the network mask *255.255.255.255* and the flag *H*.

| Flag | Description |
|---|---|
| G | Use Gateway (gateway filled in) |
| H | Target is a Host (bitmask of 32 bits) |
| U | Route is Up |
