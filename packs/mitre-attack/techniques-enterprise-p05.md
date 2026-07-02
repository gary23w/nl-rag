---
title: "Techniques - Enterprise (part 5/7)"
source: https://attack.mitre.org/techniques/enterprise/
domain: mitre-attack
license: CC-BY-SA-4.0
tags: mitre att&ck, adversary tactics techniques, att&ck framework, cyber kill chain, threat actor behavior
fetched: 2026-07-02
part: 5/7
---

# Techniques - Enterprise

Adversaries may use compression to obfuscate their payloads or files. Compressed file formats such as ZIP, gzip, 7z, and RAR can compress and archive multiple files together to make it easier and faster to transfer files. In addition to compressing files, adversaries may also compress shellcode directly - for example, in order to store it in a Windows Registry key (i.e.,

Fileless Storage

).

.016

Junk Code Insertion

Adversaries may use junk code / dead code to obfuscate a malware’s functionality. Junk code is code that either does not execute, or if it does execute, does not change the functionality of the code. Junk code makes analysis more difficult and time-consuming, as the analyst steps through non-functional code instead of analyzing the main code. It also may hinder detections that rely on static code analysis due to the use of benign functionality, especially when combined with

Compression

or

Software Packing

.

.017

SVG Smuggling

Adversaries may smuggle data and files past content filters by hiding malicious payloads inside of seemingly benign SVG files. SVGs, or Scalable Vector Graphics, are vector-based image files constructed using XML. As such, they can legitimately include

<script>

tags that enable adversaries to include malicious JavaScript payloads. However, SVGs may appear less suspicious to users than other types of executable files, as they are often treated as image files.

.018

Invisible Unicode

Adversaries may abuse invisible or non-printing Unicode characters to conceal malicious content within files, scripts, or text. By inserting characters that do not visibly render, adversaries may hide data, alter how content is interpreted, or make malicious code appear as benign text or whitespace. Adversaries may encode these malicious payloads, using binary, Base64, or custom schemes, to be reconstructed at runtime through scripting features such as

JavaScript

Proxy traps,

eval()

, or other dynamic execution methods. This technique enables adversaries to evade visual inspection and basic static analysis by hiding malicious encoded content in innocuous text.

T1588

Obtain Capabilities

Adversaries may buy and/or steal capabilities that can be used during targeting. Rather than developing their own capabilities in-house, adversaries may purchase, freely download, or steal them. Activities may include the acquisition of malware, software (including licenses), exploits, certificates, and information relating to vulnerabilities. Adversaries may obtain capabilities to support their operations throughout numerous phases of the adversary lifecycle.

.001

Malware

Adversaries may buy, steal, or download malware that can be used during targeting. Malicious software can include payloads, droppers, post-compromise tools, backdoors, packers, and C2 protocols. Adversaries may acquire malware to support their operations, obtaining a means for maintaining control of remote machines, evading defenses, and executing post-compromise behaviors.

.002

Tool

Adversaries may buy, steal, or download software tools that can be used during targeting. Tools can be open or closed source, free or commercial. A tool can be used for malicious purposes by an adversary, but (unlike malware) were not intended to be used for those purposes (ex:

PsExec

).

.003

Code Signing Certificates

Adversaries may buy and/or steal code signing certificates that can be used during targeting. Code signing is the process of digitally signing executables and scripts to confirm the software author and guarantee that the code has not been altered or corrupted. Code signing provides a level of authenticity for a program from the developer and a guarantee that the program has not been tampered with. Users and/or security tools may trust a signed piece of code more than an unsigned piece of code even if they don't know who issued the certificate or who the author is.

.004

Digital Certificates

Adversaries may buy and/or steal SSL/TLS certificates that can be used during targeting. SSL/TLS certificates are designed to instill trust. They include information about the key, information about its owner's identity, and the digital signature of an entity that has verified the certificate's contents are correct. If the signature is valid, and the person examining the certificate trusts the signer, then they know they can use that key to communicate with its owner.

.005

Exploits

Adversaries may buy, steal, or download exploits that can be used during targeting. An exploit takes advantage of a bug or vulnerability in order to cause unintended or unanticipated behavior to occur on computer hardware or software. Rather than developing their own exploits, an adversary may find/modify exploits from online or purchase them from exploit vendors.

.006

Vulnerabilities

Adversaries may acquire information about vulnerabilities that can be used during targeting. A vulnerability is a weakness in computer hardware or software that can, potentially, be exploited by an adversary to cause unintended or unanticipated behavior to occur. Adversaries may find vulnerability information by searching open databases or gaining access to closed vulnerability databases.

.007

Artificial Intelligence

Adversaries may obtain access to generative artificial intelligence tools, such as large language models (LLMs), to aid various techniques during targeting. These tools may be used to inform, bolster, and enable a variety of malicious tasks, including conducting

Reconnaissance

, creating basic scripts, assisting social engineering, and even developing payloads.

T1137

Office Application Startup

Adversaries may leverage Microsoft Office-based applications for persistence between startups. Microsoft Office is a fairly common application suite on Windows-based operating systems within an enterprise network. There are multiple mechanisms that can be used with Office for persistence when an Office-based application is started; this can include the use of Office Template Macros and add-ins.

.001

Office Template Macros

Adversaries may abuse Microsoft Office templates to obtain persistence on a compromised system. Microsoft Office contains templates that are part of common Office applications and are used to customize styles. The base templates within the application are used each time an application starts.

.002

Office Test

Adversaries may abuse the Microsoft Office "Office Test" Registry key to obtain persistence on a compromised system. An Office Test Registry location exists that allows a user to specify an arbitrary DLL that will be executed every time an Office application is started. This Registry key is thought to be used by Microsoft to load DLLs for testing and debugging purposes while developing Office applications. This Registry key is not created by default during an Office installation.

.003

Outlook Forms

Adversaries may abuse Microsoft Outlook forms to obtain persistence on a compromised system. Outlook forms are used as templates for presentation and functionality in Outlook messages. Custom Outlook forms can be created that will execute code when a specifically crafted email is sent by an adversary utilizing the same custom Outlook form.

.004

Outlook Home Page

Adversaries may abuse Microsoft Outlook's Home Page feature to obtain persistence on a compromised system. Outlook Home Page is a legacy feature used to customize the presentation of Outlook folders. This feature allows for an internal or external URL to be loaded and presented whenever a folder is opened. A malicious HTML page can be crafted that will execute code when loaded by Outlook Home Page.

.005

Outlook Rules

Adversaries may abuse Microsoft Outlook rules to obtain persistence on a compromised system. Outlook rules allow a user to define automated behavior to manage email messages. A benign rule might, for example, automatically move an email to a particular folder in Outlook if it contains specific words from a specific sender. Malicious Outlook rules can be created that can trigger code execution when an adversary sends a specifically crafted email to that user.

.006

Add-ins

Adversaries may abuse Microsoft Office add-ins to obtain persistence on a compromised system. Office add-ins can be used to add functionality to Office programs. There are different types of add-ins that can be used by the various Office products; including Word/Excel add-in Libraries (WLL/XLL), VBA add-ins, Office Component Object Model (COM) add-ins, automation add-ins, VBA Editor (VBE), Visual Studio Tools for Office (VSTO) add-ins, and Outlook add-ins.

T1003

OS Credential Dumping

Adversaries may attempt to dump credentials to obtain account login and credential material, normally in the form of a hash or a clear text password. Credentials can be obtained from OS caches, memory, or structures. Credentials can then be used to perform

Lateral Movement

and access restricted information.

.001

LSASS Memory

Adversaries may attempt to access credential material stored in the process memory of the Local Security Authority Subsystem Service (LSASS). After a user logs on, the system generates and stores a variety of credential materials in LSASS process memory. These credential materials can be harvested by an administrative user or SYSTEM and used to conduct

Lateral Movement

using

Use Alternate Authentication Material

.

.002

Security Account Manager

Adversaries may attempt to extract credential material from the Security Account Manager (SAM) database either through in-memory techniques or through the Windows Registry where the SAM database is stored. The SAM is a database file that contains local accounts for the host, typically those found with the

net user

command. Enumerating the SAM database requires SYSTEM level access.

.003

NTDS

Adversaries may attempt to access or create a copy of the Active Directory domain database in order to steal credential information, as well as obtain other information about domain members such as devices, users, and access rights. By default, the NTDS file (NTDS.dit) is located in

%SystemRoot%\NTDS\Ntds.dit

of a domain controller.

.004

LSA Secrets

Adversaries with SYSTEM access to a host may attempt to access Local Security Authority (LSA) secrets, which can contain a variety of different credential materials, such as credentials for service accounts. LSA secrets are stored in the registry at

HKEY_LOCAL_MACHINE\SECURITY\Policy\Secrets

. LSA secrets can also be dumped from memory.

.005

Cached Domain Credentials

Adversaries may attempt to access cached domain credentials used to allow authentication to occur in the event a domain controller is unavailable.

.006

DCSync

Adversaries may attempt to access credentials and other sensitive information by abusing a Windows Domain Controller's application programming interface (API) to simulate the replication process from a remote domain controller using a technique called DCSync.

.007

Proc Filesystem

Adversaries may gather credentials from the proc filesystem or

/proc

. The proc filesystem is a pseudo-filesystem used as an interface to kernel data structures for Linux based systems managing virtual memory. For each process, the

/proc/<PID>/maps

file shows how memory is mapped within the process’s virtual address space. And

/proc/<PID>/mem

, exposed for debugging purposes, provides access to the process’s virtual address space.

.008

/etc/passwd and /etc/shadow

Adversaries may attempt to dump the contents of

/etc/passwd

and

/etc/shadow

to enable offline password cracking. Most modern Linux operating systems use a combination of

/etc/passwd

and

/etc/shadow

to store user account information, including password hashes in

/etc/shadow

. By default,

/etc/shadow

is only readable by the root user.

T1201

Password Policy Discovery

Adversaries may attempt to access detailed information about the password policy used within an enterprise network or cloud environment. Password policies are a way to enforce complex passwords that are difficult to guess or crack through

Brute Force

. This information may help the adversary to create a list of common passwords and launch dictionary and/or brute force attacks which adheres to the policy (e.g. if the minimum password length should be 8, then not trying passwords such as 'pass123'; not checking for more than 3-4 passwords per account if the lockout is set to 6 as to not lock out accounts).

T1120

Peripheral Device Discovery

Adversaries may attempt to gather information about attached peripheral devices and components connected to a computer system. Peripheral devices could include auxiliary resources that support a variety of functionalities such as keyboards, printers, cameras, smart card readers, or removable storage. The information may be used to enhance their awareness of the system and network environment or may be used for further actions.

T1069

Permission Groups Discovery

Adversaries may attempt to discover group and permission settings. This information can help adversaries determine which user accounts and groups are available, the membership of users in particular groups, and which users and groups have elevated permissions.

.001

Local Groups

Adversaries may attempt to find local system groups and permission settings. The knowledge of local system permission groups can help adversaries determine which groups exist and which users belong to a particular group. Adversaries may use this information to determine which users have elevated permissions, such as the users found within the local administrators group.

.002

Domain Groups

Adversaries may attempt to find domain-level groups and permission settings. The knowledge of domain-level permission groups can help adversaries determine which groups exist and which users belong to a particular group. Adversaries may use this information to determine which users have elevated permissions, such as domain administrators.

.003

Cloud Groups

Adversaries may attempt to find cloud groups and permission settings. The knowledge of cloud permission groups can help adversaries determine the particular roles of users and groups within an environment, as well as which users are associated with a particular group.

T1566

Phishing

Adversaries may send phishing messages to gain access to victim systems. All forms of phishing are electronically delivered social engineering. Phishing can be targeted, known as spearphishing. In spearphishing, a specific individual, company, or industry will be targeted by the adversary. More generally, adversaries can conduct non-targeted phishing, such as in mass malware spam campaigns.

.001

Spearphishing Attachment

Adversaries may send spearphishing emails with a malicious attachment in an attempt to gain access to victim systems. Spearphishing attachment is a specific variant of spearphishing. Spearphishing attachment is different from other forms of spearphishing in that it employs the use of malware attached to an email. All forms of spearphishing are electronically delivered social engineering targeted at a specific individual, company, or industry. In this scenario, adversaries attach a file to the spearphishing email and usually rely upon

User Execution

to gain execution. Spearphishing may also involve social engineering techniques, such as posing as a trusted source.

.002

Spearphishing Link

Adversaries may send spearphishing emails with a malicious link in an attempt to gain access to victim systems. Spearphishing with a link is a specific variant of spearphishing. It is different from other forms of spearphishing in that it employs the use of links to download malware contained in email, instead of attaching malicious files to the email itself, to avoid defenses that may inspect email attachments. Spearphishing may also involve social engineering techniques, such as posing as a trusted source.

.003

Spearphishing via Service

Adversaries may send spearphishing messages via third-party services in an attempt to gain access to victim systems. Spearphishing via service is a specific variant of spearphishing. It is different from other forms of spearphishing in that it employs the use of third party services rather than directly via enterprise email channels.

.004

Spearphishing Voice

Adversaries may use voice communications to ultimately gain access to victim systems. Spearphishing voice is a specific variant of spearphishing. It is different from other forms of spearphishing in that it employs the use of manipulating a user into providing access to systems through a phone call or other forms of voice communications. Spearphishing frequently involves social engineering techniques, such as posing as a trusted source (ex:

Impersonation

) and/or creating a sense of urgency or alarm for the recipient.

T1598

Phishing for Information

Adversaries may send phishing messages to elicit sensitive information that can be used during targeting. Phishing for information is an attempt to trick targets into divulging information, frequently credentials or other actionable information. Phishing for information is different from

Phishing

in that the objective is gathering data from the victim rather than executing malicious code.

.001

Spearphishing Service

Adversaries may send spearphishing messages via third-party services to elicit sensitive information that can be used during targeting. Spearphishing for information is an attempt to trick targets into divulging information, frequently credentials or other actionable information. Spearphishing for information frequently involves social engineering techniques, such as posing as a source with a reason to collect information (ex:

Establish Accounts

or

Compromise Accounts

) and/or sending multiple, seemingly urgent messages.

.002

Spearphishing Attachment

Adversaries may send spearphishing messages with a malicious attachment to elicit sensitive information that can be used during targeting. Spearphishing for information is an attempt to trick targets into divulging information, frequently credentials or other actionable information. Spearphishing for information frequently involves social engineering techniques, such as posing as a source with a reason to collect information (ex:

Establish Accounts

or

Compromise Accounts

) and/or sending multiple, seemingly urgent messages.

.003

Spearphishing Link

Adversaries may send spearphishing messages with a malicious link to elicit sensitive information that can be used during targeting. Spearphishing for information is an attempt to trick targets into divulging information, frequently credentials or other actionable information. Spearphishing for information frequently involves social engineering techniques, such as posing as a source with a reason to collect information (ex:

Establish Accounts

or

Compromise Accounts

) and/or sending multiple, seemingly urgent messages.

.004

Spearphishing Voice

Adversaries may use voice communications to elicit sensitive information that can be used during targeting. Spearphishing for information is an attempt to trick targets into divulging information, frequently credentials or other actionable information. Spearphishing for information frequently involves social engineering techniques, such as posing as a source with a reason to collect information (ex:

Impersonation

) and/or creating a sense of urgency or alarm for the recipient.

T1647

Plist File Modification

Adversaries may modify property list files (plist files) to enable other malicious activity, while also potentially evading and bypassing system defenses. macOS applications use plist files, such as the

info.plist

file, to store properties and configuration settings that inform the operating system how to handle the application at runtime. Plist files are structured metadata in key-value pairs formatted in XML based on Apple's Core Foundation DTD. Plist files can be saved in text or binary format.

T1677

Poisoned Pipeline Execution

Adversaries may manipulate continuous integration / continuous development (CI/CD) processes by injecting malicious code into the build process. There are several mechanisms for poisoning pipelines:

T1653

Power Settings

Adversaries may impair a system's ability to hibernate, reboot, or shut down in order to extend access to infected machines. When a computer enters a dormant state, some or all software and hardware may cease to operate which can disrupt malicious activity.

T1542

Pre-OS Boot

Adversaries may abuse Pre-OS Boot mechanisms as a way to establish persistence on a system. During the booting process of a computer, firmware and various startup services are loaded before the operating system. These programs control flow of execution before the operating system takes control.

.001

System Firmware

Adversaries may modify system firmware to persist on systems.The BIOS (Basic Input/Output System) and The Unified Extensible Firmware Interface (UEFI) or Extensible Firmware Interface (EFI) are examples of system firmware that operate as the software interface between the operating system and hardware of a computer.

.002

Component Firmware

Adversaries may modify component firmware to persist on systems. Some adversaries may employ sophisticated means to compromise computer components and install malicious firmware that will execute adversary code outside of the operating system and main system firmware or BIOS. This technique may be similar to

System Firmware

but conducted upon other system components/devices that may not have the same capability or level of integrity checking.

.003

Bootkit

Adversaries may use bootkits to persist on systems. A bootkit is a malware variant that modifies the boot sectors of a hard drive, allowing malicious code to execute before a computer's operating system has loaded. Bootkits reside at a layer below the operating system and may make it difficult to perform full remediation unless an organization suspects one was used and can act accordingly.

.004

ROMMONkit

Adversaries may abuse the ROM Monitor (ROMMON) by loading an unauthorized firmware with adversary code to provide persistent access and manipulate device behavior that is difficult to detect.

.005

TFTP Boot

Adversaries may abuse netbooting to load an unauthorized network device operating system from a Trivial File Transfer Protocol (TFTP) server. TFTP boot (netbooting) is commonly used by network administrators to load configuration-controlled network device images from a centralized management server. Netbooting is one option in the boot sequence and can be used to centralize, manage, and control device images.

T1690

Prevent Command History Logging

Adversaries may impair command history logging to hide commands they run on a compromised system. Various command interpreters keep track of the commands users type in their terminal so that users can retrace what they have done.

T1057

Process Discovery

Adversaries may attempt to get information about running processes on a system. Information obtained could be used to gain an understanding of common software/applications running on systems within the network. Administrator or otherwise elevated access may provide better process details. Adversaries may use the information from

Process Discovery

during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

T1055

Process Injection

Adversaries may inject code into processes in order to evade process-based defenses as well as possibly elevate privileges. Process injection is a method of executing arbitrary code in the address space of a separate live process. Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via process injection may also evade detection from security products since the execution is masked under a legitimate process.

.001

Dynamic-link Library Injection

Adversaries may inject dynamic-link libraries (DLLs) into processes in order to evade process-based defenses as well as possibly elevate privileges. DLL injection is a method of executing arbitrary code in the address space of a separate live process.

.002

Portable Executable Injection

Adversaries may inject portable executables (PE) into processes in order to evade process-based defenses as well as possibly elevate privileges. PE injection is a method of executing arbitrary code in the address space of a separate live process.

.003

Thread Execution Hijacking

Adversaries may inject malicious code into hijacked processes in order to evade process-based defenses as well as possibly elevate privileges. Thread Execution Hijacking is a method of executing arbitrary code in the address space of a separate live process.

.004

Asynchronous Procedure Call

Adversaries may inject malicious code into processes via the asynchronous procedure call (APC) queue in order to evade process-based defenses as well as possibly elevate privileges. APC injection is a method of executing arbitrary code in the address space of a separate live process.

.005

Thread Local Storage

Adversaries may inject malicious code into processes via thread local storage (TLS) callbacks in order to evade process-based defenses as well as possibly elevate privileges. TLS callback injection is a method of executing arbitrary code in the address space of a separate live process.

.008

Ptrace System Calls

Adversaries may inject malicious code into processes via ptrace (process trace) system calls in order to evade process-based defenses as well as possibly elevate privileges. Ptrace system call injection is a method of executing arbitrary code in the address space of a separate live process.

.009

Proc Memory

Adversaries may inject malicious code into processes via the /proc filesystem in order to evade process-based defenses as well as possibly elevate privileges. Proc memory injection is a method of executing arbitrary code in the address space of a separate live process.

.011

Extra Window Memory Injection

Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly elevate privileges. EWM injection is a method of executing arbitrary code in the address space of a separate live process.

.012

Process Hollowing

Adversaries may inject malicious code into suspended and hollowed processes in order to evade process-based defenses. Process hollowing is a method of executing arbitrary code in the address space of a separate live process.

.013

Process Doppelgänging

Adversaries may inject malicious code into process via process doppelgänging in order to evade process-based defenses as well as possibly elevate privileges. Process doppelgänging is a method of executing arbitrary code in the address space of a separate live process.

.014

VDSO Hijacking

Adversaries may inject malicious code into processes via VDSO hijacking in order to evade process-based defenses as well as possibly elevate privileges. Virtual dynamic shared object (vdso) hijacking is a method of executing arbitrary code in the address space of a separate live process.

.015

ListPlanting

Adversaries may abuse list-view controls to inject malicious code into hijacked processes in order to evade process-based defenses as well as possibly elevate privileges. ListPlanting is a method of executing arbitrary code in the address space of a separate live process. Code executed via ListPlanting may also evade detection from security products since the execution is masked under a legitimate process.

T1572

Protocol Tunneling

Adversaries may tunnel network communications to and from a victim system within a separate protocol to avoid detection/network filtering and/or enable access to otherwise unreachable systems. Tunneling involves explicitly encapsulating a protocol within another. This behavior may conceal malicious traffic by blending in with existing traffic and/or provide an outer layer of encryption (similar to a VPN). Tunneling could also enable routing of network packets that would otherwise not reach their intended destination, such as SMB, RDP, or other traffic that would be filtered by network appliances or not routed over the Internet.

T1090

Proxy

Adversaries may use a connection proxy to direct network traffic between systems or act as an intermediary for network communications to a command and control server to avoid direct connections to their infrastructure. Many tools exist that enable traffic redirection through proxies or port redirection, including

HTRAN

, ZXProxy, and ZXPortMap. Adversaries use these types of proxies to manage command and control communications, reduce the number of simultaneous outbound network connections, provide resiliency in the face of connection loss, or to ride over existing trusted communications paths between victims to avoid suspicion. Adversaries may chain together multiple proxies to further disguise the source of malicious traffic.

.001

Internal Proxy

Adversaries may use an internal proxy to direct command and control traffic between two or more systems in a compromised environment. Many tools exist that enable traffic redirection through proxies or port redirection, including

HTRAN

, ZXProxy, and ZXPortMap. Adversaries use internal proxies to manage command and control communications inside a compromised environment, to reduce the number of simultaneous outbound network connections, to provide resiliency in the face of connection loss, or to ride over existing trusted communications paths between infected systems to avoid suspicion. Internal proxy connections may use common peer-to-peer (p2p) networking protocols, such as SMB, to better blend in with the environment.

.002

External Proxy

Adversaries may use an external proxy to act as an intermediary for network communications to a command and control server to avoid direct connections to their infrastructure. Many tools exist that enable traffic redirection through proxies or port redirection, including

HTRAN

, ZXProxy, and ZXPortMap. Adversaries use these types of proxies to manage command and control communications, to provide resiliency in the face of connection loss, or to ride over existing trusted communications paths to avoid suspicion.

.003

Multi-hop Proxy

Adversaries may chain together multiple proxies to disguise the source of malicious traffic. Typically, a defender will be able to identify the last proxy traffic traversed before it enters their network; the defender may or may not be able to identify any previous proxies before the last-hop proxy. This technique makes identifying the original source of the malicious traffic even more difficult by requiring the defender to trace malicious traffic through several proxies to identify its source.

.004

Domain Fronting

Adversaries may take advantage of routing schemes in Content Delivery Networks (CDNs) and other services which host multiple domains to obfuscate the intended destination of HTTPS traffic or traffic tunneled through HTTPS. Domain fronting involves using different domain names in the SNI field of the TLS header and the Host field of the HTTP header. If both domains are served from the same CDN, then the CDN may route to the address specified in the HTTP header after unwrapping the TLS header. A variation of the the technique, "domainless" fronting, utilizes a SNI field that is left blank; this may allow the fronting to work even when the CDN attempts to validate that the SNI and HTTP Host fields match (if the blank SNI fields are ignored).

T1682

Query Public AI Services

Adversaries may query publicly accessible artificial intelligence (AI) services, such as large language models (LLMs), to support targeting and operations. In addition to searching websites or databases directly (i.e.,

Search Open Websites/Domains

), adversaries may use AI services to synthesize, aggregate, and analyze publicly available information at scale. This may include identifying individuals or organizations to target, researching organizational structures and personnel, identifying technologies used by target organizations, researching business relationships to develop plausible pretexts for

Social Engineering

approaches, identifying contact information for use in

Phishing

or

Phishing for Information

, or gathering derogatory or sensitive information about individuals that may be used for extortion or coercion.

T1012

Query Registry

Adversaries may interact with the Windows Registry to gather information about the system, configuration, and installed software.

T1620

Reflective Code Loading

Adversaries may reflectively load code into a process in order to conceal the execution of malicious payloads. Reflective loading involves allocating then executing payloads directly within the memory of the process, vice creating a thread or process backed by a file path on disk (e.g.,

Shared Modules

).

T1219

Remote Access Tools

An adversary may use legitimate remote access tools to establish an interactive command and control channel within a network. Remote access tools create a session between two trusted hosts through a graphical interface, a command line interaction, a protocol tunnel via development or management software, or hardware-level access such as KVM (Keyboard, Video, Mouse) over IP solutions. Desktop support software (usually graphical interface) and remote management software (typically command line interface) allow a user to control a computer remotely as if they are a local user inheriting the user or software permissions. This software is commonly used for troubleshooting, software installation, and system management. Adversaries may similarly abuse response features included in EDR and other defensive tools that enable remote access.

.001

IDE Tunneling

Adversaries may abuse Integrated Development Environment (IDE) software with remote development features to establish an interactive command and control channel on target systems within a network. IDE tunneling combines SSH, port forwarding, file sharing, and debugging into a single secure connection, letting developers work on remote systems as if they were local. Unlike SSH and port forwarding, IDE tunneling encapsulates an entire session and may use proprietary tunneling protocols alongside SSH, allowing adversaries to blend in with legitimate development workflows. Some IDEs, like Visual Studio Code, also provide CLI tools (e.g.,

code tunnel

) that adversaries may use to programmatically establish tunnels and generate web-accessible URLs for remote access. These tunnels can be authenticated through accounts such as GitHub, enabling the adversary to control the compromised system via a legitimate developer portal.

.002

Remote Desktop Software

An adversary may use legitimate desktop support software to establish an interactive command and control channel to target systems within networks. Desktop support software provides a graphical interface for remotely controlling another computer, transmitting the display output, keyboard input, and mouse control between devices using various protocols. Desktop support software, such as

VNC

,

Team Viewer

,

AnyDesk

,

ScreenConnect

,

LogMein

,

AmmyyAdmin

, and other remote monitoring and management (RMM) tools, are commonly used as legitimate technical support software and may be allowed by application control within a target environment.

.003

Remote Access Hardware

An adversary may use legitimate remote access hardware to establish an interactive command and control channel to target systems within networks. These services, including IP-based keyboard, video, or mouse (KVM) devices such as TinyPilot and PiKVM, are commonly used as legitimate tools and may be allowed by peripheral device policies within a target environment.

T1563

Remote Service Session Hijacking

Adversaries may take control of preexisting sessions with remote services to move laterally in an environment. Users may use valid credentials to log into a service specifically designed to accept remote connections, such as telnet, SSH, and RDP. When a user logs into a service, a session will be established that will allow them to maintain a continuous interaction with that service.

.001

SSH Hijacking

Adversaries may hijack a legitimate user's SSH session to move laterally within an environment. Secure Shell (SSH) is a standard means of remote access on Linux and macOS systems. It allows a user to connect to another system via an encrypted tunnel, commonly authenticating through a password, certificate or the use of an asymmetric encryption key pair.

.002

RDP Hijacking

Adversaries may hijack a legitimate user’s remote desktop session to move laterally within an environment. Remote desktop is a common feature in operating systems. It allows a user to log into an interactive session with a system desktop graphical user interface on a remote system. Microsoft refers to its implementation of the Remote Desktop Protocol (RDP) as Remote Desktop Services (RDS).

T1021

Remote Services

Adversaries may use

Valid Accounts

to log into a service that accepts remote connections, such as telnet, SSH, and VNC. The adversary may then perform actions as the logged-on user.

.001

Remote Desktop Protocol

Adversaries may use

Valid Accounts

to log into a computer using the Remote Desktop Protocol (RDP). The adversary may then perform actions as the logged-on user.

.002

SMB/Windows Admin Shares

Adversaries may use

Valid Accounts

to interact with a remote network share using Server Message Block (SMB). The adversary may then perform actions as the logged-on user.

.003

Distributed Component Object Model

Adversaries may use

Valid Accounts

to interact with remote machines by taking advantage of Distributed Component Object Model (DCOM). The adversary may then perform actions as the logged-on user.

.004

SSH

Adversaries may use

Valid Accounts

to log into remote machines using Secure Shell (SSH). The adversary may then perform actions as the logged-on user.

.005

VNC

Adversaries may use

Valid Accounts

to remotely control machines using Virtual Network Computing (VNC). VNC is a platform-independent desktop sharing system that uses the RFB ("remote framebuffer") protocol to enable users to remotely control another computer’s display by relaying the screen, mouse, and keyboard inputs over the network.

.006

Windows Remote Management

Adversaries may use

Valid Accounts

to interact with remote systems using Windows Remote Management (WinRM). The adversary may then perform actions as the logged-on user.

.007

Cloud Services

Adversaries may log into accessible cloud services within a compromised environment using

Valid Accounts

that are synchronized with or federated to on-premises user identities. The adversary may then perform management actions or access cloud-hosted resources as the logged-on user.

.008

Direct Cloud VM Connections

Adversaries may leverage

Valid Accounts

to log directly into accessible cloud hosted compute infrastructure through cloud native methods. Many cloud providers offer interactive connections to virtual infrastructure that can be accessed through the

Cloud API

, such as Azure Serial Console, AWS EC2 Instance Connect, and AWS System Manager..

T1018

Remote System Discovery

Adversaries may attempt to get a listing of other systems by IP address, hostname, or other logical identifier on a network that may be used for Lateral Movement from the current system. Functionality could exist within remote access tools to enable this, but utilities available on the operating system could also be used such as

Ping

,

net view

using

Net

, or, on ESXi servers,

esxcli network diag ping

.

T1091

Replication Through Removable Media

Adversaries may move onto systems, possibly those on disconnected or air-gapped networks, by copying malware to removable media and taking advantage of Autorun features when the media is inserted into a system and executes. In the case of Lateral Movement, this may occur through modification of executable files stored on removable media or by copying malware and renaming it to look like a legitimate file to trick users into executing it on a separate system. In the case of Initial Access, this may occur through manual manipulation of the media, modification of systems used to initially format the media, or modification to the media's firmware itself.

T1496

Resource Hijacking

Adversaries may leverage the resources of co-opted systems to complete resource-intensive tasks, which may impact system and/or hosted service availability.

.001

Compute Hijacking

Adversaries may leverage the compute resources of co-opted systems to complete resource-intensive tasks, which may impact system and/or hosted service availability.

.002

Bandwidth Hijacking

Adversaries may leverage the network bandwidth resources of co-opted systems to complete resource-intensive tasks, which may impact system and/or hosted service availability.

.003

SMS Pumping

Adversaries may leverage messaging services for SMS pumping, which may impact system and/or hosted service availability. SMS pumping is a type of telecommunications fraud whereby a threat actor first obtains a set of phone numbers from a telecommunications provider, then leverages a victim’s messaging infrastructure to send large amounts of SMS messages to numbers in that set. By generating SMS traffic to their phone number set, a threat actor may earn payments from the telecommunications provider.

.004

Cloud Service Hijacking

Adversaries may leverage compromised software-as-a-service (SaaS) applications to complete resource-intensive tasks, which may impact hosted service availability.

T1207

Rogue Domain Controller

Adversaries may register a rogue Domain Controller to enable manipulation of Active Directory data. DCShadow may be used to create a rogue Domain Controller (DC). DCShadow is a method of manipulating Active Directory (AD) data, including objects and schemas, by registering (or reusing an inactive registration) and simulating the behavior of a DC. Once registered, a rogue DC may be able to inject and replicate changes into AD infrastructure for any domain object, including credentials and keys.

T1014

Rootkit

Adversaries may use rootkits to hide the presence of programs, files, network connections, services, drivers, and other system components. Rootkits are programs that hide the existence of malware by intercepting/hooking and modifying operating system API calls that supply system information.

T1688

Safe Mode Boot

Adversaries may abuse Windows safe mode to disable endpoint defenses. Safe mode starts up the Windows operating system with a limited set of drivers and services. Third-party security software such as endpoint detection and response (EDR) tools may not start after booting Windows in safe mode. There are two versions of safe mode: Safe Mode and Safe Mode with Networking. It is possible to start additional services after a safe mode boot.

T1053

Scheduled Task/Job

Adversaries may abuse task scheduling functionality to facilitate initial or recurring execution of malicious code. Utilities exist within all major operating systems to schedule programs or scripts to be executed at a specified date and time. A task can also be scheduled on a remote system, provided the proper authentication is met (ex: RPC and file and printer sharing in Windows environments). Scheduling a task on a remote system typically may require being a member of an admin or otherwise privileged group on the remote system.

.002

At

Adversaries may abuse the

at

utility to perform task scheduling for initial or recurring execution of malicious code. The

at

utility exists as an executable within Windows, Linux, and macOS for scheduling tasks at a specified time and date. Although deprecated in favor of

Scheduled Task

's

schtasks

in Windows environments, using

at

requires that the Task Scheduler service be running, and the user to be logged on as a member of the local Administrators group. In addition to explicitly running the

at

command, adversaries may also schedule a task with

at

by directly leveraging the

Windows Management Instrumentation

Win32_ScheduledJob

WMI class.

.003

Cron

Adversaries may abuse the

cron

utility to perform task scheduling for initial or recurring execution of malicious code. The

cron

utility is a time-based job scheduler for Unix-like operating systems. The

crontab

file contains the schedule of cron entries to be run and the specified times for execution. Any

crontab

files are stored in operating system-specific file paths.

.005

Scheduled Task

Adversaries may abuse the Windows Task Scheduler to perform task scheduling for initial or recurring execution of malicious code. There are multiple ways to access the Task Scheduler in Windows. The

schtasks

utility can be run directly on the command line, or the Task Scheduler can be opened through the GUI within the Administrator Tools section of the Control Panel. In some cases, adversaries have used a .NET wrapper for the Windows Task Scheduler, and alternatively, adversaries have used the Windows netapi32 library and

Windows Management Instrumentation

(WMI) to create a scheduled task. Adversaries may also utilize the Powershell Cmdlet

Invoke-CimMethod

, which leverages WMI class

PS_ScheduledTask

to create a scheduled task via an XML path.

.006

Systemd Timers

Adversaries may abuse systemd timers to perform task scheduling for initial or recurring execution of malicious code. Systemd timers are unit files with file extension

.timer

that control services. Timers can be set to run on a calendar event or after a time span relative to a starting point. They can be used as an alternative to

Cron

in Linux environments. Systemd timers may be activated remotely via the

systemctl

command line utility, which operates over

SSH

.

.007

Container Orchestration Job

Adversaries may abuse task scheduling functionality provided by container orchestration tools such as Kubernetes to schedule deployment of containers configured to execute malicious code. Container orchestration jobs run these automated tasks at a specific date and time, similar to cron jobs on a Linux system. Deployments of this type can also be configured to maintain a quantity of containers over time, automating the process of maintaining persistence within a cluster.

T1029

Scheduled Transfer

Adversaries may schedule data exfiltration to be performed only at certain times of day or at certain intervals. This could be done to blend traffic patterns with normal activity or availability.

T1113

Screen Capture

Adversaries may attempt to take screen captures of the desktop to gather information over the course of an operation. Screen capturing functionality may be included as a feature of a remote access tool used in post-compromise operations. Taking a screenshot is also typically possible through native utilities or API calls, such as

CopyFromScreen

,

xwd

, or

screencapture

.

T1597

Search Closed Sources

Adversaries may search and gather information about victims from closed (e.g., paid, private, or otherwise not freely available) sources that can be used during targeting. Information about victims may be available for purchase from reputable private sources and databases, such as paid subscriptions to feeds of technical/threat intelligence data. Adversaries may also purchase information from less-reputable sources such as dark web or cybercrime blackmarkets.

.001

Threat Intel Vendors
