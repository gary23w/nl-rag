---
title: "Ethernet flow control"
source: https://en.wikipedia.org/wiki/Ethernet_flow_control
domain: rdma-networking
license: CC-BY-SA-4.0
tags: remote direct memory access, zero-copy transfer, kernel bypass, low latency networking
fetched: 2026-07-02
---

# Ethernet flow control

**Ethernet flow control** is a mechanism for temporarily stopping the transmission of data on the Ethernet-family of computer networks. The goal of this mechanism is to avoid packet loss in the presence of network congestion.

The first flow control mechanism, the **pause frame**, was defined by the **IEEE 802.3x** standard. The follow-on **priority-based flow control**, as defined in the **IEEE 802.1Qbb** standard, provides a link-level flow control mechanism that can be controlled independently for each class of service (CoS), as defined by IEEE P802.1p and is applicable to data center bridging (DCB) networks, and to allow for prioritization of voice over IP (VoIP), video over IP, and database synchronization traffic over default data traffic and bulk file transfers.

## Description

A sending station (computer or network switch) may be transmitting data faster than the other end of the link can accept it. Using flow control, the receiving station can signal the sender requesting suspension of transmissions until the receiver catches up. Flow control on Ethernet can be implemented at the data link layer.

The first flow control mechanism, the *pause frame*, was defined by the Institute of Electrical and Electronics Engineers (IEEE) task force that defined full duplex Ethernet link segments. The IEEE standard 802.3x was issued in 1997.

### Pause frame

An overwhelmed network node can send a pause frame, which halts the transmission of the sender for a specified period of time. A media access control (MAC) frame (EtherType 0x8808) is used to carry the pause command, with the Control opcode set to 0x0001 (hexadecimal). Only stations configured for full-duplex operation may send pause frames. When a station wishes to pause the other end of a link, it sends a pause frame to either the unique 48-bit destination address of this link or to the 48-bit reserved multicast address of 01-80-C2-00-00-01. The use of a well-known address makes it unnecessary for a station to discover and store the address of the station at the other end of the link.

Another advantage of using this multicast address arises from the use of flow control between network switches. The particular multicast address used is selected from a range of addresses that have been reserved by the IEEE 802.1D standard, which specifies the operation of switches used for bridging. Normally, a frame with a multicast destination sent to a switch will be forwarded out to all other ports of the switch. However, this range of multicast addresses is special and will not be forwarded by an 802.1D-compliant switch. Instead, frames sent to this range are understood to be frames meant to be acted upon only within the switch.

A pause frame includes the period of pause time being requested, in the form of a two-byte (16-bit), unsigned integer (0 through 65535). This number is the requested duration of the pause. The pause time is measured in units of pause *quanta*, where each quanta is equal to 512 bit times.

By 1999, several vendors supported receiving pause frames, but fewer implemented sending them.

### Issues

One original motivation for the pause frame was to handle network interface controllers (NICs) that did not have enough buffering to handle full-speed reception. This problem has become less common with advances in bus speeds and memory sizes. A more likely scenario is network congestion within a switch. For example, a flow can come into a switch on a higher speed link than the one it goes out, or several flows can come in over two or more links that total more than an output link's bandwidth. These will eventually exhaust any amount of buffering in the switch. However, blocking the sending link will cause all flows over that link to be delayed, even those that are not causing any congestion. This situation is a case of head-of-line (HOL) blocking, and can happen more often in core network switches due to the large numbers of flows generally being aggregated. Many switches use a technique called virtual output queues to eliminate the HOL blocking internally, so they will never send pause frames.

## Subsequent efforts

### Congestion management

Another effort began in March 2004, and in May 2004, it became the IEEE P802.3ar Congestion Management Task Force. In May 2006, the objectives of the task force were revised to specify a mechanism to limit the transmitted data rate at about 1% granularity. The request was withdrawn and the task force was disbanded in 2008.

### Priority flow control

Ethernet flow control disturbs the Ethernet class of service (defined in IEEE 802.1p), as the data of all priorities is stopped to clear the existing buffers, which might also consist of low-priority data. As a remedy to this problem, Cisco Systems defined its own priority flow control extension to the standard protocol. This mechanism uses 14 bytes of the 42-byte padding in a regular pause frame. The MAC control opcode for a Priority pause frame is 0x0101. Unlike the original pause, Priority pause indicates the pause time in quanta for each of the eight priority classes separately. The extension was subsequently standardized by the Priority-based Flow Control (PFC) project authorized on March 27, 2008, as IEEE 802.1Qbb. Draft 2.3 was proposed on June 7, 2010. Claudio DeSanti of Cisco was the editor. The effort was part of the data center bridging task group, which developed Fibre Channel over Ethernet.
