---
title: "OpenFlow"
source: https://en.wikipedia.org/wiki/OpenFlow
domain: software-defined-networking
license: CC-BY-SA-4.0
tags: software-defined networking, sdn, openflow, network function virtualization
fetched: 2026-07-02
---

# OpenFlow

**OpenFlow** is a communications protocol that gives access to the forwarding plane of a network switch or router over the network.

## Description

OpenFlow enables network controllers to determine the path of network packets across a network of switches. The controllers are distinct from the switches. This separation of the control from the forwarding allows for more sophisticated traffic management than is feasible using access control lists (ACLs) and routing protocols. Also, OpenFlow allows switches from different vendors — often each with their own proprietary interfaces and scripting languages — to be managed remotely using a single, open protocol. The protocol's inventors consider OpenFlow an enabler of software-defined networking (SDN).

OpenFlow allows remote administration of a layer 3 switch's packet forwarding tables, by adding, modifying and removing packet matching rules and actions. This way, routing decisions can be made periodically or *ad hoc* by the controller and translated into rules and actions with a configurable lifespan, which are then deployed to a switch's flow table, leaving the actual forwarding of matched packets to the switch at wire speed for the duration of those rules. Packets which are unmatched by the switch can be forwarded to the controller. The controller can then decide to modify existing flow table rules on one or more switches or to deploy new rules, to prevent a structural flow of traffic between switch and controller. It could even decide to forward the traffic itself, provided that it has told the switch to forward entire packets instead of just their header.

The OpenFlow protocol is layered on top of the Transmission Control Protocol (TCP) and prescribes the use of Transport Layer Security (TLS). Controllers should listen on TCP port 6653 for switches that want to set up a connection. Earlier versions of the OpenFlow protocol unofficially used port 6633. Some network control plane implementations use the protocol to manage the network forwarding elements. OpenFlow is mainly used between the switch and controller on a secure channel.

## History

The Open Networking Foundation (ONF), a user-led organization dedicated to promotion and adoption of software-defined networking (SDN), manages the OpenFlow standard. ONF defines OpenFlow as the first standard communications interface defined between the control and forwarding layers of an SDN architecture. OpenFlow allows direct access to and manipulation of the forwarding plane of network devices such as switches and routers, both physical and virtual (hypervisor-based). It is the absence of an open interface to the forwarding plane that has led to the characterization of today's networking devices as monolithic, closed, and mainframe-like. A protocol like OpenFlow is needed to move network control out of proprietary network switches and into control software that's open source and locally managed.

A number of network switch and router vendors announced intent to support or are shipping supported switches for OpenFlow, including Alcatel-Lucent, Big Switch Networks, Brocade Communications, and Radisys.

### Development

Version 1.1 of the OpenFlow protocol was released on 28 February 2011, and new development of the standard was managed by the ONF. In December 2011, the ONF board approved OpenFlow version 1.2 and published it in February 2012. The current version of OpenFlow is 1.5.1. However, version 1.6 has been available since September 2016, but accessible only to ONF's members.

In May 2011, Marvell and Larch Networks announced the availability of an OpenFlow-enabled, fully featured switching solution based on Marvell's networking control stack and the Prestera family of packet processors.

Indiana University in May 2011 launched a SDN Interoperability Lab in conjunction with the ONF to test how well different vendors' software-defined networking and OpenFlow products work together.

In June 2012, Infoblox released LINC, an open-source OpenFlow version 1.2 and 1.3 compliant software switch.

In February 2012, Big Switch Networks released Project Floodlight, an Apache-licensed open-source software OpenFlow Controller, and announced its OpenFlow-based SDN Suite in November of that year, which contains a commercial controller, and virtual switching and tap monitoring applications.

In February 2012, HP said it is supporting the standard on 16 of its Ethernet switch products.

In April 2012, Google's Urs Hölzle described how the company's internal network had been completely re-designed over the previous two years to run under OpenFlow with substantial efficiency improvement.

In January 2013, NEC unveiled a virtual switch for Microsoft's Windows Server 2012 Hyper-V hypervisor, which is designed to bring OpenFlow-based software-defined networking and network virtualisation to those Microsoft environments.

### Security concerns

- Covert communications
- Denial of service
- Man-in-the middle attack
- Potential single point of attack and failure
- Programming and Communication Channel Issues (w.r.t. security) - OpenFlow Deployment Experience
