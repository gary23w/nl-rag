---
title: "pcap"
source: https://en.wikipedia.org/wiki/Pcap
domain: network-forensics
license: CC-BY-SA-4.0
tags: network forensics investigation, packet capture reconstruction, traffic flow analysis, network evidence collection, deep packet inspection
fetched: 2026-07-02
---

# pcap

In the field of computer network administration, **pcap** is an application programming interface (API) for capturing network traffic. While the name is an abbreviation of *packet capture*, that is not the API's proper name. Unix-like systems implement pcap in the *libpcap* library; for Windows, there is a port of libpcap named *WinPcap* that is no longer supported or developed, and a port named *Npcap* for Windows 7 and later that is still supported.

Monitoring software may use libpcap, WinPcap, or Npcap to capture network packets traveling over a computer network and, in newer versions, to transmit packets on a network at the link layer, and to get a list of network interfaces for possible use with libpcap, WinPcap, or Npcap.

The pcap API is written in C, so other languages such as Java, .NET languages, and scripting languages generally use a wrapper; no such wrappers are provided by libpcap or WinPcap itself. C++ programs may link directly to the C API or make use of an object-oriented wrapper.

## Features

libpcap, WinPcap, and Npcap provide the packet-capture and filtering engines of many open-source and commercial network tools, including protocol analyzers (packet sniffers), network monitors, network intrusion detection systems, traffic-generators and network-testers.

Most current Unix-like systems provide a mechanism by which a program can capture network traffic to and from the machine running the program and, in some cases, other traffic to which that machine is attached. However, these mechanisms are significantly different from one another; the libpcap library provides a common API to access these mechanisms, allowing programs to be written to capture network traffic without having to worry about the details of all those mechanisms.

libpcap, WinPcap, and Npcap also support saving captured packets to a file, and reading files containing saved packets; applications can be written, using libpcap, WinPcap, or Npcap, to be able to capture network traffic and analyze it, or to read a saved capture and analyze it, using the same analysis code. A capture file saved in the format that libpcap, WinPcap, and Npcap use can be read by applications that understand that format, such as tcpdump, Wireshark, CA NetMaster, or Microsoft Network Monitor 3.x. The file format is described by Internet-Draft draft-ietf-opsawg-pcap; the current editors' version of the draft is also available.

The MIME type for the file format created and read by libpcap, WinPcap, and Npcap is application/vnd.tcpdump.pcap. The typical file extension is .pcap, although .cap and .dmp are also in common use.

## History

libpcap was originally developed by the tcpdump developers in the Network Research Group at Lawrence Berkeley Laboratory. The low-level packet capture, capture file reading, and capture file writing code of tcpdump was extracted and made into a library, with which tcpdump was linked. It is now developed by the same tcpdump.org group that develops tcpdump.

## pcap libraries for Windows

While libpcap was originally developed for Unix-like operating systems, a successful port for Windows was made, called WinPcap. It has been unmaintained since 2013, and several competing forks have been released with new features and support for newer versions of Windows.

### WinPcap

WinPcap consists of:

- x86 and x86-64 drivers for the Windows NT family (Windows NT 4.0, 2000, XP, Server 2003, Vista, 7, 8, and 10), which use Network Driver Interface Specification (NDIS) 5.x to read packets directly from a network adapter;
- implementations of a lower-level library for the listed operating systems, to communicate with those drivers;
- a port of libpcap that uses the API offered by the low-level library implementations.

Programmers at the Politecnico di Torino wrote the original code. As of 2008, CACE Technologies, a company set up by some of the WinPcap developers, developed and maintained the product. CACE was acquired by Riverbed Technology on October 21, 2010.

Because WinPcap uses the older NDIS 5.x APIs, it does not work on some builds of Windows 10, which have deprecated or removed those APIs in favor of the newer NDIS 6.x APIs. It also forces some limitations such as being unable to capture 802.1Q VLAN tags in Ethernet headers.

The WinPcap project has ceased development and WinPcap and WinDump are no longer maintained. The last official WinPcap release was 4.1.3 released March 8, 2013.

### Npcap

Npcap is the Nmap Project's packet sniffing library for Windows. It is based on WinPcap, but written to make use of Windows networking improvements in NDIS version 6. Its authors rewrote the WinPcap NDIS 5 Protocol Driver as a Light-Weight Filter (LWF) driver, a change that reduces processing overhead. Npcap maintenance releases updated the version of the included libpcap library to the latest available, allowing software authors to use the newer API features that Linux software had already supported. Most software that used WinPcap can be easily ported to use Npcap with minimal changes.

Npcap introduced several innovations that were not available in WinPcap:

- Npcap can be restricted so that only Administrators can sniff packets.
- Npcap is able to sniff and inject loopback packets (transmissions between services on the same machine) by using the Windows Filtering Platform.
- Npcap can capture 802.11 WiFi frames on a variety of commonly-available network adapters.

Unlike Nmap, Npcap is proprietary software and requires a special license for use and redistribution except for some limited internal uses.

### Win10Pcap

Win10Pcap implementation is also based on the NDIS 6 driver model and works stably with Windows 10. The project, however, has been inactive since 2016.

## Programs that use or used libpcap

- Bit-Twist, a libpcap-based Ethernet packet generator and editor for BSD, Linux, and Windows.
- Cain and Abel, a discontinued password recovery tool for Microsoft Windows
- EtherApe, a graphical tool for monitoring network traffic and bandwidth usage in real time.
- Firesheep, a discontinued extension for the Firefox web browser that captured packets and performed session hijacking
- iftop, a tool for displaying bandwidth usage (like top for network traffic)
- Kismet, for 802.11 wireless LANs
- L0phtCrack, a password auditing and recovery application.
- McAfee ePolicy Orchestrator, Rogue System Detection feature
- ngrep, aka "network grep", isolate strings in packets, show packet data in human-friendly output.
- Nmap, a port-scanning and fingerprinting network utility
- Pirni, a discontinued network security tool for jailbroken iOS devices.
- Scapy, a packet manipulation tool for computer networks, written in Python by Philippe Biondi.
- Snort, a network-intrusion-detection system.
- Suricata, a network intrusion prevention and analysis platform.
- Symantec Data Loss Prevention, Used to monitor and identify sensitive data, track its use, and location. Data loss policies allow sensitive data to be blocked from leaving the network or copied to another device.
- tcpdump, a tool for capturing and dumping packets for further analysis, and WinDump, the Windows port of tcpdump.
- Zeek, an intrusion detection system and network monitoring platform.
- URL Snooper, locate the URLs of audio and video files in order to allow recording them.
- WhatPulse, a statistical (input, network, uptime) measuring application.
- Wireshark (formerly Ethereal), a graphical packet-capture and protocol-analysis tool.
- XLink Kai, software that allows various LAN console games to be played online
- Xplico, a network forensics analysis tool (NFAT).
- PCAP Analyzer designed to process captured network traffic and provide protocol-level decoding and metadata extraction.

## Wrapper libraries for libpcap

- C++: Libtins, Libcrafter, PcapPlusPlus
- Perl: Net::Pcap
- Python: python-libpcap, Pcapy, WinPcapy
- Ruby: PacketFu
- Rust: pcap
- Tcl: tclpcap, tcap, pktsrc
- Java: jpcap, jNetPcap, Jpcap, Pcap4j, Jxnet
- .NET: WinPcapNET, SharpPcap, Pcap.Net
- Haskell: pcap
- OCaml: mlpcap
- Chicken Scheme: pcap
- Common Lisp: PLOKAMI
- Racket: SPeaCAP
- Go: pcap by Andreas Krennmair, pcap fork of the previous by Miek Gieben, pcap developed as part of the gopacket package
- Erlang: epcap
- Node.js: node_pcap

## Non-pcap libraries that read pcap files

- Python: pycapfile
- Python: PyPCAPKit

## Other applications or devices that read or write pcap or pcapng files

- Apache Drill, an open source SQL engine for interactive analysis of large scale datasets.
- Endace's EndaceProbe, a high scale packet capture system that continuously records weeks or months of network traffic.
