---
title: "RTP Control Protocol"
source: https://en.wikipedia.org/wiki/Real-time_Transport_Control_Protocol
domain: rtp-streaming
license: CC-BY-SA-4.0
tags: rtp streaming, real-time transport protocol, media streaming protocol, audio video transport
fetched: 2026-07-02
---

# RTP Control Protocol

(Redirected from

Real-time Transport Control Protocol

)

The **RTP Control Protocol** (**RTCP**) is a binary-encoded out-of-band signaling protocol that functions alongside the Real-time Transport Protocol (RTP). RTCP provides statistics and control information for an RTP session. It partners with RTP in the delivery and packaging of multimedia data but does not transport any media data itself.

The primary function of RTCP is to provide feedback on the quality of service (QoS) in media distribution by periodically sending statistics information such as transmitted octet and packet counts, packet loss, packet delay variation, and round-trip delay time to participants in a streaming multimedia session. An application may use this information to control quality of service parameters, perhaps by limiting flow, or using a different codec.

## Protocol functions

Typically, RTP will be sent on an even-numbered UDP port, with RTCP messages being sent over the next higher odd-numbered port.

RTCP itself does not provide any flow encryption or authentication methods. Such mechanisms may be implemented, for example, with the Secure Real-time Transport Protocol (SRTP)

RTCP provides basic functions expected to be implemented in all RTP sessions:

- The primary function of RTCP is to gather statistics on quality aspects of the media distribution during a session and transmit this data to the session media source and other session participants. Such information may be used by the source for adaptive media encoding (codec) and detection of transmission faults. If the session is carried over a multicast network, this permits non-intrusive session quality monitoring.
- RTCP provides canonical end-point identifiers (CNAME) to all session participants. Although a source identifier (SSRC) of an RTP stream is expected to be unique, the instantaneous binding of source identifiers to endpoints may change during a session. The CNAME establishes unique identification of endpoints across an application instance (multiple use of media tools) and for third-party monitoring.
- Provisioning of session control functions. RTCP is a convenient means to reach all session participants, whereas RTP itself is not. RTP is only transmitted by a media source.

RTCP reports are expected to be sent by all participants, even in a multicast session, which may involve thousands of recipients. Such traffic will increase proportionally with the number of participants. Thus, to avoid network congestion, the protocol must include session bandwidth management. This is achieved by dynamically controlling the frequency of report transmissions. RTCP bandwidth usage should generally not exceed 5% of the total session bandwidth. Furthermore, 25% of the RTCP bandwidth should be reserved to media sources at all times, so that in large conferences, new participants can receive the CNAME identifiers of the senders without excessive delay.

The RTCP reporting interval is randomized to prevent unintended synchronization of reporting. The recommended minimum RTCP report interval per station is 5 seconds. Stations should not transmit RTCP reports more often than once every 5 seconds.

## Packet header

RTCP packet header

Offset

Octet

0

1

2

3

Octet

Bit

0

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

0

0

Version

P

RC

PT

Length

4

32

SSRC Identifier

**Version: 2 bits**

Identifies the version of RTP, which is the same in RTCP packets as in RTP data packets. The version defined by this specification is two (2).

**Padding (P): 1 bit**

Indicates if there are extra padding bytes at the end of the RTP packet. Padding may be used to fill up a block of certain size, for example as required by an encryption algorithm. The last byte of the padding contains the number of padding bytes that were added (including itself).

**Reception Report Count (RC): 5 bits**

The number of reception report blocks contained in this packet. A value of zero is valid.

**Packet Type (PT): 8 bits**

Contains a constant to identify RTCP packet type.

**Length: 16 bits**

Indicates the length of this RTCP packet (including the header itself) in 32-bit units minus one.

**SSRC Identifier: 32 bits**

Synchronization Source Identifier

uniquely identifies the source of a stream.

Note that multiple reports can be concatenated into a single compound RTCP packet, each with its own packet header.

## Message types

RTCP distinguishes several types of packets: *sender report*, *receiver report*, *source description*, and *goodbye*. In addition, the protocol is extensible and allows application-specific RTCP packets. A standards-based extension of RTCP is the *extended report* packet type.

**Sender report (SR)**

The sender report is sent periodically by the active senders in a conference to report transmission and reception statistics for all RTP packets sent during the interval. The sender report includes two distinct timestamps, an absolute timestamp, represented using the timestamp format of the Network Time Protocol (NTP) (which is in seconds relative to midnight UTC on 1 January 1900) and an RTP timestamp that corresponds to the same time as the NTP timestamp, but in the same units and with the same random offset as the RTP timestamps in data packets described by this Sender Report.

The absolute timestamp allows the receiver to synchronize RTP messages. It is particularly important when both audio and video are transmitted simultaneously because audio and video streams use independent relative timestamps.

**Receiver report (RR)**

The receiver report is for passive participants, those that do not send RTP packets. The report informs the sender and other receivers about the quality of service.

**Source description (SDES)**

The Source Description message is used to send the CNAME item to session participants. It may also be used to provide additional information such as the name, e-mail address, telephone number, and address of the owner or controller of the source.

**Goodbye (BYE)**

A source sends a BYE message to shut down a stream. It allows an endpoint to announce that it is leaving the conference. Although other sources can detect the absence of a source, this message is a direct announcement. It is also useful to a media mixer.

**Application-specific message (APP)**

The application-specific message provides a mechanism to design application-specific extensions to the RTCP protocol.

## Scalability in large deployments

In large-scale applications, such as in Internet Protocol television (IPTV), very long delays (minutes to hours) between RTCP reports may occur, because of the RTCP bandwidth control mechanism required to control congestion (see § Protocol functions). Acceptable frequencies are usually less than one per minute. This affords the potential of inappropriate reporting of the relevant statistics by the receiver or causes evaluation by the media sender to be inaccurate relative to the current state of the session. Methods have been introduced to alleviate the problems: RTCP filtering, RTCP biasing and hierarchical aggregation.

### Hierarchical aggregation

The Hierarchical Aggregation (or also known as RTCP feedback hierarchy) is an optimization of the RTCP feedback model and its aim is to shift the maximum number of users limit further together with quality of service (QoS) measurement. The RTCP bandwidth is constant and takes just 5% of session bandwidth. Therefore, the reporting interval about QoS depends, among others, on the number of session members, and for very large sessions, it can become very high (minutes or even hours). However, the acceptable interval is about 10 seconds of reporting. Bigger values would cause time-shifted and very inaccurate reported status about the current session status, and any optimization made by the sender could even have a negative effect on network or QoS conditions.

The Hierarchical Aggregation is used with Source-Specific Multicast where only a single source is allowed, i.e., IPTV. Another type of multicast could be Any-Source Multicast, but it is not so suitable for large-scale applications with a huge number of users.

As of June 2007, only the most modern IPTV systems use Hierarchical aggregation.

Feedback Target is a new type of member that was first introduced by the Internet Draft draft-ietf-avt-rtcpssm-13. The Hierarchical Aggregation method has extended its functionality. The function of this member is to receive Receiver Reports (RR) (see RTCP) and retransmit summarized RR packets, so-called Receiver Summary Information (RSI) to a sender (in case of single-level hierarchy).

## Standards documents

- RFC 3550 – "*RTP: A Transport Protocol for Real-Time Applications,*" *Internet Standard 64.*
