---
title: "Fibre Channel"
source: https://en.wikipedia.org/wiki/Fibre_Channel
domain: infiniband
license: CC-BY-SA-4.0
tags: infiniband fabric, high performance interconnect, hpc networking, channel adapter
fetched: 2026-07-02
---

# Fibre Channel

**Fibre Channel** (**FC**) is a high-speed data transfer protocol providing in-order, lossless delivery of raw block data. Fibre Channel is primarily used to connect computer data storage to servers in storage area networks (SAN) in commercial data centers.

Fibre Channel networks form a switched fabric because the switches in a network operate in unison as one big switch. Fibre Channel typically runs on optical fiber cables within and between data centers, but can also run on copper cabling. Supported data rates include 1, 2, 4, 8, 16, 32, 64, and 128 gigabit per second resulting from improvements in successive technology generations. The industry now notates this as Gigabit Fibre Channel (GFC).

There are various upper-level protocols for Fibre Channel, including two for block storage. Fibre Channel Protocol (FCP) is a protocol that transports SCSI commands over Fibre Channel networks. FICON is a protocol that transports ESCON commands, used by IBM mainframe computers, over Fibre Channel. Fibre Channel can be used to transport data from storage systems that use solid-state flash memory storage medium by transporting NVMe protocol commands.

## Etymology

When the technology was originally devised, it ran over optical fiber cables only and, as such, was called "Fiber Channel". Later, the ability to run over copper cabling was added to the specification. In order to avoid confusion and to create a unique name, the industry decided to change the spelling and use the British English *fibre* for the name of the standard.

## History

Fibre Channel is standardized in the T11 Technical Committee of the International Committee for Information Technology Standards (INCITS), an American National Standards Institute (ANSI)-accredited standards committee. Fibre Channel started in 1988, with ANSI standard approval in 1994, to merge the benefits of multiple physical layer implementations, including SCSI, HIPPI and ESCON.

Fibre Channel was designed as a serial interface to overcome limitations of the SCSI and HIPPI physical-layer parallel-signal copper wire interfaces. Such interfaces face the challenge of, among other things, maintaining signal timing coherence across all the data-signal wires (8, 16 and finally 32 for SCSI, 50 for HIPPI) so that a receiver can determine when all the electrical signal values are "good" (stable and valid for simultaneous reception sampling). This challenge becomes evermore difficult in a mass-manufactured technology as data signal frequencies increase, with part of the technical compensation being ever reducing the supported connecting copper-parallel cable length. See Parallel SCSI. FC was developed with leading-edge multi-mode optical fiber technologies that overcame the speed limitations of the ESCON protocol. By appealing to the large base of SCSI disk drives and leveraging mainframe technologies, Fibre Channel developed economies of scale for advanced technologies and deployments became economical and widespread.

Commercial products were released while the standard was still in draft. By the time the standard was ratified, lower speed versions were already growing out of use. Fibre Channel was the first serial storage transport to achieve gigabit speeds where it saw wide adoption, and its success grew with each successive speed. Fibre Channel has doubled in speed every few years since 1996.

In addition to a modern physical layer, Fibre Channel also added support for any number of "upper layer" protocols, including ATM, IP (IPFC) and FICON, with SCSI (FCP) being the predominant usage.

Fibre Channel has seen active development since its inception, with numerous speed improvements on a variety of underlying transport media. The following tables show the progression of native Fibre Channel speeds:

| Name | Line-rate (gigabaud) | Line coding | Nominal throughput per direction (MB/s) | T11 Spec (Year) | Market availability |   |
|---|---|---|---|---|---|---|
| 133 Mbit/s | 0.1328125 | ? | 8b10b | 12.5 | — | 1993 |
| 266 Mbit/s | 0.265625 | 25 | 1994 |   |   |   |
| 533 Mbit/s | 0.53125 | 50 | ? |   |   |   |
| 1GFC (Gen 1) | 1.0625 | NRZ | 100 | 1996 | 1997 |   |
| 2GFC (Gen 2) | 2.125 | 200 | 2000 | 2001 |   |   |
| 4GFC (Gen 3) | 4.25 | 400 | 2003 | 2005 |   |   |
| 8GFC (Gen 4) | 8.5 | 800 | 2006 | 2008 |   |   |
| 16GFC (Gen 5) | 14.025 | 64b66b | 1,600 | 2009 | 2011 |   |
| 32GFC (Gen 6) | 28.05 | 256b257b | 3,200 | 2013 | 2016 |   |
| 64GFC (Gen 7) | 28.9 | PAM-4 | 6,400 | 2017 | 2020 |   |
| 128GFC (Gen 8) | 56.1 | 12,425 | 2022 | 2026 |   |   |
| 256GFC (Gen 9) | 112.2 | 24,850 | TBA | TBA |   |   |

FC used throughout all applications for Fibre Channel infrastructure and devices, including edge and ISL interconnects. Each speed maintains backward compatibility at least two previous generations (I.e., 32GFC backward compatible to 16GFC and 8GFC)

| Name | Line-rate (gigabaud) | Line coding | Nominal throughput per direction (MB/s) | T11 Spec (Year) | Market availability |   |
|---|---|---|---|---|---|---|
| 10GFC | 10.51875 | NRZ | 64b66b | 1,200 | 2003 | 2009 |
| 128GFC (Gen 6) | 4 × 28.05 | 256b257b | 12,800 | 2014 | 2016 |   |
| 256GFC (Gen 7) | 4 × 28.9 | PAM-4 | 25,600 | 2018 | 2020 |   |

Inter-Switch Links, ISLs, are usually multi-lane interconnects used for non-edge, core connections, and other high-speed applications demanding maximum bandwidth. ISLs utilize high bit-rates to accommodate the funneling of edge connections. Some ISL solutions are vendor-proprietary.

## Characteristics

Two major characteristics of Fibre Channel networks are in-order delivery and lossless delivery of raw block data. Lossless delivery of raw data block is achieved based on a credit mechanism.

## Topologies

There are three major Fibre Channel topologies, describing how a number of ports are connected together. A *port* in Fibre Channel terminology is any entity that actively communicates over the network, not necessarily a hardware port. This port is usually implemented in a device such as disk storage, a Host Bus Adapter (HBA) network connection on a server or a Fibre Channel switch.

- **Point-to-point** (see *FC-FS-3*). Two devices are connected directly to each other using Node ports. This is the simplest topology, with limited connectivity. The bandwidth is dedicated.
- **Arbitrated loop** (see *FC-AL-2*). In this design, all devices are in a loop or ring, similar to Token Ring networking. Adding or removing a device from the loop causes all activity on the loop to be interrupted. The failure of one device causes a break in the ring. Fibre Channel hubs exist to connect multiple devices together and may bypass failed ports. A loop may also be made by cabling each port to the next in a ring.
  - A minimal loop containing only two ports, while appearing to be similar to point-to-point, differs considerably in terms of the protocol.
  - Only one pair of ports can communicate concurrently on a loop.
  - Maximum speed of 8GFC.
  - Arbitrated Loop has been rarely used after 2010 and its support is being discontinued for new gen switches.
- **Switched Fabric** (see *FC-SW-6*). In this design, all devices are connected to Fibre Channel switches, similar conceptually to modern Ethernet implementations. Advantages of this topology over point-to-point or Arbitrated Loop include:
  - The Fabric can scale to tens of thousands of ports.
  - The switches manage the state of the Fabric, providing optimized paths via Fabric Shortest Path First (FSPF) data routing protocol.
  - The traffic between two ports flows through the switches and not through any other ports like in Arbitrated Loop.
  - Failure of a port is isolated to a link and should not affect operation of other ports.
  - Multiple pairs of ports may communicate simultaneously in a Fabric.

| Attribute | Point-to-point | Arbitrated loop | Switched fabric |
|---|---|---|---|
| Max ports | 2 | 127 | ~16777216 (224) |
| Address size | —N/a | 8-bit ALPA | 24-bit port ID |
| Side effect of port failure | Link fails | Loop fails (until port bypassed) | —N/a |
| Access to medium | Dedicated | Arbitrated | Dedicated |

## Layers

Fibre Channel does not follow the OSI model layering, and is split into five layers:

- **FC-4** – Protocol-mapping layer, in which upper-level protocols such as NVM Express (NVMe), SCSI, IP, and FICON are encapsulated into Information Units (IUs) for delivery to FC-2. Current FC-4s include FCP-4, FC-SB-5, and FC-NVMe.
- **FC-3** – Common services layer, a thin layer that could eventually implement functions like encryption or RAID redundancy algorithms; multiport connections;
- **FC-2** – Signaling Protocol, defined by the *Fibre Channel Framing and Signaling* standard, consists of the low level Fibre Channel network protocols; port to port connections;
- **FC-1** – Transmission Protocol, which implements line coding of signals;
- **FC-0** – physical layer, defined by *Fibre Channel Physical Interfaces* standard, includes cabling, connectors etc.;

Fibre Channel products are available at 1, 2, 4, 8, 10, 16, 32, 64 and 128 Gbit/s; these protocol flavors are called accordingly 1GFC, 2GFC, 4GFC, 8GFC, 10GFC, 16GFC, 32GFC, 64GFC or 128GFC. The 32GFC standard was approved by the INCITS T11 committee in 2013, and those products became available in 2016. The 1GFC, 2GFC, 4GFC, 8GFC designs all use 8b/10b encoding, while the 10GFC and 16GFC standard uses 64b/66b encoding. Unlike the 10GFC standards, 16GFC provides backward compatibility with 4GFC and 8GFC since it provides exactly twice the throughput of 8GFC or four times that of 4GFC.

## Ports

Fibre Channel ports come in a variety of logical configurations. The most common types of ports are:

- **N_Port (Node port)** An N_Port is typically an HBA port that connects to a switch's F_Port or another N_Port. Nx_Port communicating through a PN_Port that is not operating a Loop Port State Machine.
- **F_Port (Fabric port)** An F_Port is a switch port that is connected to an N_Port.
- **E_Port (Expansion port)** Switch port that attaches to another E_Port to create an Inter-Switch Link.

Fibre Channel Loop protocols create multiple types of Loop Ports:

- **L_Port (Loop port)** FC_Port that contains Arbitrated Loop functions associated with the Arbitrated Loop topology.
- **FL_Port (Fabric Loop port)** L_Port that is able to perform the function of an F_Port, attached via a link to one or more NL_Ports in an Arbitrated Loop topology.
- **NL_Port (Node Loop port)** PN_Port that is operating a Loop port state machine.

If a port can support loop and non-loop functionality, the port is known as:

- **Fx_Port** switch port capable of operating as an F_Port or FL_Port.
- **Nx_Port** end point for Fibre Channel frame communication, having a distinct address identifier and Name_Identifier, providing an independent set of FC-2V functions to higher levels, and having the ability to act as an Originator, a Responder, or both.

Ports have virtual components and physical components and are described as:

- **PN_Port** entity that includes a Link_Control_Facility and one or more Nx_Ports.
- **VF_Port (Virtual F_Port)** instance of the FC-2V sublevel that connects to one or more VN_Ports.
- **VN_Port (Virtual N_Port)** instance of the FC-2V sublevel. VN_Port is used when it is desired to emphasize support for multiple Nx_Ports on a single Multiplexer (e.g., via a single PN_Port).
- **VE_Port (Virtual E_Port)** instance of the FC-2V sublevel that connects to another VE_Port or to a B_Port to create an Inter-Switch Link.

The following types of ports are also used in Fibre Channel:

- **A_Port (Adjacent port)** combination of one PA_Port and one VA_Port operating together.
- **B_Port (Bridge Port)** Fabric inter-element port used to connect bridge devices with E_Ports on a Switch.
- **D_Port (Diagnostic Port)** A configured port used to perform diagnostic tests on a link with another D_Port.
- **EX_Port** A type of E_Port used to connect to an FC router fabric.
- **G_Port (Generic Fabric port)** Switch port that may function either as an E_Port, A_Port, or as an F_Port.
- **GL_Port (Generic Fabric Loop port)** Switch port that may function either as an E_Port, A_Port, or as an Fx_Port.
- **PE_Port** LCF within the Fabric that attaches to another PE_Port or to a B_Port through a link.
- **PF_Port** LCF within a Fabric that attaches to a PN_Port through a link.
- **TE_Port (Trunking E_Port) A trunking expansion port that** expands the functionality of E ports to support VSAN trunking, Transport quality of service (QoS) parameters, and Fibre Channel trace (fctrace) feature.
- **U_Port** **(Universal port)** A port waiting to become another port type
- **VA_Port (Virtual A_Port)** instance of the FC-2V sublevel of Fibre Channel that connects to another VA_Port.
- **VEX_Port** VEX_Ports are no different from EX_Ports, except underlying transport is IP rather than FC.

## Media and modules

The Fibre Channel physical layer is based on serial connections that use fiber optics to copper between corresponding pluggable modules. The modules may have a single lane, dual lanes or quad lanes that correspond to the SFP, SFP-DD and QSFP form factors. Fibre Channel does not use 8- or 16-lane modules (like CFP8, QSFP-DD, or COBO used in 400GbE) and there are no plans to use these expensive and complex modules.

The Small Form-factor Pluggable (SFP) module and its enhanced version SFP+, SFP28 and SFP56 are common form factors for Fibre Channel ports. SFP modules support a variety of distances via multi-mode and single-mode optical fiber as shown in the table below. SFP modules use duplex fiber cabling with LC connectors.

SFP-DD modules are used for high-density applications that need to double the throughput of an SFP Port. SFP-DD is defined by the SFP-DD MSA and enables breakout to two SFP ports. Two rows of electrical contacts enable doubling the throughput of SFP modules in a similar fashion as QSFP-DD.

The Quad Small Form-factor Pluggable (QSFP) module began being used for switch inter-connectivity and was later adopted for use in 4-lane implementations of Gen-6 Fibre Channel supporting 128GFC. QSFP uses either LC connectors for 128GFC-CWDM4 or MPO connectors for 128GFC-SW4 or 128GFC-PSM4. MPO cabling uses 8- or 12-fiber cabling infrastructure that connects to another 128GFC port or may be broken out into four duplex LC connections to 32GFC SFP+ ports. Fibre Channel switches use either SFP or QSFP modules.

| Fiber type | Speed (MB/s) | Transmitter | Medium variant | Distance |
|---|---|---|---|---|
| Single-mode fiber (SMF) | 12,800 | 1,310 nm longwave light | 128GFC-PSM4 | 0.5m - 0.5 km |
| 1,270, 1,290, 1,310 and 1,330 nm longwave light | 128GFC-CWDM4 | 0.5 m – 2 km |   |   |
| 6,400 | 1,310 nm longwave light | 64GFC-LW | 0.5m - 10 km |   |
| 3,200 | 1,310 nm longwave light | 3200-SM-LC-L | 0.5 m - 10 km |   |
| 1,600 | 1,310 nm longwave light | 1600-SM-LC-L | 0.5 m – 10 km |   |
| 1,490 nm longwave light | 1600-SM-LZ-I | 0.5 m – 2 km |   |   |
| 800 | 1,310 nm longwave light | 800-SM-LC-L | 2 m – 10 km |   |
| 800-SM-LC-I | 2 m – 1.4 km |   |   |   |
| 400 | 1,310 nm longwave light | 400-SM-LC-L | 2 m – 10 km |   |
| 400-SM-LC-M | 2 m – 4 km |   |   |   |
| 400-SM-LL-I | 2 m – 2 km |   |   |   |
| 200 | 1,550 nm longwave light | 200-SM-LL-V | 2 m – 50 km |   |
| 1,310 nm longwave light | 200-SM-LC-L | 2 m – 10 km |   |   |
| 200-SM-LL-I | 2 m – 2 km |   |   |   |
| 100 | 1,550 nm longwave light | 100-SM-LL-V | 2 m – 50 km |   |
| 1,310 nm longwave light | 100-SM-LL-L 100-SM-LC-L | 2 m – 10 km |   |   |
| 100-SM-LL-I | 2 m – 2 km |   |   |   |
| Multi-mode fiber (MMF) | 12,800 | 850 nm shortwave light | 128GFC-SW4 | 0–100 m |
| 6,400 | 64GFC-SW | 0–100 m |   |   |
| 3,200 | 3200-SN | 0–100 m |   |   |
| 1,600 | 1600-M5F-SN-I | 0.5–125 m |   |   |
| 1600-M5E-SN-I | 0.5–100 m |   |   |   |
| 1600-M5-SN-S | 0.5–35 m |   |   |   |
| 1600-M6-SN-S | 0.5–15 m |   |   |   |
| 800 | 800-M5F-SN-I | 0.5–190 m |   |   |
| 800-M5E-SN-I | 0.5–150 m |   |   |   |
| 800-M5-SN-S | 0.5–50 m |   |   |   |
| 800-M6-SN-S | 0.5–21 m |   |   |   |
| 400 | 400-M5F-SN-I | 0.5–400 m |   |   |
| 400-M5E-SN-I | 0.5–380 m |   |   |   |
| 400-M5-SN-I | 0.5–150 m |   |   |   |
| 400-M6-SN-I | 0.5–70 m |   |   |   |
| 200 | 200-M5E-SN-I | 0.5–500 m |   |   |
| 200-M5-SN-I | 0.5–300 m |   |   |   |
| 200-M6-SN-I | 0.5–150 m |   |   |   |
| 100 | 100-M5E-SN-I | 0.5–860 m |   |   |
| 100-M5-SN-I | 0.5–500 m |   |   |   |
| 100-M6-SN-I | 0.5–300 m |   |   |   |
| 100-M5-SL-I | 2–500 m |   |   |   |
| 100-M6-SL-I | 2–175 m |   |   |   |

| Multi-mode fiber | Fiber diameter | FC media designation |
|---|---|---|
| OM1 | 62.5 μm | M6 |
| OM2 | 50 μm | M5 |
| OM3 | 50 μm | M5E |
| OM4 | 50 μm | M5F |
| OM5 | 50 μm | N/A |

Modern Fibre Channel devices support SFP+ transceivers, mainly with LC (Lucent Connector) fiber connector. Older 1GFC devices used GBIC transceivers, mainly with SC (Subscriber Connector) fiber connectors.

## Storage area networks

The goal of Fibre Channel is to create a storage area network (SAN) to connect servers to storage.

The SAN is a dedicated network that enables multiple servers to access data from one or more storage devices. Enterprise storage uses the SAN to backup to secondary storage devices, including disk arrays, tape libraries, and other backup, while the storage is still accessible to the server. Servers may access storage from multiple storage devices over the network as well.

SANs are often designed with dual fabrics to increase fault tolerance. Two completely separate fabrics are operational and if the primary fabric fails, then the second fabric becomes the primary.

## Switches

Fibre Channel switches can be divided into two classes. These classes are not part of the standard, and the classification of every switch is a marketing decision of the manufacturer:

- **Directors** offer a high port-count in a modular (slot-based) chassis with no single point of failure (high availability).
- **Switches** are typically smaller, fixed-configuration (sometimes semi-modular), less redundant devices.

A fabric consisting entirely of one vendor's products is considered to be *homogeneous*. This is often referred to as operating in its "native mode" and allows the vendor to add proprietary features that may not be compliant with the Fibre Channel standard.

If multiple switch vendors are used within the same fabric, it is *heterogeneous*, the switches may only achieve adjacency if all switches are placed into their interoperability modes. This is called the *open fabric* mode, as each vendor's switch may have to disable its proprietary features to comply with the Fibre Channel standard.

Some switch manufacturers offer a variety of interoperability modes above and beyond the "native" and "open fabric" states. These "native interoperability" modes allow switches to operate in the native mode of another vendor and still maintain some of the proprietary behaviors of both. However, running in native interoperability mode may still disable some proprietary features and can produce fabrics of questionable stability.

## Host bus adapters

Fibre Channel HBAs, as well as CNAs, are available for all major open systems, computer architectures, and buses, including PCI and SBus. HBAs connect servers to the Fibre Channel network and are part of a class of devices known as translation devices. Some are OS dependent. Each HBA has a unique World Wide Name (WWN), which is similar to an Ethernet MAC address in that it uses an Organizationally Unique Identifier (OUI) assigned by the IEEE. However, WWNs are longer (8 bytes). There are two types of WWNs on an HBA; a World Wide Node Name (WWNN), which can be shared by some or all ports of a device, and a World Wide Port Name (WWPN), which is necessarily unique to each port. Adapters or routers can connect Fibre Channel networks to IP or Ethernet networks.
