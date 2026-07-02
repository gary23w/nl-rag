---
title: "Generic routing encapsulation"
source: https://en.wikipedia.org/wiki/Generic_Routing_Encapsulation
domain: vpn-tunneling
license: CC-BY-SA-4.0
tags: vpn tunneling, virtual private network, tunneling protocol, openvpn
fetched: 2026-07-02
---

# Generic routing encapsulation

(Redirected from

Generic Routing Encapsulation

)

**Generic routing encapsulation** (**GRE**) is a tunneling protocol developed by Cisco Systems that can encapsulate a wide variety of network layer protocols inside virtual point-to-point links or point-to-multipoint links over an Internet Protocol network.

## Example uses

- In conjunction with PPTP to create VPNs.
- In conjunction with IPsec VPNs to allow passing of routing information between connected networks.
- In mobility management protocols.
- In A8/A10 interfaces to encapsulate IP data to/from Packet Control Function (PCF).
- Linux and BSD can establish ad-hoc IP over GRE tunnels which are interoperable with Cisco equipment.
- Distributed denial of service (DDoS) protected appliance to an unprotected endpoint.

### Example protocol stack

| OSI model layer | Protocol example |
|---|---|
| 7. Application | HTTP |
| 4. Transport | TCP |
| 3. Network (GRE-encapsulated) | IPv4 |
| Encapsulation | **GRE** |
| 3. Network | IPv6 |
| 2. Data link | Ethernet |
| 1. Physical | Ethernet physical layer |

Based on the principles of protocol layering in OSI, protocol encapsulation, not specifically GRE, breaks the layering order. It may be viewed as a separator between two different protocol stacks, one acting as a carrier for another.

## Delivery protocols

GRE packets that are encapsulated within IP directly, use IP protocol type 47 in the IPv4 header's *Protocol* field or the IPv6 header's *Next Header* field.

For performance reasons, GRE can also be encapsulated in UDP packets. Better throughput may be achieved by using Equal-cost multi-path routing.

## Packet header

### Extended GRE packet header (RFC 2890)

The extended version of the GRE packet header is represented below:

Extended GRE header format

Offsets

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

C

K

S

Reserved 0

Version

Protocol Type

4

32

Checksum

(optional)

Reserved 1 (optional)

8

64

Key (optional)

12

96

Sequence Number (optional)

***C (1 bit)***

Checksum

bit. Set to 1 if a checksum is present.

***K (1 bit)***

Key bit. Set to 1 if a key is present.

***S (1 bit)***

Sequence number bit. Set to 1 if a sequence number is present.

***Reserved 0 (9 bits)***

Reserved bits; set to 0.

***Version (3 bits)***

GRE Version number; set to 0.

***Protocol Type (16 bits)***

Indicates the

ether protocol type

of the encapsulated payload. (For

IPv4

, this would be hex 0800.)

***Checksum (16 bits)***

Present if the

C

bit is set; contains the checksum for the GRE header and payload.

***Reserved 1 (16 bits)***

Present if the

C

bit is set; is set to 0.

***Key (32 bits)***

Present if the

K

bit is set; contains an application-specific key value.

***Sequence Number (32 bits)***

Present if the

S

bit is set; contains a sequence number for the GRE packet.

### Standard GRE packet header (RFC 2784)

A standard GRE packet header structure is represented in the diagram below.

Standard GRE header format

Offsets

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

C

Reserved 0

Version

Protocol Type

4

32

Checksum

(optional)

Reserved 1 (optional)

***C (1 bit)***

Checksum

bit. Set to 1 if a checksum is present.

***Reserved 0 (12 bits)***

Reserved bits; set to 0.

***Version (3 bits)***

GRE Version number; set to 0.

***Protocol Type (16 bits)***

Indicates the

ether protocol type

of the encapsulated payload. (For

IPv4

, this would be

hexadecimal

0x0800; for

IPv6

, it would be 0x86DD.

)

***Checksum (16 bits)***

Present if the

C

bit is set; contains the checksum for the GRE header and payload.

***Reserved 1 (16 bits)***

Present if the

C

bit is set; its contents is set to 0.

### Original GRE packet header (RFC 1701)

The newer structure superseded the original structure:

Original GRE header format

Offsets

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

C

R

K

S

s

Recur

Flags

Version

Protocol Type

4

32

Checksum

(optional)

Offset (optional)

8

64

Key (optional)

12

96

Sequence Number (optional)

16

128

Routing (optional, variable length)

The original GRE RFC defined further fields in the packet header which became obsolete in the current standard:

***C (1 bit)***

Checksum

bit. Set to 1 if a checksum is present.

***R (1 bit)***

Routing Bit. Set to 1 if Routing and Offset information are present.

***K (1 bit)***

Key bit. Set to 1 if a key is present.

***S (1 bit)***

Sequence number bit. Set to 1 if a sequence number is present.

***s (1 bit)***

Strict source route bit.

***Recur (3 bits)***

Recursion

control bits.

***Flags (5 bits)***

Reserved for future use, set to 0.

***Version (3 bits)***

Set to 0.

***Protocol Type (16 bits)***

Indicates the

ether protocol type

of the encapsulated payload.

***Checksum (16 bits)***

Present if the

C

bit is set; contains the checksum for the GRE header and payload.

***Offset (16 bits)***

Present if

R

bit or

C

bit is set; contains valid information, only if

R

bit is set. An offset field indicating the offset within the

Routing

field to the active source route entry.

***Key (32 bits)***

Present if the

K

bit is set; contains an application-specific key value.

***Sequence Number (32 bits)***

Present if the

S

bit is set; contains a sequence number for the GRE packet.

***Routing (variable)***

Present if

R

bit is set; contains a list of source route entries, therefore is of variable length.

### PPTP GRE packet header

The Point-to-Point Tunneling Protocol (PPTP) uses a variant GRE packet header structure, represented below. PPTP creates a GRE tunnel through which the PPTP GRE packets are sent.

PPTP GRE header format

Offsets

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

C

R

K

S

s

Recur

A

Flags

Version

Protocol Type

4

32

Key Payload Length

Key Call ID

8

64

Sequence Number (optional)

12

96

Acknowledgement Number (optional)

***C (1 bit)***

Checksum

bit. For PPTP GRE packets, this is set to 0.

***R (1 bit)***

Routing bit. For PPTP GRE packets, this is set to 0.

***K (1 bit)***

Key bit. For PPTP GRE packets, this is set to 1. (All PPTP GRE packets carry a key.)

***S (1 bit)***

Sequence number bit. Set to 1 if a sequence number is supplied, indicating a PPTP GRE data packet.

***s (1 bit)***

Strict source route bit. For PPTP GRE packets, this is set to 0.

***Recur (3 bits)***

Recursion

control bits. For PPTP GRE packets, these are set to 0.

***A (1 bit)***

Acknowledgment number present. Set to 1 if an acknowledgment number is supplied, indicating a PPTP GRE acknowledgment packet.

***Flags (4 bits)***

Flag bits. For PPTP GRE packets, these are set to 0.

***Version (3 bits)***

GRE Version number. For PPTP GRE packets, this is set to 1.

***Protocol Type (16 bits)***

For PPTP GRE packets, this is set to hex 880B.

***Key Payload Length (16 bits)***

Contains the size of the payload, not including the GRE header.

***Key Call ID (16 bits)***

Contains the Peer's Call ID for the session to which the packet belongs.

***Sequence Number (32 bits)***

Present if the S bit is set; contains the GRE payload sequence number.

***Acknowledgement Number (32 bits)***

Present if the A bit is set; contains the sequence number of the highest GRE payload packet received by the sender.

## Standards

- RFC 1701: *Generic Routing Encapsulation (GRE)* (informational)
- RFC 1702: *Generic Routing Encapsulation over IPv4 networks* (informational)
- RFC 2637: *Point to Point Tunneling Protocol* (informational)
- RFC 2784: *Generic Routing Encapsulation (GRE)* (proposed standard, updated by RFC 2890)
- RFC 2890: *Key and Sequence Number Extensions to GRE* (proposed standard)
- RFC 8086: *GRE-in-UDP Encapsulation* (proposed standard)
