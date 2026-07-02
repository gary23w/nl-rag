---
title: "Broadcast storm"
source: https://en.wikipedia.org/wiki/Broadcast_storm
domain: storm-control
license: CC-BY-SA-4.0
tags: storm control, broadcast radiation, broadcast storm, traffic rate limiting
fetched: 2026-07-02
---

# Broadcast storm

A **broadcast storm** or **broadcast radiation** is the accumulation of broadcast and multicast traffic on a computer network. Extreme amounts of broadcast traffic constitute a *broadcast storm*. It can consume sufficient network resources so as to render the network unable to transport normal traffic. A packet that induces such a storm is occasionally nicknamed a **Chernobyl packet**.

## Causes

Most commonly the cause is a switching loop in the Ethernet network topology (i.e. two or more paths exist between switches). A simple example is both ends of a single Ethernet patch cable connected to a switch. As broadcasts and multicasts are forwarded by switches out of every port, the switch or switches will repeatedly rebroadcast broadcast messages and flood the network. Since the layer-2 header does not support a time to live (TTL) value, if a frame is sent into a looped topology, it can loop forever.

In some cases, a broadcast storm can be instigated for the purpose of a denial of service (DOS) using one of the packet amplification attacks, such as the smurf attack or fraggle attack, where an attacker sends a large amount of ICMP Echo Requests (ping) traffic to a broadcast address, with each ICMP Echo packet containing the spoof source address of the victim host. When the spoofed packet arrives at the destination network, all hosts on the network reply to the spoofed address. The initial Echo Request is multiplied by the number of hosts on the network. This generates a storm of replies to the victim host tying up network bandwidth, using up CPU resources or possibly crashing the victim.

In wireless networks a disassociation packet spoofed with the source to that of the wireless access point and sent to the broadcast address can generate a disassociation broadcast DOS attack.

## Prevention

- Switching loops are largely addressed through link aggregation, Shortest Path Bridging or Spanning Tree Protocol. In Metro Ethernet rings it is prevented using the Ethernet Ring Protection Switching (ERPS) or Ethernet Automatic Protection System (EAPS) protocols.
- Filtering broadcasts by Layer 3 equipment, typically routers (and even switches that employ advanced filtering called brouters).
- Physically segmenting the broadcast domains using routers at Layer 3 (or logically with VLANs at Layer 2) in the same fashion switches decrease the size of collision domains at Layer 2.
- Routers and firewalls can be configured to detect and prevent maliciously inducted broadcast storms (e.g. due to a magnification attack).
- Broadcast storm control is a feature of many managed switches in which the switch intentionally ceases to forward all broadcast traffic if the bandwidth consumed by incoming broadcast frames exceeds a designated threshold. Although this does not resolve the root broadcast storm problem, it limits broadcast storm intensity and thus allows a network manager to communicate with network equipment to diagnose and resolve the root problem.

## MANET broadcast storms

In a mobile ad hoc network (MANET), route request (RREQ) packets are usually broadcast to discover new routes. These RREQ packets may cause broadcast storms and compete over the channel with data packets. One approach to alleviate the broadcast storm problem is to inhibit some hosts from rebroadcasting to reduce the redundancy, and thus contention and collision.
