---
title: "Optical transport network"
source: https://en.wikipedia.org/wiki/Optical_transport_network
domain: sonet-sdh
license: CC-BY-SA-4.0
tags: synchronous optical networking, synchronous digital hierarchy, optical transport, time division multiplexing
fetched: 2026-07-02
---

# Optical transport network

An **optical transport network** (**OTN**) is a digital wrapper that encapsulates frames of data, to allow multiple data sources to be sent on the same channel. This creates an optical virtual private network for each client signal.

ITU-T defines an optical transport network as a set of optical network elements (ONE) connected by optical fiber links, able to provide functionality of transport, multiplexing, switching, management, supervision and survivability of optical channels carrying client signals. An ONE may re-time, re-Amplify, re-shape (3R) but it does not have to be 3R – it can be purely photonic. Unless connected by optical fibre links, it shall not be OTN. Mere functionality of switching, management, supervision shall not make it OTN, unless the signals are carried through optical fibre. Unlike SONET/SDH, OTN provides a mechanism to manage multiplexed wavelengths in a DWDM system.

## Comparing OTN and SONET/SDH

|   | OTN | SONET/SDH |
|---|---|---|
| Scaling | 400Gbit/s (2021) | 40Gbit/s |
| Error correcting | Yes, Forward Error Correction, 64b/66b encoding, 512B/513B encoding, 1024B/1027B encoding | Yes, Forward Error Correction, BCH code |
| Timing | Does not require | Requires |
| Octet-based block frame structure | Fixed, 16300 Byte | Variable, 2430- 622 080 Byte |
| Frame rate | Variable (98.354 - 1.163 μs) | 125 μs |

## Standards

OTN was designed to provide higher throughput (currently 400G) than its predecessor SONET/SDH, which stops at 40 Gbit/s, per channel.

ITU-T Recommendation G.709 is commonly called Optical Transport Network (OTN) (also called **digital wrapper technology** or **optical channel wrapper**). As of December 2009, OTN has standardized the following line rates.

Signal

Marketing data Rate (Gbit/s)

True Signal rate (OTU) (Gbit/s)

Applications

Maximum number of signals per channel

# of ODU0, 1.2G

# of ODU1, 2.5G

# of ODU2, 10G

# of ODU2e, 10.4G

# of ODU25, 26.4G

# of ODU3, 40.3G

# of ODU50, 52.8G

# of ODU4, 104G

OTU1

2.5

2.66

Transports

SONET

OC-48

or synchronous digital hierarchy (SDH)

STM-16

signal

2

1

0

0

0

0

0

0

OTU2

10

10.7

Transports an

OC-192

,

STM-64

or

wide area network

(WAN) physical layer (PHY) for

10 Gigabit Ethernet

(10GBASE-W)

8

4

1

0

0

0

0

0

OTU2e

10.5

11.1

Transports a 10 Gigabit Ethernet

local area network

(LAN) PHY coming from IP/Ethernet switches and routers at full line rate (10.3 Gbit/s). This is specified in G.Sup43.

8

4

1

1

0

0

0

0

OTU25

25

26.4

Transports a

25 Gigabit Ethernet

signal

20

10

2

2

1

0

0

0

OTU3

40

43

Transports an

OC-768

or

STM-256

signal or a

40 Gigabit Ethernet

signal.

32

16

4

3

1

1

0

0

OTU3e1/2

41

44.5

develop for transport of 10G LAN PHY, and one for 10G WAN PHY, over SDH and OTN.

32

16

4

3

1

1

0

0

OTU50

50

52.8

Transports a

50 Gigabit Ethernet

signal

40

20

5

5

2

1

1

0

OTU4

100

111.8

Transports a

100 Gigabit Ethernet

signal

80

40

10

10

2

2

2

1

OTUCn

n x 100

n x 105.2

n instances of a logically interleaved 100G (C=100) frame format

Total bandwidth / ODU size. e.g. 200G Channel support 4xODU3 and 4xODU2

The OTUk (k=1/2/2e/3/3e2/4) is an information structure into which another information structure called ODUk (k=1/2/2e/3/3e2/4) is mapped. The ODUk signal is the server layer signal for client signals. The following ODUk information structures are defined in ITU-T Recommendation G.709

| Signal | Data Rate (Gbit/s) | Typical Applications |
|---|---|---|
| ODU0 | 1.24416 | Transport of a timing transparent transcoded (compressed) 1000BASE-X signal or a stream of packets (such as Ethernet, MPLS or IP) using Generic Framing Procedure |
| ODU1 | 2.49877512605042 | Transport of two ODU0 signals or a STS-48/STM-16 signal or a stream of packets (such as Ethernet, MPLS or IP) using Generic Framing Procedure. |
| ODU2 | 10.0372739240506 | Transport of up to eight ODU0 signals or up to four ODU1 signals or a STS-192/STM-64 signal or a WAN PHY (10GBASE-W) or a stream of packets (such as Ethernet, MPLS or IP) using Generic Framing Procedure |
| ODU2e | 10.3995253164557 | Transport of a 10 Gigabit Ethernet signal or a timing transparent transcoded (compressed) Fibre Channel 10GFC signal |
| ODU3 | 40.3192189830509 | Transport of up to 32 ODU0 signals or up to 16 ODU1 signals or up to four ODU2 signals or a STS-768/STM-256 signal or a timing transparent transcoded 40 Gigabit Ethernet signal or a stream of packets (such as Ethernet, MPLS or IP) using Generic Framing Procedure |
| ODU3e2 | 41.7859685595012 | Transport of up to four ODU2e signals |
| ODU4 | 104.794445814978 | Transport of up to 80 ODU0 signals or up to 40 ODU1 signals or up to ten ODU2 signals or up to two ODU3 signals or a 100 Gigabit Ethernet signal |
| ODUflex (CBR) | 239⁄238 x client bit rate | Transport of a constant bitrate signal such as Fibre Channel 8GFC, InfiniBand or Common Public Radio Interface |
| ODUflex (GFP) | any configured rate | Transport of a stream of packets (such as Ethernet, MPLS or IP) using Generic Framing Procedure |

## Equipment

At a very high level, the typical signals processed by OTN equipment at the Optical Channel layer are:

- SONET/SDH
- Ethernet/FibreChannel
- Packets
- OTN

A few of the key functions performed on these signals are:

- Protocol processing of all the signals:-
  - Mapping and de-mapping of non-OTN signals into and out of OTN signals
  - Multiplexing and de-multiplexing of OTN signals
  - Forward error correction (FEC) on OTN signals

- Packet processing in conjunction with mapping/de-mapping of packet into and out of OTN signals

### Switch Fabric

The OTN signals at all data-rates have the same frame structure but the frame period reduces as the data-rate increases. As a result, the Time-Slot Interchange (TSI) technique of implementing SONET/SDH switch fabrics is not directly applicable to OTN switch fabrics. OTN switch fabrics are typically implemented using Packet Switch Fabrics.

### FEC Latency

On a point-to-point OTN link there is latency due to forward error correction (FEC) processing. Hamming distance of the RS(255,239) code is 17
