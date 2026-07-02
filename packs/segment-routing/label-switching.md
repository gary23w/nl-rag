---
title: "Label switching"
source: https://en.wikipedia.org/wiki/Label_switching
domain: segment-routing
license: CC-BY-SA-4.0
tags: segment routing, source routing, srv6 dataplane, traffic steering
fetched: 2026-07-02
---

# Label switching

**Label switching** is a technique of network relaying to overcome the problems perceived by traditional IP-table switching (also known as traditional layer 3 hop-by-hop routing). Here, the switching of network packets occurs at a lower level, namely the data link layer rather than the traditional network layer.

Each packet is assigned a label number and the switching takes place after examination of the label assigned to each packet. The switching is much faster than IP-routing. New technologies such as Multiprotocol Label Switching (MPLS) use label switching. The established ATM protocol also uses label switching at its core.

According to RFC 2475 (An Architecture for Differentiated Services, December 1998):

"Examples of the label switching (or virtual circuit) model include Frame Relay, ATM, and MPLS. In this model, path forwarding state and traffic management or

quality of service

(QoS) state is established for traffic streams on each hop along a network path. Traffic aggregates of varying granularity are associated with a label-switched path at an ingress node, and packets/cells within each label-switched path are marked with a forwarding label that is used to look up the next-hop node, the per-hop forwarding behavior, and the replacement label at each hop. This model permits finer granularity resource allocation to traffic streams, since label values are not globally significant but are only significant on a single link; therefore resources can be reserved for the aggregate of packets/cells received on a link with a particular label, and the label switching semantics govern the next-hop selection, allowing a traffic stream to follow a specially engineered path through the network."

A related topic is multilayer switching, which discusses silicon-based wire-speed routing devices that examine not only network-layer packet information but also layer 4 (transport) and layer-7 (application) information.
