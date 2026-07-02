---
title: "RSVP-TE"
source: https://en.wikipedia.org/wiki/RSVP-TE
domain: traffic-engineering-mpls
license: CC-BY-SA-4.0
tags: mpls traffic engineering, label distribution, resource reservation, path signaling
fetched: 2026-07-02
---

# RSVP-TE

**Resource Reservation Protocol - Traffic Engineering** (**RSVP-TE**) is an extension of the Resource Reservation Protocol (RSVP) for traffic engineering. It supports the reservation of resources across an IP network. Applications running on IP end systems can use RSVP to indicate to other nodes the nature (bandwidth, jitter, maximum burst, and so forth) of the packet streams they want to receive. RSVP runs on both IPv4 and IPv6.

RSVP-TE generally allows the establishment of Multiprotocol Label Switching (MPLS) label-switched paths (LSPs), taking into consideration network constraint parameters such as available bandwidth and explicit hops.

## History

As of February 2003, the Internet Engineering Task Force (IETF) MPLS working group deprecated Constraint-based Routing Label Distribution Protocol (CR-LDP) and decided to focus purely on RSVP-TE. Operational overhead of RSVP-TE compared to the more widely deployed Label Distribution Protocol (LDP) will generally be higher. This is a classic trade-off between complexity and optimality in the use of technologies in telecommunications networks.

## Standards

- RFC 3209 - RSVP-TE: Extensions to RSVP for LSP Tunnels
- RFC 3468 - The Multiprotocol Label Switching (MPLS) Working Group decision on MPLS signaling protocols
- RFC 4090 - Fast Reroute Extensions to RSVP-TE for LSP Tunnels
- RFC 4874 - Exclude Routes - Extension to Resource ReserVation Protocol-Traffic Engineering (RSVP-TE)
- RFC 4920 - Crankback Signaling Extensions for MPLS and GMPLS RSVP-TE
- RFC 5151 - Inter-Domain MPLS and GMPLS Traffic Engineering—Resource Reservation Protocol-Traffic Engineering (RSVP-TE) Extensions
- RFC 5420 - Encoding of Attributes for Multiprotocol Label Switching (MPLS) Label Switched Path (LSP) Establishment Using Resource ReserVation Protocol-Traffic Engineering (RSVP-TE)
- RFC 5711 - Node Behavior upon Originating and Receiving Resource Reservation Protocol (RSVP) Path Error Messages
- RFC 6001 - Generalized MPLS (GMPLS) Protocol Extensions for Multi-Layer and Multi-Region Networks (MLN/MRN)
