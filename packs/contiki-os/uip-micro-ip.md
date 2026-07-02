---
title: "uIP (software)"
source: https://en.wikipedia.org/wiki/UIP_(micro_IP)
domain: contiki-os
license: CC-BY-SA-4.0
tags: contiki os, contiki ng, protothread model, micro ip stack
fetched: 2026-07-02
---

# uIP (software)

(Redirected from

UIP (micro IP)

)

The **uIP** is an open-source implementation of the TCP/IP network protocol stack intended for use with tiny 8- and 16-bit microcontrollers. It was initially developed by Adam Dunkels of the Networked Embedded Systems group at the Swedish Institute of Computer Science, licensed under a BSD style license, and further developed by a wide group of developers.

uIP can be very useful in embedded systems because it requires very small amounts of code and RAM. It has been ported to several platforms, including DSP platforms.

In October 2008, Cisco, Atmel, and SICS announced a fully compliant IPv6 extension to uIP, called uIPv6.

## Implementation

uIP makes many unusual design choices in order to reduce the resources it requires. uIP's native software interface is designed for small computer systems with no operating system. It can be called in a timed loop, and the call manages all the retries and other network behavior. The hardware driver is called after uIP is called. uIP builds the packet, and then the driver sends it, and optionally receives a response.

It is normal for IP protocol stack software to keep many copies of different IP packets, for transmission, reception and to keep copies in case they need to be resent. uIP is economical in its use of memory because it uses only one packet buffer. First, it uses the packet buffer in a half-duplex way, using it in turn for transmission and reception. Also, when uIP needs to retransmit a packet, it calls the application code in a way that requests for the previous data to be reproduced.

Another oddity is how uIP manages connections. Most IP implementations have one task per connection, and the task communicates with a task in a distant computer on the other end of the connection. In uIP, no multitasking operating system is assumed. Connections are held in an array. On each call, uIP tries to serve a connection, making a subroutine call to application code that responds to, or sends data. The size of the connection array is a number that can be adjusted when uIP is recompiled.

uIP is fully compliant with the RFCs that define TCP, UDP and IP. It also implements the mandatory maintenance protocol ICMP.

## Versions

uIP 0.9 is the version with the least dependence on operating systems, the smallest resource use, and the only version that presents a pure event loop API, but in its original form does not support IP version 6, only the older, more common IPv4. It may be used in embedded systems with very small amounts of resources.

It was delivered with a set of examples of higher-level protocols that also run on an event loop system, including HTTP (a simple web server), SMTP (simple mail transmission protocol), FTP (file transfer protocol), telnet (terminal emulation), and others. Despite the examples and its small size, uIP 0.9 can be difficult to apply because it does not use any form of socket API.

uIP is widely used code with well-known weaknesses. The design minimizes and separates 32-bit arithmetic so that it can be adjusted or optimized for 8 and 16-bit CPUs. Also, 16-bit software timers (common on small microcontrollers) can overflow and cause defective operation. This can be fixed with a timer system that does not overflow (e.g. the timers count down or use modular arithmetic).

Another issue is that its single packet buffer can have substantial throughput problems because a PC host usually delays the "ACK" packet, waiting for more packets. In slow, serial port implementations, the ack-throughput can be fixed by modifying uIP to send every packet as two half-packet fragments. uIP systems with fast ethernet or WiFi can modify the hardware driver to send every packet twice.

Some PCs do not correctly respond to a fast uIP system on a local Ethernet, because the uIP system can start a responding packet before the PC is ready to receive it. The solution is to call the uIP system less frequently in the main loop (Windows PCs are designed for a response time of about 1 millisecond). Typical implementations of uIP have a fixed IP address, which can make them impractical in real networks, although some have implemented DHCP.

Later versions of uIP, including the reference version of uIPv6, are integrated with Contiki, an operating system that uses coroutines for cooperative multitasking. Contiki provides the multitasking needed by a simplified socket API, simplifying the use of uIP. These versions may be less popular than 0.9 however. Many examples of embedded code do not use them.
