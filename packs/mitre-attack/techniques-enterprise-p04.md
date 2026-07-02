---
title: "Techniques - Enterprise (part 4/7)"
source: https://attack.mitre.org/techniques/enterprise/
domain: mitre-attack
license: CC-BY-SA-4.0
tags: mitre att&ck, adversary tactics techniques, att&ck framework, cyber kill chain, threat actor behavior
fetched: 2026-07-02
part: 4/7
---

# Techniques - Enterprise

(Linux) for inspection. Operating systems and applications use xattrs for tagging, integrity checks, and access control. On Linux, xattrs are organized into namespaces such as

user.

(user permissions),

trusted.

(root permissions),

security.

, and

system.

, each with specific permissions. On macOS, xattrs are flat strings without namespace prefixes, commonly prefixed with

com.apple.*

(e.g.,

com.apple.quarantine

,

com.apple.metadata:_kMDItemUserTags

) and used by system features like Gatekeeper and Spotlight.

T1665

Hide Infrastructure

Adversaries may manipulate network traffic in order to hide and evade detection of their C2 infrastructure. This can be accomplished by identifying and filtering traffic from defensive tools, masking malicious domains to obfuscate the true destination from both automated scanning tools and security researchers, and otherwise hiding malicious artifacts to delay discovery and prolong the effectiveness of adversary infrastructure that could otherwise be identified, blocked, or taken down entirely.

T1574

Hijack Execution Flow

Adversaries may execute their own malicious payloads by hijacking the way operating systems run programs. Hijacking execution flow can be for the purposes of persistence, since this hijacked execution may reoccur over time. Adversaries may also use these mechanisms to elevate privileges or evade defenses, such as application control or other restrictions on execution.

.001

DLL

Adversaries may abuse dynamic-link library files (DLLs) in order to achieve persistence, escalate privileges, and evade defenses. DLLs are libraries that contain code and data that can be simultaneously utilized by multiple programs. While DLLs are not malicious by nature, they can be abused through mechanisms such as side-loading, hijacking search order, and phantom DLL hijacking.

.004

Dylib Hijacking

Adversaries may execute their own payloads by placing a malicious dynamic library (dylib) with an expected name in a path a victim application searches at runtime. The dynamic loader will try to find the dylibs based on the sequential order of the search paths. Paths to dylibs may be prefixed with

@rpath

, which allows developers to use relative paths to specify an array of search paths used at runtime based on the location of the executable. Additionally, if weak linking is used, such as the

LC_LOAD_WEAK_DYLIB

function, an application will still execute even if an expected dylib is not present. Weak linking enables developers to run an application on multiple macOS versions as new APIs are added.

.005

Executable Installer File Permissions Weakness

Adversaries may execute their own malicious payloads by hijacking the binaries used by an installer. These processes may automatically execute specific binaries as part of their functionality or to perform other actions. If the permissions on the file system directory containing a target binary, or permissions on the binary itself, are improperly set, then the target binary may be overwritten with another binary using user-level permissions and executed by the original process. If the original process and thread are running under a higher permissions level, then the replaced binary will also execute under higher-level permissions, which could include SYSTEM.

.006

Dynamic Linker Hijacking

Adversaries may execute their own malicious payloads by hijacking environment variables the dynamic linker uses to load shared libraries. During the execution preparation phase of a program, the dynamic linker loads specified absolute paths of shared libraries from various environment variables and files, such as

LD_PRELOAD

on Linux or

DYLD_INSERT_LIBRARIES

on macOS. Libraries specified in environment variables are loaded first, taking precedence over system libraries with the same function name. Each platform's linker uses an extensive list of environment variables at different points in execution. These variables are often used by developers to debug binaries without needing to recompile, deconflict mapped symbols, and implement custom functions in the original library.

.007

Path Interception by PATH Environment Variable

Adversaries may execute their own malicious payloads by hijacking environment variables used to load libraries. The PATH environment variable contains a list of directories (User and System) that the OS searches sequentially through in search of the binary that was called from a script or the command line.

.008

Path Interception by Search Order Hijacking

Adversaries may execute their own malicious payloads by hijacking the search order used to load other programs. Because some programs do not call other programs using the full path, adversaries may place their own file in the directory where the calling program is located, causing the operating system to launch their malicious software at the request of the calling program.

.009

Path Interception by Unquoted Path

Adversaries may execute their own malicious payloads by hijacking vulnerable file path references. Adversaries can take advantage of paths that lack surrounding quotations by placing an executable in a higher level directory within the path, so that Windows will choose the adversary's executable to launch.

.010

Services File Permissions Weakness

Adversaries may execute their own malicious payloads by hijacking the binaries used by services. Adversaries may use flaws in the permissions of Windows services to replace the binary that is executed upon service start. These service processes may automatically execute specific binaries as part of their functionality or to perform other actions. If the permissions on the file system directory containing a target binary, or permissions on the binary itself are improperly set, then the target binary may be overwritten with another binary using user-level permissions and executed by the original process. If the original process and thread are running under a higher permissions level, then the replaced binary will also execute under higher-level permissions, which could include SYSTEM.

.011

Services Registry Permissions Weakness

Adversaries may execute their own malicious payloads by hijacking the Registry entries used by services. Flaws in the permissions for Registry keys related to services can allow adversaries to redirect the originally specified executable to one they control, launching their own code when a service starts. Windows stores local service configuration information in the Registry under

HKLM\SYSTEM\CurrentControlSet\Services

. The information stored under a service's Registry keys can be manipulated to modify a service's execution parameters through tools such as the service controller, sc.exe,

PowerShell

, or

Reg

. Access to Registry keys is controlled through access control lists and user permissions.

.012

COR_PROFILER

Adversaries may leverage the COR_PROFILER environment variable to hijack the execution flow of programs that load the .NET CLR. The COR_PROFILER is a .NET Framework feature which allows developers to specify an unmanaged (or external of .NET) profiling DLL to be loaded into each .NET process that loads the Common Language Runtime (CLR). These profilers are designed to monitor, troubleshoot, and debug managed code executed by the .NET CLR.

.013

KernelCallbackTable

Adversaries may abuse the

KernelCallbackTable

of a process to hijack its execution flow in order to run their own payloads. The

KernelCallbackTable

can be found in the Process Environment Block (PEB) and is initialized to an array of graphic functions available to a GUI process once

user32.dll

is loaded.

.014

AppDomainManager

Adversaries may execute their own malicious payloads by hijacking how the .NET

AppDomainManager

loads assemblies. The .NET framework uses the

AppDomainManager

class to create and manage one or more isolated runtime environments (called application domains) inside a process to host the execution of .NET applications. Assemblies (

.exe

or

.dll

binaries compiled to run as .NET code) may be loaded into an application domain as executable code.

T1525

Implant Internal Image

Adversaries may implant cloud or container images with malicious code to establish persistence after gaining access to an environment. Amazon Web Services (AWS) Amazon Machine Images (AMIs), Google Cloud Platform (GCP) Images, and Azure Images as well as popular container runtimes such as Docker can be implanted or backdoored. Unlike

Upload Malware

, this technique focuses on adversaries implanting an image in a registry within a victim’s environment. Depending on how the infrastructure is provisioned, this could provide persistent access if the infrastructure provisioning tool is instructed to always use the latest image.

T1070

Indicator Removal

Adversaries may selectively delete or modify artifacts generated to reduce indications of their presence and blend in with legitimate activity. Rather than broadly removing evidence, adversaries may target specific artifacts that appear anomalous or are likely to draw scrutiny, while leaving sufficient data intact to maintain the appearance of normal system behavior.

.003

Clear Command History

In addition to clearing system logs, an adversary may clear the command history of a compromised account to conceal the actions undertaken during an intrusion. Various command interpreters keep track of the commands users type in their terminal so that users can retrace what they've done.

.004

File Deletion

Adversaries may delete files left behind by the actions of their intrusion activity. Malware, tools, or other non-native files dropped or created on a system by an adversary (ex:

Ingress Tool Transfer

) may leave traces to indicate to what was done within a network and how. Removal of these files can occur during an intrusion, or as part of a post-intrusion process to minimize the adversary's footprint.

.005

Network Share Connection Removal

Adversaries may remove share connections that are no longer useful in order to clean up traces of their operation. Windows shared drive and

SMB/Windows Admin Shares

connections can be removed when no longer needed.

Net

is an example utility that can be used to remove network share connections with the

net use \system\share /delete

command.

.006

Timestomp

Adversaries may modify file time attributes to hide new files or changes to existing files. Timestomping is a technique that modifies the timestamps of a file (the modify, access, create, and change times), often to mimic files that are in the same folder and blend malicious files with legitimate files.

.007

Clear Network Connection History and Configurations

Adversaries may clear or remove evidence of malicious network connections in order to clean up traces of their operations. Configuration settings as well as various artifacts that highlight connection history may be created on a system and/or in application logs from behaviors that require network connections, such as

Remote Services

or

External Remote Services

. Defenders may use these artifacts to monitor or otherwise analyze network connections created by adversaries.

.008

Clear Mailbox Data

Adversaries may modify mail and mail application data to remove evidence of their activity. Email applications allow users and other programs to export and delete mailbox data via command line tools or use of APIs. Mail application data can be emails, email metadata, or logs generated by the application or operating system, such as export requests.

.009

Clear Persistence

Adversaries may clear artifacts associated with previously established persistence on a host system to remove evidence of their activity. This may involve various actions, such as removing services, deleting executables,

Modify Registry

,

Plist File Modification

, or other methods of cleanup to prevent defenders from collecting evidence of their persistent presence. Adversaries may also delete accounts previously created to maintain persistence (i.e.

Create Account

).

.010

Relocate Malware

Once a payload is delivered, adversaries may reproduce copies of the same malware on the victim system to remove evidence of their presence and/or avoid defenses. Copying malware payloads to new locations may also be combined with

File Deletion

to cleanup older artifacts.

T1202

Indirect Command Execution

Adversaries may abuse utilities that allow for command execution to bypass security restrictions that limit the use of command-line interpreters. Various Windows utilities may be used to execute commands, possibly without invoking

cmd

. For example,

Forfiles

, the Program Compatibility Assistant (

pcalua.exe

), components of the Windows Subsystem for Linux (WSL),

Scriptrunner.exe

, as well as other utilities may invoke the execution of programs and commands from a

Command and Scripting Interpreter

, Run window, or via scripts. Adversaries may also abuse the

ssh.exe

binary to execute malicious commands via the

ProxyCommand

and

LocalCommand

options, which can be invoked via the

-o

flag or by modifying the SSH config file.

T1105

Ingress Tool Transfer

Adversaries may transfer tools or other files from an external system into a compromised environment. Tools or files may be copied from an external adversary-controlled system to the victim network through the command and control channel or through alternate protocols such as

ftp

. Once present, adversaries may also transfer/spread tools between victim devices within a compromised environment (i.e.

Lateral Tool Transfer

).

T1490

Inhibit System Recovery

Adversaries may delete or remove built-in data and turn off services designed to aid in the recovery of a corrupted system to prevent recovery. This may deny access to available backups and recovery options.

T1056

Input Capture

Adversaries may use methods of capturing user input to obtain credentials or collect information. During normal system usage, users often provide credentials to various different locations, such as login pages/portals or system dialog boxes. Input capture mechanisms may be transparent to the user (e.g.

Credential API Hooking

) or rely on deceiving the user into providing input into what they believe to be a genuine service (e.g.

Web Portal Capture

).

.001

Keylogging

Adversaries may log user keystrokes to intercept credentials as the user types them. Keylogging is likely to be used to acquire credentials for new access opportunities when

OS Credential Dumping

efforts are not effective, and may require an adversary to intercept keystrokes on a system for a substantial period of time before credentials can be successfully captured. In order to increase the likelihood of capturing credentials quickly, an adversary may also perform actions such as clearing browser cookies to force users to reauthenticate to systems.

.002

GUI Input Capture

Adversaries may mimic common operating system GUI components to prompt users for credentials with a seemingly legitimate prompt. When programs are executed that need additional privileges than are present in the current user context, it is common for the operating system to prompt the user for proper credentials to authorize the elevated privileges for the task (ex:

Bypass User Account Control

).

.003

Web Portal Capture

Adversaries may install code on externally facing portals, such as a VPN login page, to capture and transmit credentials of users who attempt to log into the service. For example, a compromised login page may log provided user credentials before logging the user in to the service.

.004

Credential API Hooking

Adversaries may hook into Windows application programming interface (API) functions and Linux system functions to collect user credentials. Malicious hooking mechanisms may capture API or function calls that include parameters that reveal user authentication credentials. Unlike

Keylogging

, this technique focuses specifically on API functions that include parameters that reveal user credentials.

T1674

Input Injection

Adversaries may simulate keystrokes on a victim’s computer by various means to perform any type of action on behalf of the user, such as launching the command interpreter using keyboard shortcuts, typing an inline script to be executed, or interacting directly with a GUI-based application. These actions can be preprogrammed into adversary tooling or executed through physical devices such as Human Interface Devices (HIDs).

T1559

Inter-Process Communication

Adversaries may abuse inter-process communication (IPC) mechanisms for local code or command execution. IPC is typically used by processes to share data, communicate with each other, or synchronize execution. IPC is also commonly used to avoid situations such as deadlocks, which occurs when processes are stuck in a cyclic waiting pattern.

.001

Component Object Model

Adversaries may use the Windows Component Object Model (COM) for local code execution. COM is an inter-process communication (IPC) component of the native Windows application programming interface (API) that enables interaction between software objects, or executable code that implements one or more interfaces. Through COM, a client object can call methods of server objects, which are typically binary Dynamic Link Libraries (DLL) or executables (EXE). Remote COM execution is facilitated by

Remote Services

such as

Distributed Component Object Model

(DCOM).

.002

Dynamic Data Exchange

Adversaries may use Windows Dynamic Data Exchange (DDE) to execute arbitrary commands. DDE is a client-server protocol for one-time and/or continuous inter-process communication (IPC) between applications. Once a link is established, applications can autonomously exchange transactions consisting of strings, warm data links (notifications when a data item changes), hot data links (duplications of changes to a data item), and requests for command execution.

.003

XPC Services

Adversaries can provide malicious content to an XPC service daemon for local code execution. macOS uses XPC services for basic inter-process communication between various processes, such as between the XPC Service daemon and third-party application privileged helper tools. Applications can send messages to the XPC Service daemon, which runs as root, using the low-level XPC Service

C API

or the high level

NSXPCConnection API

in order to handle tasks that require elevated privileges (such as network connections). Applications are responsible for providing the protocol definition which serves as a blueprint of the XPC services. Developers typically use XPC Services to provide applications stability and privilege separation between the application client and the daemon.

T1534

Internal Spearphishing

After they already have access to accounts or systems within the environment, adversaries may use internal spearphishing to gain access to additional information or compromise other users within the same organization. Internal spearphishing is multi-staged campaign where a legitimate account is initially compromised either by controlling the user's device or by compromising the account credentials of the user. Adversaries may then attempt to take advantage of the trusted internal account to increase the likelihood of tricking more victims into falling for phish attempts, often incorporating

Impersonation

.

T1570

Lateral Tool Transfer

Adversaries may transfer tools or other files between systems in a compromised environment. Once brought into the victim environment (i.e.,

Ingress Tool Transfer

) files may then be copied from one system to another to stage adversary tools or other files over the course of an operation.

T1680

Local Storage Discovery

Adversaries may enumerate local drives, disks, and/or volumes and their attributes like total or free space and volume serial number. This can be done to prepare for ransomware-related encryption, to perform

Lateral Movement

, or as a precursor to

Direct Volume Access

.

T1654

Log Enumeration

Adversaries may enumerate system and service logs to find useful data. These logs may highlight various types of valuable insights for an adversary, such as user authentication records (

Account Discovery

), security or vulnerable software (

Software Discovery

), or hosts within a compromised network (

Remote System Discovery

).

T1036

Masquerading

Adversaries may attempt to manipulate features of their artifacts to make them appear legitimate or benign to users and/or security tools. Masquerading occurs when the name or location of an object, legitimate or malicious, is manipulated or abused for the sake of evading defenses and observation. This may include manipulating file metadata, tricking users into misidentifying the file type, and giving legitimate task or service names.

.001

Invalid Code Signature

Adversaries may attempt to mimic features of valid code signatures to increase the chance of deceiving a user, analyst, or tool. Code signing provides a level of authenticity on a binary from the developer and a guarantee that the binary has not been tampered with. Adversaries can copy the metadata and signature information from a signed program, then use it as a template for an unsigned program. Files with invalid code signatures will fail digital signature validation checks, but they may appear more legitimate to users and security tools may improperly handle these files.

.002

Right-to-Left Override

Adversaries may abuse the right-to-left override (RTLO or RLO) character (U+202E) to disguise a string and/or file name to make it appear benign. RTLO is a non-printing Unicode character that causes the text that follows it to be displayed in reverse. For example, a Windows screensaver executable named

March 25 \u202Excod.scr

will display as

March 25 rcs.docx

. A JavaScript file named

photo_high_re\u202Egnp.js

will be displayed as

photo_high_resj.png

.

.003

Rename Legitimate Utilities

Adversaries may rename legitimate / system utilities to try to evade security mechanisms concerning the usage of those utilities. Security monitoring and control mechanisms may be in place for legitimate utilities adversaries are capable of abusing, including both built-in binaries and tools such as PSExec, AutoHotKey, and IronPython. It may be possible to bypass those security mechanisms by renaming the utility prior to utilization (ex: rename

rundll32.exe

). An alternative case occurs when a legitimate utility is copied or moved to a different directory and renamed to avoid detections based on these utilities executing from non-standard paths.

.004

Masquerade Task or Service

Adversaries may attempt to manipulate the name of a task or service to make it appear legitimate or benign. Tasks/services executed by the Task Scheduler or systemd will typically be given a name and/or description. Windows services will have a service name as well as a display name. Many benign tasks and services exist that have commonly associated names. Adversaries may give tasks or services names that are similar or identical to those of legitimate ones.

.005

Match Legitimate Resource Name or Location

Adversaries may match or approximate the name or location of legitimate files, Registry keys, or other resources when naming/placing them. This is done for the sake of evading defenses and observation.

.006

Space after Filename

Adversaries can hide a program's true filetype by changing the extension of a file. With certain file types (specifically this does not work with .app extensions), appending a space to the end of a filename will change how the file is processed by the operating system.

.007

Double File Extension

Adversaries may abuse a double extension in the filename as a means of masquerading the true file type. A file name may include a secondary file type extension that may cause only the first extension to be displayed (ex:

File.txt.exe

may render in some views as just

File.txt

). However, the second extension is the true file type that determines how the file is opened and executed. The real file extension may be hidden by the operating system in the file browser (ex: explorer.exe), as well as in any software configured using or similar to the system’s policies.

.008

Masquerade File Type

Adversaries may masquerade malicious payloads as legitimate files through changes to the payload's formatting, including the file’s signature, extension, icon, and contents. Various file types have a typical standard format, including how they are encoded and organized. For example, a file’s signature (also known as header or magic bytes) is the beginning bytes of a file and is often used to identify the file’s type. For example, the header of a JPEG file, is

0xFF 0xD8

and the file extension is either

.JPE

,

.JPEG

or

.JPG

.

.009

Break Process Trees

An adversary may attempt to evade process tree-based analysis by modifying executed malware's parent process ID (PPID). If endpoint protection software leverages the "parent-child" relationship for detection, breaking this relationship could result in the adversary’s behavior not being associated with previous process tree activity. On Unix-based systems breaking this process tree is common practice for administrators to execute software using scripts and programs.

.010

Masquerade Account Name

Adversaries may match or approximate the names of legitimate accounts to make newly created ones appear benign. This will typically occur during

Create Account

, although accounts may also be renamed at a later date. This may also coincide with

Account Access Removal

if the actor first deletes an account before re-creating one with the same name.

.011

Overwrite Process Arguments

Adversaries may modify a process's in-memory arguments to change its name in order to appear as a legitimate or benign process. On Linux, the operating system stores command-line arguments in the process’s stack and passes them to the

main()

function as the

argv

array. The first element,

argv[0]

, typically contains the process name or path - by default, the command used to actually start the process (e.g.,

cat /etc/passwd

). By default, the Linux

/proc

filesystem uses this value to represent the process name. The

/proc/<PID>/cmdline

file reflects the contents of this memory, and tools like

ps

use it to display process information. Since arguments are stored in user-space memory at launch, this modification can be performed without elevated privileges.

.012

Browser Fingerprint

Adversaries may attempt to blend in with legitimate traffic by spoofing browser and system attributes like operating system, system language, platform, user-agent string, resolution, time zone, etc. The HTTP User-Agent request header is a string that lets servers and network peers identify the application, operating system, vendor, and/or version of the requesting user agent.

T1556

Modify Authentication Process

Adversaries may modify authentication mechanisms and processes to access user credentials or enable otherwise unwarranted access to accounts. The authentication process is handled by mechanisms, such as the Local Security Authentication Server (LSASS) process and the Security Accounts Manager (SAM) on Windows, pluggable authentication modules (PAM) on Unix-based systems, and authorization plugins on MacOS systems, responsible for gathering, storing, and validating credentials. By modifying an authentication process, an adversary may be able to authenticate to a service or system without using

Valid Accounts

.

.001

Domain Controller Authentication

Adversaries may patch the authentication process on a domain controller to bypass the typical authentication mechanisms and enable access to accounts.

.002

Password Filter DLL

Adversaries may register malicious password filter dynamic link libraries (DLLs) into the authentication process to acquire user credentials as they are validated.

.003

Pluggable Authentication Modules

Adversaries may modify pluggable authentication modules (PAM) to access user credentials or enable otherwise unwarranted access to accounts. PAM is a modular system of configuration files, libraries, and executable files which guide authentication for many services. The most common authentication module is

pam_unix.so

, which retrieves, sets, and verifies account authentication information in

/etc/passwd

and

/etc/shadow

.

.004

Network Device Authentication

Adversaries may use

Patch System Image

to hard code a password in the operating system, thus bypassing of native authentication mechanisms for local accounts on network devices.

.005

Reversible Encryption

An adversary may abuse Active Directory authentication encryption properties to gain access to credentials on Windows systems. The

AllowReversiblePasswordEncryption

property specifies whether reversible password encryption for an account is enabled or disabled. By default this property is disabled (instead storing user credentials as the output of one-way hashing functions) and should not be enabled unless legacy or other software require it.

.006

Multi-Factor Authentication

Adversaries may disable or modify multi-factor authentication (MFA) mechanisms to enable persistent access to compromised accounts.

.007

Hybrid Identity

Adversaries may patch, modify, or otherwise backdoor cloud authentication processes that are tied to on-premises user identities in order to bypass typical authentication mechanisms, access credentials, and enable persistent access to accounts.

.008

Network Provider DLL

Adversaries may register malicious network provider dynamic link libraries (DLLs) to capture cleartext user credentials during the authentication process. Network provider DLLs allow Windows to interface with specific network protocols and can also support add-on credential management functions. During the logon process, Winlogon (the interactive logon module) sends credentials to the local

mpnotify.exe

process via RPC. The

mpnotify.exe

process then shares the credentials in cleartext with registered credential managers when notifying that a logon event is happening.

.009

Conditional Access Policies

Adversaries may disable or modify conditional access policies to enable persistent access to compromised accounts. Conditional access policies are additional verifications used by identity providers and identity and access management systems to determine whether a user should be granted access to a resource.

T1578

Modify Cloud Compute Infrastructure

An adversary may attempt to modify a cloud account's compute service infrastructure to evade defenses. A modification to the compute service infrastructure can include the creation, deletion, or modification of one or more components such as compute instances, virtual machines, and snapshots.

.001

Create Snapshot

An adversary may create a snapshot or data backup within a cloud account to evade defenses. A snapshot is a point-in-time copy of an existing cloud compute component such as a virtual machine (VM), virtual hard drive, or volume. An adversary may leverage permissions to create a snapshot in order to bypass restrictions that prevent access to existing compute service infrastructure, unlike in

Revert Cloud Instance

where an adversary may revert to a snapshot to evade detection and remove evidence of their presence.

.002

Create Cloud Instance

An adversary may create a new instance or virtual machine (VM) within the compute service of a cloud account to evade defenses. Creating a new instance may allow an adversary to bypass firewall rules and permissions that exist on instances currently residing within an account. An adversary may

Create Snapshot

of one or more volumes in an account, create a new instance, mount the snapshots, and then apply a less restrictive security policy to collect

Data from Local System

or for

Remote Data Staging

.

.003

Delete Cloud Instance

An adversary may delete a cloud instance after they have performed malicious activities in an attempt to evade detection and remove evidence of their presence. Deleting an instance or virtual machine can remove valuable forensic artifacts and other evidence of suspicious behavior if the instance is not recoverable.

.004

Revert Cloud Instance

An adversary may revert changes made to a cloud instance after they have performed malicious activities in attempt to evade detection and remove evidence of their presence. In highly virtualized environments, such as cloud-based infrastructure, this may be accomplished by restoring virtual machine (VM) or data storage snapshots through the cloud management dashboard or cloud APIs.

.005

Modify Cloud Compute Configurations

Adversaries may modify settings that directly affect the size, locations, and resources available to cloud compute infrastructure in order to evade defenses. These settings may include service quotas, subscription associations, tenant-wide policies, or other configurations that impact available compute. Such modifications may allow adversaries to abuse the victim’s compute resources to achieve their goals, potentially without affecting the execution of running instances and/or revealing their activities to the victim.

T1666

Modify Cloud Resource Hierarchy

Adversaries may attempt to modify hierarchical structures in infrastructure-as-a-service (IaaS) environments in order to evade defenses.

T1112

Modify Registry

Adversaries may interact with the Windows Registry as part of a variety of other techniques to aid in defense evasion, persistence, and execution.

T1601

Modify System Image

Adversaries may make changes to the operating system of embedded network devices to weaken defenses and provide new capabilities for themselves. On such devices, the operating systems are typically monolithic and most of the device functionality and capabilities are contained within a single file.

.001

Patch System Image

Adversaries may modify the operating system of a network device to introduce new capabilities or weaken existing defenses. Some network devices are built with a monolithic architecture, where the entire operating system and most of the functionality of the device is contained within a single file. Adversaries may change this file in storage, to be loaded in a future boot, or in memory during runtime.

.002

Downgrade System Image

Adversaries may install an older version of the operating system of a network device to weaken security. Older operating system versions on network devices often have weaker encryption ciphers and, in general, fewer/less updated defensive features.

T1111

Multi-Factor Authentication Interception

Adversaries may target multi-factor authentication (MFA) mechanisms, (i.e., smart cards, token generators, etc.) to gain access to credentials that can be used to access systems, services, and network resources. Use of MFA is recommended and provides a higher level of security than usernames and passwords alone, but organizations should be aware of techniques that could be used to intercept and bypass these security mechanisms.

T1621

Multi-Factor Authentication Request Generation

Adversaries may attempt to bypass multi-factor authentication (MFA) mechanisms and gain access to accounts by generating MFA requests sent to users.

T1104

Multi-Stage Channels

Adversaries may create multiple stages for command and control that are employed under different conditions or for certain functions. Use of multiple stages may obfuscate the command and control channel to make detection more difficult.

T1106

Native API

Adversaries may interact with the native OS application programming interface (API) to execute behaviors. Native APIs provide a controlled means of calling low-level OS services within the kernel, such as those involving hardware/devices, memory, and processes. These native APIs are leveraged by the OS during system boot (when other system components are not yet initialized) as well as carrying out tasks and requests during routine operations.

T1599

Network Boundary Bridging

Adversaries may bridge network boundaries by compromising perimeter network devices or internal devices responsible for network segmentation. Breaching these devices may enable an adversary to bypass restrictions on traffic routing that otherwise separate trusted and untrusted networks.

.001

Network Address Translation Traversal

Adversaries may bridge network boundaries by modifying a network device’s Network Address Translation (NAT) configuration. Malicious modifications to NAT may enable an adversary to bypass restrictions on traffic routing that otherwise separate trusted and untrusted networks.

T1498

Network Denial of Service

Adversaries may perform Network Denial of Service (DoS) attacks to degrade or block the availability of targeted resources to users. Network DoS can be performed by exhausting the network bandwidth services rely on. Example resources include specific websites, email services, DNS, and web-based applications. Adversaries have been observed conducting network DoS attacks for political purposes and to support other malicious activities, including distraction, hacktivism, and extortion.

.001

Direct Network Flood

Adversaries may attempt to cause a denial of service (DoS) by directly sending a high-volume of network traffic to a target. This DoS attack may also reduce the availability and functionality of the targeted system(s) and network.

Direct Network Flood

s are when one or more systems are used to send a high-volume of network packets towards the targeted service's network. Almost any network protocol may be used for flooding. Stateless protocols such as UDP or ICMP are commonly used but stateful protocols such as TCP can be used as well.

.002

Reflection Amplification

Adversaries may attempt to cause a denial of service (DoS) by reflecting a high-volume of network traffic to a target. This type of Network DoS takes advantage of a third-party server intermediary that hosts and will respond to a given spoofed source IP address. This third-party server is commonly termed a reflector. An adversary accomplishes a reflection attack by sending packets to reflectors with the spoofed address of the victim. Similar to Direct Network Floods, more than one system may be used to conduct the attack, or a botnet may be used. Likewise, one or more reflectors may be used to focus traffic on the target. This Network DoS attack may also reduce the availability and functionality of the targeted system(s) and network.

T1046

Network Service Discovery

Adversaries may attempt to get a listing of services running on remote hosts and local network infrastructure devices, including those that may be vulnerable to remote software exploitation. Common methods to acquire this information include port, vulnerability, and/or wordlist scans using tools that are brought onto a system.

T1135

Network Share Discovery

Adversaries may look for folders and drives shared on remote systems as a means of identifying sources of information to gather as a precursor for Collection and to identify potential systems of interest for Lateral Movement. Networks often contain shared network drives and folders that enable users to access file directories on various systems across a network.

T1040

Network Sniffing

Adversaries may passively sniff network traffic to capture information about an environment, including authentication material passed over the network. Network sniffing refers to using the network interface on a system to monitor or capture information sent over a wired or wireless connection. An adversary may place a network interface into promiscuous mode to passively access data in transit over the network, or use span ports to capture a larger amount of data.

T1095

Non-Application Layer Protocol

Adversaries may use an OSI non-application layer protocol for communication between host and C2 server or among infected hosts within a network. The list of possible protocols is extensive. Specific examples include use of network layer protocols, such as the Internet Control Message Protocol (ICMP), transport layer protocols, such as the User Datagram Protocol (UDP), session layer protocols, such as Socket Secure (SOCKS), as well as redirected/tunneled protocols, such as Serial over LAN (SOL).

T1571

Non-Standard Port

Adversaries may communicate using a protocol and port pairing that are typically not associated. For example, HTTPS over port 8088 or port 587 as opposed to the traditional port 443. Adversaries may make changes to the standard port used by a protocol to bypass filtering or muddle analysis/parsing of network data.

T1027

Obfuscated Files or Information

Adversaries may attempt to make an executable or file difficult to discover or analyze by encrypting, encoding, or otherwise obfuscating its contents on the system or in transit. This is common behavior that can be used across different platforms and the network to evade defenses.

.001

Binary Padding

Adversaries may use binary padding to add junk data and change the on-disk representation of malware. This can be done without affecting the functionality or behavior of a binary, but can increase the size of the binary beyond what some security tools are capable of handling due to file size limitations.

.002

Software Packing

Adversaries may perform software packing or virtual machine software protection to conceal their code. Software packing is a method of compressing or encrypting an executable. Packing an executable changes the file signature in an attempt to avoid signature-based detection. Most decompression techniques decompress the executable code in memory. Virtual machine software protection translates an executable's original code into a special format that only a special virtual machine can run. A virtual machine is then called to run this code.

.003

Steganography

Adversaries may use steganography techniques in order to prevent the detection of hidden information. Steganographic techniques can be used to hide data in digital media such as images, audio tracks, video clips, or text files.

.004

Compile After Delivery

Adversaries may attempt to make payloads difficult to discover and analyze by delivering files to victims as uncompiled code. Text-based source code files may subvert analysis and scrutiny from protections targeting executables/binaries. These payloads will need to be compiled before execution; typically via native utilities such as ilasm.exe, csc.exe, or GCC/MinGW.

.005

Indicator Removal from Tools

Adversaries may remove indicators from tools if they believe their malicious tool was detected, quarantined, or otherwise curtailed. They can modify the tool by removing the indicator and using the updated version that is no longer detected by the target's defensive systems or subsequent targets that may use similar systems.

.006

HTML Smuggling

Adversaries may smuggle data and files past content filters by hiding malicious payloads inside of seemingly benign HTML files. HTML documents can store large binary objects known as JavaScript Blobs (immutable data that represents raw bytes) that can later be constructed into file-like objects. Data may also be stored in Data URLs, which enable embedding media type or MIME files inline of HTML documents. HTML5 also introduced a download attribute that may be used to initiate file downloads.

.007

Dynamic API Resolution

Adversaries may obfuscate then dynamically resolve API functions called by their malware in order to conceal malicious functionalities and impair defensive analysis. Malware commonly uses various

Native API

functions provided by the OS to perform various tasks such as those involving processes, files, and other system artifacts.

.008

Stripped Payloads

Adversaries may attempt to make a payload difficult to analyze by removing symbols, strings, and other human readable information. Scripts and executables may contain variables names and other strings that help developers document code functionality. Symbols are often created by an operating system’s

linker

when executable payloads are compiled. Reverse engineers use these symbols and strings to analyze code and to identify functionality in payloads.

.009

Embedded Payloads

Adversaries may embed payloads within other files to conceal malicious content from defenses. Otherwise seemingly benign files (such as scripts and executables) may be abused to carry and obfuscate malicious payloads and content. In some cases, embedded payloads may also enable adversaries to

Subvert Trust Controls

by not impacting execution controls such as digital signatures and notarization tickets.

.010

Command Obfuscation

Adversaries may obfuscate content during command execution to impede detection. Command-line obfuscation is a method of making strings and patterns within commands and scripts more difficult to signature and analyze. This type of obfuscation can be included within commands executed by delivered payloads (e.g.,

Phishing

and

Drive-by Compromise

) or interactively via

Command and Scripting Interpreter

.

.011

Fileless Storage

Adversaries may store data in "fileless" formats to conceal malicious activity from defenses. Fileless storage can be broadly defined as any format other than a file. Common examples of non-volatile fileless storage in Windows systems include the Windows Registry, event logs, or WMI repository. Shared memory directories on Linux systems (

/dev/shm

,

/run/shm

,

/var/run

, and

/var/lock

) and volatile directories on Network Devices (

/tmp

and

/volatile

) may also be considered fileless storage, as files written to these directories are mapped directly to RAM and not stored on the disk..

.012

LNK Icon Smuggling

Adversaries may smuggle commands to download malicious payloads past content filters by hiding them within otherwise seemingly benign windows shortcut files. Windows shortcut files (.LNK) include many metadata fields, including an icon location field (also known as the

IconEnvironmentDataBlock

) designed to specify the path to an icon file that is to be displayed for the LNK file within a host directory.

.013

Encrypted/Encoded File

Adversaries may encrypt or encode files to obfuscate strings, bytes, and other specific patterns to impede detection. Encrypting and/or encoding file content aims to conceal malicious artifacts within a file used in an intrusion. Many other techniques, such as

Software Packing

,

Steganography

, and

Embedded Payloads

, share this same broad objective. Encrypting and/or encoding files could lead to a lapse in detection of static signatures, only for this malicious content to be revealed (i.e.,

Deobfuscate/Decode Files or Information

) at the time of execution/use.

.014

Polymorphic Code

Adversaries may utilize polymorphic code (also known as metamorphic or mutating code) to evade detection. Polymorphic code is a type of software capable of changing its runtime footprint during code execution. With each execution of the software, the code is mutated into a different version of itself that achieves the same purpose or objective as the original. This functionality enables the malware to evade traditional signature-based defenses, such as antivirus and antimalware tools.

Other obfuscation techniques can be used in conjunction with polymorphic code to accomplish the intended effects, including using mutation engines to conduct actions such as

Software Packing

,

Command Obfuscation

, or

Encrypted/Encoded File

.

.015

Compression
