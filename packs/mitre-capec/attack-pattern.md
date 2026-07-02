---
title: "Attack patterns"
source: https://en.wikipedia.org/wiki/Attack_pattern
domain: mitre-capec
license: CC-BY-SA-4.0
tags: mitre capec catalog, common attack pattern enumeration, attack pattern taxonomy, common weakness enumeration, adversary technique classification
fetched: 2026-07-02
---

# Attack patterns

(Redirected from

Attack pattern

)

In computer science, **attack patterns** are a group of rigorous methods for finding bugs or errors in code related to computer security.

Attack patterns are often used for testing purposes and are very important for ensuring that potential vulnerabilities are prevented. The attack patterns themselves can be used to highlight areas which need to be considered for security hardening in a software application. They also provide, either physically or in reference, the common solution pattern for preventing the attack. Such a practice can be termed *defensive coding patterns*.

Attack patterns define a series of repeatable steps that can be applied to simulate an attack against the security of a system.

## Categories

There are several ways to categorize attack patterns.

### General categories

**Architectural** attack patterns are used to attack flaws in the architectural design of the system. These are things like weaknesses in protocols, authentication strategies, and system modularization. These are more logic-based attacks than actual bit-manipulation attacks. Time-of-check vs time-of-use can be classified as architectural flaws.

**Parsing and validation**. SQL injection attacks and cross-site scripting fall into this category.

**Memory safety**. In memory-unsafe programming languages, lower-level issues such as buffer overflows and race conditions can be exploited to take partial or complete control of the software.

**Spoofing and friends**. Often targeting web domain names with attacks such as phishing, spoofing, and typosquatting.

**GUI attacks**. These attack graphical user interface (GUI) primitives: clickjacking, mousetrapping, HTML iframe overlay tricks.

**Multipliers**. Malvertising, "viral" attacks that spread via social media, "worm" pattern, preparing a list of vulnerable hosts before releasing a worm

### By technology

Another way is to group them into general categories. Another way of categorizing attack patterns is to group them by a specific technology or type of technology (e.g. database attack patterns, web application attack patterns, network attack patterns, etc. or SQL Server attack patterns, Oracle Attack Patterns, .Net attack patterns, Java attack patterns, etc.)

## Structure

Attack Patterns are structured very much like structure of Design patterns. Using this format is helpful for standardizing the development of attack patterns and ensures that certain information about each pattern is always documented the same way.

A recommended structure for recording Attack Patterns is as follows:

- **Pattern Name**

The label given to the pattern which is commonly used to refer to the pattern in question.

- **Type & Subtypes**

The pattern type and its associated subtypes aid in classification of the pattern. This allows users to rapidly locate and identify pattern groups that they will have to deal with in their security efforts.

Each pattern will have a type, and zero or more subtypes that identify the category of the attack pattern. Typical types include Injection Attack, Denial of Service Attack, Cryptanalysis Attack, etc. Examples of typical subtypes for Denial Of Service, for example, would be: DOS – Resource Starvation, DOS-System Crash, DOS-Policy Abuse.

Another important use of this field is to ensure that true patterns are not repeated unnecessarily. Often it is easy to confuse a new exploit with a new attack. New exploits are created all the time for the same attack patterns. The Buffer Overflow Attack Pattern is a good example. There are many known exploits and viruses that take advantage of a Buffer Overflow vulnerability. But they all follow the same pattern. Therefore, the Type and Subtype classification mechanism provides a way to classify a pattern. If the pattern you are creating doesn't have a unique Type and Subtype, chances are it is a new exploit for an existing pattern.

This section is also used to indicate if it is possible to automate the attack. If it is possible to automate the attack, it is recommended to provide a sample in the Sample Attack Code section which is described below.

- **Also Known As**

Certain attacks may be known by several different names. This field is used to list those other names.

- **Description**

This is a description of the attack itself, and where it may have originated from. It is essentially a free-form field that can be used to record information that doesn’t easily fit into the other fields.

- **Attacker Intent**

This field identifies the intended result of the attacker. This indicates the attacker’s main target and goal for the attack itself. For example, The Attacker Intent of a DOS – Bandwidth Starvation attack is to make the target web site unreachable to legitimate traffic.

- **Motivation**

This field records the attacker’s reason for attempting this attack. It may be to crash a system in order to cause financial harm to the organization, or it may be to execute the theft of critical data in order to create financial gain for the attacker.

This field is slightly different from the Attacker Intent field in that it describes why the attacker may want to achieve the Intent listed in the Attacker Intent field, rather than the physical result of the attack.

- **Exploitable Vulnerability**

This field indicates the specific type of vulnerability that creates the attack opportunity in the first place. An example of this in an Integer Overflow attack would be that the integer-based input field is not checking size of the value of the incoming data to ensure that the target variable is capable of managing the incoming value. This is the vulnerability that the associated exploit will take advantage of in order to carry out the attack.

- **Participants**

The Participants are one or more entities that are required for this attack to succeed. This includes the victim systems as well as the attacker and the attacker’s tools or system components. The name of the entity should be accompanied by a brief description of their role in the attack and how they interact with each other.

- **Process Diagram**

These are one or more diagrams of the attack to visually explain how the attack is executed. This diagram can take whatever form is appropriate but it is recommended that the diagram be similar to a system or class diagram showing data flows and the components involved.

- **Dependencies and Conditions**

Every attack must have some context to operate in and the conditions that make the attack possible. This section describes what conditions are required and what other systems or situations need to be in place in order for the attack to succeed. For example, for the attacker to be able to execute an Integer Overflow attack, they must have access to the vulnerable application. That will be common amongst most of the attacks. However, if the vulnerability only exposes itself when the target is running on a remote RPC server, that would also be a condition that would be noted here.

- **Sample Attack Code**

If it is possible to demonstrate the exploit code, this section provides a location to store the demonstration code. In some cases, such as a Denial of Service attack, specific code may not be possible. However, in Overflow, and Cross Site Scripting type attacks, sample code would be very useful.

- **Existing Exploits**

Exploits can be automated or manual. Automated exploits are often found as viruses, worms and hacking tools. If there are any existing exploits known for the attack this section should be used to list a reference to those exploits. These references can be internal such as corporate knowledge bases, or external such as the various CERT, and Virus databases.

Exploits are not to be confused with vulnerabilities. An Exploit is an automated or manual attack that utilises the vulnerability. It is not a listing of a vulnerability found in a particular product for example.

- **Follow-On Attacks**

Follow-on attacks are any other attacks that may be enabled by this particular attack pattern. For example, a Buffer Overflow attack pattern, is usually followed by Escalation of Privilege attacks, Subversion attacks or setting up for Trojan Horse /Backdoor attacks. This field can be particularly useful when researching an attack and identifying what other potential attacks may have been carried out or set up.

- **Mitigation Types**

The mitigation types are the basic types of mitigation strategies that would be used to prevent the attack pattern. This would commonly refer to Security Patterns and Defensive Coding Patterns. Mitigation Types can also be used as a means of classifying various attack patterns. By classifying Attack Patterns in this manner, libraries can be developed to implement particular mitigation types which can then be used to mitigate entire classes of Attack Patterns. These libraries can then be used and reused throughout various applications to ensure consistent and reliable coverage against particular types of attacks.

- **Recommended Mitigation**

Since this is an attack pattern, the recommended mitigation for the attack can be listed here in brief. Ideally, this will point the user to a more thorough mitigation pattern for this class of attack.

- **Related Patterns**

This section will have a few subsections such as Related Patterns, Mitigation Patterns, Security Patterns, and Architectural Patterns. These are references to patterns that can support, relate to or mitigate the attack and the listing for the related pattern should note that.

An example of related patterns for an Integer Overflow Attack Pattern is:

Mitigation Patterns – Filtered Input Pattern, Self Defending Properties pattern

Related Patterns – Buffer Overflow Pattern

- **Related Alerts, Listings and Publications**

This section lists all the references to related alerts listings and publications such as listings in the Common Vulnerabilities and Exposures list, CERT, SANS, and any related vendor alerts. These listings should be hyperlinked to the online alerts and listings in order to ensure it references the most up to date information possible.

- CVE:
- CWE:
- CERT:

Various Vendor Notification Sites.
