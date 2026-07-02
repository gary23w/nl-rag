---
title: "Object identifier"
source: https://en.wikipedia.org/wiki/Object_identifier
domain: snmp
license: CC-BY-SA-4.0
tags: snmp, simple network management protocol, management information base, object identifier
fetched: 2026-07-02
---

# Object identifier

In computing, **object identifiers** or **OIDs** are an identifier mechanism standardized by the International Telecommunication Union (ITU) and ISO/IEC for naming any object, concept, or "thing" with a globally unambiguous persistent name.

## Syntax and lexicon

An OID corresponds to a node in the "OID tree" or hierarchy, which is formally defined using the ITU's OID standard, X.660. The root of the tree contains the following three arcs:

- 0: ITU-T
- 1: ISO
- 2: joint-iso-itu-t

Each node in the tree is represented by a series of integers separated by periods, corresponding to the path from the root through the series of ancestor nodes, to the node. Thus, an OID denoting Intel Corporation appears as follows,

1.3.6.1.4.1.343

and corresponds to the following path through the OID tree:

- 1 ISO
- 1.3 identified-organization (ISO/IEC 6523),
- 1.3.6 DoD,
- 1.3.6.1 internet,
- 1.3.6.1.4 private,
- 1.3.6.1.4.1 IANA enterprise numbers,
- 1.3.6.1.4.1.343 Intel Corporation

A textual representation of the OID paths is also commonly seen; for example,

- iso.identified-organization.dod.internet.private.enterprise.intel

Each node in the tree is controlled by an assigning authority, which may define child nodes under the node and delegate assigning authority for the child nodes. Continuing with the example, the node numbers under root node "1" are assigned by ISO; the nodes under "1.3.6" are assigned by the US Department of Defense; the nodes under "1.3.6.1.4.1" are assigned by IANA; the nodes under "1.3.6.1.4.1.343" are assigned by Intel Corporation, and so forth.

## Usage

- ISO/IEC 6523 "International Code Designator" uses OIDs with the prefix "1.3".
- In computer security, OIDs serve to name almost every object type in X.509 certificates, such as components of Distinguished Names, CPSs, etc.
- Within X.500 and LDAP schemas and protocols, OIDs uniquely name each attribute type and object class, and other elements of schema.
- In Simple Network Management Protocol (SNMP), each node in a management information base (MIB) is identified by an OID.
- IANA assigns Private Enterprise Numbers (PEN) to companies and other organizations under the 1.3.6.1.4.1 node. OIDs down-tree from these are among the most commonly seen; for example, within SNMP MIBs, as LDAP attributes, and as vendor suboptions in the Dynamic Host Configuration Protocol (DHCP).
- In the United States, HL7 International, a standards-developing organization in the area of electronic health care data exchange, is the assigning authority at the 2.16.840.1.113883 (joint-iso-itu-t.country.us.organization.hl7) node. HL7 maintains its own OID registry, and as of December 1, 2020 it contained almost 20,000 nodes, most of them under the HL7 root.
- DICOM uses OIDs.
- The Centers for Disease Control and Prevention uses OIDs to manage the many complex values sets or "vocabularies" used in the Public Health Information Network (PHIN) Vocabulary Access and Distribution System (VADS).
- Slovakia assigns each Identifikačné číslo organizácie (also called IČO) an OID under the 1.3.158 node. Each legal or natural person has an allocated IČO and thus an allocated OID node.

## Acquisition

There are multiple ways to acquire a OID. Both free and paid ones exist.

- Free registration with [IANA] below *1.3.6.1.4.1* (ASN.1-Notation *{iso(1) identified-organization(3) dod(6) internet(1) private(4) enterprise(1)}*).
- Below of *2.25* (ASN.1-Notation *{joint-iso-itu-t(2) uuid(25)}*) a self generated UUID can be used.
- At national agencies. Like e.g. for the health sector BfArM in Germany[1], BMSGPK in Austria[2] or de:Refdata in Switzerland[3].
- At any organization that already has an OID and decides to sub allocate them.
