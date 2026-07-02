---
title: "Threat hunting"
source: https://en.wikipedia.org/wiki/Cyber_threat_hunting
domain: threat-hunting
license: CC-BY-SA-4.0
tags: cyber threat hunting, proactive threat detection, indicator of compromise, advanced persistent threat, hypothesis driven investigation
fetched: 2026-07-02
---

# Threat hunting

(Redirected from

Cyber threat hunting

)

In information security, **threat hunting** is the process of proactively searching for threats against computer systems in order to protect them. This is in contrast to traditional threat management measures, such as firewalls, intrusion detection systems (IDS), malware sandbox (computer security) and SIEM systems, which typically involve an investigation of evidence-based data *after* there has been a warning of a potential threat. Threat analyst Lesley Carhart stated that there is no consensus amongst practitioners what threat hunting actually entails.

## Methodologies

### Overview

Recently, the world has seen a rise in the number and severity of cyber attacks, data breaches, malware infections, and online fraud incidents. According to cybersecurity and AI company SonicWall, the number of ransomware attacks grew by 105% globally. Major corporations around the world have fallen victim to high-profile data breaches, with the average cost of a data breach now estimated at $4.24 million, according to IBM.

### Cyber threat hunting methodologies

Threat hunting has traditionally been a manual process, in which a security analyst sifts through various data information using their own knowledge and familiarity with the network to create hypotheses about potential threats, such as, but not limited to, lateral movement by threat actors. To be even more effective and efficient, however, threat hunting can be partially automated, or machine-assisted, as well. In this case, the analyst uses software that leverages machine learning and user and entity behavior analytics (UEBA) to inform the analyst of potential risks. The analyst then investigates these potential risks, tracking suspicious behavior in the network. Thus, hunting is an iterative process, meaning that it must be continuously carried out in a loop, beginning with a hypothesis.

- Analytics-Driven: "Machine-learning and UEBA, used to develop aggregated risk scores that can also serve as hunting hypotheses"
- Situational-Awareness Driven: "Crown Jewel analysis, enterprise risk assessments, company- or employee-level trends"
- Intelligence-Driven: "Threat intelligence reports, threat intelligence feeds, malware analysis, vulnerability scans"

The analysts research their hypothesis by going through vast amounts of data about the network. The results are then stored so that they can be used to improve the automated portion of the detection system and to serve as a foundation for future hypotheses.

The Detection Maturity Level (DML) model expresses threat indicators can be detected at different semantic levels. High semantic indicators such as goal and strategy or tactics, techniques and procedures (TTPs) are more valuable to identify than low semantic indicators such as network artifacts and atomic indicators such as IP addresses. SIEM tools typically only provide indicators at relatively low semantic levels. There is therefore a need to develop SIEM tools that can provide threat indicators at higher semantic levels.

## Indicators

There are two types of indicators:

1. Indicator of compromise - An indicator of compromise (IOC) tells you that an action has happened and you are in a reactive mode. This type of IOC is done by looking inward at your own data from transaction logs and or SIEM data. Examples of IOC include unusual network traffic, unusual privileged user account activity, login anomalies, increases in database read volumes, suspicious registry or system file changes, unusual DNS requests and Web traffic showing non-human behavior. These types of unusual activities allow security administration teams to spot malicious actors earlier in the cyberattack process.
2. Indicator of Concern - Using Open-source intelligence (OSINT), data can be collected from publicly available sources to be used for cyberattack detection and threat hunting.

## Tactics, Techniques and Procedures (TTPs)

The SANS Institute identifies a threat hunting maturity model as follows:

- Initial – At Level 0 maturity, an organization relies primarily on automated reporting and does little or no routine data collection.
- Minimal – At Level 1 maturity, an organization incorporates threat intelligence indicator searches. It has a moderate or high level of routine data collection.
- Procedural – At Level 2 maturity, an organization follows analysis procedures created by others. It has a high or very high level of routine data collection.
- Innovative – At Level 3 maturity, an organization creates new data analysis procedures. It has a high or very high level of routine data collection.
- Leading – At Level 4 maturity, automates the majority of successful data analysis procedures. It has a high or very high level of routine data collection.

## Dwell time

The dwell time either indicates the entire span of a security incident (initial compromise until detection and full cleanup) or the 'mean time to detect' (from initial compromise until detection). According to the 2022 Mandiant M-Trends Report, cyberattackers operate undetected for an average of 21 days (a 79% reduction, compared to 2016), but this varies greatly by region. Per Mandiant, the dwell time can be as low as 17 days (in the Americas) or as high as 48 days (in EMEA). The study also showed that 47% of attacks are discovered only after notification from an external party.

## Example reports

- Seedworm: Group Compromises Government Agencies, Oil & Gas, NGOs, Telecoms, and IT Firms

## Example threat hunting

- Threat hunting using DNS firewalls and data enrichment

## Threat hunting methodologies

**Inside the network perimeter**

- Reactive Threat Hunting - This method is triggered by a malicious event, typically after a data breach or theft is discovered. Efforts are typically focused on forensics and remediation.
- Proactive Threat Hunting - This method actively seeks out ongoing malicious events and activities inside the network, the goal is to detect an in progress cyber attack. Efforts are typically focused on detection and remediation.

**Outside the network perimeter**

- External Threat Hunting - This method proactively seeks out malicious threat actor infrastructure to map and predict where cyber attacks are likely to emerge to prepare defensive strategies. Efforts are typically focused on Cyber Threat Reconnaissance, Threat Surface Mapping and monitoring of third-party risks. In a Team Cymru blog, they explain that unlike internal threat hunting, the threat actors themselves are proactively tracked, traced, and monitored as they shift infrastructure and claim victims. Indicators of compromise (IOCs), typically used to inform of a breach, become signals intelligence beyond the network perimeter.

## Regulatory context

Regulatory frameworks increasingly emphasize proactive threat detection as part of comprehensive security programs. The Health Insurance Portability and Accountability Act (HIPAA) Security Rule requires covered entities to implement procedures for monitoring log-in attempts and reporting discrepancies (45 CFR 164.308(a)(5)(ii)(C)) and to maintain audit controls that record and examine activity in systems containing electronic protected health information (45 CFR 164.312(b)). The December 2024 HIPAA Security Rule NPRM proposed requiring regulated entities to deploy technology capable of detecting and responding to suspicious network activity, including continuous monitoring of information systems for unauthorized access attempts.

NIST Special Publication 800-53 addresses threat hunting through several control families, including SI-4 (System Monitoring), which recommends organizations monitor information systems to detect attacks, indicators of potential attacks, and unauthorized connections, and IR-6 (Incident Reporting), which establishes requirements for reporting suspected security incidents. The NIST Cybersecurity Framework 2.0 Detect function specifically addresses continuous monitoring and anomaly detection as foundational security activities.
