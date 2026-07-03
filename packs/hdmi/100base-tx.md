---
title: "Fast Ethernet"
source: https://en.wikipedia.org/wiki/100BASE-TX
domain: hdmi
license: CC-BY-SA-4.0
tags: hdmi
fetched: 2026-07-03
---

# Fast Ethernet

(Redirected from

100BASE-TX

)

In computer networking, **Fast Ethernet** physical layers carry traffic at the nominal rate of 100 Mbit/s. The prior Ethernet speed was 10 Mbit/s. Of the Fast Ethernet physical layers, **100BASE-TX** is by far the most common.

Fast Ethernet was introduced in 1995 as the **IEEE 802.3u** standard and remained the fastest version of Ethernet for three years before the introduction of Gigabit Ethernet. The acronym *GE/FE* is sometimes used for devices supporting both standards.

## Nomenclature

The *100* in the media type designation refers to the transmission speed of 100 Mbit/s, while the *BASE* refers to baseband signaling. The letter following the dash (*T* or *F*) refers to the physical medium that carries the signal (twisted pair or fiber, respectively), while the last character (*X*, *4*, etc.) refers to the line code method used. Fast Ethernet is sometimes referred to as **100BASE-X**, where *X* is a placeholder for the FX and TX variants. IEEE 802.2 refers to Fast Ethernet collectively as **100BASE-T**, including fiber variants.

## General design

Fast Ethernet is an extension of the 10-megabit Ethernet standard. It runs on twisted pair or optical fiber cable in a star wired bus topology, similar to the IEEE standard 802.3i called 10BASE-T, itself an evolution of 10BASE5 (802.3) and 10BASE2 (802.3a). Fast Ethernet devices are generally backward compatible with existing 10BASE-T systems, enabling plug-and-play upgrades from 10BASE-T. Most switches and other networking devices with ports capable of Fast Ethernet can perform autonegotiation, sensing a piece of 10BASE-T equipment and setting the port to 10BASE-T half duplex if the 10BASE-T equipment cannot perform autonegotiation itself. The standard specifies the use of CSMA/CD for media access control. A full-duplex mode is also specified, and in practice, modern networks use Ethernet switches and operate in full-duplex mode, even as legacy devices that use half duplex still exist.

A Fast Ethernet adapter can be logically divided into a media access controller (MAC), which deals with the higher-level issues of medium availability, and a physical layer interface (PHY). The MAC is typically linked to the PHY by a four-bit 25 MHz synchronous parallel interface known as a media-independent interface (MII), or by a two-bit 50 MHz variant called reduced media independent interface (RMII). In rare cases, the MII may be an external connection, but it is usually a connection between ICs in a network adapter or even two sections within a single IC. The specs are written based on the assumption that the interface between MAC and PHY will be an MII, but they do not require it. Fast Ethernet or Ethernet hubs may use the MII to connect to multiple PHYs for their different interfaces.

The MII fixes the theoretical maximum data bit rate for all versions of Fast Ethernet to 100 Mbit/s. The information rate actually observed on real networks is less than the theoretical maximum, due to the necessary header and trailer (addressing and error-detection bits) on every Ethernet frame, and the required interpacket gap between transmissions.

## Copper

Initially, several Fast Ethernet standards for twisted-pair cable were standardized, including: 100BASE-TX (100 Mbit/s over two-pair Cat5 or better cable), 100BASE-T4 (100 Mbit/s over four-pair Cat3 or better cable, defunct), 100BASE-T2 (100 Mbit/s over two-pair Cat3 or better cable, also defunct). The segment length for Ethernet over a twisted-pair link is limited to 100 metres (328 ft), the same limit as 10BASE-T and gigabit Ethernet. All initial standards were approved under IEEE 802.3 in 1995. Of those, 100BASE-TX became extremely popular, supplanting the others.

Comparison of

twisted-pair-based Ethernet

physical transport layers (TP-PHYs)

Name

Added in amendment

Status

Speed

Pairs

re

­

quired

Lanes per

di

­

rec

­

tion

Bits per hertz

Line code

Symbol rate

per lane

Band

­

width

Max

dis

­

tance

Cable

Cable

ra

­

ting

Usage

(Mb/s)

(MBd)

(MHz)

(m)

(MHz)

100BASE-TX

802.3u-1995

current

100

2

1

3.2

0

4B5B

MLT-3

NRZI

125

31.25

100

Cat

5

100

LAN

100BASE-T1

802.3bw-2015

(CL96)

1

1

2.6

6

PAM-3 4B/3B

75

37.5

15

Cat

5e

66

Auto

­

motive, IoT, M2M

100BASE-T2

802.3y-1997

obsolete

2

2

4

.00

LFSR PAM-5

25

12.5

100

Cat

3

16

Market failure

100BASE-T4

802.3u-1995

4

3

2.6

6

8B6T PAM-3

Half-duplex only

25

12.5

100

Cat

3

16

100BaseVG

802.12-1995

4

4

1.6

6

5B6B

Half-duplex only

30

15

100

Cat

3

16

| **8P8C wiring (ANSI/TIA-568 T568A)** |   | **8P8C wiring (ANSI/TIA-568 T568B)** |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
| Pin | Pair | Wire | Color | Pin | Pair | Wire | Color |
| 1 | 3 | +/tip | (Pair 3 Wire 1) white/green | 1 | 2 | +/tip | (Pair 2 Wire 1) white/orange |
| 2 | 3 | −/ring | (Pair 3 Wire 2) green | 2 | 2 | −/ring | (Pair 2 Wire 2) orange |
| 3 | 2 | +/tip | (Pair 2 Wire 1) white/orange | 3 | 3 | +/tip | (Pair 3 Wire 1) white/green |
| 4 | 1 | +/ring | (Pair 1 Wire 2) blue | 4 | 1 | +/ring | (Pair 1 Wire 2) blue |
| 5 | 1 | −/tip | (Pair 1 Wire 1) white/blue | 5 | 1 | −/tip | (Pair 1 Wire 1) white/blue |
| 6 | 2 | −/ring | (Pair 2 Wire 2) orange | 6 | 3 | −/ring | (Pair 3 Wire 2) green |
| 7 | 4 | +/tip | (Pair 4 Wire 1) white/brown | 7 | 4 | +/tip | (Pair 4 Wire 1) white/brown |
| 8 | 4 | −/ring | (Pair 4 Wire 2) brown | 8 | 4 | −/ring | (Pair 4 Wire 2) brown |

### 100BASE-TX

**100BASE-TX** is the predominant form of Fast Ethernet, and runs over two pairs of wire inside a Category 5 or above cable. Cable distance between nodes can be up to 100 metres (328 ft). One pair is used for each direction, providing full-duplex operation at 100 Mbit/s in each direction.

Like 10BASE-T, the active pairs in a standard connection are terminated on pins 1, 2, 3 and 6. Since a typical Category 5 cable contains four pairs and the performance requirements of 100BASE-TX do not exceed the capabilities of even the worst-performing pair, one typical cable can carry two 100BASE-TX links with a simple wiring adaptor on each end. Cabling is conventionally wired to one of ANSI/TIA-568's termination standards, T568A or T568B. 100BASE-TX uses pairs 2 and 3 (orange and green).

The configuration of 100BASE-TX networks is very similar to 10BASE-T. When used to build a local area network, the devices on the network (computers, printers, etc.) are typically connected to a hub or switch, creating a star network. Alternatively, it is possible to connect two devices directly using a crossover cable. With today's equipment, crossover cables are generally not needed as most equipment supports auto-negotiation along with auto MDI-X to select and match speed, duplex and pairing.

With 100BASE-TX hardware, the raw bits, presented 4 bits wide clocked at 25 MHz at the MII, go through 4B5B binary encoding to generate a series of 0 and 1 symbols clocked at a 125 MHz symbol rate. The 4B5B encoding provides DC equalization and spectrum shaping. Just as in the 100BASE-FX case, the bits are then transferred to the physical medium attachment layer using NRZI encoding. However, 100BASE-TX introduces an additional, medium-dependent sublayer, which employs MLT-3 as a final encoding of the data stream before transmission, resulting in a maximum fundamental frequency of 31.25 MHz. The procedure is borrowed from the ANSI X3.263 FDDI specifications, with minor changes.

### 100BASE-T1

In **100BASE-T1**, the data is transmitted over a single copper pair, 3 bits per symbol, each transmitted as a code pair using PAM3. It supports full-duplex transmission. The twisted-pair cable is required to support 66 MHz, with a maximum length of 15 m. No specific connector is defined. The standard is intended for automotive applications or when Fast Ethernet is to be integrated into another application. It was developed as Open Alliance BroadR-Reach (OABR) before IEEE standardization.

### 100BASE-T2

| Symbol | Line signal level |
|---|---|
| 000 | 0+0 |
| 001 | 0+1 |
| 010 | 0−1 |
| 011 | 0−2 |
| 100 (ESC) | 0+2 |

In **100BASE-T2**, standardized in IEEE 802.3y, the data is transmitted over two copper pairs, but these pairs are only required to be Category 3 (voice grade) rather than the Category 5 required by 100BASE-TX. Data is transmitted and received on both pairs simultaneously, thus allowing full-duplex operation. Transmission uses 4 bits per symbol. The 4-bit symbol is expanded into two 3-bit symbols through a non-trivial scrambling procedure based on a linear-feedback shift register. This is needed to flatten the bandwidth and emission spectrum of the signal, as well as to match transmission line properties. The mapping of the original bits to the symbol codes is not constant in time and has a fairly large period (appearing as a pseudo-random sequence). The final mapping from symbols to PAM-5 line modulation levels obeys the table on the right. 100BASE-T2 was not widely adopted, but the technology developed for it is used in 1000BASE-T.

### 100BASE-T4

**100BASE-T4** was an early implementation of Fast Ethernet. It required four twisted copper pairs of voice grade twisted pair (Category 3), a lower-performing cable compared to Category 5 cable used by 100BASE-TX. Maximum distance was limited to 100 meters. One pair was reserved for transmission and one for reception, and the remaining two switched direction. The fact that three pairs were used to transmit in each direction made 100BASE-T4 inherently half-duplex. Using three cable pairs allowed it to reach 100 Mbit/s while running at lower carrier frequencies, which allowed it to run on older cabling that many companies had recently installed for 10BASE-T networks.

A very unusual 8B6T code was used to convert 8 data bits into 6 base-3 digits (the signal shaping is possible as there are nearly three times as many 6-digit base-3 numbers as there are 8-digit base-2 numbers). The two resulting 3-digit base-3 symbols were sent in parallel over three pairs using 3-level pulse-amplitude modulation (PAM-3).

100BASE-T4 was not widely adopted but some of the technology developed for it is used in 1000BASE-T. Very few hubs were released with 100BASE-T4 support. Some examples include the 3com 3C250-T4 Superstack II HUB 100, IBM 8225 Fast Ethernet Stackable Hub and Intel LinkBuilder FMS 100 T4. The same applies to network interface controllers. Bridging 100BASE-T4 with 100BASE-TX required additional network equipment.

### 100BaseVG

Proposed and marketed by Hewlett-Packard, 100BaseVG was an alternative design using category 3 cabling and a token concept instead of CSMA/CD. It was slated for standardization as IEEE 802.12, but it quickly vanished when switched 100BASE-TX became popular. The IEEE standard was later withdrawn.

VG was similar to T4 in that it used more cable pairs combined with a lower carrier frequency to allow it to reach 100 Mbit/s on voice-grade cables. It differed in the way those cables were assigned. Whereas T4 would use the two extra pairs in different directions depending on the direction of data exchange, VG instead used two transmission modes. In one, *control*, two pairs are used for transmission and reception as in classic Ethernet, while the other two pairs are used for flow control. In the second mode, *transmission*, all four are used to transfer data in a single direction. The hubs implemented a token passing scheme to choose which of the attached nodes were allowed to communicate at any given time, based on signals sent to it from the nodes using control mode. When one node was selected to become active, it would switch to transfer mode, send or receive a packet, and return to control mode.

This concept was intended to solve two problems. The first was that it eliminated the need for collision detection and thereby reduced contention on busy networks. While any particular node may find itself throttled due to heavy traffic, the network as a whole would not end up losing efficiency due to collisions and the resulting rebroadcasts. Under heavy use, the total throughput was increased compared to the other standards. The other was that the hubs could examine the payload types and schedule the nodes based on their bandwidth requirements. For instance, a node sending a video signal may not require much bandwidth, but will require it to be predictable in terms of when it is delivered. A VG hub could schedule access on that node to ensure it received the transmission timeslots it needed while opening up the network at all other times to the other nodes. This style of access was known as demand priority.

## Fiber optics

Fiber variants use fiber-optic cable with the listed interface types. Interfaces may be fixed or modular, often as Small Form-factor Pluggable (SFP).

| Fibre type | In­tro­duc­ed | Per­form­ance |
|---|---|---|
| MMF FDDI 62.5/125 µm | 1987 | 0160 MHz·km @ 850 nm |
| MMF OM1 62.5/125 µm | 1989 | 0200 MHz·km @ 850 nm |
| MMF OM2 50/125 µm | 1998 | 0500 MHz·km @ 850 nm |
| MMF OM3 50/125 µm | 2003 | 1500 MHz·km @ 850 nm |
| MMF OM4 50/125 µm | 2008 | 3500 MHz·km @ 850 nm |
| MMF OM5 50/125 µm | 2016 | 3500 MHz·km @ 850 nm and 1850 MHz·km @ 950 nm |
| SMF OS1 9/125 µm | 1998 | 1.0 dB/km @ 1300/1550 nm |
| SMF OS2 9/125 µm | 2000 | 0.4 dB/km @ 1300/1550 nm |

Name

Added in Amendment

Status

Media

Connector

Transceiver

Module

Reach

in m

#

Media

(⇆)

#

Lambdas

(→)

#

Lanes

(→)

Notes

Fast Ethernet

–

(

Data rate

:

100 Mbit/s

–

Line code

:

4B5B

×

NRZI

– Line rate: 125

MBd

– Full-Duplex / Half-Duplex)

100BASE-FX

802.3u-1995

(CL24/26)

current

fiber

1300

nm

ST

SC

MT-RJ

MIC (FDDI)

—

N/a

FDDI: 2k (FDX)

2

1

1

max. 412

m for half-duplex connections to ensure collision detection;

specification largely derived from FDDI.

Modal bandwidth

: 800

MHz·km

OM1: 4k

50/125: 5k

100BASE-LFX

proprietary

(non IEEE)

current

fiber

1310

nm

LC (SFP)

ST

SC

SFP

OM1: 2k

2

1

1

vendor-specific

FP laser transmitter

Full-duplex

Modal bandwidth

: 800

MHz·km

OM2: 2k

62.5/125: 4k

50/125: 4k

OSx: 40k

100BASE-SX

TIA-785

(2000)

legacy

fiber

850

nm

ST

SC

LC

—

N/a

OM1: 300

2

1

1

optics sharable with 10BASE-FL, thus making it possible to have an auto-negotiation scheme and use 10/100 fiber adapters.

OM2: 300

100BASE-LX10

802.3ah-2004

(CL58)

phase-out

fiber

1310

nm

LC

SFP

OSx: 10k

2

1

1

full-duplex only

100BASE-BX10

phase-out

fiber

TX:

1310

nm

RX:

1550

nm

OSx: 40k

1

full-duplex only

;

optical multiplexer used to split TX and RX signals into different wavelengths.

### Fast Ethernet SFP ports

Fast Ethernet speed is not available on all SFP ports, but supported by some devices. An SFP port for Gigabit Ethernet should not be assumed to be backwards compatible with Fast Ethernet.

### Optical interoperability

To have interoperability there are some criteria that have to be met:

- Line encoding
- Wavelength
- Duplex mode
- Media count
- Media type and dimension

100BASE-X Ethernet is not backward compatible with 10BASE-F and is not forward compatible with 1000BASE-X.

### 100BASE-FX

100BASE-FX is a version of Fast Ethernet over optical fiber. The 100BASE-FX physical medium dependent (PMD) sublayer is defined by FDDI's PMD, so 100BASE-FX is not compatible with 10BASE-FL, the 10 Mbit/s version over optical fiber.

100BASE-FX is still used for existing installations of multimode fiber where more speed is not required, like industrial automation plants.

### 100BASE-LFX

100BASE-LFX is a non-standard term to refer to Fast Ethernet transmission. It is very similar to 100BASE-FX but achieves longer distances up to 4–5 km over a pair of multi-mode fibers through the use of Fabry–Pérot laser transmitter running on 1310 nm wavelength. The signal attenuation per km at 1300 nm is about half the loss of 850 nm.

### 100BASE-SX

100BASE-SX is a version of Fast Ethernet over optical fiber standardized in TIA/EIA-785-1-2002. It is a lower-cost, shorter-distance alternative to 100BASE-FX. Because of the shorter wavelength used (850 nm) and the shorter distance supported (up to 300 m), 100BASE-SX may use less expensive optical components.

Because it uses the same wavelength as 10BASE-FL, the 10 Mbit/s version of Ethernet over optical fiber, 100BASE-SX can be backward-compatible with 10BASE-FL. Cost and compatibility make 100BASE-SX an option for those upgrading from 10BASE-FL and who do not require longer distances.

### 100BASE-LX10

100BASE-LX10 is a version of Fast Ethernet over optical fiber standardized in 802.3ah-2004 clause 58. It has a 10 km reach over a pair of single-mode fibers.

### 100BASE-BX10

100BASE-BX10 is a version of Fast Ethernet over optical fiber standardized in 802.3ah-2004 clause 58. It uses an optical multiplexer to split TX and RX signals into different wavelengths on the same fiber. It has a 10 km reach over a single strand of single-mode fiber.

### 100BASE-EX

100BASE-EX is very similar to 100BASE-LX10 but achieves longer distances up to 40 km over a pair of single-mode fibers due to higher quality optics than a LX10, running on 1310 nm wavelength lasers. 100BASE-EX is not a formal standard but an industry-accepted term. It is sometimes referred to as 100BASE-LH (long haul), and is easily confused with 100BASE-LX10 or 100BASE-ZX because the use of -LX(10), -LH, -EX, and -ZX is ambiguous between vendors.

### 100BASE-ZX

100BASE-ZX is a non-standard but multi-vendor term to refer to Fast Ethernet transmission using 1,550 nm wavelength to achieve distances of at least 70 km over single-mode fiber. Some vendors specify distances up to 160 km over single-mode fiber, sometimes called 100BASE-EZX. Ranges beyond 80 km are highly dependent upon the path loss of the fiber in use, specifically the attenuation figure in dB per km, the number and quality of connectors/patch panels and splices located between transceivers.
