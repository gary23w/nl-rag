---
title: "Remote direct memory access"
source: https://en.wikipedia.org/wiki/Remote_direct_memory_access
domain: infiniband
license: CC-BY-SA-4.0
tags: infiniband fabric, high performance interconnect, hpc networking, channel adapter
fetched: 2026-07-02
---

# Remote direct memory access

In computing, **remote direct memory access** (**RDMA**) is direct memory access from the memory of one computer into that of another without involving either computer's operating system. This permits high-throughput, low-latency memory access over a network, which is especially useful in massively parallel computer clusters.

## Overview

RDMA supports zero-copy networking by enabling the network adapter to transfer data from the wire directly to application memory or from application memory directly to the wire, eliminating the need to copy data between application memory and the data buffers in the operating system. Such transfers require no work to be done by CPUs, caches, or context switches, and transfers continue in parallel with other system operations. This reduces latency in message transfer.

However, this strategy presents several problems related to the fact that the target node is not notified of the completion of the request (single-sided communications).

## Acceptance

As of 2018 RDMA had achieved broader acceptance as a result of implementation enhancements that enable good performance over ordinary networking infrastructure. For example RDMA over Converged Ethernet (RoCE) now is able to run over either lossy or lossless infrastructure. In addition iWARP enables an Ethernet RDMA implementation at the physical layer using TCP/IP as the transport, combining the performance and latency advantages of RDMA with a low-cost, standards-based solution. The RDMA Consortium and the DAT Collaborative have played key roles in the development of RDMA protocols and APIs for consideration by standards groups such as the Internet Engineering Task Force and the Interconnect Software Consortium.

Hardware vendors have started working on higher-capacity RDMA-based network adapters, with rates of 100 Gbit/s reported. Software vendors, such as IBM, Red Hat and Oracle Corporation, support these APIs in their latest products, and since 2013, engineers have been developing network adapters that implement RDMA over Ethernet. Both Red Hat Enterprise Linux and Red Hat Enterprise MRG have support for RDMA. Microsoft supports RDMA in Windows Server 2012 via SMB Direct. VMware ESXi also supports RDMA as of 2015.

Common RDMA implementations include the Virtual Interface Architecture, RDMA over Converged Ethernet (RoCE), InfiniBand, Omni-Path, iWARP and Ultra Ethernet.

## Using RDMA

Applications access control structures using well-defined APIs originally designed for the InfiniBand Protocol (although the APIs can be used for any of the underlying RDMA implementations). Using send and completion queues, applications perform RDMA operations by submitting work queue entries (WQEs) into the submission queue (SQ) and getting notified of responses from the completion queue (CQ).

## Transport types

RDMA can transport data reliably or unreliably over the Reliably Connected (RC) and Unreliable Datagram (UD) transport protocols, respectively. The former has the benefit of preserving requests (no requests are lost), while the latter requires fewer queue pairs when handling multiple connections. This is due to the fact that UD is connection-less, allowing a single host to communicate with any other using a single queue.
