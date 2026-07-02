---
title: "Real-time communication"
source: https://en.wikipedia.org/wiki/Real-time_communication
domain: webrtc-datachannel
license: CC-BY-SA-4.0
tags: webrtc datachannel, peer-to-peer data channel, browser peer connection, webrtc data transfer
fetched: 2026-07-02
---

# Real-time communication

**Real-time communication** (**RTC**) is a category of software protocols and communication hardware media that gives real-time guarantees, which is necessary to support real-time guarantees of real-time computing. Real-time communication protocols are dependent not only on the validity and integrity of data transferred but also the timeliness of the transfer. Real-time communication systems are generally understood as one of two types: hard real-time (HRT) and soft real-time (SRT). The difference between a hard and soft real-time communication system is the consequences of incorrect operation. Safety-critical systems capable of causing catastrophic consequences upon a fault, such as aircraft fly-by-wire systems, are designated as hard real-time, whereas non-critical but ideally real-time systems, such as hotel reservation systems, are designated as soft real-time. The designation of a real-time communication system as hard or soft has significant influence on its design.

## Hard real-time systems

Hard real-time communication systems are frequently electromechanically linked to a physical mechanism, often one that interfaces directly with people or property, which often contributes to or defines the potential danger of a fault. Due to their safety-critical nature, the communication protocols defined in a hard real-time system generally must be deterministic. Hard real-time communication systems are particularly common in the transportation, industrial, and medical sectors. Common applications include control systems, automotive controllers, medical devices, and critical safety systems such as airbag firing computers.

### Examples

- The spacecraft communication network SpaceWire supports real-time communication.
- Time-Triggered Ethernet supports real-time synchronous communication in complex multi-hop Ethernet networks.

## Soft real-time systems

Unlike hard real-time communication systems, soft real-time communication systems generally do not have the capacity to cause catastrophic harm upon a fault, which allows for non-deterministic, less rigorous network infrastructure. This allows soft real-time communication systems to operate over consumer networks such as residential internet connections and cellular networks. A large amount of soft real-time systems are telecommunications products such as VoIP systems and certain video calling platforms such as Discord and Google Meet. Data transmitted over a soft real-time communication system is not stored in a centralized server, and peers are connected directly to one another rather than through a server, although intermediary connecting nodes between peers are allowed when a direct link cannot be established.

### Examples

- WebRTC, an open-source real-time communication framework for mobile applications and web browsers, is the current most prominent implementation of real-time communication in the web-oriented telecommunications space.
