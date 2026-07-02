---
title: "ATT&CK"
source: https://en.wikipedia.org/wiki/MITRE_ATT%26CK
domain: mitre-attack
license: CC-BY-SA-4.0
tags: mitre att&ck, adversary tactics techniques, att&ck framework, cyber kill chain, threat actor behavior
fetched: 2026-07-02
---

# ATT&CK

(Redirected from

MITRE ATT&CK

)

The **Adversarial Tactics, Techniques, and Common Knowledge** (**ATT&CK**) is a guideline for classifying and describing cyberattacks and intrusions. It was created by the Mitre Corporation and released in 2013.

The MITRE ATT&CK framework is widely used within cybersecurity, because it is a public catalog of known attacker techniques, where every technique has an ID, such as "T1566-Phishing". It gives the industry a shared vocabulary: an analyst can write the ID in a report and every reader will know exactly what is meant. The US Cybersecurity and Infrastructure Security Agency's (CISA) formally recognised the importance of this framework in "Best practices for Mitre ATT&CK mapping", cementing its status as government-endorsed for the standardization of threat intelligence work.

Rather than examining the results of an attack (also known as indicators of compromise (IoCs)), it identifies tactics that indicate an attack is in progress. Tactics are the “why” of an attack technique.

The framework consisted in 2022 of 14 tactic categories, which encompass the methods of an adversary. Examples include privilege escalation and command and control. These categories are then broken down further into specific techniques and sub-techniques. In the latest release of the framework, ATT&CK version 19 released in April 2026, there are now 15 Tactic categories. The previous "Defense Evasion" category has been split in 2: "Stealth" where defenses appear intact depite having been broken by adversaries and "Defense Impairment" capturing behavior where Defenses are actively and visibly broken.

The framework is an alternative to the cyber kill chain developed by Lockheed Martin.

## ATT&CK Matrix for Enterprise

The ATT&CK Matrix for Enterprise is a comprehensive framework that is presented as a kanban board-style diagram. It defined in 2022 14 categories of tactics, techniques and procedures (TTPs) used by cybercriminals with the associated techniques and sub-techniques.

| Category | Description | Techniques |
|---|---|---|
| Reconnaissance | Gathering information about a target. | 12 |
| Resource Development | Identifying and acquiring resources for the attack. | 9 |
| Initial Access | Gaining initial access to a system or network. | 11 |
| Execution | Running malicious code on a system. | 20 |
| Persistence | Maintaining access to a system or network. | 22 |
| Privilege Escalation | Obtaining elevated privileges within a system or network. | 13 |
| Defense Evasion | Disabling or evading security measures. | 43 |
| Credential Access | Obtaining credentials to access systems or data. | 17 |
| Discovery | Identifying additional systems or information within a network. | 34 |
| Lateral Movement | Moving laterally within a compromised network. | 9 |
| Collection | Collecting data from compromised systems. | 17 |
| Command and Control | Establishing communication with compromised systems. | 18 |
| Exfiltration | Transferring stolen data from a compromised system. | 9 |
| Impact | Taking actions to achieve the attacker's objectives. | 15 |

### Reconnaissance

Reconnaissance is the initial stage of information gathering for an eventual cyberattack.

There are 10 techniques – including the use of network scanning, social engineering and Open-source intelligence (OSINT).

| MITRE ID | Techniques | Summary |
|---|---|---|
| T1595 | Active Scanning | Active reconnaissance by scanning the target network using a port scanning tool such as Nmap, vulnerability scanning tools and wordlist scanning for common file extensions and software used by the victim. |
| T1598 | Phishing for Information | Using social engineering techniques to elicit useful information from the target. Using a communication channel such as e-mail, including generic phishing and targeted spearphishing which has been specifically created to target an individual victim |
| T1592 | Gather Victim Host Information | Discover the configuration of specific endpoints such as their hardware, software and administrative configuration (such as Active Directory domain membership). Especially security protections such as antivirus and locks (biometric, smart card or even a Kensington K-Slot). |
| T1590 | Gather Victim Network Information | Discover the target network's configuration such as the network topology, security appliances (network firewall, VPN), IP address ranges (either IPv4, IPv6 or both), fully qualified domain names (FQDN) and the Domain Name System (DNS) configuration. |
