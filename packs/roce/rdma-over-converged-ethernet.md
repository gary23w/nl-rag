---
title: "RDMA over Converged Ethernet"
source: https://en.wikipedia.org/wiki/RDMA_over_Converged_Ethernet
domain: roce
license: CC-BY-SA-4.0
tags: rdma over converged ethernet, lossless ethernet, priority flow control, data center bridging
fetched: 2026-07-02
---

# RDMA over Converged Ethernet

**RDMA over Converged Ethernet** (**RoCE**) is a network protocol which allows remote direct memory access (RDMA) over an Ethernet network. There are multiple RoCE versions. RoCE v1 is an Ethernet link layer protocol and hence allows communication between any two hosts in the same Ethernet broadcast domain. RoCE v2 is an internet layer protocol which means that RoCE v2 packets can be routed. Although the RoCE protocol benefits from the characteristics of a converged Ethernet network, the protocol can also be used on a traditional or non-converged Ethernet network.The RoCE protocol is published and maintained by the InfiniBand Trade Association (IBTA).

## Background

Network-intensive applications like networked storage or cluster computing need a network infrastructure with a high bandwidth and low latency. The advantages of RDMA over other network application programming interfaces such as Berkeley sockets are lower latency, lower CPU load and higher bandwidth. The RoCE protocol allows lower latencies than its predecessor, the iWARP protocol. There are RoCE HCAs (Host Channel Adapter) with a latency as low as 1.3 microseconds while the lowest known iWARP HCA latency in 2011 was 3 microseconds.

## RoCE Family

RoCE versions differ in Layers 3 through Layer 4 of the OSI model. All versions of RoCE support RDMA functionality via the same underlying InfiniBand messages. These messages exist within the Base Transport Header (BTH), Extended Transport Header, (ETH) and payload, followed by an invariant cyclic redundancy check used for data integrity.

## RoCE v1

The RoCE v1 protocol is an Ethernet link layer protocol with Ethertype 0x8915. This means that the frame length limits of the Ethernet protocol apply: 1500 bytes for a regular Ethernet frame and 9000 bytes for a jumbo frame.

## RoCE v1.5

The RoCE v1.5 is an uncommon, experimental, non-standardized protocol that is based on the IP protocol. RoCE v1.5 uses the IP protocol field to differentiate its traffic from other IP protocols such as TCP and UDP. The value used for the protocol number is unspecified and is left to the deployment to select.

## RoCE v2

The RoCE v2 protocol exists on top of either the UDP/IPv4 or the UDP/IPv6 protocol. The UDP destination port number 4791 has been reserved for RoCE v2. Since RoCE v2 packets are routable the RoCE v2 protocol is sometimes called Routable RoCE or RRoCE. Although in general the delivery order of UDP packets is not guaranteed, the RoCE v2 specification requires that packets with the same UDP source port and the same destination address must not be reordered. In addition, RoCE v2 defines a congestion control mechanism that uses the IP ECN bits for marking and CNP frames for the acknowledgment notification. Software support for RoCE v2 is still emerging. Mellanox OFED 2.3 or later has RoCE v2 support and also Linux Kernel v4.5.

## RoCE versus InfiniBand

Both InfiniBand and RoCE are comprehensive network standards, not an individual protocol. However, InfiniBand specifies the transport layer, as the 'InfiniBand Transport Layer', which RoCE also makes use of. This can lead to confusion between the two standards, as RoCE implements the uppermost layers of InfiniBand but not the rest of the architecture.

RoCE defines how to perform RDMA over Ethernet while the InfiniBand architecture specification defines how to perform RDMA over an InfiniBand network. RoCE was expected to bring InfiniBand applications, which are predominantly based on clusters, onto a common Ethernet converged fabric. Others expected that InfiniBand will keep offering a higher bandwidth and lower latency than what is possible over Ethernet.

The technical differences between the RoCE and InfiniBand protocols are:

- Link Level Flow Control: InfiniBand uses a credit-based algorithm to guarantee lossless HCA-to-HCA communication. RoCE runs on top of Ethernet. Implementations may require lossless Ethernet network for reaching to performance characteristics similar to InfiniBand. Lossless Ethernet is typically configured via Ethernet flow control or priority flow control (PFC). Configuring a Data center bridging (DCB) Ethernet network can be more complex than configuring an InfiniBand network.
- Congestion Control: Infiniband defines congestion control based on FECN/BECN marking, RoCE v2 defines a congestion control protocol that uses ECN for marking as implemented in standard switches and CNP frames for acknowledgments.
- InfiniBand switches typically have lower latency than Ethernet switches. Port-to-port latency for one particular type of Ethernet switch is 230 ns versus 100 ns for an InfiniBand switch with the same number of ports.

## RoCE versus iWARP

While the RoCE protocols define how to perform RDMA using Ethernet and UDP/IP frames, the iWARP protocol defines how to perform RDMA over a connection-oriented transport like the Transmission Control Protocol (TCP). RoCE v1 is limited to a single Ethernet broadcast domain. RoCE v2 and iWARP packets are routable. The memory requirements of a large number of connections along with TCP's flow and reliability controls lead to scalability and performance issues when using iWARP in large-scale datacenters and for large-scale applications (i.e., large-scale enterprises, cloud computing, web 2.0 applications etc.). Also, multicast is defined in the RoCE specification while the current iWARP specification does not define how to perform multicast RDMA.

Reliability in iWARP is given by the protocol itself, as TCP is reliable. RoCE v2 on the other hand utilizes UDP which has a far smaller overhead and better performance but does not provide inherent reliability, and therefore reliability must be implemented alongside RoCE v2. One solution is to use converged Ethernet switches to make the local area network reliable. This requires converged Ethernet support on all the switches in the local area network and prevents RoCE v2 packets from traveling through a wide area network such as the internet which is not reliable. Another solution is to add reliability to the RoCE protocol (i.e., reliable RoCE) which adds handshaking to RoCE to provide reliability at the cost of performance.

The question of which protocol is better depends on the vendor. Chelsio recommends and exclusively support iWARP. Mellanox, Xilinx, and Broadcom recommend and exclusively support RoCE/RoCE v2. Intel initially supported iWARP but now supports both iWARP and RoCE v2. Other vendors involved in the network industry provide support for both protocols such as Marvell, Microsoft, Linux and Kazan. Cisco supports both RoCE and their own VIC RDMA protocol.

Both Protocols are standardized with iWARP being the standard for RDMA over TCP defined by the IETF and RoCE being the standard for RDMA over Ethernet defined by the IBTA.

## Criticism

Some aspects that could have been defined in the RoCE specification have been left out. These are:

- How to translate between primary RoCE v1 GIDs and Ethernet MAC addresses.
- How to translate between secondary RoCE v1 GIDs and Ethernet MAC addresses. It is not clear whether it is possible to implement secondary GIDs in the RoCE v1 protocol without adding a RoCE-specific address resolution protocol.
- How to implement VLANs for the RoCE v1 protocol. Current RoCE v1 implementations store the VLAN ID in the twelfth and thirteenth byte of the sixteen-byte GID, although the RoCE v1 specification does not mention VLANs at all.
- How to translate between RoCE v1 multicast GIDs and Ethernet MAC addresses. Implementations in 2010 used the same address mapping that has been specified for mapping IPv6 multicast addresses to Ethernet MAC addresses.
- How to restrict RoCE v1 multicast traffic to a subset of the ports of an Ethernet switch. As of September 2013, an equivalent of the Multicast Listener Discovery protocol has not yet been defined for RoCE v1.

In addition, any protocol running over IP cannot assume the underlying network has guaranteed ordering, any more than it can assume congestion cannot occur.

It is known that the use of PFC can lead to a network-wide deadlock.

## Vendors

Some vendors of RoCE enabled equipment include:

- Mellanox (acquired by Nvidia in 2020, brand retained)
- ATTO Technology
- Bloombase
- Broadcom
- Emulex (acquired by Broadcom)
- Cavium (acquired by Marvell, rebranded)
- QLogic (acquired by Cavium, rebranded)
- Dell Technologies
- H3C
- Huawei
- Intel
- Xilinx (acquired by AMD) (via FPGA soft IP core)
- Grovf
- Cerio
