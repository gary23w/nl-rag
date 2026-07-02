---
title: "OPC Unified Architecture"
source: https://en.wikipedia.org/wiki/OPC_Unified_Architecture
domain: plc-scada
license: CC-BY-SA-4.0
tags: plc, scada, ladder logic, industrial control, iec 61131, automation system
fetched: 2026-07-02
---

# OPC Unified Architecture

**OPC Unified Architecture** (**OPC UA**) is a cross-platform, open-source, IEC62541 standard for data exchange from sensors to cloud applications developed by the OPC Foundation. Distinguishing characteristics are:

- Standardized data models freely available for over 60 types of industrial equipment, published by the OPC Foundation via Companion Specifications
- Extensible security profiles, including authentication, authorization, encryption and checksums
- Extensible security key management, including X.509, token and password
- Support for both client-server and publish-subscribe communication patterns
- Communication protocol independent. Mappings to several communication protocols like TCP/IP, UDP/IP, WebSockets, AMQP and MQTT are specified
- Initially successful in standardized data exchange with industrial equipment (discrete manufacturing, process manufacturing, energy) and systems for data collection and control, but now also leveraged in building automation, weighing and kitchen equipment and cloud applications
- Open – open-source reference implementations freely available to OPC Foundation members, non members under GPL 2.0 license
- Cross-platform – not tied to one operating system or programming language
- Service-oriented architecture (SOA)
- The specification is freely available on the OPC Foundation website and is split into several parts to ease implementation, but only OPC UA stack vendors need to read them, end users simply leverage existing commercial and/or open-source stacks available in all popular programming languages

## History

Although developed by the same organization, OPC UA differs significantly from its predecessor, Open Platform Communications (OPC). The Foundation's goal for OPC UA was to provide a path forward from the original OPC communications model (namely the Microsoft Windows-only process exchange COM/DCOM) that would better meet the emerging needs of industrial automation.

After more than three years of specification work and another year for a prototype implementation, the first version of the Unified Architecture was released in 2006.

The current version of the specification is on 1.04 (22 November 2017). The new version of OPC UA now has added publish/subscribe in addition to the client/server communications infrastructure.

Although the original binding to COM/DCOM helped OPC to distribute well, it had several drawbacks:

- Frequent configuration issues with DCOM;
- No configurable time-outs;
- Microsoft Windows only;
- Lower security;
- No control over DCOM (COM/DCOM is kind of a black box, developers have no access to sources and therefore have to deal with bugs or insufficient implementations).

These drawbacks along with a number of other considerations pushed the decision to develop a new and independent stack for OPC UA, which replaces COM/DCOM. The main characteristics of this communication stack were:

- Multi-platform implementation, including portable ANSI C, Java and .NET implementations;
- Scalability: from smart sensors and smart actuators to mainframes;
- Multi-threaded, as well as single-threaded/single-task operation—necessary for porting the stack to embedded devices;
- Security, based on new standards;
- Configurable time-outs for each service;
- Chunking of big datagrams.

This communication stack reflects the beginning of various innovations. The OPC UA architecture is a service-oriented architecture (SOA) and is based on different logical levels.

OPC Base Services are abstract method descriptions, which are protocol independent and provide the basis for OPC UA functionality. The transport layer puts these methods into a protocol, which means it serializes/deserializes the data and transmits it over the network. Two protocols are specified for this purpose. One is a binary TCP protocol, optimized for high performance and the second is Web service-oriented.

The OPC information model is a Mesh Network based on nodes. These nodes can include any kind of meta information, and are similar to the objects of object-oriented programming (OOP). A node can have attributes for read access such as DataAccess (DA), HistoricDataAccess (HDA), methods that can be called (Commands), and triggered events that can be transmitted (such as AlarmEvent (AE), DataAccess, and DataChange). Nodes hold process data as well as other types of metadata. The OPC namespace contains the type-model. The namespace is a URI that identifies the naming authority responsible for assigning the identifier element of the NodeId. Naming authorities include the local Server, the underlying system, standards bodies and consortia. It is expected that most Nodes will use the URI of the Server or of the underlying system. OPC UA defines a common infrastructure model to facilitate this information exchange, and specifies the following:

- The information model to represent structure, behaviour and semantics;
- The message model to interact between applications;
- The communication model to transfer the data between end-points;
- The conformance model to guarantee interoperability between systems.

Client software can verify what profiles a server supports. This is necessary to obtain information, if a server only supports DA functionality or additionally AE, HDA, etc. Additionally, information can be obtained about whether a server supports a given profile. New and important features of OPC UA are:

- Redundancy support
- Heartbeat for connections in both directions (to indicate whether the other end is "alive"). This means that both server and client recognize interrupts.
- Buffering of data and acknowledgements of transmitted data. Lost connections don't lead to lost data anymore. Lost datagrams can be refetched.

At the OPC UA DevCon in October 2006, in Munich the first prototypes were presented live. Various UA Servers have been shown on a Beckhoff programmable logic controller and an embedded test board from Euros. The Beckhoff PLC is based on Windows XP Embedded and the embedded controller is based on the real-time operating system Euros. The company Embedded Labs Ltd demonstrated an OPC UA Server based on their own C++ UA Stack executing on a single chip ARM microcontroller with 64kB RAM. In October 2012 the German Fraunhofer-Application Center IOSB-INA and the Institute for industrial Information Technologies (inIT) showed that an OPC UA server is scalable down to 15 kB RAM and 10 kB ROM and therefore usable at chip level.

The current version of the specification is 1.05.06, and was released on 22 October, 2025.

## Specifications

The OPC UA specification is a multi-part specification and consists of the following parts:

1. Concepts
2. Security Model
3. Address Space Model
4. Services
5. Information Model
6. Mappings
7. Profiles
8. Data Access
9. Alarms and Conditions
10. Programs
11. Historical Access
12. Discovery and Global Services
13. Aggregates
14. PubSub
15. Safety
16. State Machines
17. Alias Names
18. Role-Based Security
19. Dictionary Reference
20. File Transfer
21. Device Onboarding
22. Base Network Model
23. Common Reference Types
24. Scheduler

Additionally, part 100 Devices, and part 200 Industrial Automation are also available. These build on the core set of specifications, and adds new common definitions that then are used in different companion specifications. E.g. both *OPC UA for Analyser Devices* and *OPC UA for Machinery* builds directly on part 100.

In contrast to the COM-based specifications, the UA specifications are not pure application specifications. They describe typical UA internal mechanisms, which get handled through the communication stack and are normally only of interest for those that port a stack to a specific target or those that want to implement their own UA stack.

The OPC UA application developers code against the OPC UA API and therefore mainly use API documentation. Nevertheless, part 3, 4, and 5 may be of interest for application developers.

## OSI model

OPC UA is a OSI model Layer 7: Application layer

With in the Application layer, OPC UA have 4 sub layers:

| **Layer** | Description | OPC UA standard |
|---|---|---|
| UA Application | Client Server |   |
| Serialization layer | Data Encoding | OPC 10000-6 UA Part 6: Mappings: DataEncoding |
| Secure channel layer | Secure Protocols | OPC 10000-6 UA Part 6: Mappings: SecurityProtocol |
| Transport layer | Transport Protocols | OPC 10000-6 UA Part 6: Mappings: TransportProtocols OPC 10000-14: UA Part 14: PubSub: Transport Protocol Mappings |

### Transport Protocols

OPC UA is a versatile industrial communication protocol that is designed to be transport-agnostic, and operate over several transport mechanisms, each corresponding to different layers of the OSI model. It can use, TCP, UDP or Ethernet directly, or it can also be encapsulated within higher-level application protocols such as HTTPS, WebSockets, AMQP, and MQTT.

OPC-UA support:

| Protocol name | OSI Layer | OPC UA standard | info |
|---|---|---|---|
| OPC UA UDP | 4 | OPC 10000-14: UA Part 14: PubSub, OPC UA UDP | Support Multicast, Broadcast, Unicast, DTLS |
| OPC UA Ethernet | 2 | OPC 10000-14: UA Part 14: PubSub: OPC UA Ethernet | EtherType for UADP is 0xB62C |
| AMQP | 7 | OPC 10000-14: UA Part 14: PubSub: AMQP |   |
| MQTT | 7 | OPC 10000-14: UA Part 14: PubSub: MQTT |   |
| HTTPS | 7 | OPC 10000-6 UA Part 6: Mappings: OPC UA HTTPS |   |
| WebSockets | 7 | OPC 10000-6 UA Part 6: Mappings: Websockets |   |
| OPC UA TCP | 4 | OPC 10000-6 UA Part 6: Mappings: OPC UA TCP |   |

## UA communication stack

The architecture of a UA application, independent of whether it is the server or client part, is structured into levels.

Some parts equalize to the former COM Proxy/Stubs and get provided by the OPC Foundation. The portability level is new; it simplifies porting the UA ANSI C stack to other target platforms. A port layer for Windows and Linux is also provided by the OPC Foundation.

## UA security

UA Security consists of authentication and authorization, encryption and data integrity via signatures. For Web Services the WS-SecureConversation gets used and is therefore compatible with .NET and other SO–AP implementations. For the binary variant, the algorithms of WS-SecureConversation have been followed and also converted to a binary equivalent. This is named as UA Secure Conversation.

There is also a mixed version where the code is binary, but the transport layer is SOAP. This is a compromise between efficient binary coding and firewall-friendly transmission. Binary coding always requires UA Secure Conversation. The authentication uses X.509 certificates exclusively. It relies on the application developer to choose which certificate store the UA application gets bound to. For instance, it is possible to use the public key infrastructure (PKI) of an Active Directory.

## Built-in data types

The OPC UA standard defines 25 built-in data types:

| Built-in type | C/C++ equivalent | Details | NodeId type |
|---|---|---|---|
| Boolean | bool | 0/1 (false or true) | 0 (numeric) |
| SByte | int8_t | -128 to 127 |   |
| Byte | uint8_t | 0 to 255 |   |
| Int16 | int16_t | -32768 to 32767 |   |
| UInt16 | uint16_t | 0 to 65535 |   |
| Int32 | int32_t | -2147483648 to 2147483647 |   |
| UInt32 | uint32_t | 0 to 4294967295 |   |
| Int64 | int64_t | -9223372036854775808 to 9223372036854775807 |   |
| UInt64 | uint64_t | 0 to 18446744073709551615 |   |
| Float | float | IEEE single precision (32 bit) floating point value |   |
| Double | double | IEEE double precision (64 bit) floating point value |   |
| StatusCode | uint32_t |   |   |
| String | uint8_t* / std::string |   | 3 (string) |
| DateTime | int64_t | number of 100 nanosecond intervals since 1/1/1601 (UTC) |   |
| GUID | implementation dependent | 16-byte number used as a unique identifier | 4 (GUID) |
| ByteString | (same as String) |   | 5 (byte string) |
| XmlElement | (same as String) |   |   |
| NodeId |   | namespace index and NodeId type |   |
| ExpandedNodeId |   | (similar to NodeId) |   |
| QualifiedName |   | namespace index and string |   |
| LocalizedText |   | string and a locale indicator |   |
| NumericRange |   | string (e.g. "0:4,1:5" for [0..4][1..5] array) |   |
| Variant |   | (built-in data types only) |   |
| ExtensionObject |   | scalars of any type |   |
| DataValue |   | a composite of a value, timestamps and status code |   |
| DiagnosticInfo |   | detailed error/diagnostic information |   |

## OPC UA APIs

UA APIs are available in several programming languages. Commercial SDKs are available for C, C++, Java, and .NET. Open-source stacks are available at least for C, C++, Java, JavaScript(node), Tcl and Python.

### .NET implementation

The .NET implementation uses ANSI C for the lower levels and implements the rest natively in .NET. That means only the handling of the socket and the Message-Chunking gets integrated from the ANSI C stack. De-serialization takes place directly in .NET and therefore gets converted directly into .NET structures and objects. This provides better performance than de-serializing into a C structure first and then copying the data to a .NET structure afterwards.

### Java implementation

Various stacks for Java were being developed. Similar to .NET, there are principally three variants:

1. Encapsulate the complete ANSI C stack via JNI, which complicates portability. Although the stack can be ported to different operating systems, it needs to get compiled for those individually. Also, the data needs to get copied to the JNI boundary, but benefits from the performance of C during de-serialization.
2. Code directly on the network layer (similar to the current .Net implementation) and de-serialize in Java. This saves one data copy execution, but still depends on the C stack.
3. Write a native Java OPC UA stack. This was observed to be the most portable, but estimated to take the most engineering effort to implement. The Eclipse Milo project provides a pure-Java, open-source, implementation of the UA 1.05 client and server specification.
4. Apache PLC4X project provides pure-Java, open-source implementation of UA client as well as network level frame descriptions which can be used for cross-language implementations.

Alternatively, there is the simple variant to only support the WebService protocol. For that, a SOAP Toolkit that supports WS-Security is needed.

## IEC 62541

IEC 62541 is a standard for OPC Unified Architecture.

| ID | release date | title |
|---|---|---|
| IEC/TR 62541-1 | 2016 | OPC Unified Architecture – Part 1: Overview and Concepts |
| IEC/TR 62541-2 | 2016 | OPC Unified Architecture – Part 2: Security Model |
| IEC 62541-3 | 2020 | OPC Unified Architecture – Part 3: Address Space Model |
| IEC 62541-4 | 2020 | OPC Unified Architecture – Part 4: Services |
| IEC 62541-5 | 2020 | OPC Unified Architecture – Part 5: Information Model |
| IEC 62541-6 | 2020 | OPC Unified Architecture – Part 6: Mappings |
| IEC 62541-7 | 2020 | OPC Unified Architecture – Part 7: Profiles |
| IEC 62541-8 | 2020 | OPC Unified Architecture – Part 8: Data Access |
| IEC 62541-9 | 2020 | OPC Unified Architecture – Part 9: Alarms and Conditions |
| IEC 62541-10 | 2020 | OPC Unified Architecture – Part 10: Programs |
| IEC 62541-11 | 2020 | OPC Unified Architecture – Part 11: Historical Access |
| IEC 62541-12 | 2020 | OPC Unified architecture – Part 12: Discovery and global services |
| IEC 62541-13 | 2020 | OPC Unified Architecture – Part 13: Aggregates |
| IEC 62541-14 | 2020 | OPC Unified architecture – Part 14: PubSub |
| IEC 62541-100 | 2015 | OPC Unified Architecture – Part 100: Device Interface |
