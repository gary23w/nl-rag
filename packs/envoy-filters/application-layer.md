---
title: "Application layer"
source: https://en.wikipedia.org/wiki/Application_layer
domain: envoy-filters
license: CC-BY-SA-4.0
tags: envoy http filter, listener filter chain, proxy filter extension, wasm filter
fetched: 2026-07-02
---

# Application layer

An **application layer** is an abstraction layer that specifies the shared communication protocols and interface methods used by hosts in a communications network.

An *application layer* abstraction is specified in both the Internet Protocol Suite (TCP/IP) and the OSI model. Although both models use the same term for their respective highest-level layer, the detailed definitions and purposes are different.

## Historical and conceptual perspective

The concept of the application layer emerged from early efforts to standardize network communication by defining distinct layers of protocol functionality. In the OSI model developed in the late 1970s and early 1980s, the application layer was explicitly separated from lower layers like session and presentation to modularize network services and applications for interoperability and clarity. Contrasting this, the TCP/IP model, whose origins date back to the 1970s and which became the foundation of the modern Internet, integrates these functions into a broader application layer that handles process-to-process communication. This design emphasizes simplicity and robustness by placing intelligence and complexity on the network's edge rather than the core, enabling nearly any network to interconnect. As a result, the application layer serves as the interface for diverse networking protocols that drive everyday Internet-based services, reflecting decades of evolution aimed at flexible, interoperable communication across heterogeneous networks.

## Internet protocol suite

In the Internet protocol suite, the application layer contains the communications protocols and interface methods used in process-to-process communications across an Internet Protocol (IP) computer network. The application layer only standardizes communication and depends upon the underlying transport layer protocols to establish host-to-host data transfer channels and manage the data exchange in a client–server or peer-to-peer networking model. Though the TCP/IP application layer does not describe specific rules or data formats that applications must consider when communicating, the original specification (in RFC 1123) does rely on and recommend the robustness principle for application design.

## OSI model

In the OSI model, the definition of the application layer is narrower in scope. The OSI model defines the application layer as only the interface responsible for communicating with host-based and user-facing applications. OSI then explicitly distinguishes the functionality of two additional layers, the session layer and presentation layer, as separate levels below the application layer and above the transport layer. OSI specifies a strict modular separation of functionality at these layers and provides protocol implementations for each. In contrast, the Internet Protocol Suite compiles these functions into a single layer.

### Sublayers

Originally, the OSI model consisted of two kinds of application layer services with their related protocols. These two sublayers are the common application service element (CASE) and specific application service element (SASE). Generally, an application layer protocol is realized by using the functionality of several application service elements. Some application service elements invoke different procedures based on the version of the session service available.

#### CASE

The common application service element sublayer provides services for the application layer and requests services from the session layer. It provides support for common application services, such as:

- ACSE (Association Control Service Element)
- ROSE (Remote Operation Service Element)
- CCR (Commitment Concurrency and Recovery)
- RTSE (Reliable Transfer Service Element)

#### SASE

The specific application service element sublayer provides application-specific services (protocols), such as:

- FTAM (File Transfer, Access and Manager)
- VT (Virtual Terminal)
- MOTIS (Message Oriented Text Interchange Standard)
- CMIP (Common Management Information Protocol)
- JTM (Job Transfer and Manipulation)
- MMS (Manufacturing Messaging Specification)
- RDA (Remote Database Access)
- DTP (Distributed Transaction Processing)

## Protocols

The IETF definition document for the application layer in the Internet Protocol Suite is RFC 1123. It provided an initial set of protocols that covered the major aspects of the functionality of the early Internet:

- Hypertext documents: Hypertext Transfer Protocol (HTTP)
- Remote login to hosts: Telnet, Secure Shell
- File transfer: File Transfer Protocol (FTP), Trivial File Transfer Protocol (TFTP)
- Electronic mail transport: Simple Mail Transfer Protocol (SMTP)
- Networking support: Domain Name System (DNS)
- Host initialization: BOOTP
- Remote host management: Simple Network Management Protocol (SNMP), Common Management Information Protocol over TCP (CMOT)

### Examples

Additional notable application-layer protocols include the following:

- 9P, Plan 9 from Bell Labs distributed file system protocol
- AFP, Apple Filing Protocol
- APPC, Advanced Program-to-Program Communication
- AMQP, Advanced Message Queuing Protocol
- Atom Publishing Protocol
- BEEP, Block Extensible Exchange Protocol
- Bitcoin
- BitTorrent
- CFDP, Coherent File Distribution Protocol
- CoAP, Constrained Application Protocol
- DDS, Data Distribution Service
- DeviceNet
- DNS, Domain Name Services
- eDonkey
- ENRP, Endpoint Handlespace Redundancy Protocol
- FastTrack (KaZaa, Grokster, iMesh)
- Finger, User Information Protocol
- Freenet
- FTAM, File Transfer Access and Management
- FTP, File Transfer Protocol
- Gemini, Gemini protocol
- Gopher, Gopher protocol
- HL7, Health Level Seven
- HTTP, Hypertext Transfer Protocol
- Hypercore, formerly dat://
- H.323, Packet-Based Multimedia Communications System
- IMAP, Internet Message Access Protocol
- IRC, Internet Relay Chat
- IPFS, InterPlanetary File System
- Kademlia
- LDAP, Lightweight Directory Access Protocol
- LPD, Line Printer Daemon Protocol
- MIME (S-MIME), Multipurpose Internet Mail Extensions and Secure MIME
- Modbus
- MQTT Protocol
- Netconf
- NFS, Network File System
- NIS, Network Information Service
- NNTP, Network News Transfer Protocol
- NTCIP, National Transportation Communications for Intelligent Transportation System Protocol
- NTP, Network Time Protocol
- OSCAR, AOL Instant Messenger Protocol
- POP, Post Office Protocol
- PNRP, Peer Name Resolution Protocol
- RDP, Remote Desktop Protocol
- RELP, Reliable Event Logging Protocol
- RFB, Remote Framebuffer Protocol
- Rlogin, Remote Login in UNIX Systems
- RPC, Remote Procedure Call
- RTMP, Real Time Messaging Protocol
- RTP, Real-time Transport Protocol
- RTPS, Real Time Publish Subscribe
- RTSP, Real Time Streaming Protocol
- SAP, Session Announcement Protocol
- SDP, Session Description Protocol
- SIP, Session Initiation Protocol
- SLP, Service Location Protocol
- SMB, Server Message Block
- SMTP, Simple Mail Transfer Protocol
- SNTP, Simple Network Time Protocol
- SSH, Secure Shell
- SSMS, Secure SMS Messaging Protocol
- TCAP, Transaction Capabilities Application Part
- TDS, Tabular Data Stream
- Tor (anonymity network)
- Tox
- TSP, Time Stamp Protocol
- VTP, Virtual Terminal Protocol
- Whois (and RWhois), Remote Directory Access Protocol
- WebDAV
- WebRTC
- WebSocket
- X.400, Message Handling Service Protocol
- X.500, Directory Access Protocol (DAP)
- XMPP, Extensible Messaging and Presence Protocol
- Z39.50
