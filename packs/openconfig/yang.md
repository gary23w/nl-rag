---
title: "YANG"
source: https://en.wikipedia.org/wiki/YANG
domain: openconfig
license: CC-BY-SA-4.0
tags: openconfig models, vendor-neutral yang, streaming telemetry, declarative config
fetched: 2026-07-02
---

# YANG

**Yet Another Next Generation** (**YANG**, /jæŋ/) is a data modeling language for the definition of data sent over network management protocols such as the NETCONF and RESTCONF. Developed and maintained by the NETMOD working group in the Internet Engineering Task Force (IETF), YANG was initially published as RFC 6020 in October 2010, with a significant update to version 1.1 in August 2016 (RFC 7950).

YANG enables comprehensive network automation by providing a standardized way to model the configuration and state data of network elements. The language can be used to define the format of event notifications emitted by network devices and allows data modelers to define the signature of RPCs that can be invoked on network elements via the NETCONF protocol. Being protocol-independent, YANG models can be converted into various encoding formats, including XML, JSON, and CBOR, depending on the network configuration protocol's support.

YANG is a modular language and represents data structures in a hierarchical tree format. It includes numerous built-in data types, with the capability for users to derive additional application-specific types. More complex reusable data structures can be represented as "groupings," which promote model reusability and consistency. YANG data models can use XPath expressions to define constraints on the elements of a YANG data model, enabling validation of configuration data before it is committed to devices.

YANG has become the de facto standard for modeling network device configurations across the telecommunications industry and is widely supported by major network equipment manufacturers. It plays a crucial role in software-defined networking (SDN) and network function virtualization (NFV) environments by providing a consistent interface for programmatic network management.

## History

Many network management protocols have associated data modeling languages. The first widely deployed Internet standard for network management was the Simple Network Management Protocol (SNMP). The data modeling language associated with SNMP was called the Structure of Management Information (SMI). The SMI language itself was based on the 1988 version of the Abstract Syntax Notation One (ASN.1). The current version of the SMI language, SMIv2 defined in RFC 2578, 2579 and 2580, has developed into an extended subset of ASN.1.

In the late 1990s, a project was started to create a replacement for SMIv2, which was called SMIng. One motivation was to decouple SMIng from the management protocol SNMP and to give SMIng a syntactic structure that is both easy to parse for computer programs and easy to learn for people familiar with programming languages that use a C-like notation. While the SMIng project did not succeed in the IETF, the SMIng specifications were published as experimental documents in May 2004 (RFC 3780, 3781).

Soon after the development of the NETCONF protocol in the IETF, it became clear that a data modeling language was needed to define data models manipulated by the NETCONF protocol. A design team created a proposal that became the basis of the YANG language. The syntactic structure and the base type system was essentially borrowed from SMIng. However, based on the lessons learned from the SMIng project, no attempts were made to make the YANG protocol neutral. Instead, YANG ties into concepts of the NETCONF protocol, such as the assumption that data model instances can be serialized into XML. Standardization of YANG started with the formation of the NETMOD working group in April 2008. The YANG 1.0 specification was published as RFC 6020 in October 2010. Recently, the NETMOD working group has been working on YANG 1.1, which has been published in August 2016 in RFC 7950.

## Example

The following YANG module `example-sports` shows a data model for team sports. The module declares a namespace and a prefix and imports the type library module `ietf-yang-types` before defining the type `season`. It then defines a container `sports` that includes a list of `person`s and a list of `team`s. A team has a list of players that reference persons via the `leafref` type and its `path` restriction.

```mw
module example-sports {

  namespace "http://example.com/example-sports";
  prefix sports;

  import ietf-yang-types { prefix yang; }

  typedef season {
    type string;
    description
      "The name of a sports season, including the type and the year, e.g,
       'Champions League 2014/2015'.";
  }

  container sports {
    config true;

    list person {
      key "name";
      leaf name { type string; }
      leaf birthday { type yang:date-and-time; mandatory true; }
    }

    list team {
      key "name";
      leaf name { type string; }
      list player {
        key "name season";
        unique number;
        leaf name { type leafref { path "/sports/person/name"; }  }
        leaf season { type season; }
        leaf number { type uint16; mandatory true; }
        leaf scores { type uint16; default 0; }
      }
    }
  }
}
```

### JSON encoding

The code block below shows the JSON representation of an instantiation of the `example-sports` data model.

```mw
{
  "example-sports:sports": {
    "person": [
      {
        "name": "Lionel Andrés Messi",
        "birthday": "1987-06-24T00:00:00-00:00"
      },
      {
        "name": "Cristiano Ronaldo",
        "birthday": "1985-02-05T00:00:00-00:00"
      }
    ],
    "team": [
      {
        "name": "FC Barcelona",
        "player": [
          {
            "name": "Lionel Andrés Messi",
            "season": "Champions League 2014/2015",
            "number": 10,
            "scores": 43
          }
        ]
      },
      {
        "name": "Real Madrid",
        "player": [
          {
            "name": "Cristiano Ronaldo",
            "season": "Champions League 2014/2015",
            "number": 7,
            "scores": 48
          }
        ]
      }
    ]
  }
}
```

### XML encoding

The code block below shows the XML representation of an instantiation of the `example-sports` data model.

```mw
<data xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">

  <sports xmlns="http://example.com/example-sports">
    <person>
      <name>Lionel Andrés Messi</name>
      <birthday>1987-06-24T00:00:00-00:00</birthday>
    </person>
    <person>
      <name>Cristiano Ronaldo</name>
      <birthday>1985-02-05T00:00:00-00:00</birthday>
    </person>
    <team>
      <name>FC Barcelona</name>
      <player>
        <name>Lionel Andrés Messi</name>
        <season>Champions League 2014/2015</season>
        <number>10</number>
        <scores>43</scores>
      </player>
    </team>
    <team>
      <name>Real Madrid</name>
      <player>
        <name>Cristiano Ronaldo</name>
        <season>Champions League 2014/2015</season>
        <number>7</number>
        <scores>48</scores>
      </player>
    </team>
  </sports>

</data>
```

## Documentation

### Language specifications and architectural documents

The following Request for Comments (RFCs) define the YANG language and some basic extensions:

- RFC 6020: YANG - A Data Modeling Language for the Network Configuration Protocol (NETCONF)
- RFC 6110: Mapping YANG to Document Schema Definition Languages and Validating NETCONF Content
- RFC 7950: The YANG 1.1 Data Modeling Language [does not replace RFC 6020]
- RFC 7951: JSON Encoding of Data Modeled with YANG
- RFC 7952: Defining and Using Metadata with YANG
- RFC 8342: Network Management Datastore Architecture (NMDA)
- RFC 8525: YANG Library [obsoletes RFC 7895]
- RFC 8528: YANG Schema Mount
- RFC 8791: YANG Data Structure Extensions
- RFC 9254: Encoding of Data Modeled with YANG in the Concise Binary Object Representation (CBOR)
- RFC 9595: YANG Schema Item iDentifier (YANG SID)

### Guidelines and supporting documentation

The following requests for comments provide guidelines and supporting documentation:

- RFC 9907: Guidelines for Authors and Reviewers of Documents Containing YANG Data Models [obsoletes RFC 8407]
- RFC 8199: YANG Module Classification
- RFC 8340: YANG Tree Diagrams
- RFC 8969: A Framework for Automating Service and Network Management with YANG
- RFC 9195: A File Format for YANG Instance Data
- RFC 9890: An Update to YANG Module Names Registration

## IETF usage

### Standards-track protocol specifications

The following requests for comments define standards-track protocols that are (partially) defined using YANG modules:

- RFC 6241: Network Configuration Protocol (NETCONF)
- RFC 6243: With-defaults Capability for NETCONF
- RFC 6470: Network Configuration Protocol (NETCONF) Base Notifications
- RFC 8040: RESTCONF Protocol
- RFC 8071: NETCONF Call Home and RESTCONF Call Home
- RFC 8072: YANG Patch Media Type
- RFC 8341: Network Configuration Access Control Model [obsoletes RFC 6536]
- RFC 8526: NETCONF Extensions to Support the Network Management Datastore Architecture
- RFC 8527: RESTCONF Extensions to Support the Network Management Datastore Architecture
- RFC 8572: Secure Zero Touch Provisioning (SZTP)
- RFC 8639: Subscription to YANG Notifications
- RFC 8640: Dynamic Subscription to YANG Events and Datastores over NETCONF
- RFC 8641: Subscription to YANG Notifications for Datastore Updates
- RFC 8650: Dynamic Subscription to YANG Events and Datastores over RESTCONF

### Standards-track data models

The following RFCs define standards-track YANG data models:

- RFC 6022: YANG Module for NETCONF Monitoring
- RFC 6643: Translation of Structure of Management Information Version 2 (SMIv2) MIB Modules to YANG Modules
- RFC 6728: Configuration Data Model for the IP Flow Information Export (IPFIX) and Packet Sampling (PSAMP) Protocols
- RFC 7224: IANA Interface Type YANG Module
- RFC 7317: A YANG Data Model for System Management
- RFC 7407: A YANG Data Model for SNMP Configuration
- RFC 8177: YANG Data Model for Key Chains
- RFC 8194: A YANG Data Model for LMAP Measurement Agents
- RFC 8294: Common YANG Data Types for the Routing Area
- RFC 8299: YANG Data Model for L3VPN Service Delivery
- RFC 8343: A YANG Data Model for Interface Management [obsoletes RFC 7223]
- RFC 8344: A YANG Data Model for IP Management [obsoletes RFC 7277]
- RFC 8345: A YANG Data Model for Network Topologies
- RFC 8346: A YANG Data Model for Layer 3 Topologies
- RFC 8347: A YANG Data Model for the Virtual Router Redundancy Protocol (VRRP)
- RFC 8348: A YANG Data Model for Hardware Management
- RFC 8349: A YANG Data Model for Routing Management (NMDA Version) [obsoletes RFC 8022]
- RFC 8366: A Voucher Artifact for Bootstrapping Protocols
- RFC 8431: A YANG Data Model for the Routing Information Base (RIB)
- RFC 8466: A YANG Data Model for Layer 2 Virtual Private Network (L2VPN) Service Delivery
- RFC 8512: A YANG Module for Network Address Translation (NAT) and Network Prefix Translation (NPT)
- RFC 8513: A YANG Data Model for Dual-Stack Lite (DS-Lite)
- RFC 8519: YANG Data Model for Network Access Control Lists (ACLs)
- RFC 8520: Manufacturer Usage Description Specification
- RFC 8529: YANG Data Model for Network Instances
- RFC 8530: YANG Model for Logical Network Elements
- RFC 8531: Generic YANG Data Model for Connection-Oriented Operations, Administration, and Maintenance (OAM) Protocols
- RFC 8532: Generic YANG Data Model for the Management of Operations, Administration, and Maintenance (OAM) Protocols That Use Connectionless Communications
- RFC 8533: A YANG Data Model for Retrieval Methods for the Management of Operations, Administration, and Maintenance (OAM) Protocols That Use Connectionless Communication
- RFC 8542: A YANG Data Model for Fabric Topology in Data-Center Networks
- RFC 8561: A YANG Data Model for Microwave Radio Link
- RFC 8575: YANG Data Model for the Precision Time Protocol (PTP)
- RFC 8632: A YANG Data Model for Alarm Management
- RFC 8652: A YANG Data Model for the Internet Group Management Protocol (IGMP) and Multicast Listener Discovery (MLD)
- RFC 8675: A YANG Data Model for Tunnel Interface Types
- RFC 8676: YANG Modules for IPv4-in-IPv6 Address plus Port (A+P) Softwires
- RFC 8695: A YANG Data Model for the Routing Information Protocol (RIP)
- RFC 8776: Common YANG Data Types for Traffic Engineering
- RFC 8795: YANG Data Model for Traffic Engineering (TE) Topologies
- RFC 8808: A YANG Data Model for Factory Default Settings
- RFC 8916: A YANG Data Model for the Multicast Source Discovery Protocol (MSDP)
- RFC 8944: A YANG Data Model for Layer 2 Network Topologies
- RFC 8960: A YANG Data Model for MPLS Base
- RFC 8819: YANG Module Tags
- RFC 9020: YANG Data Model for Segment Routing
- RFC 9061: A YANG Data Model for IPsec Flow Protection Based on Software-Defined Networking (SDN)
- RFC 9067: A YANG Data Model for Routing Policy
- RFC 9070: YANG Data Model for MPLS LDP
- RFC 9093: A YANG Data Model for Layer 0 Types
- RFC 9094: A YANG Data Model for Wavelength Switched Optical Networks (WSONs)
- RFC 9108: YANG Types for DNS Classes and Resource Record Types
- RFC 9166: A YANG Data Model for Internet Group Management Protocol (IGMP) and Multicast Listener Discovery (MLD) Snooping
- RFC 9179: A YANG Grouping for Geographic Locations
- RFC 9181: A Common YANG Data Model for Layer 2 and Layer 3 VPNs
- RFC 9196: YANG Modules Describing Capabilities for Systems and Datastore Update Notifications
- RFC 9243: A YANG Data Model for DHCPv6 Configuration
- RFC 9249: A YANG Data Model for NTP
- RFC 9291: A YANG Network Data Model for Layer 2 VPNs
- RFC 9314: YANG Data Model for Bidirectional Forwarding Detection (BFD)
- RFC 9128: YANG Data Model for Protocol Independent Multicast (PIM)
- RFC 9129: YANG Data Model for the OSPF Protocol
- RFC 9130: YANG Data Model for the IS-IS Protocol
- RFC 9194: A YANG Module for IS-IS Reverse Metric
- RFC 9348: A YANG Data Model for IP Traffic Flow Security
- RFC 9363: A YANG Data Model for Static Context Header Compression (SCHC)
- RFC 9375: A YANG Data Model for Network and VPN Service Performance Monitoring
- RFC 9398: A YANG Data Model for Internet Group Management Protocol (IGMP) and Multicast Listener Discovery (MLD) Proxy Devices
- RFC 9403: A YANG Data Model for RIB Extensions
- RFC 9408: A YANG Network Data Model for Service Attachment Points (SAPs)
- RFC 9418: A YANG Data Model for Service Assurance
- RFC 9472: A YANG Data Model for Reporting Software Bills of Materials (SBOMs) and Vulnerability Information
- RFC 9587: YANG Data Model for OSPFv3 Extended Link State Advertisements (LSAs)
- RFC 9617: A YANG Data Model for In Situ Operations, Administration, and Maintenance
- RFC 9633: Deterministic Networking (DetNet) YANG Data Model
- RFC 9640: YANG Data Types and Groupings for Cryptography
- RFC 9641: A YANG Data Model for a Truststore
- RFC 9642: A YANG Data Model for a Keystore
- RFC 9643: YANG Groupings for TCP Clients and TCP Servers
- RFC 9644: YANG Groupings for SSH Clients and SSH Servers
- RFC 9645: YANG Groupings for TLS Clients and TLS Servers
- RFC 9646: Conveying a Certificate Signing Request (CSR) in a Secure Zero-Touch Provisioning (SZTP)
- RFC 9647: A YANG Data Model for Babel
- RFC 9648: YANG Data Model for TCP
- RFC 9656: A YANG Data Model for Microwave Topology
- RFC 9684: A YANG Data Model for Challenge-Response-Based Remote Attestation (CHARRA) Procedures Using Trusted Platform Modules (TPMs)
- RFC 9702: YANG Data Model for Maximum Segment Identifier (SID) Depth (MSD) Types and MPLS MSD
- RFC 9719: YANG Data Model for Routing in Fat Trees (RIFT)
- RFC 9731: A YANG Data Model for Virtual Network (VN) Operations
- RFC 9742: A YANG Data Model for Syslog Management
- RFC 9826: A YANG Data Model for the Path Computation Element Communication Protocol (PCEP)
- RFC 9833: A Common YANG Data Model for Attachment Circuits
- RFC 9834: YANG Data Models for Bearers and Attachment Circuits as a Service (ACaaS)
- RFC 9835: A Network YANG Data Model for Attachment Circuits
- RFC 9836: A YANG Data Model for Augmenting VPN Service and Network Models with Attachment Circuits
- RFC 9902: A YANG Data Model for IS-IS Segment Routing over the MPLS Data Plane
- RFC 9903: A YANG Data Model for OSPF Segment Routing over the MPLS Data Plane
- RFC 9899: Extensions to the YANG Data Model for Access Control Lists (ACLs)
- RFC 9911: Common YANG Data Types [obsoletes RFC 6991]
- RFC 9922: A Common YANG Data Model for Scheduling
- RFC 9950: A YANG Data Model for Terminal Access Controller Access-Control System Plus (TACACS+) [obsoletes RFC 9105]

### Experimental specifications

The following requests for comments are experimental specifications that use or extend YANG:

- RFC 6095: Extending YANG with Language Abstractions
- RFC 7758: Time Capability in NETCONF
