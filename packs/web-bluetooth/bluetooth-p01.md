---
title: "Bluetooth (part 1/2)"
source: https://en.wikipedia.org/wiki/Bluetooth
domain: web-bluetooth
license: CC-BY-SA-4.0
tags: web bluetooth api, bluetooth low energy gatt, gatt service characteristic, bluetooth device pairing
fetched: 2026-07-02
part: 1/2
---

# Bluetooth

**Bluetooth** is a short-range wireless technology standard that is used for exchanging data between fixed and mobile devices over short distances and building personal area networks (PANs). In the most widely used mode, transmission power is limited to 2.5 milliwatts, giving it a very short range of up to 10 metres (33 ft). It employs UHF radio waves in the ISM bands, from 2.402 GHz to 2.48 GHz. It is mainly used as an alternative to wired connections to exchange files between nearby portable devices and connect cell phones and music players with wireless headphones, wireless speakers, HIFI systems, car audio and wireless transmission between TVs and soundbars.

Bluetooth is managed by the Bluetooth Special Interest Group (SIG), which has more than 35,000 member companies in the areas of telecommunication, computing, networking, and consumer electronics. The IEEE standardized Bluetooth as **IEEE 802.15.1** but no longer maintains the standard. The Bluetooth SIG oversees the development of the specification, manages the qualification program, and protects the trademarks. A manufacturer must meet Bluetooth SIG standards to market it as a Bluetooth device. A network of patents applies to the technology, which is licensed to individual qualifying devices. As of 2021, 4.7 billion Bluetooth integrated circuit chips are shipped annually. Bluetooth was first demonstrated in space in 2024, an early test envisioned to enhance IoT capabilities.


## Etymology

The name "Bluetooth" was proposed in 1997 by Jim Kardach of Intel, one of the founders of the Bluetooth SIG. The name was inspired by a conversation with Sven Mattisson who related Scandinavian history through tales from Frans G. Bengtsson's *The Long Ships*, a historical novel about Vikings and the 10th-century Danish king Harald Bluetooth. Upon discovering a picture of the runestone of Harald Bluetooth in the book *A History of the Vikings* by Gwyn Jones, Kardach proposed Bluetooth as the codename for the short-range wireless program.

According to Bluetooth's official website,

> Bluetooth was only intended as a placeholder until marketing could come up with something really cool.
> 
> Later, when it came time to select a serious name, Bluetooth was to be replaced with either RadioWire or PAN (Personal Area Networking). PAN was the front runner, but an exhaustive search discovered it already had tens of thousands of hits throughout the internet.
> 
> A full trademark search on RadioWire couldn't be completed in time for launch, making Bluetooth the only choice. The name caught on fast and before it could be changed, it spread throughout the industry, becoming synonymous with short-range wireless technology.

Bluetooth is the Anglicised version of the Scandinavian *Blåtand*/*Blåtann* (or in Old Norse *blátǫnn*). It was the epithet of King Harald Bluetooth, who united the disparate Danish tribes into a single kingdom; Kardach chose the name to imply that Bluetooth similarly unites communication protocols.

### Logo

The Bluetooth logo is a bind rune merging the Younger Futhark runes  (ᚼ, Hagall) and  (ᛒ, Bjarkan), Harald's initials.


## History

The development of the "short-link" radio technology, later named Bluetooth, was initiated in 1989 by Nils Rydbeck, CTO at Ericsson Mobile in Lund, Sweden. The purpose was to develop wireless headsets, according to two inventions by Johan Ullman, SE 8902098-6, issued 12 June 1989  and SE 9202239, issued 24 July 1992 . Nils Rydbeck tasked Tord Wingren with specifying and Dutchman Jaap Haartsen and Sven Mattisson with developing. Both were working for Ericsson in Lund. Principal design and development began in 1994 and by 1997 the team had a workable solution. From 1997 Örjan Johansson became the project leader and propelled the technology and standardization.

In 1997, Adalio Sanchez, then head of IBM ThinkPad product R&D, approached Nils Rydbeck about collaborating on integrating a mobile phone into a ThinkPad notebook. The two assigned engineers from Ericsson and IBM studied the idea. The conclusion was that power consumption on cellphone technology at that time was too high to allow viable integration into a notebook and still achieve adequate battery life. Instead, the two companies agreed to integrate Ericsson's short-link technology on both a ThinkPad notebook and an Ericsson phone to accomplish the goal.

Since neither IBM ThinkPad notebooks nor Ericsson phones were the market share leaders in their respective markets at that time, Adalio Sanchez and Nils Rydbeck agreed to make the short-link technology an open industry standard to permit each player maximum market access. Ericsson contributed the short-link radio technology, and IBM contributed patents around the logical layer. Adalio Sanchez of IBM then recruited Stephen Nachtsheim of Intel to join and then Intel also recruited Toshiba and Nokia. In May 1998, the Bluetooth SIG was launched with IBM and Ericsson as the founding signatories and a total of five members: Ericsson, Intel, Nokia, Toshiba, and IBM.

The first Bluetooth device was revealed in 1999. It was a hands-free mobile headset that earned the "Best of show Technology Award" at COMDEX. The first Bluetooth mobile phone was the unreleased prototype Ericsson T36, though it was the revised Ericsson model T39 that actually made it to store shelves in June 2001. However Ericsson released the R520m in Quarter 1 of 2001, making the R520m the first ever commercially available Bluetooth phone. In parallel, IBM introduced the IBM ThinkPad A30 in October 2001 which was the first notebook with integrated Bluetooth.

Bluetooth's early incorporation into consumer electronics products continued at Vosi Technologies in Costa Mesa, California, initially overseen by founding members Bejan Amini and Tom Davidson. Vosi Technologies had been created by real estate developer Ivano Stegmenga, with United States Patent 608507, for communication between a cellular phone and a vehicle's audio system. At the time, Sony/Ericsson had only a minor market share in the cellular phone market, which was dominated in the US by Nokia and Motorola. Due to ongoing negotiations for an intended licensing agreement with Motorola beginning in the late 1990s, Vosi could not publicly disclose the intention, integration, and initial development of other enabled devices which were to be the first "Smart Home" internet connected devices.

Vosi needed a means for the system to communicate without a wired connection from the vehicle to the other devices in the network. Bluetooth was chosen, since Wi-Fi was not yet readily available or supported in the public market. Vosi had begun to develop the Vosi Cello integrated vehicular system and some other internet connected devices, one of which was intended to be a table-top device named the Vosi Symphony, networked with Bluetooth. Through the negotiations with Motorola, Vosi introduced and disclosed its intent to integrate Bluetooth in its devices. In the early 2000s a legal battle ensued between Vosi and Motorola, which indefinitely suspended release of the devices. Later, Motorola implemented it in their devices, which initiated the significant propagation of Bluetooth in the public market due to its large market share at the time.

In 2012, Jaap Haartsen was nominated by the European Patent Office for the European Inventor Award.


## Implementation

Bluetooth operates at frequencies between 2.402 and 2.480 GHz, or 2.400 and 2.4835 GHz, including guard bands 2 MHz wide at the bottom end and 3.5 MHz wide at the top. This is in the globally unlicensed (but not unregulated) industrial, scientific and medical (ISM) 2.4 GHz short-range radio frequency band. Bluetooth uses a radio technology called frequency-hopping spread spectrum. Bluetooth divides transmitted data into packets, and transmits each packet on one of 79 designated Bluetooth channels. Each channel has a bandwidth of 1 MHz. It usually performs 1600 hops per second, with adaptive frequency-hopping (AFH) enabled. Bluetooth Low Energy uses 2 MHz spacing, which accommodates 40 channels.

Originally, Gaussian frequency-shift keying (GFSK) modulation was the only modulation scheme available. Since the introduction of Bluetooth 2.0+EDR, π/4-DQPSK (differential quadrature phase-shift keying) and 8-DPSK modulation may also be used between compatible devices. Devices functioning with GFSK are said to be operating in basic rate (BR) mode, where an instantaneous bit rate of 1 Mbit/s is possible. The term *Enhanced Data Rate* (*EDR*) is used to describe π/4-DPSK (EDR2) and 8-DPSK (EDR3) schemes, transferring 2 and 3 Mbit/s respectively.

In 2019, Apple published an extension called HDR which supports data rates of 4 (HDR4) and 8 (HDR8) Mbit/s using π/4-DQPSK modulation on 4 MHz channels with forward error correction (FEC).

Bluetooth is a packet-based protocol with a master/slave architecture. One master may communicate with up to seven slaves in a piconet. All devices within a given piconet use the clock provided by the master as the base for packet exchange. The master clock ticks with a period of 312.5 μs, two clock ticks then make up a slot of 625 μs, and two slots make up a slot pair of 1250 μs. In the simple case of single-slot packets, the master transmits in even slots and receives in odd slots. The slave, conversely, receives in even slots and transmits in odd slots. Packets may be 1, 3, or 5 slots long, but in all cases, the master's transmission begins in even slots and the slave's in odd slots.

The above excludes Bluetooth Low Energy, introduced in the 4.0 specification, which uses the same spectrum but somewhat differently.

### Communication and connection

A master BR/EDR Bluetooth device can communicate with a maximum of seven devices in a piconet (an ad hoc computer network using Bluetooth technology), though not all devices reach this maximum. The devices can switch roles, by agreement, and the slave can become the master (for example, a headset initiating a connection to a phone necessarily begins as master—as an initiator of the connection—but may subsequently operate as the slave).

The Bluetooth Core Specification provides for the connection of two or more piconets to form a scatternet, in which certain devices simultaneously play the master/leader role in one piconet and the slave role in another.

At any given time, data can be transferred between the master and one other device (except for the little-used broadcast mode). The master chooses which slave device to address; typically, it switches rapidly from one device to another in a round-robin fashion. Since it is the master that chooses which slave to address, whereas a slave is (in theory) supposed to listen in each receive slot, being a master is a lighter burden than being a slave. Being a master of seven slaves is possible; being a slave of more than one master is possible. The specification is vague as to required behavior in scatternets.


## Uses

Bluetooth is a standard wire-replacement communications protocol primarily designed for low power consumption, with a short range based on low-cost transceiver microchips in each device. Because the devices use a radio (broadcast) communications system, they do not have to be in visual line of sight of each other; however, a *quasi optical* wireless path must be viable.

### Bluetooth classes and power use

| Class | Maximum permitted power |   |
|---|---|---|
| mW | dBm |   |
| 1 | 10–100 | +10–+20 |
| 1.5* | 2.5–10 | +4–+10 |
| 2 | 1–2.5 | 0–+4 |
| 3 | 0.01–1 | −20–0 |
| * Class 1.5 included in Class 1 for BR/EDR |   |   |
| Source: Bluetooth Core Specification revision 5.3, Volume 6, Part A, § 3, and Volume 2, Part A, § 3, Bluetooth SIG |   |   |

Historically, the Bluetooth range was defined by the radio class, with a lower class (and higher output power) having larger range. The actual range of a given link depends on several qualities of both communicating devices and the air and obstacles in between. The primary attributes affecting range are the data rate, protocol (Bluetooth Classic or Bluetooth Low Energy), transmission power, and receiver sensitivity, and the relative orientations and gains of both antennas.

The effective range varies depending on propagation conditions, material coverage, production sample variations, antenna configurations and battery conditions. Most Bluetooth applications are for indoor conditions, where attenuation of walls and signal fading due to signal reflections make the range far lower than specified line-of-sight ranges of the Bluetooth products.

Most Bluetooth applications are battery-powered Class 2 devices, with little difference in range whether the other end of the link is a Class 1 or Class 2 device as the lower-powered device tends to set the range limit. In some cases the effective range of the data link can be extended when a Class 2 device is connecting to a Class 1 transceiver with both higher sensitivity and transmission power than a typical Class 2 device. In general, however, Class 1 devices have sensitivities similar to those of Class 2 devices. Connecting two Class 1 devices with both high sensitivity and high power can allow ranges far in excess of the typical 100 m, depending on the throughput required by the application. Some such devices allow open field ranges of up to 1 km and beyond between two similar devices without exceeding legal emission limits.

### Bluetooth profile

To use Bluetooth wireless technology, a device must be able to interpret certain Bluetooth profiles. For example,

- The Headset Profile (HSP) connects headphones and earbuds to a cell phone or laptop.
- The Health Device Profile (HDP) can connect a cell phone to a digital thermometer or heart rate detector.
- The Video Distribution Profile (VDP) sends a video stream from a video camera to a TV screen or a recording device.

Profiles are definitions of possible applications and specify general behaviors that Bluetooth-enabled devices use to communicate with other Bluetooth devices. These profiles include settings to parameterize and to control the communication from the start. Adherence to profiles saves the time for transmitting the parameters anew before the bi-directional link becomes effective. There are a wide range of Bluetooth profiles that describe many different types of applications or use cases for devices.

### List of applications

- Wireless control and communication between a mobile phone and a handsfree headset. This was one of the earliest applications to become popular.
- Wireless control of audio and communication functions between a mobile phone and a Bluetooth compatible car stereo system (and sometimes between the SIM card and the car phone).
- Wireless communication between a smartphone and a smart lock for unlocking doors.
- Wireless control of and communication with iOS and Android device phones, tablets and portable wireless speakers.
- Wireless Bluetooth headset and intercom. Idiomatically, a headset is sometimes called "a Bluetooth".
- Wireless streaming of audio to headphones with or without communication capabilities.
- Wireless streaming of data collected by Bluetooth-enabled fitness devices to phone or PC.
- Wireless networking between PCs in a confined space and where little bandwidth is required.
- Wireless communication with PC input and output devices, the most common being the mouse, keyboard and printer.
- Transfer of files, contact details, calendar appointments, and reminders between devices with OBEX and sharing directories via FTP.
- Triggering the camera shutter of a smartphone using a Bluetooth controlled selfie stick.
- Replacement of previous wired RS-232 serial communications in test equipment, GPS receivers, medical equipment, bar code scanners, and traffic control devices.
- For controls where infrared was often used.
- For low bandwidth applications where higher USB bandwidth is not required and cable-free connection desired.
- Sending small advertisements from Bluetooth-enabled advertising hoardings to other, discoverable, Bluetooth devices.
- Wireless bridge between two Industrial Ethernet (e.g., PROFINET) networks.
- Game consoles have been using Bluetooth as a wireless communications protocol for peripherals since the seventh generation, including Nintendo's Wii and Sony's PlayStation 3 which use Bluetooth for their respective controllers.
- Dial-up internet access on personal computers or PDAs using a data-capable mobile phone as a wireless modem.
- Short-range transmission of health sensor data from medical devices to mobile phone, set-top box or dedicated telehealth devices.
- Allowing a DECT phone to ring and answer calls on behalf of a nearby mobile phone.
- Real-time location systems (RTLS) are used to track and identify the location of objects in real time using "Nodes" or "tags" attached to, or embedded in, the objects tracked, and "Readers" that receive and process the wireless signals from these tags to determine their locations.
- Personal security application on mobile phones for prevention of theft or loss of items. The protected item has a Bluetooth marker (e.g., a tag) that is in constant communication with the phone. If the connection is broken (the marker is out of range of the phone) then an alarm is raised. This can also be used as a man overboard alarm.
- Calgary, Alberta, Canada's Roads Traffic division uses data collected from travelers' Bluetooth devices to predict travel times and road congestion for motorists.
- Wireless transmission of audio (a more reliable alternative to personal FM transmitters)
- Live video streaming to the visual cortical implant device by Nabeel Fattah in Newcastle university 2017.
- Connection of motion controllers to a PC when using VR headsets
- Wireless connection between TVs and soundbars.

### Devices

Bluetooth exists in numerous products such as telephones, speakers, tablets, media players, robotics systems, laptops, and game console equipment as well as some high definition headsets, modems, hearing aids and even watches. Bluetooth is useful when transferring information between two or more devices that are near each other in low-bandwidth situations. Bluetooth is commonly used to transfer sound data with telephones (i.e., with a Bluetooth headset) or byte data with hand-held computers (transferring files).

Bluetooth protocols simplify the discovery and setup of services between devices. Bluetooth devices can advertise all of the services they provide. This makes using services easier, because more of the security, network address and permission configuration can be automated than with many other network types.


## Computer requirements

A personal computer that does not have embedded Bluetooth can use a Bluetooth adapter that enables the PC to communicate with Bluetooth devices. While some desktop computers and most recent laptops come with a built-in Bluetooth radio, others require an external adapter, typically in the form of a small USB "dongle".

Unlike its predecessor, IrDA, which requires a separate adapter for each device, Bluetooth lets multiple devices communicate with a computer over a single adapter.

### Operating system implementation

For Microsoft platforms, Windows XP Service Pack 2 and SP3 releases work natively with Bluetooth v1.1, v2.0 and v2.0+EDR. Previous versions required users to install their Bluetooth adapter's own drivers, which were not directly supported by Microsoft. Microsoft's own Bluetooth dongles (packaged with their Bluetooth computer devices) have no external drivers and thus require at least Windows XP Service Pack 2. Windows Vista RTM/SP1 with the Feature Pack for Wireless or Windows Vista SP2 work with Bluetooth v2.1+EDR. Windows 7 works with Bluetooth v2.1+EDR and Extended Inquiry Response (EIR). The Windows XP and Windows Vista/Windows 7 Bluetooth stacks support the following Bluetooth profiles natively: PAN, SPP, DUN, HID, HCRP. The Windows XP stack can be replaced by a third party stack that supports more profiles or newer Bluetooth versions. The Windows Vista/Windows 7 Bluetooth stack supports vendor-supplied additional profiles without requiring that the Microsoft stack be replaced. Windows 8 and later support Bluetooth Low Energy (BLE). It is generally recommended to install the latest vendor driver and its associated stack to be able to use the Bluetooth device at its fullest extent.

Apple products have worked with Bluetooth since Mac OS X v10.2, which was released in 2002.

Linux has two popular Bluetooth stacks, BlueZ and Fluoride. The BlueZ stack is included with most Linux kernels and was originally developed by Qualcomm. Fluoride, earlier known as Bluedroid, is included in Android OS and was originally developed by Broadcom. There is also Affix stack, developed by Nokia. It was once popular, but has not been updated since 2005.

FreeBSD has included Bluetooth since its v5.0 release, implemented through netgraph.

NetBSD has included Bluetooth since its v4.0 release. Its Bluetooth stack was ported to OpenBSD as well, however OpenBSD later removed it as unmaintained.

DragonFly BSD has had NetBSD's Bluetooth implementation since 1.11 (2008). A netgraph-based implementation from FreeBSD has also been available in the tree, possibly disabled until 2014-11-15, and may require more work.


## Specifications and features

| Version | Adoption year | Maximum rate | Max range | Radio frequency |   |   |
|---|---|---|---|---|---|---|
| Major | Minor | Classic | Low Energy |   |   |   |
| 1 | 1.0 | 1999 | 732.2 kbit/s | —N/a | 10 m | 2.4 GHz |
| 1.1 | 2001 |   |   |   |   |   |
| 1.2 | 2003 | 1 Mbit/s |   |   |   |   |
| 2 | 2.0 | 2004 | 2.1 Mbit/s |   |   |   |
| 2.1 | 2007 |   |   |   |   |   |
| 3 | 3.0 | 2009 |   |   |   |   |
| 4 | 4.0 | 2009 | 1 Mbit/s | 60 m |   |   |
| 4.1 | 2013 |   |   |   |   |   |
| 4.2 | 2014 |   |   |   |   |   |
| 5 | 5.0 | 2016 | 2 Mbit/s | 240 m |   |   |
| 5.1 | 2019 |   |   |   |   |   |
| 5.2 | 2020 |   |   |   |   |   |
| 5.3 | 2021 |   |   |   |   |   |
| 5.4 | 2023 |   |   |   |   |   |
| 6 | 6.0 | 2024 | 3 Mbit/s | 300 m |   |   |
| 6.1 | 2025 | ? | ? | ? |   |   |
| 6.2 | ? | ? | ? |   |   |   |

The specifications were formalized by the Bluetooth Special Interest Group (SIG) and formally announced on 20 May 1998. In 2014 it had a membership of over 30,000 companies worldwide. It was established by Ericsson, IBM, Intel, Nokia and Toshiba, and later joined by many other companies.

All versions of the Bluetooth standards are backward-compatible with all earlier versions.

The Bluetooth Core Specification Working Group (CSWG) produces mainly four kinds of specifications:

- The Bluetooth Core Specification – typically released every few years
- Core Specification Addendum (CSA)
- Core Specification Supplements (CSS) – can be released more frequently than Addenda
- Errata – published privately to Bluetooth SIG members

### Bluetooth 1.0 and 1.0B

- Products were not interoperable.
- Anonymity was not possible, preventing certain services from using Bluetooth environments.

### Bluetooth 1.1

- Ratified as IEEE Standard 802.15.1–2002
- Many errors found in the v1.0B specifications were fixed.
- Added possibility of non-encrypted channels.
- Received signal strength indicator (RSSI)

### Bluetooth 1.2

Major enhancements include:

- Faster connection and discovery
- *Adaptive frequency-hopping spread spectrum (AFH)*, which improves resistance to radio frequency interference by avoiding the use of crowded frequencies in the hopping sequence
- Higher transmission speeds in practice than in v1.1, up to 721 kbit/s
- Extended Synchronous Connections (eSCO), which improve voice quality of audio links by allowing retransmissions of corrupted packets, and may optionally increase audio latency to provide better concurrent data transfer
- Host Controller Interface (HCI) operation with three-wire UART
- Ratified as IEEE Standard 802.15.1–2005
- Introduced flow control and retransmission modes for L2CAP

### Bluetooth 2.0 + EDR

This version of the Bluetooth Core Specification was released before 2005. The main difference is the introduction of an Enhanced Data Rate (EDR) for faster data transfer. The data rate of EDR is 3 Mbit/s, although the maximum data transfer rate (allowing for inter-packet time and acknowledgements) is 2.1 Mbit/s. EDR uses a combination of GFSK and phase-shift keying modulation (PSK) with two variants, π/4-DQPSK and 8-DPSK. EDR can provide a lower power consumption through a reduced duty cycle.

The specification is published as *Bluetooth v2.0 + EDR*, which implies that EDR is an optional feature. Aside from EDR, the v2.0 specification contains other minor improvements, and products may claim compliance to "Bluetooth v2.0" without supporting the higher data rate. At least one commercial device states "Bluetooth v2.0 without EDR" on its data sheet.

### Bluetooth 2.1 + EDR

Bluetooth Core Specification version 2.1 + EDR was adopted by the Bluetooth SIG on 26 July 2007.

The headline feature of v2.1 is secure simple pairing (SSP): this improves the pairing experience for Bluetooth devices, while increasing the use and strength of security.

Version 2.1 allows various other improvements, including *extended inquiry response* (EIR), which provides more information during the inquiry procedure to allow better filtering of devices before connection; and sniff subrating, which reduces the power consumption in low-power mode.

### Bluetooth 3.0 + HS

Version 3.0 + HS of the Bluetooth Core Specification was adopted by the Bluetooth SIG on 21 April 2009. Bluetooth v3.0 + HS provides theoretical data transfer speeds of up to 24 Mbit/s, though not over the Bluetooth link itself. Instead, the Bluetooth link is used for negotiation and establishment, and the high data rate traffic is carried over a colocated 802.11 link.

The main new feature is AMP (Alternative MAC/PHY), the addition of 802.11 as a high-speed transport. The high-speed part of the specification is not mandatory, and hence only devices that display the "+HS" logo actually support Bluetooth over 802.11 high-speed data transfer. A Bluetooth v3.0 device without the "+HS" suffix is only required to support features introduced in Core Specification version 3.0 or earlier Core Specification Addendum 1.

**L2CAP Enhanced modes**

Enhanced Retransmission Mode (ERTM) implements reliable L2CAP channel, while Streaming Mode (SM) implements unreliable channel with no retransmission or flow control. Introduced in Core Specification Addendum 1.

**Alternative MAC/PHY**

Enables the use of alternative

MAC

and

PHYs

for transporting Bluetooth profile data. The Bluetooth radio is still used for device discovery, initial connection and profile configuration. However, when large quantities of data must be sent, the high-speed alternative MAC PHY 802.11 (typically associated with Wi-Fi) transports the data. This means that Bluetooth uses proven low power connection models when the system is idle, and the faster radio when it must send large quantities of data. AMP links require enhanced L2CAP modes.

**Unicast Connectionless Data**

Permits sending service data without establishing an explicit L2CAP channel. It is intended for use by applications that require low latency between user action and reconnection/transmission of data. This is only appropriate for small amounts of data.

**Enhanced Power Control**

Updates the power control feature to remove the open loop power control, and also to clarify ambiguities in power control introduced by the new modulation schemes added for EDR. Enhanced power control removes the ambiguities by specifying the behavior that is expected. The feature also adds closed loop power control, meaning RSSI filtering can start as the response is received. Additionally, a "go straight to maximum power" request has been introduced. This is expected to deal with the headset link loss issue typically observed when a user puts their phone into a pocket on the opposite side to the headset.

#### Ultra-wideband

The high-speed (AMP) feature of Bluetooth v3.0 was originally intended for UWB, but the WiMedia Alliance, the body responsible for the flavor of UWB intended for Bluetooth, announced in March 2009 that it was disbanding, and ultimately UWB was omitted from the Core v3.0 specification.

On 16 March 2009, the WiMedia Alliance announced it was entering into technology transfer agreements for the WiMedia Ultra-wideband (UWB) specifications. WiMedia has transferred all current and future specifications, including work on future high-speed and power-optimized implementations, to the Bluetooth Special Interest Group (SIG), Wireless USB Promoter Group and the USB Implementers Forum. After successful completion of the technology transfer, marketing, and related administrative items, the WiMedia Alliance ceased operations.

In October 2009, the Bluetooth Special Interest Group suspended development of UWB as part of the alternative MAC/PHY, Bluetooth v3.0 + HS solution. A small, but significant, number of former WiMedia members had not and would not sign up to the necessary agreements for the IP transfer. As of 2009, the Bluetooth SIG was in the process of evaluating other options for its longer-term roadmap.

### Bluetooth 4.0

The Bluetooth SIG completed the Bluetooth Core Specification version 4.0 (called Bluetooth Smart) and has been adopted as of 30 June 2010. It includes *Classic Bluetooth*, *Bluetooth high speed* and *Bluetooth Low Energy* (BLE) protocols. Bluetooth high speed is based on Wi-Fi, and Classic Bluetooth consists of legacy Bluetooth protocols.

Bluetooth Low Energy, previously known as Wibree, is a subset of Bluetooth v4.0 with an entirely new protocol stack for rapid build-up of simple links. As an alternative to the Bluetooth standard protocols that were introduced in Bluetooth v1.0 to v3.0, it is aimed at very low power applications powered by a coin cell. Chip designs allow for two types of implementation, dual-mode, single-mode and enhanced past versions. The provisional names *Wibree* and *Bluetooth ULP* (Ultra Low Power) were abandoned and the BLE name was used for a while. In late 2011, new logos "Bluetooth Smart Ready" for hosts and "Bluetooth Smart" for sensors were introduced as the general-public face of BLE.

Compared to *Classic Bluetooth*, Bluetooth Low Energy is intended to provide considerably reduced power consumption and cost while maintaining a similar communication range. In terms of lengthening the battery life of Bluetooth devices, BLE represents a significant progression.

- In a single-mode implementation, only the low energy protocol stack is implemented. Dialog Semiconductor, STMicroelectronics, AMICCOM, CSR, Nordic Semiconductor and Texas Instruments have released single mode Bluetooth Low Energy solutions.
- In a dual-mode implementation, Bluetooth Smart functionality is integrated into an existing Classic Bluetooth controller. As of March 2011, the following semiconductor companies have announced the availability of chips meeting the standard: Qualcomm Atheros, CSR, Broadcom and Texas Instruments. The compliant architecture shares all of Classic Bluetooth's existing radio and functionality resulting in a negligible cost increase compared to Classic Bluetooth.

Cost-reduced single-mode chips, which enable highly integrated and compact devices, feature a lightweight Link Layer providing ultra-low power idle mode operation, simple device discovery, and reliable point-to-multipoint data transfer with advanced power-save and secure encrypted connections at the lowest possible cost.

General improvements in version 4.0 include the changes necessary to facilitate BLE modes, as well the Generic Attribute Profile (GATT) and Security Manager (SM) services with AES Encryption.

Core Specification Addendum 2 was unveiled in December 2011; it contains improvements to the audio Host Controller Interface and to the High Speed (802.11) Protocol Adaptation Layer.

Core Specification Addendum 3 revision 2 has an adoption date of 24 July 2012.

Core Specification Addendum 4 has an adoption date of 12 February 2013.

### Bluetooth 4.1

The Bluetooth SIG announced formal adoption of the Bluetooth v4.1 specification on 4 December 2013. This specification is an incremental software update to Bluetooth Specification v4.0, and not a hardware update. The update incorporates Bluetooth Core Specification Addenda (CSA 1, 2, 3 & 4) and adds new features that improve consumer usability. These include increased co-existence support for LTE, bulk data exchange rates—and aid developer innovation by allowing devices to support multiple roles simultaneously.

New features of this specification include:

- Mobile wireless service coexistence signaling
- Train nudging and generalized interlaced scanning
- Low Duty Cycle Directed Advertising
- L2CAP connection-oriented and dedicated channels with credit-based flow control
- Dual Mode and Topology
- LE Link Layer Topology
- 802.11n PAL
- Audio architecture updates for Wide Band Speech
- Fast data advertising interval
- Limited discovery time

Some features were already available in a Core Specification Addendum (CSA) before the release of v4.1.

### Bluetooth 4.2

Released on 2 December 2014, it introduces features for the Internet of things.

The major areas of improvement are:

- Bluetooth Low Energy Secure Connection with Data Packet Length Extension to improve the cryptographic protocol
- Link Layer Privacy with Extended Scanner Filter Policies to improve data security
- Internet Protocol Support Profile (IPSP) version 6 ready for Bluetooth smart devices to support the Internet of things and home automation

Older Bluetooth hardware may receive 4.2 features such as Data Packet Length Extension and improved privacy via firmware updates.

### Bluetooth 5.0

The Bluetooth SIG released Bluetooth 5 on 6 December 2016. Its new features are mainly focused on new Internet of Things technology. Sony was the first to announce Bluetooth 5.0 support with its Xperia XZ Premium in Feb 2017 during the Mobile World Congress 2017. The Samsung Galaxy S8 launched with Bluetooth 5 support in April 2017. In September 2017, the iPhone 8, 8 Plus and iPhone X launched with Bluetooth 5 support as well. Apple also integrated Bluetooth 5 in its new HomePod offering released on 9 February 2018. Marketing drops the point number; so that it is just "Bluetooth 5" (unlike Bluetooth 4.0); the change is for the sake of "Simplifying our marketing, communicating user benefits more effectively and making it easier to signal significant technology updates to the market."

Bluetooth 5 provides, for BLE, options that can double the data rate (2 Mbit/s burst) at the expense of range, or provide up to four times the range at the expense of data rate. The increase in transmissions could be important for Internet of Things devices, where many nodes connect throughout a whole house. Bluetooth 5 increases capacity of connectionless services such as location-relevant navigation of low-energy Bluetooth connections.

The major areas of improvement are:

- Slot Availability Mask (SAM)
- 2 Mbit/s PHY for LE
- LE Long Range
- High Duty Cycle Non-Connectable Advertising
- LE Advertising Extensions
- LE Channel Selection Algorithm #2

Features added in CSA5 – integrated in v5.0:

- Higher Output Power

The following features were removed in this version of the specification:

- Park State

### Bluetooth 5.1

The Bluetooth SIG presented Bluetooth 5.1 on 21 January 2019.

The major areas of improvement are:

- Angle of arrival (AoA) and Angle of Departure (AoD) which are used for locating and tracking of devices
- Advertising Channel Index
- GATT caching
- Minor Enhancements batch 1:
  - HCI support for debug keys in LE Secure Connections
  - Sleep clock accuracy update mechanism
  - ADI field in scan response data
  - Interaction between QoS and Flow Specification
  - Block Host channel classification for secondary advertising
  - Allow the SID to appear in scan response reports
  - Specify the behavior when rules are violated
- Periodic Advertising Sync Transfer

Features added in Core Specification Addendum (CSA) 6 – integrated in v5.1:

- Models
- Mesh-based model hierarchy

The following features were removed in this version of the specification:

- Unit keys

### Bluetooth 5.2

On 31 December 2019, the Bluetooth SIG published the Bluetooth Core Specification version 5.2. This version adds the following new features:

- Enhanced Attribute Protocol (EATT), an improved version of the Attribute Protocol (ATT)
- LE Power Control
- LE Isochronous Channels
- LE Audio that is built on top of the new 5.2 features. BT LE Audio was announced in January 2020 at CES by the Bluetooth SIG. Compared to regular Bluetooth Audio, Bluetooth Low Energy Audio makes lower battery consumption possible and creates a standardized way of transmitting audio over BT LE. Bluetooth LE Audio also allows one-to-many and many-to-one transmission, allowing multiple receivers from one source or one receiver for multiple sources, known as Auracast. It uses a new LC3 codec. BLE Audio will also add support for hearing aids. On 12 July 2022, the Bluetooth SIG announced the completion of Bluetooth LE Audio. The standard has a lower minimum latency claim of 20–30 ms vs Bluetooth Classic audio of 100–200 ms. At IFA in August 2023 Samsung announced support for Auracast through a software update for their Galaxy Buds2 Pro and two of their TVs. In October users started getting updates for the earbuds.

### Bluetooth 5.3

The Bluetooth SIG published the Bluetooth Core Specification version 5.3 on 13 July 2021. This version adds the following new features:

- Connection Subrating
- Periodic Advertisement Interval
- Channel Classification Enhancement
- Encryption key size control enhancements

The following features were removed in this version of the specification:

- Alternate MAC and PHY (AMP) Extension

### Bluetooth 5.4

The Bluetooth SIG released the Bluetooth Core Specification version 5.4 on 7 February 2023. This version adds the following new features:

- Periodic Advertising with Responses (PAwR)
- Encrypted Advertising Data
- LE GATT Security Levels Characteristic
- Advertising Coding Selection

### Bluetooth 6.0

The Bluetooth SIG released the Bluetooth Core Specification version 6.0 on 27 August 2024. This version adds the following new features:

- Bluetooth Channel Sounding
- Decision-based advertising filtering
- Monitoring advertisers
- ISOAL enhancement
- LL extended feature set
- Frame space update

### Bluetooth 6.1

The Bluetooth SIG released the Bluetooth Core Specification version 6.1 on 7 May 2025. This version adds the following new features:

- Increased device privacy
- Improved power efficiency

### Bluetooth 6.2

The Bluetooth SIG released the Bluetooth Core Specification version 6.2 on 3 November 2025. This version adds the following new features:

- HCI USB LE Isochronous support
- LE Direct Test Mode enhancements
- Shorter connection intervals
- Channel Sounding amplitude-based attack resilience
