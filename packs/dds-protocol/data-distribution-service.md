---
title: "Data Distribution Service"
source: https://en.wikipedia.org/wiki/Data_Distribution_Service
domain: dds-protocol
license: CC-BY-SA-4.0
tags: dds protocol, data distribution service, real-time pub-sub, omg data distribution
fetched: 2026-07-02
---

# Data Distribution Service

The **Data Distribution Service** (**DDS**) for real-time systems is an Object Management Group (OMG) machine-to-machine (sometimes called middleware or connectivity framework) standard that aims to enable dependable, high-performance, interoperable, real-time, scalable data exchanges using a publish–subscribe pattern.

DDS addresses the real-time data exchange needs of applications within aerospace, defense, air-traffic control, autonomous vehicles, medical devices, robotics, power generation, simulation and testing, smart grid management, transportation systems, and other applications.

## Architecture

### Model

DDS is a networking middleware that simplifies complex network programming. It implements a publish–subscribe pattern for sending and receiving data, events, and commands among the nodes. Nodes that produce information (publishers) create "topics" (e.g., temperature, location, pressure) and publish "samples". DDS delivers the samples to subscribers that declare an interest in that topic.

DDS handles transfer chores: message addressing, data marshalling and de-marshalling (so subscribers can be on different platforms from the publisher), delivery, flow control, retries, etc. Any node can be a publisher, subscriber, or both simultaneously.

The DDS publish-subscribe model virtually eliminates complex network programming for distributed applications.

DDS supports mechanisms that go beyond the basic publish-subscribe model. The key benefit is that applications that use DDS for their communications are decoupled. Little design time needs be spent on handling their mutual interactions. In particular, the applications never need information about the other participating applications, including their existence or locations. DDS transparently handles message delivery without requiring intervention from the user applications, including:

- determining who should receive the messages
- where recipients are located
- what happens if messages cannot be delivered

DDS allows the user to specify quality of service (QoS) parameters to configure discovery and behavior mechanisms up-front. By exchanging messages anonymously, DDS simplifies distributed applications and encourages modular, well-structured programs. DDS also automatically handles hot-swapping redundant publishers if the primary fails. Subscribers always get the sample with the highest priority whose data is still valid (that is, whose publisher-specified validity period has not expired). It automatically switches back to the primary when it recovers, too.

### Interoperability

Both proprietary and open-source software implementations of DDS are available. These include application programming interfaces (APIs) and libraries of implementations in Ada, C, C++, C#, Java, Python, Scala, Lua, Pharo, Ruby, and Rust.

DDS vendors participated in interoperability demonstrations at the OMG Spring technical meetings from 2009 to 2013.

During demos, each vendor published and subscribed to each other's topics using a test suite called the shapes demo. For example, one vendor publishes information about a shape and the other vendors can subscribe to the topic and display the results on their own shapes display. Each vendor takes turns publishing the information and the other subscribe. Two things made the demos possible: the DDS-I or Real-Time Publish-Subscribe (RTPS) protocol, and the agreement to use a common model.

In March 2009, three vendors demonstrated interoperability between the individual, independent products that implemented the OMG Real-time Publish-Subscribe protocol version 2.1 from January 2009. The demonstration included the discovery of each other's publishers and subscribers on different OS Platforms (Microsoft Windows and Linux) and supported multicast and unicast network communications.

The DDS interoperability demonstration used scenarios such as:

- Basic connectivity to network using Internet Protocol (IP)
- Discovery of publishers and subscribers
- Quality of service (QoS) Compatibility between requester and offerer
- Delay-tolerant networking
- Multiple topics and instances of topics
- Exclusive ownerships of topics
- Content filtering of topic data including time and geographic

## History

Development of the DDS specification started in 2001. In 2004, the Object Management Group (OMG) published DDS version 1.0. Version 1.1 was published in December 2005, 1.2 in January 2007, and 1.4 in April 2015. DDS is covered by several US patents, among others.

The DDS specification describes two levels of interfaces:

- A lower data-centric publish-subscribe (DCPS) level that is targeted towards the efficient delivery of the proper information to the proper recipients.
- An optional higher data local reconstruction layer (DLRL), which allows for a simple integration of DDS into the application layer.

Other related standards followed the initial core document. The Real-time Publish-Subscribe Wire Protocol DDS Interoperability Wire Protocol Specification ensured that information published on a topic using one vendor's DDS implementation is consumable by one or more subscribers using the same or different vendor's DDS implementations. Although the specification is targeted at the DDS community, its use is not limited. Versions 2.0 was published in April 2008, version 2.1 in November 2010, 2.2 in September 2014, and 2.3 in May 2019.

DDS for Lightweight CCM (dds4ccm) offers an architectural pattern that separates the business logic from the non-functional properties. A 2012 extension added support for streams. A Java 5 Language PSM for DDS defined a Java 5 language binding, referred to as a Platform Specific Model (PSM) for DDS. It specified only the Data-Centric Publish-Subscribe (DCPS) portion of the DDS specification; Additionally, it encompasses the DDS APIs introduced by DDS-XTypes and DDS-CCM. DDS-PSM-Cxx defines the ISO/IEC C++ PSM language binding, referred to as a Platform Specific Model (PSM) for DDS. It provides a new C++ API for programming DDS that is more natural to a C++ programmer. The specification provides mappings for the application programming interface (API) specified in DDS-XTypes, and accessing quality of service (QoS) profiles specified in DDS-CCM.

Extensible and Dynamic Topic Types for DDS (DDS-XTypes) provided support for data-centric publish-subscribe communication where topics are defined with specific data structures. To be *extensible*, DDS topics use data types defined before compile time and used throughout the DDS global data space. This model is desirable when static type checking is useful. A Unified Modeling Language (UML) profile specified DDS domains and topics to be part of analysis and design modeling. This specification also defined how to publish and subscribe objects without first describing the types in another language, such as XML or OMG IDL. An interface definition language (IDL) was specified in 2014 independently from the Common Object Request Broker Architecture (CORBA) specification chapter 3. This IDL 3.5 was compatible with the CORBA 3 specification, but extracted as its own specification allowing it to evolve independently from CORBA.

Other protocols to be mentioned are: DDS-XRCE (DDS for eXtremely Resource Constrained Environments), this specification protocol allows the communication between devices of limited resources, like microcontroller for example and a DDS network. It makes publishing and subscribing to topics via an intermediate service in a DDS domain possible and DDS-RPC (RPC Over DDS) which defines Remote Procedure Calls. These provide a bidirectional request/reply communication and determine distributed services, and are detailed using a service interface. It also supports both synchronous and asynchronous method invocation.

Starting with DDS version 1.4 in 2015, the optional DLRL layer was moved to a separate specification.
