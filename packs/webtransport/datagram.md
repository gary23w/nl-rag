---
title: "Datagram"
source: https://en.wikipedia.org/wiki/Datagram
domain: webtransport
license: CC-BY-SA-4.0
tags: webtransport protocol, quic web transport, low-latency web transport, browser datagram transport
fetched: 2026-07-02
---

# Datagram

A **datagram** is a basic transfer unit associated with a packet-switched network. Datagrams are typically structured in header and payload sections. Datagrams provide a connectionless communication service across a packet-switched network. The delivery, arrival time, and order of arrival of datagrams need not be guaranteed by the network.

## History

In the early 1970s, the term *datagram* was created by combining the words *data* and *telegram* by the CCITT rapporteur on packet switching, Halvor Bothner-By. While the word was new, the concept had already a long history.

In 1964, Paul Baran described, in a RAND Corporation report, a hypothetical military network having to resist a nuclear attack. Small standardized *message blocks*, bearing source and destination addresses, were stored and forwarded in computer nodes of a highly redundant meshed computer network. Baran wrote: "The network user who has called up a *virtual connection* to an end station and has transmitted messages ... might also view the system as a black box providing an apparent circuit connection". The concept of what we now call a virtual circuit appears in the design, although no network was built.

In 1967, Donald Davies published a seminal article in which he introduced the *packet* and *packet switching*. His proposed core network is similar to the one proposed by Paul Baran though developed independently. He assumes that "all users of the network will provide themselves with some kind of error control". His target is a "common-carrier communication network". To support remote access to computer services by user terminals, which at that time were transmitted character by character, he included, at the network periphery, interface computers that convert character flows into packet flows and vice versa. Davies wrote: "we were really rather against the virtual circuit, because we believed that a communication network should only concern itself with packets, and that any protocols involved in assembling these packets should be done end-to-end, between the customers themselves."

In 1970, Lawrence Roberts and Barry D. Wessler published an article about ARPANET, the first multi-node packet-switching network. An accompanying paper described its switching nodes (the IMPs) and its packet formats. The network core performed datagram switching as in Baran's and Davies' model, but the service offered to hosts by the network was connection oriented. A reliable message transfer service was thus offered to user computers, thus greatly simplifying the network design. This made the ARPANET what would come to be called a virtual circuit network.

Roberts presented the idea of packet switching to the communication professionals and faced anger and hostility. Before ARPANET was operating, they argued that the router buffers would quickly run out. After the ARPANET was operating, they argued packet switching would never be economic without the government subsidy. Baran faced the same rejection and thus failed to convince the military to construct a packet-switching network.

In 1973, Louis Pouzin presented his design for CYCLADES, the first large-scale network implementing the pure Davies datagram model. The CYCLADES team has thus been the first to tackle the highly complex problem of providing user applications a reliable virtual circuit service while using the end-to-end principle in a network service known to possibly produce non-negligible datagram losses and reordering. Although Pouzin's concern "in a first stage is not to make breakthrough [sic] in packet switching technology, but to build a reliable communications tool for Cyclades", two members of his team, Hubert Zimmerman and Gérard Le Lann, made significant contributions to the design of Internet's TCP that Vint Cerf, its main designer, acknowledged.

In 1981, the Defense Advanced Research Projects Agency (DARPA) issued the first specification the Internet Protocol (IP). It introduced a major evolution of the datagram concept: *fragmentation.* With fragmentation, some parts of the global network may use large packet size (typically local area networks to minimize processing overhead), while some others may impose smaller packet sizes (typically wide area networks to minimize response time). Network nodes may fragment a datagram into several smaller packets.

In 1999, the Internet Engineering Task Force (IETF) sanctioned the use of the already largely deployed network address translation (NAT) whereby each public address can be shared by several private devices. With it, the forthcoming Internet Address exhaustion was delayed, leaving enough time to introduce IPv6, the new generation of Internet Protocol supporting longer addresses. The initial principle of full end to end network transparency to datagrams was for this relaxed: NAT nodes had to manage per-connection states, making them in part connection oriented.

In 2015, the IETF upgraded its *informational* 1998 RFC 2309 that datagram switching nodes perform active queue management, to make it a stronger and more detailed *best current practice* recommendation through the publication of RFC 7567. While the initial datagram queueing model was simple to implement and needed no more tuning than queue lengths, support of more sophisticated and parametrized mechanisms were found necessary "to improve and preserve Internet performance" (RED, ECN etc.). Further research on the subject was also called for, with a list of identified items.

## Definition

The term *datagram* is defined as follows:

> "A self-contained, independent entity of data carrying sufficient information to be routed from the source to the destination computer without reliance on earlier exchanges between this source and destination computer and the transporting network."

— RFC 1594

A datagram needs to be self-contained without reliance on earlier exchanges because there is no connection of fixed duration between the two communicating points as there is, for example, in most voice telephone conversations.

Datagram service is often compared to a mail delivery service; the user only provides the destination address but receives no guarantee of delivery, and no confirmation upon successful receipt. Datagram service is therefore considered unreliable. Datagram service routes datagrams without first creating a predetermined path. Datagram service is therefore considered connectionless. There is also no consideration given to the order in which it and other datagrams are sent or received. In fact, many datagrams in the same group can travel along different paths before reaching the same destination in a different order.

## Structure

Each datagram has two components, a header and a data payload. The header contains all the information sufficient for routing from the originating equipment to the destination without relying on prior exchanges between the equipment and the network. Headers may include source and destination addresses as well as type and length fields. The payload is the data to be transported. This process of nesting data payloads in a tagged header is called encapsulation.

## Examples

| OSI layer | Name |
|---|---|
| Layer 4 | TCP segment |
| Layer 3 | Network packet |
| Layer 2 | Ethernet frame (IEEE 802.3) Wireless LAN frame (IEEE 802.11) |
| Layer 1 | Chip (CDMA) |

### Internet Protocol

The Internet Protocol (IP) defines standards for several types of datagrams. The internet layer is a datagram service provided by an IP. For example, UDP is run by a datagram service on the internet layer. IP is an entirely connectionless, best effort, unreliable, message delivery service. TCP is a higher-level protocol running on top of IP that provides a reliable connection-oriented service.
