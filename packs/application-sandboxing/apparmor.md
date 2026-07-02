---
title: "AppArmor"
source: https://en.wikipedia.org/wiki/AppArmor
domain: application-sandboxing
license: CC-BY-SA-4.0
tags: application sandboxing, seccomp filtering, apparmor profile, security enhanced linux, capability based security
fetched: 2026-07-02
---

# AppArmor

**AppArmor** ("Application Armor") is a Linux kernel security module that allows system administrators to restrict programs' capabilities with per-program profiles. Profiles can allow capabilities like network access, raw socket access, and the permission to read, write, or execute files on matching paths. AppArmor supplements the traditional Unix discretionary access control (DAC) model by providing mandatory access control (MAC). It has been partially included in the mainline Linux kernel since version 2.6.36. Canonical has supported the development of AppArmor since 2009.

## Details

In addition to manually creating profiles, AppArmor includes a learning mode, in which profile violations are logged, but not prevented. This log can then be used for generating an AppArmor profile, based on the program's typical behavior.

AppArmor is implemented using the Linux Security Modules (LSM) kernel interface.

AppArmor is offered in part as an alternative to SELinux, which critics consider difficult for administrators to set up and maintain. Unlike SELinux, which is based on applying labels to files, AppArmor works with file paths. Proponents of AppArmor claim that it is less complex and easier for the average user to learn than SELinux. They also claim that AppArmor requires fewer modifications to work with existing systems. For example, SELinux requires a filesystem that supports "security labels", and thus cannot provide access control for files mounted via NFS. AppArmor is filesystem-agnostic.

## History

AppArmor was first used in Immunix Linux 1998–2003. At the time, AppArmor was known as SubDomain, a reference to the ability for a security profile for a specific program to be segmented into different domains, which the program can switch between dynamically. AppArmor was first made available in SLES and openSUSE and was first enabled by default in SLES 10 and in openSUSE 10.1.

In May 2005 Novell acquired Immunix and rebranded SubDomain as AppArmor and began code cleaning and rewriting for the inclusion in the Linux kernel. From 2005 to September 2007, AppArmor was maintained by Novell. SUSE is now the legal owner of the trademarked name AppArmor. openSUSE Tumbleweed transitioned from AppArmor to SELinux for new installation since 11 February 2025, openSUSE Leap 16 switched to SELinux by default as well. AppArmor is still available as install-time selection for users who prefer it.

AppArmor was first successfully ported/packaged for Ubuntu in April 2007. AppArmor became a default package starting in Ubuntu 7.10. In Ubuntu 8.04 it protected only CUPS by default. As of Ubuntu 9.04 more items such as MySQL had installed profiles. AppArmor hardening continued to improve in Ubuntu 9.10 with profiles for its guest session, libvirt virtual machines, Evince (document viewer), and an optional Firefox profile.

AppArmor was integrated into the October 2010, 2.6.36 kernel release.

AppArmor has been integrated to Synology's DSM since 5.1 Beta in 2014.

AppArmor was enabled in Solus Release 3 on 2017/8/15.

AppArmor is enabled by default in Debian 10 (Buster), released in July 2019.

## Other systems

AppArmor represents one of several possible approaches to the problem of restricting the actions that installed software may take.

The SELinux system generally takes an approach similar to AppArmor. One important difference: SELinux identifies file system objects by inode number instead of path. Under AppArmor an inaccessible file may become accessible if a hard link to it is created. This difference may be less important than it once was, as Ubuntu 10.10 and later mitigate this with a security module called Yama, which is also used in other distributions. SELinux's inode-based model has always inherently denied access through newly created hard links because the hard link would be pointing to an inaccessible inode.

SELinux and AppArmor also differ significantly in how they are administered and how they integrate into the system.

Isolation of processes can also be accomplished by mechanisms like virtualization.

In 2007, the Simplified Mandatory Access Control Kernel was introduced.

In 2009, a new solution called Tomoyo was included in Linux 2.6.30; like AppArmor, it also uses path-based access control.
