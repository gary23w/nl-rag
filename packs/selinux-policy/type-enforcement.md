---
title: "Type enforcement"
source: https://en.wikipedia.org/wiki/Type_enforcement
domain: selinux-policy
license: CC-BY-SA-4.0
tags: selinux type enforcement, security enhanced linux policy, mandatory access control label, domain transition policy
fetched: 2026-07-02
---

# Type enforcement

The concept of **type enforcement** (**TE**), in the field of information technology, is an access control mechanism for regulating access in computer systems. Implementing TE gives priority to mandatory access control (MAC) over discretionary access control (DAC). Access clearance is first given to a subject (e.g. process) accessing objects (e.g. files, records, messages) based on rules defined in an attached security context. A security context in a domain is defined by a domain security policy. In the Linux security module (LSM) in SELinux, the security context is an extended attribute. Type enforcement implementation is a prerequisite for MAC, and a first step before multilevel security (MLS) or its replacement multi categories security (MCS). It is a complement of role-based access control (RBAC).

## Control

Type enforcement implies fine-grained control over the operating system, not only to have control over process execution, but also over domain transition or authorization scheme. This is why it is best implemented as a kernel module, as is the case with SELinux. Using type enforcement is a way to implement the FLASK architecture.

## Access

Using type enforcement, users may (as in Microsoft Active Directory) or may not (as in SELinux) be associated with a Kerberos realm, although the original type enforcement model implies so. It is always necessary to define a TE access matrix containing rules about clearance granted to a given security context, or subject's rights over objects according to an authorization scheme.

## Security

Practically, type enforcement evaluates a set of rules from the source security context of a subject, against a set of rules from the target security context of the object. A clearance decision occurs depending on the TE access description (matrix). Then, DAC or other access control mechanisms (MLS / MCS, ...) apply.

## History

Type enforcement was introduced in the Secure Ada Target architecture in the late 1980s with a full implementation developed in the Logical Coprocessing Kernel (LOCK) system. The Sidewinder Internet Firewall was implemented on a custom version of Unix that incorporated type enforcement.

A variant called *domain type enforcement* was developed in the Trusted MACH system.

The original type enforcement model stated that labels should be attached to subject and object: a “domain label” for a subject and a “type label” for an object. This implementation mechanism was improved by the FLASK architecture, substituting complex structures and implicit relationship. Also, the original TE access matrix was extended to other structures: lattice-based, history-based, environment-based, policy logic... This is a matter of implementation of TE by the various operating systems. In SELinux, TE implementation does not internally distinguish TE-domain from TE-types. It should be considered a weakness of TE original model to specify detailed implementation aspects such as labels and matrix, especially using the terms “domain” and “types” which have other, more generic, widely accepted meanings.
