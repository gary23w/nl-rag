---
title: "Countermeasure (computer)"
source: https://en.wikipedia.org/wiki/Countermeasure_(computer)
domain: mitre-d3fend
license: CC-BY-SA-4.0
tags: mitre d3fend, defensive countermeasure knowledge graph, cyber defense technique, att&ck countermeasure mapping, security knowledge graph
fetched: 2026-07-02
---

# Countermeasure (computer)

In computer security a **countermeasure** is an action, device, procedure, or technique that reduces a threat, vulnerability, or attack, eliminating or preventing it by minimizing the harm it can cause. It can also include discovering and reporting vunerabilities so that corrective action can be taken.

The definition is given in IETF RFC 2828 and CNSS Instruction No. 4009 dated 26 April 2010 by the Committee on National Security Systems.

According to the Glossary by InfosecToday, the meaning of countermeasure is:

The deployment of a set of security services to protect against a security threat.

A synonym is security control. In telecommunications, communication countermeasures are defined as security services as part of the OSI Reference model by ITU-T X.800 Recommendation. X.800 and ISO ISO 7498-2 (Information processing systems – Open systems interconnection – Basic Reference Model – Part 2: Security architecture are technically aligned.

The following picture explains the relationships between these concepts and terms:

```
      + - - - - - - - - - - - - +  + - - - - +  + - - - - - - - - - - -+
      | An Attack:              |  |Counter- |  | A System Resource:   |
      | i.e., A Threat Action   |  | measure |  | Target of the Attack |
      | +----------+            |  |         |  | +-----------------+  |
      | | Attacker |<==================||<=========                 |  |
      | |   i.e.,  |   Passive  |  |         |  | |  Vulnerability  |  |
      | | A Threat |<=================>||<========>                 |  |
      | |  Agent   |  or Active |  |         |  | +-------|||-------+  |
      | +----------+   Attack   |  |         |  |         VVV          |
      |                         |  |         |  | Threat Consequences  |
      + - - - - - - - - - - - - +  + - - - - +  + - - - - - - - - - - -+
```

A resource (both physical or logical) can have one or more vulnerabilities that can be exploited by a threat agent in a threat action. The result can potentially compromise the confidentiality, integrity or availability properties of these resources (potentially different than the vulnerable one) of the organization and other involved parties (customers, suppliers). The so-called CIA triad is the basis of information security.

The attack can be active when it attempts to alter system resources or affect their operation: so it compromises integrity or availability. A "passive attack" attempts to learn or make use of information from the system but does not affect system resources, compromising confidentiality.

A threat is a potential for violation of security, which exists when there is a circumstance, capability, action, or event that could breach security and cause harm. That is, a threat is a possible danger enabling the exploitation of a vulnerability. A threat can be either "intentional" (i.e., intelligent; e.g., an individual cracker or a criminal organization) or "accidental" (e.g., the possibility of a computer malfunctioning, or the possibility of an "act of God" such as an earthquake, fire, or tornado).

A set of policies concerned with information security management, the information security management systems (ISMS), has been developed to manage, according to risk management principles, the countermeasures in order to accomplish to a security strategy set up following rules and regulations applicable in a country.

## Countermeasures against physical attacks

If a potential malicious actor has physical access to a computer system, they have a greater chance of inflicting harm upon it.

### Electronic destruction devices

Devices such as a USB Killer may be used to damage or render completely unusable anything with a connection to the motherboard of a computer, such as a USB port, video port, Ethernet port, or serial port. Without proper protection, these devices may result in the destruction of ports, adapter cards, storage devices, RAM, motherboards, CPUs, or anything physically connected to the device attacked, such as monitors, flash drives, or wired switches. These types of devices can even be used to damage smartphones and cars, as well.

This threat can be mitigated by not installing or restricting physical access to easily accessible ports in situations where they are not necessary. A port-closing lock which permanently disables access to a port short of the actual port being disassembled. When it is necessary for a port to be accessible, an optocoupler can allow for a port to send and receive data to a computer or device without a direct electrical connection, preventing the computer or device from receiving any dangerous voltage from an external device.

### Hard drives and storage

In an unsecured scenario, a malicious actor may steal or destroy storage devices such as hard drives or SSDs, resulting in the destruction or theft of valuable data.

If the data of a storage device is no longer necessary, data theft is best prevented against by physically destroying or shredding the storage device.

If the data of a storage device is in use and must be secured, one can use encryption to encrypt the contents of a storage device, or even encrypt the whole storage device save for the master boot record. The device can then be unlocked with a password, biometric authentication, a physical dongle, a network interchange, a one-time password, or any combination thereof. If this device is a boot drive, however, it must be unencrypted in a pre-boot environment so the operating system can be accessed. Striping, or breaking data into chunks stored upon multiple drives which must be assembled in order to access the data, is a possible solution to physical drive theft, provided that the drives are stored in multiple, individually secured locations, and are enough in number that no one drive can be used to piece together meaningful information.

Not to be neglected is the process of adding physical barriers to the storage devices themselves. Locked cases or physically hidden drives, with a limited number of personnel with knowledge and access to the keys or locations, may prove to be a good first line against physical theft.
