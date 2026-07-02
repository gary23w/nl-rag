---
title: "USB - Wikipedia (part 1/2)"
source: https://en.wikipedia.org/wiki/USB
domain: hardware-interfaces
license: CC-BY-SA-4.0
tags: i2c, spi bus, uart, can bus, gpio, pwm, serial port, jtag
fetched: 2026-07-02
part: 1/2
---

# USB

**Universal Serial Bus** (**USB**) is an industry standard, developed by USB Implementers Forum (USB-IF), for digital data transmission and power delivery between many types of electronics. It specifies the architecture, in particular the physical interfaces, and communication protocols to and from *hosts*, such as personal computers, to and from peripheral *devices*, e.g. displays, keyboards, and mass storage devices, and to and from intermediate *hubs*, which multiply the number of a host's ports.

Introduced in 1996, USB was originally designed to standardize the connection of peripherals to computers, replacing various interfaces such as serial ports, parallel ports, game ports, and Apple Desktop Bus (ADB) ports. Early versions of USB became commonplace on a wide range of devices, such as keyboards, mice, cameras, printers, scanners, flash drives, smartphones, game consoles. USB has since evolved into a standard to replace virtually all common ports on computers, mobile devices, peripherals, power supplies, and various other small electronics.

In the latest standard, the USB-C connector replaces many types of connectors for power (up to 240 W), displays (e.g. DisplayPort, HDMI), and many other uses, as well as all previous USB connectors.

As of 2024, USB consists of four generations of specifications: USB 1.*x*, USB 2.0, USB 3.*x*, and USB4. The USB4 specification enhances the data transfer and power delivery functionality with "a connection-oriented tunneling architecture designed to combine multiple protocols onto a single physical interface so that the total speed and performance of the USB4 Fabric can be dynamically shared." In particular, USB4 supports the tunneling of the Thunderbolt 3 protocols, namely PCI Express (PCIe, load/store interface) and DisplayPort (display interface). USB4 also adds host-to-host interfaces.

Each specification sub-version supports different signaling rates from 1.5 and 12 Mbit/s half-duplex in USB 1.0/1.1 to 80 Gbit/s full-duplex in USB4 2.0. USB also provides power to peripheral devices; the latest versions of the standard extend the power delivery limits for battery charging and devices requiring up to 240 watts as defined in USB Power Delivery (USB-PD) Rev. 3.1 V1.1 in 2021. Over the years, USB(-PD) has been adopted as the standard power supply and charging format for many mobile devices, such as mobile phones, reducing the need for proprietary chargers.


## Overview

USB was designed to standardize the connection of peripherals to personal computers, both to exchange data and to supply electric power. It has largely replaced interfaces such as serial ports and parallel ports and has become commonplace on various devices. Peripherals connected via USB include computer keyboards and mice, video cameras, printers, portable media players, mobile (portable) digital telephones, disk drives, and network adapters.

USB connectors have been increasingly replacing other types of charging cables for portable devices.

USB connector interfaces are classified into three types: the many various *legacy* Type-A (controlling host) and Type-B (attached device) connectors found on *hosts*, *hubs*, and *peripheral devices*, and the modern Type-C (USB-C) connector, which replaces the many legacy connectors as the only applicable connector for USB4.

The Type-A and Type-B connectors came in Standard, Mini, and Micro sizes. The standard format was the largest and was mainly used for desktop and larger peripheral equipment. The Mini-USB connectors (Mini-A, Mini-B, Mini-AB) were introduced for mobile devices. Still, they were quickly replaced by the thinner Micro-USB connectors (Micro-A, Micro-B, Micro-AB). The Type-C connector, also known as USB-C, is not exclusive to USB, is the only current standard for USB, is required for USB4, and is required by other standards, including modern DisplayPort and Thunderbolt. It is reversible and can support various functionalities and protocols, including USB; some are mandatory, and many are optional, depending on the type of hardware: host, peripheral device, or hub.

USB specifications provide backward compatibility, usually resulting in decreased signaling rates, maximal power offered, and other capabilities. The USB 1.1 specification replaces USB 1.0. The USB 2.0 specification is backward-compatible with USB 1.0/1.1. The USB 3.2 specification replaces USB 3.1 (and USB 3.0) while including the USB 2.0 specification. USB4 "functionally replaces" USB 3.2 while retaining the USB 2.0 bus operating in parallel.

The USB 3.0 specification defined a new architecture and protocol named *SuperSpeed* (aka *SuperSpeed USB*, marketed as *SS*), which included a new lane for a new signal coding scheme (8b/10b symbols, 5 Gbit/s; later also known as *Gen 1*) providing full-duplex data transfers that physically required five additional wires and pins, while preserving the USB 2.0 architecture and protocols and therefore keeping the original four pins/wires for the USB 2.0 backward-compatibility resulting in 9 wires (with 9 or 10 pins at connector interfaces; ID-pin is not wired) in total.

The USB 3.1 specification introduced an *Enhanced SuperSpeed System* – while preserving the *SuperSpeed* architecture and protocol (*SuperSpeed USB*) – with an additional *SuperSpeedPlus* architecture and protocol (aka *SuperSpeedPlus USB*) adding a new coding schema (128b/132b symbols, 10 Gbit/s; also known as *Gen 2*); for some time marketed as *SuperSpeed+* (*SS+*).

The USB 3.2 specification added a second lane to the *Enhanced SuperSpeed System* besides other enhancements so that the *SuperSpeedPlus USB* system part implements the *Gen 1×2*, *Gen 2×1,* and *Gen 2×2* operation modes. However, the *SuperSpeed USB* part of the system still implements the one-lane *Gen 1×1* operation mode. Therefore, two-lane operations, namely *USB 3.2 Gen 1×**2***(10 Gbit/s) and *Gen 2×**2***(20 Gbit/s), are only possible with Full-Featured USB-C. As of 2023, they are somewhat rarely implemented; Intel, however, started to include them in its 11th-generation SoC processor models, but Apple never provided them. On the other hand, *USB 3.2 Gen 1(×1)* (5 Gbit/s) and *Gen 2(×1)* (10 Gbit/s) have been quite common for some years.

### Connector type quick reference

Each USB connection is made using two connectors: a *receptacle* and a *plug*. Pictures show only receptacles:

Available connectors by USB standard

Standard

USB 1.0

1996

USB 1.1

1998

USB 2.0

2000

USB 2.0

Revised

USB 3.0

2008

USB 3.1

2013

USB 3.2

2017

USB4

2019

USB4 2.0

2022

Max Speed

Recommended marketing

since 2022

Basic-Speed

High-Speed

USB 5Gbps

USB 10Gbps

USB 20Gbps

USB 40Gbps

USB 80Gbps

Original label

Low-Speed & Full-Speed

SuperSpeed

, or

SS

SuperSpeed+

, or

SS+

SuperSpeed USB 20Gbps

Operation mode

USB

3.2 Gen

1×1

USB

3.2 Gen

2×1

USB

3.2 Gen

2×2

USB4 Gen

3×2

USB4 Gen

4×2

Signaling rate

1.5 Mbit/s & 12

Mbit/s

480 Mbit/s

5 Gbit/s

10 Gbit/s

20 Gbit/s

40 Gbit/s

80 Gbit/s

Connector

Standard-A

—

N/a

Standard-B

Mini-A

—

N/a

Mini-AB

Mini-B

Micro-A

—

N/a

Micro-AB

Micro-B

Type-C

(USB-C)

(Enlarged to show detail)

Remarks:

1. Limited to max speed at 10 Gbit/s, since only one-lane (*×1*) operation mode is possible.
2. Backward compatibility given.
3. Only as receptacle.
4. Accepts both Mini-A and Mini-B plugs.
5. Only as plug.
6. Backward compatibility given by USB 2.0 implementation.
7. Accepts both Micro-A and Micro-B plugs.

### Objectives

The Universal Serial Bus was developed to simplify and improve the interface between personal computers and peripheral devices, such as cell phones, computer accessories, and monitors, when compared with previously existing standard or *ad hoc* proprietary interfaces.

From the computer user's perspective, the USB interface improves ease of use in several ways:

- The USB interface is self-configuring, eliminating the need for the user to adjust the device's settings for speed or data format, or configure interrupts, input/output addresses, or direct memory access channels.
- USB connectors are standardized at the host, so any peripheral can use most available receptacles.
- USB takes full advantage of the additional processing power that can be economically put into peripheral devices so that they can manage themselves. As such, USB devices often do not have user-adjustable interface settings.
- The USB interface is hot-swappable (devices can be exchanged without shutting the host computer down).
- Small devices can be powered directly from the USB interface, eliminating the need for additional power supply cables.
- Because the use of the USB logo is only permitted after compliance testing, the user can have confidence that a USB device will work as expected without extensive interaction with settings and configuration.
- The USB interface defines protocols for recovery from common errors, improving reliability over previous interfaces.
- Installing a device that relies on the USB standard requires minimal operator action. When a user plugs a device into a port on a running computer, either it entirely automatically configures using existing device drivers or the system prompts the user to locate a driver, which it then installs and configures automatically.

The USB standard also provides multiple benefits for hardware manufacturers and software developers, specifically in the relative ease of implementation:

- The USB standard eliminates the requirement to develop proprietary interfaces to new peripherals.
- The wide range of transfer speeds available from a USB interface suits devices ranging from keyboards and mice up to streaming video interfaces.
- A USB interface can be designed to provide the best available latency for time-critical functions or can be set up to do background transfers of bulk data with little impact on system resources.
- The USB interface is generalized with no signal lines dedicated to only one function of one device.

### Limitations

As with all standards, USB possesses multiple limitations to its design:

- USB cables are limited in length, as the standard was intended for peripherals on the same tabletop, not between rooms or buildings. However, a USB port can be connected to a gateway that accesses distant devices.
- USB data transfer rates are slower than those of other interconnects (e.g., ethernet) released in the same timeframe.
- USB has a strict tree network topology and master/slave protocol for addressing peripheral devices; slave devices cannot interact with one another except via the host, and two hosts cannot communicate over their USB ports directly. Some extension to this limitation is possible through USB On-The-Go, Dual-Role-Devices and protocol bridge.
- A host cannot broadcast signals to all peripherals at once; each must be addressed individually.
- While converters exist between certain legacy interfaces and USB, they might not provide a full implementation of the legacy hardware. For example, a USB-to-parallel-port converter might work well with a printer, but not with a scanner that requires bidirectional use of the data pins.

For a product developer, using USB requires the implementation of a complex protocol and implies an "intelligent" controller in the peripheral device. Developers of USB devices intended for public sale generally must obtain a USB ID, which requires that they pay a fee to the USB Implementers Forum (USB-IF). Developers of products that use the USB specification must sign an agreement with the USB-IF. Use of the USB logos on the product requires annual fees and membership in the organization.


## History

A group of seven companies began the development of USB in 1995: Compaq, DEC, IBM, Intel, Microsoft, NEC, and Nortel. The goal was to make it fundamentally easier to connect external devices to PCs by replacing the multitude of connectors at the back of PCs, addressing the usability issues of existing interfaces, and simplifying software configuration of all devices connected to USB, as well as permitting greater data transfer rates for external devices and plug and play features. Concepts of the 1979 Atari SIO serial bus, of the 8-bit Atari computers, and the 1980 IEEE-488 derived Commodore bus, and Hewlett Packard's HP-IL bus pioneered this approach. A consortium led by Apple, and containing Sony, Panasonic (Matsushita), LG, Toshiba, Hitachi, Cannon, Philips Electronics, Compaq, Thomson and Texas Instruments, would develop the concept further, from 1986, as the IEEE 1394 firewire standard and patent pool. Joseph C. Decuir, originally of Atari, then Commodore, and a designer of the Atari SIO common bus, would work on the USB project for Microsoft, obtaining one of the related US patents; SIO was cited as prior art when defending USB against a patent troll. Ajay Bhatt and his team worked on the standard at Intel; the first integrated circuits supporting USB were produced by Intel in 1995.

### USB 1.*x*

Released in January 1996, USB 1.0 specified signaling rates of 1.5 Mbit/s (*Low Bandwidth* or *Low Speed*) and 12 Mbit/s (*Full Speed*). It did not allow for extension cables, due to timing and power limitations. Few USB devices made it to the market until USB 1.1 was released in August 1998. USB 1.1 was the earliest revision that was widely adopted and led to what Microsoft designated the "Legacy-free PC".

Neither USB 1.0 nor 1.1 specified a design for any connector smaller than the standard type A or type B. Though many designs for a miniaturized type B connector appeared on many peripherals, conformity to the USB 1.*x* standard was hampered by treating peripherals that had miniature connectors as though they had a tethered connection (that is: no plug or receptacle at the peripheral end). There was no known miniature type A connector until USB 2.0 (revision 1.01) introduced one.

### USB 2.0

USB 2.0 was released in April 2000, adding a higher maximum signaling rate of 480 Mbit/s (maximum theoretical data throughput 53 MByte/s) named *High Speed* or *High Bandwidth*, in addition to the USB 1.*x* *Full Speed* signaling rate of 12 Mbit/s (maximum theoretical data throughput 1.2 MByte/s).

Various improvements of USB 2.0 includes:

- *USB Selective Suspend* was introduced since USB 2.0.
- *USB Over Current Protection* was introduced.

Modifications to the USB specification have been made via engineering change notices (ECNs). The most important of these ECNs are included into the USB 2.0 specification package available from USB.org:

- *Mini-A and Mini-B Connector*
- *Micro-USB Cables and Connectors Specification 1.01*
- *InterChip USB Supplement*
- *On-The-Go Supplement 1.3* USB On-The-Go makes it possible for two USB devices to communicate with each other without requiring a separate USB host
- *Battery Charging Specification 1.1* Added support for dedicated chargers, host chargers behavior for devices with dead batteries
- *Battery Charging Specification 1.2*: with increased current of 1.5 A on charging ports for unconfigured devices, allowing high-speed communication while having a current up to 1.5 A
- *Link Power Management Addendum ECN*, which adds a *sleep* power state

### USB 3.*x*

The USB 3.0 specification was released on 12 November 2008, with its management transferring from USB 3.0 Promoter Group to the USB Implementers Forum (USB-IF) and announced on 17 November 2008 at the SuperSpeed USB Developers Conference.

USB 3.0 adds a new architecture and protocol named *SuperSpeed*, with associated backward-compatible plugs, receptacles, and cables. SuperSpeed plugs and receptacles are identified with a distinct logo and blue inserts in standard format receptacles.

The SuperSpeed architecture provides for an operation mode at a rate of 5.0 Gbit/s, in addition to the three existing operation modes. Its efficiency is dependent on a number of factors including physical symbol encoding and link-level overhead. At a 5 Gbit/s signaling rate with 8b/10b encoding, each byte needs 10 bits to transmit, so the raw throughput is 500 MB/s. When flow control, packet framing and protocol overhead are considered, it is realistic for about two-thirds of the raw throughput, or 330 MB/s to transmit to an application. SuperSpeed's architecture is full-duplex; all earlier implementations, USB 1.0-2.0, are half-duplex, arbitrated by the host.

Low-power and high-power devices remain operational with this standard, but devices implementing SuperSpeed can provide an increased current of between 150 mA and 900 mA, by discrete steps of 150 mA.

USB 3.0 also introduced the USB Attached SCSI Protocol (UASP), which provides generally faster transfer speeds than the BOT (Bulk-Only-Transfer) protocol.

USB 3.1 specification, released in July 2013. Firstly, it preserves USB 3.0's *SuperSpeed* architecture and protocol and its operation mode is newly named *USB 3.1 Gen 1* (previously called *USB 3.0*, and with USB 3.2 specification finally named *USB 3.2 Gen 1x1*, and later marketed as *USB 5Gbps* in 2023) Secondly, it introduces a distinctively new *SuperSpeedPlus* architecture and protocol with a second operation mode named as *USB 3.1 Gen 2*. This doubles the maximum signaling rate to 10 Gbit/s (later finally named *USB 3.2 Gen 2x1*, since 2023 marketed as *USB 10Gbps*), while reducing line encoding overhead to just 3% by changing the scheme to 128b/132b while flow control, packet framing and protocol overhead still have a significant impact on real world data rates.

USB 3.2 specification, released in September 2017, preserves existing *SuperSpeed* and *SuperSpeedPlus* architectures and protocols and their respective operation modes, but introduces two additional *SuperSpeedPlus* operation modes (*USB 3.2 Gen 1×2* and *USB 3.2 Gen 2×2*) with total signaling rates of 10 and 20 Gbit/s (raw data rates of 1212 and 2424 MB/s), respectively. The increased bandwidth is a result of two-lane operation over the additional wires included in all Full-Featured USB‑C Fabrics (all involved devices, hubs, cables and host).

#### Naming scheme

Starting with the USB 3.2 specification, USB-IF introduced a new marketing related naming scheme. To help companies with the branding of the different operation modes, USB-IF recommended branding the 5, 10, and 20 Gbit/s capabilities as *SuperSpeed USB 5Gbps*, *SuperSpeed USB 10Gbps*, and *SuperSpeed USB 20Gbps*, respectively.

In 2023, they were replaced again, removing *"SuperSpeed"*, with *USB 5Gbps*, *USB 10Gbps*, and *USB 20Gbps*. With new *Packaging* and *Port* logos.

### USB4

The **USB4** specification (Version 1.0) was released on 29 August 2019. It is based on the Thunderbolt 3 protocol, defines 20 and 40 Gbit/s signalling rates over USB-C, and allows tunneling of USB 3.2, USB 2.0, PCIe and DisplayPort protocols; Thunderbolt 3 compatibility is optional for USB4 hosts/devices.

**USB4 Version 2.0** (announced 1 September 2022) adds a new physical layer and higher signalling rates: up to **80 Gbit/s** bidirectional, and an asymmetric mode supporting **120/40 Gbit/s** (host→device / device→host) for video-heavy use cases. It achieves this using PAM3 signaling and, in many cases, existing passive “40 Gbit/s” USB-C cables; a new 80 Gbit/s active cable category is also defined. Version 2.0 updates tunneling to align with DisplayPort 2.1 and PCIe 4.0, and maintains backward compatibility with USB4 1.0, USB 3.2/2.0, and Thunderbolt 3. Since 2023, the USB-IF recommends consumer-facing product names that reflect signalling rates (e.g., **USB 40Gbps**, **USB 80Gbps**), replacing “USB4 v1/v2” in marketing and certification listings.

| Connection | Mandatory for | Remarks |   |   |
|---|---|---|---|---|
| host | hub | device |   |   |
| **USB 2.0** (480 Mbit/s) | Yes | Yes | Yes | Contrary to other functions – which use the multiplexing of high-speed links – USB 2.0 over USB-C utilizes its own differential pair of data wires. |
| **Tunneled USB 3.2 Gen 2×1** (10 Gbit/s) | Yes | Yes | No |   |
| **Tunneled USB 3.2 Gen 2×2** (20 Gbit/s) | No | No | No |   |
| **Tunneled USB 3 Gen T** (5–80 Gbit/s) | No | No | No | A type of USB 3 Tunneling architecture where the Enhanced SuperSpeed System is extended to allow operation at the maximum bandwidth available on the USB4 Link. |
| **USB4 Gen 2** (10 or 20 Gbit/s) | Yes | Yes | Yes | Either one or two lanes |
| **USB4 Gen 3** (20 or 40 Gbit/s) | No | Yes | No |   |
| **Tunneled DisplayPort 1.4a** | Yes | Yes | No | The specification requires that hosts and hubs support the DisplayPort Alternate Mode. |
| **Tunneled PCI Express 3.0** | No | Yes | No | The PCI Express function of USB4 replicates the functionality of previous versions of the Thunderbolt specification. |
| **Host-to-Host communications** | Yes | Yes | —N/a | A LAN-like connection between two peers |
| **Thunderbolt 3 Alternate Mode** | No | Yes | No | Thunderbolt 3 uses cables with USB‑C plugs; the USB4 specification allows hosts and devices, and requires hubs, to support interoperability with the standard using the Thunderbolt 3 Alternate Mode (namely DisplayPort and PCIe). |
| **Other Alternate Modes** | No | No | No | USB4 products may optionally offer interoperability with the HDMI, MHL, and VirtualLink Alternate Modes. |

#### September 2022 marketing naming scheme

Because of the previous confusing naming schemes, USB-IF decided to change it once again. As of 2 September 2022, marketing names follow the syntax "USB *x*Gbps", where *x* is the signalling rate in Gbit/s. Overview of the updated names and logos can be seen in the adjacent table.

The operation modes USB 3.2 Gen 2×2 and USB4 Gen 2×2 – or: USB 3.2 Gen 2×1 and USB4 Gen 2×1 – are not interchangeable or compatible; all participating controllers must operate with the same mode.

### Version histories

#### Specification history

| Spec name | Issue date | Maximum signaling rates: mode names | Note |
|---|---|---|---|
| USB 0.7 | 11 November 1994 | ? | Pre-release |
| USB 0.8 | 30 December 1994 | ? |   |
| USB 0.9 | 13 April 1995 | 12 Mbit/s: Full Speed (FS) |   |
| USB 0.99 | 25 August 1995 | ? |   |
| USB 1.0 FDR | 13 November 1995 | ? | Release Candidate |
| USB 1.0 | 15 January 1996 | 1.5 Mbit/s: Low Speed (LS) 12 Mbit/s: Full Speed (FS) | First official specification |
| USB 1.1 | 23 September 1998 | Updated all chapters to fix problems identified |   |
| USB 2.0 | 27 April 2000 | 480 Mbit/s: High Speed (HS) | Fully replaced and backward compatible with USB 1.0/1.1 |
| USB 3.0 | 12 November 2008 | 5 Gbit/s: USB 3.0 | Fully incorporated USB 2.0 and also marketed as SuperSpeed (SS) |
| USB 3.1 | 26 July 2013 | 10 Gbit/s: USB 3.1 Gen 2 | Fully replaced USB 3.0 and also marketed as SuperSpeed+ (SS+) |
| USB 3.2 Revision 1.0 | 22 September 2017 | 10 Gbit/s: USB 3.2 Gen 1×2 20 Gbit/s: USB 3.2 Gen 2×2 | Fully replaced USB 3.1 and requires Full-Featured USB-C Fabrics for two lane operation. |
| USB 3.2 Revision 1.1 | June 2022 | Incorporated errata and ECNs |   |
| USB4 | August 2019 | 20 Gbit/s: USB4 Gen 3×1 40 Gbit/s: USB4 Gen 3×2 | First Version, USB4 "functionally replaces" USB 3.2 while retaining the USB 2.0 bus operating in parallel. |
| USB4 Version 2.0 | October 2022 | 80 Gbit/s: Gen 4 symmetric 120 ⇄ 40 Gbit/s: Gen 4 asymmetric | Version 2.0 |

| Release name | Release date | Max. power |
|---|---|---|
| USB 1.0/1.1 specification, chapter 7.2 Power Distribution and chapter 7.3 Physical Layer | 1996-01-15/1998-09-23 | LPD: 0.5 W (5 V, 100 mA) HPD: 2.5 W (5 V, 500 mA) |
| USB 2.0 specification, chapter 7.2 Power Distribution and chapter 7.3 Physical Layer | 2000-04-27 |   |
| USB 3.0 specification, chapter 11 Interoperability and Power Delivery | 2008-11-12 | LPD: 0.75 W (5 V, 150 mA) HPD: 4.5 W (5 V, 900 mA) |
| USB 3.1 specification, chapter 11 Interoperability and Power Delivery | 2013-07-26 |   |
| USB 3.2 Revision 1.1 specification, chapter 11 Interoperability and Power Delivery | 2022-07 |   |
|   |   |   |
| USB Battery Charging Rev. 1.0 | 2007-03-08 | 7.5 W (5 V, 1.5 A) |
| USB Battery Charging Rev. 1.1 | 2009-04-15 |   |
| USB Battery Charging Rev. 1.2 | 2010-10-05 |   |
|   |   |   |
| USB Power Delivery Rev. 1.0 (V. 1.0-1.3) | 2012-07-05 | SPR: 100 W (20 V, 5 A) |
| USB Power Delivery Rev. 2.0 (V. 1.0-1.3) | 2014-08-11 |   |
| USB Power Delivery Rev. 3.0 (V. 1.0-2.0) | 2015-12-11 |   |
| USB Power Delivery Rev. 3.1 (V. 1.0-1.9) | 2021-05-24 | EPR: 240 W (48 V, 5 A) |
| USB Power Delivery Rev. 3.2 (V. 1.0-1.1) | 2023-10 |   |
|   |   |   |
| USB Type-C Rev. 1.0 | 2014-08-11 | 7.5 W (5 V, 1.5 A) and/or 15 W (5 V, 3 A) |
| USB Type-C Rev. 1.1 | 2015-04-03 |   |
| USB Type-C Rev. 1.2 | 2016-03-25 |   |
| USB Type-C Rev. 1.3 | 2017-07-14 |   |
| USB Type-C Rev. 1.4 | 2019-03-29 |   |
| USB Type-C Rev. 2.0 | 2019-08-29 |   |
| USB Type-C Rev. 2.1 | 2021-05-25 |   |
| USB Type-C Rev. 2.2 | 2022-10 |   |
| USB Type-C Rev. 2.3 | 2023-10 |   |
| USB Type-C Rev. 2.4 | 2024-10-28 |   |


## System design

A USB system consists of a host with one or more downstream facing ports (DFP), and multiple peripherals, forming a tiered-star topology. Additional USB hubs may be included, allowing up to five tiers. A USB host may have multiple controllers, each with one or more ports. Up to 127 devices may be connected to a single host controller. USB devices are linked in series through hubs. The hub built into the host controller is called the *root hub*.

A USB device may consist of several logical sub-devices that are referred to as *device functions*. A *composite device* may provide several functions, for example, a webcam (video device function) with a built-in microphone (audio device function). An alternative to this is a *compound device,* in which the host assigns each logical device a distinct address and all logical devices connect to a built-in hub that connects to the physical USB cable.

USB device communication is based on *pipes* (logical channels). A pipe connects the host controller to a logical entity within a device, called an *endpoint*. Because pipes correspond to endpoints, the terms are sometimes used interchangeably. Each USB device can have up to 32 endpoints (16 *in* and 16 *out*), though it is rare to have so many. Endpoints are defined and numbered by the device during initialization (the period after physical connection called *enumeration*) and so are relatively permanent, whereas pipes may be opened and closed.

There are two types of pipe: stream and message.

- A *message* pipe is bi-directional and is used for *control* transfers. Message pipes are typically used for short, simple commands to the device, and for status responses from the device, used, for example, by the bus control pipe number 0.
- A *stream* pipe is a uni-directional pipe connected to a uni-directional endpoint that transfers data using an *isochronous*, *interrupt*, or *bulk* transfer: Isochronous transfersAt some guaranteed data rate (for fixed-bandwidth streaming data) but with possible data loss (e.g., realtime audio or video) Interrupt transfersDevices that need guaranteed quick responses (bounded latency) such as pointing devices, mice, and keyboards Bulk transfersLarge sporadic transfers using all remaining available bandwidth, but with no guarantees on bandwidth or latency (e.g., file transfers)

When a host starts a data transfer, it sends a TOKEN packet containing an endpoint specified with a tuple of *(device_address, endpoint_number)*. If the transfer is from the host to the endpoint, the host sends an OUT packet (a specialization of a TOKEN packet) with the desired device address and endpoint number. If the data transfer is from the device to the host, the host sends an IN packet instead. If the destination endpoint is a uni-directional endpoint whose manufacturer's designated direction does not match the TOKEN packet (e.g. the manufacturer's designated direction is IN while the TOKEN packet is an OUT packet), the TOKEN packet is ignored. Otherwise, it is accepted and the data transaction can start. A bi-directional endpoint, on the other hand, accepts both IN and OUT packets.

Endpoints are grouped into *interfaces* and each interface is associated with a single device function. An exception to this is endpoint zero, which is used for device configuration and is not associated with any interface. A single device function composed of independently controlled interfaces is called a *composite device*. A composite device only has a single device address because the host only assigns a device address to a function.

When a USB device is first connected to a USB host, the USB device enumeration process is started. The enumeration starts by sending a reset signal to the USB device. The signaling rate of the USB device is determined during the reset signaling. After reset, the USB device's information is read by the host and the device is assigned a unique 7-bit address. If the device is supported by the host, the device drivers needed for communicating with the device are loaded and the device is set to a configured state. If the USB host is restarted, the enumeration process is repeated for all connected devices.

The host controller directs traffic flow to devices, so no USB device can transfer any data on the bus without an explicit request from the host controller. In USB 2.0, the host controller polls the bus for traffic, usually in a round-robin fashion. The throughput of each USB port is determined by the slower speed of either the USB port or the USB device connected to the port.

High-speed USB 2.0 hubs contain devices called transaction translators that convert between high-speed USB 2.0 buses and full and low speed buses. There may be one translator per hub or per port.

Because there are two separate controllers in each USB 3.0 host, USB 3.0 devices transmit and receive at USB 3.0 signaling rates regardless of USB 2.0 or earlier devices connected to that host. Operating signaling rates for earlier devices are set in the legacy manner.


## Device classes

The functionality of a USB device is defined by a class code sent to a USB host. This allows the host to load software modules for the device and to support new devices from different manufacturers.

Device classes include:

| Class (hex) | Usage | Description | Examples, or exception |
|---|---|---|---|
| 00 | Device | Unspecified | Device class is unspecified, interface descriptors are used to determine needed drivers |
| 01 | Interface | Audio | Speaker, microphone, sound card, MIDI |
| 02 | Both | Communications and CDC control | Serial adapter, modem, Wi-Fi adapter, Ethernet adapter. Used together with class 0Ah *(CDC-Data*) below |
| 03 | Interface | Human interface device (HID) | Keyboard, mouse, joystick |
| 05 | Interface | Physical interface device (PID) | Force feedback joystick |
| 06 | Interface | Media (PTP/MTP) | Scanner, Camera |
| 07 | Interface | Printer | Laser printer, inkjet printer, CNC machine |
| 08 | Interface | USB mass storage, USB Attached SCSI | USB flash drive, memory card reader, digital audio player, digital camera, external drive |
| 09 | Device | USB hub | High speed USB hub |
| 0A | Interface | CDC-Data | Used together with class 02h *(Communications and CDC Control*) above |
| 0B | Interface | Smart card | USB smart card reader |
| 0D | Interface | Content security | Fingerprint reader |
| 0E | Interface | Video | Webcam |
| 0F | Interface | Personal healthcare device class (PHDC) | Pulse monitor (watch) |
| 10 | Interface | Audio/video (AV) | Webcam, TV |
| 11 | Device | Billboard | Describes USB-C alternate modes supported by device |
| DC | Both | Diagnostic device | USB compliance testing device |
| E0 | Interface | Wireless controller | Bluetooth adapter |
| EF | Both | Miscellaneous | ActiveSync device |
| FE | Interface | Application-specific | IrDA Bridge, RNDIS, Test & Measurement Class (USBTMC), USB DFU (Device Firmware Upgrade) |
| FFh | Both | Vendor-specific | Indicates that a device needs vendor-specific drivers |

### USB mass storage / USB drive

The USB mass storage device class (MSC or UMS) standardizes connections to storage devices. At first intended for magnetic and optical drives, it has been extended to support flash drives and SD card readers. The ability to boot a write-locked SD card with a USB adapter is particularly advantageous for maintaining the integrity and non-corruptible, pristine state of the booting medium.

Though most personal computers since early 2005 can boot from USB mass storage devices, USB is not intended as a primary bus for a computer's internal storage. However, USB has the advantage of allowing hot-swapping, making it useful for mobile peripherals, including drives of various kinds.

Several manufacturers offer external portable USB hard disk drives, or empty enclosures for disk drives. These offer performance comparable to internal drives, limited by the number and types of attached USB devices, and by the upper limit of the USB interface. Other competing standards for external drive connectivity include eSATA, ExpressCard, FireWire (IEEE 1394), and most recently Thunderbolt.

Another use for USB mass storage devices is the portable execution of software applications (such as web browsers and VoIP clients) with no need to install them on the host computer.

### Media Transfer Protocol

Media Transfer Protocol (MTP) was designed by Microsoft to give higher-level access to a device's filesystem than USB mass storage, at the level of files rather than disk blocks. It also has optional DRM features. MTP was designed for use with portable media players, but it has since been adopted as the primary storage access protocol of the Android operating system from the version 4.1 Jelly Bean as well as Windows Phone 8 (Windows Phone 7 devices had used the Zune protocol—an evolution of MTP). The primary reason for this is that MTP does not require exclusive access to the storage device the way UMS does, alleviating potential problems should an Android program request the storage while it is attached to a computer. The main drawback is that MTP is not as well supported outside of Windows operating systems.

### Human interface devices

A USB mouse or keyboard can usually be used with older computers that have PS/2 ports with the aid of a small USB-to-PS/2 adapter. For mice and keyboards with dual-protocol support, a passive adapter that contains no logic circuitry may be used: the USB hardware in the keyboard or mouse is designed to detect whether it is connected to a USB or PS/2 port, and communicate using the appropriate protocol. Active converters that connect USB keyboards and mice (usually one of each) to PS/2 ports also exist.

### Device Firmware Upgrade mechanism

*Device Firmware Upgrade* (DFU) is a generic mechanism for upgrading the firmware of USB devices with improved versions provided by their manufacturers, offering (for example) a way to deploy firmware bug fixes. During the firmware upgrade operation, USB devices change their operating mode effectively becoming a PROM programmer. Any class of USB device can implement this capability by following the official DFU specifications. Doing so allows use of DFU-compatible host tools to update the device.

DFU is sometimes used as a flash memory programming protocol in microcontrollers with built-in USB bootloader functionality.

Examples of devices can using DFU include iPod and iPhone.

### Audio streaming

The USB Device Working Group has laid out specifications for audio streaming, and specific standards have been developed and implemented for audio class uses, such as microphones, speakers, headsets, telephones, musical instruments, etc. The working group has published four versions of audio device specifications: USB Audio 1.0, 2.0, 3.0 and 4.0, referred to as "USB Audio Class" (UAC) or "Audio Device Class" (ADC).

UAC 3.0 primarily introduces improvements for portable devices, such as reduced power usage by bursting the data and staying in low power mode more often, and power domains for different components of the device, allowing them to be shut down when not in use.

UAC 2.0 introduced support for High Speed USB (in addition to Full Speed), allowing greater bandwidth for multi-channel interfaces, higher sample rates, lower inherent latency, and 8× improvement in timing resolution in synchronous and adaptive modes. UAC2 also introduced the concept of clock domains, which provides information to the host about which input and output terminals derive their clocks from the same source, as well as improved support for audio encodings like DSD, audio effects, channel clustering, user controls, and device descriptions.

UAC 1.0 devices are still common, however, due to their cross-platform driverless compatibility, and also partly due to Microsoft's failure to implement UAC 2.0 for over a decade after its publication, having finally added support to Windows 10 through the Creators Update on 20 March 2017. UAC 2.0 is also supported by macOS, iOS, and Linux, however Android only implements a subset of the UAC 1.0 specification.

USB provides three isochronous (fixed-bandwidth) synchronization types, all of which are used by audio devices:

- Asynchronous — The ADC or DAC are not synced to the host computer's clock at all, operating off a free-running clock local to the device.
- Synchronous — The device's clock is synced to the USB start-of-frame (SOF) or Bus Interval signals. For instance, this can require syncing an 11.2896 MHz clock to a 1 kHz SOF signal, a large frequency multiplication.
- Adaptive — The device's clock is synced to the amount of data sent per frame by the host

While the USB spec originally described asynchronous mode being used in "low cost speakers" and adaptive mode in "high-end digital speakers", the opposite perception exists in the hi-fi world, where asynchronous mode is advertised as a feature, and adaptive/synchronous modes have a bad reputation. In reality, all types can be high-quality or low-quality, depending on the quality of their engineering and the application. Asynchronous has the benefit of being untied from the computer's clock, but the disadvantage of requiring sample rate conversion when combining multiple sources.


## Connectors

The connectors the USB committee specifies support a number of USB's underlying goals, and reflect lessons learned from the many connectors the computer industry has used. The female connector mounted on the host or device is called the *receptacle*, and the male connector attached to the cable is called the *plug*. The official USB specification documents also periodically define the term *male* to represent the plug, and *female* to represent the receptacle.

The design is intended to make it difficult to insert a USB plug into its receptacle incorrectly. The USB specification requires that the cable plug and receptacle be marked so the user can recognize the proper orientation. The USB-C plug however is reversible. USB cables and small USB devices are held in place by the gripping force from the receptacle, with no screws, clips, or thumb-turns as some connectors use.

The distinction of *A* and *B* connectors was to enforce the directionality inherent in USB: The single *host* has Type‑A receptacles and each *peripheral device* has a single Type‑B receptacle. A *hub* provides multiple *downstream*-facing Type‑A receptacles and connects to the host through its single Type‑B receptacle (or a captive cable with a Type‑A plug). A hub may connect to the host either directly or through one or more additional hubs. Prior to Type‑C, USB On-The-Go allowed a device such as a smartphone to take either the *host* or the *peripheral device* role, with a single Type‑AB receptacle (Micro‑AB, superseded in 2014, or Mini-AB, deprecated 2007) that accepted both Type‑A and Type‑B plugs.

USB connector types multiplied as the specification progressed. The original USB specification detailed Standard‑A and Standard‑B plugs and receptacles. These were originally referred to as simply *Type‑A* and *Type‑B*; they were renamed *Standard* out of necessity to distinguish from Mini and later Micro connectors. The data contacts in the Standard plugs are recessed compared to the power and ground contacts so that devices are safely electrically connected before the more delicate data communications circuitry is connected, preventing damage. Some devices operate in different modes depending on whether the data connection is made. Simple power sources do not include data connections, instead shorting the data contacts together, but allow any capable USB device to charge or operate through a standard USB cable. Charging cables provide power connections but not data, though the standard requires at least a USB 2.0 data connection capability. In a non-standard charge-only cable, the data wires are shorted at the device end; otherwise, the device may reject the charger as unsuitable.


## Cabling

The USB 1.1 standard specifies that a standard cable can have a maximum length of 5 meters (16 ft 5 in) with devices operating at full speed (12 Mbit/s), and a maximum length of 3 meters (9 ft 10 in) with devices operating at low speed (1.5 Mbit/s).

USB 2.0 provides for a maximum cable length of 5 meters (16 ft 5 in) for devices running at high speed (480 Mbit/s).

The USB 3.0 standard does not directly specify a maximum cable length, requiring only that all cables meet an electrical specification: for copper cabling with AWG 26 wires the maximum practical length is 3 meters (9 ft 10 in).

### USB bridge "cables"

Two computers (*hosts*) can easily be connected through a USB‑C cable, but before Type‑C hosts could not be connected to each other with common USB cables. USB bridge "cables", or data transfer cables, can be found within the market, offering direct PC to PC connections. A bridge "cable" is actually an electronic device that appears as a USB *peripheral device* to each of the connected *hosts*, allowing peer-to-peer communication between the computers. Such USB bridge cables are used to transfer files between two computers via their USB ports.

Popularized by Microsoft as Windows Easy Transfer, the Microsoft utility used a special USB bridge cable to transfer personal files and settings from a computer running an earlier version of Windows to a computer running a newer version. In the context of the use of *Windows Easy Transfer* software, the bridge cable can sometimes be referenced as *Easy Transfer cable*.

Many USB bridge / data transfer cables are still USB 2.0, but there are also a number of USB 3.0 transfer cables. Despite USB 3.0 being ten times as fast as USB 2.0, USB 3.0 transfer cables are only two to three times as fast given their design.

The USB 3.0 specification introduced an A-to-A cross-over cable without power for connecting two PCs. These are not meant for data transfer but are aimed at diagnostic uses.

#### Dual-role USB connections

USB bridge cables have become less important with USB dual-role-device capabilities introduced with the USB 3.1 specification. Under the most recent specifications, USB supports most scenarios connecting systems directly with a Type-C cable. For the capability to work, however, connected systems must support role-switching. Dual-role capability requires there be *two* controllers within the system, as well as a *role controller*. While this can be expected in a mobile platform such as a tablet or a phone, desktop PCs and laptops often do not support dual roles.


## Power

USB host and hub recepticles supply power at a nominal 5 V DC via the V_BUS pin to upstreaming USB devices.

### Low-power and high-power devices

This section describes the power distribution model of USB that existed before USB Power Delivery (USB-PD). On devices that do not use BC or PD, USB provides up to 4.5 W through Type-A and Type-B connectors, and up to 15 W through USB-C. All pre-PD USB power is provided at 5 V.

For a host providing power to devices, USB has a concept of the *unit load*. Any device may draw power of one unit, and devices may request more power in these discrete steps. It is not required that the host provide requested power, and a device may not draw more power than negotiated.

*Low-power* devices can draw no more than one unit. All devices must act as low-power devices when starting out as unconfigured. For USB devices up to USB 2.0 a unit load is 100 mA (or 500 mW), while USB 3.0 defines a unit load as 150 mA (750 mW). Full-featured USB-C can support low-power devices with a unit load of 250 mA (or 1250 mW).

*High-power* devices, e.g. typical 2.5-inch hard disk drives, can draw more than one unit. USB up to 2.0 allows a host or hub to provide up to 2.5 W to each device, in five discrete steps of 100 mA, and SuperSpeed devices (USB 3.x) allows a host or a hub to provide up to 4.5 W in six steps of 150 mA. USB-C allows for dual-lane operation of USB 3.x with larger unit load (250 mA; up to 7.5 W). USB-C also allows for Type-C Current as a replacement for USB BC, signaling power availability in a simple way, without needing any data connection.

| Specification | max current | Voltage | max power |
|---|---|---|---|
| Low-power device up to USB 2.0 | 100 mA | 5 V | 0.50 W |
| Low-power SuperSpeed / USB 3.x device | 150 mA | 5 V | 0.75 W |
| High-power device up to USB 2.0 | 500 mA | 5 V | 2.5 W |
| High-power SuperSpeed / USB 3.x single-lane device | 900 mA | 5 V | 4.5 W |
| High-power SuperSpeed / USB 3.x dual-lane device | 1.5 A | 5 V | 7.5 W |
| Battery Charging (BC) | 1.5 A | 5 V | 7.5 W |
| Type-C | 1.5 A, 3 A | 5 V | 7.5 W, 15 W |
| Power Delivery SPR | 5 A | up to 20 V | 100 W |
| Power Delivery EPR | 5 A | up to 48 V | 240 W |
| The VBUS supply from a low-powered hub port may drop to 4.40 V. Up to five unit loads; with non-SuperSpeed devices, one unit load is 100 mA. Up to six unit loads; with SuperSpeed devices, one unit load is 150 mA. for USB-C only Up to six unit loads; with multi-lane devices, one unit load is 250 mA. >3 A (>60 W) operation requires an electronically marked cable rated at 5 A. >20 V (>100 W) operation requires an electronically marked Extended Power Range (EPR) cable. |   |   |   |

To recognize Battery Charging mode, a dedicated charging port places a resistance not exceeding 200 Ω across the D+ and D− terminals. Shorted or near-shorted data lanes with less than 200 Ω of resistance across the D+ and D− terminals signify a dedicated charging port (DCP) with indefinite charging rates.

In addition to standard USB, there is a proprietary high-powered system known as PoweredUSB, developed in the 1990s, and mainly used in point-of-sale terminals such as cash registers.
