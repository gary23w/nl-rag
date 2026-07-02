---
title: "Broadcast domain"
source: https://en.wikipedia.org/wiki/Broadcast_domain
domain: spanning-tree-protocol
license: CC-BY-SA-4.0
tags: spanning tree protocol, loop prevention, network bridging, broadcast domain
fetched: 2026-07-02
---

# Broadcast domain

A **broadcast domain** is a logical division of a computer network, in which all nodes can reach each other by broadcast at the data link layer. A broadcast domain can be within the same LAN segment or it can be bridged to other LAN segments.

In terms of current popular technologies, any computer connected to the same Ethernet repeater or switch is a member of the same broadcast domain. Further, any computer connected to the same set of interconnected switches or repeaters is a member of the same broadcast domain. Routers and other network-layer devices form boundaries between broadcast domains.

The notion of a broadcast domain can be compared with a collision domain, which would be all nodes on the same set of inter-connected repeaters and divided by switches and network bridges. Collision domains are generally smaller than and contained within broadcast domains. While some data-link-layer devices are able to divide the collision domains, broadcast domains are only divided by network-layer devices such as routers or layer-3 switches. Separating VLANs divides broadcast domains as well.

## Further explanation

The distinction between broadcast and collision domains comes about because simple Ethernet and similar systems use a shared medium for communication. In simple Ethernet (without switches or bridges), data frames are transmitted to all other nodes on a network. Each receiving node checks the destination address of each frame and simply ignores any frame not addressed to its own MAC address or the broadcast address.

Switches act as buffers, receiving and analyzing the frames from each connected network segment. Frames destined for nodes connected to the originating segment are not forwarded by the switch. Frames destined for a specific node on a different segment are sent only to that segment. Only broadcast frames are forwarded to all other segments. This reduces unnecessary traffic and collisions.

In such a switched network, transmitted frames may not be received by all other reachable nodes. Nominally, only broadcast frames will be received by all other nodes. Collisions are localized to the physical-layer network segment they occur on. Thus, the broadcast domain is the entire inter-connected layer-2 network, and the segments connected to each switch or bridge port are each a collision domain. To clarify; repeaters do not divide collision domains but switches do. This means that since switches have become commonplace, collision domains are isolated to the specific segment between the switch port and the connected node. Full-duplex segments, or links, don't form a collision domain as there is a dedicated channel between each transmitter and receiver, eliminating the possibility of collisions.

## Broadcast domain control

With a sufficiently sophisticated switch, it is possible to create a network in which a broadcast domain is strictly controlled. One implementation of this concept is a private VLAN. Another implementation is possible with Linux and iptables. One analogy is that by creating multiple VLANs, the number of broadcast domains increases, but the size of each broadcast domain decreases. This is because a VLAN defines a broadcast domain.

This is achieved by designating one or more *provider* nodes, either by MAC address or switch port. Broadcast frames are allowed to originate from these sources and are sent to all other nodes. Broadcast frames from all other sources are directed only to the provider nodes. Traffic from other sources not destined to the provider nodes (peer-to-peer traffic) is blocked.

The result is a network based on a nominally shared transmission system; like Ethernet, but in which client nodes cannot communicate with each other, only with the provider. Allowing direct data link layer communication between client nodes exposes the network to various security attacks, such as ARP spoofing.
