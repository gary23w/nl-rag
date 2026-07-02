---
title: "Attack surface"
source: https://en.wikipedia.org/wiki/Attack_surface
domain: threat-modeling
license: CC-BY-SA-4.0
tags: threat modeling, attack surface analysis, attack tree, data flow diagram, stride threat model
fetched: 2026-07-02
---

# Attack surface

The **attack surface** of a software environment is the sum of the different points (for "attack vectors") where an unauthorized user (the "attacker") can try to enter data to, extract data from, or control a device or critical software in an environment. Keeping the attack surface as small as possible is a basic security measure.

## Elements of an attack surface

Worldwide digital change has accelerated the size, scope, and composition of an organization's attack surface. The size of an attack surface may fluctuate over time, adding and subtracting assets and digital systems (e.g. websites, hosts, cloud and mobile apps, etc.). Attack surface sizes can change rapidly as well. Digital assets eschew the physical requirements of traditional network devices, servers, data centers, and on-premise networks. This leads to attack surfaces changing rapidly, based on the organization's needs and the availability of digital services to accomplish it.

Attack surface scope also varies from organization to organization. With the rise of digital supply chains, interdependencies, and globalization, an organization's attack surface has a broader scope of concern (viz. vectors for cyberattacks). Lastly, the composition of an organization's attack surface consists of small entities linked together in digital relationships and connections to the rest of the internet and organizational infrastructure, including the scope of third-parties, digital supply chain, and even adversary-threat infrastructure.

An attack surface composition can range widely between various organizations, yet often identify many of the same elements, including:

- Autonomous System Numbers (ASNs)
- IP Address and IP Blocks
- Domains and Sub-Domains (direct and third-parties)
- SSL Certificates and Attribution
- WHOIS Records, Contacts, and History
- Host and Host Pair Services and Relationship
- Internet Ports and Services
- NetFlow
- Web Frameworks (PHP, Apache, Java, etc.)
- Web Server Services (email, database, applications)
- Public and Private Cloud

## Understanding an attack surface

Due to the increase in the countless potential vulnerable points each enterprise has, there has been increasing advantage for hackers and attackers as they only need to find one vulnerable point to succeed in their attack.

There are three steps towards understanding and visualizing an attack surface:

**Step 1: Visualize.** Visualizing the system of an enterprise is the first step, by mapping out all the devices, paths and networks.

**Step 2: Find indicators of exposures.** The second step is to correspond each indicator of a vulnerability being potentially exposed to the visualized map in the previous step. Indicators of exposures (IOEs) include "missing security controls in systems and software".

**Step 3: Find indicators of compromise.** This is an indicator that an attack has already succeeded.

## Surface reduction

One approach to improving information security is to reduce the attack surface of a system or software. The basic strategies of attack surface reduction include the following: reduce the amount of code running, reduce entry points available to untrusted users, and eliminate services requested by relatively few users. By having less code available to unauthorized actors, there tend to be fewer failures. By turning off unnecessary functionality, there are fewer security risks.

Although attack surface reduction helps prevent security failures, it does not mitigate the amount of damage an attacker could inflict once a vulnerability is found.
