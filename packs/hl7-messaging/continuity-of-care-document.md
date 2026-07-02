---
title: "Continuity of Care Document"
source: https://en.wikipedia.org/wiki/Continuity_of_Care_Document
domain: hl7-messaging
license: CC-BY-SA-4.0
tags: hl7 messaging, hl7 v2, clinical document, health message exchange
fetched: 2026-07-02
---

# Continuity of Care Document

The **Continuity of Care Document** (**CCD**) specification is an XML-based markup standard intended to specify the encoding, structure, and semantics of a patient summary clinical document for exchange.

## Structure

The CCD specification is a constraint on the HL7 Clinical Document Architecture (CDA) standard. The CDA specifies that the content of the document consists of a mandatory textual part (which ensures human interpretation of the document contents) and optional structured parts (for software processing). The structured part is based on the HL7 Reference Information Model (RIM) and provides a framework for referring to concepts from coding systems, such as SNOMED or LOINC.

The patient summary contains a core data set of the most relevant administrative, demographic, and clinical information facts about a patient's healthcare, covering one or more healthcare encounters. It provides a means for one healthcare practitioner, system, or setting to aggregate all of the pertinent data about a patient and forward it to another practitioner, system, or setting to support the continuity of care. Its primary use case is to provide a snapshot in time containing the pertinent clinical, demographic, and administrative data for a specific patient.

The CCD specification contains U.S. specific requirements; its use is therefore limited to the U.S. The U.S. Healthcare Information Technology Standards Panel has selected the CCD as one of its standards. CCDs are quickly becoming one of the most ubiquitous and thorough means of transferring health data on patients as each can contain vast amounts of data based on the standard format, in a relatively easy to use and portable file.

## Development history

CCD was developed by Health Level Seven International with consultation and advice from several members of ASTM E31, the technical committee responsible for development and maintenance of the Continuity of Care Record (CCR) standard. In the opinion of HL7 and its members, the CDA CCD combines the benefits of ASTMs Continuity of Care Record (CCR) and the HL7 Clinical Document Architecture (CDA) specifications. It is intended as an alternate implementation to the one specified in ASTM ADJE2369 for those institutions or organizations committed to implementation of the HL7 Clinical Document Architecture.

The public library is relatively limited of reference CCDs available for developers to examine how to encode medical data using the structure and format of the CCD. Not surprisingly, different electronic health record vendors have implemented the CCD standard in different and often incompatible ways. The National Institute of Standards and Technology (NIST) has produced a sample CCD with valid data that is available for public download.

## CCD and Stage 1 of meaningful use

As part of the first stage of U.S. federal incentives for the adoption of electronic health records, known as meaningful use, the CCD and Continuity of Care Record (CCR) were both selected as acceptable extract formats for clinical care summaries. To be certified for this federal program, an electronic health record must be able to generate a CCD (or equivalent CCR) that has the sections of allergies, medications, problems, and laboratory results, in addition to patient header information. Several of these sections also have mandated vocabularies, such as LOINC for laboratory results, according to the federal program.

When ambulatory and inpatient care providers attest that they have achieved the first stage of meaningful use, they document that they have tested their capability to "exchange clinical information and patient summary record", which is a core objective of the program. Most electronic health record vendors have adopted the CCD rather than the Continuity of Care Record since it is a newer format that harmonizes the Continuity of Care Record and the HL7 Clinical Document Architecture (CDA) specifications.

## CCD and Stage 2 of meaningful use

In the second stage of meaningful use, the CCD, but not the CCR, was included as part of the standard for clinical document exchange. The selected standard, known as the Consolidated Clinical Document Architecture (C-CDA) was developed by Health Level 7 and includes nine document types, one of which is an updated version of the CCD. The second stage of MEANINGFUL USE requires that healthcare providers use C-CDA document exchange regularly in care transitions and the CCD has been identified as the most appropriate document for this purpose. These documents must be capable of including data elements known as the "Common MU Data Set" that include: Patient name, sex, date of birth, race, ethnicity, preferred language, smoking status, problems, medications, medication allergies, laboratory tests, laboratory values/results, vital signs, care plan fields including goals and instructions, procedures and care team members. In addition encounter diagnoses, immunizations, referral reason and discharge instructions may be required based on context. Several tools for the development, testing, validation and implementation have been advanced to support CCD and C-CDA use in the second stage of meaningful use which has helped the standard mature in its capability to transmit data between care providers and for other purposes.

## Competing standards

CCD and Continuity of Care Record (CCR) are often seen as competing standards. Google Health supported a subset of CCR until the service was discontinued in January 2012. while Microsoft HealthVault claims to support a subset of both CCR and CCD.
