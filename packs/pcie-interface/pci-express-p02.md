---
title: "PCI Express (part 2/2)"
source: https://en.wikipedia.org/wiki/PCI_Express
domain: pcie-interface
license: CC-BY-SA-4.0
tags: pci express, pcie root complex, message signaled interrupts, serial expansion bus
fetched: 2026-07-02
part: 2/2
---

## Hardware protocol summary

The PCIe link is built around dedicated unidirectional couples of serial (1-bit), point-to-point connections known as *lanes*. This is in sharp contrast to the earlier PCI connection, which is a bus-based system where all the devices share the same bidirectional, 32-bit or 64-bit parallel bus.

PCI Express is a layered protocol, consisting of a *transaction layer*, a *data link layer*, and a *physical layer*. The Data Link Layer is subdivided to include a media access control (MAC) sublayer. The Physical Layer is subdivided into logical and electrical sublayers. The Physical logical-sublayer contains a physical coding sublayer (PCS). The terms are borrowed from the IEEE 802 networking protocol model.

### Physical layer

| Lanes | Pins | Length in mm (in) |   |   |   |   |
|---|---|---|---|---|---|---|
| Board connector | Connector slot |   |   |   |   |   |
| Total | Variable | Total | Variable | Total | Variable |   |
| ×1 | 2×18=36 | 2×7=14 | 20.3 (0.8) | 7.2 (0.28) | 25 (1.0) | 7.65 (0.30) |
| ×4 | 2×32=64 | 2×21=42 | 34.3 (1.4) | 21.2 (0.8) | 39 (1.5) | 21.65 (0.85) |
| ×8 | 2×49=98 | 2×38=76 | 51.3 (2.0) | 38.2 (1.5) | 56 (2.2) | 38.65 (1.52) |
| ×16 | 2×82=164 | 2×71=142 | 84.3 (3.3) | 71.2 (2.8) | 89 (3.5) | 71.65 (2.82) |

The PCIe Physical Layer (*PHY*, *PCIEPHY*, *PCI Express PHY*, or *PCIe PHY*) specification is divided into two sub-layers, corresponding to electrical and logical specifications. The logical sublayer is sometimes further divided into a MAC sublayer and a PCS, although this division is not formally part of the PCIe specification. A specification published by Intel, the PHY Interface for PCI Express (PIPE), defines the MAC/PCS functional partitioning and the interface between these two sub-layers. The PIPE specification also identifies the *physical media attachment* (PMA) layer, which includes the SerDes (serializer/deserializer) and other analog circuitry; however, since SerDes implementations vary greatly among ASIC vendors, PIPE does not specify an interface between the PCS and PMA.

At the electrical level, each lane consists of two unidirectional differential pairs operating at 2.5, 5, 8, 16 or 32 Gbit/s, depending on the negotiated capabilities. Transmit and receive are separate differential pairs, for a total of four data wires per lane.

A connection between any two PCIe devices is known as a *link*, and is built up from a collection of one or more *lanes*. All devices must minimally support single-lane (×1) link. Devices may optionally support wider links composed of up to 32 lanes. This allows for very good compatibility in two ways:

- A PCIe card physically fits (and works correctly) in any slot that is at least as large as it is (e.g., a ×1 sized card works in any sized slot);
- A slot of a large physical size (e.g., ×16) can be wired electrically with fewer lanes (e.g., ×1, ×4, ×8, or ×12) as long as it provides the ground connections required by the larger physical slot size.

In both cases, PCIe negotiates the highest mutually supported number of lanes. Many graphics cards, motherboards and BIOS versions are verified to support ×1, ×4, ×8 and ×16 connectivity on the same connection.

The width of a PCIe connector is 8.8 mm, while the height is 11.25 mm, and the length is variable. The fixed section of the connector is 11.65 mm in length and contains two rows of 11 pins each (22 pins total), while the length of the other section is variable depending on the number of lanes. The pins are spaced at 1 mm intervals, and the thickness of the card going into the connector is 1.6 mm.

#### Data transmission

PCIe sends all control messages, including interrupts, over the same links used for data. The serial protocol can never be blocked, so latency is still comparable to conventional PCI, which has dedicated interrupt lines. When the problem of IRQ sharing of pin based interrupts is taken into account and the fact that message signaled interrupts (MSI) can bypass an I/O APIC and be delivered to the CPU directly, MSI performance ends up being substantially better.

Data transmitted on multiple-lane links is interleaved, meaning that each successive byte is sent down successive lanes. The PCIe specification refers to this interleaving as *data striping*. While requiring significant hardware complexity to synchronize (or deskew) the incoming striped data, striping can significantly reduce the latency of the *n*th byte on a link. While the lanes are not tightly synchronized, there is a limit to the *lane to lane skew* of 20/8/6 ns for 2.5/5/8 GT/s so the hardware buffers can re-align the striped data. Due to padding requirements, striping may not necessarily reduce the latency of small data packets on a link.

As with other high data rate serial transmission protocols, the clock is embedded in the signal. At the physical level, PCI Express 2.0 utilizes the 8b/10b encoding scheme (line code) to ensure that strings of consecutive identical digits (zeros or ones) are limited in length. This coding was used to prevent the receiver from losing track of where the bit edges are. In this coding scheme every eight (uncoded) payload bits of data are replaced with 10 (encoded) bits of transmit data, causing a 20% overhead in the electrical bandwidth. To improve the available bandwidth, PCI Express version 3.0 instead uses 128b/130b encoding (1.54% overhead). Line encoding limits the run length of identical-digit strings in data streams and ensures the receiver stays synchronised to the transmitter via clock recovery.

A desirable balance (and therefore spectral density) of 0 and 1 bits in the data stream is achieved by XORing a known binary polynomial as a "scrambler" to the data stream in a feedback topology. Because the scrambling polynomial is known, the data can be recovered by applying the XOR a second time. Both the scrambling and descrambling steps are carried out in hardware.

Dual simplex in PCIe means there are two simplex channels on every PCIe lane. Simplex means communication is only possible in one direction. By having two simplex channels, two-way communication is made possible. One differential pair is used for each channel.

### Data link layer

The data link layer performs three vital services for the PCIe link:

1. sequence the transaction layer packets (TLPs) that are generated by the transaction layer,
2. ensure reliable delivery of TLPs between two endpoints via an acknowledgement protocol (ACK and NAK signaling) that explicitly requires replay of unacknowledged/bad TLPs,
3. initialize and manage flow control credits

On the transmit side, the data link layer generates an incrementing sequence number for each outgoing TLP. It serves as a unique identification tag for each transmitted TLP, and is inserted into the header of the outgoing TLP. A 32-bit cyclic redundancy check code (known in this context as Link CRC or LCRC) is also appended to the end of each outgoing TLP.

On the receive side, the received TLP's LCRC and sequence number are both validated in the link layer. If either the LCRC check fails (indicating a data error), or the sequence-number is out of range (non-consecutive from the last valid received TLP), then the bad TLP, as well as any TLPs received after the bad TLP, are considered invalid and discarded. The receiver sends a negative acknowledgement message (NAK) with the sequence-number of the invalid TLP, requesting re-transmission of all TLPs forward of that sequence-number. If the received TLP passes the LCRC check and has the correct sequence number, it is treated as valid. The link receiver increments the sequence-number (which tracks the last received good TLP), and forwards the valid TLP to the receiver's transaction layer. An ACK message is sent to remote transmitter, indicating the TLP was successfully received (and by extension, all TLPs with past sequence-numbers.)

If the transmitter receives a NAK message, or no acknowledgement (NAK or ACK) is received until a timeout period expires, the transmitter must retransmit all TLPs that lack a positive acknowledgement (ACK). Barring a persistent malfunction of the device or transmission medium, the link-layer presents a reliable connection to the transaction layer, since the transmission protocol ensures delivery of TLPs over an unreliable medium.

In addition to sending and receiving TLPs generated by the transaction layer, the data-link layer also generates and consumes data link layer packets (DLLPs). ACK and NAK signals are communicated via DLLPs, as are some power management messages and flow control credit information (on behalf of the transaction layer).

In practice, the number of in-flight, unacknowledged TLPs on the link is limited by two factors: the size of the transmitter's replay buffer (which must store a copy of all transmitted TLPs until the remote receiver ACKs them), and the flow control credits issued by the receiver to a transmitter. PCI Express requires all receivers to issue a minimum number of credits, to guarantee a link allows sending PCIConfig TLPs and message TLPs.

### Transaction layer

PCI Express implements split transactions (transactions with request and response separated by time), allowing the link to carry other traffic while the target device gathers data for the response.

PCI Express uses credit-based flow control. In this scheme, a device advertises an initial amount of credit for each received buffer in its transaction layer. The device at the opposite end of the link, when sending transactions to this device, counts the number of credits each TLP consumes from its account. The sending device may only transmit a TLP when doing so does not make its consumed credit count exceed its credit limit. When the receiving device finishes processing the TLP from its buffer, it signals a return of credits to the sending device, which increases the credit limit by the restored amount. The credit counters are modular counters, and the comparison of consumed credits to credit limit requires modular arithmetic. The advantage of this scheme (compared to other methods such as wait states or handshake-based transfer protocols) is that the latency of credit return does not affect performance, provided that the credit limit is not encountered. This assumption is generally met if each device is designed with adequate buffer sizes.

PCIe 1.x is often quoted to support a data rate of 250 MB/s in each direction, per lane. This figure is a calculation from the physical signaling rate (2.5 gigabaud) divided by the encoding overhead (10 bits per byte). This means a sixteen lane (×16) PCIe card would then be theoretically capable of 16×250 MB/s = 4 GB/s in each direction. While this is correct in terms of data bytes, more meaningful calculations are based on the usable data payload rate, which depends on the profile of the traffic, which is a function of the high-level (software) application and intermediate protocol levels.

Like other high data rate serial interconnect systems, PCIe has a protocol and processing overhead due to the additional transfer robustness (CRC and acknowledgements). Long continuous unidirectional transfers (such as those typical in high-performance storage controllers) can approach >95% of PCIe's raw (lane) data rate. These transfers also benefit the most from increased number of lanes (×2, ×4, etc.) But in more typical applications (such as a USB or Ethernet controller), the traffic profile is characterized as short data packets with frequent enforced acknowledgements. This type of traffic reduces the efficiency of the link, due to overhead from packet parsing and forced interrupts (either in the device's host interface or the PC's CPU). Being a protocol for devices connected to the same printed circuit board, it does not require the same tolerance for transmission errors as a protocol for communication over longer distances, and thus, this loss of efficiency is not particular to PCIe.

### Efficiency of the link

As for any network-like communication links, some of the raw bandwidth is consumed by protocol overhead:

A PCIe 1.x lane for example offers a data rate on top of the physical layer of 250 MB/s (simplex). This is due to a 2.5 GT/s bit rate multiplied by the efficiency of the 8b/10b line code (see #Comparison table). This is not the payload bandwidth but the physical layer bandwidth – a PCIe lane has to carry additional information for full functionality.

| Layer | PHY | Data Link Layer | Transaction | Data Link Layer | PHY |   |   |
|---|---|---|---|---|---|---|---|
| Data | Start | Sequence | Header | Payload | ECRC | LCRC | End |
| Size (Bytes) | 1 | 2 | 12 or 16 | 0 to 4096 | 4 (optional) | 4 | 1 |

The Gen2 overhead is then 20, 24, or 28 bytes per transaction.

| Layer | PHY | Data Link Layer | Transaction Layer | Data Link Layer |   |   |
|---|---|---|---|---|---|---|
| Data | Start | Sequence | Header | Payload | ECRC | LCRC |
| Size (Bytes) | 4 | 2 | 12 or 16 | 0 to 4096 | 4 (optional) | 4 |

The Gen3 overhead is then 22, 26 or 30 bytes per transaction.

The Packet Efficiency = ⁠Payload/Payload + Overhead⁠ for a 128 byte payload is 86%, and 98% for a 1024 byte payload. For small accesses like register settings (4 bytes), the efficiency drops as low as 16%. That said, most PCIe config registers reside in a DMA region mapped to the CPU's control registers and require no bus access.

The maximum payload size (MPS) is set on all devices based on smallest maximum on any device in the chain. If one device has an MPS of 128 bytes, *all* devices of the tree must set their MPS to 128 bytes. In this case the bus will have a maximum efficiency of 86% for writes.


## Applications

PCI Express operates in consumer, server, and industrial applications, as a motherboard-level interconnect (to link motherboard-mounted peripherals), a passive backplane interconnect and as an expansion card interface for add-in boards.

In virtually all modern (as of 2012) PCs, from consumer laptops and desktops to enterprise servers, the PCIe bus serves as the primary motherboard-level interconnect, connecting the host system-processor with both integrated peripherals (surface-mounted ICs) and add-on peripherals (expansion cards). In some of these systems, the PCIe bus co-exists with one or more legacy PCI buses, for backward compatibility with the large body of legacy PCI peripherals.

As of 2013, PCI Express has replaced AGP as the default interface for graphics cards on new systems. Almost all models of graphics cards released since 2010 by AMD (ATI) and Nvidia use PCI Express. AMD, Nvidia, and Intel have released motherboard chipsets that support as many as four PCIe ×16 slots, allowing tri-GPU and quad-GPU card configurations.

### External GPUs

Theoretically, external PCIe could give a notebook the graphics power of a desktop, by connecting a notebook with any PCIe desktop video card (enclosed in its own external housing, with a power supply and cooling); this is possible with an ExpressCard or Thunderbolt interface. An ExpressCard interface provides bit rates of 5 Gbit/s (0.5 GB/s throughput), whereas a Thunderbolt interface provides bit rates of up to 40 Gbit/s (5 GB/s throughput).

In 2006, Nvidia developed the Quadro Plex external PCIe family of GPUs that can be used for advanced graphic applications for the professional market. These video cards require a PCI Express ×8 or ×16 slot for the host-side card, which connects to the Plex via a VHDCI carrying eight PCIe lanes.

In 2008, AMD announced the ATI XGP technology, based on a proprietary cabling system that is compatible with PCIe ×8 signal transmissions. This connector is available on the Fujitsu Amilo and the Acer Ferrari One notebooks. Fujitsu launched their AMILO GraphicBooster enclosure for XGP soon thereafter. Around 2010 Acer launched the Dynavivid graphics dock for XGP.

In 2010, external card hubs were introduced that can connect to a laptop or desktop through a PCI ExpressCard slot. These hubs can accept full-sized graphics cards. Examples include MSI GUS, Village Instrument's ViDock, the Asus XG Station, Bplus PE4H V3.2 adapter, as well as more improvised DIY devices. However such solutions are limited by the size (often only ×1) and version of the available PCIe slot on a laptop.

The Intel Thunderbolt interface has provided a new option to connect with a PCIe card externally. Magma has released the ExpressBox 3T, which can hold up to three PCIe cards (two at ×8 and one at ×4). MSI also released the Thunderbolt GUS II, a PCIe chassis dedicated for video cards. Other products such as the Sonnet's Echo Express and mLogic's mLink are Thunderbolt PCIe chassis in a smaller form factor.

In 2017, more fully featured external card hubs were introduced, such as the Razer Core, which has a full-length PCIe ×16 interface.

### Storage devices

The PCI Express protocol can be used as data interface to flash memory devices, such as memory cards and solid-state drives (SSDs).

The XQD card is a memory card format utilizing PCI Express, developed by the CompactFlash Association, with transfer rates of up to 1 GB/s.

Many high-performance, enterprise-class SSDs are designed as PCI Express RAID controller cards. Before NVMe was standardized, many of these cards utilized proprietary interfaces and custom drivers to communicate with the operating system; they had much higher transfer rates (over 1 GB/s) and IOPS (over one million I/O operations per second) when compared to Serial ATA or SAS drives. For example, in 2011 OCZ and Marvell co-developed a native PCI Express solid-state drive controller for a PCI Express 3.0 ×16 slot with maximum capacity of 12 TB and a performance of to 7.2 GB/s sequential transfers and up to 2.52 million IOPS in random transfers.

SATA Express was an interface for connecting SSDs through SATA-compatible ports, optionally providing multiple PCI Express lanes as a pure PCI Express connection to the attached storage device. M.2 is a specification for internally mounted computer expansion cards and associated connectors, which can use up to four PCI Express lanes.

PCI Express storage devices can implement both AHCI logical interface for backward compatibility, and NVM Express logical interface for much faster I/O operations provided by utilizing internal parallelism offered by such devices. Enterprise-class SSDs can also implement SCSI over PCI Express.

### Cluster interconnect

Certain data-center applications (such as large computer clusters) require the use of fiber-optic interconnects due to the distance limitations inherent in copper cabling. Typically, a network-oriented standard such as Ethernet or Fibre Channel suffices for these applications, but in some cases the overhead introduced by routable protocols is undesirable and a lower-level interconnect, such as InfiniBand, RapidIO, or NUMAlink is needed. Local-bus standards such as PCIe and HyperTransport can in principle be used for this purpose, but as of 2015, solutions are only available from niche vendors such as Dolphin ICS, and TTTech Auto.


## Competing protocols

PCIe 1.0 initially competed with PCI-X 2.0, with both specifications being ratified in 2003 and offering roughly the same maximum bandwidth (~4 GB/s). By 2005, however, PCIe emerged as the dominant technology.

Other communications standards based on high bandwidth serial architectures include InfiniBand, RapidIO, HyperTransport, Intel QuickPath Interconnect, the Mobile Industry Processor Interface (MIPI), and NVLink. Differences are based on the trade-offs between flexibility and extensibility vs latency and overhead. For example, making the system hot-pluggable, as with Infiniband but not PCI Express, requires that software track network topology changes.

Another example is making the packets shorter to decrease latency (as is required if a bus must operate as a memory interface). Smaller packets mean packet headers consume a higher percentage of the packet, thus decreasing the effective bandwidth. Examples of bus protocols designed for this purpose are RapidIO and HyperTransport.

PCI Express falls somewhere in the middle, targeted by design as a system interconnect (local bus) rather than a device interconnect or routed network protocol. Additionally, its design goal of software transparency constrains the protocol and raises its latency somewhat.

Delays in PCIe 4.0 implementations led to the Gen-Z consortium, the CCIX effort and an open Coherent Accelerator Processor Interface (CAPI) all being announced by the end of 2016.

On 11 March 2019, Intel presented Compute Express Link (CXL), a new interconnect bus, based on the PCI Express 5.0 physical layer infrastructure. The initial promoters of the CXL specification included: Alibaba, Cisco, Dell EMC, Facebook, Google, HPE, Huawei, Intel and Microsoft.


## Integrators list

The PCI-SIG Integrators List lists products made by PCI-SIG member companies that have passed compliance testing. The list include switches, bridges, NICs, SSDs, etc.
