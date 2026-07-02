---
title: "Cyber kill chain"
source: https://en.wikipedia.org/wiki/Cyber_kill_chain
domain: mitre-attack
license: CC-BY-SA-4.0
tags: mitre att&ck, adversary tactics techniques, att&ck framework, cyber kill chain, threat actor behavior
fetched: 2026-07-02
---

# Cyber kill chain

The **cyber kill chain** is the process by which perpetrators carry out cyberattacks. Lockheed Martin adapted the concept of the *kill chain* from a military setting to information security, using it as a method for modeling intrusions on a computer network. The cyber kill chain model has seen some adoption in the information security community. However, acceptance is not universal, with critics pointing to what they believe are fundamental flaws in the model.

## Attack phases and countermeasures

Computer scientists at Lockheed-Martin corporation described a new "intrusion kill chain" framework or model to defend computer networks in 2011. They wrote that attacks may occur in phases and can be disrupted through controls established at each phase. Since then, the "cyber kill chain" has been adopted by data security organizations to define phases of cyberattacks.

A cyber kill chain reveals the phases of a cyberattack: from early reconnaissance to the goal of data exfiltration. The kill chain can also be used as a management tool to help continuously improve network defense. According to Lockheed Martin, threats must progress through several phases in the model, including:

1. Reconnaissance: Intruder selects target, researches it, and attempts to identify vulnerabilities in the target network.
2. Weaponization: Intruder creates remote access malware weapon, such as a virus or worm, tailored to one or more vulnerabilities.
3. Delivery: Intruder transmits weapon to target (e.g., via e-mail attachments, websites or USB drives)
4. Exploitation: Malware weapon's program code triggers, which takes action on target network to exploit vulnerability.
5. Installation: Malware weapon installs an access point (e.g., "backdoor") usable by the intruder.
6. Command and Control: Malware enables intruder to have "hands on the keyboard" persistent access to the target network.
7. Actions on Objective: Intruder takes action to achieve their goals, such as data exfiltration, data destruction, or encryption for ransom.

Defensive courses of action can be taken against these phases:

1. Detect: Determine whether an intruder is present.
2. Deny: Prevent information disclosure and unauthorized access.
3. Disrupt: Stop or change outbound traffic (to attacker).
4. Degrade: Counter-attack command and control.
5. Deceive: Interfere with command and control.
6. Contain: Network segmentation changes

A U.S. Senate investigation of the 2013 Target Corporation data breach included analysis based on the Lockheed-Martin kill chain framework. It identified several stages where controls did not prevent or detect progression of the attack.

## Alternatives

Different organizations have constructed their own kill chains to try to model different threats. FireEye proposes a linear model similar to Lockheed-Martin's. In FireEye's kill chain the persistence of threats is emphasized. This model stresses that a threat does not end after one cycle.

1. Reconnaissance: This is the initial phase where the attacker gathers information about the target system or network. This could involve scanning for vulnerabilities, researching potential entry points, and identifying potential targets within the organization.
2. Initial Intrusion: Once the attacker has gathered enough information, they attempt to breach the target system or network. This could involve exploiting vulnerabilities in software or systems, utilizing social engineering techniques to trick users, or using other methods to gain initial access.
3. Establish a Backdoor: After gaining initial access, the attacker often creates a backdoor or a persistent entry point into the compromised system. This ensures that even if the initial breach is discovered and mitigated, the attacker can still regain access.
4. Obtain User Credentials: With a foothold in the system, the attacker may attempt to steal user credentials. This can involve techniques like keylogging, phishing, or exploiting weak authentication mechanisms.
5. Install Various Utilities: Attackers may install various tools, utilities, or malware on the compromised system to facilitate further movement, data collection, or control. These tools could include remote access Trojans (RATs), keyloggers, and other types of malicious software.
6. Privilege Escalation / Lateral Movement / Data Exfiltration: Once inside the system, the attacker seeks to elevate their privileges to gain more control over the network. They might move laterally within the network, trying to access more valuable systems or sensitive data. Data exfiltration involves stealing and transmitting valuable information out of the network.
7. Maintain Persistence: This stage emphasizes the attacker's goal to maintain a long-term presence within the compromised environment. They do this by continuously evading detection, updating their tools, and adapting to any security measures put in place.

## Critiques

Among the critiques of Lockheed Martin's cyber kill chain model as threat assessment and prevention tool is that the first phases happen outside the defended network, making it difficult to identify or defend against actions in these phases. Similarly, this methodology is said to reinforce traditional perimeter-based and malware prevention-based defensive strategies. Others have noted that the traditional cyber kill chain isn't suitable to model the insider threat. This is particularly troublesome given the likelihood of successful attacks that breach the internal network perimeter, which is why organizations "need to develop a strategy for dealing with attackers inside the firewall. They need to think of every attacker as [a] potential insider".

## Unified kill chain

The Unified Kill Chain was developed in 2017 by Paul Pols in collaboration with Fox-IT and Leiden University to overcome common critiques against the traditional cyber kill chain, by uniting and extending Lockheed Martin's kill chain and MITRE's ATT&CK framework (both of which are based on the "Get In, Stay In, and Act" model constructed by James Tubberville and Joe Vest). The unified version of the kill chain is an ordered arrangement of 18 unique attack phases that may occur in an end-to-end cyberattack, which covers activities that occur outside and within the defended network. As such, the unified kill chain improves over the scope limitations of the traditional kill chain and the time-agnostic nature of tactics in MITRE's ATT&CK. The unified model can be used to analyze, compare, and defend against end-to-end cyberattacks by advanced persistent threats. A subsequent whitepaper on the unified kill chain was published in 2021.
