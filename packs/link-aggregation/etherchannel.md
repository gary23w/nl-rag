---
title: "EtherChannel"
source: https://en.wikipedia.org/wiki/EtherChannel
domain: link-aggregation
license: CC-BY-SA-4.0
tags: link aggregation, port channel, etherchannel bonding, network bonding
fetched: 2026-07-02
---

# EtherChannel

**EtherChannel** is a port link aggregation technology or port-channel architecture used primarily on Cisco switches. It allows grouping of several physical Ethernet links to create one logical Ethernet link for the purpose of providing fault-tolerance and high-speed links between switches, routers and servers. An EtherChannel can be created from between two and eight active Fast, Gigabit or 10-Gigabit Ethernet ports, with an additional one to eight inactive (failover) ports which become active as the other active ports fail. EtherChannel is primarily used in the backbone network, but can also be used to connect end user machines.

EtherChannel technology was invented by Kalpana in the early 1990s. Kalpana was acquired by Cisco Systems in 1994. In 2000, the IEEE passed 802.3ad, which is an open standard version of EtherChannel.

## Benefits

Using an EtherChannel has numerous advantages, and probably the most desirable aspect is the bandwidth. Using the maximum of 8 active ports a total bandwidth of 800 Mbit/s, 8 Gbit/s or 80 Gbit/s is possible depending on port speed. This assumes there is a traffic mixture, as those speeds do not apply to a single application only. It can be used with Ethernet running on twisted pair wiring, single-mode and multimode fiber.

Because EtherChannel takes advantage of existing wiring it makes it very scalable. It can be used at all levels of the network to create higher bandwidth links as the traffic needs of the network increase. All Cisco switches have the ability to support EtherChannel.

When an EtherChannel is configured all adapters that are part of the channel share the same Layer 2 (MAC) address. This makes the EtherChannel transparent to network applications and users because they only see the one logical connection; they have no knowledge of the individual links.

EtherChannel aggregates the traffic across all the available active ports in the channel. The port is selected using a Cisco-proprietary hash algorithm, based on source or destination MAC addresses, IP addresses or TCP and UDP port numbers. The hash function gives a number between 0 and 7, and the following table shows how the 8 numbers are distributed among the 2 to 8 physical ports. In the hypothesis of real random hash algorithm, 2, 4 or 8 ports configurations lead to fair load-balancing, whereas other configurations lead to unfair load-balancing.

| Number of Ports in the EtherChannel | Load Balancing ratio between Ports |
|---|---|
| 8 | 1:1:1:1:1:1:1:1 |
| 7 | 2:1:1:1:1:1:1 |
| 6 | 2:2:1:1:1:1 |
| 5 | 2:2:2:1:1 |
| 4 | 2:2:2:2 |
| 3 | 3:3:2 |
| 2 | 4:4 |

Fault-tolerance is another key aspect of EtherChannel. Should a link fail, the EtherChannel technology will automatically redistribute traffic across the remaining links. This automatic recovery takes less than one second and is transparent to network applications and the end user. This makes it very resilient and desirable for mission-critical applications.

Spanning Tree Protocol (STP) can be used with an EtherChannel. STP treats all the links as a single one and BPDUs are only sent down one of the links. Without the use of an EtherChannel, STP would effectively shutdown any redundant links between switches until one connection goes down. This is where an EtherChannel is most desirable, it allows use of all available links between two devices.

EtherChannels can be also configured as VLAN trunks. If any single link of an EtherChannel is configured as a VLAN trunk, the entire EtherChannel will act as a VLAN trunk. Cisco ISL, VTP and IEEE 802.1Q are compatible with EtherChannel.

## Limitations

A limitation of EtherChannel is that all the physical ports in the aggregation group must reside on the same switch except in the case of a switch stack, where they can reside on different switches on the stack. Avaya's SMLT protocol removes this limitation by allowing the physical ports to be split between two switches in a triangle configuration or 4 or more switches in a mesh configuration. Cisco's Virtual Switching System (VSS) allows the creation of a Multichassis Etherchannel (MEC) similar to the DMLT protocol allowing ports to be aggregated towards different physical chassis that form a single *virtual switch* entity. Also Extreme Networks may do this functionality via M-LAG Multilink Agreggation. Cisco Nexus series of switches allow the creation of a **Virtual PortChannel** (vPC) between a remote device and two individual Nexus switches. The two Cisco Nexus switches involved in a vPC differ from stacking or VSS technology in that stacking and VSS create a single data and control plane across the multiple switches, whereas vPC creates a single data plane across the two Nexus switches while keeping the two control planes separate.

## Components

EtherChannel is made up of the following key elements:

- Ethernet links — EtherChannel works over links defined by the IEEE 802.3 standard, including all sub-standards. All links in a single EtherChannel must be the same speed.
- Compatible hardware — the entire line of Cisco Catalyst switches as well as Cisco IOS software-based routers support EtherChannel. Configuring an EtherChannel between a switch and a computer requires support built into the operating system; FreeBSD, for example, supports EtherChannel via LACP. Multiple EtherChannels per device are supported; the number depends on the type of equipment. Catalyst 6500 and 6000 switches support a maximum of 64 EtherChannels.
- Configuration — an EtherChannel must be configured using the Cisco IOS on switches and router, and using specific drivers when connecting a server. There are two main ways an EtherChannel can be set up. The first is by manually issuing a command on each port of the device that is part of the EtherChannel. This must be done for the corresponding ports on both sides of the EtherChannel. The second way is by using Cisco's Port Aggregation Protocol (PAgP) or the IETF's LACP for the automated aggregation of Ethernet ports.

## EtherChannel vs. 802.3ad

EtherChannel and IEEE 802.3ad standards are very similar and accomplish the same goal. There are a few differences between the two, other than the fact that EtherChannel is Cisco proprietary and 802.3ad is an open standard, listed below:

Both technologies are capable of automatically configuring this logical link. EtherChannel supports both LACP and Cisco's PAgP, whereas 802.3ad uses LACP.

LACP allows for up to 8 active and 8 standby links, whereas PAgP only allows for 8 active links.
