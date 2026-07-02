---
title: "USB - Wikipedia (part 2/2)"
source: https://en.wikipedia.org/wiki/USB
domain: hardware-interfaces
license: CC-BY-SA-4.0
tags: i2c, spi bus, uart, can bus, gpio, pwm, serial port, jtag
fetched: 2026-07-02
part: 2/2
---

## Signaling

USB signals are transmitted using differential signaling on twisted-pair data wires with 90 Ω ± 15% characteristic impedance. USB 2.0 and earlier specifications define a single pair in half-duplex (HDx). USB 3.0 and later specifications define one dedicated pair for USB 2.0 compatibility and two or four pairs for data transfer: two data wire pairs realising full-duplex (FDx) for single lane (*×1*) variants require at least SuperSpeed (SS) connectors; four pairs realising full-duplex for two lane (*×2*) variants require USB-C connectors.

USB4 Gen 4 requires the use of all four pairs but allow for asymmetrical pairs configuration. In this case one data wire pair is used for the upstream data and the other three for the downstream data or vice-versa. USB4 Gen 4 use pulse-amplitude modulation on three levels, providing a trit of information every baud transmitted, the transmission frequency of 12.8 GHz translate to a transmission rate of 25.6 GBd and the 11-bit–to–7-trit translation provides a theoretical maximum transmission speed just over 40.2 Gbit/s.

USB Data operation modes

Operation mode name

Introduced in

Lanes

Encoding

# data wires

Nominal signaling rate

Original label

USB-IF

current

current

old

marketing name

logo

Low-Speed

—

N/a

USB 1.0

1

HDx

NRZI

2

1.5 Mbit/s

half-duplex

Low-Speed USB (LS)

Basic-Speed USB

Full-Speed

12

Mbit/s

half-duplex

Full-Speed USB (FS)

High-Speed

USB 2.0

480

Mbit/s

half-duplex

Hi-Speed USB (HS)

USB 3.2 Gen

1

×1

USB

3.0,

USB

3.1 Gen

1

USB 3.0

1

FDx

(+ 1 HDx)

8b/10b

6

5

Gbit/s

symmetric

SuperSpeed USB (SS)

USB 5Gbps

USB

3.2 Gen

2

×1

USB

3.1 Gen

2

USB 3.1

128b/132b

10

Gbit/s

symmetric

SuperSpeed+ (SS+)

USB 10Gbps

USB

3.2 Gen

1

×2

—

N/a

USB 3.2

2 FDx (+ 1 HDx)

8b/10b

10

10

Gbit/s

symmetric

—

N/a

USB

3.2 Gen

2

×2

128b/132b

20

Gbit/s

symmetric

SuperSpeed USB 20Gbps

USB 20Gbps

USB4 Gen

2

×1

USB4

1 FDx (+ 1 HDx)

64b/66b

6 (used of 10)

10

Gbit/s

symmetric

USB 10Gbps

USB4 Gen

2

×2

2 FDx (+ 1 HDx)

10

20

Gbit/s

symmetric

USB 20Gbps

USB4 Gen

3

×1

1 FDx (+ 1 HDx)

128b/132b

6 (used of 10)

20

Gbit/s

symmetric

USB4 Gen

3

×2

2 FDx (+ 1 HDx)

10

40

Gbit/s

symmetric

USB 40Gbps

USB4 Gen

4

×2

USB4 2.0

2 FDx (+ 1 HDx)

PAM-3

11b/7

t

10

80 Gbit/s

symmetric

USB 80Gbps

asymmetric (+ 1 HDx)

40

Gbit/s

up

120

Gbit/s down

—

N/a

120

Gbit/s

up

40

Gbit/s down

1. USB 2.0 implementation
2. USB4 can use optional Reed–Solomon forward error correction (RS FEC). In this mode, 12 × 16 B (128 bit) symbols are assembled together with 2 B (12 bit + 4 bit reserved) synchronization bits indicating the respective symbol types and 4 B of RS FEC to allow to correct up to 1 B of errors anywhere in the total 198 B block.

- **Low-speed (LS)** and **Full-speed (FS)** modes use a single data wire pair, labeled D+ and D−, in half-duplex. Transmitted signal levels are 0.0–0.3 V for logical low, and 2.8–3.6 V for logical high level. The signal lines are not terminated.
- **High-speed (HS)** uses the same wire pair, but with different electrical conventions. Lower signal voltages of −10 to 10 mV for low and 360 to 440 mV for logical high level, and termination of 45 Ω to ground or 90 Ω differential to match the data cable impedance.
- **SuperSpeed (SS)** adds two additional pairs of shielded twisted data wires (and new, mostly compatible expanded connectors) besides another grounding wire. These are dedicated to full-duplex SuperSpeed operation. The SuperSpeed link operates independently from the USB 2.0 channel and takes precedence on connection. Link configuration is performed using LFPS (Low Frequency Periodic Signaling, approximately at 20 MHz frequency), and electrical features include voltage de-emphasis at the transmitter side, and adaptive linear equalization on the receiver side to combat electrical losses in transmission lines, and thus the link introduces the concept of *link training*.
- **SuperSpeed+ (SS+)** uses a new coding scheme with an increased signaling rate (Gen 2×1 mode) and/or the additional lane of USB-C (Gen 1×2 and Gen 2×2 modes).

A USB connection is always between an *A* end, a downstream-facing port (DFP) of either a *host* or a *hub*, and a *B* end, the upstream-facing port (UFP) of either a *peripheral device* or a *hub*. Historically, this was made clear by the fact that hosts had only Type-A and peripheral devices had only Type-B ports, and every compatible cable had one Type-A plug and one Type-B plug.

USB-C (Type-C) is a single connector that replaces all legacy Type-A and Type-B connectors, so when both sides are equipment with USB Type-C ports, normally the device's type defines which is the DFP and which is the UFP. Some devices, e.g. modern smart phones, can act as both. Consequently, the connected devices negotiate which is the *host* and which is the *peripheral device*.


## Protocol layer

During USB communication, data is transmitted as packets. Initially, all packets are sent from the host via the root hub, and possibly more hubs, to devices. Some of those packets direct a device to send some packets in reply.


## Transactions

The basic transactions of USB are:

- OUT transaction
- IN transaction
- SETUP transaction
- Control transfer exchange

### Media Agnostic USB

The USB Implementers Forum introduced the Media Agnostic USB (MA-USB) v.1.0 wireless communication standard based on the USB protocol on 29 July 2015. Wireless USB is a cable-replacement technology, and uses ultra-wideband wireless technology for data rates of up to 480 Mbit/s.

The USB-IF used WiGig Serial Extension v1.2 specification as its initial foundation for the MA-USB specification and is compliant with SuperSpeed USB (3.0 and 3.1) and Hi-Speed USB (USB 2.0). Devices that use MA-USB will be branded as "Powered by MA-USB", provided the product qualifies its certification program.

### InterChip USB

InterChip USB is a chip-to-chip variant that eliminates the conventional transceivers found in normal USB. The HSIC physical layer uses about 50% less power and 75% less board area compared to USB 2.0. It is an alternative standard to SPI and I2C.

### USB-C

USB-C (officially *USB Type-C*) is a standard that defines a new connector, and several new connection features. Among them it supports *Alternate Mode*, which allows transporting other protocols via the USB-C connector and cable. This is commonly used to support the DisplayPort or HDMI protocols, which allows connecting a display, such as a computer monitor or television set, via USB-C.

All other connectors are not capable of two-lane operations (Gen 1×2 and Gen 2×2) in USB 3.2, but can be used for one-lane operations (Gen 1×1 and Gen 2×1).

### DisplayLink

DisplayLink is a technology which allows multiple displays to be connected to a computer via USB. It was introduced around 2006, and before the advent of Alternate Mode over USB-C it was the only way to connect displays via USB. It is a proprietary technology, not standardized by the USB Implementers Forum and typically requires a separate device driver on the computer.


## Comparisons with other connection methods

### FireWire (IEEE 1394)

At first, USB was considered a complement to FireWire (IEEE 1394) technology, which was designed as a high-bandwidth serial bus that efficiently interconnects peripherals such as disk drives, audio interfaces, and video equipment. In the initial design, USB operated at a far lower data rate and used less sophisticated hardware. It was suitable for small peripherals such as keyboards and pointing devices.

The most significant technical differences between FireWire and USB include:

- USB networks use a tiered-star topology, while IEEE 1394 networks use a tree topology.
- USB 1.0, 1.1, and 2.0 use a "speak-when-spoken-to" protocol, meaning that each peripheral communicates with the host when the host specifically requests communication. USB 3.0 allows for device-initiated communications towards the host. A FireWire device can communicate with any other node at any time, subject to network conditions.
- A USB network relies on a single host at the top of the tree to control the network. All communications are between the host and one peripheral. In a FireWire network, any capable node can control the network.
- USB runs with a 5 V power line, while FireWire supplies 12 V and theoretically can supply up to 30 V.
- Standard USB hub ports can provide from the typical 500 mA/2.5 W of current, only 100 mA from non-hub ports. USB 3.0 and USB On-The-Go supply 1.8 A/9.0 W (for dedicated battery charging, 1.5 A/7.5 W full bandwidth or 900 mA/4.5 W high bandwidth), while FireWire can in theory supply up to 60 watts of power, although 10 to 20 watts is more typical.

These and other differences reflect the differing design goals of the two buses: USB was designed for simplicity and low cost, while FireWire was designed for high performance, particularly in time-sensitive applications such as audio and video. Although similar in theoretical maximum signaling rate, FireWire 400 is faster than USB 2.0 high-bandwidth in real-use, especially in high-bandwidth use such as external hard drives. The newer FireWire 800 standard is twice as fast as FireWire 400 and faster than USB 2.0 high-bandwidth both theoretically and practically. However, FireWire's speed advantages rely on low-level techniques such as direct memory access (DMA), which in turn have created opportunities for security exploits such as the DMA attack.

The chipset and drivers used to implement USB and FireWire have a crucial impact on how much of the bandwidth prescribed by the specification is achieved in the real world, along with compatibility with peripherals.

### Ethernet

The *IEEE 802.3af*, *802.3at*, and *802.3bt* Power over Ethernet (PoE) standards specify more elaborate power negotiation schemes than powered USB. They operate at 48 V DC and can supply more power (up to 12.95 W for *802.3af*, 25.5 W for *802.3at*, a.k.a. *PoE+*, 71 W for *802.3bt*, a.k.a. *4PPoE*) over a cable up to 100 meters compared to USB 2.0, which provides 2.5 W with a maximum cable length of 5 meters. This has made PoE popular for Voice over IP telephones, security cameras, wireless access points, and other networked devices within buildings. However, USB is cheaper than PoE provided that the distance is short and power demand is low.

Ethernet standards require electrical isolation between the networked device (computer, phone, etc.) and the network cable up to 1500 V AC or 2250 V DC for 60 seconds. USB has no such requirement as it was designed for peripherals closely associated with a host computer, and in fact it connects the peripheral and host grounds. This gives Ethernet a significant safety advantage over USB with peripherals such as cable and DSL modems connected to external wiring that can assume hazardous voltages under certain fault conditions.

### MIDI

The *USB Device Class Definition for MIDI Devices* transmits Music Instrument Digital Interface (MIDI) music data over USB. The MIDI capability is extended to allow up to sixteen simultaneous *virtual MIDI cables*, each of which can carry the usual MIDI sixteen channels and clocks.

USB is competitive for low-cost and physically adjacent devices. However, Power over Ethernet and the MIDI plug standard have an advantage in high-end devices that may have long cables. USB can cause ground loop problems between equipment, because it connects ground references on both transceivers. By contrast, the MIDI plug standard and Ethernet have built-in isolation to 500V or more.

### eSATA/eSATAp

The eSATA connector is a more robust SATA connector, intended for connection to external hard drives and SSDs. eSATA's transfer rate (up to 6 Gbit/s) is similar to that of USB 3.0 (up to 5 Gbit/s) and USB 3.1 (up to 10 Gbit/s). A device connected by eSATA appears as an ordinary SATA device, giving both full performance and full compatibility associated with internal drives.

eSATA does not supply power to external devices. This is an increasing disadvantage compared to USB. Even though USB 3.0's 4.5 W is sometimes insufficient to power external hard drives, technology is advancing, and external drives gradually need less power, diminishing the eSATA advantage. eSATAp (power over eSATA, a.k.a. ESATA/USB) is a connector introduced in 2009 that supplies power to attached devices using a new, backward compatible, connector. On a notebook eSATAp usually supplies only 5 V to power a 2.5-inch HDD/SSD; on a desktop workstation it can additionally supply 12 V to power larger devices including 3.5-inch HDD/SSD and 5.25-inch optical drives.

eSATAp support can be added to a desktop machine in the form of a bracket connecting the motherboard SATA, power, and USB resources.

eSATA, like USB, supports hot plugging, although this might be limited by OS drivers and device firmware.

### Thunderbolt

Thunderbolt combines PCI Express and DisplayPort into a new serial data interface. Original Thunderbolt implementations have two channels, each with a transfer speed of 10 Gbit/s, resulting in an aggregate unidirectional bandwidth of 20 Gbit/s.

Thunderbolt 2 uses link aggregation to combine the two 10 Gbit/s channels into one bidirectional 20 Gbit/s channel.

Thunderbolt 3 and Thunderbolt 4 use USB-C. Thunderbolt 3 has two physical 20 Gbit/s bi-directional channels, aggregated to appear as a single logical 40 Gbit/s bi-directional channel. Thunderbolt 3 controllers can incorporate a USB 3.1 Gen 2 controller to provide compatibility with USB devices. They are also capable of providing DisplayPort Alternate Mode as well as DisplayPort over USB4 Fabric, making the function of a Thunderbolt 3 port a superset of that of a USB 3.1 Gen 2 port.

DisplayPort Alternate Mode 2.0: USB4 (requiring USB-C) requires that hubs support DisplayPort 2.0 over a USB-C Alternate Mode. DisplayPort 2.0 can support 8K resolution at 60 Hz with HDR10 color. DisplayPort 2.0 can use up to 80 Gbit/s, which is double the amount available to USB data, because it sends all the data in one direction (to the monitor) and can thus use all eight data wires at once.

After the specification was made royalty-free and custodianship of the Thunderbolt protocol was transferred from Intel to the USB Implementers Forum, Thunderbolt 3 has been effectively implemented in the USB4 specification – with compatibility with Thunderbolt 3 optional but encouraged for USB4 products.


## Interoperability

Various protocol converters are available that convert USB data signals to and from other communications standards.


## Security threats

Due to the USB standard's plug-and-play nature, host computers are vulnerable to USB devices containing malicious software. It is possible to create a device that looks like a flash drive, but when plugged in, simulates a keyboard and types malicious commands. For example, on a computer running Microsoft Windows, the device can wait a set amount of time, then open PowerShell and download a malware script. The attack is called a BadUSB attack.

Another malicious device is a USB killer, which sends high voltage pulses across the data lines, destroying or damaging whatever it is plugged into.

In versions of Microsoft Windows before Windows XP, Windows would automatically run a script (if present) on certain devices via AutoRun, one of which are USB mass storage devices, which may contain malicious software.

It is possible to gain full system control by hacking a USB controller.
