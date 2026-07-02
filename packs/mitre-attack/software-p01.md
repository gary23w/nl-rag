---
title: "Software (part 1/5)"
source: https://attack.mitre.org/software/
domain: mitre-attack
license: CC-BY-SA-4.0
tags: mitre att&ck, adversary tactics techniques, att&ck framework, cyber kill chain, threat actor behavior
fetched: 2026-07-02
part: 1/5
---

# Software

Software is a generic term for custom or commercial code, operating system utilities, open-source software, or other tools used to conduct behavior modeled in ATT&CK. Some instances of software have multiple names associated with the same instance due to various organizations tracking the same set of software by different names. The team makes a best effort to track overlaps between names based on publicly reported associations, which are designated as “Associated Software” on each page (formerly labeled “Aliases”), because we believe these overlaps are useful for analyst awareness.

Software entries include publicly reported technique use or capability to use a technique and may be mapped to Groups who have been reported to use that Software. The information provided does not represent all possible technique use by a piece of Software, but rather a subset that is available solely through open source reporting.

- Tool - Commercial, open-source, built-in, or publicly available software that could be used by a defender, pen tester, red teamer, or an adversary. This category includes both software that generally is not found on an enterprise system as well as software generally available as part of an operating system that is already present in an environment. Examples include PsExec, Metasploit, Mimikatz, as well as Windows utilities such as Net, netstat, Tasklist, etc.
- Malware - Commercial, custom closed source, or open source software intended to be used for malicious purposes by adversaries. Examples include PlugX, CHOPSTICK, etc.

###### Software: 949

ID

Name

Associated Software

Description

S0066

3PARA RAT

3PARA RAT is a remote access tool (RAT) programmed in C++ that has been used by Putter Panda.

S0065

4H RAT

4H RAT is malware that has been used by Putter Panda since at least 2007.

S0677

AADInternals

AADInternals is a PowerShell-based framework for administering, enumerating, and exploiting Azure Active Directory. The tool is publicly available on GitHub.

S0469

ABK

ABK is a downloader that has been used by BRONZE BUTLER since at least 2019.

S1061

AbstractEmu

AbstractEmu is mobile malware that was first seen in Google Play and other third-party stores in October 2021. It was discovered in 19 Android applications, of which at least 7 abused known Android exploits for obtaining root permissions. AbstractEmu was observed primarily impacting users in the United States, however victims are believed to be across a total of 17 countries.

S1000

ACAD/Medre.A

ACAD/Medre.A is a worm that steals operational information. The worm collects AutoCAD files with drawings. ACAD/Medre.A has the capability to be used for industrial espionage.

S1167

AcidPour

AcidPour is a variant of AcidRain designed to impact a wider range of x86 architecture Linux devices. AcidPour is an x86 ELF binary that expands on the targeted devices and locations in AcidRain by including items such as Unsorted Block Image (UBI), Deice Mapper (DM), and various flash memory references. Based on this expanded targeting, AcidPour can impact a variety of device types including IoT, networking, and ICS embedded device types. AcidPour is a wiping payload associated with the Sandworm Team threat actor, and potentially linked to attacks against Ukrainian internet service providers (ISPs) in 2023.

S1125

AcidRain

AcidRain is an ELF binary targeting modems and routers using MIPS architecture. AcidRain is associated with the ViaSat KA-SAT communication outage that took place during the initial phases of the 2022 full-scale invasion of Ukraine. Analysis indicates overlap with another network device-targeting malware, VPNFilter, associated with Sandworm Team. US and European government sources linked AcidRain to Russian government entities, while Ukrainian government sources linked AcidRain specifically to Sandworm Team.

S1028

Action RAT

Action RAT is a remote access tool written in Delphi that has been used by SideCopy since at least December 2021 against Indian and Afghani government personnel.

S0202

adbupd

adbupd is a backdoor used by PLATINUM that is similar to Dipsind.

S0552

AdFind

AdFind is a free command-line query tool that can be used for gathering information from Active Directory.

S0309

Adups

Adups is software that was pre-installed onto Android devices, including those made by BLU Products. The software was reportedly designed to help a Chinese phone manufacturer monitor user behavior, transferring sensitive data to a Chinese server.

S0045

ADVSTORESHELL

AZZY, EVILTOSS, NETUI, Sedreco

ADVSTORESHELL is a spying backdoor that has been used by APT28 from at least 2012 to 2016. It is generally used for long-term espionage and is deployed on targets deemed interesting after a reconnaissance phase.

S0440

Agent Smith

Agent Smith is mobile malware that generates financial gain by replacing legitimate applications on devices with malicious versions that include fraudulent ads. As of July 2019 Agent Smith had infected around 25 million devices, primarily targeting India though effects had been observed in other Asian countries as well as Saudi Arabia, the United Kingdom, and the United States.

S0331

Agent Tesla

Agent Tesla is a spyware Trojan written for the .NET framework that has been observed since at least 2014.

S0092

Agent.btz

Agent.btz is a worm that primarily spreads itself via removable devices such as USB drives. It reportedly infected U.S. military networks in 2008.

S1095

AhRat

AhRat is an Android remote access tool based on the open-source AhMyth remote access tool. AhRat initially spread in August 2022 on the Google Play Store via an update containing malicious code to the previously benign application, "iRecorder – Screen Recorder," which itself was released in September 2021.

S1129

Akira

Akira ransomware, written in C++, is most prominently (but not exclusively) associated with the ransomware-as-a-service entity Akira. Akira ransomware has been used in attacks across North America, Europe, and Australia, with a focus on critical infrastructure sectors including manufacturing, education, and IT services. Akira ransomware employs hybrid encryption and threading to increase the speed and efficiency of encryption and runtime arguments for tailored attacks. Notable variants include Rust-based Megazord for targeting Windows and Akira _v2 for targeting VMware ESXi servers.

S1194

Akira _v2

Akira _v2 is a Rust-based variant of Akira ransomware that has been in use since at least 2024. Akira _v2 is designed to target VMware ESXi servers and includes a new command-line argument set and other expanded capabilities.

S0319

Allwinner

Allwinner is a company that supplies processors used in Android tablets and other devices. A Linux kernel distributed by Allwinner for use on these devices reportedly contained a backdoor.

S1025

Amadey

Amadey is a Trojan bot that has been used since at least October 2018.

S0504

Anchor

Anchor_DNS

Anchor is one of a family of backdoor malware that has been used in conjunction with TrickBot on selected high profile targets since at least 2018.

S0525

Android/AdDisplay.Ashas

Android/AdDisplay.Ashas is a variant of adware that has been distributed through multiple apps in the Google Play Store.

S0304

Android/Chuli.A

Android/Chuli.A is Android malware that was delivered to activist groups via a spearphishing email with an attachment.

S1214

Android/SpyAgent

Android/SpyAgent is a variant of spyware in the MoqHao phishing campaign primarily targeting Korean and Japanese users. Fake security applications were used to target Japanese users, while fake police applications were used to target Korean users. Both fake applications have common C2 commands and share the same crash report key on a cloud service.

S0524

AndroidOS/MalLocker.B

AndroidOS/MalLocker.B is a variant of a ransomware family targeting Android devices. It prevents the user from interacting with the UI by displaying a screen containing a ransom note over all other windows.

S0310

ANDROIDOS_ANSERVER.A

ANDROIDOS_ANSERVER.A is Android malware that is unique because it uses encrypted content within a blog site for command and control.

S1074

ANDROMEDA

ANDROMEDA is commodity malware that was widespread in the early 2010's and continues to be observed in infections across a wide variety of industries. During the 2022 C0026 campaign, threat actors re-registered expired ANDROMEDA C2 domains to spread malware to select targets in Ukraine.

S0292

AndroRAT

AndroRAT is an open-source remote access tool for Android devices. AndroRAT is capable of collecting data, such as device location, call logs, etc., and is capable of executing actions, such as sending SMS messages and taking pictures. It is originally available through the `The404Hacking` Github repository.

S9027

ANELLDR

ANELLDR, a loader that has been in use since at least 2018, was designed to decrypt and execute UPPERCUT in memory. ANELLDR can use anti-analysis techniques and is known to share code overlap with HiddenFace.

S0422

Anubis

Anubis is Android malware that was originally used for cyber espionage, and has been retooled as a banking trojan.

S1133

Apostle

Apostle is malware that has functioned as both a wiper and, in more recent versions, as ransomware. Apostle is written in .NET and shares various programming and functional overlaps with IPsec Helper.

S0584

AppleJeus

AppleJeus is a family of downloaders initially discovered in 2018 embedded within trojanized cryptocurrency applications. AppleJeus has been used by Lazarus Group, targeting companies in the energy, finance, government, industry, technology, and telecommunications sectors, and several countries including the United States, United Kingdom, South Korea, Australia, Brazil, New Zealand, and Russia. AppleJeus has been used to distribute the FALLCHILL RAT.

S0622

AppleSeed

AppleSeed is a backdoor that has been used by Kimsuky to target South Korean government, academic, and commercial targets since at least 2021.

S0456

Aria-body

Aria-body is a custom backdoor that has been used by Naikon since approximately 2017.

S0099

Arp

arp.exe

Arp displays and modifies information about a system's Address Resolution Protocol (ARP) cache.

S0540

Asacub

Trojan-SMS.AndroidOS.Smaps

Asacub is a banking trojan that attempts to steal money from victims’ bank accounts. It attempts to do this by initiating a wire transfer via SMS message from compromised devices.

S9031

AshTag

AshTag is a modular .NET backdoor with multiple features that has been used by WIRTE since at least 2025. AshTag is designed for persistence and remote command execution and can masquerade as a legitimate VisualServer utility.

S0073

ASPXSpy

ASPXTool

ASPXSpy is a Web shell. It has been modified by Threat Group-3390 actors to create the ASPXTool version.

S0373

Astaroth

Guildma

Astaroth is a Trojan and information stealer known to affect companies in Europe, Brazil, and throughout Latin America. It has been known publicly since at least late 2017.

S1087

AsyncRAT

AsyncRAT is an open-source remote access tool originally available through the NYANxCAT Github repository that has been used in malicious campaigns.

S0110

at

at.exe

at is used to schedule tasks on a system to run at a specified date or time.

S0438

Attor

Attor is a Windows-based espionage platform that has been seen in use since 2013. Attor has a loadable plugin architecture to customize functionality for specific targets.

S1176

attrib

attrib.exe

attrib is a Windows utility used to display, set or remove attributes assigned to files or directories.

S0347

AuditCred

Roptimizer

AuditCred is a malicious DLL that has been used by Lazarus Group during their 2018 attacks.

S1029

AuTo Stealer

AuTo Stealer is malware written in C++ has been used by SideCopy since at least December 2021 to target government agencies and personnel in India and Afghanistan.

S0129

AutoIt backdoor

AutoIt backdoor is malware that has been used by the actors responsible for the MONSOON campaign. The actors frequently used it in weaponized .pps files exploiting CVE-2014-6352. This malware makes use of the legitimate scripting language for Windows GUI automation with the same name.

S0640

Avaddon

Avaddon is ransomware written in C++ that has been offered as Ransomware-as-a-Service (RaaS) since at least June 2020.

S0473

Avenger

Avenger is a downloader that has been used by BRONZE BUTLER since at least 2019.

S1053

AvosLocker

AvosLocker is ransomware written in C++ that has been offered via the Ransomware-as-a-Service (RaaS) model. It was first observed in June 2021 and has been used against financial services, critical manufacturing, government facilities, and other critical infrastructure sectors in the United States. As of March 2022, AvosLocker had also been used against organizations in Belgium, Canada, China, Germany, Saudi Arabia, Spain, Syria, Taiwan, Turkey, the United Arab Emirates, and the United Kingdom.

S0344

Azorult

Azorult is a commercial Trojan that is used to steal information from compromised hosts. Azorult has been observed in the wild as early as 2016. In July 2018, Azorult was seen used in a spearphishing campaign against targets in North America. Azorult has been seen used for cryptocurrency theft.

S0638

Babuk

Babyk, Vasa Locker

Babuk is a Ransomware-as-a-service (RaaS) malware that has been used since at least 2021. The operators of Babuk employ a "Big Game Hunting" approach to targeting major enterprises and operate a leak site to post stolen data as part of their extortion scheme.

S0414

BabyShark

LATEOP

BabyShark is a Microsoft Visual Basic (VB) script-based malware family that is believed to be associated with several North Korean campaigns.

S0475

BackConfig

BackConfig is a custom Trojan with a flexible plugin architecture that has been used by Patchwork.

S0093

Backdoor.Oldrea

Havex

Backdoor.Oldrea is a modular backdoor that used by Dragonfly against energy companies since at least 2013. Backdoor.Oldrea was distributed via supply chain compromise, and included specialized modules to enumerate and map ICS-specific systems, processes, and protocols.

S0031

BACKSPACE

Lecna

BACKSPACE is a backdoor used by APT30 that dates back to at least 2005.

S0606

Bad Rabbit

Win32/Diskcoder.D

Bad Rabbit is a self-propagating ransomware that affected the Ukrainian transportation sector in 2017. Bad Rabbit has also targeted organizations and consumers in Russia.

S0245

BADCALL

BADCALL is a Trojan malware variant used by the group Lazarus Group.

S0642

BADFLICK

BADFLICK is a backdoor used by Leviathan in spearphishing campaigns first reported in 2018 that targeted the U.S. engineering and maritime industries.

S1081

BADHATCH

BADHATCH is a backdoor that has been utilized by FIN8 since at least 2019. BADHATCH has been used to target the insurance, retail, technology, and chemical industries in the United States, Canada, South Africa, Panama, and Italy.

S0128

BADNEWS

BADNEWS is malware that has been used by the actors responsible for the Patchwork campaign. Its name was given due to its use of RSS feeds, forums, and blogs for command and control.

S0337

BadPatch

BadPatch is a Windows Trojan that was used in a Gaza Hackers-linked campaign.

S0234

Bandook

Bandook is a commercially available RAT, written in Delphi and C++, that has been available since at least 2007. It has been used against government, financial, energy, healthcare, education, IT, and legal organizations in the US, South America, Europe, and Southeast Asia. Bandook has been used by Dark Caracal, as well as in a separate campaign referred to as "Operation Manul".

S0239

Bankshot

Trojan Manuscript

Bankshot is a remote access tool (RAT) that was first reported by the Department of Homeland Security in December of 2017. In 2018, Lazarus Group used the Bankshot implant in attacks against the Turkish financial sector.

S0534

Bazar

KEGTAP, Team9, Bazaloader

Bazar is a downloader and backdoor that has been used since at least April 2020, with infections primarily against professional services, healthcare, manufacturing, IT, logistics and travel companies across the US and Europe. Bazar reportedly has ties to TrickBot campaigns and can be used to deploy additional malware, including ransomware, and to steal sensitive data.

S0470

BBK

BBK is a downloader that has been used by BRONZE BUTLER since at least 2019.

S0127

BBSRAT

BBSRAT is malware with remote access tool functionality that has been used in targeted compromises.

S1246

BeaverTail

BeaverTail is a malware that has both a JavaScript and C++ variant. Active since 2022, BeaverTail is capable of stealing logins from browsers and serves as a downloader for second stage payloads. BeaverTail has previously been leveraged by North Korea-affiliated actors identified as DeceptiveDevelopment or Contagious Interview. BeaverTail has been delivered to victims through code repository sites and has been embedded within malicious attachments.

S0574

BendyBear

BendyBear is an x64 shellcode for a stage-zero implant designed to download malware from a C2 server. First discovered in August 2020, BendyBear shares a variety of features with Waterbear, malware previously attributed to the Chinese cyber espionage group BlackTech.

S1136

BFG Agonizer

BFG Agonizer is a wiper related to the open-source project CRYLINE-v.5.0. The malware is associated with wiping operations conducted by the Agrius threat actor.

S1215

Binary Validator

Binary Validator is a Mach-O binary file used during Operation Triangulation. Binary Validator first collects information about the device, such as the device's phone number and a list of installed applications, before the deployment of the TriangleDB implant. After the actions are completed and the data is collected, Binary Validator encrypts and sends the data to the C2 server, and in turn, the C2 server sends the TriangleDB implant.

S0017

BISCUIT

BISCUIT is a backdoor that has been used by APT1 since as early as 2007.

S0268

Bisonal

Bisonal is a remote access tool (RAT) that has been used by Tonto Team against public and private sector organizations in Russia, South Korea, and Japan since at least December 2010.

S0570

BitPaymer

wp_encrypt, FriedEx

BitPaymer is a ransomware variant first observed in August 2017 targeting hospitals in the U.K. BitPaymer uses a unique encryption key, ransom note, and contact information for each operation. BitPaymer has several indicators suggesting overlap with the Dridex malware and is often delivered via Dridex.

S0190

BITSAdmin

BITSAdmin is a command line tool used to create and manage BITS Jobs.

S1070

Black Basta

Black Basta is ransomware written in C++ that has been offered within the ransomware-as-a-service (RaaS) model since at least April 2022; there are variants that target Windows and VMWare ESXi servers. Black Basta operations have included the double extortion technique where in addition to demanding ransom for decrypting the files of targeted organizations the cyber actors also threaten to post sensitive information to a leak site if the ransom is not paid. Black Basta affiliates have targeted multiple high-value organizations, with the largest number of victims based in the U.S. Based on similarities in TTPs, leak sites, payment sites, and negotiation tactics, security researchers assess the Black Basta RaaS operators could include current or former members of the Conti group.

S1181

BlackByte 2.0 Ransomware

BlackByte 2.0 Ransomware is a replacement for BlackByte Ransomware. Unlike BlackByte Ransomware, BlackByte 2.0 Ransomware does not have a common key for victim decryption. BlackByte 2.0 Ransomware remains uniquely associated with BlackByte operations.

S1180

BlackByte Ransomware

BlackByte Ransomware is uniquely associated with BlackByte operations. BlackByte Ransomware used a common key for infections, allowing for the creation of a universal decryptor. BlackByte Ransomware was replaced in BlackByte operations by BlackByte 2.0 Ransomware by 2023.

S1068

BlackCat

ALPHV, Noberus

BlackCat is ransomware written in Rust that has been offered via the Ransomware-as-a-Service (RaaS) model. First observed November 2021, BlackCat has been used to target multiple sectors and organizations in various countries and regions in Africa, the Americas, Asia, Australia, and Europe.

S0069

BLACKCOFFEE

BLACKCOFFEE is malware that has been used by several Chinese groups since at least 2013.

S0089

BlackEnergy

Black Energy

BlackEnergy is a malware toolkit that has been used by both criminal and APT actors. It dates back to at least 2007 and was originally designed to create botnets for use in conducting Distributed Denial of Service (DDoS) attacks, but its use has evolved to support various plug-ins. It is well known for being used during the confrontation between Georgia and Russia in 2008, as well as in targeting Ukrainian institutions. Variants include BlackEnergy 2 and BlackEnergy 3.

S0564

BlackMould

BlackMould is a web shell based on China Chopper for servers running Microsoft IIS. First reported in December 2019, it has been used in malicious campaigns by GALLIUM against telecommunication providers.

S0520

BLINDINGCAN

BLINDINGCAN is a remote access Trojan that has been used by the North Korean government since at least early 2020 in cyber operations against defense, engineering, and government organizations in Western Europe and the US.

S0521

BloodHound

BloodHound is an Active Directory (AD) reconnaissance tool that can reveal hidden relationships and identify attack paths within an AD environment.

S0657

BLUELIGHT

BLUELIGHT is a remote access Trojan used by APT37 that was first observed in early 2021.

S1184

BOLDMOVE

BOLDMOVE is a type of backdoor malware written in C linked to People’s Republic of China operations from 2022 through 2023. BOLDMOVE includes both Windows and Linux variants, with some Linux variants specifically designed for FortiGate Firewall devices. BOLDMOVE is linked to zero-day exploitation of CVE-2022-42475 in FortiOSS SSL-VPNs. The record for BOLDMOVE only covers known Linux variants.

S0486

Bonadan

Bonadan is a malicious version of OpenSSH which acts as a custom backdoor. Bonadan has been active since at least 2018 and combines a new cryptocurrency-mining module with the same credential-stealing module used by the Onderon family of backdoors.

S0360

BONDUPDATER

BONDUPDATER is a PowerShell backdoor used by OilRig. It was first observed in November 2017 during targeting of a Middle Eastern government organization, and an updated version was observed in August 2018 being used to target a government organization with spearphishing emails.

S1226

BOOKWORM

BOOKWORM is a modular trojan known to be leveraged by Mustang Panda and was first observed utilized in 2015. BOOKWORM was later updated in late 2021 and the fall of 2022 to launch shellcode represented as UUID parameters.

S0635

BoomBox

BoomBox is a downloader responsible for executing next stage components that has been used by APT29 since at least 2021.

S0415

BOOSTWRITE

BOOSTWRITE is a loader crafted to be launched via abuse of the DLL search order of applications used by FIN7.

S0114

BOOTRASH

BOOTRASH is a Bootkit that targets Windows operating systems. It has been used by threat actors that target the financial sector.

S1079

BOULDSPY

BOULDSPY is an Android malware, detected in early 2023, with surveillance and remote-control capabilities. Analysis of exfiltrated C2 data suggests that BOULDSPY primarily targeted minority groups in Iran.

S0651

BoxCaon

BoxCaon is a Windows backdoor that was used by IndigoZebra in a 2021 spearphishing campaign against Afghan government officials. BoxCaon's name stems from similarities shared with the malware family xCaon.

S1161

BPFDoor

JustForFun, Backdoor.Linux.BPFDOOR, Backdoor.Solaris.BPFDOOR.ZAJE

BPFDoor is a Linux based passive long-term backdoor used by China-based threat actors. First seen in 2021, BPFDoor is named after its usage of Berkley Packet Filter (BPF) to execute single task instructions. BPFDoor supports multiple protocols for communicating with a C2 including TCP, UDP, and ICMP and can start local or reverse shells that bypass firewalls using iptables.

S0293

BrainTest

BrainTest is a family of Android malware.

S1094

BRATA

BRATA (Brazilian Remote Access Tool, Android), is an evolving Android malware strain, detected in late 2018 and again in late 2021. Originating in Brazil, BRATA was later also found in the UK, Poland, Italy, Spain, and USA, where it is believed to have targeted financial institutions such as banks. There are currently three known variants of BRATA.

S0252

Brave Prince

Brave Prince is a Korean-language implant that was first observed in the wild in December 2017. It contains similar code and behavior to Gold Dragon, and was seen along with Gold Dragon and RunningRAT in operations surrounding the 2018 Pyeongchang Winter Olympics.

S0432

Bread

Joker

Bread was a large-scale billing fraud malware family known for employing many different cloaking and obfuscation techniques in an attempt to continuously evade Google Play Store’s malware detection. 1,700 unique Bread apps were detected and removed from the Google Play Store before being downloaded by users.

S0204

Briba

Briba is a trojan used by Elderwood to open a backdoor and download files on to compromised hosts.

S9015

BRICKSTORM

BRICKSTORM is a cross-platform backdoor with variants written in Go and Rust that facilitates command and control, the ingress transfer of other malware, and the exfiltration of data. BRICKSTORM has also been created from a .NET application using ahead-of-time (AOT) compilation to blend in within victim environments. BRICKSTORM was first observed in April 2024. BRICKSTORM has previously been leveraged by People's Republic of China (PRC) state-nexus actors identified as UNC6201, UNC5221, WARP PANDA, PunyToad, and SYLVANITE.

S9011

BRUSHFIRE

BRUSHFIRE is a passive backdoor written in C that executes in-memory within an existing process. First reported in March 2025, BRUSHFIRE has been observed in activity attributed to People's Republic of China (PRC) state-affiliated threat actors, including UNC5221 and SYLVANITE.

S1063

Brute Ratel C4

BRc4

Brute Ratel C4 is a commercial red-teaming and adversarial attack simulation tool that first appeared in December 2020. Brute Ratel C4 was specifically designed to avoid detection by endpoint detection and response (EDR) and antivirus (AV) capabilities, and deploys agents called badgers to enable arbitrary command execution for lateral movement, privilege escalation, and persistence. In September 2022, a cracked version of Brute Ratel C4 was leaked in the cybercriminal underground, leading to its use by threat actors.

S0014

BS2005

BS2005 is malware that was used by Ke3chang in spearphishing campaigns since at least 2011.

S0043

BUBBLEWRAP

Backdoor.APT.FakeWinHTTPHelper

BUBBLEWRAP is a full-featured, second-stage backdoor used by the admin@338 group. It is set to run when the system boots and includes functionality to check, upload, and register plug-ins that can further enhance its capabilities.

S0471

build_downer

build_downer is a downloader that has been used by BRONZE BUTLER since at least 2019.

S1039

Bumblebee

Bumblebee is a custom loader written in C++ that has been used by multiple threat actors, including possible initial access brokers, to download and execute additional payloads since at least March 2022. Bumblebee has been linked to ransomware operations including Conti, Quantum, and Mountlocker and derived its name from the appearance of "bumblebee" in the user-agent.

S0482

Bundlore

OSX.Bundlore

Bundlore is adware written for macOS that has been in use since at least 2015. Though categorized as adware, Bundlore has many features associated with more traditional backdoors.

S1118

BUSHWALK

BUSHWALK is a web shell written in Perl that was inserted into the legitimate querymanifest.cgi file on compromised Ivanti Connect Secure VPNs during Cutting Edge.

S0655

BusyGasper

BusyGasper is Android spyware that has been in use since May 2016. There have been less than 10 victims, all who appear to be located in Russia, that were all infected via physical access to the device.

S0119

Cachedump

Cachedump is a publicly-available tool that program extracts cached password hashes from a system’s registry.

S0693

CaddyWiper

CaddyWiper is a destructive data wiper that has been used in attacks against organizations in Ukraine since at least March 2022.

S0454

Cadelspy

Cadelspy is a backdoor that has been used by APT39.

S0025

CALENDAR

CALENDAR is malware used by APT1 that mimics legitimate Gmail Calendar traffic.

S0274

Calisto

Calisto is a macOS Trojan that opens a backdoor on the compromised machine. Calisto is believed to have first been developed in 2016.

S0077

CallMe

CallMe is a Trojan designed to run on Apple OSX. It is based on a publicly available tool called Tiny SHell.

S9016

Caminho

VMDetectLoader

Caminho is a downloader that has been used by threat actors since at least 2025 to deliver various strains of malware such as XWorm.

S0351

Cannon

Cannon is a Trojan with variants written in C# and Delphi. It was first observed in April 2018.

S1237

CANONSTAGER

CANONSTAGER is a loader known to be leveraged by Mustang Panda and was first observed utilized in 2025. Mustang Panda utilizes DLL side-loading to execute within the victim environment prior to delivering a follow-on malicious encrypted payload. CANONSTAGER leverages Thread Local Storage (TLS) and Native Windows APIs within the victim environment to elude detections. CANONSTAGER also hides its code utilizing window procedures and message queues.

S0030

Carbanak

Anunak

Carbanak is a full-featured, remote backdoor used by a group of the same name (Carbanak). It is intended for espionage, data exfiltration, and providing remote access to infected machines.

S0484

Carberp

Carberp is a credential and information stealing malware that has been active since at least 2009. Carberp's source code was leaked online in 2013, and subsequently used as the foundation for the Carbanak backdoor.

S0335

Carbon

Carbon is a sophisticated, second-stage backdoor and framework that can be used to steal sensitive information from victims. Carbon has been selectively used by Turla to target government and foreign affairs-related organizations in Central Asia.

S0529

CarbonSteal

CarbonSteal is one of a family of four surveillanceware tools that share a common C2 infrastructure. CarbonSteal primarily deals with audio surveillance.

S0348

Cardinal RAT

Cardinal RAT is a potentially low volume remote access trojan (RAT) observed since December 2015. Cardinal RAT is notable for its unique utilization of uncompiled C# source code and the Microsoft Windows built-in csc.exe compiler.

S0465

CARROTBALL

CARROTBALL is an FTP downloader utility that has been in use since at least 2019. CARROTBALL has been used as a downloader to install SYSCON.

S0462

CARROTBAT

CARROTBAT is a customized dropper that has been in use since at least 2017. CARROTBAT has been used to install SYSCON and has infrastructure overlap with KONNI.

S1224

CASTLETAP

CASTLETAP is an ICMP port knocking backdoor that has been installed on compromised FortiGate firewalls by UNC3886.

S0261

Catchamas

Catchamas is a Windows Trojan that steals information from compromised systems.

S0572

Caterpillar WebShell

Caterpillar WebShell is a self-developed Web Shell tool created by the group Volatile Cedar.

S0222

CCBkdr

CCBkdr is malware that was injected into a signed version of CCleaner and distributed from CCleaner's distribution website.

S1043

ccf32

ccf32 is data collection malware that has been used since at least February 2019, most notably during the FunnyDream campaign; there is also a similar x64 version.

S1204

cd00r

cd00r is an open-source backdoor for UNIX and UNIX-variant operating systems that was orginally released in 2000. cd00r source code is primarily based on a packet-capturing program as it utilizes a sniffer to listen for specific sequences of network traffic or "secret knock" before executing the attacker's code.

S0480

Cerberus

Cerberus is a banking trojan whose usage can be rented on underground forums and marketplaces. Prior to being available to rent, the authors of Cerberus claim was used in private operations for two years.

S0160

certutil

certutil.exe

certutil is a command-line utility that can be used to obtain certificate authority information and configure Certificate Services.

S0631

Chaes

Chaes is a multistage information stealer written in several programming languages that collects login credentials, credit card numbers, and other financial information. Chaes was first observed in 2020, and appears to primarily target victims in Brazil as well as other e-commerce customers in Latin America.

S1083

Chameleon

Chameleon is an Android banking trojan that can leverage Android’s Accessibility Services to perform malicious activities. Believed to have been first active in January 2023, Chameleon has been observed targeting users in Australia and Poland by masquerading as official applications. A new variant of Chameleon has expanded its targets to include Android users in the United Kingdom and Italy.

S0220

Chaos

Chaos is Linux malware that compromises systems by brute force attacks against SSH services. Once installed, it provides a reverse shell to its controllers, triggered by unsolicited packets.

S0323

Charger

Charger is Android malware that steals steals contacts and SMS messages from the user's device. It can also lock the device and demand ransom payment if it receives admin permissions.

S0674

CharmPower

CharmPower is a PowerShell-based, modular backdoor that has been used by Magic Hound since at least 2022.

S0144

ChChes

Scorpion, HAYMAKER

ChChes is a Trojan that appears to be used exclusively by menuPass. It was used to target Japanese organizations in 2016. Its lack of persistence methods suggests it may be intended as a first-stage tool.

S1096

Cheerscrypt

Cheerscrypt is a ransomware that was developed by Cinnamon Tempest and has been used in attacks against ESXi and Windows environments since at least 2022. Cheerscrypt was derived from the leaked Babuk source code and has infrastructure overlaps with deployments of Night Sky ransomware, which was also derived from Babuk.

S0555

CHEMISTGAMES

CHEMISTGAMES is a modular backdoor that has been deployed by Sandworm Team.

S0107

Cherry Picker

Cherry Picker is a point of sale (PoS) memory scraper.

S1225

CherryBlos

CherryBlos is an Android malware that steals credentials and redirects cryptocurrency to adversary-controlled wallets. CherryBlos was labelled Robot 999 in its first appearance in April 2023; since then, various aliases have been used, including GPTalk, Happy Miner, and SynthNet. The threat actors behind CherryBlos uploaded the malware to different Google Play regions, such as Malaysia, Vietnam, Indonesia, Philippines, Uganda, and Mexico.

S1149

CHIMNEYSWEEP

CHIMNEYSWEEP is a backdoor malware that was deployed during HomeLand Justice along with ROADSWEEP ransomware, and has been used to target Farsi and Arabic speakers since at least 2012.

S0020

China Chopper

China Chopper is a Web Shell hosted on Web servers to provide access back into an enterprise network that does not rely on an infected system calling back to a remote command and control server. It has been used by several threat groups.

S1041

Chinoxy

Chinoxy is a backdoor that has been used since at least November 2018, during the FunnyDream campaign, to gain persistence and drop additional payloads. According to security researchers, Chinoxy has been used by Chinese-speaking threat actors.

S0023

CHOPSTICK

Backdoor.SofacyX, SPLM, Xagent, X-Agent, webhp

CHOPSTICK is a malware family of modular backdoors used by APT28. It has been used since at least 2012 and is usually dropped on victims as second-stage malware, though it has been used as first-stage malware in several cases. It has both Windows and Linux variants. It is tracked separately from the X-Agent for Android.

S0667

Chrommme

Chrommme is a backdoor tool written using the Microsoft Foundation Class (MFC) framework that was first reported in June 2021; security researchers noted infrastructure overlaps with Gelsemium malware.

S1205

cipher.exe

cipher.exe is a native Microsoft utility that manages encryption of directories and files on NTFS (New Technology File System) partitions by using the Encrypting File System (EFS).

S0602

Circles

Circles reportedly takes advantage of Signaling System 7 (SS7) weaknesses, the protocol suite used to route phone calls, to both track the location of mobile devices and intercept voice calls and SMS messages. It can be connected to a telecommunications company’s infrastructure or purchased as a cloud service. Circles has reportedly been linked to the NSO Group.

S1236

CLAIMLOADER

CLAIMLOADER is a malware variant that frequently accompanies legitimate executables that are used for DLL side-loading known to be leveraged by Mustang Panda and was first observed utilized in 2021.

S0660

Clambling

Clambling is a modular backdoor written in C++ that has been used by Threat Group-3390 since at least 2017.

S0611

Clop

Clop is a ransomware family that was first observed in February 2019 and has been used against retail, transportation and logistics, education, manufacturing, engineering, automotive, energy, financial, aerospace, telecommunications, professional and legal services, healthcare, and high tech industries. Clop is a variant of the CryptoMix ransomware.

S0054

CloudDuke

MiniDionis, CloudLook

CloudDuke is malware that was used by APT29 in 2015.

S0106

cmd

cmd.exe

cmd is the Windows command-line interpreter that can be used to interact with systems and execute other processes and utilities.

Cmd.exe contains native functionality to perform many operations to interact with the system, including listing files in a directory (e.g., `dir` ), deleting files (e.g., `del` ), and copying files (e.g., `copy` ).

S1105

COATHANGER

COATHANGER is a remote access tool (RAT) targeting FortiGate networking appliances. First used in 2023 in targeted intrusions against military and government entities in the Netherlands along with other victims, COATHANGER was disclosed in early 2024, with a high confidence assessment linking this malware to a state-sponsored entity in the People's Republic of China. COATHANGER is delivered after gaining access to a FortiGate device, with in-the-wild observations linked to exploitation of CVE-2022-42475. The name COATHANGER is based on a unique string in the malware used to encrypt configuration files on disk: `"She took his coat and hung it up"`.

S0154

Cobalt Strike

Cobalt Strike is a commercial, full-featured, remote access tool that bills itself as "adversary simulation software designed to execute targeted attacks and emulate the post-exploitation actions of advanced threat actors". Cobalt Strike’s interactive post-exploit capabilities cover the full range of ATT&CK tactics, all executed within a single, integrated system.

In addition to its own capabilities, Cobalt Strike leverages the capabilities of other well-known tools such as Metasploit and Mimikatz.

S0338

Cobian RAT

Cobian RAT is a backdoor, remote access tool that has been observed since 2016.

S0369

CoinTicker

CoinTicker is a malicious application that poses as a cryptocurrency price ticker and installs components of the open source backdoors EvilOSX and EggShell.

S0244

Comnie

Comnie is a remote backdoor which has been used in attacks in East Asia.

S0126

ComRAT

ComRAT is a second stage implant suspected of being a descendant of Agent.btz and used by Turla. The first version of ComRAT was identified in 2007, but the tool has undergone substantial development for many years since.

S0426

Concipit1248

Corona Updates

Concipit1248 is iOS spyware that was discovered using the same name as the developer of the Android spyware Corona Updates. Further investigation revealed that the two pieces of software contained the same C2 URL and similar functionality.

S0608

Conficker

Kido, Downadup

Conficker is a computer worm first detected in October 2008 that targeted Microsoft Windows using the MS08-067 Windows vulnerability to spread. In 2016, a variant of Conficker made its way on computers and removable disk drives belonging to a nuclear power plant.

S0591

ConnectWise

ScreenConnect

ConnectWise is a legitimate remote administration tool that has been used since at least 2016 by threat actors including MuddyWater and GOLD SOUTHFIELD to connect to and conduct lateral movement in target environments.

S0575

Conti

Conti is a Ransomware-as-a-Service (RaaS) that was first observed in December 2019. Conti has been deployed via TrickBot and used against major corporations and government agencies, particularly those in North America. As with other ransomware families, actors using Conti steal sensitive files and information from compromised networks, and threaten to publish this data unless the ransom is paid.

S0492

CookieMiner

CookieMiner is mac-based malware that targets information associated with cryptocurrency exchanges as well as enabling cryptocurrency mining on the victim system itself. It was first discovered in the wild in 2019.

S0212

CORALDECK

CORALDECK is an exfiltration tool used by APT37.

S0137

CORESHELL

Sofacy, SOURFACE

CORESHELL is a downloader used by APT28. The older versions of this malware are known as SOURFACE and newer versions as CORESHELL.

S1235

CorKLOG

CorKLOG is a keylogger known to be leveraged by Mustang Panda and was first observed utilized in 2024. CorKLOG is delivered through a RAR archive (e.g., src.rar), which contains two files: an executable (lcommute.exe) and the CorKLOG DLL (mscorsvc.dll). CorKLOG has established persistence on the system by creating services or with scheduled tasks.

S0425

Corona Updates

Wabi Music, Concipit1248

Corona Updates is Android spyware that took advantage of the Coronavirus pandemic. The campaign distributing this spyware is tracked as Project Spy. Multiple variants of this spyware have been discovered to have been hosted on the Google Play Store.

S0050

CosmicDuke

TinyBaron, BotgenStudios, NemesisGemina

CosmicDuke is malware that was used by APT29 from 2010 to 2015.

S0614

CostaBricks

CostaBricks is a loader that was used to deploy 32-bit backdoors in the CostaRicto campaign.

S1155

Covenant

Covenant is a multi-platform command and control framework written in .NET. While designed for penetration testing and security research, the tool has also been used by threat actors such as HAFNIUM during operations. Covenant functions through a central listener managing multiple deployed "Grunts" that communicate back to the controller.

S0046

CozyCar

CozyDuke, CozyBear, Cozer, EuroAPT

CozyCar is malware that was used by APT29 from 2010 to 2015. It is a modular malware platform, and its backdoor component can be instructed to download and execute a variety of modules with different functionality.

S0488

CrackMapExec

CrackMapExec, or CME, is a post-exploitation tool developed in Python and designed for penetration testing against networks. CrackMapExec collects Active Directory information to conduct lateral movement through targeted networks.

S1023

CreepyDrive

CreepyDrive is a custom implant has been used by POLONIUM since at least early 2022 for C2 with and exfiltration to actor-controlled OneDrive accounts.

POLONIUM has used a similar implant called CreepyBox that relies on actor-controlled DropBox accounts.

S1024

CreepySnail

CreepySnail is a custom PowerShell implant that has been used by POLONIUM since at least 2022.

S0115

Crimson

MSIL/Crimson

Crimson is a remote access Trojan that has been used by Transparent Tribe since at least 2016.

S9004

Crocodilus

Crocodilus is an Android banking Trojan that was discovered in March 2025. Crocodilus targeted users worldwide, including Turkey, Poland, Argentina, Brazil, Spain, the United States, Indonesia and India. Crocodilus has been customized based on the target location. For example, Crocodilus mimicked major Turkish and Spanish banks for users in Turkey and Spain, while users in Poland saw Facebook advertisements that promoted Crocodilus to claim bonus points.

S0235

CrossRAT

CrossRAT is a cross platform RAT.

S0538

Crutch

Crutch is a backdoor designed for document theft that has been used by Turla since at least 2015.

S0498

Cryptoistic

Cryptoistic is a backdoor, written in Swift, that has been used by Lazarus Group.

S0527

CSPY Downloader

CSPY Downloader is a tool designed to evade analysis and download additional payloads used by Kimsuky.

S0625

Cuba

Cuba is a Windows-based ransomware family that has been used against financial institutions, technology, and logistics organizations in North and South America as well as Europe since at least December 2019.

S1153

Cuckoo Stealer

Cuckoo Stealer is a macOS malware with characteristics of spyware and an infostealer that has been in use since at least 2024. Cuckoo Stealer is a universal Mach-O binary that can run on Intel or ARM-based Macs and has been spread through trojanized versions of various potentially unwanted programs or PUP's such as converters, cleaners, and uninstallers.

S0687

Cyclops Blink

Cyclops Blink is a modular malware that has been used in widespread campaigns by Sandworm Team since at least 2019 to target Small/Home Office (SOHO) network devices, including WatchGuard and Asus. Cyclops Blink is assessed to be a replacement for VPNFilter, a similar platform targeting network devices.

S0497

Dacls

Dacls is a multi-platform remote access tool used by Lazarus Group since at least December 2019.

S1014

DanBot

DanBot is a first-stage remote access Trojan written in C# that has been used by HEXANE since at least 2018.

S0334

DarkComet

DarkKomet, Fynloski, Krademok, FYNLOS

DarkComet is a Windows remote administration tool and backdoor.

S1111

DarkGate

DarkGate first emerged in 2018 and has evolved into an initial access and data gathering tool associated with various criminal cyber operations. Written in Delphi and named "DarkGate" by its author, DarkGate is associated with credential theft, cryptomining, cryptotheft, and pre-ransomware actions. DarkGate use increased significantly starting in 2022 and is under active development by its author, who provides it as a Malware-as-a-Service offering.

S1066

DarkTortilla

DarkTortilla is a highly configurable .NET-based crypter that has been possibly active since at least August 2015. DarkTortilla has been used to deliver popular information stealers, RATs, and payloads such as Agent Tesla, AsyncRat, NanoCore, RedLine, Cobalt Strike, and Metasploit.

S0673

DarkWatchman

DarkWatchman is a lightweight JavaScript-based remote access tool (RAT) that avoids file operations; it was first observed in November 2021.

S0187

Daserf

Muirim, Nioupale

Daserf is a backdoor that has been used to spy on and steal from Japanese, South Korean, Russian, Singaporean, and Chinese victims. Researchers have identified versions written in both Visual C and Delphi.

S1243

DCHSpy

DCHSpy is an Android spyware likely used by MuddyWater. DCHSpy uses political decoys and masquerades as legitimate applications, such as VPNs and banking applications, to trick victims into downloading the malware. Once downloaded, DCHSpy collects information from the device and exfiltrates the data to the command and control (C2) server.

S9017

DCRAT
