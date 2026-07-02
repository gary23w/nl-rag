---
title: "HL7 - Wikipedia"
source: https://en.wikipedia.org/wiki/Health_Level_7
domain: electronic-health-informatics
license: CC-BY-SA-4.0
tags: electronic health record, health informatics, clinical data standard, health information exchange
fetched: 2026-07-02
---

# HL7

(Redirected from

Health Level 7

)

**Health Level Seven** (**HL7**) is a set of technical standards for health information exchange between software applications. The name is a reference to the 7th layer, the application layer, in the OSI model. The standards are produced by HL7 International, an international standards organization, and are adopted by other standards-issuing bodies such as American National Standards Institute and International Organization for Standardization.

## Purpose

Health organizations typically have many different computer systems used to process different patient administration or clinical tasks, such as billing, medication management, patient tracking, and documentation. All of these systems should communicate, or "interface", with each other when they receive new information or when they wish to retrieve information. HL7 International specifies a number of flexible standards, guidelines, and methodologies by which these healthcare systems can communicate with each other. The standards allow for easier 'interoperability' of healthcare data as it is shared and processed uniformly and consistently by the different systems. This allows clinical and non-clinical data to be shared more easily, theoretically improving patient care and health system performance.

## Standards

HL7 International considers the following standards to be its primary standards – those standards that are most commonly used and implemented:

- Version 2.x Messaging Standard – an interoperability specification for health and medical transactions
- Version 3 Messaging Standard – an interoperability specification for health and medical transactions
- Clinical Document Architecture (CDA) – an exchange model for clinical documents, based on HL7 Version 3
- Continuity of Care Document (CCD) – a US specification for the exchange of medical summaries, based on CDA.
- Structured Product Labeling (SPL) – the published information that accompanies a medicine, based on HL7 Version 3
- Clinical Context Object Workgroup (CCOW) – an interoperability specification for the visual integration of user applications

Other HL7 standards/methodologies include:

- Fast Healthcare Interoperability Resources (FHIR) – a standard for the exchange of resources
- Arden Syntax – a grammar for representing medical conditions and recommendations as a Medical Logic Module (MLM)
- Claims Attachments – a Standard Healthcare Attachment to augment another healthcare transaction
- Functional Specification of Electronic Health Record (EHR) and Personal Health Record (PHR) systems – a standardized description of health and medical functions sought for or available in such software applications
- GELLO – a standard expression language used for clinical decision support

### Version 2

The HL7 version 2 standard (also known as Pipehat) supports the day-to-day workflow of a hospital: administrative tasks, billing, logistics, and clinical processes such as orders and results. It was first released in 1987 and has been revised regularly since, producing more than ten versions (2.1 through 2.9). The v2.x versions are backward compatible with one another, so a message built to version 2.3 will still be understood by an application that supports version 2.6.

Unlike newer HL7 standards, version 2.x messages are written as plain delimited text rather than XML. A message is built up in four nested layers, each separated from the next by its own punctuation character:

- **Segments** each segment occupies one line and begins with a three-character code identifying what it contains (for example, *PID* for patient identification, or *PV1* for patient visit details). Every message opens with an *MSH* segment, which states the message type; this determines which other segments are expected to follow.
- **Fields** a segment is split into fields by the pipe character (`|`). For instance, one field of the PID segment holds the patient's name.
- **Components** a field can be split further into components by a caret (`^`), so a name field can hold separate components for family name, given name, and so on.
- **Subcomponents** components can in turn be split by an ampersand (`&`) where even finer detail is needed.

Two further characters round out the syntax: a tilde (`~`) marks repeated values within a field, and since HL7v2.7 a number sign (`#`) is the default truncation character.

The example below is an admission message. `MSH` is the header; `PID` carries the patient's identity; `PV1` carries details of the visit. In the PID segment, the patient's name field contains three components separated by carets, family name (`KLEINSAMPLE`), given name (`BARRY`) and middle initial (`Q`), illustrating the field/component split described above.

```
MSH|^~\&|MegaReg|XYZHospC|SuperOE|XYZImgCtr|20060529090131-0500||ADT^A01^ADT_A01|01052901|P|2.5
EVN||200605290901||||
PID|||56782445^^^UAReg^PI||KLEINSAMPLE^BARRY^Q^JR||19620910|M||2028-9^^HL70005^RA99113^^XYZ|260 GOODWIN CREST DRIVE^^BIRMINGHAM^AL^35209^^M~NICKELL'S PICKLES^10000 W 100TH AVE^BIRMINGHAM^AL^35200^^O|||||||0105I30001^^^99DEF^AN
PV1||I|W^389^1^UABH^^^^3||||12345^MORGAN^REX^J^^^MD^0010^UAMC^L||67890^GRAINGER^LUCY^X^^^MD^0010^UAMC^L|MED|||||A0||13579^POTTER^SHERMAN^T^^^MD^0010^UAMC^L|||||||||||||||||||||||||||200605290900
OBX|1|NM|^Body Height||1.80|m^Meter^ISO+|||||F
OBX|2|NM|^Body Weight||79|kg^Kilogram^ISO+|||||F
AL1|1||^ASPIRIN
DG1|1||786.50^CHEST PAIN, UNSPECIFIED^I9|||A
```

This flexibility has allowed HL7 v2.x to interconnect a wide range of hospital systems, from patient administration to electronic health records to specialised laboratory and radiology systems, and it remains supported by every major health informatics vendor in the United States.

### Version 3

The HL7 version 3 standard has the aim to support all healthcare workflows. Development of version 3 started around 1995, resulting in an initial standard publication in 2005. The v3 standard, as opposed to version 2, is based on a formal methodology (the HDF) and object-oriented principles.

**RIM - ISO/HL7 21731**

The Reference Information Model (RIM) is the cornerstone of the HL7 Version 3 development process and an essential part of the HL7 V3 development methodology. RIM expresses the data content needed in a specific clinical or administrative context and provides an explicit representation of the semantic and lexical connections that exist between the information carried in the fields of HL7 messages.

**HL7 Development Framework - ISO/HL7 27931**

The HL7 Version 3 Development Framework (HDF) is a continuously evolving process that seeks to develop specifications that facilitate interoperability between healthcare systems. The HL7 RIM, vocabulary specifications, and model-driven process of analysis and design combine to make HL7 Version 3 one methodology for the development of consensus-based standards for healthcare information systems interoperability. The HDF is the most current edition of the HL7 V3 development methodology.

The HDF not only documents messaging, but also the processes, tools, actors, rules, and artifacts relevant to the development of all HL7 standard specifications. Eventually, the HDF will encompass all of the HL7 standard specifications, including any new standards resulting from the analysis of electronic health record architectures and requirements.

HL7 specifications draw upon codes and vocabularies from a variety of sources. The V3 vocabulary work ensures that the systems implementing HL7 specifications have an unambiguous understanding of the code sources and code value domains they are using.

**V3 Messaging**

The HL7 version 3 messaging standard defines a series of Secure Text messages (called *interactions*) to support all healthcare workflows.

HL7 v3 messages are based on an XML encoding syntax, as shown in this example:

```mw
<POLB_IN224200 ITSVersion="XML_1.0" xmlns="urn:hl7-org:v3"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
  <id root="2.16.840.1.113883.19.1122.7" extension="CNTRL-3456"/>
  <creationTime value="200202150930-0400"/>
  <!-- The version of the datatypes/RIM/vocabulary used is that of May 2006 -->
  <versionCode code="2006-05"/>
  <!-- interaction id= Observation Event Complete, w/o Receiver Responsibilities -->
  <interactionId root="2.16.840.1.113883.1.6" extension="POLB_IN224200"/>
  <processingCode code="P"/>
  <processingModeCode nullFlavor="OTH"/>
  <acceptAckCode code="ER"/>
  <receiver typeCode="RCV">
    <device classCode="DEV" determinerCode="INSTANCE">
      <id extension="GHH LAB" root="2.16.840.1.113883.19.1122.1"/>
      <asLocatedEntity classCode="LOCE">
        <location classCode="PLC" determinerCode="INSTANCE">
          <id root="2.16.840.1.113883.19.1122.2" extension="ELAB-3"/>
        </location>
      </asLocatedEntity>
    </device>
  </receiver>
  <sender typeCode="SND">
    <device classCode="DEV" determinerCode="INSTANCE">
      <id root="2.16.840.1.113883.19.1122.1" extension="GHH OE"/>
      <asLocatedEntity classCode="LOCE">
        <location classCode="PLC" determinerCode="INSTANCE">
          <id root="2.16.840.1.113883.19.1122.2" extension="BLDG24"/>
        </location>
      </asLocatedEntity>
    </device>
  </sender>
  <!-- Trigger Event Control Act & Domain Content -->
</POLB_IN224200>
```

### Clinical Document Architecture

The HL7 Clinical Document Architecture (CDA) is an XML-based markup standard intended to specify the encoding, structure and semantics of clinical documents for exchange. The standard was jointly published with ISO as ISO/HL7 27932.

### Continuity of Care Document

The Continuity of Care Document framework is a US-specific standard for the exchange of medical summaries, based on the Clinical Document Architecture standard.

### Structured Product Labeling

Structured Product Labeling describes the published information that accompanies a medicine, based on HL7 Version 3.

### Clinical Context Object Workgroup

CCOW, or "Clinical Context Object Workgroup," is a standard protocol designed to enable disparate applications to share user context and patient context in real-time, and at the user-interface level. CCOW implementations typically require a CCOW vault system to manage user security between applications.

### Fast Healthcare Interoperability Resources (FHIR)

Fast Healthcare Interoperability Resources is a modern interoperability specification from HL7 International designed to be easier to implement, more open, and more extensible than HL7 versions 2.x or 3.x. It leverages a modern web-based suite of API technology, including a HTTP-based RESTful protocol, HTML and Cascading Style Sheets for user interface integration, a choice of JSON or XML for data representation, OAuth for authorization and Atom for query results. The main purpose of the FHIR standard is to ensure interoperability between different computer systems. It defines the data format and protocol for exchanging medical information, regardless of how it is stored in these systems.

### Services Aware Interoperability Framework

The HL7 Services-Aware Enterprise Architecture Framework (SAIF) provides consistency between all HL7 artifacts, and enables a standardized approach to Enterprise Architecture (EA) development and implementation, and a way to measure the consistency.

SAIF is a way of thinking about producing specifications that explicitly describe the governance, conformance, compliance, and behavioral semantics that are needed to achieve computable semantic working interoperability. The intended information transmission technology might use a messaging, document exchange, or service approach.

SAIF is the framework that is required to rationalize interoperability of other standards. SAIF is an architecture for achieving interoperability, but it is not a whole-solution design for enterprise architecture management.

### Arden syntax

The Arden syntax is a language for encoding medical knowledge. HL7 International adopted and oversees the standard beginning with Arden syntax 2.0. These Medical Logic Modules (MLMs) are used in the clinical setting as they can contain sufficient knowledge to make single medical decisions. They can produce alerts, diagnoses, and interpretations along with quality assurance function and administrative support. An MLM must run on a computer that meets the minimum system requirements and has the correct program installed. Then, the MLM can give advice for when and where it is needed.

### Clinical Quality Language

**Clinical Quality Language** (CQL) is a ANSI certified clinically focused high-level expression language standard curated by Health Level 7. It is designated for clinical knowledge sharing in the domains of electronic clinical quality measurement and clinical decision support.

Clinical quality language is being used for a variety of clinical applications including WHO SMART guidelines where it is used for encoding decision logic and performance indicators. The Centers for Medicare & Medicaid Services adopted CQL for clinical quality measure specifications since 2019.

CQL allows modular and flexible expression of logic and is both human-readable and machine processable.

An implementation of CQL was open sourced and published by the National Committee for Quality Assurance in 2023 with the aim of encouraging adoption of the language.

### MLLP

### Functional EHR and PHR specifications

Functional specifications for an electronic health record.

## Message details

### The OBR segment

An OBR Segment carries information about an exam, diagnostic study/observation. It is a required segment in an ORM (order message) or an ORU (Observation Result) message.
