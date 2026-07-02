---
title: "Traffic shaping"
source: https://en.wikipedia.org/wiki/Traffic_shaping
domain: traffic-shaping
license: CC-BY-SA-4.0
tags: traffic shaping, token bucket, leaky bucket, traffic policing
fetched: 2026-07-02
---

# Traffic shaping

**Traffic shaping** is a bandwidth management technique used on computer networks which delays some or all datagrams to bring them into compliance with a desired *traffic profile*. Traffic shaping is used to optimize or guarantee performance, improve latency, or increase usable bandwidth for some kinds of packets by delaying other kinds. It is often confused with traffic policing, the distinct but related practice of packet dropping and packet marking.

One type of traffic shaping is application-based traffic shaping. In application-based traffic shaping, fingerprinting tools are first used to identify applications of interest, which are then subject to shaping policies. Some controversial cases of application-based traffic shaping include bandwidth throttling of peer-to-peer file sharing traffic. Many application protocols use encryption to circumvent application-based traffic shaping.

Another type of traffic shaping is route-based traffic shaping. Route-based traffic shaping is conducted based on previous-hop or next-hop information.

## Functionality

If a link becomes utilized to the point where there is a significant level of congestion, latency can rise substantially. Traffic shaping can be used to prevent this from occurring and keep latency in check. Traffic shaping provides a means to control the volume of traffic being sent into a network in a specified period (bandwidth throttling), or the maximum rate at which the traffic is sent (rate limiting), or more complex criteria such as generic cell rate algorithm. This control can be accomplished in many ways and for many reasons; however, traffic shaping is always achieved by delaying packets.

Traffic shaping is commonly applied at the network edges to control traffic entering the network, but can also be applied by the traffic source (for example, computer or network card) or by an element in the network.

## Uses

Traffic shaping is sometimes applied by traffic sources to ensure the traffic they send complies with a contract, which may be enforced in the network by traffic policing.

Shaping is widely used for teletraffic engineering, and appears in domestic ISPs' networks as one of several Internet Traffic Management Practices (ITMPs). Some Internet service providers (ISPs) may use traffic shaping to limit resources consumed by peer-to-peer file-sharing networks, such as BitTorrent.

Data centers use traffic shaping to maintain service level agreements for the variety of applications and the many tenants hosted as they all share the same physical network.

Audio Video Bridging includes an integral traffic-shaping provision defined in IEEE 802.1Qav.

Nodes in an IP network that buffer packets before sending on a link that is at capacity produce an unintended traffic shaping effect. This can appear across, for example, a low bandwidth link, a particularly expensive WAN link or satellite hop.

## Implementation

A traffic shaper works by delaying metered traffic such that each packet complies with the relevant traffic contract. Metering may be implemented with, for example, the leaky bucket or token bucket algorithms (the former typically in ATM and the latter in IP networks). Metered packets or cells are then stored in a FIFO buffer, one for each separately shaped class, until they can be transmitted in compliance with the associated traffic contract. Transmission may occur immediately (if the traffic arriving at the shaper is already compliant), after some delay (waiting in the buffer until its scheduled release time) or never (in case of packet loss).

### Overflow condition

All traffic shaper implementations have a finite buffer and must cope with the case where the buffer is full. A simple and common approach is to drop traffic arriving while the buffer is full a strategy known as tail drop and which results in traffic policing as well as shaping. A more sophisticated implementation could apply a dropping algorithm such as random early detection.

### Traffic classification

Simple traffic shaping schemes shape all traffic uniformly. More sophisticated shapers first classify traffic. *Traffic classification* categorises traffic (for example, based on port number or protocol). Different *classes* can then be shaped separately to achieve a desired effect.

### Self-limiting sources

A *self-limiting source* produces traffic which never exceeds some upper bound, for example, media sources which cannot transmit faster than their encoded rate allows. Self-limiting sources shape the traffic they generate to a greater or lesser degree. Congestion control mechanisms can also affect traffic shaping of sorts - for example, TCP's window mechanism implements a variable rate constraint related to bandwidth-delay product.

TCP Nice, a modified version of TCP developed by researchers at the University of Texas at Austin, allows applications to request that certain TCP connections be managed by the operating system as near-zero-cost background transfers, or *nice* flows. Such flows interfere only minimally with foreground (non-nice) flows, while reaping a large fraction of spare network bandwidth.

### Relationship to bandwidth management

Traffic shaping is a specific technique and one of several that, combined, constitute bandwidth management.

## ISPs and traffic management

Traffic shaping is of interest, especially to ISPs. Their high-cost, high-traffic networks are their major assets, and as such, are the focus of their attention. They sometimes use traffic shaping to optimize the use of their network, sometimes by shaping traffic according to their assessment of importance and thus discouraging use of certain applications.

## Enterprises

Most companies with remote offices are now connected via a wide area network (WAN). Applications tend to be centrally hosted at the head office and remote offices are expected to pull data from central databases and server farms. As applications become hungrier in terms of bandwidth and prices of dedicated circuits being relatively high in most areas of the world, instead of increasing the size of their WAN circuits, companies feel the need to properly manage their circuits to make sure business-oriented traffic gets priority over other traffic. Traffic shaping is thus a good means for companies to avoid purchasing additional bandwidth while properly managing these resources.

Alternatives to traffic shaping in this regard are application acceleration and WAN optimization and compression, which are fundamentally different from traffic shaping. Traffic shaping defines bandwidth rules, whereas application acceleration uses multiple techniques like a TCP performance-enhancing proxy. WAN optimization, on the other hand, compresses data streams or sends only differences in file updates. The latter is quite effective for chatty protocols like CIFS.

## Traffic shaping detection

There are several methods to detect and measure traffic shaping. Tools have been developed to assist with detection.
