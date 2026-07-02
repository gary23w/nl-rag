---
title: "lwIP"
source: https://en.wikipedia.org/wiki/LwIP
domain: contiki-os
license: CC-BY-SA-4.0
tags: contiki os, contiki ng, protothread model, micro ip stack
fetched: 2026-07-02
---

# lwIP

**lwIP** (**lightweight IP**) is a widely used open-source TCP/IP stack designed for embedded systems. lwIP was originally developed by Adam Dunkels in 2001 at the Swedish Institute of Computer Science and is now developed and maintained by a worldwide network of developers.

lwIP is used by many manufacturers of embedded systems, including Intel/Altera, Analog Devices, Xilinx, TI, ST and Freescale.

## lwIP network stack

The focus of the lwIP network stack implementation is to reduce resource usage while still having a full-scale TCP stack. This makes lwIP suitable for use in embedded systems with tens of kilobytes of free RAM and room for around 40 kilobytes of code ROM.

## lwIP protocol implementations

Aside from the TCP/IP stack, lwIP has several other important parts, such as a network interface, an operating system emulation layer, buffers and a memory management section. The operating system emulation layer and the network interface allow the network stack to be transplanted into an operating system, as it provides a common interface between lwIP code and the operating system kernel.

The network stack of lwIP includes an IP (Internet Protocol) implementation at the Internet layer that can handle packet forwarding over multiple network interfaces. Both IPv4 and IPv6 are supported dual stack since lwIP v2.0.0 . For network maintenance and debugging, lwIP implements ICMP (Internet Control Message Protocol). IGMP (Internet Group Management Protocol) is supported for multicast traffic management. While ICMPv6 (including MLD) is implemented to support the use of IPv6.

lwIP includes an implementation of IPv4 ARP (Address Resolution Protocol) and IPv6 Neighbor Discovery Protocol to support Ethernet at the data link layer. lwIP may also be operated on top of a PPP (Point-to-Point Protocol) implementation at the data link layer.

At the transport layer lwIP implements TCP (Transmission Control Protocol) with congestion control, RTT estimation and fast recovery/fast retransmit. UDP (User Datagram Protocol) is implemented with experimental UDP-Lite extensions.

### APIs and sockets

lwIP provides a specialized no-copy application programming interface (API) for enhanced network stack performance. The Berkeley socket API is optional. Raw sockets, or raw pcbs (protocol control blocks), are provided depending on the API used.

### Application layer support

At the application layer the lwIP network stack may be supported through the implementation of the following protocols. The DNS (Domain Name System), an SNMP (Simple Network Management Protocol) agent, in v1, v2 or v3, with private MIB (management information base) support and MIB compiler.

Operating systems that implement the lwIP TCP/IP stack may provide a range of supporting clients and servers at the application layer. Such as an IPv4 DHCP (Dynamic Host Configuration Protocol) client or IPv4 link-local addresses (AutoIP). Specialized raw API applications include: an HTTP server, a SNTP client, a SMTP client, a NetBIOS nameserver, a mDNS responder, a MQTT client and a TFTP server.

## OS implementations

lwIP is used as network stack in ReactOS and Genode and can be used in Minix and GNU Hurd to implement network servers.
