---
title: "Type of service"
source: https://en.wikipedia.org/wiki/Type_of_service
domain: qos-networking
license: CC-BY-SA-4.0
tags: quality of service, class of service, differentiated services, integrated services
fetched: 2026-07-02
---

# Type of service

The **type of service** (**ToS**) field is the second byte of the IPv4 header. It has had various purposes over the years, and has been defined in different ways by five RFCs.

Before the redefinition, the ToS field could specify a datagram's priority and request a route for low-latency, high-throughput, or highly-reliable service. Based on these ToS values, a packet would be placed in a prioritized outgoing queue or take a route with appropriate latency, throughput, or reliability. In practice, the ToS field never saw widespread use outside of the US Department of Defense networks. However, a great deal of experimental, research, and deployment work has focused on how to make use of these eight bits, resulting in the current DS field definition.

The modern redefinition of the ToS field (as well as the *Traffic Class* field in IPv6 packets) splits this byte into a 6-bit Differentiated Services (DS) field and a 2-bit Explicit Congestion Notification (ECN) field. While Differentiated Services is somewhat backwards compatible with ToS, ECN is not.

## History

The Type of Service field in the IP header was originally defined in RFC 791, and has been interpreted for *IP Precedence* and *ToS* ever since. The definition was largely derived from a US DoD Specification JANAP-128, which defines message multilevel precedence and preemption. It defined a mechanism for assigning a precedence to each IP packet, as well as a mechanism to request specific treatment such as high throughput, high reliability, or low latency, etc. In the RFC 1349 update, the Monetary Cost bit is introduced (this bit was previously marked "Reserved for Future Use"). Section 2.4 of RFC 1583 (OSPFv2) introduces a ToS-aware routing method.

In practice, only the IP Precedence part of the field was ever used outside US DoD networks: the higher the value of the IP Precedence field, the higher the priority of the IP packet. Some US DoD networks did use the delay bit for route selection between oceanic cable paths and Satellite Communication (SATCOM) paths when both paths existed. IPv6 has never had an IPv4-like "traditional" ToS field, partially because the authors were aware of DiffServ efforts at its drafting (RFC 2460 Section 7).

In RFC 2474, the definition of this entire field was changed. It is now called the "DS" (Differentiated Services, "DiffServ") field, and the upper 6 bits contain a value called the "DSCP" (Differentiated Services Code Point). The upper 3 bits of DS maintain compatibility with IP Precedence. Since RFC 3168, the remaining two bits (the two least significant bits) are used for Explicit Congestion Notification.

RFC 8622 added lower-effort (LE) DS for traffic that may be pre-empted by other traffic (best-effort traffic). It is intended for background traffic of low precedence, such as bulk data transfers with low priority in time.

## Allocation

### Precedence and ToS

Before its deprecation, the Type of Service field was defined as follows from RFC 791:

| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|---|---|---|---|---|---|---|---|
| Precedence | Type of Service | Unused (0) |   |   |   |   |   |

Precedence was a 3 bit field which treats high priority packets as more important than other packets. If a router is congested and needs to discard some packets, it will discard packets having the lowest priority first. Although the precedence field was part of IP version 4, it was never used.

RFC 1349 introduced an additional "low-cost" field. The four available ToS bits now become:

| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|---|---|---|---|---|---|---|---|
| (IP Precedence) | lowdelay | throughput | reliability | lowcost (RFC 1349) | (Must be zero) |   |   |

The naming here follows the convention of Unix operating systems. RFC 1349 and RFC 1060 only show examples of one bit used at a time for application-default values, although RFC 791 mentions that at most two of the three indications it has should be set nominally. One such use is known from mod_iptos.

Because the last three bits went through many definitions prior to RFC 2474 (see below), documentation and implementations may be confusing and contradictory.

### DSCP and ECN

RFC 2474 (which was released in December 1998) reserved the first six bits of the DS (or IPv4 ToS) field for the Differentiated Services Code Point (DSCP), and RFC 3168 reserved the last two bits for Explicit Congestion Notification.

| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|---|---|---|---|---|---|---|---|
| DSCP | ECN |   |   |   |   |   |   |

DSCP defines a Class Selector (CS) naming for each value it defines, mirroring what would have been interpreted as the IP Precedence if one follows the older specification:

| DSCP Name | DS Field Value (Dec) | IP Precedence (Description) |
|---|---|---|
| CS0 | 0 | 0: Best Effort |
| LE | 1 | n/a |
| CS1, AF11-13 | 8,10,12,14 | 1: Priority |
| CS2, AF21-23 | 16,18,20,22 | 2: Immediate |
| CS3, AF31-33 | 24,26,28,30 | 3: Flash - mainly used for voice signaling |
| CS4, AF41-43 | 32,34,36,38 | 4: Flash Override |
| CS5, EF | 40,46 | 5: Critical - mainly used for voice RTP |
| CS6 | 48 | 6: Internetwork Control |
| CS7 | 56 | 7: Network Control |

DSCP Nomenclature:

**CS**

Class Selector (RFC 2474)

**AFxy**

Assured Forwarding (x=class, y=drop precedence) (RFC 2597)

**EF**

Expedited Forwarding (RFC 3246)

**LE**

Lower-Effort (RFC 8622)

The above table, with individual values written out for values of the entire ToS field (not to be confused with the little-used 5-bit part):

| DSCP Dec | ToS value | IP Prec |
|---|---|---|
| 0 | 0 | 0 |
| 8 | 32 | 1 |
| 10 | 40 | 1 |
| 14 | 56 | 1 |
| 18 | 72 | 2 |
| 22 | 88 | 2 |
| 24 | 96 | 3 |
| 28 | 112 | 3 |
| 34 | 136 | 4 |
| 36 | 144 | 4 |
| 38 | 152 | 4 |
| 40 | 160 | 5 |
| 46 | 184 | 5 |
| 48 | 192 | 6 |
| 56 | 224 | 7 |

Note: In the above table, ToS is shown in decimal format. However, many routers express ToS in hex format.

### Example: mixed interpretation

Let's start with an IP precedence of 1, or `001` in binary. The entire ToS field would then be `001 00000`, assuming that the unused 5 bits are zero. The DSCP can be interpreted by resegmenting to `001000 00`, where `001000` = 8 is the DSCP value, corresponding to CS1.

## Software support

Although not frequently used, IP ToS definitions are widely found in `netinet/ip.h` of Unix-like or Unix operating systems as `IPTOS_FIELDNAME` macros. The "lowcost" field is commented out in OpenBSD due to its newer use for indicating ECN support. Remnants of the old RFC 1349 terminology can be found in Transmission 2.93 as well as other tools that support setting this field.

An old Apache module, "mod_iptos", once packaged in Ubuntu, notes that a way to use multiple RFC 1349 option bits together emerged after some point.
