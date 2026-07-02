---
title: "IEEE 802.1ah"
source: https://en.wikipedia.org/wiki/Provider_Backbone_Bridges
domain: metro-ethernet
license: CC-BY-SA-4.0
tags: metro ethernet, metropolitan area network, ethernet transport, service provider ethernet
fetched: 2026-07-02
---

# IEEE 802.1ah

(Redirected from

Provider Backbone Bridges

)

**IEEE 802.1ah** is an amendment to the IEEE 802.1Q networking standard which adds support for **Provider Backbone Bridges**. It includes an architecture and a set of protocols for routing over a provider's network, allowing interconnection of multiple provider bridge networks without losing each customer's individually defined VLANs. It was initially created by Nortel before being submitted to the IEEE 802.1 committee for standardization. The final version was approved by the IEEE in June 2008 and has been integrated into IEEE 802.1Q-2011.

## History

The now-ubiquitous Ethernet was initially defined as a local area network (LAN) technology to interconnect the computers within a small organization in which these host computers were very close in proximity to each other. Over the years, Ethernet has become such a popular technology that it became the default Data Link Layer (OSI Layer 2) mechanism for data transport. This created a need for extending the Ethernet from a customer LAN bridging domain to service provider MAN, also known as the Provider bridging domain. For this, a 4 byte S-Tag or Service Tag, a type of Virtual LAN tag, was added to the header of the Ethernet frame in IEEE 802.1ad standard. In the service provider domain, switching was based on S-Tag and destination MAC address, and C-tag was used to create virtual LAN within the customer domain. This technology is also known as QinQ or Q-tunneling.

QinQ does not offer true separation of customer and provider domains but is merely a way to overcome the limitations on the VLAN identifier space. It can also help in separation of the customer and provider control domains when used with other features like control protocol tunneling or Per-VLAN Spanning Tree etc. There is still the problem of having too little control on the MAC addresses, since QinQ forwarding is still based on the customer destination addresses. Thus, better mechanisms are needed.

## Description

The idea of PBB is to offer complete separation of customer and provider domains. For this purpose, a new Ethernet header has been defined. This header may take multiple different forms, but the main components of the header are:

Example Ethernet frame for Provider Backbone Bridges

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

Backbone Destination Address (B-DA)

4

32

8

64

Backbone Source Address (B-SA)

12

96

Backbone EtherType

(

0x88A8

)

BB Flags

Backbone VLAN Identifier (B-VID)

16

128

MIM EtherType

(

0x88E7

)

MIM Flags

MIM Service Identifier (I-SID)

↴

20

160

↪

MIM Service Identifier (I-SID)

24

192

Customer Destination Address (C-DA)

28

224

Customer Source Address (C-SA)

32

256

Customer VLAN EtherType

(0x8100)

36

288

C Flags

Customer VLAN Identifier (C-VID)

Customer Payload EtherType

(0x0800)

40

320

Customer Payload. An IPv4 packet, containing TCP with HTTPS, for example.

44

352

⋮

⋮

⋮

⋮

Frame Check Sequence

**Backbone Destination Address (B-DA): 48 bits**

Backbone destination MAC address.

**Backbone Source Address (B-SA): 48 bits**

Backbone source MAC address.

**Backbone EtherType: 16 bits**

Backbone EtherType. 0x88A8 indicates Service VLAN tag identifier (S-Tag).

**Backbone Flags: 4 bits**

Backbone flag bits. They are (in order, from most significant to least significant):

**Priority Code Point (PCP): 3 bits**

Priority Code Point.

**Drop Eligible Indicator (DEI): 1 bit**

Drop Eligible Indicator.

**Backbone VLAN ID (B-VID): 12 bits**

Backbone VLAN identifier.

**MIM EtherType: 16 bits**

MIM EtherType. 0x887E indicates Provider Backbone Bridges.

**MIM Flags: 8 bits**

Flag bits. They are (in order, from most significant to least significant):

**Priority Code Point (PCP): 3 bits**

Priority Code Point.

**Drop Eligible Indicator (DEI): 1 bit**

Drop Eligible Indicator.

**No Customer Access (NCA): 1 bit**

E.g. OAM frames.

**Reserved1 (Res1): 1 bit**

Reserved.

**Reserved2 (Res2): 2 bits**

Reserved.

**MIM Service Identifier (I-SID): 24 bits**

Service Instance VLAN ID.

**Customer Destination Address (C-DA): 48 bits**

Customer destination MAC address.

**Customer Source Address (C-SA): 48 bits**

Customer source MAC address.

The bridges in the PBB domain switch based on the B-VID and B-DA values, which contain 60 bits total. Bridges learn based on the B-SA and ingress port value and hence is completely unaware of the customer MAC addresses. I-SID allows distinguishing the services within a PBB domain. PBB is the foundation for the IEEE 802.1Qay PBB-TE standard, which was standardized in 2009.

PBB is sometimes referred to as MAC-in-MAC.
