---
title: "Label Distribution Protocol"
source: https://en.wikipedia.org/wiki/Label_Distribution_Protocol
domain: mpls
license: CC-BY-SA-4.0
tags: mpls, multiprotocol label switching, label distribution protocol, mpls vpn
fetched: 2026-07-02
---

# Label Distribution Protocol

**Label Distribution Protocol** (**LDP**) is a protocol in which routers capable of Multiprotocol Label Switching (MPLS) exchange label mapping information. Two routers with an established session are called LDP peers and the exchange of information is bi-directional. LDP is used to build and maintain label-switched path (LSP) databases that are used to forward traffic through MPLS networks.

LDP can be used to distribute the inner label (VC/VPN/service label) and outer label (path label) in MPLS. For inner label distribution, targeted LDP (tLDP) is used.

LDP and tLDP discovery runs on UDP port 646 and the session is built on TCP port 646. During the discovery phase hello packets are sent on UDP port 646 to the 'all routers on this subnet' group multicast address (224.0.0.2). However, tLDP unicasts the hello packets to the targeted neighbor's address.

## LDP

The Label Distribution Protocol (LDP) is a protocol defined by the IETF (RFC 5036) for the purpose of distributing labels in an MPLS environment. LDP relies on the underlying routing information provided by an IGP in order to forward label packets. The router forwarding information base, or FIB, is responsible for determining the hop-by-hop path through the network. Unlike traffic-engineered paths, which use constraints and explicit routes to establish end-to-end LSPs, LDP is used only for signaling best-effort LSPs.

### Authentication

LDP sessions carried over TCP can be authenticated using the *TCP MD5 Authentication Option*. While the IETF considers the *TCP MD5 Authentication Option* deprecated in favor of the algorithm-independent *TCP Authentication Option*, in practice the *TCP MD5 Authentication Option* is much more widely available in commercial routers as of July 2023. Use of authenticated LDP-over-TCP helps provide strong integrity protection against misconfigured would-be LDP peers.

## T-LDP

Targeted LDP sessions are different because during the discovery phase hellos are unicast to the LDP peer rather than using multicast. A consequence of this is that tLDP can be set up between non-directly connected peers whereas non-targeted LDP peers must be on the same subnet. tLDP may still be used between connected peers if desired.

On a router running TiMOS when an SDP (Service Distribution Path) is configured, automatic ingress and egress labeling (targeted LDP) is enabled by default and ingress and egress "service" labels are signaled over a TLDP connection. If signaling is turned off on an SDP, ingress and egress “service” labels must be manually configured when the SDP is bound to a service.

## RSVP-TE

This method determines a path through the network based on the interior gateway protocol's view of the network. If no constraints are applied to the LSP then the routers simply send the request for a path to the active next hop for that destination, without explicit routing. The IGP at each router is free to select active next hops based on the link state database.
