---
title: "Stream Reservation Protocol"
source: https://en.wikipedia.org/wiki/Stream_Reservation_Protocol
domain: ieee-802-1-tsn
license: CC-BY-SA-4.0
tags: ieee 802.1 tsn, stream reservation, frame preemption, credit-based shaper
fetched: 2026-07-02
---

# Stream Reservation Protocol

**Stream Reservation Protocol** (**SRP**) is an enhancement to Ethernet that implements admission control. In September 2010 SRP was standardized as **IEEE 802.1Qat** which has subsequently been incorporated into IEEE 802.1Q-2011. SRP defines the concept of streams at layer 2 of the OSI model. Also provided is a mechanism for end-to-end management of the streams' resources, to guarantee quality of service (QoS).

SRP is part of the IEEE Audio Video Bridging (AVB) and Time-Sensitive Networking (TSN) standards. The SRP technical group started work in September 2006 and finished meetings in 2009.

## Description

SRP registers a stream and reserves the resources required through the entire path taken by the stream, based on the bandwidth requirement and the latency which are defined by a stream reservation traffic class.

*Listener* (stream destination) and *Talker* (stream source) primitives are utilized. Listeners indicate what streams are to be received, and Talkers announce the streams that can be supplied by a bridged entity. Network resources are allocated and configured in both the end nodes of the data stream and the transit nodes along the data streams' path. An end-to-end signaling mechanism to detect the success/failure of the effort is also provided.

SRP "talker advertise" message includes QoS requirements (e.g., VLAN ID and Priority Code Point (PCP) to define traffic class, rank (emergency or nonemergency), traffic specification (maximum frame size and maximum number of frames in a traffic class), measurement interval, and accumulated worst case latency).

- Static across network:
  - StreamID (48-bit MAC address plus a 16-bit UniqueID)
  - Stream destination address (or a multicast group MAC address)
  - VLAN ID (used by MVRP)
  - Priority (PCP)
  - Rank
  - Traffic specification
    - Maximum frame size
    - Maximum number of frames (per measurement interval)
  - Measurement interval
- Adjusted per each hop:
  - Accumulated latency
  - Failure Information (Bridge ID and failure code)

Required bandwidth is calculated as MaxFrameSize × MaxIntervalFrames. If a bridge is able to reserve the required resources, it propagates the advertisement to the next bridge; otherwise a 'talker failed' message is raised. When the advertise message reaches the listener, it replies with 'listener ready' message that propagates back to the talker.

Talker advertise and listener ready messages can be de-registered, which terminates the stream. Periodic polling of advertise and ready messages is used to detect unresponsive devices.

Worst case latency is recalculated at every bridge, so higher protocol layers can use it for media synchronization.

For credit-based shaper defined in IEEE 802.1Qav, Stream Reservation Class A is the highest, with worst-case latency requirement of 2 ms, and a measurement interval (maximum transmission period) of 125 μs; Class B has the second highest with worst-case latency of 50 ms, and a measurement interval of 250 μs. The maximum number of hops is 7. The per-port peer delay provided by gPTP and the network bridge residence delay are added to calculate the accumulated delays and ensure the latency requirement is met. Control traffic has the third highest priority and includes gPTP and SRP traffic.

The SRP works using the Multiple MAC Registration Protocol (MMRP), the Multiple VLAN Registration Protocol (MVRP), and the Multiple Stream Registration Protocol (MSRP). MMRP controls propagation of group registration, and MVRP controls VLAN membership (MAC address information).

MSRP works in a distributed network of bridges and end stations; it registers and advertises data streams and reserves bridge resources to provide the QoS guarantees.

SRP essentially operates in the following sequence:

1. Advertise a stream from a talker
2. Register the paths along data flow
3. Calculate worst-case latency
4. Create an AVB domain
5. Reserve the bandwidth for the stream

A station (talker) sends a reservation request with the general MRP application. All participants in the stream have an MSRP application and the MRP Attribute Declaration (MAD) specification for describing the stream characteristics. Then each bridge within the same SRP domain can map, allocate, and forward the stream with the necessary resources by using the MRP attribute propagation.
