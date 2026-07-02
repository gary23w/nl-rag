---
title: "Segment routing"
source: https://en.wikipedia.org/wiki/SRv6
domain: segment-routing
license: CC-BY-SA-4.0
tags: segment routing, source routing, srv6 dataplane, traffic steering
fetched: 2026-07-02
---

# Segment routing

(Redirected from

SRv6

)

**Segment routing**, a form of computer networking, is a modern variant of source routing that is being developed within the SPRING and IPv6 working groups of the IETF. In a segment routed network, an ingress node may prepend a header to packets that contain a list of segments, which are instructions that are executed on subsequent nodes in the network. These instructions may be forwarding instructions, such as an instruction to forward a packet to a specific destination or interface.

Segment routing works either on top of a MPLS network or on an IPv6 network. In an MPLS network, segments are encoded as MPLS labels. Under IPv6, a new header called a Segment Routing Header (SRH) is used. Segments in a SRH are encoded in a list of IPv6 addresses. The *5f00::/16* prefix has been allocated for this purpose as part of an Internet-Draft.
