---
title: "Virtual Extensible LAN"
source: https://en.wikipedia.org/wiki/Virtual_Extensible_LAN
domain: network-overlays
license: CC-BY-SA-4.0
tags: network overlay, overlay tunneling, virtual networks, data center fabric
fetched: 2026-07-02
---

# Virtual Extensible LAN

**Virtual eXtensible LAN** (**VXLAN**) is a network virtualization technology that uses a VLAN-like encapsulation technique to encapsulate OSI layer 2 Ethernet frames within layer 4 UDP datagrams, using 4789 as the default IANA-assigned destination UDP port number, although many implementations that predate the IANA assignment use port 8472. VXLAN attempts to address the scalability problems associated with large cloud computing deployments. VXLAN endpoints, which terminate VXLAN tunnels and may be either virtual or physical switch ports, are known as **VXLAN tunnel endpoints** (**VTEPs**).

## History

VXLAN addresses the limitations of the VLAN standard for segmenting a physical network into multiple virtual networks. The 12-bit VLAN identifier limits the number of virtual networks on a physical network to 4096, while in some applications, IEEE 802.1ad can be used to extend this limit, this is generally insufficient for large-scale cloud computing infrastructures with many tenants. Also, the VXLAN standard provides for extending a virtual network across multiple geographically distributed physical networks by encapsulating layer 2 frames in UDP packets. This is useful for large distributed data centers.

VXLAN is an evolution of efforts to standardize on an overlay encapsulation protocol that addresses these issues. Compared to single-tagged IEEE 802.1Q VLANs, which provide a limited number of layer-2 VLANs (4094, using a 12-bit VLAN ID), VXLAN increases scalability up to about 16 million logical networks (using a 24-bit VNID) and allows for layer-2 adjacency across IP networks. Multicast or unicast with head-end replication (HER) is used to flood Broadcast, unknown-unicast and multicast traffic.

The VXLAN specification was originally created by VMware, Arista Networks and Cisco.

## Implementations

VXLAN is widely, but not universally, implemented in commercial networking equipment. Several open-source implementations of VXLAN also exist, including built-in capabilities in the Linux kernel.

### Commercial

Arista, Cisco, and VMware were the originators of VXLAN and support it in various products.

Other backers of the VXLAN technology include Adtran, Arrcus, Big Switch Networks, Broadcom, Citrix, Cumulus Networks, Dell EMC, Ericsson, Huawei, Joyent, Juniper Networks, Mellanox, MikroTik, Netgate, Netgear, Pica8, and Red Hat.

### Open source

- FreeBSD,
- OpenBSD,
- Linux,
- Open vSwitch is an example of a software-based virtual network switch that supports VXLAN overlay networks.

## Standards specifications

VXLAN is officially documented by the IETF in RFC 7348. VXLAN encapsulates a MAC frame in a UDP datagram for transport across an IP network, creating an overlay network or tunnel.

## Alternative technologies

Alternative technologies addressing the same or similar operational concerns include:

- IEEE 802.1ad ("Q-in-Q"), which greatly increases the number of VLANs supported by standard IEEE 802 Ethernet beyond 4K.
- IEEE 802.1ah ("MAC-in-MAC"), which supports tunneling Ethernet in a way that greatly increases the number of VLANs supported while avoiding a large increase in the size of the MAC Address table in a Carrier Ethernet deployment.
- Network Virtualization using Generic Route Encapsulation (NVGRE), which uses different framing but has similar goals to VxLAN.
