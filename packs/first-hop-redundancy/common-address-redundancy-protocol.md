---
title: "Common Address Redundancy Protocol"
source: https://en.wikipedia.org/wiki/Common_Address_Redundancy_Protocol
domain: first-hop-redundancy
license: CC-BY-SA-4.0
tags: first hop redundancy, gateway redundancy, virtual router, hot standby
fetched: 2026-07-02
---

# Common Address Redundancy Protocol

The **Common Address Redundancy Protocol** or **CARP** is a computer networking protocol which allows multiple hosts on the same local area network to share a set of IP addresses. Its primary purpose is to provide failover redundancy, especially when used with firewalls and routers. In some configurations, CARP can also provide load balancing functionality. CARP provides functionality similar to Virtual Router Redundancy Protocol (VRRP) and to Cisco Systems' Hot Standby Router Protocol (HSRP). It is implemented in several BSD-based operating systems and has been ported to Linux (ucarp).

## Example

If there is a single computer running a packet filter, and it goes down, the networks on either side of the packet filter can no longer communicate with each other, or they communicate without any packet filtering. If, however, there are two computers running a packet filter, running CARP, then if one fails, the other will take over, and computers on either side of the packet filter will not be aware of the failure, so operation will continue as normal. In order to make sure the new master operates the same as the old one, the packet filter used must support synchronization of state between the two computers.

## Principle of redundancy

A group of hosts using CARP is called a "group of redundancy". The group of redundancy allocates itself an IP address which is shared or divided among the members of the group. Within this group, a host is designated as "master". The other members are "backup". The main host is that which "takes" the IP address. It answers any traffic or ARP request brought to the attention of this address. Each host can belong to several groups of redundancy. Each host must have a second unique IP address.

A common use of CARP is the creation of a group of redundant firewalls. The virtual IP address allotted to the group of redundancy is indicated as the address of the default router on the computers behind this group of firewalls. If the main firewall breaks down or is disconnected from the network, the virtual IP address will be taken by one of the firewall slaves and the service availability will not be interrupted.

## History

In the late 1990s the Internet Engineering Task Force (IETF) began work on a protocol for router redundancy. In 1997, Cisco informed the IETF that it had patents in this area and, in 1998, pointed out its patent on HSRP. Nonetheless, IETF continued work on VRRP. After some debate, the IETF VRRP working group decided to approve the standard, despite its reliance on patented techniques, as long as Cisco made the patent available to third parties under reasonable and non-discriminatory licensing terms.

Cisco informed the OpenBSD developers that it would enforce its patent on HSRP. Cisco's position may have been due to their lawsuit with Alcatel. As Cisco's licensing terms prevented an open-source VRRP implementation, the OpenBSD developers began developing CARP instead. OpenBSD focuses on security. They designed CARP to use cryptography. This made CARP fundamentally different from VRRP and ensured that CARP did not infringe on Cisco's patent. CARP became available in October 2003. Later, it was integrated into FreeBSD (first released in May 2005 with FreeBSD 5.4), NetBSD and Linux (ucarp). While Cisco's US patent expired in 2014, the two incompatible protocols continue to coexist.

## Incompatibility with IETF standards

OpenBSD uses VRRP's protocol number and MAC addresses. The OpenBSD project requested unique numbers from the Internet Assigned Numbers Authority (IANA) but was denied.

To allocate numbers, IANA has several requirements. At the time, these were specified in RFC 2780. Requirements include participating in a collaborative, lengthy discussion process within the IETF and producing a detailed textual specification of the protocol. The OpenBSD developers met neither requirement. OpenBSD's website states the following:

> As a final note of course, when we petitioned IANA, the IETF body regulating[sic] "official" internet protocol numbers, to give us numbers for CARP and *pfsync*, our request was denied. Apparently we had failed to go through an official standards organization. Consequently we were forced to choose a protocol number which would not conflict with anything else of value, and decided to place CARP at IP protocol 112. We also placed *pfsync* at an open and unused number. We informed IANA of these decisions, but they declined to reply.

IANA had assigned protocol number 112 to VRRP (in 1998, via RFC 2338). Protocol number 112 remains in use by VRRP.

CARP also uses a range of Ethernet MAC addresses which IEEE had assigned to IANA/IETF for the VRRP protocol.

In spite of the overlap, it is still possible to use VRRP and CARP in the same broadcast domain, as long as the VRRP group ID and the CARP virtual host ID are different.
