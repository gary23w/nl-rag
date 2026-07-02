---
title: "Cyber threat intelligence"
source: https://en.wikipedia.org/wiki/Threat_intelligence
domain: indicators-of-compromise
license: CC-BY-SA-4.0
tags: indicators of compromise, structured threat information, cyber threat intelligence feed, malware artifact detection, threat intelligence sharing
fetched: 2026-07-02
---

# Cyber threat intelligence

(Redirected from

Threat intelligence

)

**Cyber threat intelligence** (**CTI**) is a part of cybersecurity that focuses on collecting, analyzing, and sharing information about potential or existing cyber threats. It gives organizations the information needed to predict, prevent, and respond to cyberattacks, enabling them to understand attackers’ behavior, tactics, and the vulnerabilities they exploit.

Sources of cyber threat intelligence include open-source data, social media, operational and technical intelligence, device log files, forensic analysis, internet traffic, as well as data from the dark web and deep web.

Modern CTI programs stand out from just using raw security data because they combine technical monitoring, outside intelligence sources, and analysis methods to prepare specific and useful assessments about cyber threats aimed at particular organizations or business sectors.

Analytical interpretation gives context to attackers’ actions, capabilities, and intentions, helping organizations set priorities and allocate security resources effectively. When companies base decisions on intelligence and analysis, they can act proactively instead of just reacting to security incidents, stopping breaches before they happen. This approach has become increasingly important in recent years, as IBM estimates that exploiting vulnerabilities is the most common way companies are breached, making up 47% of all attacks.

The COVID-19 pandemic and the rise in remote work have also contributed to increased vulnerability to threats, making corporate data more exposed. Due to growing threats on the one hand, and increasing analytical demands on the other, many companies have decided in recent years to outsource their threat analytics tasks to a managed security service provider (MSSP).

Cyber threat analytics has also become an important component of modern Security Operations Centers (SOCs), where threat intelligence data is used to enrich alerts, identify malicious infrastructure, and support incident response and threat hunting activities.

## Types

There are three categorical levels of cyber threat intelligence: tactical, operational, and strategic. Each serves a distinct audience and purpose in building a comprehensive threat assessment.

- Tactical: The most technical level, focused on immediate detection and response. Tactical intelligence consists of specific indicators of compromise (IOCs): IP addresses, domain names, file hashes, malware signatures, and similar artifacts. Security operations teams use these indicators to identify and block threats in real time through SIEM rules, firewall policies, and endpoint detection systems.
- Operational: Focused on understanding adversary behavior and campaigns. Operational intelligence analyzes who the threat actors are, their tactics, techniques, and procedures (TTPs), infrastructure patterns, motivations, and ongoing campaigns. This level helps security teams anticipate how attacks unfold, recognize adversary tradecraft, and understand the broader context behind specific incidents. Sources include incident response findings, malware analysis, threat actor profiling, security vendor reporting, and intelligence from industry sharing groups and government advisories.
- Strategic: Tailored for non-technical audiences, particularly executives and board members. Strategic intelligence addresses high-level business risk: which threat actors target the organization's sector, geopolitical factors affecting the threat landscape, long-term trends, and the potential business impact of cyber threats. Delivered through reports, briefings, and risk assessments, it helps leadership prioritize security investments and understand how cyber risk aligns with organizational objectives.

Technical threat analysis focuses on machine-readable indicators of compromise (IoCs): malicious IP addresses, domain names, file hashes, and command-and-control (C2) servers or infrastructure. This enables automated detection and response. While the conventional distinction is between strategic, tactical, and operational analytics, some large organizations often define technical threat analytics as a separate (fourth) category essential for Security Operations Centers (SOCs).

Some threat analytics platforms also distinguish between indicator-based analytics and behavior-based analytics. Indicator-based analytics focuses on specific technical artifacts: malicious IP addresses, file hashes, etc. Behavior-based analytics analyzes attackers’ tactics and techniques to detect threats that may change their infrastructure or indicators over time.

## Sources of cyber threat intelligence

Information about cybersecurity threats can be obtained from various sources: internal telemetry from security tools, network log data, endpoint system data, malware analysis, dedicated threat intelligence feeds from cybersecurity vendors, open-source intelligence (OSINT), dark web monitoring, and analytical reports from government agencies or private security firms. To obtain effective analytical insights, it is necessary to combine data from internal security tools with external technical and strategic reports to gain a more comprehensive view of the threat landscape.

## Process - intelligence cycle

The process of developing cyber threat intelligence is a circular and continuous process, known as the intelligence cycle, which is composed of five phases, carried out by intelligence teams to provide to leadership relevant and convenient intelligence to reduce danger and uncertainty.

The five phases are: 1) planning and direction; 2) collection; 3) processing; 4) analysis; 5) dissemination.

In planning and directing, the customer of the intelligence product requests intelligence on a specific topic or objective. Then, once directed by the client, the second phase begins, collection, which involves accessing the raw information that will be required to produce the finished intelligence product. Since information is not intelligence, it must be transformed and therefore must go through the processing and analysis phases: in the processing (or pre-analytical phase) the raw information is filtered and prepared for analysis through a series of techniques (decryption, language translation, data reduction, etc.); In the analysis phase, organized information is transformed into intelligence. Finally, the dissemination phase, in which the newly selected threat intelligence is sent to the various users for their use.

The intelligence cycle model in the field of cyber threat analysis is based on traditional intelligence methods used by military and government intelligence agencies, where structured analysis is employed to transform raw data into the insights needed for decision-making.

## Key requirements for threat intelligence

There are three key elements needed for information or data to qualify as threat intelligence:

- Evidence-based: To be useful, threat intelligence must be gathered through proper evidence-gathering methods. For example, analyzing malware can help generate threat intelligence.
- Utility: Threat intelligence should positively impact a security incident by providing useful information. It must offer clear context and data about specific behaviors and methods.
- Actionable: For information to be considered threat intelligence, it must lead to action. This is what distinguishes intelligence from mere data.

Cybersecurity researchers also highlight other factors for good threat intelligence, such as accuracy, completeness, timeliness, compatibility, and relevance to the environment where it will be used.

## Benefits of cyber threat intelligence

Cyber threat intelligence provides a number of benefits, which include:

- Gives organizations, agencies or other entities, the ability to develop a proactive and robust cybersecurity posture and to bolster overall risk management and cybersecurity policies and responses.
- Drives momentum toward a proactive cybersecurity posture that is predictive, not simply reactive after a cyber attack.
- It provides context and insights about active attacks and potential threats to aid decision making.
- It prevents data breaches from exposing sensitive information, thus preventing data loss.
- Reduces costs. Since data breaches are costly, reducing the risk of data breaches helps save money.
- It provides organizations with guidance on implementing security measures to prevent future attacks.
- Enables sharing of knowledge, skills and experiences among the cybersecurity community and system stakeholders.
- It helps to more easily and better identify risks and threats, as well as delivery mechanisms, indicators of compromise across the infrastructure, and potential specific actors and motivators.
- Helps in the detection of attacks during and before these stages.
- Provides indicators of actions taken during each stage of the attack.
- Communicates threat surfaces, attack vectors and malicious activities directed to both information technology and operational technology platforms.
- Serves as a fact-based repository of data on successful and failed cyberattacks.
- Provides indicators for computer emergency response teams and incident response groups.

Threat analytics helps improve threat detection mechanisms by identifying attackers’ methods and behavioral patterns that are not yet detected by automated security monitoring systems.

## Threat intelligence platforms

Organizations often deploy specialized software known as threat intelligence platforms (TIPs) to aggregate, analyze, and distribute threat intelligence data.

Threat intelligence platforms gather data from both internal and external sources, including security system telemetry, open-source intelligence feeds, malware repositories, vulnerability databases, and reports from security vendors. By aggregating and correlating indicators of compromise (IoCs) like malicious IP addresses, domain names, file hashes, and command-and-control infrastructure, these platforms help security professionals better understand threat contexts and identify the most significant threats.

TI platforms are commonly integrated with other cybersecurity systems. Integrations with tools such as security information and event management (SIEM) systems, endpoint detection and response (EDR) solutions, and incident response platforms enable automated alert enrichment and faster investigation of security incidents.

Threat intelligence platforms also support threat hunting and incident response by organizing indicators and intelligence reports within searchable repositories, allowing analysts to correlate events and identify patterns associated with specific campaigns or threat actors.

Some threat intelligence platforms use automated data pipelines and machine learning techniques to process large volumes of threat data and generate analytical insights for proactive cybersecurity strategies.

## Structured threat intelligence

Modern programs for collecting and analyzing cyber threat intelligence rely on standardized formats that enable automated exchange between organizations and security tools, as well as the processing of analytical data.

STIX (Structured Threat Information Expression) is a standardized language for representing analytical information about cyber threats in a machine-readable format, allowing analysts to describe attackers, campaigns, vulnerabilities, and indicators within a structured data model.

Trusted Automated Exchange of Intelligence Information (TAXII) is a protocol for supporting the automated exchange of threat intelligence data, typically used to transmit intelligence in STIX format.

The Traffic Light Protocol (TLP) is widely used in the exchange of threat intelligence to determine how sensitive information is shared among members of trusted communities.

## Analytical frameworks

Analysts use structured analytical models to understand the behavior of attackers and implement defensive measures.

The Cyber Kill Chain model, developed by Lockheed Martin, describes the stages of a cyberattack as a linear progression: reconnaissance, weaponization (preparation of attack tools), delivery, exploitation of vulnerabilities, installation, command and control, and actions on objectives. This framework helps defenders identify at which stage an attack can be disrupted.

The Diamond Model of Intrusion Analysis examines the relationships between four core features of any intrusion event: the adversary, their capabilities (tools and techniques), the infrastructure they use (domains, IP addresses, email addresses), and the victim. Using these relationships across multiple events, analysts can pivot between incidents, identify patterns, and attribute activity to specific threat actors or campaigns.

The MITRE ATT&CK framework is a knowledge base of adversary tactics and techniques based on real-world observations. It organizes attacker behavior into 14 tactics (the "why" of an action - initial access, persistence, privilege escalation, defense evasion, etc.), and hundreds of techniques (the "how" - specific methods used to achieve each tactic). Unlike the linear Cyber Kill Chain, ATT&CK provides a detailed matrix of adversary behaviors that can occur in any order or simultaneously. Security teams use ATT&CK to map threat intelligence to defensive controls, assess coverage gaps, conduct red team exercises, and build detections aligned with actual adversary tradecraft. It has become the de facto standard for describing and sharing operational threat intelligence.

## Automation of threat intelligence analysis

The increasing volume and velocity of cyber threat data have led organizations to automate significant parts of the threat intelligence lifecycle, including data collection, processing, correlation, and distribution. Automated threat intelligence systems typically ingest data from multiple sources, and then process and correlate this information to identify patterns of malicious activity.

Machine-readable standards and transport protocols (STIX and TAXII) are an important component of automated CTI systems.

Integration between threat intelligence platforms and security operations center (SOC) systems enables automated prioritization of alerts and enrichment of security events using intelligence indicators.

The drawback of automated analytics systems is that they can generate false positives or rely on low-quality indicators, which means analysts have to verify the results and provide a contextual interpretation. For this reason, many organizations adopt a hybrid model in which automated systems perform large-scale data processing while human analysts focus on interpretation, attribution, and strategic assessment of cyber threats.

## Attribution

Attribution is the process of identifying who conducted a cyber attack: the individual actors, organized groups, or nation-state sponsors behind an intrusion. In threat intelligence, attribution helps organizations understand adversary intent, prioritize defenses, anticipate future targeting, and inform strategic decisions. It also supports law enforcement investigations and policy responses.

Attribution relies on multiple evidence types: technical indicators (infrastructure, malware code), behavioral analysis (tactics, techniques, and operational tradecraft), linguistic artifacts, targeting patterns (victim selection and geopolitical alignment), and intelligence from human sources or signals intelligence.

However, attribution is inherently difficult and often remains probabilistic rather than definitive. Attackers routinely employ obfuscation techniques: using proxy infrastructure, VPNs, compromised intermediary systems, and stolen or leased tools. Advanced threat actors deliberately plant false flags by mimicking the TTPs, language, or infrastructure patterns of other groups to misdirect attribution efforts.

As a result, different threat intelligence vendors take varying approaches to attribution. Some explicitly attribute threat groups to specific nation-states or sponsoring organizations based on their analysis and confidence thresholds. Others intentionally avoid geopolitical attribution, instead documenting only observable, undisputable facts, such as language artifacts in malware, shared infrastructure, or technical capabilities, and tracking adversary clusters by neutral designators. Attribution assessments are typically expressed with varying levels of confidence (low, medium, high) rather than certainty, and erroneous conclusions can have diplomatic, legal, or strategic consequences.

## CTI sharing

In 2015 U.S. government legislation in the form of the Cybersecurity Information Sharing Act encouraged the sharing of CTI indicators between government and private organizations. This act required the U.S. federal government to facilitate and promote four CTI objectives:

1. Sharing of "classified and declassified cyber threat indicators in possession of the federal government with private entities, nonfederal government agencies, or state, tribal, or local governments";
2. Sharing of "unclassified indicators with the public";
3. Sharing of "information with entities under cybersecurity threats to prevent or mitigate adverse effects";
4. Sharing of "cybersecurity best practices with attention to the challenges faced by small businesses."

In 2016, the U.S. government agency National Institute of Standards and Technology (NIST) issued a publication (NIST SP 800–150) which further outlined the necessity for Cyber Threat Information Sharing as well as a framework for implementation.

In addition to the United States, the exchange of real-time information on cyber threats is coordinated through international and industry organizations, such as Information Sharing and Analysis Centers (ISACs), which facilitate cooperation among companies in critical infrastructure sectors, including finance, energy, and transport.
