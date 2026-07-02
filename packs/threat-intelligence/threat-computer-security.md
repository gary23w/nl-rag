---
title: "Threat (computer security)"
source: https://en.wikipedia.org/wiki/Threat_(computer_security)
domain: threat-intelligence
license: CC-BY-SA-4.0
tags: cyber threat intelligence, indicator of compromise, structured threat information, threat intelligence platform, open source intelligence
fetched: 2026-07-02
---

# Threat (computer security)

In computer security, a **threat** is a potential negative action or event enabled by a vulnerability that results in an unwanted impact to a computer system or application.

A threat can be either a negative "intentional" event like hacking or an "accidental" negative event or otherwise a circumstance, capability, action, or event (incident is often used as a blanket term). A *threat actor* who is an individual or group that can perform the threat action, such as exploiting a vulnerability to actualise a negative impact. An *exploit* is a vulnerability that a threat actor used to cause an incident.

## Phenomenology

The term "threat" relates to some other basic security terms as shown in the following diagram:

A resource (both physical or logical) can have one or more vulnerabilities that can be exploited by a threat agent in a threat action. The result can potentially compromise the confidentiality, integrity or availability properties of resources (potentially different than the vulnerable one) of the organization and others involved parties (customers, suppliers). The so-called CIA triad is the basis of information security.

The attack can be *active* when it attempts to alter system resources or affect their operation: so it compromises Integrity or Availability. A "*passive attack*" attempts to learn or make use of information from the system but does not affect system resources: so it compromises Confidentiality.

OWASP (see figure) depicts the same phenomenon in slightly different terms: a threat agent through an attack vector exploits a weakness (vulnerability) of the system and the related security controls causing a technical impact on an IT resource (asset) connected to a business impact.

A set of policies concerned with information security management, the Information security management systems (ISMS), has been developed to manage, according to risk management principles, the countermeasures in order to accomplish to a security strategy set up following rules and regulations applicable in a country. Countermeasures are also called security controls; when applied to the transmission of information are named security services.

The overall picture represents the risk factors of the risk scenario.

The widespread of computer dependencies and the consequent raising of the consequence of a successful attack, led to a new term cyberwarfare.

Nowadays the many real attacks exploit Psychology at least as much as technology. Phishing and Pretexting and other methods are called social engineering techniques. The Web 2.0 applications, specifically Social network services, can be a mean to get in touch with people in charge of system administration or even system security, inducing them to reveal sensitive information. One famous case is Robin Sage.

The most widespread documentation on computer insecurity is about technical threats such as a computer virus, trojan and other malware, but a serious study to apply cost effective countermeasures can only be conducted following a rigorous IT risk analysis in the framework of an ISMS: a pure technical approach will let out the psychological attacks that are increasing threats.

## Threats classification

Threats can be classified according to their type and origin:

- Types of threats:
  - Physical damage: fire, water, pollution
  - Natural events: climatic, seismic, volcanic
  - Loss of essential services: electrical power, air conditioning, telecommunication
  - Compromise of information: eavesdropping, theft of media, retrieval of discarded materials
  - Technical failures: equipment, software, capacity saturation
  - Compromise of functions: error in use, abuse of rights, denial of actions

Note that a threat type can have multiple origins.

- Deliberate: aiming at information asset
  - spying
  - illegal processing of data
- Accidental
  - equipment failure
  - software failure
- Environmental
  - natural event
  - loss of power supply
- Negligence: Known but neglected factors, compromising the network safety and sustainability

## Threats Trends

Recent trends in computer threats show an increase in ransomware attacks, supply chain attacks, and fileless malware. Ransomware attacks involve the encryption of a victim's files and a demand for payment to restore access. Supply chain attacks target the weakest links in a supply chain to gain access to high-value targets. Fileless malware attacks use techniques that allow malware to run in memory, making it difficult to detect.

### Common Threats

Below are the few common emerging threats:

- Computer viruses
- Trojan horses
- Worms
- Rootkits
- Spyware
- Adware
- Ransomware
- Fileless malware

## Threat classification

Microsoft published a mnemonic, STRIDE, from the initials of threat groups:

- **S**poofing of user identity
- **T**ampering
- **R**epudiation
- **I**nformation disclosure (privacy breach or Data leak)
- **D**enial of Service (D.o.S.)
- **E**levation of privilege

Microsoft previously rated the risk of security threats using five categories in a classification called DREAD: Risk assessment model.

The spread over a network of threats can lead to dangerous situations. In military and civil fields, threat level has been defined: for example INFOCON is a threat level used by the US. Leading antivirus software vendors publish global threat level on their websites.

## Associated terms

### Threat agents or actors

In cybersecurity and risk assessment, a threat actor (or *threat agents*, *attackers*, or *adversaries*) is a person, group, organisation, state, or other entity with the ability to cause, carry, transmit, support, or exploit a threat.

Threat actors are commonly analysed according to their motivations, resources, technical capability, access to systems, relationship to a target, and degree of connection to state authority. They may exploit vulnerabilities, conduct social engineering, steal or monetise data, disrupt operations, or support other actors who carry out such activity. Because the term covers a wide range of actors, researchers and security organisations use taxonomies that distinguish between groups such as cybercriminals, state-linked actors, ideologically motivated actors, thrill seekers or trolls, insiders, and competitors.

Threat actor classifications are used in risk management, cyber threat intelligence, and incident response to connect observed behaviour with possible objectives and likely future activity. The categories are not always mutually exclusive: the same actor may combine criminal, ideological, commercial, or state-linked motivations, and different organisations may use different names for similar actors.

### Threat action

**Threat action** is an assault on system security. A complete security architecture deals with both intentional acts and accidental events.

### Threat analysis

**Threat analysis** is the analysis of the probability of occurrences and consequences of damaging actions to a system. It is the basis of risk analysis.

### Threat modeling

**Threat modeling** is a process that helps organizations identify and prioritize potential threats to their systems. It involves analyzing the system's architecture, identifying potential threats, and prioritizing them based on their impact and likelihood. By using threat modeling, organizations can develop a proactive approach to security and prioritize their resources to address the most significant risks.

### Threat intelligence

**Threat intelligence** is the practice of collecting and analyzing information about potential and current threats to an organization. This information can include indicators of compromise, attack techniques, and threat actor profiles.

### Threat consequence

**Threat consequence** is a security violation that results from a threat action.

### Threat landscape or environment

A collection of threats in a particular domain or context, with information on identified vulnerable assets, threats, risks, threat actors and observed trends.

## Threat management

Threats should be managed by operating an ISMS, performing all the IT risk management activities foreseen by laws, standards and methodologies.

Very large organizations tend to adopt business continuity management plans in order to protect, maintain and recover business-critical processes and systems. Some of these plans are implemented by computer security incident response team (CSIRT).

Threat management must identify, evaluate, and categorize threats. There are two primary methods of threat assessment:

- Information security audit
- Penetration test

Many organizations perform only a subset of these methods, adopting countermeasures based on a non-systematic approach, resulting in *computer insecurity*.

Information security awareness is a significant market. There has been a lot of software developed to deal with IT threats, including both open-source software and proprietary software.

### Cyber threat management

Threat management involves a wide variety of threats including physical threats like flood and fire. While ISMS risk assessment process does incorporate threat management for cyber threats such as remote buffer overflows the risk assessment process doesn't include processes such as threat intelligence management or response procedures.

Cyber threat management (CTM) is emerging as the best practice for managing cyber threats beyond the basic risk assessment found in ISMS. It enables early identification of threats, data-driven situational awareness, accurate decision-making, and timely threat mitigating actions.

CTM includes:

- Manual and automated intelligence gathering and threat analytics
- Comprehensive methodology for real-time monitoring including advanced techniques such as behavioral modelling
- Use of advanced analytics to optimize intelligence, generate security intelligence, and provide Situational Awareness
- Technology and skilled people leveraging situational awareness to enable rapid decisions and automated or manual actions

## Threat hunting

**Cyber threat hunting** is "the process of proactively and iteratively searching through networks to detect and isolate advanced threats that evade existing security solutions."

The SANS Institute has conducted research and surveys on the effectiveness of threat hunting to track and disrupt cyber adversaries as early in their process as possible. According to a survey performed in 2019, "61% [of the respondents] report at least an 11% measurable improvement in their overall security posture" and 23.6% of the respondents have experienced a 'significant improvement' in reducing the dwell time.
