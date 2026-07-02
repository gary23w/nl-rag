---
title: "Mandatory access control"
source: https://en.wikipedia.org/wiki/Mandatory_access_control
domain: apparmor-mac
license: CC-BY-SA-4.0
tags: apparmor mandatory access control, path based confinement profile, application confinement policy, linux security module profile
fetched: 2026-07-02
---

# Mandatory access control

In computer security, **mandatory access control** (**MAC**) refers to a type of access control by which a secured environment (e.g., an operating system or a database) constrains the ability of a *subject* or *initiator* to access or modify on an *object* or *target*. In the case of operating systems, the subject is a process or thread, while objects are files, directories, TCP/UDP ports, shared memory segments, or IO devices. Subjects and objects each have a set of security attributes. Whenever a subject attempts to access an object, the operating system kernel examines these security attributes, examines the authorization rules (aka *policy*) in place, and decides whether to grant access. A database management system, in its access control mechanism, can also apply mandatory access control; in this case, the objects are tables, views, procedures, etc.

In mandatory access control, the security policy is centrally controlled by a policy administrator and is guaranteed (in principle) to be enforced for all users. Users cannot override the policy and, for example, grant access to files that would otherwise be restricted. By contrast, discretionary access control (DAC), which also governs the ability of subjects to access objects, allows users the ability to make policy decisions or assign security attributes.

Historically and traditionally, MAC has been closely associated with multilevel security (MLS) and specialized military systems. In this context, MAC implies a high degree of rigor to satisfy the constraints of MLS systems. More recently, however, MAC has deviated out of the MLS niche and has started to become more mainstream. The more recent MAC implementations, such as SELinux and AppArmor for Linux and Mandatory Integrity Control for Windows, allow administrators to focus on issues such as network attacks and malware without the rigor or constraints of MLS.

## History and background

Historically, MAC was strongly associated with multilevel security (MLS) as a means of protecting classified information of the United States. The Trusted Computer System Evaluation Criteria (TCSEC), the seminal work on the subject and often known as the Orange Book, provided the original definition of MAC as "a means of restricting access to objects based on the sensitivity (as represented by a label) of the information contained in the objects and the formal authorization (i.e., clearance) of subjects to access information of such sensitivity". Early implementations of MAC such as Honeywell's SCOMP, USAF's SACDIN, NSA's Blacker, and Boeing's MLS LAN focused on MLS to protect military-oriented security classification levels with robust enforcement.

The word "mandatory" in MAC has acquired a special meaning derived from its use with military systems. In this context, MAC implies an extremely high degree of robustness that assures that the control mechanisms can resist any type of subversion, thereby enabling them to enforce access controls that are mandated by the order of a government such as the Executive Order 12958. Enforcement is supposed to be more imperative than for commercial applications. This precludes enforcement by best-effort mechanisms. Only mechanisms that can provide absolute or near-absolute enforcement of the mandate are acceptable for MAC. This is a tall order and sometimes assumed unrealistic by those unfamiliar with high assurance strategies, and very difficult for those who are.

In some systems, users have the authority to decide whether to grant access to any other user. To allow that, all users have clearances for all data. This is not necessarily true of an MLS system. If individuals or processes exist that may be denied access to any of the data in the system environment, then the system must be trusted to enforce MAC. Since there can be various levels of data classification and user clearances, this implies a quantified scale for robustness. For example, more robustness is indicated for system environments containing classified "Top Secret" information and uncleared users than for one with "Secret" information and users cleared to at least "Confidential." To promote consistency and eliminate subjectivity in degrees of robustness, an extensive scientific analysis and risk assessment of the topic produced a landmark benchmark standardization quantifying security robustness capabilities of systems and mapping them to the degrees of trust warranted for various security environments. The result was documented in CSC-STD-004-85. Two relatively independent components of robustness were defined: *Assurance level* and *functionality*. Both were specified with a degree of precision that warranted significant confidence in certifications based on these criteria.

The Common Criteria standard is based on this science and it intended to preserve the assurance level as EAL levels and the functionality specifications as Protection Profiles. Of these two essential components of objective robustness benchmarks, only EAL levels were faithfully preserved. In one case, TCSEC level C2 (not a MAC-capable category) was fairly faithfully preserved in the Common Criteria, as the Controlled Access Protection Profile (CAPP). MLS Protection Profiles (such as MLSOSPP similar to B2) is more general than B2. They are pursuant to MLS, but lack the detailed implementation requirements of their Orange Book predecessors, focusing more on objectives. This gives certifiers more subjective flexibility in deciding whether the evaluated product’s technical features adequately achieve the objective, potentially eroding consistency of evaluated products and making it easier to attain certification for less trustworthy products. For these reasons, the importance of the technical details of the Protection Profile is critical to determining the suitability of a product.

Such an architecture prevents an authenticated user or process at a specific classification or trust-level from accessing information, processes, or devices in a different level. This provides a containment mechanism of users and processes, both known and unknown. An unknown program might comprise an untrusted application where the system should monitor or control accesses to devices and files.

A few MAC implementations, such as Unisys' Blacker project, were certified robust enough to separate Top Secret from Unclassified late in the last millennium. Their underlying technology became obsolete and they were not refreshed. Today there are no current implementations certified by TCSEC to that level of robust implementation. However, some less robust products exist.

## In operating systems

### Microsoft

Starting with Windows Vista and Server 2008, Microsoft has incorporated Mandatory Integrity Control (MIC) in the Windows operating system, which adds *integrity levels* (IL) to running processes. The goal is to restrict access of less trustworthy processes to sensitive info. MIC defines four integrity levels: Low, medium, high, and system. By default, processes started at medium IL. Elevated processes receive high IL. Child processes, by default, inherit their parent's integrity, although the parent process can launch them with a lower IL. For example, Internet Explorer 7 launches its subprocesses with low IL. Windows controls access to objects based on ILs. Named objects, including files, registry keys or other processes and threads, have an entry in their ACL indicating the minimum IL of the process that can use the object. MIC enforces that a process can write to or delete an object only when its IL is equal to or higher than the object’s IL. Furthermore, to prevent access to sensitive data in memory, processes can’t open processes with a higher IL for read access.

### Apple

Apple Inc. has incorporated an implementation of the TrustedBSD framework in its iOS and macOS operating systems. (The word "mac" in "macOS" is short for "Macintosh" and has nothing to do with the abbreviation of "mandatory access control.") The command-line function `sandbox_init` provides a limited high-level sandboxing interface.

### Google

Version 5.0 and later of the Android operating system, developed by Google, use SELinux (as SEAndroid) to enforce a MAC security model on top of its original UID-based DAC approach.

### Linux family

Linux and many other Unix distributions have MAC for CPU (multi-ring), disk, and memory. While OS software may not manage privileges well, Linux became famous during the 1990s as being more secure and far more stable than non-Unix alternatives. The three main Linux Security Modules implementing MAC are SELinux, AppArmor, and TOMOYO Linux.

Security-Enhanced Linux (SELinux) was originally developed by the NSA and released to the Open Source community in 2000. It is one of the first MAC implementations for Linux and is also one of the most popular. It has been incorporated into Linux kernels since v2.4, and is enabled by default on Android 5.0+, Red Hat Enterprise Linux/Fedora Linux, and SUSE Linux Enterprise/openSUSE. SELinux provides powerful fine-grained control which makes it suitable for high-security environments, but many users find that its power and granularity come with a high degree of complexity and a steep learning curve.

TOMOYO Linux is a lightweight MAC implementation for Linux and Embedded Linux, developed by NTT Data Corporation. It has been merged in Linux Kernel mainline version 2.6.30 in June 2009. Differently from the *label-based* approach used by SELinux, TOMOYO Linux performs a *pathname-based* Mandatory Access Control, separating security domains according to process invocation history, which describes the system behavior. Policy are described in terms of pathnames. A security domain is simply defined by a process call chain, and represented by a string. There are 4 modes: disabled, *learning*, permissive, enforcing. Administrators can assign different modes for different domains. TOMOYO Linux introduced the "learning" mode, in which the accesses occurred in the kernel are automatically analyzed and stored to generate MAC policy: this mode could then be the first step of policy writing, making it easy to customize later.

AppArmor is a MAC implementation which utilizes the Linux Security Modules (LSM) interface of Linux 2.6 and is incorporated into SUSE Linux and Ubuntu 7.10. LSM provides a kernel API that allows modules of kernel code to govern ACL (DAC ACL, access-control lists). AppArmor is not capable of restricting all programs and is optionally in the Linux kernel as of version 2.6.36. SUSE moved to SELinux for new installations since 2025, Ubuntu is using AppArmor by default, along with Debian and Solus.

Amon Ott's RSBAC (Rule Set Based Access Control) provides a framework for Linux kernels that allows several different security policy / decision modules. One of the models implemented is Mandatory Access Control model. A general goal of RSBAC design was to try to reach (obsolete) Orange Book (TCSEC) B1 level. The model of mandatory access control used in RSBAC is mostly the same as in Unix System V/MLS, Version 1.2.1 (developed in 1989 by the National Computer Security Center of the USA with classification B1/TCSEC). RSBAC requires a set of patches to the stock kernel, which are maintained quite well by the project owner.

Smack (Simplified Mandatory Access Control Kernel) is a Linux kernel security module that protects data and process interaction from malicious manipulation using a set of custom mandatory access control rules, with simplicity as its main design goal. It has been officially merged since the Linux 2.6.25 release.

`grsecurity` is a patch for the Linux kernel providing a MAC implementation (precisely, it is an RBAC implementation). `grsecurity` is not implemented via the LSM API.

Astra Linux OS developed for Russian Army has its own mandatory access control.

### Other OSes

FreeBSD supports *Mandatory Access Control*, implemented as part of the TrustedBSD project. It was introduced in FreeBSD 5.0. Since FreeBSD 7.2, MAC support is enabled by default. The framework is extensible; various MAC modules implement policies such as Biba and multilevel security.

Sun's Trusted Solaris uses a mandatory and system-enforced access control mechanism (MAC), where clearances and labels are used to enforce a security policy. However note that the capability to manage labels does not imply the kernel strength to operate in multilevel security mode. Access to the labels and control mechanisms are not robustly protected from corruption in protected domain maintained by a kernel. The applications a user runs are combined with the security label at which the user works in the session. Access to information, programs and devices are only weakly controlled.
