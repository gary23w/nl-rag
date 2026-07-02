---
title: "Fibre Channel over Ethernet"
source: https://en.wikipedia.org/wiki/Fibre_Channel_over_Ethernet
domain: infiniband
license: CC-BY-SA-4.0
tags: infiniband fabric, high performance interconnect, hpc networking, channel adapter
fetched: 2026-07-02
---

# Fibre Channel over Ethernet

**Fibre Channel over Ethernet** (**FCoE**) is a computer network technology that encapsulates Fibre Channel frames over Ethernet networks. This allows Fibre Channel to use 10 Gigabit Ethernet networks (or higher speeds) while preserving the Fibre Channel protocol. The specification was part of the International Committee for Information Technology Standards T11 FC-BB-5 standard published in 2009. FCoE did not see widespread adoption.

## Functionality

FCoE transports Fibre Channel directly over Ethernet while being independent of the Ethernet forwarding scheme. The FCoE protocol specification replaces the FC0 and FC1 layers of the Fibre Channel stack with Ethernet. By retaining the native Fibre Channel constructs, FCoE was meant to integrate with existing Fibre Channel networks and management software.

Traditionally, data centers used both Ethernet for TCP/IP networks and Fibre Channel for SANs, each having different and mostly incompatible interfaces/connections and interconnects/wiring and thus requires separate cabling/wiring and interconnects such as switching hardware for each. With the advent of FCoE, SANs that would have traditionally used Fibre Channel is consolidated with Ethernet and becomes another network protocol running on the Ethernet fabric, alongside traditional traffic such as IP. FCoE operates on top of the data link layer in the OSI model which contrasts with most other well-known protocols that may use Ethernet, such as (for a storage-related example) iSCSI, which runs on top of TCP over IP. As a consequence, FCoE is not routable at the IP layer and will not work across routed IP networks such as the Internet.

Since classical Ethernet had no priority-based flow control, unlike Fibre Channel, FCoE required enhancements to the Ethernet standard to support a priority-based flow control mechanism (to reduce frame loss from congestion). The IEEE standards body added priorities in the data center bridging (dcb) Task Group.

Fibre Channel required three primary extensions to deliver the capabilities of Fibre Channel over Ethernet networks:

- Encapsulation of native Fibre Channel frames into Ethernet Frames.
- Extensions to the Ethernet protocol itself to enable an Ethernet fabric in which frames are not routinely lost during periods of congestion.
- Mapping between Fibre Channel N_port IDs (aka FCIDs) and Ethernet MAC addresses.

Computers can connect to FCoE with converged network adapters (CNAs), which contain both Fibre Channel host bus adapter (HBA) and Ethernet network interface controller (NIC) functionality on the same physical card. CNAs have one or more physical Ethernet ports. FCoE encapsulation can be done in software with a conventional Ethernet network interface card, however FCoE CNAs offload (from the CPU) the low level frame processing and SCSI protocol functions traditionally performed by Fibre Channel host bus adapters.

## Application

The main application of FCoE is in data center storage area networks (SANs). FCoE has particular application in data centers due to the cabling reduction it makes possible, as well as in server virtualization applications, which often require many physical I/O connections per server.

With FCoE, network (IP) and storage (SAN) data traffic can be consolidated using a single network. This consolidation can:

- reduce the number of network interface cards required to connect to disparate storage and IP networks
- reduce the number of cables and switches
- reduce power and cooling costs

## Frame format

FCoE is encapsulated over Ethernet with the use of a dedicated Ethertype, 0x8906. A single 4-bit field (version) satisfies the IEEE sub-type requirements. The 802.1Q tag is optional but may be necessary in a given implementation. The SOF (start of frame) and EOF (end of frame) are encoded as specified in RFC 3643. Reserved bits are present to guarantee that the FCoE frame meets the minimum length requirement of Ethernet. Inside the encapsulated Fibre Channel frame, the frame header is retained so as to allow connecting to a storage network by passing on the Fibre Channel frame directly after de-encapsulation.

The FIP (FCoE Initialization Protocol) is an integral part of FCoE. Its main goal is to discover and initialize FCoE capable entities connected to an Ethernet cloud. FIP uses a dedicated Ethertype of 0x8914.

## Timeline

In October 2003, Azul Technology developed early version and applied for a patent.

In April 2007, the FCoE standardization activity started.

In October 2007, the first public end-to-end FCoE demo occurred at Storage Network World including adapters from QLogic, switches from Nuova Systems, and storage from NetApp (none of the companies involved made any product announcements at the time).

In April 2008, an early implementor was Nuova Systems, a subsidiary of Cisco Systems, which announced a switch. Brocade Communications Systems also announced support in 2008. After the Great Recession, any new technology had a hard time getting established.

In June 2009, the FCoE technology that had been defined as part of the International Committee for Information Technology Standards (INCITS) T11 FC-BB-5 standard was forwarded to ANSI for publication.

In May 2010, the FC-BB-5 standard was published as ANSI/INCITS 462-2010. Some additional work was done in the INCITS.

Data center switches from Force10 and Dell PowerConnect supported FCoE and in June 2013, Dell Networking, which is the new brand-name for all networking portfolio of Dell, introduced the S5000 series which can be a fully native FCoE switch with the option to include a native fibre channel module, allowing you to connect the S5000 directly to an FC SAN environment.
