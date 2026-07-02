---
title: "Clinical Document Architecture"
source: https://en.wikipedia.org/wiki/Clinical_Document_Architecture
domain: hl7-messaging
license: CC-BY-SA-4.0
tags: hl7 messaging, hl7 v2, clinical document, health message exchange
fetched: 2026-07-02
---

# Clinical Document Architecture

**Clinical Document Architecture** (**CDA**) is a technical standard by HL7 International. It uses XML to specify the encoding, structure and semantics of health data for health information exchange. Release 1.0 was published in November 2000 and Release 2.0 in 2005.

## Content

CDA specifies the syntax and supplies a framework for specifying the full semantics of a clinical document, defined by six characteristics:

1. Persistence
2. Stewardship
3. Potential for authentication
4. Context
5. Wholeness
6. Human readability

CDA can hold any kind of clinical information that would be included in a patient's medical record; examples include:

- Discharge summary (following inpatient care)
- History & physical
- Specialist reports, such as those for medical imaging or pathology

An XML element in a CDA supports unstructured text, as well as links to composite documents encoded in pdf, docx, or rtf, as well as image formats like jpg and png.

It was developed using the HL7 Development Framework (HDF) and it is based on the HL7 Reference Information Model (RIM) and the HL7 Version 3 Data Types.

The CDA specifies that the content of the document consists of a mandatory textual part (which ensures human interpretation of the document contents) and optional structured parts (for software processing). The structured part relies on coding systems (such as from SNOMED and LOINC) to represent concepts.

## Consolidated Clinical Document Architecture

In 2012, in response to conflicting CDAs in use by the healthcare industry, the Office of the National Coordinator for Health Information Technology (ONC) streamlined commonly used templates to create the Consolidated-CDA (C-CDA).

## Transport

The CDA standard doesn't specify how the documents should be transported. CDA documents can be transported using HL7 version 2 messages, HL7 version 3 messages, IHE protocols such as XDS, as well as by other mechanisms including: DICOM, MIME attachments to email, http or ftp.

## Standard certification and adoption

The standard is certified by ANSI.

CDA Release 2 has been adopted as an ISO standard, ISO/HL7 27932:2009.

## Country-specific implementations

### Australia

Australia's Personally Controlled Electronic Health Record (PCEHR), known as "My Health Record", uses a specialized implementation of HL7 CDA Release 2.

### United Kingdom

In the UK the Interoperability Toolkit (ITK) utilises the "CDA R2 from HL7 V3 – for CDA profiles" for the Correspondence pack.

### United States

In the U.S. the CDA standard is probably best known as the basis for the Continuity of Care Document (CCD) specification, based on the data model as specified by ASTM's Continuity of Care Record. The U.S. Healthcare Information Technology Standards Panel has selected the CCD as one of its standards.
