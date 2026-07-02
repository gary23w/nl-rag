---
title: "SELinux"
source: https://en.wikipedia.org/wiki/Security-Enhanced_Linux
domain: selinux-policy
license: CC-BY-SA-4.0
tags: selinux type enforcement, security enhanced linux policy, mandatory access control label, domain transition policy
fetched: 2026-07-02
---

# SELinux

(Redirected from

Security-Enhanced Linux

)

**Security-Enhanced Linux** (**SELinux**) is a Linux kernel security module that provides a mechanism for supporting access control security policies, including mandatory access controls (MAC).

SELinux is a set of kernel modifications and user-space tools that have been added to various Linux distributions. Its architecture strives to separate enforcement of security decisions from the security policy, and streamlines the amount of software involved with security policy enforcement. The key concepts underlying SELinux can be traced to several earlier projects by the United States National Security Agency (NSA).

## Overview

The NSA Security-enhanced Linux Team describes NSA SELinux as

> a set of patches to the Linux kernel and utilities to provide a strong, flexible, mandatory access control (MAC) architecture into the major subsystems of the kernel. It provides an enhanced mechanism to enforce the separation of information based on confidentiality and integrity requirements, which allows threats of tampering, and bypassing of application security mechanisms, to be addressed and enables the confinement of damage that can be caused by malicious or flawed applications. It includes a set of sample security policy configuration files designed to meet common, general-purpose security goals.

A Linux kernel integrating SELinux enforces mandatory access control policies that confine user programs and system services, as well as access to files and network resources. Limiting privilege to the minimum required to work reduces or eliminates the ability of these programs and daemons to cause harm if faulty or compromised (for example via buffer overflows or misconfigurations). This confinement mechanism operates independently of the traditional Linux (discretionary) access control mechanisms. It has no concept of a "root" superuser, and does not share the well-known shortcomings of the traditional Linux security mechanisms, such as a dependence on setuid/setgid binaries.

The security of an "unmodified" Linux system (a system without SELinux) depends on the correctness of the kernel, of all the privileged applications, and of each of their configurations. A fault in any one of these areas may allow the compromise of the entire system. In contrast, the security of a "modified" system (based on an SELinux kernel) depends primarily on the correctness of the kernel and its security-policy configuration. While problems with the correctness or configuration of applications may allow the limited compromise of individual user programs and system daemons, they do not necessarily pose a threat to the security of other user programs and system daemons or to the security of the system as a whole.

From a purist perspective, SELinux provides a hybrid of concepts and capabilities drawn from mandatory access controls, mandatory integrity controls, role-based access control (RBAC), and type enforcement architecture. Third-party tools enable one to build a variety of security policies.

## History

The earliest work directed toward standardizing an approach providing mandatory and discretionary access controls (MAC and DAC) within a UNIX (more precisely, POSIX) computing environment can be attributed to the National Security Agency's Trusted UNIX (TRUSIX) Working Group, which met from 1987 to 1991 and published one Rainbow Book (#020A), and produced a formal model and associated evaluation evidence prototype (#020B) that was ultimately unpublished.

SELinux was designed to demonstrate the value of mandatory access controls to the Linux community and how such controls could be added to Linux. Originally, the patches that make up SELinux had to be explicitly applied to the Linux kernel source; SELinux was merged into the Linux kernel mainline in the 2.6 series of the Linux kernel.

The NSA, the original primary developer of SELinux, released the first version to the open source development community under the GNU GPL on 22 December 2000. The software was merged into the mainline Linux kernel 2.6.0-test3, released on 8 August 2003. Other significant contributors include Red Hat, Network Associates, Secure Computing Corporation, Tresys Technology, and Trusted Computer Solutions. Experimental ports of the FLASK/TE implementation have been made available via the TrustedBSD Project for the FreeBSD and Darwin operating systems.

Security-Enhanced Linux implements the Flux Advanced Security Kernel (FLASK). Such a kernel contains architectural components prototyped in the Fluke operating system. These provide general support for enforcing many kinds of mandatory access control policies, including those based on the concepts of type enforcement, role-based access control, and multilevel security. FLASK, in turn, was based on DTOS, a Mach-derived Distributed Trusted Operating System developed as a part of earlier research in mandatory access control systems.

### Original and external contributors

A comprehensive list of the original and external contributors to SELinux was hosted at the NSA website until maintenance ceased sometime in 2009. The following list reproduces the original as preserved by the Internet Archive Wayback Machine. The scope of their contributions was listed in the page and has been omitted for brevity, but it can be accessed through the archived copy.

- The National Security Agency (NSA)
- Network Associates Laboratories (NAI Labs)
- The MITRE Corporation
- Secure Computing Corporation (SCC)
- Matt Anderson
- Ryan Bergauer
- Bastian Blank
- Thomas Bleher
- Joshua Brindle
- Russell Coker
- John Dennis
- Janak Desai
- Ulrich Drepper
- Lorenzo Hernandez Garcia-Hierro
- Darrel Goeddel
- Carsten Grohmann
- Steve Grubb
- Ivan Gyurdiev
- Serge Hallyn
- Chad Hanson
- Joerg Hoh
- Trent Jaeger
- Dustin Kirkland
- Kaigai Kohei
- Paul Krumviede
- Joy Latten
- Tom London
- Karl MacMillan
- Brian May
- Frank Mayer
- Todd Miller
- Roland McGrath
- Paul Moore
- James Morris
- Yuichi Nakamura
- Greg Norris
- Eric Paris
- Chris PeBenito
- Red Hat
- Petre Rodan
- Shaun Savage
- Chad Sellers
- Rogelio Serrano Jr.
- Justin Smith
- Manoj Srivastava
- Tresys Technology
- Michael Thompson
- Trusted Computer Solutions
- Tom Vogt
- Reino Wallin
- Dan Walsh
- Colin Walters
- Mark Westerman
- David A. Wheeler
- Venkat Yekkirala
- Catherine Zhang

## Users, policies and security contexts

SELinux users and roles do not have to be related to the actual system users and roles. For every current user or process, SELinux assigns a three string context consisting of a username, role, and domain (or type). This system is more flexible than normally required: as a rule, most of the real users share the same SELinux username, and all access control is managed through the third tag, the domain. The circumstances under which a process is allowed into a certain domain must be configured in the policies. The command `runcon` allows for the launching of a process into an explicitly specified context (user, role, and domain), but SELinux may deny the transition if it is not approved by the policy.

Files, network ports, and other hardware also have an SELinux context, consisting of a name, role (seldom used), and type. In the case of file systems, mapping between files and the security contexts is called labeling. The labeling is defined in policy files but can also be manually adjusted without changing the policies. Hardware types are quite detailed, for instance, `bin_t` (all files in the folder /bin) or `postgresql_port_t` (PostgreSQL port, 5432). The SELinux context for a remote file system can be specified explicitly at mount time.

SELinux adds the `-Z` switch to the shell commands `ls`, `ps`, and some others, allowing the security context of the files or process to be seen.

Typical policy rules consist of explicit permissions, for example, which domains the user must possess to perform certain actions with the given target (read, execute, or, in case of network port, bind or connect), and so on. More complex mappings are also possible, involving roles and security levels.

A typical policy consists of a mapping (labeling) file, a rule file, and an interface file, that define the domain transition. These three files must be compiled together with the SELinux tools to produce a single policy file. The resulting policy file can be loaded into the kernel to make it active. Loading and unloading policies does not require a reboot. The policy files are either hand written or can be generated from the more user friendly SELinux management tool. They are normally tested in permissive mode first, where violations are logged but allowed. The `audit2allow` tool can be used later to produce additional rules that extend the policy to allow all legitimate activities of the application being confined.

## Features

SELinux features include:

- Clean separation of policy from enforcement
- Well-defined policy interfaces
- Support for applications querying the policy and enforcing access control (for example, crond running jobs in the correct context)
- Independence of specific policies and policy languages
- Independence of specific security-label formats and contents
- Individual labels and controls for kernel objects and services
- Support for policy changes
- Separate measures for protecting system integrity (domain-type) and data confidentiality (multilevel security)
- Flexible policy
- Controls over process initialization and inheritance, and program execution
- Controls over file systems, directories, files, and open file descriptors
- Controls over sockets, messages, and network interfaces
- Controls over the use of "capabilities"
- Cached information on access-decisions via the *Access Vector Cache* (AVC)
- Default-deny policy (anything not explicitly specified in the policy is disallowed)

## Adoption

SELinux has been implemented in Android since version 4.3.

Among free community-supported Linux distributions, Fedora was one of the earliest adopters, including support for it by default since Fedora Core 2. Other distributions include support for it such as Debian as of version 9 Stretch release and Ubuntu as of 8.04 Hardy Heron. As of version 11.1, openSUSE contains SELinux "basic enablement". SUSE Linux Enterprise (SLE) 11 features SELinux as a "technology preview".

SELinux is popular in systems based on Linux containers, such as CoreOS Container Linux and rkt. It is useful as an additional security control to help further enforce isolation between deployed containers and their host.

SELinux is available since 2005 as part of Red Hat Enterprise Linux (RHEL) version 4 and all future releases. This presence is also reflected in corresponding versions of derived systems such as CentOS, Scientific Linux, AlmaLinux and Rocky Linux. The supported policy in RHEL4 is targeted policy which aims for maximum ease of use and thus is not as restrictive as it might be. Future versions of RHEL are planned to have more targets in the targeted policy which will mean more restrictive policies. RHEL version 5 introduced multilevel security (MLS) policy for servers only. Fedora Linux 10 introduced a minimum policy, designed for certain platforms such as low-memory devices and virtual machines.

openSUSE Tumbleweed transitioned from AppArmor to SELinux for new installation since 11 February 2025, and SLE/openSUSE Leap 16 was shipped with SELinux by default as well. openSUSE/SLE adopted RHEL/Fedora policies for its SELinux implementation although with some differences. AppArmor is retained for existing Tumbleweed and SLE/openSUSE Leap 15.x installation (users can manually migrate their existing installation to SELinux). AppArmor is also available as an install-time selection for Tumbleweed users, but not on SLE/Leap 16.

## Use case scenarios

SELinux can potentially control which activities a system allows each user, process, and daemon, with very precise specifications. It is used to confine daemons such as database engines or web servers that have clearly defined data access and activity rights. This limits potential harm from a confined daemon that becomes compromised.

Command-line utilities include: `chcon`, `restorecon`, `restorecond`, `runcon`, `secon`, `fixfiles`, `setfiles`, `load_policy`, `booleans`, `getsebool`, `setsebool`, `togglesebool` `setenforce`, `semodule`, `postfix-nochroot`, `check-selinux-installation`, `semodule_package`, `checkmodule`, `selinux-config-enforcing`, `selinuxenabled`, and `selinux-policy-upgrade`

### Examples

To put SELinux into enforcing mode:

setenforce 1

To query the SELinux status:

getenforce

## Comparison with AppArmor

SELinux represents one of several possible approaches to the problem of restricting the actions that installed software can take. Another popular alternative is called AppArmor and is available on SUSE Linux Enterprise Server (SLES), openSUSE, and Debian-based platforms. AppArmor was developed as a component to the now-defunct Immunix Linux platform. Because AppArmor and SELinux differ radically from one another, they form distinct alternatives for software control. Whereas SELinux re-invents certain concepts to provide access to a more expressive set of policy choices, AppArmor was designed to be simple by extending the same administrative semantics used for DAC up to the mandatory access control level.

There are several key differences:

- One important difference is that AppArmor identifies file system objects by path name instead of inode. This means that, for example, a file that is inaccessible may become accessible under AppArmor when a hard link is created to it, while SELinux would deny access through the newly created hard link.
  - As a result, AppArmor can be said not to be a type enforcement system, as files are not assigned a type; instead, they are merely referenced in a configuration file.
- SELinux and AppArmor also differ significantly in how they are administered and how they integrate into the system.
- Since it endeavors to recreate traditional DAC controls with MAC-level enforcement, AppArmor's set of operations is also considerably smaller than those available under most SELinux implementations. For example, AppArmor's set of operations consist of: read, write, append, execute, lock, and link. Most SELinux implementations will support numbers of operations orders of magnitude more than that. For example, SELinux will usually support those same permissions, but also includes controls for mknod, binding to network sockets, implicit use of POSIX capabilities, loading and unloading kernel modules, various means of accessing shared memory, etc.
- There are no controls in AppArmor for categorically bounding POSIX capabilities. Since the current implementation of capabilities contains no notion of a subject for the operation (only the actor and the operation) it is usually the job of the MAC layer to prevent privileged operations on files outside the actor's enforced realm of control (i.e. "Sandbox"). AppArmor can prevent its own policy from being altered, and prevent file systems from being mounted/unmounted, but does nothing to prevent users from stepping outside their approved realms of control.
  - For example, it may be deemed beneficial for help desk employees to change ownership or permissions on certain files even if they don't own them (for example, on a departmental file share). The administrator does not want to give the user(s) root access on the box so they give them `CAP_FOWNER` or `CAP_DAC_OVERRIDE`. Under SELinux the administrator (or platform vendor) can configure SELinux to deny all capabilities to otherwise unconfined users, then create confined domains for the employee to be able to transition into after logging in, one that can exercise those capabilities, but only upon files of the appropriate type.
- There is no notion of multilevel security with AppArmor, thus there is no hard BLP or Biba enforcement available..
- AppArmor configuration is done using solely regular flat files. SELinux (by default in most implementations) uses a combination of flat files (used by administrators and developers to write human readable policy before it's compiled) and extended attributes.
- SELinux supports the concept of a "remote policy server" (configurable via /etc/selinux/semanage.conf) as an alternative source for policy configuration. Central management of AppArmor is usually complicated considerably since administrators must decide between configuration deployment tools being run as root (to allow policy updates) or configured manually on each server.

## Similar systems and enhancements

Isolation of processes can also be accomplished by mechanisms such as virtualization.

The NSA has adopted some of the SELinux concepts in Security-Enhanced Android.

General Dynamics builds and distributes PitBull Trusted Operating System, a multilevel security (MLS) enhancement for Red Hat Enterprise Linux.

Multi-Category Security (MCS) is an enhancement to SELinux for Red Hat Enterprise Linux that allows users to label files with categories, in order to further restrict access through discretionary access control and type enforcement. Categories provide additional compartments within sensitivity levels used by multilevel security (MLS).
