---
title: "Domain controller"
source: https://en.wikipedia.org/wiki/Domain_controller
domain: active-directory
license: CC-BY-SA-4.0
tags: active directory, domain controller, group policy, directory service, identity and access management
fetched: 2026-07-02
---

# Domain controller

A **domain controller** (**DC**) is a server that responds to security authentication requests within a computer network domain. It is a network server that is responsible for allowing host access to domain resources. It authenticates users, stores user account information and enforces security policy for a domain. It is most commonly implemented in Microsoft Windows environments (see Domain controller (Windows)), where it is the centerpiece of the Windows Active Directory service. However, non-Windows domain controllers can be established via identity management software such as Samba and Red Hat FreeIPA.

## Software

The software and operating system used to run a domain controller usually consists of several key components shared across platforms. This includes the operating system (usually Windows Server or Linux), an LDAP service (Red Hat Directory Server, etc.), a network time service (ntpd, chrony, etc.), and a computer network authentication protocol (usually Kerberos). Other components, such as a public key infrastructure (Active Directory Certificate Services, DogTag, OpenSSL) service and Domain Name System (Windows DNS or BIND) may also be included on the same server or on another domain-joined server.

## Implementation

Domain controllers are typically deployed as a cluster to ensure high-availability and maximize reliability. In a Windows environment, one domain controller serves as the Primary Domain Controller (PDC) and all other servers promoted to domain controller status in the domain serve as a Backup Domain Controller (BDC). In Unix-based environments, one machine serves as the master domain controller and others serve as replica domain controllers, periodically replicating database information from the main domain controller and storing it in a read-only format.
