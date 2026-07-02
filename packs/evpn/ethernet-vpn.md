---
title: "Ethernet VPN"
source: https://en.wikipedia.org/wiki/Ethernet_VPN
domain: evpn
license: CC-BY-SA-4.0
tags: ethernet vpn, layer 2 vpn, provider backbone, mac learning
fetched: 2026-07-02
---

# Ethernet VPN

**Ethernet VPN** (**EVPN**) is a technology for carrying layer 2 Ethernet traffic as a virtual private network using wide area network protocols. EVPN technologies include Ethernet over Multiprotocol Label Switching (MPLS) and Ethernet over Virtual Extensible LAN (VXLAN).

EVPN uses encapsulation methods to enhance the efficiency and scalability of Ethernet traffic over MPLS or IP-based networks. The Ethernet frames are encapsulated within MPLS or VXLAN headers for transport.

## MPLS encapsulation

In MPLS-based EVPN, Ethernet frames are encapsulated with:

1. **MPLS label stack:** Each EVPN instance is associated with a unique label that helps in identifying the destination bridge domain.
2. **Control word (optional):** Provides additional information for synchronization and alignment in certain scenarios.

The encapsulated packet flow includes:

- **Original Ethernet frame**
- **MPLS labels**
- **Outer IP header** (in case of IP/MPLS networks)

EVPNs are covered by a number of Internet RFCs, including:

- RFC 7209 – "*Requirements for Ethernet VPN (EVPN),*" *Informational.*
- RFC 7432 – "*BGP MPLS-Based Ethernet VPN,*" *Proposed Standard.*
- RFC 8317 – "*Ethernet-Tree (E-Tree) Support in Ethernet VPN (EVPN) and Provider Backbone Bridging EVPN (PBB-EVPN),*" *Proposed Standard.*
- RFC 8365 – "*A Network Virtualization Overlay Solution Using Ethernet VPN (EVPN),*" *Proposed Standard.*
- RFC 9161 – "*Operational Aspects of Proxy ARP/ND in Ethernet Virtual Private Networks,*" *Proposed Standard.*
