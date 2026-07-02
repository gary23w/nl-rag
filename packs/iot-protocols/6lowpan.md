---
title: "6LoWPAN"
source: https://en.wikipedia.org/wiki/6LoWPAN
domain: iot-protocols
license: CC-BY-SA-4.0
tags: iot, internet of things, mqtt, coap, zigbee, lora, bluetooth low energy, smart home
fetched: 2026-07-02
---

# 6LoWPAN

**6LoWPAN** (**IPv6 over Low-Power Wireless Personal Area Networks**) was a working group of the Internet Engineering Task Force (IETF). It was created with the intention of applying the Internet Protocol (IP) even to the smallest devices, enabling low-power devices with limited processing capabilities to participate in the Internet of Things.

The 6LoWPAN group defined encapsulation, header compression, neighbor discovery and other mechanisms that allow IPv6 to operate over IEEE 802.15.4 based networks. Although IPv4 and IPv6 protocols do not generally care about the physical and MAC layers they operate over, the low-power devices and small packet size defined by IEEE 802.15.4 make it desirable to adapt to these layers.

The base specification developed by the 6LoWPAN IETF group is RFC 4944 (updated by RFC 6282 with header compression, RFC 6775 with neighbor discovery optimization, RFC 8931 with selective fragment recovery and with smaller changes in RFC 8025 and RFC 8066). The problem statement document is RFC 4919. IPv6 over Bluetooth Low Energy using 6LoWPAN techniques is described in RFC 7668.

## Application areas

The targets for IPv6 networking for low-power radio communication are devices that need wireless connectivity to many other devices at lower data rates for devices with very limited power consumption. The header compression mechanisms in RFC 6282 are used to allow IPv6 packets to travel over such networks.

IPv6 is also in use on the smart grid enabling smart meters and other devices to build a micro mesh network before sending the data back to the billing system using the IPv6 backbone. Some of these networks run over IEEE 802.15.4 radios, and therefore use the header compression and fragmentation as specified by RFC6282.

### Thread

Thread is a standard from a group of more than fifty companies for a protocol running over 6LoWPAN to enable home automation. The specification is available at no cost as of 24 June 2022, but paid membership is required to implement the protocol. Version 1.0 of the specification was published on 2015-10-29. The protocol most directly competes with Z-Wave and Zigbee IP. In IoT device communications using the Matter standard, Thread is one of two possible wireless transport layers.

## Functions

As with all link-layer mappings of IP, RFC4944 provides a number of functions. Beyond the usual differences between L2 and L3 networks, mapping from the IPv6 network to the IEEE 802.15.4 network poses additional design challenges (see RFC 4919 for an overview).

### Adapting the packet sizes of the two networks

IPv6 requires the link maximum transmission unit (MTU) to be at least 1280 octets. In contrast, IEEE 802.15.4's standard frame size is 127 octets. A maximum frame overhead of 25 octets and an optional but highly recommended security feature at the link layer poses an additional overhead of up to 21 octets are for AES-CCM-128. This leaves only 81 octets for the upper layers. Since this is so much less than 1280, 6LoWPAN defines a fragmentation and reassembly layer. Further, the standard IPv6 Header is 40 octets long, so header compression is defined as well.

### Address resolution

IPv6 nodes are assigned 128 bit IP addresses in a hierarchical manner, through an arbitrary length network prefix. IEEE 802.15.4 devices may use either of IEEE 64 bit extended addresses or, after an association event, 16 bit addresses that are unique within a PAN. There is also a PAN-ID for a group of physically collocated IEEE 802.15.4 devices.

### Differing device designs

IEEE 802.15.4 devices are intentionally constrained in form factor to reduce costs (allowing for large-scale network of many devices), reduce power consumption (allowing battery powered devices) and allow flexibility of installation (e.g. small devices for body-worn networks). On the other hand, wired nodes in the IP domain are not constrained in this way; they can be larger and make use of mains power supplies.

### Differing focus on parameter optimization

IPv6 nodes are geared towards attaining high speeds. Algorithms and protocols implemented at the higher layers such as TCP kernel of the TCP/IP are optimized to handle typical network problems such as congestion. In IEEE 802.15.4-compliant devices, energy conservation and code-size optimization remain at the top of the agenda.

### Adaptation layer for interoperability and packet formats

An adaptation mechanism to allow interoperability between IPv6 domain and the IEEE 802.15.4 can best be viewed as a layer problem. Identifying the functionality of this layer and defining newer packet formats, if needed, is an enticing research area. RFC 4944 proposes an adaptation layer to allow the transmission of IPv6 datagrams over IEEE 802.15.4 networks.

### Addressing management mechanisms

The management of addresses for devices that communicate across the two dissimilar domains of IPv6 and IEEE 802.15.4 is cumbersome, if not exhaustingly complex.

### Routing considerations and protocols for mesh topologies in 6LoWPAN

Routing per se is a two phased problem that is being considered for low-power IP networking:

- Mesh routing in the personal area network (PAN) space.
- The routability of packets between the IPv6 domain and the PAN domain.

Several routing protocols have been proposed by the 6LoWPAN community such as LOAD, DYMO-LOW, HI-LOW. However, only two routing protocols are currently legitimate for large-scale deployments: LOADng standardized by the ITU under the recommendation ITU-T G.9903 and RPL standardized by the IETF ROLL working group.

### Routing

The 6LoWPAN routing scheme can be carried out in two different ways: *mesh-under* and *route-over*.

*Mesh-under* consists of implementing routing at the adaptation layer (which takes place between the link layer and the network layer of the model OSI), while *route-over* performs this implementation at the network layer (see 6LoWPAN routing scheme). In *route-over*, the IPv6 packet is reconstituted on each intermediate device in order to make the routing decision. Conversely, in *mesh-under*, the routing decision is made at the 6LoWPAN level and therefore only with fragments of the IPv6 packet. In this case, the IPv6 packet is only reconstituted on the recipient equipment. Therefore :

- *mesh-under* allows for a shorter transmission time;
- *route-over* is more effective in degraded conditions (packet loss).

Improved versions of mesh-under and route-over have been proposed :

- *Controlled mesh under* : By analyzing the contents of the header of the first fragment, equipment can know which fragments are expected next. If the next fragment received does not correspond to the expected fragment, the equipment requests its reissue;
- *Enhanced route over* A virtual circuit is created by associating the IPv6 address and the field *datagram_tag* from the header of the first fragment. The virtual circuit is then taken by all the fragments having the same *datagram_tag*.

Initially, several routing protocols were developed by the 6LoWPAN community, such as LOAD, DYMO-LOW, HI-LOW .

Today, only two protocols are legitimate for large deployments:

- LOADng (*Lightweight On-demand Ad hoc distance-vector routing protocol – next generation*), the successor to LOAD, a protocol *mesh-under*, standardized to the ITU within the recommendation ITU-T G.9903. This standard is used in particular within the program Linky communicating electricity meters.
- RPL (*Routing Protocol for Low power and Lossy Networks*, "routing protocol for LLN"), a protocol *route-over*, standardized within the ROLL working group from the IETF responsible for defining routing mechanisms for LLNs (*Low Power and Lossy Network*, "low power and lossy networks").

### Device and service discovery

Since IP-enabled devices may require the formation of ad hoc networks, the current state of neighboring devices and the services hosted by such devices will need to be known. IPv6 neighbour discovery extensions is an internet draft proposed as a contribution in this area.

### Security

IEEE 802.15.4 nodes can operate in either secure mode or non-secure mode. Two security modes are defined in the specification in order to achieve different security objectives: Access Control List (ACL) and Secure mode

### Header compression

There RFC 4944 defines the IPv6 header compression mechanism for LowPAN: LOWPAN_HC1. It also includes compression of the UDP header over 4 bytes, but does not allow compression of the *Checksum*. Additionally, it restricts the range of UDP ports from 61616 to 61631 in order to compress this value to 4 bits.

This IPv6 header compression can only be applied to local link addresses. To overcome this problem, an IETF LOWPAN_HC1g draft was published. LOWPAN_HC1g applies to global addresses for IP multi-hop communications. These two compression mechanisms (LOWPAN_HC1 and LOWPAN_HC1g) are complementary. It is therefore necessary to implement both.

Today the proposal of the 6LoWPAN group is to use LOWPAN_IPHC. It replaces LOWPAN_HC1 and LOWPAN_HC1g. IPHC bytes result from compression of the IPv6 header. They mainly integrate information from quality of service (DSCP and ECN), next headers, number of hops and compressed source/destination addresses.

With LOWPAN_IPHC the compression rate depends on the type of communication :

- For communications over a local link, the IPv6 header can be reduced to 2 bytes (1-byte Dispatch and 1-byte LOWPAN_IPHC).
- For communications requiring multiple IP hops, the header can be compressed to 7 bytes (1-byte Dispatch, 1-byte LOWPAN_IPHC, 1-byte Hop Limit, 2-byte Source Address, and 2-byte Destination Address).

The example below shows the increase in payload compared to the original problem (see 1re figure). This payload is in the best case 70 to 75 bytes. Indeed, if we add the fragmentation information as indicated in the paragraph above, it will decrease to 65-70 bytes for this scenario.

## History of 6LoWPAN

Technological developments in the 1990s (miniaturization of electronics, deployment of new wireless networks and embedded systems) enabled the emergence of new applications for sensor and actuator networks. With the advent of wireless technologies, the first solutions used were completely proprietary (for example Z-Wave or EnOcean). With the standard IEEE 802.15.4 (radio use of wireless sensors) new proprietary standards have appeared (for example, ZigBee, WirelessHART **(in)**, etc.).

When first thinking about wireless sensor networking, 6LoWPAN was born from a simple idea: why reinvent a protocol when we already have IP? ".

**2001**

Geoff Mulligan proposes the use of IP on 802.15.4 for sensor type equipment. Although receiving unfavorable feedback from several groups like Zigbee, others like

Internet 0

of

MIT's Center for Bits and Atoms

or the working group ROHC (from english

RObust Header Compression

, "robust header compression") of IETF were interested.

**2005**

- THE International Telecommunications Union publishes a theme onInternet of Things which is a reference today.
- THEI ETF creates the 6LoWPAN group to work specifically on the subject of implementing IP in wireless sensor networks.
- Geoff Mulligan proposes using the name Quibble for Quad Nibble (each of the 4 parts of an IPv6 address).

**2007**

- Maher Chebbo, member of the European Technology Platform Smart Grid ", indicates that the " smart grids " electrical integrating "smart objects" " which make it possible to manage and optimize electricity consumption are strategic.
- THE United States launch a program to support the development of smart grids for the modernization of electricity transmission and distribution system to maintain reliable and secure electricity infrastructure.

**March**

A first implementation of 6LoWPAN on TinyOS released on the implementation of "Arch Rock Company: Primer Pack/IP".

**April**

A first implementation of 6LoWPAN on TinyOS is available on the implementation of "Sensinode Company: NanoStack v0.9.4".

**August**

The 6LoWPAN group publishes the RFC 4919 to ensure the interoperability of the network layer.

**September**

There RFC 4944 sees the light of day, based on the RFC4919. This should allow direct connectivity to the Internet of LoWPAN equipment via IPv6 and replace them communication protocols owners like ZigBee,, which was developed after the end of the Smart Dust project.

**2008**

- The first tests demonstrate that the equipment of a 6LoWPAN network using the battery UIP (micro IP) (also noted ųIPv6) could meet the requirements of phase 1 *from IPv6 Ready*. The implementation of the ųIPv6 stack consumes very little resources (less than 12 KB ROM and less than 2KB of RAM). That same year, Arch Rock launched a commercial IPv6/6LoWPAN product meeting the requirements *from IPv6 Ready* phase 2 (Gold). In addition, a four-week experiment in a real environment shows that the use of 6LoWPAN networks is realistic (message delivery rate of 99.98% and average latency rate per hop < 62 ms).
- The United States National Intelligence Council (*National Intelligence Council*, NIC) indicates that the Internet of Things (IoT) is one of the disruptive technologies that will structure trends until 2025.

**July**

The IETF launches the ROLL Working Group.

**September**

The IPSO alliance (from English

IP for Smart Objects

, "IP for Smart Objects"), chaired by Geoff Mulligan, is created to promote the use of IP in smart objects. Smart objects are small type objects switch, detector more commonly called sensors.

**2009**

- Tests show the interoperability of certain implementations of 6LoWPAN (Berkeley IP, Arch Rock, SICSlowpan, Sensinode and Hitachi) having operating systems open source " (TinyOS and Contiki) and owners (Sensinode and Hitachi).
- Book release *6LoWPAN: The Wireless Embedded Internet* by Zach Shelby and Carsten Bormann, one of the two reference books on 6LoWPAN

**October**

To develop smart grids, President Obama announces an investment of $3.4 billion.

**2010**

- A 12-month experiment in different environments shows that the implementation of 6LoWPAN networks is viable (message delivery rate > 99.9% and average latency rate per hop < 125 ms).
- Book release *Interconnecting Smart Objects with IP: The Next Internet* by Jean-Philippe Vasseur and Adam Dunkels, one of the two reference books concerning 6LoWPAN.

**January**

Study demonstrates significant economic prospects in IoT.

**March**

- The IETF launches the new CORE working group.
- A report indicates that better management of heart failure, through sensor systems remotely monitoring weight, blood pressure, heart rate and rhythm, could reduce health costs (hospitalization and treatment) by one billion dollars per year in the United States. Likewise, the use of IoT in transport could reduce the number of accidents on the road and thus save around 100 billion dollars per year.

**September**

Cisco buys the company Arch Rock (one of the leaders in BAC applications for WSN), which strengthens the strategic alliance previously signed between Cisco and Itron (metering specialist smart grid),.

**2011**

**January**

- A new IETF working group, LWIG (from english *Light-Weight Implementation Guidance*, "light implementation tips") is created with the aim of optimizing the 6loWPAN stack (less memory usage, power consumption and complexity) for better performance of 6LoWPAN equipment. Currently in this working group we find:
- A guide to implementing one API 6loWPAN
- A study on the problems of interconnection of 6LoWPAN to IPv4 networks as well as some solutions.
