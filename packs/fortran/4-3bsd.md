---
title: "History of the Berkeley Software Distribution"
source: https://en.wikipedia.org/wiki/4.3BSD
domain: fortran
license: CC-BY-SA-4.0
tags: fortran
fetched: 2026-07-03
---

# History of the Berkeley Software Distribution

(Redirected from

4.3BSD

)

The **history of the Berkeley Software Distribution** began in the 1970s when University of California, Berkeley received a copy of Unix. Professors and students at the university began adding software to the operating system and released it as BSD to select universities. Since it contained proprietary Unix code, it originally had to be distributed subject to AT&T licenses. The bundled software from AT&T was then rewritten and released as free software under the BSD license. However, this resulted in a lawsuit with Unix System Laboratories, the AT&T subsidiary responsible for Unix. Eventually, in the 1990s, the final versions of BSD were publicly released without any proprietary licenses, which led to many descendants of the operating system that are still maintained today.

## 1BSD (PDP-11)

The earliest distributions of Unix from Bell Labs in the 1970s included the source code to the operating system, allowing researchers at universities to modify and extend Unix. The operating system arrived at Berkeley in 1974, at the request of computer science professor Bob Fabry who had been on the program committee for the Symposium on Operating Systems Principles where Unix was first presented. A PDP-11/45 was bought to run the system, but for budgetary reasons, this machine was shared with the mathematics and statistics groups at Berkeley, who used RSTS, so that Unix only ran on the machine eight hours per day (sometimes during the day, sometimes during the night). A larger PDP-11/70 was installed at Berkeley the following year, using money from the Ingres database project.

Also in 1975, Ken Thompson took a sabbatical from Bell Labs and came to Berkeley as a visiting professor. He helped to install Version 6 Unix and started working on a Pascal implementation for the system. Graduate students Chuck Haley and Bill Joy improved Thompson's Pascal and implemented an improved text editor, ex. Other universities became interested in the software at Berkeley, and so in 1977 Joy started compiling the first Berkeley Software Distribution (1BSD), which was released on March 9, 1978. 1BSD was an add-on to Version 6 Unix rather than a complete operating system in its own right. Some thirty copies were sent out.

## 2BSD (PDP-11)

The Second Berkeley Software Distribution (2BSD), released in May 1979, included updated versions of the 1BSD software as well as two new programs by Joy that persist on Unix systems to this day: the vi text editor (a visual version of ex) and the C shell. Some 75 copies of 2BSD were sent out by Bill Joy. A further feature was a networking package called Berknet, developed by Eric Schmidt as part of his master's thesis work, that could connect up to twenty-six computers and provided email and file transfer.

After 3BSD (see below) had come out for the VAX line of computers, new releases of 2BSD for the PDP-11 were still issued and distributed through USENIX; for example, 1982's 2.8.1BSD included a collection of fixes for performance problems in Version 7 Unix, and later releases contained ports of changes from the VAX-based releases of BSD back to the PDP-11 architecture. 2.9BSD from 1983 included code from 4.1cBSD, and was the first release that was a full OS (a modified V7 Unix) rather than a set of applications and patches.

The most recent release, **2.11BSD**, was first issued in 1991. Unlike the previous releases, it required split instruction/data space, to accommodate the ever-increasing size of its utility programs. In the 21st century, maintenance updates from volunteers continued: patch ***#499*** was released on January 2, 2026.

## 3BSD

A DEC VAX computer was installed at Berkeley in 1978. The port of Version 7 Unix to the VAX architecture, UNIX/32V, did not take advantage of the VAX's virtual memory capabilities, which were necessary to run large programs such as Franz Lisp. The kernel of 32V was largely rewritten by Berkeley graduate student Özalp Babaoğlu to include a virtual memory implementation, and a complete operating system including the new kernel, ports of the 2BSD utilities to the VAX, and the utilities from 32V was released as 3BSD at the end of 1979. 3BSD was also alternatively called Virtual VAX/UNIX or VMUNIX (for Virtual Memory Unix), and BSD kernel images were normally called `/vmunix` until 4.4BSD.

The success of 3BSD was a major factor in the Defense Advanced Research Projects Agency's (DARPA) decision to fund Berkeley's Computer Systems Research Group (CSRG), which would develop a standard Unix platform for future DARPA research in the VLSI Project.

## 4BSD

4BSD (November 1980) offered a number of enhancements over 3BSD, notably job control in the previously released csh, delivermail (the ancestor of sendmail), "reliable" signals, and the Curses programming library. In a 1985 review of BSD releases, John Quarterman *et al.*, wrote:

> 4BSD was the operating system of choice for VAXs from the beginning until the release of System III (1979–1982) [...] Most organizations would buy a 32V license and order 4BSD from Berkeley without ever bothering to get a 32V tape. Many installations inside the Bell System ran 4.1BSD (many still do, and many others run 4.2BSD).

## 4.1BSD

4.1BSD (June 1981) was a response to criticisms of BSD's performance relative to the dominant VAX operating system, VMS. The 4.1BSD kernel was systematically tuned up by Bill Joy until it could perform as well as VMS on several benchmarks. The release would have been called *5BSD*, but after objections from AT&T the name was changed; AT&T feared confusion with AT&T's UNIX System V. Several tapes have turned up, all with a label that says 4.1BSD, yet differences between the tapes are present. The software development that would lead from 4.1BSD to 4.2BSD was funded from sources including ARPA, Order Number 4031, Contract N00039-82-C-0235 which was in effect at least from November 15, 1981 through September 30, 1983.

## 4.2BSD

4.2BSD (August 1983) would take over two years to implement and contained several major overhauls. Before its official release came three intermediate versions: **4.1a** from April 1982 incorporated a modified version of BBN's preliminary TCP/IP implementation; **4.1b** from June 1982 included the new Berkeley Fast File System, implemented by Marshall Kirk McKusick; and **4.1c** in April 1983 was an interim release during the last few months of 4.2BSD's development. Back at Bell Labs, 4.1cBSD became the basis of the 8th Edition of Research Unix, and a commercially supported version was available from mt Xinu.

To guide the design of 4.2BSD, Duane Adams of DARPA formed a "steering committee" consisting of Bob Fabry, Bill Joy and Sam Leffler from Berkeley, Alan Nemeth and Rob Gurwitz from BBN, Dennis Ritchie from Bell Labs, Keith Lantz from Stanford, Rick Rashid from Carnegie Mellon, Bert Halstead from MIT, Dan Lynch from ISI, and Gerald J. Popek of UCLA. The committee met from April 1981 to June 1983.

Apart from the Fast File System, several features from outside contributors were accepted, including disk quotas. Sun Microsystems provided testing on its Motorola 68000 machines prior to release, improving portability of the system. Sun hardware support is plainly visible in the 4.1c BSD artifacts in the CSRG ISO.

The official 4.2BSD release came in August 1983. It was notable as the first version released after the 1982 departure of Bill Joy to co-found Sun Microsystems; Mike Karels and Marshall Kirk McKusick took on leadership roles within the project from that point forward. On a lighter note, it also marked the debut of BSD's daemon mascot in a drawing by John Lasseter that appeared on the cover of the printed manuals distributed by USENIX.

## 4.3BSD

4.3BSD was released in June 1986. Its main changes were to improve the performance of many of the new contributions of 4.2BSD that had not been as heavily tuned as the 4.1BSD code. Prior to the release, BSD's implementation of TCP/IP had diverged considerably from BBN's official implementation. After several months of testing, DARPA determined that the 4.2BSD version was superior and would remain in 4.3BSD. (See also History of the Internet.)

After 4.3BSD, it was determined that BSD would move away from the aging VAX platform. The Power 6/32 platform (codenamed "Tahoe") developed by Computer Consoles Inc. seemed promising at the time, but was abandoned by its developers shortly thereafter. Nonetheless, the **4.3BSD-Tahoe** port (June 1988) proved valuable, as it led to a separation of machine-dependent and machine-independent code in BSD which would improve the system's future portability.

Apart from portability, the CSRG worked on an implementation of the OSI network protocol stack, improvements to the kernel virtual memory system and (with Van Jacobson of LBL) new TCP/IP algorithms to accommodate the growth of the Internet.

Until then, all versions of BSD incorporated proprietary AT&T Unix code and were, therefore, subject to an AT&T software license. Source code licenses had become very expensive and several outside parties had expressed interest in a separate release of the networking code, which had been developed entirely outside AT&T and would not be subject to the licensing requirement. This led to **Networking Release 1** (**Net/1**), which was made available to non-licensees of AT&T code and was freely redistributable under the terms of the BSD license. It was released in June 1989.

**4.3BSD-Reno** came in early 1990. It was an interim release during the early development of 4.4BSD, and its use was considered a "gamble", hence the naming after the gambling center of Reno, Nevada. This release explicitly moved towards POSIX compliance. Among the new features were an NFS implementation from the University of Guelph, a status key ("Ctrl-T") and support for the HP 9000 range of computers, originating in the University of Utah's "HPBSD" port.

In August 2006, *InformationWeek* magazine rated 4.3BSD as the "Greatest Software Ever Written". They commented: "BSD 4.3 represents the single biggest theoretical undergirder of the Internet."

## Net/2 and legal troubles

After Net/1, BSD developer Keith Bostic proposed that more non-AT&T sections of the BSD system be released under the same license as Net/1. To this end, he started a project to reimplement most of the standard Unix utilities without using the AT&T code. For example, vi, which had been based on the original Unix version of ed, was rewritten as nvi (new vi). Within eighteen months, all of the AT&T utilities had been replaced, and it was determined that only a few AT&T files remained in the kernel. These files were removed, and the result was the June 1991 release of **Networking Release 2** (**Net/2**), aka Network(ing) 2, a nearly complete operating system that was freely distributable.

Net/2 was the basis for two separate ports of BSD to the Intel 80386 architecture: the free 386BSD by William Jolitz and the proprietary BSD/386 (later renamed BSD/OS) by Berkeley Software Design (BSDi). 386BSD itself was short-lived, but became the initial code base of the NetBSD and FreeBSD projects that were started shortly thereafter.

BSDi soon found itself in legal trouble with AT&T's Unix System Laboratories (USL) subsidiary, then the owners of the System V copyright and the Unix trademark. The *USL v. BSDi* lawsuit was filed in April 1992 and led to an injunction on the distribution of Net/2 until the validity of USL's copyright claims on the source could be determined.

The lawsuit slowed development of the free-software descendants of BSD for nearly two years while their legal status was in question, and as a result systems based on the Linux kernel, which did not have such legal ambiguity, gained greater support. Although not released until 1992, development of 386BSD predated that of Linux. Linus Torvalds has said that if 386BSD or the GNU kernel had been available at the time, he probably would not have created Linux.

## 4.4BSD and descendants

In August 1992, **4.4BSD-Alpha** was released, and in June 1993, **4.4BSD-Encumbered** was released only to USL licensees.

The lawsuit was settled in January 1994, largely in Berkeley's favor. Of the 18,000 files in the Berkeley distribution, only three had to be removed and 70 modified to show USL copyright notices. A further condition of the settlement was that USL would not file further lawsuits against users and distributors of the Berkeley-owned code in the upcoming 4.4BSD release. Marshall Kirk McKusick summarizes the lawsuit and its outcome:

> Code copying and theft of trade secrets was alleged. The actual infringing code was not identified for nearly two years. The lawsuit could have dragged on for much longer but for the fact that Novell bought USL from AT&T and sought a settlement. In the end, three files were removed from the 18,000 that made up the distribution, and a number of minor changes were made to other files. In addition, the University agreed to add USL copyrights to about 70 files, with the stipulation that those files continued to be freely redistributed.

In March 1994, **4.4BSD-Lite** was released that no longer required a USL source license and also contained many other changes over the original 4.4BSD-Encumbered release.

The final release from Berkeley was 1995's **4.4BSD-Lite Release 2**, after which the CSRG was dissolved and development of BSD at Berkeley ceased. Since then, several variants based directly or indirectly on 4.4BSD-Lite (such as FreeBSD, NetBSD, OpenBSD and DragonFly BSD) have been maintained.

In addition, the permissive nature of the BSD license has allowed many other operating systems, both free and proprietary, to incorporate BSD code. For example, Microsoft Windows has used BSD-derived code in its implementation of TCP/IP and bundles recompiled versions of BSD's command-line networking tools since Windows 2000. Also Darwin, the system on which Apple's macOS is built, is a derivative of 4.4BSD-Lite2 and FreeBSD. Various commercial Unix operating systems, such as Solaris, also contain varying amounts of BSD code.

## Significant BSD descendants

BSD has been the base of a large number of operating systems. Most notable among these today are perhaps the major open source BSDs: FreeBSD, NetBSD and OpenBSD, which are all derived from 386BSD and 4.4BSD-Lite by various routes. Both NetBSD and FreeBSD started life in 1993, initially derived from 386BSD, but in 1994 migrating to a 4.4BSD-Lite code base. OpenBSD was forked in 1995 from NetBSD. A number of commercial operating systems are also partly or wholly based on BSD or its descendants, including Sun's SunOS and Apple Inc.'s macOS.

Most of the current BSD operating systems are open source and available for download, free of charge, under the BSD License, the most notable exception being macOS. They also generally use a monolithic kernel architecture, apart from macOS and DragonFly BSD which feature hybrid kernels. The various open source BSD projects generally develop the kernel and userland programs and libraries together, the source code being managed using a single central source repository.

In the past, BSD was also used as a basis for several proprietary versions of Unix, such as Sun's SunOS, Sequent's Dynix, NeXT's NeXTSTEP, DEC's Ultrix and OSF/1 AXP (now Tru64 UNIX). Parts of NeXT's software became the foundation for macOS, among the most commercially successful BSD variants in the general market.

A selection of significant Unix versions and Unix-like operating systems that descend from BSD includes:

- FreeBSD, an open source general purpose operating system.
  - Orbis OS, Sony's fork of FreeBSD 9 is the operating system for the PS4. CellOS for the PS3 system is believed to also be a FreeBSD fork, and is known to contain FreeBSD and NetBSD code
  - TrueOS, GhostBSD and DesktopBSD, distributions of FreeBSD with emphasis on ease of use and user friendly interfaces for the desktop/laptop PC user.
  - MidnightBSD, another fork of FreeBSD
  - DragonFly BSD, a fork of FreeBSD to follow an alternative design, particularly related to SMP.
  - NextBSD, new BSD distribution derived from FreeBSD 10.1 and various macOS components.
  - FreeNAS a free network-attached storage server based on a minimal version of FreeBSD.
  - NAS4Free fork of 0.7 FreeNAS version, Network attached storage server.
  - Nokia IPSO (IPSO SB variant), the FreeBSD-based OS used in Nokia Firewall Appliances.
  - The OS for the Netflix Open Connect Appliance.
  - Junos, the operating system for Juniper routers, a customized version of FreeBSD, and a variety of other embedded operating systems
  - Isilon Systems' OneFS, the operating system used on Isilon IQ-series clustered storage systems, is a heavily customized version of FreeBSD.
  - NetApp's Data ONTAP, the operating system for NetApp filers, is a customized version of FreeBSD with the ONTAP architecture built on top.
  - m0n0wall, a FreeBSD distribution tweaked for usage as a firewall.
  - pfSense free open source FreeBSD based firewall/router.
  - OPNsense, firewall, a fork of pfSense
  - Coyote Point Systems EQ/OS, a hardened high-performance runtime for server load balancing.
- NetBSD, an open source BSD focused on clean design and portability.
  - OpenBSD, a 1995 fork of NetBSD, focused on security.
  - Force10 FTOS, the operating system for Force 10 and Dell datacenter network switches.
    - Dell DNOS version 9 and above, the successor to FTOS.
- NeXT NEXTSTEP and OPENSTEP, based on the Mach kernel and 4BSD; the ancestor of macOS
  - Apple Inc.'s Darwin, the core of macOS and iOS; built on the XNU kernel (part Mach, part FreeBSD, part Apple-derived code) and a userland much of which comes from FreeBSD
- TrustedBSD
- F5 Networks, F5 BIGIP Appliances used a BSD OS as the management OS until version 9.0 was released, which is built on top of Linux.
- DEC's Ultrix, the official version of Unix for its PDP-11, VAX, and DECstation systems
- Sony NEWS-OS, a BSD-based operating system for their network engineering workstations
- OSF/1, a hybrid kernel based Unix developed by the Open Software Foundation, incorporating a modified Mach kernel and parts of 4BSD
  - Tru64 UNIX (formerly DEC OSF/1 AXP or Digital UNIX), the port of OSF/1 for DEC Alpha-based systems from DEC, Compaq and HP.
- Pre-5.0 versions of Sun Microsystems SunOS, an enhanced version of 4BSD for the Sun Motorola 68k-based Sun-2 and Sun-3 systems, SPARC-based systems, and x86-based Sun386i systems (SunOS 5.0 and later versions are System V Release 4-based)
- 386BSD, the first open source BSD-based operating system and the ancestor of most current BSD systems
- DEMOS, a Soviet BSD clone
- BSD/OS, a (now defunct) proprietary BSD for PCs
