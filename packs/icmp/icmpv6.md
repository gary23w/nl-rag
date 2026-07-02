---
title: "ICMPv6"
source: https://en.wikipedia.org/wiki/ICMPv6
domain: icmp
license: CC-BY-SA-4.0
tags: icmp, icmpv6, internet control message protocol, traceroute
fetched: 2026-07-02
---

# ICMPv6

**Internet Control Message Protocol version 6** (**ICMPv6**) is the implementation of the Internet Control Message Protocol (ICMP) for Internet Protocol version 6 (IPv6). ICMPv6 is an integral part of IPv6 and performs error reporting and diagnostic functions.

ICMPv6 has a framework for extensions to implement new features. Several extensions have been published, defining new ICMPv6 message types as well as new options for existing ICMPv6 message types. For example, Neighbor Discovery Protocol (NDP) is a node discovery protocol based on ICMPv6 which replaces and enhances functions of ARP. Secure Neighbor Discovery (SEND) is an extension of NDP with extra security. Multicast Listener Discovery (MLD) is used by IPv6 routers for discovering multicast listeners on a directly attached link, much like Internet Group Management Protocol (IGMP) is used in IPv4. Multicast Router Discovery (MRD) allows the discovery of multicast routers.

## Message types and formats

ICMPv6 messages may be classified as *error messages* and *information messages*. ICMPv6 messages are transported by IPv6 packets in which the IPv6 Next Header value for ICMPv6 is set to the value 58.

The ICMPv6 message consists of a header and the protocol payload. The header contains only three fields: *Type* (8 bits), *Code* (8 bits), and *Checksum* (16 bits).

ICMPv6 message

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

Type

Code

Checksum

4

32

Message body

8

64

⋮

⋮

**Type: 8 bits**

Specifies the type of the message. Values in the range from 0 to 127 (high-order bit is 0) indicate an error message, while values in the range from 128 to 255 (high-order bit is 1) indicate an information message.

**Code: 8 bits**

The

Code

field value depends on the message type and provides an additional level of message granularity.

**Checksum: 16 bits**

Provides a minimal level of integrity verification for the ICMP message. The checksum is calculated from the ICMP message (starting with the

Type

field), prepended with an IPv6

pseudo-header

.

See below.

**Message body: Variable**

Contents depends on the message.

### Types

Control messages are identified by the value in the *type* field. The *code* field gives additional context information for the message. Some messages serve the same purpose as the correspondingly named ICMP message types.

| Type | Code |   |   |
|---|---|---|---|
| Value | Meaning | Value | Meaning |
| ICMPv6 Error Messages |   |   |   |
| 1 | Destination unreachable | 0 | no route to destination |
| 1 | communication with destination administratively prohibited |   |   |
| 2 | beyond scope of source address |   |   |
| 3 | address unreachable |   |   |
| 4 | port unreachable |   |   |
| 5 | source address failed ingress/egress policy |   |   |
| 6 | reject route to destination |   |   |
| 7 | Error in Source Routing Header |   |   |
| 2 | Packet too big | 0 |   |
| 3 | Time exceeded | 0 | hop limit exceeded in transit |
| 1 | fragment reassembly time exceeded |   |   |
| 4 | Parameter problem | 0 | erroneous header field encountered |
| 1 | unrecognized Next Header type encountered |   |   |
| 2 | unrecognized IPv6 option encountered |   |   |
| 100 | Private experimentation |   |   |
| 101 | Private experimentation |   |   |
| 127 | Reserved for expansion of ICMPv6 error messages |   |   |
| ICMPv6 Informational Messages |   |   |   |
| 128 | Echo Request | 0 |   |
| 129 | Echo Reply | 0 |   |
| 130 | Multicast Listener Query (MLD) | 0 | There are two subtypes of Multicast Listener Query messages: General Query, used to learn which multicast addresses have listeners on an attached link. Multicast-Address-Specific Query, used to learn if a particular multicast address has any listeners on an attached link. These two subtypes are differentiated by the contents of the Multicast Address field, as described in section 3.6 of RFC 2710 |
| 131 | Multicast Listener Report (MLD) | 0 |   |
| 132 | Multicast Listener Done (MLD) | 0 |   |
| 133 | Router Solicitation (NDP) | 0 |   |
| 134 | Router Advertisement (NDP) | 0 |   |
| 135 | Neighbor Solicitation (NDP) | 0 |   |
| 136 | Neighbor Advertisement (NDP) | 0 |   |
| 137 | Redirect Message (NDP) | 0 |   |
| 138 | Router Renumbering | 0 | Router Renumbering Command |
| 1 | Router Renumbering Result |   |   |
| 255 | Sequence Number Reset |   |   |
| 139 | ICMP Node Information Query | 0 | The Data field contains an IPv6 address which is the Subject of this Query. |
| 1 | The Data field contains a name which is the Subject of this Query, or is empty, as in the case of a NOOP. |   |   |
| 2 | The Data field contains an IPv4 address which is the Subject of this Query. |   |   |
| 140 | ICMP Node Information Response | 0 | A successful reply. The Reply Data field may or may not be empty. |
| 1 | The Responder refuses to supply the answer. The Reply Data field will be empty. |   |   |
| 2 | The Qtype of the Query is unknown to the Responder. The Reply Data field will be empty. |   |   |
| 141 | Inverse Neighbor Discovery Solicitation Message | 0 |   |
| 142 | Inverse Neighbor Discovery Advertisement Message | 0 |   |
| 143 | Multicast Listener Discovery (MLDv2) reports |   |   |
| 144 | Home Agent Address Discovery Request Message | 0 |   |
| 145 | Home Agent Address Discovery Reply Message | 0 |   |
| 146 | Mobile Prefix Solicitation | 0 |   |
| 147 | Mobile Prefix Advertisement | 0 |   |
| 148 | Certification Path Solicitation (SEND) |   |   |
| 149 | Certification Path Advertisement (SEND) |   |   |
| 151 | Multicast Router Advertisement (MRD) |   |   |
| 152 | Multicast Router Solicitation (MRD) |   |   |
| 153 | Multicast Router Termination (MRD) |   |   |
| 155 | RPL Control Message |   |   |
| 160 | Extended Echo Request | 0 | Request Extended Echo |
| 161 | Extended Echo Reply | 0 | No Error |
| 1 | Malformed Query |   |   |
| 2 | No Such Interface |   |   |
| 3 | No Such Table Entry |   |   |
| 4 | Multiple Interfaces Satisfy Query |   |   |
| 200 | Private experimentation |   |   |
| 201 | Private experimentation |   |   |
| 255 | Reserved for expansion of ICMPv6 informational messages |   |   |

Note that the table above is not comprehensive. The current complete list of assigned ICMPv6 types can be found at this link: IANA: ICMPv6 Parameters.

### Checksum

ICMPv6 provides a minimal level of message integrity verification by the inclusion of a 16-bit checksum in its header. The checksum is calculated starting with a pseudo-header of IPv6 header fields according to the IPv6 standard, which consists of the source and destination addresses, the packet length and the next header field, the latter of which is set to the value 58. Following this pseudo header, the checksum is continued with the ICMPv6 message. The checksum computation is performed according to Internet protocol standards using 16-bit ones' complement summation, followed by a final ones' complement of the checksum itself and inserting it into the checksum field. Note that this differs from the way it is calculated for IPv4 in ICMP, but is similar to the calculation done in TCP.

ICMPv6 pseudo-header

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

Source Address

4

32

8

64

12

96

16

128

Destination Address

20

160

24

192

28

224

32

256

ICMPv6 Length

36

288

Zeroes

Next Header

(58)

### Format

The payload of an ICMPv6 message varies according to the type of message being sent. It begins at bit 32 immediately after the header described above. For some messages such as destination unreachable or time exceeded there is no defined message body.

| Bit offset | 0–7 | 8–15 | 16–31 |
|---|---|---|---|
| **0** | 1 | Code | Checksum |
| **32** | Unused |   |   |
| **64** | Message body (Variable Size) |   |   |

| Bit offset | 0–7 | 8–15 | 16–31 |
|---|---|---|---|
| **0** | 3 | Code | Checksum |
| **32** | Unused |   |   |
| **64** | Message body (Variable Size) |   |   |

Others define a use only for the first four bytes of the body with no other defined content:

| Bit offset | 0–7 | 8–15 | 16–31 |
|---|---|---|---|
| **0** | 2 | 0 | Checksum |
| **32** | MTU |   |   |
| **64** | Message body (Variable Size) |   |   |

| Bit offset | 0–7 | 8–15 | 16–31 |
|---|---|---|---|
| **0** | 4 | Code | Checksum |
| **32** | Pointer |   |   |
| **64** | Message body (Variable Size) |   |   |

| Bit offset | 0–7 | 8–15 | 16–31 |
|---|---|---|---|
| **0** | 128 | 0 | Checksum |
| **32** | Identifier | Sequence Number |   |
| **64** | Data (Variable Size) |   |   |

| Bit offset | 0–7 | 8–15 | 16–31 |
|---|---|---|---|
| **0** | 129 | 0 | Checksum |
| **32** | Identifier | Sequence Number |   |
| **64** | Data (Variable Size) |   |   |

In the case of NDP messages the first four bytes are either reserved or used for flags/hoplimit. While the rest of the body has unspecified structured data:

| Bit offset | 0–7 | 8–15 | 16–31 |
|---|---|---|---|
| **0** | 133 | 0 | Checksum |
| **32** | Reserved |   |   |
| **64** | Options (Variable Size) |   |   |

| Bit offset | 0–7 | 8–15 | 16–31 |   |   |
|---|---|---|---|---|---|
| **0** | 134 | 0 | Checksum |   |   |
| **32** | Cur Hop Limit | Managed Address Flag | Other Configuration Flag | Reserved | Router Lifetime |
| **64** | Reachable Time |   |   |   |   |
| **96** | Retrans Time |   |   |   |   |
| **128** | Options (Variable Size) |   |   |   |   |

| Bit offset | 0–7 | 8–15 | 16–31 |
|---|---|---|---|
| **0** | 135 | 0 | Checksum |
| **32** | Reserved |   |   |
| **64** | Target Address (16 bytes) |   |   |
| **192** | Options (Variable Size) |   |   |

| Bit offset | 0–7 | 8–15 | 16–31 |   |
|---|---|---|---|---|
| **0** | 136 | 0 | Checksum |   |
| **32** | From Router (R) | Solicited Flag(S) | Override(O) | Reserved |
| **64** | Target Address (16 bytes) |   |   |   |
| **192** | Options (Variable Size) |   |   |   |

For a redirect the first bytes of the message body are reserved but not used. This is followed by a Target and destination address. Unspecified options can be attached to the end:

| Bit offset | 0–7 | 8–15 | 16–31 |
|---|---|---|---|
| **0** | 137 | 0 | Checksum |
| **32** | Reserved |   |   |
| **64** | Target Address (16 bytes) |   |   |
| **192** | Destination Address (16 bytes) |   |   |
| **320** | Options (Variable Size) |   |   |

## Message processing

When an ICMPv6 node receives a packet, it must undertake actions that depend on the type of message. The ICMPv6 protocol must limit the number of error messages sent to the same destination to avoid network overloading. For example, if a node continues to forward erroneous packets, ICMP will signal the error to the first packet and then do so periodically, with a fixed minimum period or with a fixed network maximum load. An ICMP error message must never be sent in response to another ICMP error message.
