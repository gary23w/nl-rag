---
title: "Audio Video Bridging"
source: https://en.wikipedia.org/wiki/Audio_Video_Bridging
domain: time-sensitive-networking
license: CC-BY-SA-4.0
tags: time-sensitive networking, bounded latency, deterministic ethernet, scheduled traffic
fetched: 2026-07-02
---

# Audio Video Bridging

**Audio Video Bridging (AVB)** is a common name for a set of technical standards that provide improved synchronization, low latency, and reliability for switched Ethernet networks. AVB embodies the following technologies and standards:

- IEEE 802.1AS-2011: Timing and Synchronization for Time-Sensitive Applications (gPTP);
- IEEE 802.1Qav-2009: Forwarding and Queuing for Time-Sensitive Streams (FQTSS);
- IEEE 802.1Qat-2010: Stream Reservation Protocol (SRP);
- **IEEE 802.1BA-2011**: Audio Video Bridging (AVB) Systems;
- IEEE 1722-2011 Layer 2 Transport Protocol for Time-Sensitive Applications (AV Transport Protocol, AVTP); and
- IEEE 1722.1-2013 Device Discovery, Enumeration, Connection Management and Control Protocol (AVDECC).

IEEE 802.1Qat and 802.1Qav amendments have been incorporated to the base IEEE 802.1Q-2011 document, which specifies the operation of Media Access Control (MAC) Bridges and Virtual Bridged Local Area Networks.

AVB was initially developed by the Institute of Electrical and Electronics Engineers (IEEE) Audio Video Bridging task group of the IEEE 802.1 standards committee. In November 2012, Audio Video Bridging task group was renamed to Time-Sensitive Networking task group to reflect the expanded scope of its work, which is to "provide the specifications that will allow time-synchronized low latency streaming services through IEEE 802 networks". Further standardization efforts are ongoing in IEEE 802.1 TSN task group.

To help ensure interoperability between devices that implement the AVB and TSN standards, the AVnu Alliance develops device certification for the automotive, consumer, and professional audio and video markets.

## Background

Analog audio-video (AV) equipment historically used one-way, single-purpose, point-to-point connections. Even digital AV standards, such as S/PDIF for audio and the serial digital interface (SDI) for video, retain these properties. This connection model results in large masses of cables, especially in professional applications and high-end audio.

Attempts to solve these problems were based on multi-point network topologies, such as IEEE 1394 (FireWire), and included adaptation of standard switched computer network technologies such as Audio over Ethernet and Audio over IP. Professional, home, and automotive AV solutions came to use specialized protocols that do not interoperate with each other or standard IT protocols, while standard computer networks did not provide tight quality of service with strict timing and predictable or bounded latency.

To overcome these limitations, Audio Video Bridging networks transmit multiple audiovisual streams through standard Ethernet switches (i.e. *MAC bridges*) connected in a hierarchical tree topology. AVB includes layer 2 protocols to reserve connection bandwidth and prioritise network traffic, which guarantee precise sync clock and low transmission latency for each stream.

Tight sync between multiple AV streams is needed for lip sync between video and related audio streams, to keep multiple digitally connected speakers in phase in a professional environment (which requires 1 μs precision), and to prevent audio or video packets from arriving late to the endpoint, resulting in a dropped frame of video and unwanted audio glitches such as a pop or silence. Worst-case delay, including source and destination buffering, is required to be low and deterministic: the user-interface delay shall be around 50 ms, so that the pressing of a button and the resulting action are perceived as happening instantly, and 2 ms for live performance or studio work.

## Summary

Audio Video Bridging is implemented as a switched Ethernet network that works by reserving a fraction of the available Ethernet for AV traffic. The AVB architecture introduces three primary differences:

- Precise synchronization using Generalized Precision Time Protocol (gPTP) profile (IEEE 802.1AS),
- Traffic shaping for AV streams using frame priorities (IEEE 802.1Qav) and VLAN tags (IEEE 802.1Q), and
- Admission controls with Stream Reservation Protocol (IEEE 802.1Qat).

The IEEE 802.1BA is an umbrella standard for these three principal technologies, which defines application-specific configurations and operation procedures for devices in switched audio-video networks.

The new layer-2 configuration protocols work with backward-compatible extensions to the Ethernet 802.1 frame format; such minimal changes allow AVB devices to coexist and communicate in standard IT networks, however, only AVB-capable switches and endpoints can reserve network resources with admission control and synchronize local time to a master clock, which is required for low-latency time-sensitive traffic.

AVB traffic is replicated in a multicast manner, with one talker (stream initiator) and multiple listeners. AVB packets are sent at regular intervals in the allocated time slots, preventing collisions for AV traffic. AVB guarantees a latency of 2 ms for Class A traffic and 50 ms for Class B traffic over a maximum of 7 hops, with a transmission period of 125 μs for Class A and 250 μs for Class B traffic.

An IEEE 802.1AS network timing domain includes all devices that communicate using the gPTP protocol. The grandmaster is a device chosen as the reference clock; the 802.1BA specification requires every talker and network bridge to be grandmaster capable.

802.3 link management and 802.1AS link delay measurement protocols calculate the round-trip delay to the AVB endpoint; this needs to be better than worst-case wire delay from the 802.1AS peer delay algorithm.

Higher-level protocols may use 802.1AS clock information to set the exact presentation time for each AV stream.

## AV transport and configuration

### IEEE 1722 AVTP

IEEE Std 1722-2011 for a Layer 2 Audio Video Transport Protocol (AVTP) defines details for transmitting IEEE 1394/IEC 61883 streams and other AV formats, setting the presentation time for each AV stream, and manage latencies from worst case delay calculated by the gPTP protocol.

### IEEE 1722.1 AVDECC

IEEE Std 1722.1-2013 is a standard that provides AVB discovery, enumeration, connection management, and control (AVDECC) of devices using IEEE Std 1722-2011. AVDECC defines operations to discover device addition and removal, retrieve device entity model, connect and disconnect streams, manage device and connection status, and remote control devices.

## Interoperability

Higher-layer services can improve synchronisation and latency of media transmission by mapping the AVB Stream ID to internal stream identifiers and basing internal timestamps on gPTP master clock.

### IEEE 1733

IEEE Std 1733-2011 defines a Layer 3 protocol profile for Real-time Transport Protocol (RTP) applications with a RTCP payload format, which assigns the Stream ID from SRP to the RTP's Synchronization source identifier (SSRC), and correlates RTP timestamps for presentation time with 802.1AS gPTP master clock.

### AES67

AES67 is based on standard RTP over UDP/IP and IEEE 1588 Precision Time Protocol (PTPv2) for timing; interoperability with AVB/TSN can be achieved by linking IEEE 802.1AS timing information to AES67 PTPv2 payload data.

AES67 implementation with AVB interoperability has been demoed at InfoComm 2016.

### Milan

In 2018, the Avnu Alliance announced the Milan initiative to promote interoperability of AVB devices and provide product certification and testing.

The specification requires media clocking based on the AVTP CRF (Clock Reference Format) and sample rate of 48 kHz (optionally 96 and 192 kHz); audio stream format is based on AVTP IEC 61883-6 32-bit Standard AAF Audio Format with 1 to 8 audio channels per stream (optionally, 24- and 32-bit High Capacity Format with 56 and 64 channels). Redundancy is provided with two independent logical networks for every endpoint and a seamless switchover mechanism.

### DetNet

The IETF Deterministic Networking (DetNet) Working Group is working to define deterministic data paths with bounds on latency, loss, and packet delay variation (jitter), and high reliability. DetNet shall operate over both Layer 2 bridged segments and Layer 3 routed segments, relying on interoperability with AVB/TSN switches when possible.

One of the possible applications of DetNet is professional audio/video, such as music and film production, broadcast, cinema, live sound, and large venue (stadiums, halls, conference centers, theme parks, airports, train terminals, etc.) systems for public addressing, media streaming and emergency announcement. The stated goal is to enable geographically distributed, campus- or enterprise-wide Intranet for content delivery with bounded low latency (10-15 ms). A single network shall handle both A/V and IT traffic, with Layer 3 routing on top of AVB QoS networks to enable sharing content between Layer 2 AVB segments, and provide IntServ and DiffServ integration with AVB where possible. Unused reserved bandwidth shall be released for best-effort traffic. The protocol stack shall have Plug-and-play capabilities from top to bottom to reduce manual setup and administration, allow quick changes of network devices and network topology.

Large-scale AVB networks, like those used by the ESPN SportsCenter "Digital Center 2" broadcast facility, which hosts multiple individual studios, are laid with many miles of fiber and have ten Tbit/s of bandwidth for a hundred thousand signals transmitted simultaneously; in the absence of standards-based solution to interconnect individual AVB segments, a custom software-defined networking router is required.

## Standardization

The work on A/V streaming started at the IEEE 802.3re 'Residential Ethernet' study group in July 2004. In November 2005, it was moved to the IEEE 802.1 committee responsible for cross-network bridging standards.

| Standard | Title | Status | Publication Date |
|---|---|---|---|
| Audio Video Bridging (AVB) specifications |   |   |   |
| IEEE 802.1BA-2011 | Audio Video Bridging (AVB) Systems | Superseded by IEEE 802.1BA-2021 | 30 September 2011 |
| IEEE 802.1Qav-2009 | Forwarding and Queuing Enhancements for Time-Sensitive Streams (FQTSS) | Incorporated into IEEE 802.1Q-2011 Clause 34 | 5 January 2010 |
| IEEE 802.1Qat-2010 | Stream Reservation Protocol (SRP) | Incorporated into IEEE 802.1Q-2011 Clause 35 | 30 September 2010 |
| IEEE 802.1Q-2011 | Media Access Control (MAC) Bridges and Virtual Bridged Local Area Networks *(incorporates IEEE 802.1Qav and 802.1Qat amendmends)* | Superseded by IEEE 802.1Q-2014/2018/2022 | 31 August 2011 |
| IEEE 802.1AS-2011 | Timing and Synchronization for Time-Sensitive Applications in Bridged Local Area Networks (gPTP) | Superseded by IEEE 802.1AS-2020 | 30 March 2011 |
| Time-Sensitive Networking (TSN) specifications |   |   |   |
| IEEE 802.1AS-2020 | Timing and Synchronization for Time-Sensitive Applications (gPTP) | Current, amended by 802.1AS-2020/Cor1-2021 | 30 January 2020 |
| IEEE 802.1BA-2021 | TSN profile for Audio Video Bridging (AVB) Systems | Current | 12 December 2021 |
| IEEE 802.1Q-2022 | Bridges and Bridged Networks | Current | 22 December 2022 |
| Audio Video Transport Protocol (AVTP) and AVDECC specifications |   |   |   |
| IEEE 1733-2011 | Layer 3 Transport Protocol for Time-Sensitive Applications in Local Area Networks (RTP) | Current | 25 April 2011 |
| IEEE 1722-2011 | Layer 2 Transport Protocol for Time-Sensitive Applications in a Bridged Local Area Network (AVTP) | Superseded by IEEE 1722-2016 | 6 May 2011 |
| IEEE 1722-2016 | Layer 2 Transport Protocol for Time-Sensitive Applications in a Bridged Local Area Network (AVTP) | Current | 16 December 2016 |
| IEEE P1722b | AVTP - Amendment: New and Extended Streaming Formats | preparation | - |
| IEEE 1722.1-2013 | Device Discovery, Enumeration, Connection Management and Control Protocol (AVDECC) | Current | 23 August 2013 |
