---
title: "WirelessHART"
source: https://en.wikipedia.org/wiki/WirelessHART
domain: wirelesshart
license: CC-BY-SA-4.0
tags: wirelesshart protocol, wireless hart mesh, industrial wireless sensor, process wireless network
fetched: 2026-07-02
---

# WirelessHART

**WirelessHART** within telecommunications and computing, is a wireless sensor networking technology. It is based on the Highway Addressable Remote Transducer Protocol (HART). Developed as a multi-vendor, interoperable wireless standard, WirelessHART was defined for the requirements of process field device networks.

## Technical description

The protocol utilizes a time synchronized, self-organizing, and self-healing mesh architecture. The protocol employs Time Division Multiple Access (TDMA), dividing each second into 100 time slots of 10 milliseconds each, with the entire network synchronized across these slots to enable collision-free, deterministic communication. Combined with Frequency Hopping Spread Spectrum (FHSS), the protocol changes wireless channel with each time slot across 15 of the 16 available channels in the 2.4 GHz band, and supports channel blacklisting to avoid heavily congested frequencies. Each device in the network acts as a router, forwarding messages from other devices and providing multiple redundant communication paths. The network supports two routing modes: graph routing, in which paths are determined centrally by a network manager and distributed to field devices, and source routing, used primarily for diagnostics, in which the originating device specifies the full sequence of hops. The protocol supports operation in the 2.4 GHz ISM band using IEEE 802.15.4 standard radios. The underlying wireless technology is based on the work of Dust Networks' TSMP technology.

## History

The standard was initiated in early 2004 and developed by 37 HART Communications Foundation (HCF) companies that - amongst others - included ABB, Emerson, Endress+Hauser, Pepperl+Fuchs, Siemens, Freescale Semiconductor, Software Technologies Group (which developed the initial WirelessHART WiTECK stack), and AirSprite Technologies which went on to form WiTECK, an open non-profit membership organization whose mission is to provide a reliable, cost-effective, high-quality portfolio of core enabling system software for industrial wireless sensing applications, under a company and platform-neutral umbrella.

WirelessHART was approved by a vote of the 210 member general HCF membership, ratified by the HCF Board of Directors, and introduced to the market in September 2007. On September 27, 2007, the Fieldbus Foundation, Profibus Nutzerorganisation, and HCF announced a wireless cooperation team to develop a specification for a common interface to a wireless gateway, further protecting users' investments in technology and work practices for leveraging these industry-pervasive networks. Following its completed work on the WirelessHART standard in September 2007, the HCF offered International Society of Automation (ISA) an unrestricted, royalty-free copyright license, allowing the ISA100 committee access to the WirelessHART standard.

Backward compatibility with the HART “user layer” allows transparent adaptation of HART compatible control systems and configuration tools to integrate new wireless networks and their devices, as well as continued use of proven configuration and system-integration work practices. It is estimated that 25 million HART field devices are installed worldwide, and approximately 3 million new wired HART devices are shipping each year. In September 2008, Emerson became the first process automation supplier to begin production shipments for its WirelessHART enabled products.

During the summer of 2009 NAMUR, an international user association in the chemical and pharmaceutical processing industries, conducted a field test of WirelessHART to verify alignment with the NAMUR requirements for wireless automation in process applications.

WirelessHart was approved by the International Electrotechnical Commission (IEC) in January 2009 with revision released in April 2010. The latest edition, version 2, was released in 2016 as IEC/PAS 62591:2016.
