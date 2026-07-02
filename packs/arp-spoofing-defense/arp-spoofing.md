---
title: "ARP spoofing"
source: https://en.wikipedia.org/wiki/ARP_spoofing
domain: arp-spoofing-defense
license: CC-BY-SA-4.0
tags: arp spoofing defense, dynamic arp inspection, address resolution, man-in-the-middle prevention
fetched: 2026-07-02
---

# ARP spoofing

In computer networking, **ARP spoofing** (also **ARP cache poisoning** or **ARP poison routing**) is a technique by which an attacker sends (spoofed) Address Resolution Protocol (ARP) messages onto a local area network. Generally, the aim is to associate the attacker's MAC address with the IP address of another host, such as the default gateway, causing any traffic meant for that IP address to be sent to the attacker instead.

ARP spoofing may allow an attacker to intercept data frames on a network, modify the traffic, or stop all traffic. Often, the attack is used as an opening for other attacks, such as denial of service, man in the middle, or session hijacking attacks.

The attack can only be used on networks that use ARP, and requires the attacker to have direct access to the local network segment to be attacked.

## ARP vulnerabilities

The Address Resolution Protocol (ARP) is a widely used communications protocol for resolving internet layer addresses into link layer addresses.

When an Internet Protocol (IP) datagram is sent from one host to another in a local area network, the destination IP address must be resolved to a MAC address for transmission via the data link layer. The first host sends a broadcast packet on the local network. This packet is known as an *ARP request*. The second host with the IP in the ARP request then responds with a broadcast *ARP reply* that contains the MAC address associated with its IP.

ARP is a stateless protocol. Network hosts will automatically cache any ARP replies they receive, regardless of which or any network hosts requested them. Even ARP entries that have not yet expired in the cache will be overwritten when a new ARP reply packet is received. There is no method in the ARP protocol by which a host can authenticate the peer from which the packet originated. This behavior is the vulnerability that allows ARP spoofing to occur.

## Attack anatomy

The basic principle behind ARP spoofing is to exploit the lack of authentication in the ARP protocol by sending spoofed ARP messages onto the LAN. ARP spoofing attacks can be run from a compromised host on the LAN or from an attacker's machine that is connected directly to the target LAN.

Generally, the goal of the attack is to associate the attacker's host MAC address with the IP address of a target host, so that any traffic meant for the target host will be sent to the attacker's host. The attacker may choose to inspect the packets (spying), while forwarding the traffic to the actual default destination to avoid discovery, modify the data before forwarding it (man-in-the-middle attack), or launch a denial-of-service attack by causing some or all of the packets on the network to be dropped.

## Defenses

### Static ARP entries

The simplest form of certification is the use of static, read-only entries for critical services in the ARP cache of a host. Hosts don't need to transmit ARP requests where such entries exist. While static entries provide some security against spoofing, they increase maintenance effort as address mappings for all systems in the network must be generated and distributed. Securing ARP in this manner for all participants does not scale on a large network since the mapping has to be set for each pair of machines resulting in *n*2-*n* ARP entries that have to be configured when *n* machines are present; On each machine there must be an ARP entry for every other machine on the network; *n-1* ARP entries on each of the *n* machines.

### Detection and prevention software

Software that detects ARP spoofing generally relies on some form of certification or cross-checking of ARP responses. Uncertified ARP responses are then blocked. These techniques may be integrated with the DHCP server so that both dynamic and static IP addresses are certified. This capability may be implemented in individual hosts or may be integrated into Ethernet switches or other network equipment. The existence of multiple IP addresses associated with a single MAC address may indicate an ARP spoof attack, although there are legitimate uses of such a configuration. In a more passive approach, a device listens for ARP replies on a network and sends a notification via email when an ARP entry changes.

AntiARP also provides Windows-based spoofing prevention at the kernel level. ArpStar is a Linux module for kernel 2.6 and Linksys routers that drops invalid packets that violate mapping.

Some virtualized environments, such as the Kernel-based Virtual Machine, provide security mechanisms to prevent MAC spoofing between guests running on the same host.

Some Ethernet adapters provide MAC and VLAN anti-spoofing features.

OpenBSD watches passively for hosts impersonating the local host and notifies in case of any attempt to overwrite a permanent entry.

### OS security

Operating systems react differently. Linux ignores unsolicited replies, but, on the other hand, uses responses to requests from other machines to update its cache. Solaris accepts updates on entries only after a timeout. In Microsoft Windows, the behavior of the ARP cache can be configured through several registry entries under HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters, ArpCacheLife, ArpCacheMinReferenceLife, ArpUseEtherSNAP, ArpTRSingleRoute, ArpAlwaysSourceRoute, ArpRetryCount.

## Legitimate usage

The techniques that are used in ARP spoofing can also be used to implement redundancy of network services. For example, some software allows a backup server to issue a gratuitous ARP request in order to take over for a defective server and transparently offer redundancy. Circle and CUJO are two companies that have commercialized products centered around this strategy.

ARP spoofing is often used by developers to debug IP traffic between two hosts when a switch is in use: if host A and host B are communicating through an Ethernet switch, their traffic would normally be invisible to a third monitoring host M. The developer configures A to have M's MAC address for B, and B to have M's MAC address for A; and also configures M to forward packets. M can now monitor the traffic, exactly as in a man-in-the-middle attack.

## Tools

### Defense

| Name | OS | GUI | Free | Protection | Per interface | Active/passive | Notes |
|---|---|---|---|---|---|---|---|
| Agnitum Outpost Firewall | Windows | Yes | No | Yes | No | passive |   |
| AntiARP | Windows | Yes | No | Yes | No | active+passive |   |
| Antidote | Linux | No | Yes | No | ? | passive | Linux daemon, monitors mappings, unusually large number of ARP packets. |
| Arp_Antidote | Linux | No | Yes | No | ? | passive | Linux Kernel Patch for 2.4.18 – 2.4.20, watches mappings, can define action to take when. |
| Arpalert | Linux | No | Yes | No | Yes | passive | Predefined list of allowed MAC addresses, alert if MAC that is not in list. |
| ArpON | Linux | No | Yes | Yes | Yes | active+passive | Portable handler daemon for securing ARP against spoofing, cache poisoning or poison routing attacks in static, dynamic and hybrid networks. |
| ArpGuard | Mac | Yes | No | Yes | Yes | active+passive |   |
| ArpStar | Linux | No | Yes | Yes | ? | passive |   |
| Arpwatch | Linux | No | Yes | No | Yes | passive | Keep mappings of IP-MAC pairs, report changes via Syslog, Email. |
| ArpwatchNG | Linux | No | Yes | No | No | passive | Keep mappings of IP-MAC pairs, report changes via Syslog, Email. |
| Colasoft Capsa | Windows | Yes | No | No | Yes | no detection, only analysis with manual inspection |   |
| cSploit | Android (rooted only) | Yes | Yes | No | Yes | passive |   |
| elmoCut | Windows | Yes | Yes | No | ? | passive | EyeCandy ARP spoofer for Windows |
| Prelude IDS | ? | ? | ? | ? | ? | ? | ArpSpoof plugin, basic checks on addresses. |
| Panda Security | Windows | ? | ? | Yes | ? | Active | Performs basic checks on addresses |
| remarp | Linux | No | Yes | No | No | passive |   |
| Snort | Windows/Linux | No | Yes | No | Yes | passive | Snort preprocessor Arpspoof, performs basic checks on addresses |
| Winarpwatch | Windows | No | Yes | No | No | passive | Keep mappings of IP-MAC pairs, report changes via Syslog, Email. |
| XArp | Windows, Linux | Yes | Yes (+pro version) | Yes (Linux, pro) | Yes | active + passive | Advanced ARP spoofing detection, active probing and passive checks. Two user interfaces: normal view with predefined security levels, pro view with per-interface configuration of detection modules and active validation. Windows and Linux, GUI-based. |
| Seconfig XP | Windows 2000/XP/2003 only | Yes | Yes | Yes | No | only activates protection built-in some versions of Windows |   |
| zANTI | Android (rooted only) | Yes | Yes | No | ? | passive |   |
| NetSec Framework | Linux | No | Yes | No | No | active |   |
| anti-arpspoof | Windows | Yes | Yes | ? | ? | ? |   |
| DefendARP: | ? | ? | ? | ? | ? | ? | A host-based ARP table monitoring and defense tool designed for use when connecting to public wifi. DefendARP detects ARP poisoning attacks, corrects the poisoned entry, and identifies the MAC and IP address of the attacker. |
| NetCutDefender: | Windows | ? | ? | ? | ? | ? | GUI for Windows that can protect from ARP attacks |

### Spoofing

Some of the tools that can be used to carry out ARP spoofing attacks:

- Dsniff
- Ettercap
- arping
- Cain and Abel
