---
title: "Darwin (operating system)"
source: https://en.wikipedia.org/wiki/Darwin_(operating_system)
domain: macos-darwin
license: CC-BY-SA-4.0
tags: macos internals, darwin operating system, xnu kernel, grand central dispatch
fetched: 2026-07-02
---

# Darwin (operating system)

**Darwin** is the core Unix-like operating system of macOS, iOS, watchOS, tvOS, iPadOS, audioOS, visionOS, and bridgeOS. It previously existed as an independent open-source operating system, first released by Apple in 2000. It is composed of code derived from NeXTSTEP, FreeBSD and other BSD operating systems, Mach, and other free software projects' code, as well as code developed by Apple. Darwin's unofficial mascot is Hexley the Platypus.

Darwin is mostly POSIX-compatible, but has never, by itself, been certified as compatible with any version of POSIX. Starting with Leopard, macOS has been certified as compatible with the Single UNIX Specification version 3 (SUSv3).

## History

The heritage of Darwin began with Unix derivatives supplemented by aspects of NeXT's NeXTSTEP operating system (later, since version 4.0, known as OPENSTEP), first released in 1989. After Apple bought NeXT in 1996, it announced it would base its next operating system on OPENSTEP. This was developed into Rhapsody in 1997, Mac OS X Server 1.0 in 1999, Mac OS X Public Beta in 2000, and Mac OS X 10.0 in 2001.

In 1999, Apple announced it would release the source code for the Mach 2.5 microkernel, BSD Unix 4.4 OS, and the Apache Web server components of Mac OS X Server. At the time, interim CEO Steve Jobs alluded to British naturalist Charles Darwin by announcing "because it's about evolution". In 2000, the core operating system components of Mac OS X were released as open-source software under the Apple Public Source License (APSL) as Darwin; the higher-level components, such as the Cocoa and Carbon frameworks, remained closed-source.

Up to Darwin 8.0.1, released in April 2005, Apple released a binary installer (as an ISO image) after each major Mac OS X release that allowed one to install Darwin on PowerPC and Intel x86 systems as a standalone operating system. Minor updates were released as packages that were installed separately. Darwin is now only available as source code. As of January 2023, Apple no longer mentions Darwin by name on its Open Source website and only publishes an incomplete collection of open-source projects relating to macOS and iOS.

## Design

### Kernel

The kernel of Darwin is XNU, a hybrid kernel which uses Open Software Foundation Mach Kernel (OSFMK) 7.3 from the OSF, various elements of FreeBSD (including the process model, network stack, and virtual file system), and an object-oriented device driver API called IOKit. The hybrid kernel design provides the flexibility of a microkernel and the performance of a monolithic kernel.

### Hardware and software support

The last bootable full release of Darwin supported 32-bit and 64-bit Apple PowerPC systems and 32-bit Intel PCs.

Darwin currently includes support for the 64-bit x86-64 variant of the Intel x86 processors used in Intel-based Macs and the 64-bit ARM processors used in the iPhone 5S and later, the 6th generation iPod Touch, the 5th generation iPad and later, the iPad Air family, the iPad Mini 2 and later, the iPad Pro family, the fourth generation and later Apple TVs, the HomePod family, and Macs with Apple silicon such as the 2020 Apple M1 Macs, as well as the Raspberry Pi 3B. An open-source port of the XNU kernel exists that supports Darwin on Intel and AMD x86 platforms not officially supported by Apple, though it does not appear to have been updated since 2009. An open-source port of the XNU kernel also exists for ARM platforms, though it has not been updated since 2016. Older versions supported some or all of 32-bit PowerPC, 64-bit PowerPC, 32-bit x86, and 32-bit ARM.

It supports the POSIX API by way of its BSD lineage (largely FreeBSD userland), so a large number of programs written for various other UNIX-like systems can be compiled on Darwin with no changes to the source code.

Darwin does not include many of the defining elements of macOS, such as the Carbon and Cocoa APIs or the Quartz Compositor and Aqua user interface, and thus cannot run Mac applications. It does, however, support a number of lesser-known features of macOS, such as mDNSResponder, which is the multicast DNS responder and a core component of the Bonjour networking technology, and launchd, an advanced service management framework.

## License

In July 2003, Apple released Darwin under version 2.0 of the Apple Public Source License (APSL), which the Free Software Foundation (FSF) qualifies as a free software license. The APSL is similar to AGPL, including in being incompatible with the GNU General Public License.

Previous versions of the APSL license did not meet the FSF definition of free software, although they did meet the requirements of the Open Source Definition.

## Release history

The following is a table of major Darwin releases with their dates of release and their derivative operating system releases. Note that the corresponding releases may have been released on a different date.

### Darwin 0–8 and corresponding Mac OS X releases

| Version | Date | Corresponding releases | Notes |
|---|---|---|---|
| 0.1 | March 16, 1999 | Mac OS X Server 1.0 releases | Initial release 0.1 is contrived (for sorting and identification) as this identified itself simply as Rhapsody 5.3 |
| 0.2 | April 14, 1999 | Mac OS X Server 1.0.1 |   |
| 0.3 | August 5, 1999 | Based on Rhapsody 5.5 ISO image is available on archive.org After this point the kernel changed from the NeXTSTEP/OPENSTEP/Rhapsody to the newer XNU for Mac OS X |   |
| 1.0 | April 12, 2000 |   | Developer preview 3 ISO image is available on archive.org |
| 1.1 | April 5, 2000 |   | Developer preview 4 |
| 1.2.1 | November 15, 2000 | Mac OS X Public Beta (code-named "Kodiak") |   |
| 1.3.1 | April 13, 2001 | Mac OS X v10.0 (code-named "Cheetah") | First commercial release of Darwin All releases of Cheetah (v10.0.0–4) had the same version of Darwin. |
| 1.4.1 | October 2, 2001 | Mac OS X v10.1 (code-named "Puma") | Performance improvements to "boot time, real-time threads, thread management, cache flushing, and preemption handling" Support for SMB network file system Wget replaced with cURL. |
| 5.1 | November 12, 2001 | Mac OS X v10.1.1 Change in numbering scheme to match the Mac OS X build numbering scheme |   |
| 5.5 | June 5, 2002 | Mac OS X v10.1.5 |   |
| 6.0.1 | September 23, 2002 | Mac OS X v10.2 (code-named "Jaguar") | GCC upgraded from 2 to 3.1 IPv6 and IPSec support mDNSResponder service discovery daemon (Rendezvous) Addition of CUPS, Ruby, and Python Journaling support in HFS+ (Darwin 6.2) Application profiles ("pre-heat files") for faster program launching. |
| 6.8 | October 3, 2003 | Mac OS X v10.2.8 |   |
| 7.0 | October 24, 2003 | Mac OS X Panther | Mac OS X v10.3.0 BSD layer synchronized with FreeBSD 5 Automatic file defragmentation, hot-file clustering and optional case sensitivity in HFS+ Bash instead of tcsh as default shell Read-only NTFS support (Darwin 7.9) |
| 7.9 | April 15, 2005 | Mac OS X v10.3.9 |   |
| 8.0 | April 29, 2005 | Mac OS X TigerMac OS X for Apple TV | Mac OS X v10.4.0 Download for Darwin 8.0.1 can be found here Mac OS X for Apple TV in Darwin 8.8.2 Stable kernel programming interface, finer-grained kernel locking, 64-bit BSD layer launchd service management framework Extended file attributes, access control lists Commands such as cp and mv updated to preserve extended attributes and resource forks |
| 8.11 | November 14, 2007 | Mac OS X v10.4.11 |   |

The jump in version numbers from Darwin 1.4.1 to 5.1 with the release of Mac OS X v10.1.1 was designed to tie Darwin to the Mac OS X version and build numbering system, which in turn is inherited from NeXTSTEP. In the build numbering system of macOS, every version has a unique beginning build number, which identifies what whole version of macOS it is part of. Mac OS X v10.0 had build numbers starting with 4, 10.1 had build numbers starting with 5, and so forth (earlier build numbers represented developer releases).

### Darwin 9; iPhone OS introduced

| Version | Date | Corresponding releases | Notes |
|---|---|---|---|
| 9.0 | October 26, 2007 | Mac OS X LeopardiPhone OS 1 | Mac OS X v10.5.0 iPhone OS 1 support in Darwin 9.0.0d1 Full POSIX compliance, improved hierarchical process scheduling model, dynamically allocated swap files, dynamic resource limits (for files and processes), process sandboxing, address space layout randomization, DTrace tracing framework, file system events daemon, directory hard links Apache 1.3 and PHP 4 updated to Apache 2.2 and PHP 5, read-only ZFS support. First Darwin core used for iPhone devices. |
| 9.8 | August 5, 2009 | Mac OS X v.10.5.8 |   |

### Darwin 10-11; iPhone OS rebranded to iOS

| Version | Date | Corresponding releases | Notes |
|---|---|---|---|
| 10.0 | August 28, 2009 | Mac OS X Snow LeopardiPhone OS 3 | Mac OS X v10.6.0 End of official support for PPC architecture (although several fat binaries, such as Kernel, still contain PPC images) 64-bit kernel and drivers libdispatch task parallelization framework OpenCL heterogeneous computing framework Initial support for Automatic Reference Counting Support for blocks in C Transparent file compression in HFS+. |
| 10.8 | June 23, 2011 | Mac OS X v10.6.8 |   |
| 11.0.0 | July 20, 2011 | Mac OS X LioniOS 4.3 | Mac OS X v10.7.0 XNU no longer supports PPC binaries (fat binary only for i386, x86_64). XNU requires an x86_64 processor, except for iOS which is ARM based. Improved sandboxing of applications Complete support for Automatic Reference Counting |
| 11.4.2 | October 4, 2012 | Mac OS X v10.7.5 (supplemental) |   |

### Darwin 12–15; Mac OS X rebranded into OS X

| Version | Date | Corresponding releases | Notes |
|---|---|---|---|
| 12.0.0 | February 16, 2012 | OS X Mountain Lion | OS X v10.8.0 Mac OS X was rebranded into OS X. Objective-C garbage collection was deprecated in favor of Automatic Reference Counting |
| 12.6.0 | January 27, 2015 | OS X v10.8.5 (with Security Update 2015-001) |   |
| 13.0.0 | June 11, 2013 | OS X MavericksiOS 6 | OS X v10.9.0 Virtual memory compression Timer coalescing OpenGL 4.1 and OpenCL 1.2 Server Message Block version 2 (SMB2) is now the default protocol for sharing files instead of AFP. This is to increase performance and cross-platform compatibility. IPoTB (Internet Protocol over Thunderbolt Bridge). The Open Transport API has been removed |
| 13.4.0 | September 17, 2014 | OS X v10.9.5 |   |
| 14.0.0 | September 18, 2014 | OS X YosemiteiOS 7, iOS 8watchOS 1 | OS X v10.10.0 |
| 14.5.0 | August 13, 2015 | OS X v10.10.5 |   |
| 15.0.0 | September 16, 2015 | OS X El CapitaniOS 9watchOS 2tvOS 9 | OS X v10.11.0 and iOS 9.0 System Integrity Protection. Protects certain system parts from being modified or tampered with by a process even if run by root or by a user with root privileges. sudo is configured with the "tty_tickets" flag by default, restricting the session timeout to the terminal session (such as a window or tab) in which the user authenticated the program. LibreSSL replaces OpenSSL |
| 15.6.0 | July 18, 2016 | OS X v10.11.6 and iOS 9.3.3 |   |

### Darwin 16–19; OS X rebranded into macOS

| Version | Date | Corresponding releases | Notes |
|---|---|---|---|
| 16.0.0 | September 13, 2016 | macOS SierraiOS 10watchOS 3tvOS 10bridgeOS 1 | macOS v10.12.0 and iOS 10.0.1 (initial release version) OS X was rebranded into macOS. Writing to `/Volumes` directory is now restricted to root user or any user with root privileges System Integrity Protection now covers `/Library/Application Support/com.apple.TCC` directory that contains a list of applications that are allowed to "control the computer" Objective-C garbage collector removed and replaced by Automatic Reference Counting that was introduced with Darwin v12.0 (OS X v10.8). Objective-C applications that use garbage collection will no longer work. Native support for PPTP was removed. |
| 16.5.0 | March 27, 2017 | macOS v10.12.4 and iOS 10.3 Changed filesystem from HFS+ to APFS on iOS devices. APFS is already available on macOS since 10.12.0 but can't be used on boot partition. |   |
| 16.6.0 | July 19, 2017 | macOS v10.12.6 and iOS 10.3.3 |   |
| 17.0.0 | September 19, 2017 | macOS High SierraiOS 11watchOS 4tvOS 11bridgeOS 2 | APFS replaces HFS+ as the default filesystem for boot partition in macOS on Macs with flash storage. On Macs with HDDs, the boot partition must be reformatted to use APFS. ntpd replaced by timed as a time synchronization service FTP and telnet commands are removed. Kernel extensions ("kexts") will require explicit approval by the user before being able to run. |
| 17.5.0 | March 29, 2018 | macOS 10.13.4 Support for external graphics processors using Thunderbolt 3, and removes support for external graphics processors using Thunderbolt 1 and 2. |   |
| 17.6.0 | June 1, 2018 | macOS v10.13.5 |   |
| 17.7.0 | July 9, 2018 | macOS v10.13.6 and iOS 11.4.1 |   |
| 18.0.0 | September 24, 2018 | macOS MojaveiOS 12watchOS 5tvOS 12bridgeOS 3 |   |
| 18.2.0 | October 30, 2018 | macOS v10.14.1 and iOS 12.1 Added support for the new Radeon Vega 20 GPUs in the new MacBooks |   |
| 19.0.0 | September 19, 2019 | macOS CatalinaiOS 13watchOS 6tvOS 13bridgeOS 4 |   |
| 19.2.0 | December 10, 2019 | macOS 10.15.2 and iOS 13.3 |   |
| 19.3.0 | January 28, 2020 | macOS 10.15.3 and iOS 13.3.1 System Extensions replace Kexts and runs in userspace, outside of the kernel. DriverKit replaces I/O Kit. It Introduces "Dexts" (Driver Extensions) which are built using DriverKit. Driverkit is a new SDK with all new frameworks based on IOKit, but is updated and modernized. Device Drivers run in userspace, outside of the kernel. |   |
| 19.4.0 | March 24, 2020 |   |   |
| 19.5.0 | April 30, 2020 | macOS 10.15.5 and iOS 13.5 |   |
| 19.6.0 | June 1, 2020 | macOS 10.15.6 beta 2 and iOS 13.6.0 beta 2 |   |

### Darwin 20 onwards

| Version | Date | Corresponding releases | Notes |
|---|---|---|---|
| 20.0.0 | June 22, 2020 | macOS Big SuriOS 14watchOS 7tvOS 14bridgeOS 5 | macOS 11.0 beta 1 and iOS 14.0 beta 1 |
| 20.1.0 | September 3, 2020 | macOS 11.0 and iOS 14.0 |   |
| 20.2.0 | November 12, 2020 | macOS 11.1 and iOS 14.3 |   |
| 20.3.0 | February 1, 2021 | macOS 11.2, iOS 14.4, iPadOS 14.4, watchOS 7.3 and tvOS 14.4. |   |
| 20.4.0 | April 20, 2021 | macOS 11.3, iOS 14.5, iPadOS 14.5, watchOS 7.4 and tvOS 14.5. |   |
| 20.5.0 | May 24, 2021 | macOS 11.4 and iOS 14.6 |   |
| 20.6.0 | June 2, 2021 | macOS 11.5 beta 2 and iOS 14.7 beta 2 |   |
| 21.0.0 | June 7, 2021 | macOS MontereyiOS 15watchOS 8tvOS 15bridgeOS 6 | macOS 12.0 beta 1 and iOS 15.0 beta 1 |
| 21.0.1 | October 25, 2021 | macOS 12.0 |   |
| 21.1.0 | October 25, 2021 | macOS 12.0.1 and iOS 15.0 |   |
| 21.2.0 | December 7, 2021 | macOS 12.1 and iOS 15.2 |   |
| 21.3.0 | January 26, 2022 | macOS 12.2 and iOS 15.3 |   |
| 21.4.0 | March 14, 2022 | macOS 12.3 and iOS 15.4 |   |
| 21.5.0 | June 24, 2022 | macOS 12.4 and iOS 15.5 |   |
| 21.6.0 | July 20, 2022 | macOS 12.5 and iOS 15.6 |   |
| 22.0 | June 6, 2022 | macOS VenturaiOS 16iPadOS 16watchOS 9tvOS 16bridgeOS 7 | macOS 13.0 beta 1, iOS 16.0, watchOS 9.0 and tvOS 16.0 |
| 22.1.0 | October 24, 2022 | macOS 13.0, iOS 16.1, iPadOS 16.1, watchOS 9.1 and tvOS 16.1 |   |
| 22.2.0 | December 13, 2022 | macOS 13.1, iOS 16.2, iPadOS 16.2, watchOS 9.2 and tvOS 16.2 |   |
| 22.3.0 | January 23, 2023 | macOS 13.2, iOS 16.3, iPadOS 16.3, watchOS 9.3 and tvOS 16.3 |   |
| 22.4.0 | March 27, 2023 | macOS 13.3, iOS 16.4, iPadOS 16.4, watchOS 9.4 and tvOS 16.4 |   |
| 22.5.0 | May 18, 2023 | macOS 13.4, iOS 16.5, iPadOS 16.5, watchOS 9.5 and tvOS 16.5 |   |
| 22.6.0 | July 24, 2023 | macOS 13.5, iOS 16.6, iPadOS 16.6, watchOS 9.6 and tvOS 16.6 |   |
| 23.0.0 | September 18, 2023 | macOS SonomaiOS 17iPadOS 17watchOS 10tvOS 17bridgeOS 8 | macOS 14.0, iOS 17.0, iPadOS 17.0, watchOS 10.0 and tvOS 17.0 |
| 23.1.0 | October 25, 2023 | macOS 14.1, iOS 17.1, iPadOS 17.1, watchOS 10.1 and tvOS 17.1 |   |
| 23.2.0 | November 15, 2023 | macOS 14.2, iOS 17.2, iPadOS 17.2, watchOS 10.2 and tvOS 17.2 |   |
| 23.3.0 | January 22, 2024 | macOS 14.3, iOS 17.3, iPadOS 17.3, watchOS 10.3 and tvOS 17.3 |   |
| 23.4.0 | March 5, 2024 | macOS 14.4, iOS 17.4, iPadOS 17.4, watchOS 10.4 and tvOS 17.4 |   |
| 23.5.0 | May 13, 2024 | macOS 14.5, iOS 17.5, iPadOS 17.5, watchOS 10.5 and tvOS 17.5 |   |
| 23.6.0 | July 5, 2024 | macOS 14.6 |   |
| 24.0.0 | September 16, 2024 | macOS SequoiaiOS 18iPadOS 18watchOS 11tvOS 18bridgeOS 9 | macOS 15.0, iOS 18.0, iPadOS 18.0, watchOS 11.0, and tvOS 18.0 |
| 25.0.0 | September 15, 2025 | macOS TahoeiOS 26iPadOS 26watchOS 26tvOS 26bridgeOS 10 | macOS, iOS, iPadOS, watchOS, and tvOS 26.0 |
| 27.0.0 | June 8, 2026 | macOS Golden GateiOS 27iPadOS 27watchOS 27tvOS 27 | macOS, iOS, iPadOS, watchOS, and tvOS 27.0 |

*Note: the tables above contain the release dates of the corresponding OS releases. Build dates for Darwin versions are not publicly available; the commands below only give the build date for the XNU kernel.*

The command uname -r in Terminal will show the Darwin version number ("20.3.0"), and the command uname -v will show the XNU build version string, which includes the Darwin version number. The command sw_vers will show the corresponding ProductName ("macOS"), the ProductVersion number ("11.2.3") and the BuildVersion string ("20D91").

## Derived projects

Due to the free software nature of Darwin, there have been projects that aim to modify the operating system or take Darwin’s parts for their own purpose.

Among these, DarwinBSD, OpenDarwin, and PureDarwin can be termed "alternative Darwin distributions" in a sense analogous to Linux distributions.

### OpenDarwin

OpenDarwin was a project to develop a community-led operating system based on the Darwin system. It was founded in April 2002 by Apple and Internet Systems Consortium. Its goal was to increase collaboration between Apple developers and the free software community. Apple benefited from the project because improvements to OpenDarwin would be incorporated into Darwin releases; and the free/open-source community benefited from being given complete control over its own operating system, which could then be used in free software distributions such as GNU-Darwin.

On July 25, 2006, the OpenDarwin team announced that the project was shutting down, as they felt OpenDarwin had "become a mere hosting facility for Mac OS X related projects", and that the efforts to create a standalone Darwin operating system had failed. They also state: "Availability of sources, interaction with Apple representatives, difficulty building and tracking sources, and a lack of interest from the community have all contributed to this." The last stable release was version 7.2.1, released on July 16, 2004.

### PureDarwin

PureDarwin is a project to create a bootable operating system image from Apple's released source code for Darwin. Since the halt of OpenDarwin and the release of bootable images since Darwin 8.x, it has been increasingly difficult to create a full operating system as many components became closed source. In 2015 the project created a preview release based on Darwin 9 with an X11 GUI, followed by a command-line only 17.4 Beta based on Darwin 17 in 2019.

### ravynOS

ravynOS is a project to develop a Free and Open Source operating system that aims to be both source-compatible and eventually binary-compatible with Apple's macOS operating system. Although originally building upon a FreeBSD and NextBSD foundation, the lead dev, Zoë Knox, announced on October 28, 2025, that the operating system would be moving to a Darwin base. Since this change, work has been done on getting the legacy Darwin sources to build, as well as modernizing the build system and parts of the operating system.

### Other derived projects

"Darwin distributions" (see also the other package managers below):

- GNU-Darwin was a project that ports packages of free software to Darwin. They package OS images in a way similar to a Linux distribution.
- DarwinBSD Project was a Darwin distribution using NetBSD's pkgsrc package management.

Other types of derivatives:

- The Darbat project was an experimental port of Darwin to the L4 microkernel family. It aims to be binary compatible with existing Darwin binaries.
- The Darling project is a compatibility layer for running macOS binaries on Linux systems. It uses some Darwin source code.

### Projects intended to work with Darwin

The following are not Darwin derivatives, at least not beyond the extent that any program written for an operating system is partly derived from its application programming interface and other constraints.

- XQuartz is a component of the X Window System that runs on macOS (Darwin). XDarwin, before the introduction of Apple's X11.app.
- WebKit is a browser engine primarily used in Apple's Safari web browser, as well as all web browsers on iOS and iPadOS.
- MacPorts (formerly DarwinPorts), Fink, and Homebrew are projects to port UNIX programs to the Darwin operating system and provide package management. In addition, several standard UNIX package managers—such as RPM, pkgsrc, and Portage—have Darwin ports. Some of these operate in their own namespace so as not to interfere with the base system.
- The Darwine project was a port of Wine that allows one to run Microsoft Windows software on Darwin.
- SEDarwin was a port of TrustedBSD mandatory access control framework and portions of the SELinux framework to Darwin. It was incorporated into Mac OS X 10.5.
- There are various projects that focus on driver support: e.g., wireless drivers, wired NIC drivers modem drivers, card readers, and the ext2 and ext3 file systems.

### Neither substantially based on Darwin nor mainly intended to work on it

The following projects re-implements parts of macOS API that are above the level of Darwin.

- GNUstep is a free software implementation of the Cocoa (formerly OpenStep) Objective-C frameworks, widget toolkit, and application development tools for Unix-like operating systems.
  - Window Maker, a window manager designed to emulate the NeXT GUI as part of the wider GNUstep project.
