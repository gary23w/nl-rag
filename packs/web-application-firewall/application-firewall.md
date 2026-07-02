---
title: "Application firewall"
source: https://en.wikipedia.org/wiki/Application_firewall
domain: web-application-firewall
license: CC-BY-SA-4.0
tags: web application firewall, application firewall, modsecurity waf, reverse proxy filtering, http request smuggling
fetched: 2026-07-02
---

# Application firewall

An **application firewall** is a form of firewall that controls input/output or system calls of an application or service. It operates by monitoring and blocking communications based on a configured policy, generally with predefined rule sets to choose from. The two primary categories of application firewalls are *network-based* and *host-based*.

## History

Gene Spafford of Purdue University, Bill Cheswick at AT&T Laboratories, and Marcus Ranum described a third-generation firewall known as an application layer firewall. Marcus Ranum's work, based on the firewall created by Paul Vixie, Brian Reid, and Jeff Mogul, spearheaded the creation of the first commercial product. The product was released by DEC, named the DEC SEAL by Geoff Mulligan - Secure External Access Link. DEC's first major sale was on June 13, 1991, to Dupont.

Under a broader DARPA contract at TIS, Marcus Ranum, Wei Xu, and Peter Churchyard developed the Firewall Toolkit (FWTK) and made it freely available under license in October 1993. The purposes for releasing the freely available, not for commercial use, FWTK were: to demonstrate, via the software, documentation, and methods used, how a company with (at the time) 11 years experience in formal security methods, and individuals with firewall experience, developed firewall software; to create a common base of very good firewall software for others to build on (so people did not have to continue to "roll their own" from scratch); to "raise the bar" of firewall software being used. However, FWTK was a basic application proxy requiring the user interactions.

In 1994, Wei Xu extended the FWTK with the Kernel enhancement of IP stateful filter and socket transparent. This was the first transparent firewall, known as the inception of the third generation firewall, beyond a traditional application proxy (the second generation firewall), released as the commercial product known as Gauntlet firewall. Gauntlet firewall was rated one of the top application firewalls from 1995 until 1998, the year it was acquired by Network Associates Inc, (NAI). Network Associates continued to claim that Gauntlet was the "worlds most secure firewall" but in May 2000, security researcher Jim Stickley discovered a large vulnerability in the firewall, allowing remote access to the operating system and bypassing the security controls. Stickley discovered a second vulnerability a year later, effectively ending Gauntlet firewalls' security dominance.

## Description

Application layer filtering operates at a higher level than traditional security appliances. This allows packet decisions to be made based on more than just source/destination IP Address or ports and can also use information spanning across multiple connections for any given host.

### Network-based application firewalls

Network-based application firewalls operate at the application layer of a TCP/IP stack and can understand certain applications and protocols such as File Transfer Protocol (FTP), Domain Name System (DNS), or Hypertext Transfer Protocol (HTTP). This allows it to identify unwanted applications or services using a non standard port or detect if an allowed protocol is being abused.

Modern versions of network-based application firewalls can include the following technologies:

- Encryption offloading
- Intrusion prevention system
- Data loss prevention

Web application firewalls (WAF) are a specialized version of a network-based appliance that acts as a reverse proxy, inspecting traffic before being forwarded to an associated server.

### Host-based application firewalls

A host-based application firewall monitors application system calls or other general system communication. This gives more granularity and control, but is limited to only protecting the host it is running on. Control is applied by filtering on a per process basis. Generally, prompts are used to define rules for processes that have not yet received a connection. Further filtering can be done by examining the process ID of the owner of the data packets. Many host-based application firewalls are combined or used in conjunction with a packet filter.

Due to technological limitations, modern solutions such as sandboxing are being used as a replacement of host-based application firewalls to protect system processes.

## Implementations

Application firewalls are available in various forms, including free and open-source software as well as commercial products.

### Mac OS X

Starting with Mac OS X Leopard, an implementation of the TrustedBSD MAC framework (taken from FreeBSD), was included. The TrustedBSD MAC framework is used to sandbox services and provides a firewall layer, given the configuration of the sharing services in Mac OS X Leopard and Snow Leopard. Third-party applications can provide extended functionality, including filtering out outgoing connections by app.

### Linux

This is a list of security software packages for Linux, allowing filtering of application to OS communication, possibly on a by-user basis:

- AppArmor
- Little Snitch
- Kerio Control — a commercial product from Kerio Technologies
- ModSecurity — also works under Windows, Mac OS X, Oracle Solaris and other versions of Unix. ModSecurity is designed to work with the Web servers IIS, Apache2 and NGINX.
- OpenSnitch
- Portmaster — an activity monitoring application by Safing. It is also available for Microsoft Windows.
- Systrace
- Zorp firewall

### Windows

- Minimal Firewall

- Microsoft Defender Firewall

- Portmaster

- Simplewall

- Tinywall

- WinGate

### Network appliances

These devices may be sold as hardware, software, or virtualized network appliances.

**Next-Generation Firewalls:**

- Cisco Firepower Threat Defense
- Check Point
- Fortinet FortiGate Series
- Juniper Networks SRX Series
- Palo Alto Networks
- SonicWALL TZ/NSA/SuperMassive Series

**Web Application Firewalls/LoadBalancers:**

- A10 Networks Web Application Firewall
- Barracuda Networks Web Application Firewall/Load Balancer ADC
- Citrix NetScaler
- F5 Networks BIG-IP Application Security Manager
- Fortinet FortiWeb Series
- KEMP Technologies
- Imperva

**Others:**

- CloudFlare
- Meraki
- Smoothwall
- Snapt Inc
