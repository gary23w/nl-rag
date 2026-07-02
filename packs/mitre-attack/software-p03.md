---
title: "Software (part 3/5)"
source: https://attack.mitre.org/software/
domain: mitre-attack
license: CC-BY-SA-4.0
tags: mitre att&ck, adversary tactics techniques, att&ck framework, cyber kill chain, threat actor behavior
fetched: 2026-07-02
part: 3/5
---

# Software

JumbledPath is a custom-built utility written in GO that has been used by Salt Typhoon since at least 2024 for packet capture on remote Cisco devices. JumbledPath is compiled as an ELF binary using x86-64 architecture which makes it potentially useable across Linux operating systems and network devices from multiple vendors.

S1190

Kapeka

KnuckleTouch

Kapeka is a backdoor written in C++ used against victims in Eastern Europe since at least mid-2022. Kapeka has technical overlaps with Exaramel for Windows and Prestige malware variants, both of which are linked to Sandworm Team. Kapeka may have been used in advance of Prestige deployment in late 2022.

S0215

KARAE

KARAE is a backdoor typically used by APT37 as first-stage malware.

S0088

Kasidet

Kasidet is a backdoor that has been dropped by using malicious VBA macros.

S0265

Kazuar

Kazuar is a fully featured, multi-platform backdoor Trojan written using the Microsoft .NET framework.

S0585

Kerrdown

Kerrdown is a custom downloader that has been used by APT32 since at least 2018 to install spyware from a server on the victim's network.

S0487

Kessel

Kessel is an advanced version of OpenSSH which acts as a custom backdoor, mainly acting to steal credentials and function as a bot. Kessel has been active since its C2 domain began resolving in August 2018.

S1020

Kevin

Kevin is a backdoor implant written in C++ that has been used by HEXANE since at least June 2020, including in operations against organizations in Tunisia.

S0387

KeyBoy

KeyBoy is malware that has been used in targeted campaigns against members of the Tibetan Parliament in 2016.

S0276

Keydnap

OSX/Keydnap

This piece of malware steals the content of the user's keychain while maintaining a permanent backdoor .

S0271

KEYMARBLE

KEYMARBLE is a Trojan that has reportedly been used by the North Korean government.

S1051

KEYPLUG

KEYPLUG.LINUX

KEYPLUG is a modular backdoor written in C++, with Windows and Linux variants, that has been used by APT41 since at least June 2021.

S0288

KeyRaider

KeyRaider is malware that steals Apple account credentials and other data from jailbroken iOS devices. It also has ransomware functionality.

S0526

KGH_SPY

KGH_SPY is a modular suite of tools used by Kimsuky for reconnaissance, information stealing, and backdoor capabilities. KGH_SPY derived its name from PDB paths and internal names found in samples containing "KGH".

S0607

KillDisk

Win32/KillDisk.NBI, Win32/KillDisk.NBH, Win32/KillDisk.NBD, Win32/KillDisk.NBC, Win32/KillDisk.NBB

KillDisk is a disk-wiping tool designed to overwrite files with random data to render the OS unbootable. It was first observed as a component of BlackEnergy malware during cyber attacks against Ukraine in 2015. KillDisk has since evolved into stand-alone malware used by a variety of threat actors against additional targets in Europe and Latin America; in 2016 a ransomware component was also incorporated into some KillDisk variants.

S0599

Kinsing

Kinsing is Golang-based malware that runs a cryptocurrency miner and attempts to spread itself to other hosts in the victim environment.

S0437

Kivars

Kivars is a modular remote access tool (RAT), derived from the Bifrost RAT, that was used by BlackTech in a 2010 campaign.

S0250

Koadic

Koadic is a Windows post-exploitation framework and penetration testing tool that is publicly available on GitHub. Koadic has several options for staging payloads and creating implants, and performs most of its operations using Windows Script Host.

S0641

Kobalos

Kobalos is a multi-platform backdoor that can be used against Linux, FreeBSD, and Solaris. Kobalos has been deployed against high profile targets, including high-performance computers, academic servers, an endpoint security vendor, and a large internet service provider; it has been found in Europe, North America, and Asia. Kobalos was first identified in late 2019.

S0669

KOCTOPUS

KOCTOPUS's batch variant is loader used by LazyScripter since 2018 to launch Octopus and Koadic and, in some cases, QuasarRAT. KOCTOPUS also has a VBA variant that has the same functionality as the batch version.

S0162

Komplex

Komplex is a backdoor that has been used by APT28 on OS X and appears to be developed in a similar manner to XAgentOSX .

S0156

KOMPROGO

KOMPROGO is a signature backdoor used by APT32 that is capable of process, file, and registry management.

S0356

KONNI

KONNI is a remote access tool that security researchers assess has been used by North Korean cyber actors since at least 2014. KONNI has significant code overlap with the NOKKI malware family, and has been linked to several suspected North Korean campaigns targeting political organizations in Russia, East Asia, Europe and the Middle East; there is some evidence potentially linking KONNI to APT37.

S1075

KOPILUWAK

KOPILUWAK is a JavaScript-based reconnaissance tool that has been used for victim profiling and C2 since at least 2017.

S0236

Kwampirs

Kwampirs is a backdoor Trojan used by Orangeworm. Kwampirs has been found on machines which had software installed for the use and control of high-tech imaging devices such as X-Ray and MRI machines. Kwampirs has multiple technical overlaps with Shamoon based on reverse engineering analysis.

S9035

LAMEHUG

PROMPTSTEAL

LAMEHUG is Python-based information stealer first identified in July 2025 by Ukraine's Computer Emergency Response Team (CERT-UA) in phishing emails targeting Ukrainian government officials. LAMEHUG is the first known malware to integrate artificial intelligence (AI) directly into its attack workflow by querying large language models (LLMs) hosted on Hugging Face to dynamically generate reconnaissance, data theft, and system manipulation commands in real time. LAMEHUG has been attributed to APT28.

S1160

Latrodectus

IceNova, Unidentified 111

Latrodectus is a Windows malware downloader that has been used since at least 2023 to download and execute additional payloads and modules. Latrodectus has most often been distributed through email campaigns, primarily by TA577 and TA578, and has infrastructure overlaps with historic IcedID operations.

S0349

LaZagne

LaZagne is a post-exploitation, open-source tool used to recover stored passwords on a system. It has modules for Windows, Linux, and OSX, but is mainly focused on Windows systems. LaZagne is publicly available on GitHub.

S9039

LazyWiper

LazyWiper is a destructive malware observed targeting a manufacturing sector company during the 2025 Poland Wiper Attacks. LazyWiper is a native Windows PowerShell script that is believed to have been generated by a large language model (LLM). LazyWiper overwrites files on the system using the C# function `WriteRandomBytes()` and can target multiple specific file types by their extensions.

S0395

LightNeuron

LightNeuron is a sophisticated backdoor that has targeted Microsoft Exchange servers since at least 2014. LightNeuron has been used by Turla to target diplomatic and foreign affairs-related organizations. The presence of certain strings in the malware suggests a Linux variant of LightNeuron exists.

S1185

LightSpy

First observed in 2018, LightSpy is a modular malware family that initially targeted iOS devices in Southern Asia before expanding to Android and macOS platforms. It consists of a downloader, a main executable that manages network communications, and functionality-specific modules, typically implemented as `.dylib` files (iOS, macOS) or `.apk` files (Android). LightSpy can collect VoIP call recordings, SMS messages, and credential stores, which are then exfiltrated to a command and control (C2) server.

S1119

LIGHTWIRE

LIGHTWIRE is a web shell written in Perl that was used during Cutting Edge to maintain access and enable command execution by imbedding into the legitimate compcheckresult.cgi component of Ivanti Secure Connect VPNs.

S1186

Line Dancer

Line Dancer is a memory-only Lua-based shellcode loader associated with the ArcaneDoor campaign. Line Dancer allows an adversary to upload and execute arbitrary shellcode on victim devices.

S1188

Line Runner

Line Runner is a persistent backdoor and web shell allowing threat actors to upload and execute arbitrary Lua scripts. Line Runner is associated with the ArcaneDoor campaign.

S0211

Linfo

Linfo is a rootkit trojan used by Elderwood to open a backdoor on compromised hosts.

S0362

Linux Rabbit

Linux Rabbit is malware that targeted Linux servers and IoT devices in a campaign lasting from August to October 2018. It shares code with another strain of malware known as Rabbot. The goal of the campaign was to install cryptocurrency miners onto the targeted servers and devices.

S0513

LiteDuke

LiteDuke is a third stage backdoor that was used by APT29, primarily in 2014-2015. LiteDuke used the same dropper as PolyglotDuke, and was found on machines also compromised by MiniDuke.

S0680

LitePower

LitePower is a downloader and second stage malware that has been used by WIRTE since at least 2021.

S1121

LITTLELAMB.WOOLTEA

LITTLELAMB.WOOLTEA is a backdoor that was used by UNC5325 during Cutting Edge to deploy malware on targeted Ivanti Connect Secure VPNs and to establish persistence across system upgrades and patches.

S0681

Lizar

Tirion, Icebot, DiceLoader

Lizar is a modular remote access tool written using the .NET Framework that shares structural similarities to Carbanak. It has likely been used by FIN7 since at least February 2021.

S1199

LockBit 2.0

LockBit 2.0 is an affiliate-based Ransomware-as-a-Service (RaaS) that has been in use since at least June 2021 as the successor to LockBit Ransomware. LockBit 2.0 has versions capable of infecting Windows and VMware ESXi virtual machines, and has been observed targeting multiple industry verticals globally.

S1202

LockBit 3.0

LockBit Black

LockBit 3.0 is an evolution of the LockBit Ransomware-as-a-Service (RaaS) offering with similarities to BlackMatter and BlackCat ransomware. LockBit 3.0 has been in use since at least June 2022 and features enhanced defense evasion and exfiltration tactics, robust encryption methods for Windows and VMware ESXi systems, and a more refined RaaS structure over its predecessors such as LockBit 2.0.

S0372

LockerGoga

LockerGoga is ransomware that was first reported in January 2019, and has been tied to various attacks on European companies, including industrial and manufacturing firms.

S9020

LODEINFO

LODEINFO is a fileless backdoor malware first identified in 2020 that has been used by actors including MirrorFace, primarily against media, diplomatic, governmental, and public sector organizations in Japan.

S1101

LoFiSe

LoFiSe has been used by ToddyCat since at least 2023 to identify and collect files of interest on targeted systems.

S0397

LoJax

LoJax is a UEFI rootkit used by APT28 to persist remote access software on targeted systems.

S0447

Lokibot

Lokibot is a widely distributed information stealer that was first reported in 2015. It is designed to steal sensitive information such as usernames, passwords, cryptocurrency wallets, and other credentials. Lokibot can also create a backdoor into infected systems to allow an attacker to install additional payloads.

S0582

LookBack

LookBack is a remote access trojan written in C++ that was used against at least three US utility companies in July 2019. The TALONITE activity group has been observed using LookBack.

S0451

LoudMiner

LoudMiner is a cryptocurrency miner which uses virtualization software to siphon system resources. The miner has been bundled with pirated copies of Virtual Studio Technology (VST) for Windows and macOS.

S0042

LOWBALL

LOWBALL is malware used by admin@338. It was used in August 2015 in email messages targeting Hong Kong-based media organizations.

S9036

LP-Notes

LP-Notes is a C/C++ Windows credential stealer used by MuddyWater. LP-Notes was named after the `lp-notes.txt` file that is used to store stolen credentials.

S0121

Lslsass

Lslsass is a publicly-available tool that can dump active logon session password hashes from the lsass process.

S0532

Lucifer

Lucifer is a crypto miner and DDoS hybrid malware that leverages well-known exploits to spread laterally on Windows platforms.

S1213

Lumma Stealer

LummaStealer

Lumma Stealer is an information stealer malware family in use since at least 2022. Lumma Stealer is a Malware as a Service (MaaS) where captured data has been sold in criminal markets to Initial Access Brokers.

S1143

LunarLoader

LunarLoader is the loader component for the LunarWeb and LunarMail backdoors that has been used by Turla since at least 2020 including against a European ministry of foreign affairs (MFA). LunarLoader has been observed as a standalone and as a part of trojanized open-source software such as AdmPwd.

S1142

LunarMail

LunarMail is a backdoor that has been used by Turla since at least 2020 including in a compromise of a European ministry of foreign affairs (MFA) in conjunction with LunarLoader and LunarWeb. LunarMail is designed to be deployed on workstations and can use email messages and Steganography in command and control.

S1141

LunarWeb

LunarWeb is a backdoor that has been used by Turla since at least 2020 including in a compromise of a European ministry of foreign affairs (MFA) together with LunarLoader and LunarMail. LunarWeb has only been observed deployed against servers and can use Steganography to obfuscate command and control.

S0010

Lurid

Enfal

Lurid is a malware family that has been used by several groups, including PittyTiger, in targeted attacks as far back as 2006.

S0409

Machete

Pyark

Machete is a cyber espionage toolset used by Machete. It is a Python-based backdoor targeting Windows machines that was first observed in 2010.

S1016

MacMa

OSX.CDDS, DazzleSpy

MacMa is a macOS-based backdoor with a large set of functionalities to control and exfiltrate files from a compromised computer. MacMa has been observed in the wild since November 2021. MacMa shares command and control and unique libraries with MgBot and Nightdoor, indicating a relationship with the Daggerfly threat actor.

S1048

macOS.OSAMiner

macOS.OSAMiner is a Monero mining trojan that was first observed in 2018; security researchers assessed macOS.OSAMiner may have been circulating since at least 2015. macOS.OSAMiner is known for embedding one run-only AppleScript into another, which helped the malware evade full analysis for five years due to a lack of Apple event (AEVT) analysis tools.

S0282

MacSpy

MacSpy is a malware-as-a-service offered on the darkweb .

S1060

Mafalda

Mafalda is a flexible interactive implant that has been used by Metador. Security researchers assess the Mafalda name may be inspired by an Argentinian cartoon character that has been popular as a means of political commentary since the 1960s.

S1182

MagicRAT

MagicRAT is a remote access tool developed in C++ and exclusively used by the Lazarus Group threat actor in operations. MagicRAT allows for arbitrary command execution on victim machines and provides basic remote access functionality.

S0413

MailSniper

MailSniper is a penetration testing tool for searching through email in a Microsoft Exchange environment for specific terms (passwords, insider intel, network architecture information, etc.). It can be used by a non-administrative user to search their own email, or by an Exchange administrator to search the mailboxes of every user in a domain.

S0485

Mandrake

oxide, briar, ricinus, darkmatter

Mandrake is a sophisticated Android espionage platform that has been active in the wild since at least 2016. Mandrake is very actively maintained, with sophisticated features and attacks that are executed with surgical precision.

Mandrake has gone undetected for several years by providing legitimate, ad-free applications with social media and real reviews to back the apps. The malware is only activated when the operators issue a specific command.

S1169

Mango

Mango is a first-stage backdoor written in C#/.NET that was used by OilRig during the Juicy Mix campaign. Mango is the successor to Solar and includes additional exfiltration capabilities, the use of native APIs, and added detection evasion code.

S1156

Manjusaka

Manjusaka is a Chinese-language intrusion framework, similar to Sliver and Cobalt Strike, with an ELF binary written in GoLang as the controller for Windows and Linux implants written in Rust. First identified in 2022, Manjusaka consists of multiple components, only one of which (a command and control module) is freely available.

S0652

MarkiRAT

MarkiRAT is a remote access Trojan (RAT) compiled with Visual Studio that has been used by Ferocious Kitten since at least 2015.

S0167

Matryoshka

Matryoshka is a malware framework used by CopyKittens that consists of a dropper, loader, and RAT. It has multiple versions; v1 was seen in the wild from July 2016 until January 2017. v2 has fewer commands and other minor differences.

S0303

MazarBOT

MazarBOT is Android malware that was distributed via SMS in Denmark in 2016.

S0449

Maze

Maze ransomware, previously known as "ChaCha", was discovered in May 2019. In addition to encrypting files on victim machines for impact, Maze operators conduct information stealing campaigns prior to encryption and post the information online to extort affected companies.

S0500

MCMD

MCMD is a remote access tool that provides remote command shell capability used by Dragonfly.

S0459

MechaFlounder

MechaFlounder is a python-based remote access tool (RAT) that has been used by APT39. The payload uses a combination of actor developed code and code snippets freely available online in development communities.

S1220

MEDUSA

MEDUSA is an open-source rootkit that is capable of dynamic linker hijacking, command execution, and logging credentials.

S1244

Medusa Ransomware

Medusa Ransomware has been utilized in attacks since at least 2021. Medusa Ransomware has been known to be utilized in conjunction with living off the land techniques and remote management software. Medusa Ransomware has been used in campaigns associated with "double extortion" ransomware activity, where data is exfiltrated from victim environments prior to encryption, with threats to publish files if a ransom is not paid. Medusa Ransomware software was initially a closed ransomware variant which later evolved to a Ransomware as a Service (RaaS). Medusa Ransomware has impacted victims from a diverse range of sectors within a multitude of countries, and it is assessed Medusa Ransomware is used in an opportunistic manner.

S0175

meek

meek is an open-source Tor plugin that tunnels Tor traffic through HTTPS connections.

S0576

MegaCortex

MegaCortex is ransomware that first appeared in May 2019. MegaCortex has mainly targeted industrial organizations.

S1191

Megazord

Megazord is a Rust-based variant of Akira ransomware that has been in use since at least August 2023 to target Windows environments. Megazord has been attributed to the Akira group based on overlapping infrastructure though is possibly not exclusive to the group.

S0530

Melcoz

Melcoz is a banking trojan family built from the open source tool Remote Access PC. Melcoz was first observed in attacks in Brazil and since 2018 has spread to Chile, Mexico, Spain, and Portugal.

S0443

MESSAGETAP

MESSAGETAP is a data mining malware family deployed by APT41 into telecommunications networks to monitor and save SMS traffic from specific phone numbers, IMSI numbers, or that contain specific keywords.

S1059

metaMain

metaMain is a backdoor used by Metador to maintain long-term access to compromised machines; it has also been used to decrypt Mafalda into memory.

S0455

Metamorfo

Casbaneiro

Metamorfo is a Latin-American banking trojan operated by a Brazilian cybercrime group that has been active since at least April 2018. The group focuses on targeting banks and cryptocurrency services in Brazil and Mexico.

S0688

Meteor

Meteor is a wiper that was used against Iranian government organizations, including Iranian Railways, the Ministry of Roads, and Urban Development systems, in July 2021. Meteor is likely a newer version of similar wipers called Stardust and Comet that were reportedly used by a group called "Indra" since at least 2019 against private companies in Syria.

S1146

MgBot

MgBot is a modular malware framework exclusively associated with Daggerfly operations since at least 2012. MgBot was developed in C++ and features a module design with multiple available plugins that have been under active development through 2024.

S0339

Micropsia

Micropsia is a remote access tool written in Delphi.

S1015

Milan

James

Milan is a backdoor implant based on DanBot that was written in Visual C++ and .NET. Milan has been used by HEXANE since at least June 2020.

S0002

Mimikatz

Mimikatz is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks.

S0179

MimiPenguin

MimiPenguin is a credential dumper, similar to Mimikatz, designed specifically for Linux platforms.

S0133

Miner-C

Miner-C is malware that mines victims for the Monero cryptocurrency. It has targeted FTP servers and Network Attached Storage (NAS) devices to spread.

S0051

MiniDuke

MiniDuke is malware that was used by APT29 from 2010 to 2015. The MiniDuke toolset consists of multiple downloader and backdoor components. The loader has been used with other MiniDuke components as well as in conjunction with CosmicDuke and PinchDuke.

S0280

MirageFox

MirageFox is a remote access tool used against Windows systems. It appears to be an upgraded version of a tool known as Mirage, which is a RAT believed to originate in 2012.

S9022

MirrorStealer

MirrorStealer is a credential stealer that has been used by MirrorFace since at least 2022 to steal credentials from various applications, including browsers and email clients. MirrorStealer has been delivered directly into system memory via commands issued by LODEINFO.

S0084

Mis-Type

Mis-Type is a backdoor hybrid that was used in Operation Dust Storm by 2012.

S0083

Misdat

Misdat is a backdoor that was used in Operation Dust Storm from 2010 to 2011.

S1122

Mispadu

Mispadu is a banking trojan written in Delphi that was first observed in 2019 and uses a Malware-as-a-Service (MaaS) business model. This malware is operated, managed, and sold by the Malteiro cybercriminal group. Mispadu has mainly been used to target victims in Brazil and Mexico, and has also had confirmed operations throughout Latin America and Europe.

S0080

Mivast

Mivast is a backdoor that has been used by Deep Panda. It was reportedly used in the Anthem breach.

S0079

MobileOrder

MobileOrder is a Trojan intended to compromise Android mobile devices. It has been used by Scarlet Mimic.

S0553

MoleNet

MoleNet is a downloader tool with backdoor capabilities that has been observed in use since at least 2019.

S1137

Moneybird

Moneybird is a ransomware variant written in C++ associated with Agrius operations. The name "Moneybird" is contained in the malware's ransom note and as strings in the executable.

S1026

Mongall

Mongall is a backdoor that has been used since at least 2013, including by Aoqin Dragon.

S0407

Monokle

Monokle is targeted, sophisticated mobile surveillanceware. It is developed for Android, but there are some code artifacts that suggests an iOS version may be in development.

S0149

MoonWind

MoonWind is a remote access tool (RAT) that was used in 2016 to target organizations in Thailand.

S1221

MOPSLED

MOPSLED is a shellcode-based modular backdoor that has been used by China-nexus cyber espionage actors including UNC3886 and APT41.

S0284

More_eggs

SKID, Terra Loader, SpicyOmelette

More_eggs is a JScript backdoor used by Cobalt Group and FIN6. Its name was given based on the variable "More_eggs" being present in its code. There are at least two different versions of the backdoor being used, version 2.0 and version 4.4.

S1047

Mori

Mori is a backdoor that has been used by MuddyWater since at least January 2022.

S0256

Mosquito

Mosquito is a Win32 backdoor that has been used by Turla. Mosquito is made up of three parts: the installer, the launcher, and the backdoor. The main backdoor is called CommanderDLL and is launched by the loader program.

S9032

MuddyViper

MuddyViper is custom backdoor written in C and C++ used by MuddyWater for command and control (C2) communications and persistence. MuddyViper is loaded by Fooder and sends frequent messages to the C2 server.

S1135

MultiLayer Wiper

MultiLayer Wiper is wiper malware written in .NET associated with Agrius operations. Observed samples of MultiLayer Wiper have an anomalous, future compilation date suggesting possible metadata manipulation.

S0233

MURKYTOP

MURKYTOP is a reconnaissance tool used by Leviathan.

S0699

Mythic

Mythic is an open source, cross-platform post-exploitation/command and control platform. Mythic is designed to "plug-n-play" with various agents and communication channels. Deployed Mythic C2 servers have been observed as part of potentially malicious infrastructure.

S0205

Naid

Naid is a trojan used by Elderwood to open a backdoor on compromised hosts.

S0228

NanHaiShu

NanHaiShu is a remote access tool and JScript backdoor used by Leviathan. NanHaiShu has been used to target government and private-sector organizations that have relations to the South China Sea dispute.

S0336

NanoCore

NanoCore is a modular remote access tool developed in .NET that can be used to spy on victims and steal information. It has been used by threat actors since 2013.

S0637

NativeZone

NativeZone is the name given collectively to disposable custom Cobalt Strike loaders used by APT29 since at least 2021.

S0247

NavRAT

NavRAT is a remote access tool designed to upload, download, and execute files. It has been observed in attacks targeting South Korea.

S0590

NBTscan

NBTscan is an open source tool that has been used by state groups to conduct internal reconnaissance within a compromised network.

S0102

nbtstat

nbtstat is a utility used to troubleshoot NetBIOS name resolution.

S0272

NDiskMonitor

NDiskMonitor is a custom backdoor written in .NET that appears to be unique to Patchwork.

S0630

Nebulae

Nebulae Is a backdoor that has been used by Naikon since at least 2020.

S1189

Neo-reGeorg

Neo-reGeorg is an open-source web shell designed as a restructuring of reGeorg with improved usability, security, and fixes for exising reGeorg bugs.

S0691

Neoichor

Neoichor is C2 malware used by Ke3chang since at least 2019; similar malware families used by the group include Leeson and Numbldea.

S0210

Nerex

Nerex is a Trojan used by Elderwood to open a backdoor on compromised hosts.

S0039

Net

net.exe

The Net utility is a component of the Windows operating system. It is used in command-line operations for control of users, groups, services, and network connections.

Net has a great deal of functionality, much of which is useful for an adversary, such as gathering system and network information for Discovery, moving laterally through SMB/Windows Admin Shares using `net use` commands, and interacting with services. The net1.exe utility is executed for certain functionality when net.exe is run and can be used directly in commands such as `net1 user`.

S0056

Net Crawler

NetC

Net Crawler is an intranet worm capable of extracting credentials using credential dumpers and spreading to systems on a network over SMB by brute forcing accounts with recovered passwords and using PsExec to execute a copy of Net Crawler.

S0034

NETEAGLE

NETEAGLE is a backdoor developed by APT30 with compile dates as early as 2008. It has two main variants known as "Scout" and "Norton."

S0108

netsh

netsh.exe

netsh is a scripting utility used to interact with networking components on local or remote systems.

S0104

netstat

netstat is an operating system utility that displays active TCP connections, listening ports, and network statistics.

S0033

NetTraveler

NetTraveler is malware that has been used in multiple cyber espionage campaigns for basic surveillance of victims. The earliest known samples have timestamps back to 2005, and the largest number of observed samples were created between 2010 and 2013.

S0457

Netwalker

Netwalker is fileless ransomware written in PowerShell and executed directly in memory.

S0198

NETWIRE

NETWIRE is a publicly available, multiplatform remote administration tool (RAT) that has been used by criminal and APT groups since at least 2012.

S1106

NGLite

NGLite is a backdoor Trojan that is only capable of running commands received through its C2 channel. While the capabilities are standard for a backdoor, NGLite uses a novel C2 channel that leverages a decentralized network based on the legitimate NKN to communicate between the backdoor and the actors.

S0508

ngrok

ngrok is a legitimate reverse proxy tool that can create a secure tunnel to servers located behind firewalls or on local machines that do not have a public IP. ngrok has been leveraged by threat actors in several campaigns including use for lateral movement and data exfiltration.

S1192

NICECURL

NICECURL is a VBScript-based backdoor used by APT42 to download additional modules.

S0118

Nidiran

Backdoor.Nidiran

Nidiran is a custom backdoor developed and used by Suckfly. It has been delivered via strategic web compromise.

S1090

NightClub

NightClub is a modular implant written in C++ that has been used by MoustachedBouncer since at least 2014.

S1147

Nightdoor

Nightdoor is a backdoor exclusively associated with Daggerfly operations. Nightdoor uses common libraries with MgBot and MacMa, linking these malware families together.

S1100

Ninja

Ninja is a malware developed in C++ that has been used by ToddyCat to penetrate networks and control remote systems since at least 2020. Ninja is possibly part of a post exploitation toolkit exclusively used by ToddyCat and allows multiple operators to work simultaneously on the same machine. Ninja has been used against government and military entities in Europe and Asia and observed in specific infection chains being deployed by Samurai.

S0385

njRAT

Njw0rm, LV, Bladabindi

njRAT is a remote access tool (RAT) that was first observed in 2012. It has been used by threat actors in the Middle East.

S1107

NKAbuse

NKAbuse is a Go-based, multi-platform malware abusing NKN (New Kind of Network) technology for data exchange between peers, functioning as a potent implant, and equipped with both flooder and backdoor capabilities.

S0359

Nltest

Nltest is a Windows command-line utility used to list domain controllers and enumerate domain trusts.

S0353

NOKKI

NOKKI is a modular remote access tool. The earliest observed attack using NOKKI was in January 2018. NOKKI has significant code overlap with the KONNI malware family. There is some evidence potentially linking NOKKI to APT37.

S9025

NOOPLDR

NOOPLDR is a shellcode loader with XML/C# and DLL versions that has been used by MirrorFace to load HiddenFace.

S0299

NotCompatible

NotCompatible is an Android malware family that was used between at least 2014 and 2016. It has multiple variants that have become more sophisticated over time.

S0368

NotPetya

ExPetr, Diskcoder.C, GoldenEye, Petrwrap, Nyetya

NotPetya is malware that was used by Sandworm Team in a worldwide attack starting on June 27, 2017. While NotPetya appears as a form of ransomware, its main purpose was to destroy data and disk structures on compromised systems; the attackers never intended to make the encrypted data recoverable. As such, NotPetya may be more appropriately thought of as a form of wiper malware. NotPetya contains worm-like features to spread itself across a computer network using the SMBv1 exploits EternalBlue and EternalRomance.

S1131

NPPSPY

NPPSPY is an implementation of a theoretical mechanism first presented in 2004 for capturing credentials submitted to a Windows system via a rogue Network Provider API item. NPPSPY captures credentials following submission and writes them to a file on the victim system for follow-on exfiltration.

S0286

OBAD

OBAD is an Android malware family.

S0644

ObliqueRAT

ObliqueRAT is a remote access trojan, similar to Crimson, that has been in use by Transparent Tribe since at least 2020.

S0346

OceanSalt

OceanSalt is a Trojan that was used in a campaign targeting victims in South Korea, United States, and Canada. OceanSalt shares code similarity with SpyNote RAT, which has been linked to APT1.

S0340

Octopus

Octopus is a Windows Trojan written in the Delphi programming language that has been used by Nomadic Octopus to target government organizations in Central Asia since at least 2014.

S1170

ODAgent

ODAgent is a C#/.NET downloader that has been used by OilRig since at least 2022 including against target organizations in Israel to download and execute payloads and to exfiltrate staged files.

S1172

OilBooster

OilBooster is a downloader written in Microsoft Visual C/C++ that has been used by OilRig since at least 2022 including against target organizations in Israel to download and execute files and for exfiltration.

S1171

OilCheck

OilCheck is a C#/.NET downloader that has been used by OilRig since at least 2022 including against targets in Israel. OilCheck uses draft messages created in a shared email account for C2 communication.

S0439

Okrum

Okrum is a Windows backdoor that has been seen in use since December 2016 with strong links to Ke3chang.

S0138

OLDBAIT

Sasfis

OLDBAIT is a credential harvester used by APT28.

S0285

OldBoot

OldBoot is an Android malware family.

S0365

Olympic Destroyer

Olympic Destroyer is malware that was used by Sandworm Team against the 2018 Winter Olympics, held in Pyeongchang, South Korea. The main purpose of the malware was to render infected computer systems inoperable. The malware leverages various native Windows utilities and API calls to carry out its destructive tasks. Olympic Destroyer has worm-like features to spread itself across a computer network in order to maximize its destructive impact.

S0052

OnionDuke

OnionDuke is malware that was used by APT29 from 2013 to 2015.

S0264

OopsIE

OopsIE is a Trojan used by OilRig to remotely execute commands as well as upload/download files to/from victims.

S0229

Orz

AIRBREAK

Orz is a custom JavaScript backdoor used by Leviathan. It was observed being used in 2014 as well as in August 2017 when it was dropped by Microsoft Publisher files.

S0165

OSInfo

OSInfo is a custom tool used by APT3 to do internal discovery on a victim's computer and network.

S0402

OSX/Shlayer

Zshlayer, Crossrider

OSX/Shlayer is a Trojan designed to install adware on macOS that was first discovered in 2018.

S0352

OSX_OCEANLOTUS.D

Backdoor.MacOS.OCEANLOTUS.F

OSX_OCEANLOTUS.D is a macOS backdoor used by APT32. First discovered in 2015, APT32 has continued to make improvements using a plugin architecture to extend capabilities, specifically using `.dylib` files. OSX_OCEANLOTUS.D can also determine it's permission level and execute according to access type (`root` or `user`).

S0594

Out1

Out1 is a remote access tool written in python and used by MuddyWater since at least 2021.

S1017

OutSteel

OutSteel is a file uploader and document stealer developed with the scripting language AutoIT that has been used by Saint Bear since at least March 2021.

S0072

OwaAuth

OwaAuth is a Web shell and credential stealer deployed to Microsoft Exchange servers that appears to be exclusively used by Threat Group-3390.

S0598

P.A.S. Webshell

Fobushell

P.A.S. Webshell is a publicly available multifunctional PHP webshell in use since at least 2016 that provides remote access and execution on target web servers.

S0016

P2P ZeuS

Peer-to-Peer ZeuS, Gameover ZeuS

P2P ZeuS is a closed-source fork of the leaked version of the ZeuS botnet. It presents improvements over the leaked version, including a peer-to-peer architecture.

S0626

P8RAT

HEAVYPOT, GreetCake

P8RAT is a fileless malware used by menuPass to download and execute payloads since at least 2020.

S1109

PACEMAKER

PACEMAKER is a credential stealer that was used by APT5 as early as 2020 including activity against US Defense Industrial Base (DIB) companies.

S1091

Pacu

Pacu is an open-source AWS exploitation framework. The tool is written in Python and publicly available on GitHub.

S1233

PAKLOG

PAKLOG is a keylogger known to be leveraged by Mustang Panda and was first observed utilized in 2024. PAKLOG is deployed via a RAR archive (e.g., key.rar), which contains two files: a signed, legitimate binary (PACLOUD.exe) and the malicious PAKLOG DLL (pa_lang2.dll). The PACLOUD.exe binary is used to side-load the PAKLOG DLL which starts with the keylogger functionality.

S0399

Pallas

Pallas is mobile surveillanceware that was custom-developed by Dark Caracal.

S0664

Pandora

Pandora is a multistage kernel rootkit with backdoor functionality that has been in use by Threat Group-3390 since at least 2020.

S0208

Pasam

Pasam is a trojan used by Elderwood to open a backdoor on compromised hosts.

S0122

Pass-The-Hash Toolkit

Pass-The-Hash Toolkit is a toolkit that allows an adversary to "pass" a password hash (without knowing the original password) to log in to systems.

S0556

Pay2Key

Pay2Key is a ransomware written in C++ that has been used by Fox Kitten since at least July 2020 including campaigns against Israeli companies. Pay2Key has been incorporated with a leak site to display stolen sensitive information to further pressure victims into payment.

S1102

Pcexter

Pcexter is an uploader that has been used by ToddyCat since at least 2023 to exfiltrate stolen files.

S1050

PcShare

PcShare is an open source remote access tool that has been modified and used by Chinese threat actors, most notably during the FunnyDream campaign since late 2018.

S0316

Pegasus for Android

Chrysaor

Pegasus for Android is the Android version of malware that has reportedly been linked to the NSO Group. The iOS version is tracked separately under Pegasus for iOS.

S0289

Pegasus for iOS

Pegasus for iOS is the iOS version of malware that has reportedly been linked to the NSO Group. It has been advertised and sold to target high-value victims. The Android version is tracked separately under Pegasus for Android.

S0683

Peirates

Peirates is a post-exploitation Kubernetes exploitation framework with a focus on gathering service account tokens for lateral movement and privilege escalation. The tool is written in GoLang and publicly available on GitHub.

S0587

Penquin

Penquin 2.0, Penquin_x64

Penquin is a remote access trojan (RAT) with multiple versions used by Turla to target Linux systems since at least 2014.

S0643

Peppy

Peppy is a Python-based remote access Trojan, active since at least 2012, with similarities to Crimson.

S9014

PHASEJAM

PHASEJAM is a dropper written as a bash shell script that modifies Ivanti Connect Secure appliance components. PHASEJAM was first reported in January 2025. PHASEJAM has previously been leveraged by People's Republic of China (PRC)- affiliated actors identified as UNC5221 and SYLVANITE.

S1126

Phenakite

Phenakite is a mobile malware that is used by APT-C-23 to target iOS devices. According to several reports, Phenakite was developed to fill a tooling gap and to target those who owned iPhones instead of Windows desktops or Android phones.

S0158

PHOREAL

PHOREAL is a signature backdoor used by APT32.

S9028

PHPsert

PHPsert is a webshell used to execute PHP code that has been in use since at least 2023 against targets in Japan, Singapore, Peru, Taiwan, Iran, Republic of Korea, and the Philippines. PHPsert is not typically deployed as a standalone but integrated into web content such as text editors and content management systems.

S1145

Pikabot

Pikabot is a backdoor used for initial access and follow-on tool deployment active since early 2023. Pikabot is notable for extensive use of multiple encoding, encryption, and defense evasion mechanisms to evade defenses and avoid analysis. Pikabot has some overlaps with QakBot, but insufficient evidence exists to definitively link these two malware families. Pikabot is frequently used to deploy follow on tools such as Cobalt Strike or ransomware variants.

S0517

Pillowmint

Pillowmint is a point-of-sale malware used by FIN7 designed to capture credit card information.

S0048

PinchDuke

PinchDuke is malware that was used by APT29 from 2008 to 2010.

S0097

Ping

Ping is an operating system utility commonly used to troubleshoot and verify network connections.

S1031

PingPull

PingPull is a remote access Trojan (RAT) written in Visual C++ that has been used by GALLIUM since at least June 2022. PingPull has been used to target telecommunications companies, financial institutions, and government entities in Afghanistan, Australia, Belgium, Cambodia, Malaysia, Mozambique, the Philippines, Russia, and Vietnam.

S0501

PipeMon

PipeMon is a multi-stage modular backdoor used by Winnti Group.

S0124

Pisloader

Pisloader is a malware family that is notable due to its use of DNS as a C2 protocol as well as its use of anti-analysis tactics. It has been used by APT18 and is similar to another malware family, HTTPBrowser, that has been used by the group.

S1123

PITSTOP

PITSTOP is a backdoor that was deployed on compromised Ivanti Connect Secure VPNs during Cutting Edge to enable command execution and file read/write.

S0291

PJApps

PJApps is an Android malware family.

S0254

PLAINTEE

PLAINTEE is a malware sample that has been used by Rancor in targeted attacks in Singapore and Cambodia.

S1162

Playcrypt

Play

Playcrypt is a ransomware that has been used by Play since at least 2022 in attacks against against the business, government, critical infrastructure, healthcare, and media sectors in North America, South America, and Europe. Playcrypt derives its name from adding the .play extension to encrypted files and has overlap with tactics and tools associated with Hive and Nokoyawa ransomware and infrastructure associated with Quantum ransomware.

S1006

PLC-Blaster

PLC-Blaster is a piece of proof-of-concept malware that runs on Siemens S7 PLCs. This worm locates other Siemens S7 PLCs on the network and attempts to infect them. Once this worm has infected its target and attempted to infect other devices on the network, the worm can then run one of many modules.

S0435

PLEAD

PLEAD is a remote access tool (RAT) and downloader used by BlackTech in targeted attacks in East Asia including Taiwan, Japan, and Hong Kong. PLEAD has also been referred to as TSCookie, though more recent reporting indicates likely separation between the two. PLEAD was observed in use as early as March 2017.

S0013

PlugX

Thoper, TVT, DestroyRAT, Sogu, Kaba, Korplug

PlugX is a remote access tool (RAT) with modular plugins that has been used by multiple threat groups.

S0067

pngdowner

pngdowner is malware used by Putter Panda. It is a simple tool with limited functionality and no persistence mechanism, suggesting it is used only as a simple "download-and- execute" utility.

S0428

PoetRAT

PoetRAT is a remote access trojan (RAT) that was first identified in April 2020. PoetRAT has been used in multiple campaigns against the private and public sectors in Azerbaijan, including ICS and SCADA systems in the energy sector. The STIBNITE activity group has been observed using the malware. PoetRAT derived its name from references in the code to poet William Shakespeare.

S0012

PoisonIvy

Breut, Poison Ivy, Darkmoon

PoisonIvy is a popular remote access tool (RAT) that has been used by many groups.

S0518

PolyglotDuke

PolyglotDuke is a downloader that has been used by APT29 since at least 2013. PolyglotDuke has been used to drop MiniDuke.

S0453

Pony

Pony is a credential stealing malware, though has also been used among adversaries for its downloader capabilities. The source code for Pony Loader 1.0 and 2.0 were leaked online, leading to their use by various threat actors.

S0216

POORAIM

POORAIM is a backdoor used by APT37 in campaigns since at least 2014.

S0378

PoshC2

PoshC2 is an open source remote administration and post-exploitation framework that is publicly available on GitHub. The server-side components of the tool are primarily written in Python, while the implants are written in PowerShell. Although PoshC2 is primarily focused on Windows implantation, it does contain a basic Python dropper for Linux/macOS.

S0150

POSHSPY

POSHSPY is a backdoor that has been used by APT29 since at least 2015. It appears to be used as a secondary backdoor used if the actors lost access to their primary backdoors.

S0177

Power Loader

Power Loader is modular code sold in the cybercrime market used as a downloader in malware families such as Carberp, Redyms and Gapz.

S0139

PowerDuke

PowerDuke is a backdoor that was used by APT29 in 2016. It has primarily been delivered through Microsoft Word or Excel attachments containing malicious macros.

S1173

PowerExchange

PowerExchange is a PowerShell backdoor that has been used by OilRig since at least 2023 including against government targets in the Middle East.

S1012

PowerLess

PowerLess is a PowerShell-based modular backdoor that has been used by Magic Hound since at least 2022.

S0685

PowerPunch

PowerPunch is a lightweight downloader that has been used by Gamaredon Group since at least 2021.

S0441

PowerShower

PowerShower is a PowerShell backdoor used by Inception for initial reconnaissance and to download and execute second stage payloads.

S0145

POWERSOURCE

DNSMessenger

POWERSOURCE is a PowerShell backdoor that is a heavily obfuscated and modified version of the publicly available tool DNS_TXT_Pwnage. It was observed in February 2017 in spearphishing campaigns against personnel involved with United States Securities and Exchange Commission (SEC) filings at various organizations. The malware was delivered when macros were enabled by the victim and a VBS script was dropped.

S0194

PowerSploit

PowerSploit is an open source, offensive security framework comprised of PowerShell modules and scripts that perform a wide range of tasks related to penetration testing such as code execution, persistence, bypassing anti-virus, recon, and exfiltration.

S0393

PowerStallion

PowerStallion is a lightweight PowerShell backdoor used by Turla, possibly as a recovery access tool to install other backdoors.

S0223

POWERSTATS

Powermud

POWERSTATS is a PowerShell-based first stage backdoor used by MuddyWater.

S0371

POWERTON

POWERTON is a custom PowerShell backdoor first observed in 2018. It has typically been deployed as a late-stage backdoor by APT33. At least two variants of the backdoor have been identified, with the later version containing improved functionality.

S1046

PowGoop

PowGoop is a loader that consists of a DLL loader and a PowerShell-based downloader; it has been used by MuddyWater as their main loader.

S0184

POWRUNER

POWRUNER is a PowerShell script that sends and receives commands to and from the C2 server.

S1058

Prestige

Prestige ransomware has been used by Sandworm Team since at least March 2022, including against transportation and related logistics industries in Ukraine and Poland in October 2022.

S0113

Prikormka

Prikormka is a malware family used in a campaign known as Operation Groundbait. It has predominantly been observed in Ukraine and was used as early as 2008.

S0654

ProLock
