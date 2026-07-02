---
title: "Ethernet Powerlink"
source: https://en.wikipedia.org/wiki/Ethernet_Powerlink
domain: powerlink
license: CC-BY-SA-4.0
tags: ethernet powerlink, powerlink protocol, real-time industrial ethernet, deterministic ethernet
fetched: 2026-07-02
---

# Ethernet Powerlink

**Ethernet Powerlink** is a real-time protocol for standard Ethernet. It is an open protocol managed by B&R, ever since the dissolution of the Ethernet POWERLINK Standardization Group (EPSG) in 2023. It was introduced by Austrian automation company B&R in 2001.

This protocol has nothing to do with power distribution via Ethernet cabling or power over Ethernet (PoE), power line communication, or Bang & Olufsen's PowerLink cable.

## Overview

Ethernet Powerlink expands Ethernet with a mixed polling and timeslicing mechanism. This provides:

- Guaranteed transfer of time-critical data in very short isochronic cycles with configurable response time
- Time-synchronisation of all nodes in the network with very high precision of sub-microseconds
- Transmission of less time-critical data in a reserved asynchronous channel

Modern implementations reach cycle-times of under 200 μs and a time-precision (jitter) of less than 1 μs.

## Standardization

Powerlink was standardized by the Ethernet Powerlink Standardization Group (EPSG) and founded in June 2003 as an independent association. Working groups focus on tasks like safety, technology, marketing, certification and end users. The EPSG cooperates with the standardization bodies and associations, like the CAN in Automation (CiA) Group and the IEC.

## Physical layer

The original physical layer specified was 100BASE-TX Fast Ethernet. Since the end of 2006, Ethernet Powerlink with Gigabit Ethernet supported a transmission rate ten times higher (1,000 Mbit/s).

Repeating hubs instead of switches within the real-time domain is recommended to minimise delay and jitter. Ethernet Powerlink uses IAONA's Industrial Ethernet Planning and Installation Guide for clean cabling of industrial networks and both industrial Ethernet connectors 8P8C (commonly known as RJ45) and M12 are accepted.

## Data link layer

The standard Ethernet data link layer is extended by an additional bus scheduling mechanism, which guarantees that only one node at a time is accessing the network. The schedule is divided into an isochronous phase and an asynchronous phase. During the isochronous phase, time-critical data is transferred, while the asynchronous phase provides bandwidth for the transmission of non time-critical data. The Managing Node (MN) grants access to the physical medium via dedicated poll request messages. As a result, only one single node (CN) has access to the network at a time, which avoids collisions, present on older Ethernet hubs before switches. The CSMA/CD mechanism of non-switched Ethernet, which caused non-deterministic Ethernet behaviour, is avoided by the Ethernet Powerlink scheduling mechanism.

## Basic cycle

After system start-up is finished, the real-time domain is operating under real-time conditions. The scheduling of the basic cycle is controlled by the Managing Node (MN). The overall cycle time depends on the amount of isochronous data, asynchronous data and the number of nodes to be polled during each cycle.

The basic cycle consists of the following phases:

- **Start phase**: The Managing Node is sending out a synchronization message to all nodes. The frame is called SoC—Start of Cycle.
- **Isochronous phase**: The Managing Node calls each node to transfer time-critical data for process or motion control by sending the Preq - Poll Request - frame. The addressed node answers with the Pres - Poll Response - frame. Since all other nodes are listening to all data during this phase, the communication system provides a producer-consumer relationship.

The time frame which includes Preq-n and Pres-n is called time slot for the addressed node.

- **Asynchronous phase**: The Managing Node grants the right to one particular node for sending ad-hoc data by sending out the SoA—Start of Asynchronous—frame. The addressed node will answer with ASnd. Standard IP-based protocols and addressing can be used during this phase.

The quality of the Real-Time behavior depends on the precision of the overall basic cycle time. The length of individual phases can vary as long as the total of all phases remain within the basic cycle time boundaries. Adherence to the basic cycle time is monitored by the Managing Node. The duration of the isochronous and the asynchronous phase can be configured.

### Multiplex for bandwidth optimization

In addition to transferring isochronous data during each basic cycle, some nodes are also able to share transfer slots for better bandwidth utilization. For that reason, the isochronous phase can distinguish between transfer slots dedicated to particular nodes, which have to send their data in every basic cycle, and slots shared by nodes to transfer their data one after the other in different cycles. Therefore, less important yet still time-critical data can be transferred in longer cycles than the basic cycle. Assigning the slots during each cycle is at the discretion of the Managing Node.

### Poll response chaining

Mode used mainly for robotics applications and large superstructures. Key is a lower number of frames and better data distribution.

## OpenSAFETY

Today, machines, plants and safety systems are stuck in a rigid scheme made up of hardware-based safety functions. The consequences of this are cost-intensive cabling and limited diagnostic options. The solution is the integration of safety relevant application data into the standard serial control protocol. OpenSAFETY allows both publish/subscriber and client/server communication. Safety relevant data is transmitted via an embedded data frame inside of standard communication messages. Measures to avoid any undetected failures due to systematic or stochastic errors are an integral part of a functional safety protocol. OpenSAFETY is in conformance with IEC 61508. The protocol fulfills the requirements of SIL 3. Error detection techniques have no impact on existing transport layers.
