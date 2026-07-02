---
title: "MPLS VPN"
source: https://en.wikipedia.org/wiki/MPLS_VPN
domain: mpls
license: CC-BY-SA-4.0
tags: mpls, multiprotocol label switching, label distribution protocol, mpls vpn
fetched: 2026-07-02
---

# MPLS VPN

CE

P

/

LSR

PE

/

ELSR

MPLS VPN

network diagram with wikilinks

**MPLS VPN** is a family of methods for using Multiprotocol Label Switching (MPLS) to create virtual private networks (VPNs). MPLS VPN is a flexible method to transport and route several types of network traffic using an MPLS backbone.

There are three types of MPLS VPNs deployed in networks today: 1. Point-to-point (Pseudowire) 2. Layer 2 (VPLS) 3. Layer 3 (VPRN)

## Point-to-point (pseudowire)

Point-to-point MPLS VPNs employ VLL (virtual leased lines) for providing Layer 2 point-to-point connectivity between two sites. Ethernet, TDM, and ATM frames can be encapsulated within these VLLs.

Some examples of how point-to-point VPNs might be used by utilities include:

- encapsulating TDM T1 circuits attached to Remote Terminal Units
- forwarding non-routed DNP3 traffic across the backbone network to the SCADA master controller.

## Layer 2 VPN (VPLS)

Layer 2 MPLS VPNs, or VPLS (virtual private LAN service), offers a “switch in the cloud” style service. VPLS provides the ability to span VLANs between sites. L2 VPNs are typically used to route voice, video, and AMI traffic between substation and data center locations.

## Layer 3 VPN (VPRN)

Layer 3, or VPRN (virtual private routed network), utilizes layer 3 VRF (VPN/virtual routing and forwarding) to segment routing tables for each customer utilizing the service. The customer peers with the service provider router and the two exchange routes, which are placed into a routing table specific to the customer. Multiprotocol BGP (MP-BGP) is required in the cloud to utilize the service, which increases complexity of design and implementation. L3 VPNs are typically not deployed on utility networks due to their complexity; however, a L3 VPN could be used to route traffic between corporate or datacenter locations.
