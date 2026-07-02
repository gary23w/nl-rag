---
title: "Gateway Load Balancing Protocol"
source: https://en.wikipedia.org/wiki/Gateway_Load_Balancing_Protocol
domain: first-hop-redundancy
license: CC-BY-SA-4.0
tags: first hop redundancy, gateway redundancy, virtual router, hot standby
fetched: 2026-07-02
---

# Gateway Load Balancing Protocol

**Gateway Load Balancing Protocol (GLBP)** is a Cisco proprietary protocol that attempts to overcome the limitations of existing first hop redundancy protocols by adding basic load balancing functionality.

In addition to being able to set priorities on different gateway routers, GLBP allows a weighting parameter to be set. Based on this weighting (compared to others in the same virtual router group), ARP requests will be answered with MAC addresses pointing to different routers. Thus, by default, load balancing is not based on traffic load, but rather on the number of hosts that will use each gateway router. By default, GLBP load balances in round-robin fashion.

GLBP elects one AVG (Active Virtual Gateway) for each group. Other group members act as backup in case of AVG failure. In case there are more than two members, the second best AVG is placed in the Standby state and all other members are placed in the Listening state. This is monitored using hello and holdtime timers, which are 3 and 10 seconds by default. The elected AVG then assigns a virtual MAC address to each member of the GLBP group, including itself, thus enabling AVFs (Active Virtual Forwarders). Each AVF assumes responsibility for forwarding packets sent to its virtual MAC address. There could be up to four AVFs at the same time.

By default, GLBP routers use the local multicast address 224.0.0.102 to send hello packets to their peers every 3 seconds over UDP 3222 (source and destination).

Cisco implemented IPv6 support for GLBP in IOS release 12.2(33)SXI.
