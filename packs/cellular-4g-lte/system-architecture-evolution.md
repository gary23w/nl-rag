---
title: "System Architecture Evolution"
source: https://en.wikipedia.org/wiki/System_Architecture_Evolution
domain: cellular-4g-lte
license: CC-BY-SA-4.0
tags: 4g lte, long term evolution, system architecture evolution, mobile broadband
fetched: 2026-07-02
---

# System Architecture Evolution

**System Architecture Evolution** (**SAE**) is the core network architecture of mobile communications protocol group 3GPP's LTE wireless communication standard.

SAE is the evolution of the GPRS Core Network, but with a simplified architecture; an all-IP Network (AIPN); support for higher throughput and lower latency radio access networks (RANs); and support for, and mobility between, multiple heterogeneous access networks, including E-UTRA (LTE and LTE Advanced air interface), and 3GPP legacy systems (for example GERAN or UTRAN, air interfaces of GPRS and UMTS respectively), but also non-3GPP systems (for example Wi-Fi, WiMAX or CDMA2000).

## SAE Architecture

The SAE has a flat, all-IP architecture with separation of control plane and user plane traffic.

The main component of the SAE architecture is the **Evolved Packet Core** (**EPC**), also known as **SAE Core**. The EPC will serve as the equivalent of GPRS networks (via the **Mobility Management Entity**, **Serving Gateway** and **PDN Gateway** subcomponents).

### Evolved Packet Core (EPC)

The subcomponents of the EPC are:

#### MME (Mobility Management Entity)

The MME is the key control-node for the LTE access-network. It is responsible for idle mode User Equipment (UE) paging and tagging procedure including retransmissions. It is involved in the bearer activation/deactivation process and is also responsible for choosing the Serving Gateway for a UE at the initial attach and at time of intra-LTE handover involving Core Network (CN) node relocation. It is responsible for authenticating the user (by interacting with the Home Subscriber Server). The Non Access Stratum (NAS) signaling terminates at the MME and it is also responsible for generation and allocation of temporary identities to UEs. It checks the authorization of the UE to camp on the service provider's Public Land Mobile Network (PLMN) and enforces UE roaming restrictions. The MME is the termination point in the network for ciphering/integrity protection for NAS signaling and handles the security key management. Lawful interception of signaling is also supported by the MME. The MME also provides the control plane function for mobility between LTE and 2G/3G access networks with the S3 interface terminating at the MME from the SGSN. The MME also terminates the S6a interface towards the HSS for roaming UEs.

#### SGW (Serving Gateway)

The Serving Gateway routes and forwards user data packets, while also acting as the mobility anchor for the user plane during inter-eNodeB handovers and as the anchor for mobility between LTE and other 3GPP technologies (terminating S4 interface and relaying the traffic between 2G/3G systems and Packet Data Network Gateway). For idle state User Equipment, the Serving Gateway terminates the downlink data path and triggers paging when downlink data arrives for the User Equipment. It manages and stores UE contexts, e.g. parameters of the IP bearer service, network internal routing information. It also performs replication of the user traffic in case of lawful interception.

#### PGW (Packet Data Network Gateway)

The Packet Data Network Gateway (PDN Gateway, also PGW) provides connectivity from the User Equipment (UE) to external packet data networks (PDNs) by being its point of exit and entry of traffic. A piece of User Equipment may have simultaneous connectivity with more than one Packet Data Network Gateway for accessing multiple packet data networks. The PDN Gateway performs policy enforcement, packet filtering for each user, charging support, lawful interception and packet screening. Another key role of the Packet Data Network Gateway is to act as the anchor for mobility between 3GPP and non-3GPP technologies such as WiMAX and 3GPP2 (CDMA 1X and EvDO).

#### HSS (Home Subscriber Server)

The Home Subscriber Server is a central database that contains user-related and subscription-related information. The functions of the HSS include mobility management, call and session establishment support, user authentication and access authorization. The HSS is based on pre-Rel-4 Home Location Register (HLR) and Authentication Center (AuC).

#### ANDSF (Access Network Discovery and Selection Function)

The ANDSF provides information to the UE about connectivity to 3GPP and non-3GPP access networks (such as Wi-Fi). The purpose of the ANDSF is to assist the UE to discover the access networks in their vicinity and to provide rules (policies) to prioritize and manage connections to these networks.

#### ePDG (Evolved Packet Data Gateway)

The main function of the ePDG is to secure the data transmission with a UE connected to the EPC over untrusted non-3GPP access, e.g. Wi-Fi calling (VoWiFi). For this purpose, the ePDG acts as a termination node of IPsec tunnels established with the UE.

## Non Access Stratum (NAS) protocols

The Non-Access Stratum (NAS) protocols form the highest stratum of the control plane between the user equipment (UE) and MME. NAS protocols support the mobility of the UE and the session management procedures to establish and maintain IP connectivity between the UE and a PDN GW. They define the rules for a mapping between parameters during inter-system mobility with 3G networks or non-3GPP access networks. They also provide the NAS security by integrity protection and ciphering of NAS signaling messages. EPS (Evolved Packet System) provides the subscriber with a "ready-to-use" IP connectivity and an "always-on" experience by linking between mobility management and session management procedures during the UE attach procedure.

Complete NAS transactions consist of specific sequences of elementary procedures with EPS Mobility Management (EMM) and EPS Session Management (ESM) protocols.

### EMM (EPS Mobility Management)

The EPS (Evolved Packet System) Mobility Management (EMM) protocol provides procedures for the control of mobility when the User Equipment (UE) uses the Evolved UMTS Terrestrial Radio Access Network (E-UTRAN). It also provides control of security for the NAS protocols.

EMM involves different types of procedures such as:

- *EMM common procedures* — can always be initiated while a NAS signalling connection exists. The procedures belonging to this type are initiated by the network. They include GUTI reallocation, authentication, security mode control, identification and EMM information.
- *EMM specific procedures* — specific to the UE only. At any time only one UE-initiated EMM specific procedure can run. The procedures belonging to this type are attach and combined attach, detach or combined detach, normal tracking area update and combined tracking area update (S1 mode only) and periodic tracking area update (S1 mode only).
- *EMM connection management procedures* — manage the connection of the UE with the network:
  - Service request: Initiated by the UE and used to establish a secure connection to the network or to request the resource reservation for sending data, or both.
  - Paging procedure: Initiated by the network and used to request the establishment of a NAS signalling connection or to prompt the UE to re-attach if necessary as a result of a network failure.
  - Transport of NAS messages: Initiated by the UE or the network and used to transport SMS messages.
  - Generic transport of NAS messages: Initiated by the UE or the network and used to transport protocol messages from other applications.

The UE and the network execute the attach procedure, the default EPS bearer context activation procedure in parallel. During the EPS attach procedure the network activates a default EPS bearer context. The EPS session management messages for the default EPS bearer context activation are transmitted in an information element in the EPS mobility management messages. The UE and network complete the combined default EPS bearer context activation procedure and the attach procedure before the dedicated EPS bearer context activation procedure is completed. The success of the attach procedure is dependent on the success of the default EPS bearer context activation procedure. If the attach procedure fails, then the ESM session management procedures also fails.

### ESM (EPS Session Management)

The EPS Session Management (ESM) protocol provides procedures for the handling of EPS bearer contexts. Together with the bearer control provided by the Access Stratum, it provides the control of user plane bearers. The transmission of ESM messages is suspended during EMM procedures except for the attach procedure.

*EPS Bearer:* Each EPS bearer context represents an EPS bearer between the UE and a PDN. EPS bearer contexts can remain activated even if the radio and S1 bearers constituting the corresponding EPS bearers between UE and MME are temporarily released. An EPS bearer context can be either a default option bearer context or a dedicated bearer context. A default EPS bearer context is activated when the UE requests a connection to a PDN. The first default EPS bearer context, is activated during the EPS attach procedure. Additionally, the network can activate one or several dedicated EPS bearer contexts in parallel.

Generally, ESM procedures can be performed only if an EMM context has been established between the UE and the MME, and the secure exchange of NAS messages has been initiated by the MME by use of the EMM procedures. Once the UE is successfully attached, the UE can request the MME to set up connections to additional PDNs. For each additional connection, the MME activates a separate default EPS bearer context. A default EPS bearer context remains activated throughout the lifetime of the connection to the PDN.

Types of ESM procedures: ESM involves different types of procedures such as:

- *EPS bearer contexts procedures* — initiated by the network and are used for the manipulation of EPS bearer contexts, including Default EPS bearer context activation, Dedicated EPS bearer context activation, EPS bearer context modification, EPS bearer context deactivation.
- *Transaction related procedures* — initiated by the UE to request for resources, i.e. a new PDN connection or dedicated bearer resources, or to release these resources. They include PDN connectivity procedure, PDN disconnect procedure, Bearer resource allocation procedure, Bearer resource modification procedure.

The MME maintains EMM context and EPS bearer context information for UEs in the ECM-IDLE, ECM CONNECTED and EMM-DEREGISTERED states.

## EPC protocol stack

### MME (Mobility Management Entity) protocols

**The MME protocol stack consists of:**

1. S1-MME stack to support S1-MME interface with eNodeB
2. S11 stack to support S11 interface with Serving Gateway

MME supports the S1 interface with eNodeB. The integrated S1 MME interface stack consists of IP, SCTP, S1AP.

- **SCTP (Stream Control Transmission Protocol)** is a common transport protocol that uses the services of Internet Protocol (IP) to provide a reliable datagram delivery service to the adaptation modules, such as the S1AP. SCTP provides reliable and sequenced delivery on top of the existing IP framework. The main features provided by SCTP are:
  - *Association setup*: An association is a connection that is set up between two endpoints for data transfer, much like a TCP connection. A SCTP association can have multiple addresses at each end.
  - *Reliable Data Delivery*: Delivers sequenced data in a stream (Elimination of head-of-line blocking): SCTP ensures the sequenced delivery of data with multiple unidirectional streams, without blocking the chunks of data in other direction.
- **S1AP (S1 Application Part)** is the signaling service between E-UTRAN and the Evolved Packet Core (EPC) that fulfills the S1 Interface functions such as SAE Bearer management functions, Initial context transfer function, Mobility functions for UE, Paging, Reset functionality, NAS signaling transport function, Error reporting, UE context release function, Status transfer.

MME supports S11 interface with Serving Gateway. The integrated S11 interface stack consists of IP, UDP, eGTP-C.

### SGW (Serving Gateway) protocols

The SGW consists of

1. S11 control plane stack to support S11 interface with MME
2. S5/S8 control and data plane stacks to support S5/S8 interface with PGW
3. S1 data plane stack to support S1 user plane interface with eNodeB
4. S4 data plane stack to support S4 user plane interface between RNC of UMTS and SGW of eNodeB
5. Sxa: since 3GPP Rel.14, the Sx interface and the associated PFCP protocol was added to the SGW, allowing for the Control User Plane Separation between SGW-C and SGW-U.

SGW supports S11 interface with MME and S5/S8 interface with PGW. The integrated control plane stack for these interfaces consists of IP, UDP, eGTP-C.

SGW supports the S1-U interface with eNodeB and S5/S8 data plane interface with PGW. The integrated data plane stack for these interfaces consists of IP, UDP, eGTP-U.

### PGW (Packet Data Network Gateway) protocols

Main interfaces supported by the P-GW are:

1. S5/S8: this interface is defined between S-GW and P-GW. It is named S5 when the S-GW and the P-GW are located in the same network (non-roaming scenario) and S8 when the S-GW is located in the visited network and the P-GW in the home network (roaming scenario). eGTP-C and GTP-U protocols are used in the S5/S8 interface.
2. Gz: this interface is used by the P-GW to communicate with the Offline Charging System (OFCS), mainly to send the Charging Data Records (CDRs) of the post-paid users via FTP.
3. Gy: this interface is used by the P-GW to communicate with the Online Charging System (OCS). The P-GW informs the charging system about pre-paid users payload in real time. Diameter protocol is used in the Gy interface.
4. Gx: this interface is used by the P-GW to communicate with the Policy and Charging Rules Function (PCRF) in order to handle Policy and Charging Rules (PCC) rules. These rules contain charging related information as well as quality of service (QoS) parameters that will be used in the bearer establishment. Diameter protocol is used in the Gx interface.
5. SGi: this interface is defined between the P-GW and external networks, for example, Internet access, corporate access, etc.
6. Sxb: since 3GPP Rel.14, the Sx interface and the associated PFCP protocol was added to the PGW, allowing for the Control User Plane Separation between PGW-C and PGW-U.

## Support of voice services and SMS

The EPC is a packet-only core network. It does not have a circuit-switched domain, which is traditionally used for phone calls and SMS.

### Support for Voice services in EPC

3GPP specified two solutions for voice:

- **IMS**: A solution for IMS Voice over IP was specified in Rel-7.
- **Circuit-Switched fallback (CSFB)**: in order to make or receive calls, the UE changes its radio access technology from LTE to a 2G/3G technology that supports circuit-switched services. This feature requires 2G/3G coverage. A new interface (called SGs) between the MME and the MSC is required. This feature was developed in Rel-8.

### Support for SMS services in EPC

3GPP specified three solutions for SMS:

- **IMS**: A solution for SMS over IP was specified in Rel-7.
- **SMS over SGs**: this solution requires the SGs interface introduced during the work on CSFB. SMS are delivered in the Non Access Stratum over LTE. There is no inter-system change for sending or receiving SMS. This feature was specified in Rel-8.
- **SMS over SGd**: this solution requires the SGd Diameter interface at the MME and delivers SMS in the Non Access Stratum over LTE, without requiring the fully signaling neither the legacy MSC doing CSFB, nor the overhead associated with the IMS signaling and the associated EPC bearer management.

CSFB and SMS over SGs are seen as interim solutions, the long term being IMS.

## Multiple access networks

The UE can connect to the EPC using several access technologies. These access technologies are composed of:

- **3GPP accesses**: these access technologies are specified by the 3GPP. They include GPRS, UMTS, EDGE, HSPA, LTE and LTE Advanced.
- **non-3GPP accesses**: these access technologies are not specified by the 3GPP. They include technologies such as cdma2000, WiFi or fixed networks. 3GPP specifies two classes of non-3GPP access technologies with different security mechanisms:
  - *trusted accesses*, that the network operator consider trustable from a security stand point (for example: a cdma2000 network). Trusted non-3GPP accesses interface directly with the network.
  - *untrusted accesses*, that the network operator doesn't consider trustable from a security stand point (for example, a connection over a public WiFi hotspot). Untrusted non-3GPP accesses are connected to the network via an ePDG, which provide additional security mechanisms (IPsec tunneling).

It is up to the network operator to decide whether a non-3GPP access technology is trusted or untrusted.

It is worth noting that these trusted/untrusted categories do not apply to 3GPP accesses.

## 3GPP releases

The 3GPP delivers standards in parallel releases, which compose consistent sets of specifications and features.

| Version | Released | Info |
|---|---|---|
| **Release 7** | 2007 Q4 | Feasibility study on All-IP Network (AIPN) |
| **Release 8** | 2008 Q4 | **First release of EPC**. SAE specification: high level functions, support of LTE and other 3GPP accesses, support of non-3GPP accesses, inter-system mobility, Single Radio Voice Call Continuity (SRVCC), CS fallback. Earthquake and Tsunami Warning System (ETWS). Support of Home Node B / Home eNode B. |
| **Release 9** | 2009 Q4 | LCS control plane for EPS. Support of IMS emergency calls over GPRS and EPS. Enhancements to Home Node B / Home eNode B. Public Warning System (PWS). |
| **Release 10** | 2011 Q1 | Network improvements for machine-type communications. Various offload mechanisms (LIPA, SIPTO, IFOM). |
| **Release 11** | 2012 Q3 | Further improvements for machine-type communications. Simulation of USSD in IMS. QoS control based on subscriber spending limits. Further improvements to LIPA and SIPTO. Single Radio Video Call Continuity (vSRVCC). Single Radio Voice Call Continuity from UTRAN/GERAN to HSPA/E-UTRAN (rSRVCC). Support of interworking with Broadband Forum accesses. |
| **Release 12** | 2015 Q1 | Enhanced Small Cells operation, Carrier Aggregation (2 uplink carriers, 3 downlink carriers, FDD/TDD carrier aggregation), MIMO (3D channel modelling, elevation beamforming, massive MIMO), MTC - UE Cat 0 introduced, D2D communication, eMBMS enhancements. |
| **Release 13** | 2016 Q1 | Introduced LTE-U / LTE-LAA, LTE-M, Elevation beamforming / Full Dimension MIMO, Indoor positioning, LTE-M Cat 1.4 MHz & Cat 200 kHz |
| ... |   |   |
| **Release 18** |   | https://www.3gpp.org/release18 |
