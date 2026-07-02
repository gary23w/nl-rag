---
title: "Broadcast, unknown-unicast and multicast traffic"
source: https://en.wikipedia.org/wiki/Broadcast,_unknown-unicast_and_multicast_traffic
domain: storm-control
license: CC-BY-SA-4.0
tags: storm control, broadcast radiation, broadcast storm, traffic rate limiting
fetched: 2026-07-02
---

# Broadcast, unknown-unicast and multicast traffic

**Broadcast, unknown-unicast and multicast traffic** (**BUM traffic**) is network traffic transmitted using one of three methods of sending data link layer network traffic to a destination of which the sender does not know the network address. This is achieved by sending the network traffic to multiple destinations on an Ethernet network. As a concept related to computer networking, it includes three types of Ethernet modes: broadcast, unicast and multicast Ethernet. BUM traffic refers to that kind of network traffic that will be forwarded to multiple destinations or that cannot be addressed to the intended destination only.

## Overview

BUM scenarios

- (Example of Broadcast traffic) Example of *Broadcast traffic*
- (Example of Unknown unicast traffic where A is the source and B is the unknown destination) Example of *Unknown unicast traffic* where A is the source and B is the *unknown* destination
- (Example of Multicast traffic to five destinations) Example of *Multicast traffic* to five destinations

Broadcast traffic is used to transmit a message to any reachable destination in the network without the need to know any information about the receiving party. When broadcast traffic is received by a network switch it is replicated to all ports within the respective VLAN except the one from which the traffic comes from.

Unknown-unicast traffic happens when a switch receives unicast traffic intended to be delivered to a destination that is not in its forwarding information base. In this case the switch marks the frame for flooding and sends it to all forwarding ports within the respective VLAN. Forwarding this type of traffic can create unnecessary traffic that leads to poor network performance or even a complete loss of network service. This flooding of packets is known as a *unicast flooding*.

*Multicast* traffic allows a host to contact a subset of hosts or devices joined into a group. This causes the message to be broadcast when no group management mechanism is present. Flooding BUM frames is required in transparent bridging and in a data center context this does not scale well causing poor performance.

## BUM traffic control

### Throttling

One issue that may arise is that some network devices cannot handle high rates of broadcast, unknown-unicast or multicast traffic. In such cases, it is possible to limit the BUM traffic for specific ports in order to have a control on the number of packets or bytes that are flooded on the VLAN to other devices. This threshold is represented in kilobits per second (kbps), and it can be set for broadcast rate, multicast rate and unknown unicast rate independently.

### Network port security

In the case of unknown-unicast traffic, a security issue may arise. To prevent flooding unknown-unicast traffic across the switch, it is possible to configure the network equipment to divert unknown-unicast traffic to specific trunk interfaces in order to split broadcast coming from different VLANs or to use specific trunk interfaces for multiple VLANs.

## BUM handling in VXLAN

The use of VXLAN as overlay technology allows for providing data link layer connectivity services between endpoints that may be deployed across network layer network domains. Since those endpoints are logically part of the same data link layer domain, they must be capable of sending and receiving data link layer multi-destination frames (BUM traffic). BUM traffic can be exchanged across network layer network boundaries by encapsulating it into VXLAN packets addressed to a multicast group, so to leverage the network for traffic replication services.

> With the adoption of overlay networks as the standard deployment for multi-tenant network, data link layer over network layer protocols have been the favorite among network engineers. One of the data link layer over network layer (or Layer-2 over UDP) protocols adopted by the industry is VXLAN. Now, as with any other overlay network protocol, its scalability is tied into how well it can handle the Broadcast, Unknown unicast and Multicast (BUM).

In *Data Plane Learning* the broadcast traffic is flooded to multicast group members. In *Control Plane Learning* addresses are collected and forwarded via BGP. Broadcast traffic is reduced and VXLAN tunnel endpoints (VTEPs) reply to the caller directly.

VXLAN can handle BUM in two ways: *Multicast* and *Head End Replication*.

Multicast is the most common approach, and each VXLAN network identifier (VNI) is mapped to a single multicast group, while each multicast group may map to one or more VNIs. When a VTEP comes alive it uses the Internet Group Management Protocol to join the multicast groups for the VNIs it uses. When a VTEP has to send BUM traffic it will send it only to the relevant multicast group. This is a method for VTEP discovery.

Head End Replication is only available if using BGP EVPN. It is less efficient than multicast and does not scale well but it is simpler to implement if you do not have a multicast-enabled infrastructure. In Head End Replication, when BUM arrives, the VTEP creates several unicast packets and sends one to each VTEP that supports the VNI.

## BUM handling in EVPN

Ethernet VPN (EVPN) and Provider Backbone Bridging EVPN (PBB-EVPN) provide Ethernet multipoint services over MPLS networks. In EVPN operations, the Provider Edge (PE) routers automatically discover each other when connected on the same Ethernet segment and select a Designated Forwarder (DF) responsible for forwarding BUM traffic.

In a VXLAN-EVPN, MAC learning occurs via the *control plane* instead of *data plane*. Furthermore, it is accepted only traffic from VTEPs whose information is learnt via the control plane, otherwise it is dropped. This presents a secure fabric where traffic will only be forwarded between VTEPs validated by the control plane.
