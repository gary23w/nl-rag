---
title: "Cable modem termination system"
source: https://en.wikipedia.org/wiki/Cable_modem_termination_system
domain: docsis-cable
license: CC-BY-SA-4.0
tags: docsis standard, cable modem, cable termination system, hybrid fiber coax
fetched: 2026-07-02
---

# Cable modem termination system

A **cable modem termination system** (**CMTS**, also called a **CMTS Edge Router**) is a piece of equipment, typically located in a cable company's headend or hubsite, which is used to provide data services, such as cable Internet or Voice over IP, to cable subscribers.

A CMTS provides similar functions to a DSLAM in a digital subscriber line or an optical line termination in a passive optical network.

## Connections

### Mechanism

In order to provide high speed data services, a cable company will connect its headend to the Internet via very high capacity data links to a network service provider. On the subscriber side of the headend, the CMTS enables communication with subscribers' cable modems. Different CMTSs are capable of serving different cable modem population sizes—ranging from 4,000 cable modems to 150,000 or more, depending in part on traffic and thus number of channels allocated to each service group and the size of the service groups, although it is recommended for an I-CMTS to service, for example, 30,000 subscribers (cable modems). A given headend may have between 1–12 CMTSs to service the cable modem population served by that headend or HFC hub.

One way to think of a CMTS is to imagine a router with Ethernet interfaces (connections) on one side and coaxial cable RF interfaces on the other side. The Ethernet side is known as the Network Side Interface or NSI.

### Service groups and channels

A service group is a group of customers that share communication RF channels and thus bandwidth. A CMTS has separate RF interfaces and connectors for downlink and uplink signals. The RF/coax interfaces carry RF signals to and from coaxial "trunks" connected to subscribers' cable modems, using one pair of connectors per trunk, one for downlink and the other for uplink. In other words, there can be a pair of RF connectors for every service group, although it is possible to configure a network with different numbers of connectors that service a set of service groups, based on the number of downstream and upstream channels the cable modems in every service group use. Every connector has a finite number of channels it can carry, such as 16 channels per downstream connector, and 4 channels per upstream connector, depending on the CMTS. For example, if the cable modems on every service group use 24 channels for downstream, and 2 channels for upstream, then 3 downstream connectors can service the cable modems on two service groups, and be serviced by 1 upstream connector. A service group may serve up to 500 households. A service group has channels, whose bandwidth is shared among all members of the service group. The channels are later regrouped at the cable headend or distribution hub and serviced by CMTSs and other equipment such as Edge QAMs.

### Splitting and combining

The RF signals from a CMTS are connected via coaxial cable to headend RF management modules for RF splitting and combining, with other equipment such as other CMTSs so that several CMTS can service one service group, and then to an "optics platform" or headend platform, which has transmitter and receiver modules that turn the RF signals into light pulses for delivery over fiber optics through an HFC network. Examples of optics platforms are the Arris CH3000 and Cisco Prisma II. At the other end of the network, an optical node converts the light pulses into RF signals again and sends them through a coaxial cable "trunk". The trunk has one or more amplifiers along its length, and on the trunk there are distribution "taps" to which customers' modems are connected via coaxial cable.

In fact, most CMTSs have both Ethernet interfaces (or other more traditional high-speed data interfaces like SONET) as well as RF interfaces. In this way, traffic that is coming from the Internet can be routed (or bridged) through the Ethernet interface, through the CMTS and then onto the RF interfaces that are connected to the cable company's **hybrid fiber coax** (HFC). The traffic winds its way through the HFC to end up at the cable modem in the subscriber's home. Traffic from a subscriber's home system goes through the cable modem and out to the Internet in the opposite direction.

### Traffic types and security

CMTSs typically carry only IP traffic. Traffic destined for the cable modem from the Internet, known as downstream traffic, is carried in IP packets encapsulated according to DOCSIS standard. These packets are carried on data streams that are typically modulated onto a TV channel using either 64-QAM or 256-QAM versions of quadrature amplitude modulation.

Upstream data (data from cable modems to the headend or Internet) is carried in Ethernet frames encapsulated inside DOCSIS frames modulated with QPSK, 16-QAM, 32-QAM, 64-QAM or 128-QAM using TDMA, ATDMA or S-CDMA frequency sharing mechanisms. This is usually done at the "subband" or "return" portion of the cable TV spectrum (also known as the "T" channels), a much lower part of the frequency spectrum than the downstream signal, usually 5–42 MHz in DOCSIS 2.0 or 5–65 MHz in EuroDOCSIS.

A typical CMTS allows a subscriber's computer to obtain an IP address by forwarding DHCP requests to the relevant servers. This DHCP server returns, for the most part, what looks like a typical response including an assigned IP address for the computer, gateway/router addresses to use, DNS servers, etc.

The CMTS may also implement some basic filtering to protect against unauthorized users and various attacks. Traffic shaping is sometimes performed to prioritize application traffic, perhaps based upon subscribed plan or download usage and also to provide guaranteed Quality of service (QoS) for the cable operator's own PacketCable-based VOIP service. However, the function of traffic shaping is more likely done by a Cable Modem or policy traffic switch. A CMTS may also act as a bridge or router.

A customer's cable modem cannot communicate directly with other modems on the line. In general, cable modem traffic is routed to other cable modems or to the Internet through a series of CMTSs and traditional routers. However, a route could conceivably pass through a single CMTS.

### Converged cable access platforms

A **CCAP** (Converged Cable Access Platform) combines CMTS and Edge QAM functionality in a single device so that it can provide both data (internet) with CMTS functionality, and video (TV channels) with Edge QAM functionality. Edge QAM (Quadrature Amplitude Modulator/Modulation) converts video sent via IP (internet protocol) or otherwise, into a QAM signal for delivery over a cable network. Edge QAMs are normally standalone devices placed at the "edge" of a network. They can also be connected to a CMTS core, to make up an M-CMTS system which is more scalable. A CMTS core is normally a conventional or I-CMTS that supports operation as a CMTS core in an M-CMTS system.

## Architectures

A CMTS can be broken down into several different architectures, Integrated CMTS (I-CMTS), Modular (M-CMTS), Virtual CMTS (vCMTS) and remote CMTS. An I-CMTS incorporates into a single unit all components necessary for its operation. There are both pros and cons to each type of architecture.

### Modular CMTS (M-CMTS)

In a M-CMTS solution the architecture of an I-CMTS is broken up into two components. The first part is the Physical Downstream component (PHY) which is known as the Edge QAM (EQAM). The second part is the IP networking and DOCSIS MAC Component which is referred to as the M-CMTS Core. There are also several new protocols and components introduced with this type of architecture. One is the DOCSIS Timing Interface, which provides a reference frequency between the EQAM and M-CMTS Core via a DTI Server. The second is the Downstream External PHY Interface (DEPI). The DEPI protocol controls the delivery of DOCSIS frames from the M-CMTS Core to the EQAM devices Some of the challenges that entail an M-CMTS platform are increased complexity in RF combining and an increase in the number of failure points. One of the benefits of an M-CMTS architecture is that it is extremely scalable to larger numbers of downstream channels.

### Virtual CMTS

Virtual CCAPs (vCCAPs) or virtual CMTSs (vCMTSs) are implemented on commercial off the shelf x86-based servers with specialized software, and can be used to increase service capacity without purchasing new CMTS/CCAP chassis, or add features to the CMTS/CCAP more quickly.

### Remote CMTS

Remote CMTS/Remote CCAP moves all CMTS/CCAP functionality to the outside plant, in stark contrast to conventional CMTSs or CCAPs which are installed at a service provider location.

## Manufacturers

### Current

- ARRIS Group
- C9 Networks
- Catapult Technologies
- Coaxial Networks Inc.
- Casa Systems
- Cisco Systems
- Chongqing Jinghong
- Damery sa
- Gainspeed (Nokia company) Archived 2016-07-13 at the Wayback Machine
- WISI Communications GmbH
- Kathrein
- Suma Scientific
- Huawei Technologies
- Harmonic Inc.
- Teleste
- Vecima Networks

### Historical

- 3COM (Acquired by HP)
- Broadband Access Systems (Acquired by ADC Telecommunications)
- ADC Telecommunications (CMTS business acquired by BigBand Networks)
- BigBand Networks (Exited CMTS business, remaining business later acquired by ARRIS)
- Cadant (Acquired by ARRIS)
- Com21 (CMTS business acquired by ARRIS)
- RiverDelta (Acquired by Motorola)
- Terayon (Acquired by Motorola)
- Pacific Broadband Communications (Acquired by Juniper Networks)
- Juniper Networks (Exited CMTS business)
- LanCity (Acquired by BayNetworks)
- Motorola (Acquired by ARRIS)
- Daphne sa (Acquired by Damery sa)
- Scientific Atlanta (Acquired by Cisco)
