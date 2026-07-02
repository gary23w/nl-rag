---
title: "Privilege escalation"
source: https://en.wikipedia.org/wiki/Privilege_escalation
domain: authorization-bypass-defense
license: CC-BY-SA-4.0
tags: broken access control, authorization bypass defense, privilege escalation prevention, forced browsing control
fetched: 2026-07-02
---

# Privilege escalation

**Privilege escalation** is the act of exploiting a bug, a design flaw, or a configuration oversight in an operating system or software application to gain elevated access to resources that are normally protected from an application or user. The result is that an application or user with more privileges than intended by the application developer or system administrator can perform unauthorized actions.

## Background

Most computer systems are designed for use with multiple user accounts, each of which has abilities known as privileges. Common privileges include viewing and editing files or modifying system files.

Privilege escalation means users receive privileges they are not entitled to. These privileges can be used to delete files, view private information, or install unwanted programs such as viruses. It usually occurs when a system has a bug that allows security to be bypassed or, alternatively, has flawed design assumptions about how it will be used. Privilege escalation occurs in two forms:

- **Vertical privilege escalation**, also known as *privilege elevation*, where a lower privilege user or application accesses functions or content reserved for higher privilege users or applications (e.g. Internet Banking users can access site administrative functions or the password for a smartphone can be bypassed).
- **Horizontal privilege escalation**, where a normal user accesses functions or content reserved for other normal users (e.g. Internet Banking User A accesses the Internet bank account of User B).

## Vertical

This type of privilege escalation occurs when the user or process is able to obtain a higher level of access than an administrator or system developer intended, possibly by performing kernel-level operations.

### Examples

In some cases, a high-privilege application assumes that it would only be provided with input matching its interface specification, thus doesn't validate this input. Then, an attacker may be able to exploit this assumption, in order to run unauthorized code with the application's privileges:

- Some Windows services are configured to run under the Local System user account. A vulnerability such as a buffer overflow may be used to execute arbitrary code with privilege elevated to Local System. Alternatively, a system service that is impersonating a lesser user can elevate that user's privileges if errors are not handled correctly while the user is being impersonated (e.g. if the user has introduced a malicious error handler)
- Under some legacy versions of the Microsoft Windows operating system, the All Users screensaver runs under the Local System account – any account that can replace the current screensaver binary in the file system or Registry can therefore elevate privileges.
- A Windows Program, such as ProcessHacker2 or System Informer, can be used to run programs like cmd.exe as built-in accounts, also providing access to TrustedInstaller. Another method is to use a kernel driver like winring0.sys to run programs with kernel access. This driver can also be exploited to run programs as an administrator, bypassing UAC.
- In certain versions of the Linux kernel it was possible to write a program that would set its current directory to `/etc/cron.d`, request that a core dump be performed in case it crashes and then have itself killed by another process. The core dump file would have been placed at the program's current directory, that is, `/etc/cron.d`, and `cron` would have treated it as a text file instructing it to run programs on schedule. Because the contents of the file would be under attacker's control, the attacker would be able to execute any program with root privileges.
- Cross Zone Scripting is a type of privilege escalation attack in which a website subverts the security model of web browsers, thus allowing it to run malicious code on client computers.
- There are also situations where an application can use other high privilege services and has incorrect assumptions about how a client could manipulate its use of these services. An application that can execute Command line or shell commands could have a Shell Injection vulnerability if it uses unvalidated input as part of an executed command. An attacker would then be able to run system commands using the application's privileges.
- Texas Instruments calculators (particularly the TI-85 and TI-82) were originally designed to use only interpreted programs written in dialects of TI-BASIC; however, after users discovered bugs that could be exploited to allow native Z-80 code to run on the calculator hardware, TI released programming data to support third-party development. (This did not carry on to the ARM-based TI-Nspire, for which jailbreaks using Ndless have been found but are still actively fought against by Texas Instruments.)
- Some versions of the iPhone allow an unauthorised user to access the phone while it is locked.

### Jailbreaking

### Android

Android phones can be officially rooted by either going through manufacturers controlled process, using an exploit to gain root, or installing a rooting modification. Manufacturers allow rooting through a process they control, while some allow the phone to be rooted simply by pressing specific key combinations at boot time, or by other self-administered methods. Using a manufacturers method almost always factory resets the device, making rooting useless to people who want to view the data, and also voids the warranty permanently, even if the device is derooted and reflashed. Software exploits commonly either target a root-level process that is accessible to the user, by using an exploit specific to the phone's kernel, or using a known Android exploit that has been patched in newer versions; by not upgrading the phone, or intentionally downgrading the version.

### Mitigation strategies

Operating systems and users can use the following strategies to reduce the risk of privilege escalation:

- Data Execution Prevention
- Address space layout randomization (to make it harder for buffer overruns to execute privileged instructions at known addresses in memory)
- Running applications with least privilege (for example by running Internet Explorer with the Administrator SID disabled in the process token) in order to reduce the ability of buffer overrun exploits to abuse the privileges of an elevated user.
- Requiring kernel mode code to be digitally signed.
- Patching
- Use of compilers that trap buffer overruns
- Encryption of software and/or firmware components.
- Use of an operating system with Mandatory Access Controls (MAC) such as SELinux
- Kernel Data Relocation Mechanism (dynamically relocates privilege information in the running kernel, preventing privilege escalation attacks using memory corruption)

Recent research has shown what can effectively provide protection against privilege escalation attacks. These include the proposal of the additional kernel observer (AKO), which specifically prevents attacks focused on OS vulnerabilities. Research shows that AKO is in fact effective against privilege escalation attacks.

## Horizontal

Horizontal privilege escalation occurs when an application allows the attacker to gain access to resources which normally would have been protected from an application or user. The result is that the application performs actions with the same user but different security context than intended by the application developer or system administrator; this is effectively a limited form of privilege escalation (specifically, the unauthorized assumption of the capability of impersonating other users). Compared to the vertical privilege escalation, horizontal requires no upgrading the privilege of accounts. It often relies on the bugs in the system.

### Examples

This problem often occurs in web applications. Consider the following example:

- User A has access to their own bank account in an Internet Banking application.
- User B has access to their own bank account in the same Internet Banking application.
- The vulnerability occurs when User A is able to access User B's bank account by performing some sort of malicious activity.

This malicious activity may be possible due to common web application weaknesses or vulnerabilities.

Potential web application vulnerabilities or situations that may lead to this condition include:

- Predictable session IDs in the user's HTTP cookie
- Session fixation
- Cross-site scripting
- Easily guessable passwords
- Theft or hijacking of session cookies
- Keystroke logging
