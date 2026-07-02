---
title: "Defense in depth (computing)"
source: https://en.wikipedia.org/wiki/Defense_in_depth_(computing)
domain: security-hardening
license: CC-BY-SA-4.0
tags: security hardening, system hardening baseline, defense in depth, attack surface reduction, data execution prevention
fetched: 2026-07-02
---

# Defense in depth (computing)

**Defense in depth** is a concept used in information security in which multiple layers of security controls (defense) are placed throughout an information technology (IT) system. Its intent is to provide redundancy in the event a security control fails or a vulnerability is exploited.

## Background

The idea behind the defense in depth approach is to defend a system against any particular attack using several independent methods. It is a layering tactic, conceived by the National Security Agency (NSA) as a comprehensive approach to information and electronic security.

Defense in depth is sometimes thought of as forming the layers of an onion, with data at the core of the onion, people the next outer layer of the onion, and network security, host-based security, and application security forming the outermost layers of the onion.

## Tiers

Defense in depth can be divided into three overarching areas: Physical, Technical, and Administrative.

### Physical

Physical controls are anything that physically limits or prevents access to IT systems. Examples of physical defensive security are: fences, guards, dogs, and CCTV systems.

### Technical

Technical controls are hardware or software whose purpose is to protect systems and resources. Examples of technical controls include disk encryption, file integrity software, authentication, network security controls, antiviruses, and behavioural analysis software.

In the event that one layer of defence fails, defense in depth aims to ensure network security via a second-line of defence. For example, if an attacker penetrates a computer system at a given OSI layer (e.g. Layer 3), a redundancy should exist at another layer (Layer 7) to ensure layered defense.

- Authentication, authorization, and accounting
- Confidentiality, integrity, and availability
- Authentication and password security

- Encryption
- Hashing

#### Application security

- Application security
- Web application firewalls

#### Host security

- Vulnerability scanners
- Sandboxing
- Endpoint detection and response

#### Network security

- Logging
- Intrusion detection systems
- Firewalls
- Demilitarized zones
- Network segmentation
- Virtual private network

### Administrative and operational

Administrative controls are the organization's policies and procedures and govern the organisation's human resources, technology, and operations.

#### People

- Multi-factor authentication
- Password policies
- Internet Security Awareness Training

#### Technology

- Patch management
- Risk assessment
- Information assurance

#### Operations

- Principle of least privilege
