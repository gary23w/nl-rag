---
title: "Software (part 2/5)"
source: https://attack.mitre.org/software/
domain: mitre-attack
license: CC-BY-SA-4.0
tags: mitre att&ck, adversary tactics techniques, att&ck framework, cyber kill chain, threat actor behavior
fetched: 2026-07-02
part: 2/5
---

# Software

DCRAT is a variant of the open-source AsyncRAT developed in C# with additional capabilities such as patching Microsoft’s Antimalware Scan Interface (AMSI).

S1033

DCSrv

DCSrv is destructive malware that has been used by Moses Staff since at least September 2021. Though DCSrv has ransomware-like capabilities, Moses Staff does not demand ransom or offer a decryption key.

S0255

DDKONG

DDKONG is a malware sample that was part of a campaign by Rancor. DDKONG was first seen used in February 2017.

S1052

DEADEYE

DEADEYE.EMBED, DEADEYE.APPEND

DEADEYE is a malware launcher that has been used by APT41 since at least May 2021. DEADEYE has variants that can either embed a payload inside a compiled binary (DEADEYE.EMBED) or append it to the end of a file (DEADEYE.APPEND).

S1134

DEADWOOD

DEADWOOD is wiper malware written in C++ using Boost libraries. DEADWOOD was first observed in an unattributed wiping event in Saudi Arabia in 2019, and has since been incorporated into Agrius operations.

S0243

DealersChoice

DealersChoice is a Flash exploitation framework used by APT28.

S0616

DEATHRANSOM

DEATHRANSOM is ransomware written in C that has been used since at least 2020, and has potential overlap with FIVEHANDS and HELLOKITTY.

S0479

DEFENSOR ID

DEFENSOR ID is a banking trojan capable of clearing a victim’s bank account or cryptocurrency wallet and taking over email or social media accounts. DEFENSOR ID performs the majority of its malicious functionality by abusing Android’s accessibility service.

S0301

Dendroid

Dendroid is an Android remote access tool (RAT) primarily targeting Western countries. The RAT was available for purchase for $300 and came bundled with a utility to inject the RAT into legitimate applications.

S0354

Denis

Denis is a Windows backdoor and Trojan used by APT32. Denis shares several similarities to the SOUNDBITE backdoor and has been used in conjunction with the Goopy backdoor.

S0021

Derusbi

PHOTO

Derusbi is malware used by multiple Chinese APT groups. Both Windows and Linux variants have been observed.

S0505

Desert Scorpion

Desert Scorpion is surveillanceware that has targeted the Middle East, specifically individuals located in Palestine. Desert Scorpion is suspected to have been operated by the threat actor APT-C-23.

There are multiple close variants of Desert Scorpion, such as VAMP, GnatSpy, FrozenCell and SpyC23, which add some additional functionality but are not significantly different from the original malware.

S0659

Diavol

Diavol is a ransomware variant first observed in June 2021 that is capable of prioritizing file types to encrypt based on a pre-configured list of extensions defined by the attacker. The Diavol Ransomware-as-a Service (RaaS) program is managed by Wizard Spider and it has been observed being deployed by Bazar.

S0200

Dipsind

Dipsind is a malware family of backdoors that appear to be used exclusively by PLATINUM.

S1088

Disco

Disco is a custom implant that has been used by MoustachedBouncer since at least 2020 including in campaigns using targeted malicious content injection for initial access and command and control.

S9002

Diskpart

Diskpart is a Windows command-line utility that is used to manage the computer’s drives, which includes disks, partitions, volumes and virtual hard disks.

Adversaries may abuse Diskpart to perform discovery and destructive actions on a system’s storage. For example, adversaries have been observed using Diskpart to conduct Discovery techniques to enumerate disks and volumes to gather information about the host environment, and to execute commands such as `clean all` to remove partition information and overwrite data across disks, resulting in data destruction.

S1021

DnsSystem

DnsSystem is a .NET based DNS backdoor, which is a customized version of the open source tool DIG.net, that has been used by HEXANE since at least June 2022.

S9005

DocSwap

DocSwap is an Android malware first identified in 2025, and attributed to Kimsuky. DocSwap’s name is a combination of its Korean name "문서열람 인증 앱" (Document Viewing Authentication App) and a phishing page masquerading as CoinSwap at the C2 address. Based on DocSwap’s name and Korean-language strings, DocSwap potentially targets mobile device users in South Korea. Several variants of DocSwap exist; one of the latest samples indicates that the adversary added a native decryption function that decrypts an internal APK.

S0213

DOGCALL

DOGCALL is a backdoor used by APT37 that has been used to target South Korean government and military organizations in 2017. It is typically dropped using a Hangul Word Processor (HWP) exploit.

S0281

Dok

Retefe

Dok is a Trojan application disguised as a .zip file that is able to collect user credentials and install a malicious proxy server to redirect a user's network traffic (i.e. Adversary-in-the-Middle).

S0600

Doki

Doki is a backdoor that uses a unique Dogecoin-based Domain Generation Algorithm and was first observed in July 2020. Doki was used in conjunction with the ngrok Mining Botnet in a campaign that targeted Docker servers in cloud platforms.

S0695

Donut

Donut is an open source framework used to generate position-independent shellcode. Donut generated code has been used by multiple threat actors to inject and load malicious payloads into memory.

S0550

DoubleAgent

DoubleAgent is a family of RAT malware dating back to 2013, known to target groups with contentious relationships with the Chinese government.

S0472

down_new

down_new is a downloader that has been used by BRONZE BUTLER since at least 2019.

S0134

Downdelph

Delphacy

Downdelph is a first-stage downloader written in Delphi that has been used by APT28 in rare instances between 2013 and 2015.

S9021

DOWNIISSA

DOWNIISSA is a shellcode downloader that has been used by MirrorFace since at least 2022 to deploy payloads, including the LODEINFO backdoor.

S0186

DownPaper

DownPaper is a backdoor Trojan; its main functionality is to download and run second stage malware.

S0694

DRATzarus

DRATzarus is a remote access tool (RAT) that has been used by Lazarus Group to target the defense and aerospace organizations globally since at least summer 2020. DRATzarus shares similarities with Bankshot, which was used by Lazarus Group in 2017 to target the Turkish financial sector.

S0300

DressCode

DressCode is an Android malware family.

S0384

Dridex

Bugat v5

Dridex is a prolific banking Trojan that first appeared in 2014. By December 2019, the US Treasury estimated Dridex had infected computers in hundreds of banks and financial institutions in over 40 countries, leading to more than $100 million in theft. Dridex was created from the source code of the Bugat banking Trojan (also known as Cridex).

S1054

Drinik

Drinik is an evolving Android banking trojan that was observed targeting customers of around 27 banks in India in August 2021. Initially seen as an SMS stealer in 2016, Drinik resurfaced as a banking trojan with more advanced capabilities included in subsequent versions between September 2021 and August 2022.

S0320

DroidJack

DroidJack is an Android remote access tool that has been observed posing as legitimate applications including the Super Mario Run and Pokemon GO games.

S0547

DropBook

DropBook is a Python-based backdoor compiled with PyInstaller.

S0502

Drovorub

Drovorub is a Linux malware toolset comprised of an agent, client, server, and kernel modules, that has been used by APT28.

S9013

DRYHOOK

DRYHOOK is Python script used to steal credentials. DRYHOOK was first reported in January 2025, and has previously been leveraged by People's Republic of China (PRC) state-affiliated threat actors identified as UNC5221 and SYLVANITE.

S0105

dsquery

dsquery.exe

dsquery is a command-line utility that can be used to query Active Directory for information from a system within a domain. It is typically installed only on Windows Server versions but can be installed on non-server variants through the Microsoft-provided Remote Server Administration Tools bundle.

S0567

Dtrack

Dtrack is spyware that was discovered in 2019 and has been used against Indian financial institutions, research facilities, and the Kudankulam Nuclear Power Plant. Dtrack shares similarities with the DarkSeoul campaign, which was attributed to Lazarus Group.

S0315

DualToy

DualToy is Windows malware that installs malicious applications onto Android and iOS devices connected over USB.

S0038

Duqu

Duqu is a malware platform that uses a modular approach to extend functionality after deployment within a target network.

S1158

DUSTPAN

DUSTPAN is an in-memory dropper written in C/C++ used by APT41 since 2021 that decrypts and executes an embedded payload.

S1159

DUSTTRAP

DUSTTRAP is a multi-stage plugin framework associated with APT41 operations with multiple components.

S0062

DustySky

NeD Worm

DustySky is multi-stage malware written in .NET that has been used by Molerats since May 2015.

S0420

Dvmap

Dvmap is rooting malware that injects malicious code into system runtime libraries. It is credited with being the first malware that performs this type of code injection.

S9038

DynoWiper

DynoWiper is a destructive malware associated with the 2025 Poland Wiper Attacks in December of 2025. DynoWiper is a native Windows binary that is distributed by a PowerShell script and overwrites files using data generated by the Mersenne Twister algorithm before they are deleted from the system. Multiple variants of DynoWiper have been identified, with the primary differences being that one variant shuts down the system after completing its destructive operations, and another introduces a time delay between file overwriting and deletion.

S0024

Dyre

Dyzap, Dyreza

Dyre is a banking Trojan that has been used for financial gain.

S0377

Ebury

Ebury is an OpenSSH backdoor and credential stealer targeting Linux servers and container hosts developed by Windigo. Ebury is primarily installed through modifying shared libraries (`.so` files) executed by the legitimate OpenSSH program. First seen in 2009, Ebury has been used to maintain a botnet of servers, deploy additional malware, and steal cryptocurrency wallets, credentials, and credit card details.

S0593

ECCENTRICBANDWAGON

ECCENTRICBANDWAGON is a remote access Trojan (RAT) used by North Korean cyber actors that was first identified in August 2020. It is a reconnaissance tool--with keylogging and screen capture functionality--used for information gathering on compromised systems.

S0624

Ecipekac

HEAVYHAND, SigLoader, DESLoader

Ecipekac is a multi-layer loader that has been used by menuPass since at least 2019 including use as a loader for P8RAT, SodaMaster, and FYAnti.

S0554

Egregor

Egregor is a Ransomware-as-a-Service (RaaS) tool that was first observed in September 2020. Researchers have noted code similarities between Egregor and Sekhmet ransomware, as well as Maze ransomware.

S0605

EKANS

SNAKEHOSE

EKANS is ransomware variant written in Golang that first appeared in mid-December 2019 and has been used against multiple sectors, including energy, healthcare, and automotive manufacturing, which in some cases resulted in significant operational disruptions. EKANS has used a hard-coded kill-list of processes, including some associated with common ICS software platforms (e.g., GE Proficy, Honeywell HMIWeb, etc), similar to those defined in MegaCortex.

S0081

Elise

BKDR_ESILE, Page

Elise is a custom backdoor Trojan that appears to be used exclusively by Lotus Blossom. It is part of a larger group of tools referred to as LStudio, ST Group, and APT0LSTU.

S0064

ELMER

ELMER is a non-persistent, proxy-aware HTTP backdoor written in Delphi that has been used by APT16.

S1247

Embargo

Embargo is a ransomware variant written in Rust that has been active since at least May 2024. Embargo ransomware operations are associated with "double extortion" ransomware activity, where data is exfiltrated from victim environments prior to encryption, with threats to publish files if a ransom is not paid. Embargo ransomware has been known to be delivered through a loader known as MDeployer which also leverages a malware component known as MS4Killer that facilitates termination of processes operating on the victim hosts. Embargo is also reportedly a Ransomware as a Service (RaaS).

S0082

Emissary

Emissary is a Trojan that has been used by Lotus Blossom. It shares code with Elise, with both Trojans being part of a malware group referred to as LStudio.

S0367

Emotet

Geodo

Emotet is a modular malware variant which is primarily used as a downloader for other malware variants such as TrickBot and IcedID. Emotet first emerged in June 2014, initially targeting the financial sector, and has expanded to multiple verticals over time.

S0363

Empire

EmPyre, PowerShell Empire

Empire is an open-source, cross-platform remote administration and post-exploitation framework that is publicly available on GitHub. While the tool itself is primarily written in Python, the post-exploitation agents are written in pure PowerShell for Windows and Python for Linux/macOS. Empire was one of five tools singled out by a joint report on public hacking tools being widely used by adversaries.

S0634

EnvyScout

EnvyScout is a dropper that has been used by APT29 since at least 2021.

S0091

Epic

Tavdig, Wipbot, WorldCupSec, TadjMakhal

Epic is a backdoor that has been used by Turla.

S1092

Escobar

Escobar is an Android banking trojan, first detected in March 2021, believed to be a new variant of AbereBot.

S0404

esentutl

esentutl.exe

esentutl is a command-line tool that provides database utilities for the Windows Extensible Storage Engine.

S0507

eSurv

eSurv is mobile surveillanceware designed for the lawful intercept market that was developed over the course of many years.

S0478

EventBot

EventBot is an Android banking trojan and information stealer that abuses Android’s accessibility service to steal data from various applications. EventBot was designed to target over 200 different banking and financial applications, the majority of which are European bank and cryptocurrency exchange applications.

S0396

EvilBunny

EvilBunny is a C++ malware sample observed since 2011 that was designed to be a execution platform for Lua scripts.

S9003

evilginx2

evilginx2 is an open-source adversary-in-the-middle (AiTM) attack framework based on the open-source nginx web server. evilginx2 can be used as a reverse proxy between victims and legitimate web services to intercept and capture credentials, authentication tokens, and session cookies.

S0152

EvilGrab

EvilGrab is a malware family with common reconnaissance capabilities. It has been deployed by menuPass via malicious Microsoft Office documents as part of spearphishing campaigns.

S0568

EVILNUM

EVILNUM is fully capable backdoor that was first identified in 2018. EVILNUM is used by the APT group Evilnum which has the same name.

S0401

Exaramel for Linux

Exaramel for Linux is a backdoor written in the Go Programming Language and compiled as a 64-bit ELF binary. The Windows version is tracked separately under Exaramel for Windows.

S0343

Exaramel for Windows

Exaramel for Windows is a backdoor used for targeting Windows systems. The Linux version is tracked separately under Exaramel for Linux.

S1179

Exbyte

Exbyte is an exfiltration tool written in Go that is uniquely associated with BlackByte operations. Observed since 2022, Exbyte transfers collected files to online file sharing and hosting services.

S0522

Exobot

Exobot is Android banking malware, primarily targeting financial institutions in Germany, Austria, and France.

S0405

Exodus

Exodus One, Exodus Two

Exodus is Android spyware deployed in two distinct stages named Exodus One (dropper) and Exodus Two (payload).

S0361

Expand

Expand is a Windows utility used to expand one or more compressed CAB files. It has been used by BBSRAT to decompress a CAB file into executable content.

S0569

Explosive

Explosive is a custom-made remote access tool used by the group Volatile Cedar. It was first identified in the wild in 2015.

S1080

Fakecalls

Fakecalls is an Android trojan, first detected in January 2021, that masquerades as South Korean banking apps. It has capabilities to intercept calls to banking institutions and even maintain realistic dialogues with the victim using pre-recorded audio snippets.

S0076

FakeM

FakeM is a shellcode-based Windows backdoor that has been used by Scarlet Mimic.

S0509

FakeSpy

FakeSpy is Android spyware that has been operated by the Chinese threat actor behind the Roaming Mantis campaigns.

S0181

FALLCHILL

FALLCHILL is a RAT that has been used by Lazarus Group since at least 2016 to target the aerospace, telecommunications, and finance industries. It is usually dropped by other Lazarus Group malware or delivered when a victim unknowingly visits a compromised website.

S0512

FatDuke

FatDuke is a backdoor used by APT29 since at least 2016.

S0171

Felismus

Felismus is a modular backdoor that has been used by Sowbug.

S0267

FELIXROOT

GreyEnergy mini

FELIXROOT is a backdoor that has been used to target Ukrainian victims.

S0679

Ferocious

Ferocious is a first stage implant composed of VBS and PowerShell scripts that has been used by WIRTE since at least 2021.

S0120

Fgdump

Fgdump is a Windows password hash dumper.

S0355

Final1stspy

Final1stspy is a dropper family that has been used to deliver DOGCALL.

S0182

FinFisher

FinSpy

FinFisher is a government-grade commercial surveillance spyware reportedly sold exclusively to government agencies for use in targeted and lawful criminal investigations. It is heavily obfuscated and uses multiple anti-analysis techniques. It has other variants including Wingbird.

S0618

FIVEHANDS

FIVEHANDS is a customized version of DEATHRANSOM ransomware written in C++. FIVEHANDS has been used since at least 2021, including in Ransomware-as-a-Service (RaaS) campaigns, sometimes along with SombRAT.

S1208

FjordPhantom

FjordPhantom is a malicious Android application first discovered in September 2024 with targets in Southeast Asia, specifically Indonesia, Thailand, and Vietnam. FjordPhantom was distributed through email and messaging applications. Once installed, the application launches a virtualization solution to steal important information, such as bank accounts, and to manipulate the user interface. The malicious activity from the virtualization solution runs alongside legitimate banking applications.

S0696

Flagpro

Flagpro is a Windows-based, first-stage downloader that has been used by BlackTech since at least October 2020. It has primarily been used against defense, media, and communications companies in Japan.

S0143

Flame

Flamer, sKyWIper

Flame is a sophisticated toolkit that has been used to collect information since at least 2010, largely targeting Middle East countries.

S0036

FLASHFLOOD

FLASHFLOOD is malware developed by APT30 that allows propagation and exfiltration of data over removable devices. APT30 may use this capability to exfiltrate data across air-gaps.

S0381

FlawedAmmyy

FlawedAmmyy is a remote access tool (RAT) that was first seen in early 2016. The code for FlawedAmmyy was based on leaked source code for a version of Ammyy Admin, a remote access software.

S0383

FlawedGrace

FlawedGrace is a fully featured remote access tool (RAT) written in C++ that was first observed in late 2017.

S0408

FlexiSpy

FlexiSpy is sophisticated surveillanceware for iOS and Android. Publicly-available, comprehensive analysis has only been found for the Android version.

FlexiSpy markets itself as a parental control and employee monitoring application.

S0173

FLIPSIDE

FLIPSIDE is a simple tool similar to Plink that is used by FIN5 to maintain access to victims.

S1103

FlixOnline

FlixOnline is an Android malware, first detected in early 2021, believed to target users of WhatsApp. FlixOnline primarily spreads via automatic replies to a device’s incoming WhatsApp messages.

S1067

FluBot

FluBot is a multi-purpose mobile banking malware that was first observed in Spain in late 2020. It primarily spread through European countries using a variety of SMS phishing messages in multiple languages. An international law enforcement operation of 11 countries eventually disrupted the spread of FluBot.

S1093

FlyTrap

FlyTrap is an Android trojan, first detected in March 2021, that uses social engineering tactics to compromise Facebook accounts. FlyTrap was initially detected through infected apps on the Google Play store, and is believed to have impacted over 10,000 victims across at least 140 countries.

S0661

FoggyWeb

FoggyWeb is a passive and highly-targeted backdoor capable of remotely exfiltrating sensitive information from a compromised Active Directory Federated Services (AD FS) server. It has been used by APT29 since at least early April 2021.

S9033

Fooder

Fooder is a custom 64-bit C/C++ loader used by MuddyWater that can decrypt and reflectively load embedded payloads such as a go-socks5 proxy utility, the open-source HackBrowserData infostealer, or the MuddyViper backdoor. Fooder has frequently masqueraded as an entertainment executable, such as the Snake game (e.g., `Snake_Game.exe`).

S0193

Forfiles

Forfiles is a Windows utility commonly used in batch jobs to execute commands on one or more selected files or directories (ex: list all directories in a drive, read the first line of all files created yesterday, etc.). Forfiles can be executed from either the command line, Run window, or batch files/scripts.

S1120

FRAMESTING

FRAMESTING is a Python web shell that was used during Cutting Edge to embed into an Ivanti Connect Secure Python package for command execution.

S0503

FrameworkPOS

Trinity

FrameworkPOS is a point of sale (POS) malware used by FIN6 to steal payment card data from sytems that run physical POS devices.

S1165

FrostyGoop

BUSTLEBERM

FrostyGoop is a Windows-based binary written in Golang that allows for interaction with industrial control system (ICS) equipment via Modbus TCP over port 502. FrostyGoop allows for reading and writing data to holding registers on targeted devices, manipulating the operation of systems for malicious purposes. FrostyGoop is associated with the FrostyGoop Incident in Ukraine.

S0577

FrozenCell

FrozenCell is the mobile component of a family of surveillanceware, with a corresponding desktop component known as KasperAgent and Micropsia.

There are multiple close variants of FrozenCell, such as VAMP, GnatSpy, Desert Scorpion and SpyC23, which add some additional functionality but are not significantly different from the original malware.

S1144

FRP

FRP, which stands for Fast Reverse Proxy, is an openly available tool that is capable of exposing a server located behind a firewall or Network Address Translation (NAT) to the Internet. FRP can support multiple protocols including TCP, UDP, and HTTP(S) and has been abused by threat actors to proxy command and control communications.

S0277

FruitFly

FruitFly is designed to spy on mac users .

S0095

ftp

ftp.exe

ftp is a utility commonly available with operating systems to transfer information over the File Transfer Protocol (FTP). Adversaries can use it to transfer other tools onto a system or to exfiltrate data.

S1044

FunnyDream

FunnyDream is a backdoor with multiple components that was used during the FunnyDream campaign since at least 2019, primarily for execution and exfiltration.

S1157

Fuxnet

Fuxnet is malware designed to impact the industrial network infrastructure managing control system sensors for utility operations in Moscow. Fuxnet is linked to an entity referred to as the Blackjack hacking group, which is assessed to be linked to Ukrainian intelligence services.

S0628

FYAnti

DILLJUICE stage2

FYAnti is a loader that has been used by menuPass since at least 2020, including to deploy QuasarRAT.

S0410

Fysbis

Fysbis is a Linux-based backdoor used by APT28 that dates back to at least 2014.

S0168

Gazer

WhiteBear

Gazer is a backdoor used by Turla since at least 2016.

S0666

Gelsemium

Gelsevirine, Gelsenicine, Gelsemine

Gelsemium is a modular malware comprised of a dropper (Gelsemine), a loader (Gelsenicine), and main (Gelsevirine) plug-ins written using the Microsoft Foundation Class (MFC) framework. Gelsemium has been used by the Gelsemium group since at least 2014.

S0049

GeminiDuke

GeminiDuke is malware that was used by APT29 from 2009 to 2012.

S0460

Get2

Get2 is a downloader written in C++ that has been used by TA505 to deliver FlawedGrace, FlawedAmmyy, Snatch and SDBbot.

S0032

gh0st RAT

Mydoor, Moudoor

gh0st RAT is a remote access tool (RAT). The source code is public and it has been used by multiple groups.

S0423

Ginp

Ginp is an Android banking trojan that has been used to target Spanish banks. Some of the code was taken directly from Anubis.

S1117

GLASSTOKEN

GLASSTOKEN is a custom web shell used by threat actors during Cutting Edge to execute commands on compromised Ivanti Secure Connect VPNs.

S9010

GlassWorm

GlassWorm is a worm that propagated through supply chain attacks by compromising repository credentials from victim environments and having malicious payloads added to those compromised accounts for distribution to victims across the various development ecosystems. GlassWorm has numerous variants, including Rust binaries, encrypted JavaScript and a variant leveraging invisible Unicode characters that made reverse engineering difficult. GlassWorm has employed a unique command and control (C2) methodology using Solana blockchain. GlassWorm was first reported in October 2025.

S0026

GLOOXMAIL

Trojan.GTALK

GLOOXMAIL is malware used by APT1 that mimics legitimate Jabber/XMPP traffic.

S1197

GoBear

GoBear is a Go-based backdoor that abuses legitimate, stolen certificates for defense evasion purposes. GoBear is exclusively linked to Kimsuky operations.

S1231

GodFather

GodFather is an Android banking malware that uses virtualization to mimic legitimate applications and abuses accessibility services and other permissions to evade detection and exfiltrate sensitive data. First identified in 2020, GodFather targets nearly 500 banking applications, cryptocurrency wallets, and exchanges worldwide; however, its virtualization-based attacks have primarily focused on several Turkish financial institutions. This capability enables threat actors to steal banking credentials and other sensitive account information.

S0249

Gold Dragon

Gold Dragon is a Korean-language, data gathering implant that was first observed in the wild in South Korea in July 2017. Gold Dragon was used along with Brave Prince and RunningRAT in operations targeting organizations associated with the 2018 Pyeongchang Winter Olympics.

S0535

Golden Cup

Golden Cup is Android spyware that has been used to target World Cup fans.

S0551

GoldenEagle

GoldenEagle is a piece of Android malware that has been used in targeting of Uyghurs, Muslims, Tibetans, individuals in Turkey, and individuals in China. Samples have been found as early as 2012.

S0493

GoldenSpy

GoldenSpy is a backdoor malware which has been packaged with legitimate tax preparation software. GoldenSpy was discovered targeting organizations in China, being delivered with the "Intelligent Tax" software suite which is produced by the Golden Tax Department of Aisino Credit Information Co. and required to pay local taxes.

S0597

GoldFinder

GoldFinder is a custom HTTP tracer tool written in Go that logs the route a packet takes between a compromised network and a C2 server. It can be used to inform threat actors of potential points of discovery or logging of their actions, including C2 related to other malware. GoldFinder was discovered in early 2021 during an investigation into the SolarWinds Compromise by APT29.

S0588

GoldMax

SUNSHUTTLE

GoldMax is a second-stage C2 backdoor written in Go with Windows and Linux variants that are nearly identical in functionality. GoldMax was discovered in early 2021 during the investigation into the SolarWinds Compromise, and has likely been used by APT29 since at least mid-2019. GoldMax uses multiple defense evasion techniques, including avoiding virtualization execution and masking malicious traffic.

S0421

GolfSpy

GolfSpy is Android spyware deployed by the group Bouncing Golf.

S1198

Gomir

Gomir is a Linux backdoor variant of the Go-based malware GoBear, uniquely assoicated with Kimsuky operations.

S0290

Gooligan

Ghost Push

Gooligan is a malware family that runs privilege escalation exploits on Android devices and then uses its escalated privileges to steal authentication tokens that can be used to access data from many Google applications. Gooligan has been described as part of the Ghost Push Android malware family.

S0477

Goopy

Goopy is a Windows backdoor and Trojan used by APT32 and shares several similarities to another backdoor used by the group (Denis). Goopy is named for its impersonation of the legitimate Google Updater executable.

S1138

Gootloader

Gootloader is a Javascript-based infection framework that has been used since at least 2020 as a delivery method for the Gootkit banking trojan, Cobalt Strike, REvil, and others. Gootloader operates on an "Initial Access as a Service" model and has leveraged SEO Poisoning to provide access to entities in multiple sectors worldwide including financial, military, automotive, pharmaceutical, and energy.

S0536

GPlayed

GPlayed is an Android trojan with a broad range of capabilities.

S0531

Grandoreiro

Grandoreiro is a banking trojan written in Delphi that was first observed in 2016 and uses a Malware-as-a-Service (MaaS) business model. Grandoreiro has confirmed victims in Brazil, Mexico, Portugal, and Spain.

S0237

GravityRAT

GravityRAT is a remote access tool (RAT) and has been in ongoing development since 2016. The actor behind the tool remains unknown, but two usernames have been recovered that link to the author, which are "TheMartian" and "The Invincible." According to the National Computer Emergency Response Team (CERT) of India, the malware has been identified in attacks against organization and entities in India.

S0690

Green Lambert

Green Lambert is a modular backdoor that security researchers assess has been used by an advanced threat group referred to as Longhorn and The Lamberts. First reported in 2017, the Windows variant of Green Lambert may have been used as early as 2008; a macOS version was uploaded to a multiscanner service in September 2014.

S0342

GreyEnergy

GreyEnergy is a backdoor written in C and compiled in Visual Studio. GreyEnergy shares similarities with the BlackEnergy malware and is thought to be the successor of it.

S0417

GRIFFON

GRIFFON is a JavaScript backdoor used by FIN7.

S0632

GrimAgent

GrimAgent is a backdoor that has been used before the deployment of Ryuk ransomware since at least 2020; it is likely used by FIN6 and Wizard Spider.

S0008

gsecdump

gsecdump is a publicly-available credential dumper used to obtain password hashes and LSA secrets from Windows operating systems.

S0561

GuLoader

GuLoader is a file downloader that has been used since at least December 2019 to distribute a variety of remote administration tool (RAT) malware, including NETWIRE, Agent Tesla, NanoCore, FormBook, and Parallax RAT.

S0406

Gustuff

Gustuff is mobile malware designed to steal users' banking and virtual currency credentials.

S0132

H1N1

H1N1 is a malware variant that has been distributed via a campaign using VBA macros to infect victims. Although it initially had only loader capabilities, it has evolved to include information-stealing functionality.

S0047

Hacking Team UEFI Rootkit

Hacking Team UEFI Rootkit is a rootkit developed by the company Hacking Team as a method of persistence for remote access software.

S0151

HALFBAKED

HALFBAKED is a malware family consisting of multiple components intended to establish persistence in victim networks.

S0037

HAMMERTOSS

HammerDuke, NetDuke

HAMMERTOSS is a backdoor that was used by APT29 in 2015.

S0499

Hancitor

Chanitor

Hancitor is a downloader that has been used by Pony and other information stealing malware.

S1211

Hannotog

Hannotog is a type of backdoor malware uniquely assoicated with Lotus Blossom operations since at least 2022.

S0214

HAPPYWORK

HAPPYWORK is a downloader used by APT37 to target South Korean government and financial victims in November 2016.

S0246

HARDRAIN

HARDRAIN is a Trojan malware variant reportedly used by the North Korean government.

S0224

Havij

Havij is an automatic SQL Injection tool distributed by the Iranian ITSecTeam security company. Havij has been used by penetration testers and adversaries.

S1229

Havoc

Havoc is an open-source post-exploitation command and control (C2) framework first released on GitHub in October 2022 by C5pider (Paul Ungur), who continues to maintain and develop it with community contributors. Havoc provides a wide range of offensive security capabilities and has been adopted by multiple threat actors to establish and maintain control over compromised systems.

S0391

HAWKBALL

HAWKBALL is a backdoor that was observed in targeting of the government sector in Central Asia.

S0071

hcdLoader

hcdLoader is a remote access tool (RAT) that has been used by APT18.

S0061

HDoor

Custom HDoor

HDoor is malware that has been customized and used by the Naikon group.

S9018

HeartCrypt

HeartCrypt is a packer-as-a-service (PaaS) used to protect malware that has been available since at least 2024. HeartCrypt has been used to pack a variety of malware including Lumma Stealer, Remcos, and Rhadamanthys. In the HeartCrypt PaaS model, customers submit malware via private messaging services and it is then packed and returned by the operator as a new binary.

S0617

HELLOKITTY

HELLOKITTY is a ransomware written in C++ that shares similar code structure and functionality with DEATHRANSOM and FIVEHANDS. HELLOKITTY has been used since at least 2020, targets have included a Polish video game developer and a Brazilian electric power company.

S0170

Helminth

Helminth is a backdoor that has at least two variants - one written in VBScript and PowerShell that is delivered via a macros in Excel spreadsheets, and one that is a standalone Windows executable.

S0544

HenBox

HenBox is Android malware that attempts to only execute on Xiaomi devices running the MIUI operating system. HenBox has primarily been used to target Uyghurs, a minority Turkic ethnic group.

S0697

HermeticWiper

Trojan.Killdisk, DriveSlayer

HermeticWiper is a data wiper that has been used since at least early 2022, primarily against Ukraine with additional activity observed in Latvia and Lithuania. Some sectors targeted include government, financial, defense, aviation, and IT services.

S0698

HermeticWizard

HermeticWizard is a worm that has been used to spread HermeticWiper in attacks against organizations in Ukraine since at least 2022.

S1249

HexEval Loader

HexEval Loader is a hex-encoded loader that collects host data, decodes follow-on scripts and acts as a downloader for the BeaverTail malware. HexEval Loader was first reported in April 2025. HexEval Loader has previously been leveraged by North Korea-affiliated threat actors identified as Contagious Interview. HexEval Loader has been delivered to victims through code repository sites utilizing typosquatting naming conventions of various npm packages.

S1027

Heyoka Backdoor

Heyoka Backdoor is a custom backdoor--based on the Heyoka open source exfiltration tool--that has been used by Aoqin Dragon since at least 2013.

S0087

Hi-Zor

Hi-Zor is a remote access tool (RAT) that has characteristics similar to Sakula. It was used in a campaign named INOCNATION.

S9023

HiddenFace

NOOPDOOR

HiddenFace is a modular backdoor developed and used exclusively by MirrorFace since at least 2021. HiddenFace can communicate both actively and passively and has been used against political and academic targets.

S0394

HiddenWasp

HiddenWasp is a Linux-based Trojan used to target systems for remote control. It comes in the form of a statically linked ELF binary with stdlibc++.

S0135

HIDEDRV

HIDEDRV is a rootkit used by APT28. It has been deployed along with Downdelph to execute and hide that malware.

S0009

Hikit

Hikit is malware that has been used by Axiom for late-stage persistence and exfiltration after the initial compromise.

S1128

HilalRAT

HilalRAT is a remote access-capable Android malware, developed and used by UNC788. HilalRAT is capable of collecting data, such as device location, call logs, etc., and is capable of executing actions, such as activating a device's camera and microphone.

S0601

Hildegard

Hildegard is malware that targets misconfigured kubelets for initial access and runs cryptocurrency miner operations. The malware was first observed in January 2021. The TeamTNT activity group is believed to be behind Hildegard.

S1230

HIUPAN

HIUPAN (aka U2DiskWatch) is a is a worm that propagates through removable drives known to be leveraged by Mustang Panda and was first observed utilized in 2024.

S0232

HOMEFRY

HOMEFRY is a 64-bit Windows password dumper/cracker that has previously been used in conjunction with other Leviathan backdoors.

S0376

HOPLIGHT

HOPLIGHT is a backdoor Trojan that has reportedly been used by the North Korean government.

S1077

Hornbill

Hornbill is one of two mobile malware families known to be used by the APT Confucius. Analysis suggests that Hornbill was first active in early 2018. While Hornbill and Sunbird overlap in core capabilities, Hornbill has tools and behaviors suggesting more passive reconnaissance.

S0431

HotCroissant

HotCroissant is a remote access trojan (RAT) attributed by U.S. government entities to malicious North Korean government cyber activity, tracked collectively as HIDDEN COBRA. HotCroissant shares numerous code similarities with Rifdoor.

S0040

HTRAN

HUC Packet Transmit Tool

HTRAN is a tool that proxies connections through intermediate hops and aids users in disguising their true geographical location. It can be used by adversaries to hide their location when interacting with the victim networks.

S0070

HTTPBrowser

Token Control, HttpDump

HTTPBrowser is malware that has been used by several threat groups. It is believed to be of Chinese origin.

S0068

httpclient

httpclient is malware used by Putter Panda. It is a simple tool that provides a limited range of functionality, suggesting it is likely used as a second-stage or supplementary/backup tool.

S9007

HTTPTroy

HTTPTroy is a highly obfuscated backdoor that facilitates collection, command and control, defense evasion and exfiltration. HTTPTroy was first reported in October 2025. HTTPTroy has been observed in operations attributed to DPRK-affiliated threat actors, including Kimsuky. HTTPTroy has been delivered to victims through a separate loader leveraged by Kimsuky.

S1097

HUI Loader

HUI Loader is a custom DLL loader that has been used since at least 2015 by China-based threat groups including Cinnamon Tempest and menuPass to deploy malware on compromised hosts. HUI Loader has been observed in campaigns loading SodaMaster, PlugX, Cobalt Strike, Komplex, and several strains of ransomware.

S0322

HummingBad

HummingBad is a family of Android malware that generates fraudulent advertising revenue and has the ability to obtain root access on older, vulnerable versions of Android.

S0321

HummingWhale

HummingWhale is an Android malware family that performs ad fraud.

S0203

Hydraq

Roarur, MdmBot, HomeUnix, Homux, HidraQ, HydraQ, McRat, Aurora, 9002 RAT

Hydraq is a data-theft trojan first used by Elderwood in the 2009 Google intrusion known as Operation Aurora, though variations of this trojan have been used in more recent campaigns by other Chinese actors, possibly including APT17.

S0398

HyperBro

HyperBro is a custom in-memory backdoor used by Threat Group-3390.

S0537

HyperStack

HyperStack is a RPC-based backdoor used by Turla since at least 2018. HyperStack has similarities to other backdoors used by Turla including Carbon.

S1022

IceApple

IceApple is a modular Internet Information Services (IIS) post-exploitation framework, that has been used since at least 2021 against the technology, academic, and government sectors.

S0483

IcedID

IcedID is a modular banking malware designed to steal financial information that has been observed in the wild since at least 2017. IcedID has been downloaded by Emotet in multiple campaigns.

S0101

ifconfig

ifconfig is a Unix-based utility used to gather information about and interact with the TCP/IP settings on a system.

S0278

iKitten

OSX/MacDownloader

iKitten is a macOS exfiltration agent .

S1152

IMAPLoader

IMAPLoader is a .NET-based loader malware exclusively associated with CURIUM operations since at least 2022. IMAPLoader leverages email protocols for command and control and payload delivery.

S0434

Imminent Monitor

Imminent Monitor was a commodity remote access tool (RAT) offered for sale from 2012 until 2019, when an operation was conducted to take down the Imminent Monitor infrastructure. Various cracked versions and variations of this RAT are still in circulation.

S0357

Impacket

Impacket is an open source collection of modules written in Python for programmatically constructing and manipulating network protocols. Impacket contains several tools for remote service execution, Kerberos manipulation, Windows credential dumping, packet sniffing, and relay attacks.

S1139

INC Ransomware

INC Ransomware is a ransomware strain that has been used by the INC Ransom group since at least 2023 against multiple industry sectors worldwide. INC Ransomware can employ partial encryption combined with multi-threading to speed encryption.

S1045

INCONTROLLER

PIPEDREAM

INCONTROLLER is custom malware that includes multiple modules tailored towards ICS devices and technologies, including Schneider Electric and Omron PLCs as well as OPC UA, Modbus, and CODESYS protocols. INCONTROLLER has the ability to discover specific devices, download logic on the devices, and exploit platform-specific vulnerabilities. As of September 2022, some security researchers assessed INCONTROLLER was developed by CHERNOVITE.

S0604

Industroyer

CRASHOVERRIDE, Win32/Industroyer

Industroyer is a sophisticated malware framework designed to cause an impact to the working processes of Industrial Control Systems (ICS), specifically components used in electrical substations. Industroyer was used in the attacks on the Ukrainian power grid in December 2016. This is the first publicly known malware specifically designed to target and impact operations in the electric grid.

S1072

Industroyer2

Industroyer2 is a compiled and static piece of malware that has the ability to communicate over the IEC-104 protocol. It is similar to the IEC-104 module found in Industroyer. Security researchers assess that Industroyer2 was designed to cause impact to high-voltage electrical substations. The initial Industroyer2 sample was compiled on 03/23/2022 and scheduled to execute on 04/08/2022, however it was discovered before deploying, resulting in no impact.

S0259

InnaputRAT

InnaputRAT is a remote access tool that can exfiltrate files from a victim’s machine. InnaputRAT has been seen out in the wild since 2016.

S0463

INSOMNIA

INSOMNIA is spyware that has been used by the group Evil Eye.

S1245

InvisibleFerret

InvisibleFerret is a modular python malware that is leveraged for data exfiltration and remote access capabilities. InvisibleFerret consists of four modules: main, payload, browser, and AnyDesk. InvisibleFerret malware has been leveraged by North Korea-affiliated threat actors identified as DeceptiveDevelopment or Contagious Interview since 2023. InvisibleFerret has historically been introduced to the victim environment through the use of the BeaverTail malware.

S0260

InvisiMole

InvisiMole is a modular spyware program that has been used by the InvisiMole Group since at least 2013. InvisiMole has two backdoor modules called RC2FM and RC2CL that are used to perform post-exploitation activities. It has been discovered on compromised victims in the Ukraine and Russia. Gamaredon Group infrastructure has been used to download and execute InvisiMole against a small number of victims.

S0231

Invoke-PSImage

Invoke-PSImage takes a PowerShell script and embeds the bytes of the script into the pixels of a PNG image. It generates a one liner for executing either from a file of from the web. Example of usage is embedding the PowerShell code from the Invoke-Mimikatz module and embed it into an image file. By calling the image file from a macro for example, the macro will download the picture and execute the PowerShell code, which in this case will dump the passwords.

S0100

ipconfig

ipconfig is a Windows utility that can be used to find information about a system's TCP/IP, DNS, DHCP, and adapter configuration.

S1132

IPsec Helper

IPsec Helper is a post-exploitation remote access tool linked to Agrius operations. This malware shares significant programming and functional overlaps with Apostle ransomware, also linked to Agrius. IPsec Helper provides basic remote access tool functionality such as uploading files from victim systems, running commands, and deploying additional payloads.

S0581

IronNetInjector

IronNetInjector is a Turla toolchain that utilizes scripts from the open-source IronPython implementation of Python with a .NET injector to drop one or more payloads including ComRAT.

S9029

IronWind

IronWind is a custom loader malware that has been in use since at least 2023 by actors including WIRTE to target entities in the Middle East.

S0189

ISMInjector

ISMInjector is a Trojan used to install another OilRig backdoor, ISMAgent.

S0015

Ixeshe

Ixeshe is a malware family that has been used since at least 2009 against targets in East Asia.

S1203

J-magic

J-magic is a custom variant of the cd00r backdoor tailored to target Juniper routers that was first observed during the J-magic Campaign in mid-2023. J-magic monitors TCP traffic for five predefined parameters or "magic packets" to be sent by the attackers before activating on compromised devices.

S0163

Janicab

Janicab is an OS X trojan that relied on a valid developer ID and oblivious users to install it.

S0528

Javali

Javali is a banking trojan that has targeted Portuguese and Spanish-speaking countries since 2017, primarily focusing on customers of financial institutions in Brazil and Mexico.

S0389

JCry

JCry is ransomware written in Go. It was identified as apart of the #OpJerusalem 2019 campaign.

S0044

JHUHUGIT

Trojan.Sofacy, Seduploader, JKEYSKW, Sednit, GAMEFISH, SofacyCarberp

JHUHUGIT is malware used by APT28. It is based on Carberp source code and serves as reconnaissance malware.

S0201

JPIN

JPIN is a custom-built backdoor family used by PLATINUM. Evidence suggests developers of JPIN and Dipsind code bases were related in some way.

S0283

jRAT

JSocket, AlienSpy, Frutas, Sockrat, Unrecom, jFrutas, Adwind, jBiFrost, Trojan.Maljava

jRAT is a cross-platform, Java-based backdoor originally available for purchase in 2012. Variants of jRAT have been distributed via a software-as-a-service platform, similar to an online subscription model.

S0648

JSS Loader

JSS Loader is Remote Access Trojan (RAT) with .NET and C++ variants that has been used by FIN7 since at least 2020.

S0325

Judy

Judy is auto-clicking adware that was distributed through multiple apps in the Google Play Store.

S1206

JumbledPath
