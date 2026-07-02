---
title: "Collision domain"
source: https://en.wikipedia.org/wiki/Collision_domain
domain: network-switching
license: CC-BY-SA-4.0
tags: network switching, packet switching, cut-through switching, collision domain
fetched: 2026-07-02
---

# Collision domain

A **collision domain** is a network segment (connected by a shared medium or through repeaters) where simultaneous data transmissions collide with one another as a result of more than one device attempting to send a packet on the network segment at the same time. The collision domain applies particularly in wireless networks, but also affected early versions of Ethernet. Members of a collision domain may be involved in collisions with one another. Devices outside the collision domain do not have collisions with those inside.

A channel access method dictates that only one device in the collision domain may transmit at any one time, and the other devices in the domain listen to the network and refrain from transmitting while others are already transmitting in order to avoid collisions. Because only one device may be transmitting at any one time, total network bandwidth is shared among all devices on the collision domain. Collisions also decrease network efficiency in a collision domain as collisions require devices to abort transmission and retransmit at a later time.

Since data bits are propagated at a finite speed, *simultaneously* is to be defined in terms of the size of the collision domain and the minimum packet size allowed. A smaller packet size or a larger dimension would make it possible for a sender to finish sending the packet without the first bits of the message being able to reach the most remote node. So, that node could start sending as well, without a clue to the transmission already taking place and destroying the first packet. Unless the size of the collision domain allows the initial sender to receive the second transmission attempt – the collision – within the time it takes to send the packet, they would neither be able to detect the collision nor to repeat the transmission – this is called a late collision.

## Ethernet

On Ethernet using shared media, collisions are resolved using carrier-sense multiple access with collision detection (CSMA/CD) in which the competing packets are discarded and re-sent one at a time. This becomes a source of inefficiency in the network.

Early Ethernet variants (10BASE5, 10BASE2) were based on a shared wire and inherently half-duplex, representing a single, potentially large collision domain. Collision domains are also found in an Ethernet hub or repeater environment where each host segment connects to a hub, and all segments represent only one collision domain within one broadcast domain. Collision domains are also found in other shared medium networks, e. g. wireless networks such as Wi-Fi.

Modern wired networks use a network switch to reduce or eliminate collisions. By connecting each device directly to a port on the switch, either each port on a switch becomes its own collision domain (in the case of half-duplex links), or the possibility of collisions is eliminated in the case of full-duplex links. For Gigabit Ethernet and faster, no hubs or repeaters exist and all devices require full-duplex links.

## Wireless networks

Most wireless LAN networks use the carrier-sense multiple access with collision avoidance (CSMA/CA) method. In addition to the requirements of a shared wire medium, wireless networks add the hidden node problem where two senders can't hear each other's transmissions, but they cause a collision at the receiver between them. Multiple Access with Collision Avoidance for Wireless is one such approach used, specifically in 802.11 RTS/CTS. Central coordination is another means of solving this problem for a collision domain. This technique is employed by Wireless Multimedia Extensions. Point coordination function and distributed coordination function are specific implementations.
