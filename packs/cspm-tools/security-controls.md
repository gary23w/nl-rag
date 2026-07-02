---
title: "Security controls"
source: https://en.wikipedia.org/wiki/Security_controls
domain: cspm-tools
license: CC-BY-SA-4.0
tags: cspm tooling, cloud misconfiguration scanning, posture compliance checks, cloud attack surface, vulnerability posture assessment
fetched: 2026-07-02
---

# Security controls

**Security controls** or **security measures** are safeguards or countermeasures to avoid, detect, counteract, or minimize security risks to physical property, information, computer systems, or other assets. In the field of information security, such controls protect the confidentiality, integrity and availability of information.

Systems of controls can be referred to as frameworks or standards. Frameworks can enable an organization to manage security controls across different types of assets with consistency.

Security controls are to help reduce the likelihood or any impacts of security incidents and protect the CIA triad for the systems and the data. While protecting it helps organizations meet its responsibilities; consistent risk management to systems, assets, data, networks and physical infrastructures.

## Types of security controls

Security controls can be classified by various criteria. One approach is to classify controls by how/when/where they act relative to a security breach, sometimes termed as *control types*:

- ***Preventive controls*** are intended to prevent an incident from occurring e.g. by locking out unauthorized intruders; Sometimes known as firewalls or locked server rooms that restrict physical entry
- ***Detective controls*** are intended to identify, characterize, and log an incident e.g. isolating suspicious behavior from a malicious actor on a network or using network monitoring tolls to flag suspicious activity.;
- ***Compensating controls*** mitigate ongoing damages of an active incident, e.g. shutting down a system upon detecting malware
- After the event, *corrective controls* are intended to restore damage caused by the incident e.g. by recovering the organization to normal working status as efficiently as possible.

Security controls can also be classified according to the implementation of the control (sometimes termed *control categories*), for example:

- ***Physical controls*** - includes tangible items such as fences, doors, locks, CCTV systems and fire extinguishers;
- ***Procedural or administrative controls*** - e.g. incident response processes, management oversight, security awareness and training.
- ***Technical or logical control**s* - e.g. user authentication (login) and logical access controls, antivirus software, firewalls;
- ***Legal and regulatory or compliance controls*** - includes privacy laws, policies, regulations and clauses that help organizations handle and protect (e.g. HIPAA, GDPR).

These classifications help organizations build a well designed multi-layered defense strategy, ensuring that they layers help control and prevent when threats are being taken placed.

## Control effectiveness and Lifecycle

Security controls include both technical controls (such as access management and fire walls) and administrative controls (including policies and procedures).

Effective controls testing and verification process allows:

- Identifying safeguards are protecting confidentiality, integrity, and availability of assets.

- Detailed overview of any security posture of the service.

- Contribution to any mitigation plans that may be prioritized for reducing risks arising because of any weaknesses or failures of controls

Steps for assessment:

**Document security control implementation**: securing infrastructure, configuring components, identifying & access management, security polices

**Monitor & verifying security controls**: Usually manual or automated testing and it tests penetration, reviewing logs, vulnerability scanning, any surveys and interviews with staff, and more.

**Reporting test results**: Generating reports, metrics, trends

Controls are part of risk treatment strategy which is applied after risk assessment and then design, building, operating, and changing them is a part of the lifecycle.

## Purpose in organizations

University IT policy states that “Using a set of standardized controls allows IT security to ensure all University and Medical Center areas are protected from threats.”

**Controls in four basic categories:** Computer Controls, Data Protection, Network Protections, User Authentication

**Computer Controls:** Organizations may implement email protection, endpoint detection & response, centralized patch management, domain membership.

**Data Protection:** For protecting data organizations may equip full disk encryption and media destruction

**Network Protection:** Protecting the network is important from keeping information safe form unwanted users organizations may use flow monitoring, logging network & system activity, network border protections and prohibit firewall to be bypassed to reduce an attack.

**User Authentication:** Organizations may use two-factor authentication, may force users to change password annually, having only authorized account management, and Local admin password solution (LAPS).

## Information security standards and control frameworks

The **ISO/IEC 27000 series** standards promote good security practices and define frameworks or systems to structure the analysis and design for managing information security controls. Most recent version, ISO/IEC 27001;2022, released in October 2022, specifies 93 controls organized some of the most well known standards are outlined below.

### International Standards Organization

ISO/IEC 27001:2022 was released in October 2022. All organizations certified to ISO 27001:2013 are obliged to transition to the new version of the Standard within 3 years (by October 2025).

The 2022 version of the Standard specifies 93 controls in 4 groups:

- **A.5**: Organisational controls
- **A.6**: People controls
- **A.7**: Physical controls
- **A.8**: Technological controls

It groups these controls into operational capabilities as follows:

- Governance
- Asset management
- Information protection
- Human resource security
- Physical security
- System and network security
- Application security
- Secure configuration
- Identity and access management
- Threat and vulnerability management
- Continuity
- Supplier relationships security
- Legal and compliance
- Information security event management; and
- Information security assurance

The previous version of the Standard, ISO/IEC 27001, specified 114 controls in 14 groups:

- A.5: Information security policies
- A.6: How information security is organised
- A.7: Human resources security - controls that are applied before, during, or after employment.
- A.8: Asset management
- A.9: Access controls and managing user access
- A.10: Cryptographic technology
- A.11: Physical security of the organisation's sites and equipment
- A.12: Operational security
- A.13: Secure communications and data transfer
- A.14: Secure acquisition, development, and support of information systems
- A.15: Security for suppliers and third parties
- A.16: Incident management
- A.17: Business continuity/disaster recovery (to the extent that it affects information security)
- A.18: Compliance - with internal requirements, such as policies, and with external requirements, such as laws.

### U.S. Federal Government information security standards

The Federal Information Processing Standards (FIPS) apply to all US government agencies. However, certain national security systems, under the purview of the Committee on National Security Systems, are managed outside these standards.

**Federal information Processing Standard 200 (FIPS 200)**, "Minimum Security Requirements for Federal Information and Information Systems," specifies the minimum security controls for federal information systems and the processes by which risk-based selection of security controls occurs. The catalog of minimum security controls is found in NIST Special Publication SP 800-53.

FIPS 200 identifies 17 broad control families:

- AC Access Control
- AT Awareness and Training
- AU Audit and Accountability
- CA Security Assessment and Authorization (historical abbreviation)
- CM Configuration Management
- CP Contingency Planning
- IA Identification and Authentication
- IR Incident Response
- MA Maintenance
- MP Media Protection
- PE Physical and Environmental Protection
- PL Planning
- PS Personnel Security
- RA Risk Assessment
- SA System and Services Acquisition
- SC System and Communications Protection
- SI System and Information Integrity

National Institute of Standards and Technology

#### NIST Cybersecurity Framework

A maturity based framework divided into five functional areas and approximately 100 individual controls in its "core" and is widely used by U.S. organizations and government agencies.

#### NIST SP-800-53

A database of nearly one thousand technical controls grouped into families and cross references.

- Starting with Revision 3 of 800-53, Program Management controls were identified. These controls are independent of the system controls, but are necessary for an effective security program.
- Starting with Revision 4 of 800-53, eight families of privacy controls were identified to align the security controls with the privacy expectations of federal law.
- Starting with Revision 5 of 800-53, the controls also address data privacy as defined by the NIST Data Privacy Framework.

### Commercial Control Sets

#### COBIT5

A proprietary control set published by ISACA.

- Governance of Enterprise IT
  - Evaluate, Direct and Monitor (EDM) – 5 processes
- Management of Enterprise IT
  - Align, Plan and Organise (APO) – 13 processes
  - Build, Acquire and Implement (BAI) – 10 processes
  - Deliver, Service and Support (DSS) – 6 processes
  - Monitor, Evaluate and Assess (MEA) - 3 processes

#### CIS Controls (CIS 18)

Formerly known as the SANS Critical Security Controls now officially called the CIS Critical Security Controls (COS Controls). The CIS Controls are divided into 18 prioritized cybersecurity best practices that protect systems and data from threats.

- CIS Control 1: Inventory and Control of Enterprise Assets
- CIS Control 2: Inventory and Control of Software Assets
- CIS Control 3: Data Protection
- CIS Control 4: Secure Configuration of Enterprise Assets and Software
- CIS Control 5: Account Management
- CIS Control 6: Access Control Management
- CIS Control 7: Continuous Vulnerability Management
- CIS Control 8: Audit Log Management
- CIS Control 9: Email and Web Browser Protections
- CIS Control 10: Malware Defenses
- CIS Control 11: Data Recovery
- CIS Control 12: Network Infrastructure Management
- CIS Control 13: Network Monitoring and Defense
- CIS Control 14: Security Awareness and Skills Training
- CIS Control 15: Service Provider Management
- CIS Control 16: Application Software Security
- CIS Control 17: Incident Response Management
- CIS Control 18: Penetration Testing

The Controls are divided further into Implementation Groups (IGs) which are a recommended guidance to prioritize implementation of the CIS controls.

## Telecommunications

In telecommunications, security controls are defined as security services as part of the OSI model, these documents specify mechanisms such as authentication, access control, and data confidentiality to protect any network communications:

- ITU-T X.800 Recommendation.
- ISO ISO 7498-2

These are technically aligned. This model is widely recognized.

## Data liability (legal, regulatory, compliance)

The intersection of security risk and laws that set standards of care is where data liability are defined. A handful of databases are emerging to help risk managers research laws that define liability at the country, province/state, and local levels. In these control sets, compliance with relevant laws are the actual risk mitigators.

- Perkins Coie Security Breach Notification Chart: A set of articles (one per state) that define data breach notification requirements among US states.
- NCSL Security Breach Notification Laws: A list of US state statutes that define data breach notification requirements.
- ts jurisdiction: A commercial cybersecurity research platform with coverage of 380+ US State & Federal laws that impact cybersecurity before and after a breach. ts jurisdiction also maps to the NIST Cybersecurity Framework.

## Business control frameworks

There are a wide range of frameworks and standards looking at internal business, and inter-business controls, including:

- SSAE 16
- ISAE 3402
- Payment Card Industry Data Security Standard
- Health Insurance Portability and Accountability Act
- COBIT 4/5
- CIS Top-20
- NIST Cybersecurity Framework
