---
title: "Fast Healthcare Interoperability Resources"
source: https://en.wikipedia.org/wiki/Fast_Healthcare_Interoperability_Resources
domain: fhir-health
license: CC-BY-SA-4.0
tags: fhir standard, health interoperability, hl7 fhir, electronic health record
fetched: 2026-07-02
---

# Fast Healthcare Interoperability Resources

The **Fast Healthcare Interoperability Resources** (**FHIR**, /faɪər/, like *fire*) is a technical standard by HL7 International for health information exchange. It is designed for a wide range of settings and with different health care information systems. The standard describes data formats and elements (known as "resources") and an API (application programming interface) for exchanging electronic health records (EHR).

FHIR builds on previous data format standards from HL7, like HL7 version 2.x and HL7 version 3.x. But it is easier to implement because it uses a modern web-based suite of API technology, including a REST protocol, and a choice of JSON, XML or RDF for data representation. One of its goals is to facilitate interoperability between legacy health care systems, to make it easier to provide health care information to health care providers and individuals on a wide variety of devices, from computers to tablets to cell phones, and to allow third-party application developers to provide medical applications which can be easily integrated into existing systems.

FHIR provides an alternative to document-centric approaches by directly exposing discrete data elements as services. For example, basic elements of healthcare like patients, admissions, diagnostic reports and medications can each be retrieved and manipulated via their own resource URLs.

## Standardization

| Date | Version | Description |
|---|---|---|
| 2011-08-18 | - | The initial draft of FHIR, then known as Resources For Healthcare (RFH), was published on Grahame Grieve's blog in Australia |
| 2011-09-11 | - | The standard was adopted by Health Level Seven International (HL7) as a work item |
| 2014-09-30 | 0.082 | DSTU1 (First Draft Standard for Trial Use) official version published |
| 2015-10-24 | 1.0.2 | DSTU2 (Second Draft Standard for Trial Use) official version published |
| 2019-10-24 | 3.0.1 | STU3 (Third Standard for Trial Use) included coverage of a variety of clinical workflows, a Resource Description Framework format, and a variety of other updates |
| 2019-10-30 | 4.0.1 | Release 4 has the First Normative Content and Trial Use Developments |
| 2023-03-26 | 5.0.0 | Release 5 |

## Architecture

FHIR is organized by resources (e.g., patient, observation). Such resources can be specified further by defining FHIR profiles (for example, binding to a specific terminology). A collection of profiles can be published as an implementation guide (IG), such as The U.S. Core Data for Interoperability (USCDI). The ONC anticipates finalizing USCDI v4 in July 2023.

Because FHIR is implemented on top of HTTPS, FHIR resources can be retrieved and parsed by analytics platforms for real-time data gathering. In this concept, healthcare organizations would be able to gather real-time data from specified resource models. FHIR resources can be streamed to a data store where they can be correlated with other informatics data. Potential use cases include epidemic tracking, prescription drug fraud, adverse drug interaction warnings, and the reduction of emergency room wait times.

## Analytics

In 2025, an international working group with contributors from CSIRO, Google, Microsoft Research, Harvard Medical School, and Health Samurai published the SQL on FHIR specification in *npj Digital Medicine*. The specification defines an implementation-agnostic method for producing tabular views of FHIR resources using FHIRPath expressions, intended to address performance and complexity issues encountered when querying large FHIR datasets in their native JSON or XML formats.

The specification was validated by replicating a clinical study using two independent implementations — Pathling, developed by CSIRO, and Aidbox, developed by Health Samurai — over a dataset of approximately 580 million FHIR resources, producing identical results across both runners.

## Implementations

Globally, a number of high-profile players in the health care informatics field are showing interest in and experimenting with FHIR, including CommonWell Health Alliance and SMART (Substitutable Medical Applications, Reusable Technologies).

Open source implementations of FHIR data structures, servers, clients and tools include reference implementations from HL7 in a variety of languages, SMART on FHIR, HAPI-FHIR in Java, and many others (see reference).

A variety of applications were demonstrated at the FHIR Applications Roundtable in July 2016. The Sync for Science (S4S) profile builds on FHIR to help medical research studies ask for (and if approved by the patient, receive) patient-level electronic health record data.

In January, 2018, Apple announced that its iPhone Health App would allow viewing a user's FHIR-compliant medical records when providers choose to make them available. Johns Hopkins Medicine, Cedars-Sinai, Penn Medicine, NYU-Langone Medical Center, Dignity Health and other large hospital systems participated at launch.

### United States

In 2014, the U.S. Health IT Policy and the Health IT Standards committees endorsed recommendations for more public (open) APIs. The U.S. JASON task force report on "A Robust Health Data Infrastructure" says that FHIR is currently the best candidate API approach, and that such APIs should be part of stage 3 of the "meaningful use" criteria of the U.S. Health Information Technology for Economic and Clinical Health Act. In December 2014, a broad cross-section of US stakeholders committed to the Argonaut Project which will provide acceleration funding and political will to publish FHIR implementation guides and profiles for query/response interoperability and document retrieval by May 2015. It would then be possible for medical records systems to migrate from the current practice of exchanging complex Clinical Document Architecture (CDA) documents, and instead exchange sets of simpler, more modular and interoperable FHIR JSON objects. The initial goal was to specify two FHIR profiles that are relevant to the Meaningful Use requirements, along with an implementation guide for using OAuth 2.0 for authentication.

A collaboration agreement with Healthcare Services Platform Consortium (now called Logica) was announced in 2017. Experiences with developing medical applications using FHIR to link to existing electronic health record systems clarified some of the benefits and challenges of the approach, and with getting clinicians to use them.

In 2020, the U.S. Centers for Medicare & Medicaid Services (CMS) issued their *Interoperability and Patient Access final rule,* (CMS-9115-F), based on the 21st Century Cures Act. The rule requires the use of FHIR by a variety of CMS-regulated payers, including Medicare Advantage organizations, state Medicaid programs, and qualified health plans in the Federally Facilitated Marketplace by 2021. Specifically, the rule requires FHIR APIs for Patient Access, Provider Directory and Payer-to-Payer exchange.

Proposed rules from CMS, such as the patient burden and prior authorization proposed rule (CMS-9123-P), further specify FHIR adoption for payer-to-payer exchange. The CMS rules and Office of the National Coordinator for Health IT (ONC) Cures Act Final rule (HHS-ONC-0955-AA01) work in concert to drive FHIR adoption within their respective regulatory authorities.

Further, other agencies are using existing rule-making authority, not derived from the Cures Act, to harmonize the regulatory landscape and ease FHIR adoption. For example, the U.S. Department of Health and Human Services (HHS) Office of Civil Rights (OCR) has proposed to update the HIPAA privacy rule (HHS–OCR–0945–AA00) with an expanded right of access for personal health apps and disclosures between providers for care coordination. Unlike the CMS and ONC final rules, the OCR HIPAA privacy proposed rule is not specific to FHIR; however, OCR's emphasize on standards-based APIs clearly benefits FHIR adoption.

### Brazil

In 2020, Brazil's Ministry of Health, by the IT Department of the SUS, started one of the world's largest platforms for national health interoperability, called the National Health Data Network, which uses HL7 FHIR r4 as a standard in all its information exchanges.

### Israel

In 2020, Israel's Ministry of Health began working towards the goal of promoting accessibility of information to patients and caregivers through the adoption of the FHIR standard in health organizations in Israel. Its first act was to create the IL-CORE work team to adapt the necessary components for localization and regulation in the health system in Israel. The ministry, in cooperation with the Nonprofit Organization 8400, created the FHIR IL community, whose purpose is to encourage the adoption of the standard in the Israeli healthcare system while cooperating with healthcare organizations and the industry. As part of a joint activity of the Ministry and 8400, a number of projects were launched for the implementation of FHIR in health management organizations (HMO) and hospitals, alongside other projects that are being independently promoted by healthcare organizations. In addition, the Ministry of Health allocated budgets to the HMOs and other organizations for the purpose of establishing organizational FHIR infrastructure. In the 2020 Eli Hurvitz Conference on Economy and Society, run by the Israel Democracy Institute it was estimated that the cost of implementing central FHIR modules of in the Israeli healthcare system is estimated at about 400 million NIS over 5 years. In 2023, the Israeli government began a legislative process to promote the sharing of information between organizations in the Israeli health ecosystem for the benefit of the patient, with an emphasis on patient empowerment and reduced information blocking. The proposed legislation also refers to the need to standardize the data by adopting the FHIR standard and utilizing standard terminologies, such as SNOMED-CT, both in source systems and in the data exchange process. The sharing of information will be with the patient's consent, and this consent will be given according to data buckets.
