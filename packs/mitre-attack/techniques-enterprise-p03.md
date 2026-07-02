---
title: "Techniques - Enterprise (part 3/7)"
source: https://attack.mitre.org/techniques/enterprise/
domain: mitre-attack
license: CC-BY-SA-4.0
tags: mitre att&ck, adversary tactics techniques, att&ck framework, cyber kill chain, threat actor behavior
fetched: 2026-07-02
part: 3/7
---

# Techniques - Enterprise

Adversaries may employ a known asymmetric encryption algorithm to conceal command and control traffic rather than relying on any inherent protections provided by a communication protocol. Asymmetric cryptography, also known as public key cryptography, uses a keypair per party: one public that can be freely distributed, and one private. Due to how the keys are generated, the sender encrypts data with the receiver’s public key and the receiver decrypts the data with their private key. This ensures that only the intended recipient can read the encrypted data. Common public key encryption algorithms include RSA and ElGamal.

T1499

Endpoint Denial of Service

Adversaries may perform Endpoint Denial of Service (DoS) attacks to degrade or block the availability of services to users. Endpoint DoS can be performed by exhausting the system resources those services are hosted on or exploiting the system to cause a persistent crash condition. Example services include websites, email services, DNS, and web-based applications. Adversaries have been observed conducting DoS attacks for political purposes and to support other malicious activities, including distraction, hacktivism, and extortion.

.001

OS Exhaustion Flood

Adversaries may launch a denial of service (DoS) attack targeting an endpoint's operating system (OS). A system's OS is responsible for managing the finite resources as well as preventing the entire system from being overwhelmed by excessive demands on its capacity. These attacks do not need to exhaust the actual resources on a system; the attacks may simply exhaust the limits and available resources that an OS self-imposes.

.002

Service Exhaustion Flood

Adversaries may target the different network services provided by systems to conduct a denial of service (DoS). Adversaries often target the availability of DNS and web services, however others have been targeted as well. Web server software can be attacked through a variety of means, some of which apply generally while others are specific to the software being used to provide the service.

.003

Application Exhaustion Flood

Adversaries may target resource intensive features of applications to cause a denial of service (DoS), denying availability to those applications. For example, specific features in web applications may be highly resource intensive. Repeated requests to those features may be able to exhaust system resources and deny access to the application or the server itself.

.004

Application or System Exploitation

Adversaries may exploit software vulnerabilities that can cause an application or system to crash and deny availability to users. Some systems may automatically restart critical applications and services when crashes occur, but they can likely be re-exploited to cause a persistent denial of service (DoS) condition.

T1611

Escape to Host

Adversaries may break out of a container or virtualized environment to gain access to the underlying host. This can allow an adversary access to other containerized or virtualized resources from the host level or to the host itself. In principle, containerized / virtualized resources should provide a clear separation of application functionality and be isolated from the host environment.

T1585

Establish Accounts

Adversaries may create and cultivate accounts with services that can be used during targeting. Adversaries can create accounts that can be used to build a persona to further operations. Persona development consists of the development of public information, presence, history and appropriate affiliations. This development could be applied to social media, website, or other publicly available information that could be referenced and scrutinized for legitimacy over the course of an operation using that persona or identity.

.001

Social Media Accounts

Adversaries may create and cultivate social media accounts that can be used during targeting. Adversaries can create social media accounts that can be used to build a persona to further operations. Persona development consists of the development of public information, presence, history and appropriate affiliations.

.002

Email Accounts

Adversaries may create email accounts that can be used during targeting. Adversaries can use accounts created with email providers to further their operations, such as leveraging them to conduct

Phishing for Information

or

Phishing

. Establishing email accounts may also allow adversaries to abuse free services – such as trial periods – to

Acquire Infrastructure

for follow-on purposes.

.003

Cloud Accounts

Adversaries may create accounts with cloud providers that can be used during targeting. Adversaries can use cloud accounts to further their operations, including leveraging cloud storage services such as Dropbox, MEGA, Microsoft OneDrive, or AWS S3 buckets for

Exfiltration to Cloud Storage

or to

Upload Tool

s. Cloud accounts can also be used in the acquisition of infrastructure, such as

Virtual Private Server

s or

Serverless

infrastructure. Establishing cloud accounts may allow adversaries to develop sophisticated capabilities without managing their own servers.

T1675

ESXi Administration Command

Adversaries may abuse ESXi administration services to execute commands on guest machines hosted within an ESXi virtual environment. Persistent background services on ESXi-hosted VMs, such as the VMware Tools Daemon Service, allow for remote management from the ESXi server. The tools daemon service runs as

vmtoolsd.exe

on Windows guest operating systems,

vmware-tools-daemon

on macOS, and

vmtoolsd

on Linux.

T1546

Event Triggered Execution

Adversaries may establish persistence and/or elevate privileges using system mechanisms that trigger execution based on specific events. Various operating systems have means to monitor and subscribe to events such as logons or other user activity such as running specific applications/binaries. Cloud environments may also support various functions and services that monitor and can be invoked in response to specific cloud events.

.001

Change Default File Association

Adversaries may establish persistence by executing malicious content triggered by a file type association. When a file is opened, the default program used to open the file (also called the file association or handler) is checked. File association selections are stored in the Windows Registry and can be edited by users, administrators, or programs that have Registry access or by administrators using the built-in assoc utility. Applications can modify the file association for a given file extension to call an arbitrary program when a file with the given extension is opened.

.002

Screensaver

Adversaries may establish persistence by executing malicious content triggered by user inactivity. Screensavers are programs that execute after a configurable time of user inactivity and consist of Portable Executable (PE) files with a .scr file extension. The Windows screensaver application scrnsave.scr is located in

C:\Windows\System32\

, and

C:\Windows\sysWOW64\

on 64-bit Windows systems, along with screensavers included with base Windows installations.

.003

Windows Management Instrumentation Event Subscription

Adversaries may establish persistence and elevate privileges by executing malicious content triggered by a Windows Management Instrumentation (WMI) event subscription. WMI can be used to install event filters, providers, consumers, and bindings that execute code when a defined event occurs. Examples of events that may be subscribed to are the wall clock time, user login, or the computer's uptime.

.004

Unix Shell Configuration Modification

Adversaries may establish persistence through executing malicious commands triggered by a user’s shell. User

Unix Shell

s execute several configuration scripts at different points throughout the session based on events. For example, when a user opens a command-line interface or remotely logs in (such as via SSH) a login shell is initiated. The login shell executes scripts from the system (

/etc

) and the user’s home directory (

~/

) to configure the environment. All login shells on a system use /etc/profile when initiated. These configuration scripts run at the permission level of their directory and are often used to set environment variables, create aliases, and customize the user’s environment. When the shell exits or terminates, additional shell scripts are executed to ensure the shell exits appropriately.

.005

Trap

Adversaries may establish persistence by executing malicious content triggered by an interrupt signal. The

trap

command allows programs and shells to specify commands that will be executed upon receiving interrupt signals. A common situation is a script allowing for graceful termination and handling of common keyboard interrupts like

ctrl+c

and

ctrl+d

.

.006

LC_LOAD_DYLIB Addition

Adversaries may establish persistence by executing malicious content triggered by the execution of tainted binaries. Mach-O binaries have a series of headers that are used to perform certain operations when a binary is loaded. The LC_LOAD_DYLIB header in a Mach-O binary tells macOS and OS X which dynamic libraries (dylibs) to load during execution time. These can be added ad-hoc to the compiled binary as long as adjustments are made to the rest of the fields and dependencies. There are tools available to perform these changes.

.007

Netsh Helper DLL

Adversaries may establish persistence by executing malicious content triggered by Netsh Helper DLLs. Netsh.exe (also referred to as Netshell) is a command-line scripting utility used to interact with the network configuration of a system. It contains functionality to add helper DLLs for extending functionality of the utility. The paths to registered netsh.exe helper DLLs are entered into the Windows Registry at

HKLM\SOFTWARE\Microsoft\Netsh

.

.008

Accessibility Features

Adversaries may establish persistence and/or elevate privileges by executing malicious content triggered by accessibility features. Windows contains accessibility features that may be launched with a key combination before a user has logged in (ex: when the user is on the Windows logon screen). An adversary can modify the way these programs are launched to get a command prompt or backdoor without logging in to the system.

.009

AppCert DLLs

Adversaries may establish persistence and/or elevate privileges by executing malicious content triggered by AppCert DLLs loaded into processes. Dynamic-link libraries (DLLs) that are specified in the

AppCertDLLs

Registry key under

HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\

are loaded into every process that calls the ubiquitously used application programming interface (API) functions

CreateProcess

,

CreateProcessAsUser

,

CreateProcessWithLoginW

,

CreateProcessWithTokenW

, or

WinExec

.

.010

AppInit DLLs

Adversaries may establish persistence and/or elevate privileges by executing malicious content triggered by AppInit DLLs loaded into processes. Dynamic-link libraries (DLLs) that are specified in the

AppInit_DLLs

value in the Registry keys

HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Windows

or

HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Windows

are loaded by user32.dll into every process that loads user32.dll. In practice this is nearly every program, since user32.dll is a very common library.

.011

Application Shimming

Adversaries may establish persistence and/or elevate privileges by executing malicious content triggered by application shims. The Microsoft Windows Application Compatibility Infrastructure/Framework (Application Shim) was created to allow for backward compatibility of software as the operating system codebase changes over time. For example, the application shimming feature allows developers to apply fixes to applications (without rewriting code) that were created for Windows XP so that it will work with Windows 10.

.012

Image File Execution Options Injection

Adversaries may establish persistence and/or elevate privileges by executing malicious content triggered by Image File Execution Options (IFEO) debuggers. IFEOs enable a developer to attach a debugger to an application. When a process is created, a debugger present in an application’s IFEO will be prepended to the application’s name, effectively launching the new process under the debugger (e.g.,

C:\dbg\ntsd.exe -g notepad.exe

).

.013

PowerShell Profile

Adversaries may gain persistence and elevate privileges by executing malicious content triggered by PowerShell profiles. A PowerShell profile (

profile.ps1

) is a script that runs when

PowerShell

starts and can be used as a logon script to customize user environments.

.014

Emond

Adversaries may gain persistence and elevate privileges by executing malicious content triggered by the Event Monitor Daemon (emond). Emond is a

Launch Daemon

that accepts events from various services, runs them through a simple rules engine, and takes action. The emond binary at

/sbin/emond

will load any rules from the

/etc/emond.d/rules/

directory and take action once an explicitly defined event takes place.

.015

Component Object Model Hijacking

Adversaries may establish persistence by executing malicious content triggered by hijacked references to Component Object Model (COM) objects. COM is a system within Windows to enable interaction between software components through the operating system. References to various COM objects are stored in the Registry.

.016

Installer Packages

Adversaries may establish persistence and elevate privileges by using an installer to trigger the execution of malicious content. Installer packages are OS specific and contain the resources an operating system needs to install applications on a system. Installer packages can include scripts that run prior to installation as well as after installation is complete. Installer scripts may inherit elevated permissions when executed. Developers often use these scripts to prepare the environment for installation, check requirements, download dependencies, and remove files after installation.

.017

Udev Rules

Adversaries may maintain persistence through executing malicious content triggered using udev rules. Udev is the Linux kernel device manager that dynamically manages device nodes, handles access to pseudo-device files in the

/dev

directory, and responds to hardware events, such as when external devices like hard drives or keyboards are plugged in or removed. Udev uses rule files with

match keys

to specify the conditions a hardware event must meet and

action keys

to define the actions that should follow. Root permissions are required to create, modify, or delete rule files located in

/etc/udev/rules.d/

,

/run/udev/rules.d/

,

/usr/lib/udev/rules.d/

,

/usr/local/lib/udev/rules.d/

, and

/lib/udev/rules.d/

. Rule priority is determined by both directory and by the digit prefix in the rule filename.

.018

Python Startup Hooks

Adversaries may achieve persistence by leveraging Python’s startup mechanisms, including path configuration (

.pth

) files and the

sitecustomize.py

or

usercustomize.py

modules. These files are automatically processed during the initialization of the Python interpreter, allowing for the execution of arbitrary code whenever Python is invoked.

T1668

Exclusive Control

Adversaries who successfully compromise a system may attempt to maintain persistence by "closing the door" behind them – in other words, by preventing other threat actors from initially accessing or maintaining a foothold on the same system.

T1480

Execution Guardrails

Adversaries may use execution guardrails to constrain execution or actions based on adversary supplied and environment specific conditions that are expected to be present on the target. Guardrails ensure that a payload only executes against an intended target and reduces collateral damage from an adversary’s campaign. Values an adversary can provide about a target system or environment to use as guardrails may include specific network share names, attached physical devices, files, joined Active Directory (AD) domains, and local/external IP addresses.

.001

Environmental Keying

Adversaries may environmentally key payloads or other features of malware to evade defenses and constraint execution to a specific target environment. Environmental keying uses cryptography to constrain execution or actions based on adversary supplied environment specific conditions that are expected to be present on the target. Environmental keying is an implementation of

Execution Guardrails

that utilizes cryptographic techniques for deriving encryption/decryption keys from specific types of values in a given computing environment.

.002

Mutual Exclusion

Adversaries may constrain execution or actions based on the presence of a mutex associated with malware. A mutex is a locking mechanism used to synchronize access to a resource. Only one thread or process can acquire a mutex at a given time.

T1048

Exfiltration Over Alternative Protocol

Adversaries may steal data by exfiltrating it over a different protocol than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server.

.001

Exfiltration Over Symmetric Encrypted Non-C2 Protocol

Adversaries may steal data by exfiltrating it over a symmetrically encrypted network protocol other than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server.

.002

Exfiltration Over Asymmetric Encrypted Non-C2 Protocol

Adversaries may steal data by exfiltrating it over an asymmetrically encrypted network protocol other than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server.

.003

Exfiltration Over Unencrypted Non-C2 Protocol

Adversaries may steal data by exfiltrating it over an un-encrypted network protocol other than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server.

T1041

Exfiltration Over C2 Channel

Adversaries may steal data by exfiltrating it over an existing command and control channel. Stolen data is encoded into the normal communications channel using the same protocol as command and control communications.

T1011

Exfiltration Over Other Network Medium

Adversaries may attempt to exfiltrate data over a different network medium than the command and control channel. If the command and control network is a wired Internet connection, the exfiltration may occur, for example, over a WiFi connection, modem, cellular data connection, Bluetooth, or another radio frequency (RF) channel.

.001

Exfiltration Over Bluetooth

Adversaries may attempt to exfiltrate data over Bluetooth rather than the command and control channel. If the command and control network is a wired Internet connection, an adversary may opt to exfiltrate data using a Bluetooth communication channel.

T1052

Exfiltration Over Physical Medium

Adversaries may attempt to exfiltrate data via a physical medium, such as a removable drive. In certain circumstances, such as an air-gapped network compromise, exfiltration could occur via a physical medium or device introduced by a user. Such media could be an external hard drive, USB drive, cellular phone, MP3 player, or other removable storage and processing device. The physical medium or device could be used as the final exfiltration point or to hop between otherwise disconnected systems.

.001

Exfiltration over USB

Adversaries may attempt to exfiltrate data over a USB connected physical device. In certain circumstances, such as an air-gapped network compromise, exfiltration could occur via a USB device introduced by a user. The USB device could be used as the final exfiltration point or to hop between otherwise disconnected systems.

T1567

Exfiltration Over Web Service

Adversaries may use an existing, legitimate external Web service to exfiltrate data rather than their primary command and control channel. Popular Web services acting as an exfiltration mechanism may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to compromise. Firewall rules may also already exist to permit traffic to these services.

.001

Exfiltration to Code Repository

Adversaries may exfiltrate data to a code repository rather than over their primary command and control channel. Code repositories are often accessible via an API (ex: https://api.github.com). Access to these APIs are often over HTTPS, which gives the adversary an additional level of protection.

.002

Exfiltration to Cloud Storage

Adversaries may exfiltrate data to a cloud storage service rather than over their primary command and control channel. Cloud storage services allow for the storage, edit, and retrieval of data from a remote cloud storage server over the Internet.

.003

Exfiltration to Text Storage Sites

Adversaries may exfiltrate data to text storage sites instead of their primary command and control channel. Text storage sites, such as

pastebin[.]com

, are commonly used by developers to share code and other information.

.004

Exfiltration Over Webhook

Adversaries may exfiltrate data to a webhook endpoint rather than over their primary command and control channel. Webhooks are simple mechanisms for allowing a server to push data over HTTP/S to a client without the need for the client to continuously poll the server. Many public and commercial services, such as Discord, Slack, and

webhook.site

, support the creation of webhook endpoints that can be used by other services, such as Github, Jira, or Trello. When changes happen in the linked services (such as pushing a repository update or modifying a ticket), these services will automatically post the data to the webhook endpoint for use by the consuming application.

T1190

Exploit Public-Facing Application

Adversaries may attempt to exploit a weakness in an Internet-facing host or system to initially access a network. The weakness in the system can be a software bug, a temporary glitch, or a misconfiguration.

T1203

Exploitation for Client Execution

Adversaries may exploit software vulnerabilities in client applications to execute code. Vulnerabilities can exist in software due to unsecure coding practices that can lead to unanticipated behavior. Adversaries can take advantage of certain vulnerabilities through targeted exploitation for the purpose of arbitrary code execution. Oftentimes the most valuable exploits to an offensive toolkit are those that can be used to obtain code execution on a remote system because they can be used to gain access to that system. Users will expect to see files related to the applications they commonly used to do work, so they are a useful target for exploit research and development because of their high utility.

T1212

Exploitation for Credential Access

Adversaries may exploit software vulnerabilities in an attempt to collect credentials. Exploitation of a software vulnerability occurs when an adversary takes advantage of a programming error in a program, service, or within the operating system software or kernel itself to execute adversary-controlled code.

T1687

Exploitation for Defense Impairment

Adversaries may exploit vulnerabilities in security software, infrastructure, or defensive components to degrade, disable, or otherwise continue to impair their ability to prevent, detect, or respond to malicious activity.

T1068

Exploitation for Privilege Escalation

Adversaries may exploit software vulnerabilities in an attempt to elevate privileges. Exploitation of a software vulnerability occurs when an adversary takes advantage of a programming error in a program, service, or within the operating system software or kernel itself to execute adversary-controlled code. Security constructs such as permission levels will often hinder access to information and use of certain techniques, so adversaries will likely need to perform privilege escalation to include use of software exploitation to circumvent those restrictions.

T1211

Exploitation for Stealth

Adversaries may exploit vulnerabilities to evade detection by hiding activity, suppressing logging, or operating within trusted or unmonitored components.

T1210

Exploitation of Remote Services

Adversaries may exploit remote services to gain unauthorized access to internal systems once inside of a network. Exploitation of a software vulnerability occurs when an adversary takes advantage of a programming error in a program, service, or within the operating system software or kernel itself to execute adversary-controlled code. A common goal for post-compromise exploitation of remote services is for lateral movement to enable access to a remote system.

T1133

External Remote Services

Adversaries may leverage external-facing remote services to initially access and/or persist within a network. Remote services such as VPNs, Citrix, and other access mechanisms allow users to connect to internal enterprise network resources from external locations. There are often remote service gateways that manage connections and credential authentication for these services. Services such as

Windows Remote Management

and

VNC

can also be used externally.

T1008

Fallback Channels

Adversaries may use fallback or alternate communication channels if the primary channel is compromised or inaccessible in order to maintain reliable command and control and to avoid data transfer thresholds.

T1083

File and Directory Discovery

Adversaries may enumerate files and directories or may search in specific locations of a host or network share for certain information within a file system. Adversaries may use the information from

File and Directory Discovery

during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

T1222

File and Directory Permissions Modification

Adversaries may modify file or directory permissions/attributes to evade access control lists (ACLs) and access protected files. File and directory permissions are commonly managed by ACLs configured by the file or directory owner, or users with the appropriate permissions. File and directory ACL implementations vary by platform, but generally explicitly designate which users or groups can perform which actions (read, write, execute, etc.).

.001

Windows Permissions

Adversaries may modify file or directory permissions/attributes to evade access control lists (ACLs) and access protected files. File and directory permissions are commonly managed by ACLs configured by the file or directory owner, or users with the appropriate permissions. File and directory ACL implementations vary by platform, but generally explicitly designate which users or groups can perform which actions (read, write, execute, etc.).

.002

Linux and Mac Permissions

Adversaries may modify file or directory permissions/attributes to evade access control lists (ACLs) and access protected files. File and directory permissions are commonly managed by ACLs configured by the file or directory owner, or users with the appropriate permissions. File and directory ACL implementations vary by platform, but generally explicitly designate which users or groups can perform which actions (read, write, execute, etc.).

T1657

Financial Theft

Adversaries may steal monetary resources from targets through extortion, social engineering, technical theft, or other methods aimed at their own financial gain at the expense of the availability of these resources for victims. Financial theft is the ultimate objective of several popular campaign types including extortion by ransomware, business email compromise (BEC) and fraud, "pig butchering," bank hacking, and exploiting cryptocurrency networks.

T1495

Firmware Corruption

Adversaries may overwrite or corrupt the flash memory contents of system BIOS or other firmware in devices attached to a system in order to render them inoperable or unable to boot, thus denying the availability to use the devices and/or the system. Firmware is software that is loaded and executed from non-volatile memory on hardware devices in order to initialize and manage device functionality. These devices may include the motherboard, hard drive, or video cards.

T1187

Forced Authentication

Adversaries may gather credential material by invoking or forcing a user to automatically provide authentication information through a mechanism in which they can intercept.

T1606

Forge Web Credentials

Adversaries may forge credential materials that can be used to gain access to web applications or Internet services. Web applications and services (hosted in cloud SaaS environments or on-premise servers) often use session cookies, tokens, or other materials to authenticate and authorize user access.

.001

Web Cookies

Adversaries may forge web cookies that can be used to gain access to web applications or Internet services. Web applications and services (hosted in cloud SaaS environments or on-premise servers) often use session cookies to authenticate and authorize user access.

.002

SAML Tokens

An adversary may forge SAML tokens with any permissions claims and lifetimes if they possess a valid SAML token-signing certificate. The default lifetime of a SAML token is one hour, but the validity period can be specified in the

NotOnOrAfter

value of the

conditions ...

element in a token. This value can be changed using the

AccessTokenLifetime

in a

LifetimeTokenPolicy

. Forged SAML tokens enable adversaries to authenticate across services that use SAML 2.0 as an SSO (single sign-on) mechanism.

T1592

Gather Victim Host Information

Adversaries may gather information about the victim's hosts that can be used during targeting. Information about hosts may include a variety of details, including administrative data (ex: name, assigned IP, functionality, etc.) as well as specifics regarding its configuration (ex: operating system, language, etc.).

.001

Hardware

Adversaries may gather information about the victim's host hardware that can be used during targeting. Information about hardware infrastructure may include a variety of details such as types and versions on specific hosts, as well as the presence of additional components that might be indicative of added defensive protections (ex: card/biometric readers, dedicated encryption hardware, etc.).

.002

Software

Adversaries may gather information about the victim's host software that can be used during targeting. Information about installed software may include a variety of details such as types and versions on specific hosts, as well as the presence of additional components that might be indicative of added defensive protections (ex: antivirus, SIEMs, etc.).

.003

Firmware

Adversaries may gather information about the victim's host firmware that can be used during targeting. Information about host firmware may include a variety of details such as type and versions on specific hosts, which may be used to infer more information about hosts in the environment (ex: configuration, purpose, age/patch level, etc.).

.004

Client Configurations

Adversaries may gather information about the victim's client configurations that can be used during targeting. Information about client configurations may include a variety of details and settings, including operating system/version, virtualization, architecture (ex: 32 or 64 bit), language, and/or time zone.

T1589

Gather Victim Identity Information

Adversaries may gather information about the victim's identity that can be used during targeting. Information about identities may include a variety of details, including personal data (ex: employee names, email addresses, security question responses, etc.) as well as sensitive details such as credentials or multi-factor authentication (MFA) configurations.

.001

Credentials

Adversaries may gather credentials that can be used during targeting. Account credentials gathered by adversaries may be those directly associated with the target victim organization or attempt to take advantage of the tendency for users to use the same passwords across personal and business accounts.

.002

Email Addresses

Adversaries may gather email addresses that can be used during targeting. Even if internal instances exist, organizations may have public-facing email infrastructure and addresses for employees.

.003

Employee Names

Adversaries may gather employee names that can be used during targeting. Employee names be used to derive email addresses as well as to help guide other reconnaissance efforts and/or craft more-believable lures.

T1590

Gather Victim Network Information

Adversaries may gather information about the victim's networks that can be used during targeting. Information about networks may include a variety of details, including administrative data (ex: IP ranges, domain names, etc.) as well as specifics regarding its topology and operations.

.001

Domain Properties

Adversaries may gather information about the victim's network domain(s) that can be used during targeting. Information about domains and their properties may include a variety of details, including what domain(s) the victim owns as well as administrative data (ex: name, registrar, etc.) and more directly actionable information such as contacts (email addresses and phone numbers), business addresses, and name servers.

.002

DNS

Adversaries may gather information about the victim's DNS that can be used during targeting. DNS information may include a variety of details, including registered name servers as well as records that outline addressing for a target’s subdomains, mail servers, and other hosts. DNS MX, TXT, and SPF records may also reveal the use of third party cloud and SaaS providers, such as Office 365, G Suite, Salesforce, or Zendesk.

.003

Network Trust Dependencies

Adversaries may gather information about the victim's network trust dependencies that can be used during targeting. Information about network trusts may include a variety of details, including second or third-party organizations/domains (ex: managed service providers, contractors, etc.) that have connected (and potentially elevated) network access.

.004

Network Topology

Adversaries may gather information about the victim's network topology that can be used during targeting. Information about network topologies may include a variety of details, including the physical and/or logical arrangement of both external-facing and internal network environments. This information may also include specifics regarding network devices (gateways, routers, etc.) and other infrastructure.

.005

IP Addresses

Adversaries may gather the victim's IP addresses that can be used during targeting. Public IP addresses may be allocated to organizations by block, or a range of sequential addresses. Information about assigned IP addresses may include a variety of details, such as which IP addresses are in use. IP addresses may also enable an adversary to derive other details about a victim, such as organizational size, physical location(s), Internet service provider, and or where/how their publicly-facing infrastructure is hosted.

.006

Network Security Appliances

Adversaries may gather information about the victim's network security appliances that can be used during targeting. Information about network security appliances may include a variety of details, such as the existence and specifics of deployed firewalls, content filters, and proxies/bastion hosts. Adversaries may also target information about victim network-based intrusion detection systems (NIDS) or other appliances related to defensive cybersecurity operations.

T1591

Gather Victim Org Information

Adversaries may gather information about the victim's organization that can be used during targeting. Information about an organization may include a variety of details, including the names of divisions/departments, specifics of business operations, as well as the roles and responsibilities of key employees.

.001

Determine Physical Locations

Adversaries may gather the victim's physical location(s) that can be used during targeting. Information about physical locations of a target organization may include a variety of details, including where key resources and infrastructure are housed. Physical locations may also indicate what legal jurisdiction and/or authorities the victim operates within.

.002

Business Relationships

Adversaries may gather information about the victim's business relationships that can be used during targeting. Information about an organization’s business relationships may include a variety of details, including second or third-party organizations/domains (ex: managed service providers, contractors, etc.) that have connected (and potentially elevated) network access. This information may also reveal supply chains and shipment paths for the victim’s hardware and software resources.

.003

Identify Business Tempo

Adversaries may gather information about the victim's business tempo that can be used during targeting. Information about an organization’s business tempo may include a variety of details, including operational hours/days of the week. This information may also reveal times/dates of purchases and shipments of the victim’s hardware and software resources.

.004

Identify Roles

Adversaries may gather information about identities and roles within the victim organization that can be used during targeting. Information about business roles may reveal a variety of targetable details, including identifiable information for key personnel as well as what data/resources they have access to.

T1683

Generate Content

Adversaries may create or generate content to support targeting and operations. This content may be used to establish personas, impersonate known individuals or organizations, and support

Social Engineering

, fraud, or influence activities. Written materials, audio, images, video, or other media may be developed and tailored to the target and objective.

.001

Written Content

Adversaries may create or tailor written materials to support targeting and malicious operations. Content may include phishing lures, fraudulent financial communications, fabricated job postings, fabricated employment credentials and documentation, decoy documents, social media persona content, and supporting narratives used to sustain fabricated personas over time. Content may be authored manually, commissioned through third parties, or produced using AI-assisted tools.

.002

Audio-Visual Content

Adversaries may create or manipulate audio, image, and video content to support targeting and malicious operations. Adversaries may also use synthetic voice recordings, real-time altered audio or video during live interactions, fabricated profile photos and identity documents, or video content depicting fabricated or impersonated individuals.

T1615

Group Policy Discovery

Adversaries may gather information on Group Policy settings to identify paths for privilege escalation, security measures applied within a domain, and to discover patterns in domain objects that can be manipulated or used to blend in the environment. Group Policy allows for centralized management of user and computer settings in Active Directory (AD). Group policy objects (GPOs) are containers for group policy settings made up of files stored within a predictable network path

\<DOMAIN>\SYSVOL\<DOMAIN>\Policies\

.

T1200

Hardware Additions

Adversaries may physically introduce computer accessories, networking hardware, or other computing devices into a system or network that can be used as a vector to gain access. Rather than just connecting and distributing payloads via removable storage (i.e.

Replication Through Removable Media

), more robust hardware additions can be used to introduce new functionalities and/or features into a system that can then be abused.

T1564

Hide Artifacts

Adversaries may attempt to hide artifacts associated with their behaviors to evade detection. Operating systems may have features to hide various artifacts, such as important system files and administrative task execution, to avoid disrupting user work environments and prevent users from changing files or features on the system. Adversaries may abuse these features to hide artifacts such as files, directories, user accounts, or other system activity to evade detection.

.001

Hidden Files and Directories

Adversaries may set files and directories to be hidden to evade detection mechanisms. To prevent normal users from accidentally changing special files on a system, most operating systems have the concept of a ‘hidden’ file. These files don’t show up when a user browses the file system with a GUI or when using normal commands on the command line. Users must explicitly ask to show the hidden files either via a series of Graphical User Interface (GUI) prompts or with command line switches (

dir /a

for Windows and

ls –a

for Linux and macOS).

.002

Hidden Users

Adversaries may use hidden users to hide the presence of user accounts they create or modify. Administrators may want to hide users when there are many user accounts on a given system or if they want to hide their administrative or other management accounts from other users.

.003

Hidden Window

Adversaries may use hidden windows to conceal malicious activity from the plain sight of users. In some cases, windows that would typically be displayed when an application carries out an operation can be hidden. This may be utilized by system administrators to avoid disrupting user work environments when carrying out administrative tasks.

.004

NTFS File Attributes

Adversaries may use NTFS file attributes to hide their malicious data in order to evade detection. Every New Technology File System (NTFS) formatted partition contains a Master File Table (MFT) that maintains a record for every file/directory on the partition. Within MFT entries are file attributes, such as Extended Attributes (EA) and Data [known as Alternate Data Streams (ADSs) when more than one Data attribute is present], that can be used to store arbitrary data (and even complete files).

.005

Hidden File System

Adversaries may use a hidden file system to conceal malicious activity from users and security tools. File systems provide a structure to store and access data from physical storage. Typically, a user engages with a file system through applications that allow them to access files and directories, which are an abstraction from their physical location (ex: disk sector). Standard file systems include FAT, NTFS, ext4, and APFS. File systems can also contain other structures, such as the Volume Boot Record (VBR) and Master File Table (MFT) in NTFS.

.006

Run Virtual Instance

Adversaries may carry out malicious operations using a virtual instance to avoid detection. A wide variety of virtualization technologies exist that allow for the emulation of a computer or computing environment. By running malicious code inside of a virtual instance, adversaries can hide artifacts associated with their behavior from security tools that are unable to monitor activity inside the virtual instance. Additionally, depending on the virtual networking implementation (ex: bridged adapter), network traffic generated by the virtual instance can be difficult to trace back to the compromised host as the IP address and hostname might not match known values.

.007

VBA Stomping

Adversaries may hide malicious Visual Basic for Applications (VBA) payloads embedded within MS Office documents by replacing the VBA source code with benign data.

.008

Email Hiding Rules

Adversaries may use email rules to hide inbound emails in a compromised user's mailbox. Many email clients allow users to create inbox rules for various email functions, including moving emails to other folders, marking emails as read, or deleting emails. Rules may be created or modified within email clients or through external features such as the

New-InboxRule

or

Set-InboxRule

PowerShell

cmdlets on Windows systems.

.009

Resource Forking

Adversaries may abuse resource forks to hide malicious code or executables to evade detection and bypass security applications. A resource fork provides applications a structured way to store resources such as thumbnail images, menu definitions, icons, dialog boxes, and code. Usage of a resource fork is identifiable when displaying a file’s extended attributes, using

ls -l@

or

xattr -l

commands. Resource forks have been deprecated and replaced with the application bundle structure. Non-localized resources are placed at the top level directory of an application bundle, while localized resources are placed in the

/Resources

folder.

.010

Process Argument Spoofing

Adversaries may attempt to hide process command-line arguments by overwriting process memory. Process command-line arguments are stored in the process environment block (PEB), a data structure used by Windows to store various information about/used by a process. The PEB includes the process command-line arguments that are referenced when executing the process. When a process is created, defensive tools/sensors that monitor process creations may retrieve the process arguments from the PEB.

.011

Ignore Process Interrupts

Adversaries may evade defensive mechanisms by executing commands that hide from process interrupt signals. Many operating systems use signals to deliver messages to control process behavior. Command interpreters often include specific commands/flags that ignore errors and other hangups, such as when the user of the active session logs off. These interrupt signals may also be used by defensive tools and/or analysts to pause or terminate specified running processes.

.012

File/Path Exclusions

Adversaries may attempt to hide their file-based artifacts by writing them to specific folders or file names excluded from antivirus (AV) scanning and other defensive capabilities. AV and other file-based scanners often include exclusions to optimize performance as well as ease installation and legitimate use of applications. These exclusions may be contextual (e.g., scans are only initiated in response to specific triggering events/alerts), but are also often hardcoded strings referencing specific folders and/or files assumed to be trusted and legitimate.

.013

Bind Mounts

Adversaries may abuse bind mounts on file structures to hide their activity and artifacts from native utilities. A bind mount maps a directory or file from one location on the filesystem to another, similar to a shortcut on Windows. It’s commonly used to provide access to specific files or directories across different environments, such as inside containers or chroot environments, and requires sudo access.

.014

Extended Attributes

Adversaries may abuse extended attributes (xattrs) on macOS and Linux to hide their malicious data in order to evade detection. Extended attributes are key-value pairs of file and directory metadata used by both macOS and Linux. They are not visible through standard tools like

Finder

,

ls

, or

cat

and require utilities such as

xattr

(macOS) or

getfattr
