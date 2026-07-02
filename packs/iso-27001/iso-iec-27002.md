---
title: "ISO/IEC 27002"
source: https://en.wikipedia.org/wiki/ISO/IEC_27002
domain: iso-27001
license: CC-BY-SA-4.0
tags: iso 27001, iso 27002 controls, information security management, isms certification, common criteria evaluation
fetched: 2026-07-02
---

# ISO/IEC 27002

**ISO/IEC 27002** is an information security standard published by the International Organization for Standardization (ISO) and by the International Electrotechnical Commission (IEC), titled *Information security, cybersecurity and privacy protection — Information security controls*.

The ISO/IEC 27000 family of standards are descended from a corporate security standard donated by Shell to a UK government initiative in the early 1990s. The Shell standard was developed into British Standard BS 7799 in the mid-1990s, and was adopted as ISO/IEC 17799 in 2000. The ISO/IEC standard was revised in 2005, and renumbered ISO/IEC 27002 in 2007 to align with the other ISO/IEC 27000-series standards. It was revised again in 2013 and in 2022. Later in 2015 the ISO/IEC 27017 was created from that standard in order to suggest additional security controls for the cloud which were not completely defined in ISO/IEC 27002.

ISO/IEC 27002 provides best practice recommendations on information security controls for use by those responsible for initiating, implementing or maintaining information security management systems (ISMS). Information security is defined within the standard in the context of the CIA triad:

the preservation of

confidentiality

(ensuring that information is accessible only to those authorized to have access),

integrity

(safeguarding the accuracy and completeness of information and processing methods) and

availability

(ensuring that authorized users have access to information and associated assets when required)

.

## Outline

### Outline for ISO/IEC 27002:2022

The standard starts with 4 introductory chapters:

1. Scope
2. Normative Reference
3. Terms, definitions, and abbreviated terms
4. Structure of this document

These are followed by 4 main chapters:

1. Organizational controls
2. People controls
3. Physical controls
4. Technological controls

### Outline for ISO/IEC 27002:2013

The standard starts with 5 introductory chapters:

1. Introduction
2. Scope
3. Normative references
4. Terms and definitions
5. Structure of this standard

These are followed by 14 main chapters:

1. Information Security Policies
2. Organization of Information Security
3. Human Resource Security
4. Asset Management
5. Access Control
6. Cryptography
7. Physical and environmental security
8. Operation Security- procedures and responsibilities, Protection from malware, Backup, Logging and monitoring, Control of operational software, Technical vulnerability management and Information systems audit coordination
9. Communication security - Network security management and Information transfer
10. System acquisition, development and maintenance - Security requirements of information systems, Security in development and support processes and Test data
11. Supplier relationships - Information security in supplier relationships and Supplier service delivery management
12. Information security incident management - Management of information security incidents and improvements
13. Information security aspects of business continuity management - Information security continuity and Redundancies
14. Compliance - Compliance with legal and contractual requirements and Information security reviews

### Controls

Within each chapter, information security controls and their objectives are specified and outlined. The information security controls are generally regarded as best practice means of achieving those objectives. For each of the controls, implementation guidance is provided.

Specific controls are not mandated since:

1. Each organization is expected to undertake a structured information security risk assessment process to determine its specific requirements before selecting controls that are appropriate to its particular circumstances. The introduction section outlines a risk assessment process although there are more specific standards covering this area such as ISO/IEC 27005. The use of information security risk analysis to drive the selection and implementation of information security controls is an important feature of the ISO/IEC 27000-series standards: it means that the generic good practice advice in this standard gets tailored to the specific context of each user organization, rather than being applied by rote. Not all of the 39 control objectives are necessarily relevant to every organization for instance, hence entire categories of control may not be deemed necessary. The standards are also open ended in the sense that the information security controls are 'suggested', leaving the door open for users to adopt alternative controls if they wish, just so long as the key control objectives relating to the mitigation of information security risks, are satisfied. This helps keep the standard relevant despite the evolving nature of information security threats, vulnerabilities and impacts, and trends in the use of certain information security controls.
2. It is practically impossible to list all conceivable controls in a general purpose standard. Industry-specific implementation guidelines for ISO/IEC 27001:2013 and ISO/IEC 27002 offer advice tailored to organizations in the telecomms industry (see ISO/IEC 27011) and healthcare (see ISO 27799).

Most organizations implement a wide range of information security-related controls, many of which are recommended in general terms by ISO/IEC 27002. Structuring the information security controls infrastructure in accordance with ISO/IEC 27002 may be advantageous since it:

- Is associated with a well-respected international standard
- Helps avoid coverage gaps and overlaps
- Is likely to be recognized by those who are familiar with the ISO/IEC standard

## Implementation example of ISO/IEC 27002

Here are a few examples of typical information security policies and other controls relating to three parts of ISO/IEC 27002. (Note: this is merely an illustration. The list of example controls is incomplete and not universally applicable.)

### Physical and Environmental security

- Physical access to premises and support infrastructure (communications, power, air conditioning etc.) must be monitored and restricted to prevent, detect and minimize the effects of unauthorized and inappropriate access, tampering, vandalism, criminal damage, theft etc.
- The list of people authorized to access secure areas must be reviewed and approved periodically (at least once a year) by Administration or Physical Security Department, and cross-checked by their departmental managers.
- Photography or video recording is forbidden inside Restricted Areas without prior permission from the designated authority.
- Suitable video surveillance cameras must be located at all entrances and exits to the premises and other strategic points such as Restricted Areas, recorded and stored for at least one month, and monitored around the clock by trained personnel.
- Access cards permitting time-limited access to general and/or specific areas may be provided to trainees, vendors, consultants, third parties and other personnel who have been identified, authenticated, and authorized to access those areas.
- Other than in public areas such as the reception foyer, and private areas such as rest rooms, visitors should be escorted at all times by an employee while on the premises.
- The date and time of entry and departure of visitors along with the purpose of visits must be recorded in a register maintained and controlled by Site Security or Reception.
- Everyone on site (employees and visitors) must wear and display their valid, issued pass at all times, and must present their pass for inspection on request by a manager, security guard or concerned employee.
- Access control systems must themselves be adequately secured against unauthorized/inappropriate access and other compromises.
- Fire/evacuation drills must be conducted periodically (at least once a year).
- Smoking is forbidden inside the premises other than in designated Smoking Zones.

### Human Resource security

- All employees must be screened prior to employment, including identity verification using a passport or similar photo ID and at least two satisfactory professional references. Additional checks are required for employees taking up trusted positions.
- All employees must formally accept a binding confidentiality or non-disclosure agreement concerning personal and proprietary information provided to or generated by them in the course of employment.
- Human Resources department must inform Administration, Finance and Operations when an employee is taken on, transferred, resigns, is suspended or released on long-term leave, or their employment is terminated.
- Upon receiving notification from HR that an employee's status has changed, Administration must update their physical access rights and IT Security Administration must update their logical access rights accordingly.
- An employee's manager must ensure that all access cards, keys, IT equipment, storage media and other valuable corporate assets are returned by the employee on or before their last day of employment.

### Access control

- User access to corporate IT systems, networks, applications and information must be controlled in accordance with access requirements specified by the relevant Information Asset Owners, normally according to the user's role.
- Generic or test IDs must not be created or enabled on production systems unless specifically authorized by the relevant Information Asset Owners.
- After a predefined number of unsuccessful logon attempts, security log entries and (where appropriate) security alerts must be generated and user accounts must be locked out as required by the relevant Information Asset Owners.
- Passwords or pass phrases must be lengthy and complex, consisting of a mix of letters, numerals and special characters that would be difficult to guess.
- Passwords or pass phrases must not be written down or stored in readable format.
- Authentication information such as passwords, security logs, security configurations and so forth must be adequately secured against unauthorized or inappropriate access, modification, corruption or loss.
- Privileged access rights typically required to administer, configure, manage, secure and monitor IT systems must be reviewed periodically (at least twice a year) by Information Security and cross-checked by the appropriate departmental managers.
- Users must either log off or password-lock their sessions before leaving them unattended.
- Password-protected screensavers with an inactivity timeout of no more than 10 minutes must be enabled on all workstations/PCs.
- Write access to removable media (USB drives, CD/DVD writers etc.) must be disabled on all desktops unless specifically authorized for legitimate business reasons.

## History

| Year | Description |   |
|---|---|---|
| 2005 | ISO/IEC 27002 (1st Edition) |   |
| 2013 | ISO/IEC 27002 (2nd Edition) |   |
| 2022 | ISO/IEC 27002 (3rd Edition) |   |

## National equivalent standards

ISO/IEC 27002 has directly equivalent national standards in several countries. Translation and local publication often results in several months' delay after the main ISO/IEC standard is revised and released, but the national standard bodies go to great lengths to ensure that the translated content accurately and completely reflects ISO/IEC 27002.

| Countries | Equivalent Standard |
|---|---|
| Argentina | IRAM-ISO-IEC 27002:2008 |
| Australia New Zealand | AS/NZS ISO/IEC 27002:2006 |
| Brazil | ABNT NBR ISO/IEC 27002:2022 |
| Indonesia | SNI ISO/IEC 27002:2014 |
| Chile | NCH2777 ISO/IEC 17799/2000 |
| China | GB/T 22081-2008 |
| Czech Republic | ČSN ISO/IEC 27002:2006 |
| Croatia | HRN ISO/IEC 27002:2013 |
| Denmark | DS/ISO27002:2022 (DK) |
| Estonia | EVS-ISO/IEC 17799:2003, 2005 version in translation |
| France | NF ISO/CEI 27002:2014 |
| Germany | DIN ISO/IEC 27002:2008 |
| Japan | JIS Q 27002 |
| Lithuania | LST ISO/IEC 27002:2009 (adopted ISO/IEC 27002:2005, ISO/IEC 17799:2005) |
| Mexico | NMX-I-27002-NYCE-2015 |
| Netherlands | NEN-ISO/IEC 27002:2013 |
| Peru | NTP-ISO/IEC 17799:2007 |
| Poland | PN-ISO/IEC 17799:2007, based on ISO/IEC 17799:2005 |
| Russia | ГОСТ Р ИСО/МЭК 27002-2012, based on ISO/IEC 27002:2005 |
| Slovakia | STN ISO/IEC 27002:2006 |
| South Africa | SANS 27002:2014/ISO/IEC 27002:2013 |
| Spain | UNE 71501 |
| Sweden | SS-ISO/IEC 27002:2014 |
| Turkey | TS ISO/IEC 27002 |
| Thailand | UNIT/ISO |
| Ukraine | ДСТУ ISO/IEC 27002:2015 |
| United Kingdom | BS ISO/IEC 27002:2005 |
| Uruguay | UNIT/ISO 17799:2005 |

## Certification

ISO/IEC 27002 is an advisory standard that is meant to be interpreted and applied to all types and sizes of organization according to the particular information security risks they face. In practice, this flexibility gives users a lot of latitude to adopt the information security controls that make sense to them, but makes it unsuitable for the relatively straightforward compliance testing implicit in most formal certification schemes.

ISO/IEC 27001:2013 (*Information technology – Security techniques – Information security management systems – Requirements*) is a widely recognized certifiable standard. ISO/IEC 27001 specifies a number of firm requirements for establishing, implementing, maintaining and improving an ISMS, and in Annex A there is a suite of information security controls that organizations are encouraged to adopt where appropriate within their ISMS. The controls in Annex A are derived from and aligned with ISO/IEC 27002.

## Ongoing development

Both ISO/IEC 27001 and ISO/IEC 27002 are revised by ISO/IEC JTC1/SC27 every few years in order to keep them current and relevant. Revision involves, for instance, incorporating references to other issued security standards (such as ISO/IEC 27000, ISO/IEC 27004 and ISO/IEC 27005) and various good security practices that have emerged in the field since they were last published. Due to the significant 'installed base' of organizations already using ISO/IEC 27002, particularly in relation to the information security controls supporting an ISMS that complies with ISO/IEC 27001, any changes have to be justified and, wherever possible, evolutionary rather than revolutionary in nature.
