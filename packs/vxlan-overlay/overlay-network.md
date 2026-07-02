---
title: "Overlay network"
source: https://en.wikipedia.org/wiki/Overlay_network
domain: vxlan-overlay
license: CC-BY-SA-4.0
tags: vxlan overlay, network overlay, layer 2 tunneling, network virtualization
fetched: 2026-07-02
---

# Overlay network

An **overlay network** is a logical computer network that is layered on top of a physical network. The concept of overlay networking is distinct from the traditional model of OSI layered networks, and almost always assumes that the underlay network is an IP network of some kind.

Some examples of overlay networking technologies are, VXLAN, BGP VPNs, and IP-over-IP technologies, such as GRE, IPSEC tunnels, or SD-WAN.

## Structure

Nodes in an overlay network can be thought of as being connected by logical links, each of which corresponds to a path, perhaps through many physical links, in the underlying network. For example, distributed systems such as peer-to-peer networks are overlay networks because their nodes form networks over existing network connections.

The Internet was originally built as an overlay upon the telephone network, while today (through the advent of VoIP), the telephone network is increasingly turning into an overlay network built on top of the Internet.

### Attributes

Overlay networks have a certain set of attributes, including separation of logical addressing, security and quality of service. Other optional attributes include resiliency, encryption and bandwidth control.

### Quality of Service

Guaranteeing bandwidth through marking traffic has multiple solutions, including IntServ and DiffServ. IntServ requires per-flow tracking and consequently causes scaling issues in routing platforms. It has not been widely deployed. DiffServ has been widely deployed in many operators as a method to differentiate traffic types. DiffServ itself provides no guarantee of throughput; it does allow the network operator to decide which traffic is higher priority, and hence will be forwarded first in congestion situations.

Overlay networks implement a much finer granularity of quality of service, allowing enterprise users to decide on an application and user or site basis which traffic should be prioritized.

## Uses

Many telcos use overlay networks to provide services over their physical infrastructure. In the networks that connect physically diverse sites (wide area networks, WANs), one common overlay network technology is BGP VPNs. These VPNs are provided in the form of a service to enterprises to connect their own sites and applications. The advantage of these kinds of overlay networks is that the telecom operator does not need to manage addressing or other enterprise-specific network attributes.

Within data centers, it was more common to use VXLAN, however due to its complexity and the need to stitch layer-2 VXLAN-based overlay networks to layer-3 IP/BGP networks, it has become more common to use BGP within data centers to provide layer-2 connectivity between virtual machines or Kubernetes clusters.

Enterprise private networks were first overlaid on telecommunication networks such as Frame Relay and Asynchronous Transfer Mode (ATM) packet switching infrastructures but migration from these (now legacy) infrastructures to IP-based MPLS networks and virtual private networks started (2001~2002) and is now completed, with very few remaining Frame Relay or ATM networks. From an enterprise point of view, while an overlay VPN service configured by the operator might fulfill their basic connectivity requirements, SD-WAN overlay networks offer additional flexibility.

The Internet is the basis for more overlaid networks that can be constructed in order to permit routing of messages to destinations not specified by an IP address. For example, distributed hash tables can be used to route messages to a node having a specific logical address, whose IP address is not known in advance.

Overlay networks can be incrementally deployed at end-user sites or on hosts running the overlay protocol software, without cooperation from Internet service providers. The overlay has no control over how packets are routed in the underlying network between two overlay nodes, but it can control, for example, the sequence of overlay nodes a message traverses before reaching its destination.

## Advantages

### Resilience

The objective of resilience in telecommunications networks is to enable automated recovery during failure events in order to maintain a wanted service level or availability. As telecommunications networks are built in a layered fashion, resilience can be used in the physical, optical, IP or session to application layers. Each layer relies on the resilience features of the layer below it. Overlay IP networks in the form of SD-WAN services therefore rely on the physical, optical and underlying IP services they are transported over. Application-layer overlays depend on all the layers below them. The advantage of overlays is that they are more flexible and programmable than traditional network infrastructure, which can outweigh the disadvantages of additional latency, complexity and bandwidth overheads.

#### Application layer resilience approaches

**Resilient overlay networks (RONs)** are architectures that allow distributed Internet applications to detect and recover from disconnection or interference. Current wide-area routing protocols that take at least several minutes to recover from are improved upon with this application-layer overlay. The RON nodes monitor the Internet paths among themselves and will determine whether or not to reroute packets directly over the Internet or over other RON nodes, thus optimizing application-specific metrics. The RON has a relatively simple conceptual design. RON nodes are deployed at various locations on the Internet. These nodes form an application-layer overlay that cooperates in routing packets. Each of the RON nodes monitors the quality of the Internet paths between each other and uses this information to accurately and automatically select paths from each packet, thus reducing the amount of time required to recover from poor quality of service.

### Multicast

*Overlay multicast* is also known as *End System* or *Peer-to-Peer Multicast* supports high bandwidth multi-source multicast among widely distributed nodes. It is a critical capability for a wide range of applications, including audio and video conferencing, multi-party games and content distribution. Multicast decouples the size of the receiver set from the amount of state kept at any single node and potentially avoids redundant communication in the network.

The limited deployment of IP multicast, a best-effort network-layer multicast protocol, has led to considerable interest in alternate approaches that are implemented at the application layer in accordance with the end-to-end principle. In an overlay or end-system multicast approach, participating peers organize themselves into an overlay topology for data delivery. Each edge in this topology corresponds to a unicast path between two end-systems or peers in the underlying internet. All multicast-related functionality is implemented at the peers instead of at routers, and the goal of the multicast protocol is to construct and maintain an efficient overlay for data transmission.

## Disadvantages

- No knowledge of the real network topology, subject to the routing inefficiencies of the underlying network, may be routed on sub-optimal paths.
- Possible increased latency compared to non-overlay services.
- Duplicate packets at certain points.
- Additional encapsulation overhead, meaning lower total network capacity due to multiple payload encapsulation.

## List of overlay network protocols

Overlay network protocols based on TCP/IP include:

- Distributed hash tables (DHTs) based on the Chord
- JXTA
- XMPP: the routing of messages based on an endpoint Jabber ID (Example: nodeId_or_userId@domainId\resourceId) instead of by an IP Address
- Many peer-to-peer protocols including Gnutella, Gnutella2, Freenet, I2P and Tor.
- PUCC
- Solipsis: a France Télécom system for massively shared virtual world

Overlay network protocols based on UDP/IP include:

- Distributed hash tables (DHTs) based on Kademlia algorithm, such as KAD, etc.
- Real Time Media Flow Protocol – Adobe Flash
