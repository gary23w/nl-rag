---
title: "Management information base"
source: https://en.wikipedia.org/wiki/Management_information_base
domain: snmp
license: CC-BY-SA-4.0
tags: snmp, simple network management protocol, management information base, object identifier
fetched: 2026-07-02
---

# Management information base

A **management information base** (**MIB**) is a database used for managing the entities in a communication network. Most often associated with the Simple Network Management Protocol (SNMP), the term is also used more generically in contexts such as in OSI/ISO Network management model. While intended to refer to the complete collection of management information available on an entity, it is often used to refer to a particular subset, more correctly referred to as a MIB module.

Objects in the MIB are defined using a subset of Abstract Syntax Notation One (ASN.1) called "Structure of Management Information Version 2 (SMIv2)" RFC 2578. The software that performs the parsing is a MIB compiler.

The database is hierarchical (tree-structured) and each entry is addressed through an object identifier (OID). Internet documentation RFCs discuss MIBs, notably RFC 1155, "Structure and Identification of Management Information for TCP/IP based internets", and its two companions, RFC 1213, "Management Information Base for Network Management of TCP/IP-based internets", and RFC 1157, "A Simple Network Management Protocol".

## ASN.1

Abstract Syntax Notation One (ASN.1) is a standard and flexible notation that describes data structures for representing, encoding, transmitting, and decoding data. It provides a set of formal rules for describing the structure of objects that are independent of machine-specific encoding techniques and is a precise, formal notation that removes ambiguities.

ASN.1 is a joint ISO and ITU-T standard, originally defined in 1984 as part of CCITT X.409:1984. ASN.1 moved to its own standard, X.208, in 1988 due to its broader applicability. The substantially revised 1995 version is covered by the X.680 standards series.

An adapted subset of ASN.1, Structure of Management Information (SMI), is specified for use in SNMP to define sets of related MIB objects; these sets are termed MIB modules.

## MIB hierarchy

The MIB hierarchy can be depicted as a tree with a nameless root, the levels of which are assigned by different organizations. The top-level MIB OIDs belong to different standards organizations, while lower-level object IDs are allocated by associated organizations. This model permits management across all layers of the OSI reference model, extending into applications such as databases, email, and the Java reference model, as MIBs can be defined for all such area-specific information and operations.

A managed object (sometimes called a MIB object or object) is one of any number of specific characteristics of a managed device. Managed objects are made up of one or more object instances, which are essentially variables. An OID uniquely identifies a managed object in the MIB hierarchy.

Two types of managed objects exist:

- Scalar objects define a single object instance.
- Tabular objects define multiple related object instances that are grouped in MIB tables.

An example of a managed object is *`atInput`*, which is a scalar object that contains a single object instance, the integer value that indicates the total number of input AppleTalk packets on a router interface.

### SNMPv1 and SMI-specific data types

The first version of the Structure of Management Information (SMIv1) specifies the use of a number of SMI-specific data types, which are divided into two categories: simple data types and application-wide data types.

#### Simple data types

Three simple data types are defined in the SNMPv1 SMI:

- The *integer* data type is a signed integer in the range of −231 to 231−1.
- *Octet strings* are ordered sequences of 0 to 65,535 octets.
- *Object IDs* represent object identifiers that are allocated according to the rules specified in ASN.1.

#### Application-wide data types

The following application-wide data types exist in the SNMPv1 SMI:

- *Network addresses* represent addresses from a particular protocol family. SMIv1 supports only 32-bit (IPv4) addresses. SMIv2 uses Octet Strings to represent addresses generically, and thus are usable in SMIv1 too. SMIv1 had an explicit IPv4 address datatype.
- *Counters* are non-negative integers that increase until they reach a maximum value and then roll over to zero. SNMPv1 specifies a counter size of 32 bits.
- *Gauges* are non-negative integers that can increase or decrease between specified minimum and maximum values. Whenever the system property represented by the gauge is outside of that range, the value of the gauge itself will vary no further than the respective maximum or minimum, as specified in RFC 2578.
- *Time ticks* represent time since some event, measured in hundredths of a second.
- *Opaques* represent an arbitrary encoding that is used to pass arbitrary information strings that do not conform to the strict data typing used by the SMI.
- *Integers* represent signed integer-valued information. This data type redefines the integer data type, which has arbitrary precision in ASN.1 but bounded precision in the SMI.
- *Unsigned integers* represent unsigned integer-valued information, which is useful when values are always non-negative. This data type redefines the integer data type, which has arbitrary precision in ASN.1 but bounded precision in the SMI.

### SNMPv1 MIB tables

The SNMPv1 SMI defines highly structured tables that are used to group the instances of a tabular object (that is, an object that contains multiple variables). Tables are composed of zero or more rows, which are indexed in a way that allows an SNMP manager to retrieve or alter an entire row with a single `Get`, `GetNext`, or `Set` command.

### SMIv2

The second version of the SMI (SMIv2) is described in RFC 2578 and RFC 2579. It enhances and adds to the SMIv1-specific data types, such as including bit strings, network addresses, and counters. Bit strings are defined only in SMIv2 and comprise zero or more named bits that specify a value. Network addresses represent an address from a particular protocol family. Counters are non-negative integers that increase until they reach a maximum value and then return to zero. In SMIv1, a 32-bit counter size is specified. In SMIv2, 32-bit and 64-bit counters are defined.

SMIv2 also specifies information modules, which specify a group of related definitions. Three types of SMI information modules exist: MIB modules, compliance statements, and capability statements.

- MIB modules contain definitions of interrelated managed objects.
- Compliance statements provide a systematic way to describe a group of managed objects that must be implemented for conformance to a standard.
- Capability statements are used to indicate the precise level of support that an agent claims with respect to a MIB group. An NMS can adjust its behavior toward agents according to the capabilities statements associated with each agent.

## Updating MIB modules

MIB modules are occasionally updated to add new functionality, remove ambiguities and fix defects. These changes are made in conformance to section 10 of RFC 2578 and section 5 of RFC 2579. An example of a MIB module that has been updated many times is the important set of objects that was originally defined in RFC 1213, also known as "MIB-II". This MIB module has since been split up and can be found in MIB modules such as RFC 4293 "Management Information Base for the Internet Protocol (IP)", RFC 4022 "Management Information Base for the Transmission Control Protocol (TCP)", RFC 4113 "Management Information Base for the User Datagram Protocol (UDP)", RFC 2863 "The Interfaces Group MIB" and RFC 3418 "Management Information Base (MIB) for the Simple Network Management Protocol (SNMP)".

## Example

Example of MIB for SNMP RFC 3418

```mw
└── SNMPv2-MIB(.1.3.6.1.2.1)
  └── system(.1)
    ├── sysDescr (.1)
    ├── sysObjectID (.2)
    ├── sysUpTime (.3)
    ├── sysName (.5)
    ├── sysContact (.4)
    ├── sysLocation (.6)
    ├── sysServices (.7)
    ├── sysORLastChange (.8)
    └── sysORTable (.9)
      └── sysOREntry (.1)
        ├── sysORIndex (.1)
        ├── sysORID (.2)
        ├── sysORDescr (.3)
        └── sysORUpTime (.4)
```

To call the value of sysName one would use:

```mw
# snmpwalk 10.32.13.36 -v2c -c public sysName
SNMPv2-MIB::sysName.0 = STRING: SOME_HOSTNAME
```

or

```mw
# snmpwalk 10.32.13.36 -v2c -c public .1.3.6.1.2.1.1.5
SNMPv2-MIB::sysName.0 = STRING: SOME_HOSTNAME
```

or

```mw
# snmpwalk 10.32.13.36 -v2c -c public .1.3.6.1.2.1.1.5.0
SNMPv2-MIB::sysName.0 = STRING: SOME_HOSTNAME
```

## Index

There are a large number of MIBs defined by standards organizations like the IETF, private enterprises and other entities.

### IETF maintained

There are 318 RFCs in the first 5000 RFCs from the IETF that contain MIBs. This list is a mere fraction of the MIBs that have been written:

- **SNMP - SMI**: RFC 1155 — Defines the Structure of Management Information (SMI)
- **MIB-I**: RFC 1156 — Historically used with CMOT, not to be used with SNMP
- **SNMPv2-SMI**: RFC 2578 — Structure of Management Information Version 2 (SMIv2)
- **MIB-II**: RFC 1213 — Management Information Base for Network Management of TCP/IP-based internets
- **SNMPv2-MIB**: RFC 3418 — Management Information Base (MIB) for the Simple Network Management Protocol (SNMP)
- **TCP-MIB**: RFC 4022 — Management Information Base for the Transmission Control Protocol (TCP)
- **UDP-MIB**: RFC 4113 — Management Information Base for the User Datagram Protocol (UDP)
- **IP-MIB**: RFC 4293 — Management Information Base for the Internet Protocol (IP)
- **IF-MIB**: RFC 2863 — The Interfaces Group MIB
- **ENTITY-MIB**: RFC 4133 — Entity MIB (Version 3)
- **ENTITY-STATE-MIB**: RFC 4268 — Entity State MIB
- **ALARM-MIB**: RFC 3877 — Alarm Management Information Base (MIB)
- Fibre Channel
  - **FC-MGMT-MIB**: RFC 4044 Fibre Channel Management MIB
  - **FIBRE-CHANNEL-FE-MIB**: RFC 2837 Definitions of Managed Objects for the Fabric Element in Fibre Channel Standard
- **HPR-IP-MIB**: RFC 2584 — Definitions of Managed Objects for APPN/HPR in IP Networks

### IEEE maintained

The IETF and IEEE have agreed to move MIBs relating to IEEE work (for example, Ethernet and bridging) to their respective IEEE workgroup. This is in process and a few items are complete.

- Network bridge
  - IEEE 802.1ap-2008 consolidated the IEEE and IETF RFCs related to bridging networks into eight related MIBs.
- Management Information Base (MIB) Modules / IEEE 802.1
