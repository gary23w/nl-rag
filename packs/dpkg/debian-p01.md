---
title: "Debian (part 1/2)"
source: https://en.wikipedia.org/wiki/Debian
domain: dpkg
license: CC-BY-SA-4.0
tags: dpkg debian, debian packages, package manager, deb archive
fetched: 2026-07-02
part: 1/2
---

# Debian

**Debian** (/ˈdɛbiən/) is a free, general-purpose operating system developed by the Debian Project, a worldwide association of volunteers founded by Ian Murdock on August 16, 1993. It is the second-oldest Linux distribution still being developed (only Slackware is older) and forms the base of many others.

It is deployed across servers, personal computers, and embedded devices. Among Linux distributions, it ranks second only to Ubuntu (which is itself derived from Debian), with 16% of the overall market. According to the 2025 Stack Overflow Developer Survey, 11.4% of developers use it as their primary personal operating system and 10.4% professionally. Its emphasis on stability and long-term support over frequent package updates has made it prevalent in server and embedded deployments.

Development is led by the Project Leader and guided by two foundational documents: the Debian Social Contract, a summary of the project's commitments that includes the Debian Free Software Guidelines (DFSG), and the Debian Constitution, which describes the organizational structure. The project publishes three concurrent development branches: stable, testing, and unstable, which correspond to different levels of software maturity. The current stable release, "Trixie", released on August 9, 2025, includes tens of thousands of packages maintained by more than a thousand active contributors.

Since 1997, the project has operated independently through Software in the Public Interest (SPI), a non-profit corporation founded by project members to hold its assets and trademarks. It previously received support from the Free Software Foundation (FSF) between 1994 and 1995, a sponsorship that ended due to disagreements.


## History

### Version history

Debian uses version numbers and code names based on the characters of the *Toy Story* franchise to refer to its releases. This naming convention was introduced by former project leader Bruce Perens, who was working at Pixar at the time. The unstable branch is permanently named after Sid, the neighborhood child known for destroying toys.

### Founding (1993–1999)

The first public mention of the project occurred on August 16, 1993, when Ian Murdock posted an announcement to the *comp.os.linux.development* newsgroup. Murdock founded the project due to his dissatisfaction with the Softlanding Linux System (SLS); after making extensive modifications to this system, he concluded that it would be more efficient to develop a new distribution from scratch. Similar to the original announcement of Linux, Murdock's post solicited feedback and suggestions on how the system could be improved. The name *Debian* was a portmanteau of his first name and that of his then-wife, Deborah Lynn.

The first internal release, pre-alpha 0.01, came out on September 15, 1993. The first public versions, beta 0.90 and beta 0.91, followed on January 26 and 29, 1994, respectively, with their mailing lists hosted by Pixar. These releases included the Debian Linux Manifesto, in which Murdock outlined his vision for the project, advocating for a distribution "developed openly in the spirit of Linux and GNU".

Between November 1994 and November 1995, the project was sponsored by the FSF, whose sponsorship Murdock had sought with the hope that it would also give the FSF experience in packaging a complete GNU system. In March 1995, Murdock stepped down as project leader to dedicate more time to his studies, work, and family; the new team did not seek to continue the FSF sponsorship. While the Debian Project remained aligned with the FSF's political and philosophical goals, differences in technical direction led to an end to the arrangement, with the FSF invited to continue participating in the project on the same basis as individual developers and other contributing organizations. Following the end of that sponsorship, Debian motivated the formation of Software in the Public Interest (SPI), a non-profit corporation registered in the state of New York. SPI was founded to help Debian and other similar organizations develop and distribute open hardware and software, acting as a fiscal sponsor by handling non-technical administrative tasks so that projects are not required to operate their own legal entity.

In April 1996, Bruce Perens became the project leader. On June 17 of the same year, Debian 1.1 "Buzz" was released, the first release under his leadership. By that time, Ian Jackson's dpkg had already become an integral part of Debian. The concept of a social contract with the free software community was suggested to Perens by Ean Schussler; Perens composed a draft, which was subsequently refined by Debian developers through email discussion over most of June and approved by vote, producing the Debian Social Contract and the DFSG, published on July 4, 1997. He created BusyBox to enable running the installer from a single floppy disk. By the time Debian 1.2 "Rex" was released on December 12, 1996, the project had grown to nearly 200 volunteers. Perens stepped down as project leader in December 1997 and left the project entirely on March 18, 1998.

Ian Jackson became project leader in January 1998. Debian 2.0 "Hamm", released on July 24, 1998, was the first multi-architecture release of Debian, adding support for the Motorola 68000 family (m68k). On December 2, 1998, the Debian Constitution was ratified for the first time, simultaneously initiating the election process that would result in Wichert Akkerman succeeding Jackson as project leader in January 1999. On March 9, 1999, Debian 2.1 "Slink" was released, alongside the package manager front-end APT. On May 23, 1999, the Internal Revenue Service determined that SPI qualifies for 501(c)(3) status, providing a mechanism by which the Debian Project may accept contributions that are tax deductible in the United States.

### Consolidation (2000–2004)

On December 13, 2000, Debian activated package pools on its ftp-master archive server, a change to the archive system that had to be made before preparation of the "Woody" release could begin. A package pool consists of a collection of different versions of a given package, from which branches, experimental, unstable, testing, and stable, draw packages for inclusion in their respective package files. This change enabled special-purpose distributions, including a new testing branch that was used for the first time to prepare "Woody" for release. Under this system, packages from unstable considered to be sufficiently stable were promoted to testing after a waiting period of several weeks, a mechanism intended to reduce freeze time and allow the project to prepare a new release at any point.

The first Debian Conference was held in Bordeaux, France, from July 5 to 9, 2000. The event brought Debian developers and advanced users together in person for the first time, giving the Debian project a physical presence as an organization rather than existing solely as an online collective. In addition to working sessions, the conference served as a venue for attendees to meet other members of the free software community, with some presentations open to the general public. Discussion topics included the Debian user base and its adoption in corporate settings and derived distributions, ongoing development of "Woody", the Debian GNU/Hurd port, the project's quality-control processes, the procedure for becoming a Debian developer, and tools such as debconf and boot-floppies. The program combined presentations, technical talks, birds-of-a-feather sessions, and coding parties.

In May 2001, Hewlett-Packard (HP) announced that it would use Debian as the basis for its future Linux development work. Martin Fink, HP's general manager of Linux systems operations, said the company chose Debian because it was the most free and open Linux distribution available, a factor he believed would help prevent proprietary software from dominating efforts to establish a standardized Linux platform, since Debian was not controlled by any single commercial entity. Debian developer Bruce Perens, who acted as HP's Linux advocate, disclosed the decision in an email to the Debian development mailing list, noting that HP had already begun distributing Debian to customers and planned to offer support and training for it. Perens described the move as an initial step toward HP's broader support for the Linux Standard Base (LSB) project.

On November 20, 2002, a fire destroyed the network operations center at the University of Twente in the Netherlands, which hosted one of Debian's servers, satie.debian.org. The blaze broke out around 8:00 a.m. local time and consumed the building so thoroughly that firefighters could not save the server room. Because satie had hosted the project's security archive, its non-US archive, and the databases supporting new-maintainer applications and quality assurance, the corresponding services (security.debian.org, non-us.debian.org, nm.debian.org, and qa.debian.org) went offline as a result. Debian subsequently rebuilt these services on another host, klecker, which had recently been relocated from the United States to the Netherlands.

Released on July 19, 2002, Debian 3.0 "Woody" expanded the project's scope. Supported by a community of over 900 developers and led by newly appointed Project Leader Bdale Garbee, the release included approximately 8,500 binary packages distributed across seven official binary CDs. This version broadened hardware compatibility by introducing support for several new architectures, including IA-64, HP PA-RISC, MIPS (both big and little endian), and S/390. Furthermore, it was the first Debian release to incorporate cryptographic software, following the relaxation of Cold War US cryptography export restrictions, as well as the first to feature the KDE desktop environment after its Qt licensing issues were resolved.

On October 20, 2004, Mark Shuttleworth announced the first release of Ubuntu, 4.10 "Warty Warthog", a new Debian-derived distribution aimed at combining Debian's extensive package base with a faster installer, a fixed six-month release cycle, and 18 months of security support per release. The rapid growth of Ubuntu sparked debate within the Debian community regarding the long-term compatibility of Debian-derived distributions. Some Debian developers warned that as more developers began building packages targeting Ubuntu rather than Debian proper, divergence between the two could erode that compatibility, mimicking the fragmentation seen among RPM-based distributions. Other community members argued that Debian should address its lengthy release cycles, calling for a predictable, time-based release schedule similar to that adopted by the GNOME Project, in order to reduce the incentive for downstream distributions to fork.

### Sarge and later releases (2005–present)

The 3.1 Sarge release was made in June 2005. This release updated 73% of the software and included over 9,000 new packages. A new installer with a modular design, Debian-Installer, allowed installations with redundant array of inexpensive disks (RAID), file system XFS, and Logical Volume Manager (LVM) support, improved hardware detection, made installations easier for novice users, and was translated into almost forty languages. An installation manual and release notes were in ten and fifteen languages respectively. The efforts of Skolelinux, Debian-Med and Debian-Accessibility raised the number of packages that were educational or had a medical affiliation, and of packages made for people with disabilities.

In 2006, as a result of a much-publicized dispute, Mozilla software was rebranded in Debian. The Mozilla Corporation stated that software with unapproved modifications could not be distributed under the Firefox trademark. Two reasons that Debian had modified the Firefox software were to replace non-free artwork and to provide security patches. Consequently, Debian contained a fork of Firefox named Iceweasel and one of Thunderbird named Icedove. In February 2016, it was announced that Mozilla and Debian had reached an agreement and Iceweasel would revert to the name Firefox; a similar agreement was anticipated for Icedove/Thunderbird.

A fundraising experiment, Dunc-Tank, was created to solve the release cycle problem and release managers were paid to work full-time; in response, unpaid developers slowed down their work and the release was delayed.

Debian 4.0 (Etch) was released in April 2007, featuring the x86-64 port and a graphical installer. Debian 5.0 (Lenny) was released in February 2009, supporting Marvell's Orion platform and netbooks such as the Asus Eee PC. The release was dedicated to Thiemo Seufer, a developer who died in a car crash.

In July 2009, the policy of time-based development freezes on a two-year cycle was announced. Time-based freezes are intended to blend the predictability of time based releases with Debian's policy of feature-based releases, and to reduce overall freeze time. The Squeeze cycle was going to be especially short; however, this initial schedule was abandoned. In September 2010, the backporting service became official, providing more recent versions of some software for the stable release.

Debian 6.0 (Squeeze) was released in February 2011, featuring Debian GNU/kFreeBSD as a technology preview, along with adding a dependency-based boot system, and moving problematic firmware to the non-free section. Debian 7 (Wheezy) was released in May 2013, featuring multiarch support. Debian 8 (Jessie) was released in April 2015, using systemd as the new init system. Debian 9 (Stretch) was released in June 2017, with nftables as a replacement for iptables, support for Flatpak apps, and MariaDB as the replacement for MySQL. Debian was formerly released as a very large set of CDs for each architecture, but with the release of Debian 9 (Stretch) in 2017, many of the images have been dropped from the archive but remain buildable via jigdo.

Debian 10 (Buster) was released in July 2019, adding support for Secure Boot and enabling AppArmor by default. Debian 11 (Bullseye) was released in August 2021, enabling persistency in the system journal, adding support for driverless scanning, and containing kernel-level support for exFAT filesystems.

Debian 12 (Bookworm) was released on June 10, 2023, including various improvements and features, increasing the supported Linux kernel to version 6.1, and leveraging new "Emerald" artwork. Debian 12 also was the first version under a revised Debian Social Contract that includes non-free firmware in its installation media by default, if and when the installer detects that it is needed for installed hardware to function, such as with Wi-Fi cards. Debian 13 (Trixie) was released on August 9, 2025.

Debian 14 has been announced to have the code name Forky, and Debian 15 has been announced to have the code name Duke.

Debian is under continuous development and new packages are uploaded to *unstable* every day.

Throughout Debian's lifetime, both the Debian distribution and its website have won various awards from different organizations, including Server Distribution of the Year 2011, The best Linux distro of 2011, and a *Best of the Net* award for October 1998.

On December 2, 2015, Microsoft announced that they would offer Debian as an endorsed distribution on the Azure cloud platform. Debian has also been made available for installation in Microsoft's Windows Subsystem for Linux, which allows a user to install a tightly integrated Debian virtual machine within Windows.


## Features

Debian has online repositories that contain nearly 70,000 packages for the stable release. Debian officially contains only free software, but non-free software can be downloaded and installed from the Debian repositories. Debian includes popular free programs such as LibreOffice, Firefox web browser, Thunderbird e-mail client, VLC media player, GIMP image editor, and Okular document viewer. Debian is a popular choice for servers, for example as the operating system component of a LAMP stack.

Beyond the typical server environment, Debian is increasingly used in cloud computing, containerization, and artificial intelligence (AI) development. It serves as a foundation for Docker containers and is supported by Google Cloud's deep learning virtual machines (VMs), positioning it as a platform for new workloads.

### Kernels

Several flavors of the Linux kernel exist for each port. For example, the i386 port has flavors for IA-32 PCs supporting Physical Address Extension and real-time computing, for older PCs, and for x86-64 PCs. The Linux kernel does not officially contain firmware lacking source code, although such firmware is available in non-free packages and alternative installation media.

### Graphical user interfaces

Many desktop environments are available in the project's main repository. GNOME (the default in the installer) and KDE Plasma are the most widely installed according to the Debian Popularity Contest. Other environments are also available, such as Xfce, LXDE, LXQt, MATE, and Lumina. Standalone X11 window managers and Wayland compositors are also included, such as Openbox, Fluxbox, Compiz, awesome, i3, dwm, Notion, Sway, and wmii.

### Localization

Several parts of Debian are translated into languages other than American English, including package descriptions, configuration messages, documentation and the website. The level of software localization depends on the language, ranging from the highly supported German and French to the barely translated Creek and Samoan. The Debian 10 installer is available in 76 languages.

### Multimedia support

Multimedia support has been problematic in Debian regarding codecs threatened by possible patent infringements, lacking source code, or under too restrictive licenses. Even though packages with problems related to their distribution could go into the non-free area, software such as libdvdcss is not hosted at Debian .


## Distribution

Debian offers DVD and CD images for installation that can be downloaded using HTTP, FTP, BitTorrent or jigdo. Physical discs can also be bought from retailers. The full sets are made up of several discs (the amd64 port consists of 13 DVDs or 84 CDs), but only the first disc is required for installation, as the installer can retrieve software not contained in the first disc image from online repositories.

Debian offers different network installation methods. A minimal install of Debian is available via the *netinst* CD, whereby Debian is installed with just a base and later added software can be downloaded from the Internet. Another option is to boot the installer from the network.

The default bootstrap loader is GNU GRUB version 2, though the package name is simply grub, while version 1 was renamed to grub-legacy. This conflicts with distros (e.g., Fedora Linux), where grub version 2 is named grub2.

The default desktop may be chosen from the DVD boot menu among GNOME, KDE Plasma, Xfce, LXDE, and LXQt and from special disc 1 CDs.

Debian releases live install images for CDs, DVDs and USB flash drives for x86-64 architecture, and with a choice of desktop environments. These *Debian Live* images allow users to boot from removable media and run Debian without affecting the contents of their computer. A full install of Debian to the computer's hard drive can be initiated from the live image environment. Personalized images can be built with the live-build tool for discs, USB drives and for network booting purposes. Installation images are hybrid on some architectures and can be used to create a bootable USB drive (Live USB).


## Packages

Package management operations can be performed with different tools available on Debian, from the lowest level command dpkg to graphical front-ends like Synaptic. The recommended standard for administering packages on a Debian system is the apt toolset.

dpkg provides the low-level infrastructure for package management. The dpkg database contains the list of installed software on the current system. The dpkg command tool does not know about repositories. It works with local .deb package files. These can be either under the dpkg database directory tree or in arbitrary locations specified by the user.

### APT tools

An Advanced Packaging Tool (APT) allows a Debian system to retrieve and resolve package dependencies from repositories. APT tools share dependency information and cached packages.

- The apt command is intended as an end user interface and enables some options better suited for interactive usage by default compared to more specialized APT like apt-get and apt-cache explained below.
- apt-get and apt-cache are command tools of the standard apt package. apt-get installs and removes packages, and apt-cache is used for searching packages and displaying package information.
- Aptitude is a command line tool that also offers a text-based user interface. The program comes with enhancements such as better search on package metadata.

### GDebi and other front-ends

GDebi is an APT tool which can be used in command-line and on the GUI. GDebi can install a local .deb file via the command line like the dpkg command, but with access to repositories to resolve dependencies. Other graphical front-ends for APT include Software Center, Synaptic and Apper.

GNOME Software is a graphical front-end for PackageKit, which can work on various software packaging systems.

### Repositories

The Debian Free Software Guidelines (DFSG) define the distinctive meaning of the word "free" as in "free and open-source software". Packages that comply with these guidelines, usually under the GNU General Public License, Modified BSD License or Artistic License, are included inside the *main* area; otherwise, they are included inside the *non-free* and *contrib* areas. These last two areas are not distributed within the official installation media, but they can be adopted manually.

Non-free includes packages that do not comply with the DFSG, such as documentation with invariant sections and proprietary software, and legally questionable packages. Contrib includes packages which do comply with the DFSG but fail other requirements. For example, they may depend on packages which are in non-free or requires such for building them.

Richard Stallman and the Free Software Foundation have criticized the Debian project for hosting the non-free repository and because the contrib and non-free areas are easily accessible, an opinion echoed by some in Debian including the former project leader Wichert Akkerman. The internal dissent in the Debian project regarding the non-free section has persisted, but the last time it came to a vote in 2004, the majority voted to keep it.

### Cross-distribution package managers

The most popular optional Linux cross-distribution package manager are graphical (front-ends) package managers. They are available within the official Debian Repository but are not installed by default. They are widely popular with both Debian users and Debian software developers who are interested in installing the most recent versions of application or using the cross-distribution package manager built-in sandbox environment. While at the same time remaining in control of the security.

**Four most popular cross-distribution package managers, sorted in alphabetical order:**

- AppImage Linux distribution-agnostic binary software deployment
- Flatpak software code is owned and maintained by the not for profit Flatpak Team, with an open source LGPL-2.1-or-later license.
- Homebrew software code is owned and maintained by its original author Max Howell, with an open source BSD 2-Clause License.
- Snap software code is owned and maintained by the for-profit Canonical Group Limited, with an open source GNU General Public License, version 3.0.


## Branches

Three branches of Debian (also called *releases*, *distributions* or *suites*) are regularly maintained:

- *Stable* is the current release and targets stable and well-tested software needs. *Stable* is made by freezing *Testing* for a few months where bugs are fixed and packages with too many bugs are removed; then the resulting system is released as *stable*. It is updated only if major security or usability fixes are incorporated. This branch has an optional backporting service that provides more recent versions of some software. *Stable*'s images (for USB sticks, CDs, DVDs, etc) can be found in the Debian website. The current version of *Stable* is codenamed *trixie*.
- *Testing* is the preview branch that will eventually become the next major release. The packages included in this branch have had some testing in *unstable* but they may not be fit for release yet. It contains newer packages than *stable* but older than *unstable*. This branch is updated continually until it is frozen. *Testing*'s images (for USB sticks, CDs, DVDs, etc) can be found on the Debian website. The current version of *Testing* is codenamed *forky*.
- *Unstable*, always codenamed *sid*, is the trunk. Packages are accepted without checking the distribution as a whole. This branch is usually run by software developers who participate in a project and need the latest libraries available, and by those who prefer bleeding-edge software. Debian does not provide full Sid installation discs, but rather a minimal ISO that can be used to install over a network connection. Additionally, this branch can be installed through a system upgrade from *stable* or *testing*.

Other branches in Debian:

- *Oldstable* is the prior *stable* release. It is supported by the Debian Security Team until one year after a new *stable* is released, and since the release of Debian 6, for another two years through the Long Term Support project. Eventually, *oldstable* is moved to a repository for archived releases. Debian 12 is the current Oldstable release (since 2025-08-09).
- *Oldoldstable* is the prior *oldstable* release. It is supported by the Long Term Support community. Eventually, *oldoldstable* is moved to a repository for archived releases. Debian 11 is the current Oldoldstable release (since 2025-08-09).
- *Experimental* is a temporary staging area of highly experimental software that is likely to break the system. It is not a full distribution and missing dependencies are commonly found in *unstable*, where new software without the damage risk is normally uploaded.

The *snapshot* archive provides older versions of the branches. They may be used to install a specific older version of some software.

### Numbering scheme

*Stable* and *oldstable* get minor updates, called *point releases*; as of August 2021, the *stable* release is version 11.7, released on April 29, 2023 (2023-04-29), and the *oldstable* release is version 10.10.

The numbering scheme for the point releases up to Debian 4.0 was to include the letter *r* (for *revision*) after the main version number and then the number of the point release; for example, the latest point release of version 4.0 is 4.0r9. This scheme was chosen because a new dotted version would make the old one look obsolete and vendors would have trouble selling their CDs.

From Debian 5.0, the numbering scheme of point releases was changed, conforming to the GNU version numbering standard; the first point release of Debian 5.0 was 5.0.1 instead of 5.0r1. The numbering scheme was once again changed for the first Debian 7 update, which was version 7.1. The *r* scheme is no longer in use, but point release announcements include a note about not throwing away old installation media.


## Branding

Debian has two logos. The official logo (also known as *open use logo*) contains the well-known Debian *swirl* and best represents the visual identity of the Debian Project. A separate logo also exists for use by the Debian Project and its members only.

The Debian "swirl" logo was designed by Raul Silva in 1999 as part of a contest to replace the semi-official logo that had been used. The winner of the contest received an @Debian.org email address, and a set of Debian 2.1 install CDs for the architecture of their choice. Initially, the swirl was magic smoke arising from an also included bottle of an Arabian-style genie presented in black profile, but shortly after was reduced to the red smoke swirl for situations where space or multiple colours were not an option, and before long the bottle version effectively was superseded. There has been no official statement from the Debian project on the logo's meaning, but at the time of the logo's selection, it was suggested that the logo represented the magic smoke that made computers work.

One theory about the origin of the Debian logo is that Buzz Lightyear, the chosen character for the first named Debian release, has a swirl in his chin. Stefano Zacchiroli also suggested that this swirl is the Debian one. Buzz Lightyear's swirl is a more likely candidate as the codenames for Debian are names of Toy Story characters. The former Debian project leader Bruce Perens used to work for Pixar and is credited as a studio tools engineer on *Toy Story 2* (1999).


## Hardware

Hardware requirements are at least those of the kernel and the GNU toolsets. Debian's recommended system requirements depend on the level of installation, which corresponds to increased numbers of installed components:

| Type | Minimum RAM size | Recommended RAM size | Minimum processor clock speed (IA-32) | Hard-drive capacity |
|---|---|---|---|---|
| Non-desktop | 256 MiB | 512 MiB |   | 4 GB |
| Desktop | 1 GiB | 2 GiB | 1GHz | 10 GB |

The real minimum memory requirements depend on the architecture and may be much less than the numbers listed in this table. It is possible to install Debian with 170 MB of RAM for x86-64; the installer will run in low memory mode and it is recommended to create a swap partition. The installer for z/Architecture requires about 20 MB of RAM, but relies on network hardware. Similarly, disk space requirements, which depend on the packages to be installed, can be reduced by manually selecting the packages needed. As of May 2019, no Pure Blend exists that would lower the hardware requirements easily.

It is possible to run graphical user interfaces on older or low-end systems. However, installing window managers instead of desktop environments is recommended, as desktop environments use more resources. Requirements for individual software vary widely and must be considered, with those of the base operating environment.

### Architectures

As of 9 August 2025, the Trixie release, the instruction set architecture officially supported are:

- amd64: x86-64 64-bit
- arm64: ARMv8 64-bit
- armel: ARMv5 32-bit for use on legacy embedded systems (support dropped from *unstable* on 2025-11-03)
- armhf: ARMv7 32-bit, requires a floating-point unit
- ppc64el: PowerPC 64-bit for use with POWER7+ and POWER8 CPUs
- riscv64: RISC-V 64-bit
- s390x: z/Architecture 64-bit

Unofficial ports are available as part of the *unstable* distribution:

- alpha: DEC Alpha
- hppa: HP PA-RISC
- hurd-i386: GNU Hurd kernel on IA-32
- hurd-amd64: GNU Hurd kernel on x86-64
- i386: IA-32 32-bit, compatible with x86 machines
- loong64: LoongArch
- mips64el: MIPS 64-bit
- mipsel: MIPS 32-bit (support dropped on 2025-11-03)
- m68k: Motorola 68k on Amiga, Atari, Macintosh and various embedded VME systems
- powerpc: PowerPC 32-bit
- sh4: Hitachi SuperH
- sparc64: Sun SPARC 64-bit
- x32: x32 ABI for x86-64

Debian supports a variety of ARM-based network-attached storage (NAS) devices. The NSLU2 was supported by the installer in Debian 4.0 and 5.0, and Martin Michlmayr is providing installation tarballs since version 6.0. Other supported NAS devices are the Buffalo Kurobox Pro, GLAN Tank, Thecus N2100 and QNAP Turbo Stations.

Devices based on the Kirkwood system on a chip (SoC) are supported too, such as the SheevaPlug plug computer and OpenRD products. There are efforts to run Debian on mobile devices, but this is not a project goal yet since the Debian Linux kernel maintainers would not apply the needed patches. Nevertheless, packages exist for resource-limited systems.

There are efforts to support Debian on wireless access points. Debian is known to run on set-top boxes. Work is ongoing to support the AM335x processor, which is used in electronic point of service solutions. Debian may be customized to run on cash machines. BeagleBoard, a low-power open-source hardware single-board computer made by Texas Instruments, has switched to Debian Linux preloaded on its Beaglebone Black board's flash. Roqos Core, a x86-64 based IPS firewall router, runs on Debian Linux.


## Organization

General Resolution

elect↓

override↓

Leader

↓appoint

Delegate

↓decide

Developer

propose↑

Simplified organizational structure

Debian's policies and team efforts focus on collaborative software development and testing processes. As a result, a new major release tends to occur every two years with revision releases that fix security issues and important problems. The Debian project is a volunteer organization with two foundation documents:

- The *Debian Social Contract* defines a set of basic principles by which the project and its developers conduct affairs.
- The *Debian Free Software Guidelines* define the criteria for "free software" and thus what software is permissible in the distribution. These guidelines have been adopted as the basis of The Open Source Definition. Although this document can be considered separate, it formally is part of the Social Contract.
- The *Debian Constitution* describes the organizational structure for formal decision-making within the project, and enumerates the powers and responsibilities of the Project Leader, the Secretary and other roles.

| Year | DD | ±% |
|---|---|---|
| 1999 | 347 | — |
| 2000 | 347 | +0.0% |
| 2001 | ? | — |
| 2002 | 939 | — |
| 2003 | 831 | −11.5% |
| 2004 | 911 | +9.6% |
| 2005 | 965 | +5.9% |
| 2006 | 972 | +0.7% |
| 2007 | 1,036 | +6.6% |
| 2008 | 1,075 | +3.8% |
| 2009 | 1,013 | −5.8% |
| 2010 | 886 | −12.5% |
| 2011 | 911 | +2.8% |
| 2012 | 948 | +4.1% |
| 2013 | 988 | +4.2% |
| 2014 | 1,003 | +1.5% |
| 2015 | 1,033 | +3.0% |
| 2016 | 1,023 | −1.0% |
| 2017 | 1,062 | +3.8% |
| 2018 | 1,001 | −5.7% |
| 2019 | 1,003 | +0.2% |
| 2020 | 1,011 | +0.8% |
| 2021 | 1,018 | +0.7% |
| 2022 | 1,023 | +0.5% |
| 2023 | 996 | −2.6% |
| 2024 | 1,010 | +1.4% |
| 2025 | 1,030 | +2.0% |
| Source: Debian Voting Information |   |   |

Debian developers are organized in a web of trust. There are at present about one thousand active Debian developers, but it is possible to contribute to the project without being an official developer.

The project maintains official mailing lists and conferences for communication and coordination between developers. For issues with single packages and other tasks, a public bug tracking system is used by developers and end users. Internet Relay Chat is also used for communication among developers and to provide real time help.

Debian is supported by donations made to organizations authorized by the leader. The largest supporter is Software in the Public Interest, the owner of the Debian trademark, manager of the monetary donations and umbrella organization for various other community free software projects.

A Project Leader is elected once per year by the developers. The leader has special powers, but they are not absolute, and appoints delegates to perform specialized tasks. Delegates make decisions as they think is best, taking into account technical criteria and consensus. By way of a General Resolution, the developers may recall the leader, reverse a decision made by the leader or a delegate, amend foundation documents and make other binding decisions. The voting method is based on the Schulze method (Cloneproof Schwartz Sequential Dropping).

| Debian project leaders |   |
|---|---|
|   |   |
| 1993 —–1994 —–1995 —–1996 —–1997 —–1998 —–1999 —–2000 —–2001 —–2002 —–2003 —–2004 —–2005 —–2006 —–2007 —–2008 —–2009 —–2010 —–2011 —–2012 —–2013 —–2014 —–2015 —–2016 —–2017 —–2018 —–2019 —–2020 —–2021 —–2022 —–2023 —–2024 —–2025 —–2026 —–2027 — | Ian MurdockBruce PerensIan JacksonWichert AkkermanBen CollinsBdale GarbeeMartin MichlmayrBranden RobinsonAnthony TownsSam HocevarSteve McIntyreStefano ZacchiroliLucas NussbaumNeil McGovernMehdi DogguyChris LambSam HartmanJonathan CarterAndreas TilleSruthi Chandran |
|   |   |

Project leadership is distributed occasionally. Branden Robinson was helped by the Project Scud, a team of developers that assisted the leader, but there were concerns that such leadership would split Debian into two developer classes. Anthony Towns created a supplemental position, Second In Charge (2IC), that shared some powers of the leader. Steve McIntyre was 2IC and had a 2IC himself.

One important role in Debian's leadership is that of a release manager. The release team sets goals for the next release, supervises the processes and decides when to release. The team is led by the next release managers and stable release managers. Release assistants were introduced in 2003.

### Developers

The Debian Project has an influx of applicants wishing to become developers. These applicants must undergo a vetting process which establishes their identity, motivation, understanding of the project's principles, and technical competence. This process has become much harder throughout the years.

Debian developers join the project for many reasons. Some that have been cited include:

- Debian is their main operating system and they want to promote Debian
- To improve the support for their favorite technology
- They are involved with a Debian derivative
- A desire to contribute back to the free software community
- To make their Debian maintenance work easier

Debian developers may resign their position at any time, or when deemed necessary, they can be expelled. Those who follow the retiring protocol are granted *emeritus* status and may regain their membership via a shortened new member process.

Debian has made efforts to diversify and have members represented from the community. Debian Women in 2004 was established with the aim of having more women involved in development. Debian also partnered with Outreachy, which offers internships to individuals with underrepresented identities in technology.


## Development

|   |   |   |   |
|---|---|---|---|
| upstream |   |   |   |
|   | ↓ | packaging |   |
| package |   |   |   |
|   | ↓ | upload |   |
| incoming |   |   |   |
|   | ↓ | checks |   |
| unstable |   |   |   |
|   | ↓ | migration |   |
| testing |   |   |   |
|   | ↓ | freeze |   |
| frozen |   |   |   |
|   | ↓ | release |   |
| stable |   |   |   |

Flowchart of the life cycle of a Debian package

Each software package has a *maintainer* that may be either one person or a team of Debian developers and non-developer maintainers. The maintainer keeps track of upstream releases, and ensures that the package coheres with the rest of the distribution and meets the standards of quality of Debian. Packages may include modifications introduced by Debian to achieve compliance with Debian Policy, even to fix non-Debian specific bugs, although coordination with upstream developers is advised.

The maintainer releases a new version by uploading the package to the "incoming" system, which verifies the integrity of the packages and their digital signatures. If the package is found to be valid, it is installed in the package archive into an area called the *pool* and distributed every day to hundreds of mirrors worldwide. As of April 5, 2025, there were a total of 379 Debian mirrors operating. The upload must be signed using OpenPGP-compatible software. All Debian developers have individual cryptographic key pairs. Developers are responsible for any package they upload even if the packaging was prepared by another contributor.

Initially, an accepted package is only available in the *unstable* branch. For a package to become a candidate for the next release, it must migrate to the *Testing* branch by meeting the following:

- It has been in *unstable* for a certain length of time that depends on the urgency of the changes.
- It does not have "release-critical" bugs, except for the ones already present in *Testing*. Release-critical bugs are those considered serious enough that they make the package unsuitable for release.
- There are no outdated versions in *unstable* for any release ports.
- The migration does not break any packages in *Testing*.
- Its dependencies can be satisfied by packages already in *Testing* or by packages being migrated at the same time.
- The migration is not blocked by a freeze.

Thus, a release-critical bug in a new version of a shared library on which many packages depend may prevent those packages from entering *Testing*, because the updated library must meet the requirements too. From the branch viewpoint, the migration process happens twice per day, rendering *Testing* in perpetual beta.

Periodically, the release team publishes guidelines to the developers in order to ready the release. A new release occurs after a freeze, when all important software is reasonably up-to-date in the *Testing* branch and any other significant issues are solved. At that time, all packages in the *testing* branch become the new *stable* branch. Although freeze dates are time-based, release dates are not, which are announced by the release managers a couple of weeks beforehand.

A version of a package can belong to more than one branch, usually *testing* and *unstable*. It is possible for a package to keep the same version between stable releases and be part of *oldstable*, *stable*, *testing* and *unstable* at the same time. Each branch can be seen as a collection of pointers into the package "pool" mentioned above.

One way to resolve the challenge of a release-critical bug in a new application version is the use of optional package managers. They allow software developers to use sandbox environments, while at the same time remaining in control of security. Another benefit of a cross-distribution package manager is that they allow application developers to directly provide updates to users without going through distributions, and without having to package and test the application separately for each distribution.

### Release cycle

A new *stable* branch of Debian is released about every 2 years. It will receive official support for about 3 years with update for major security or usability fixes. Point releases will be available every several months as determined by Stable Release Managers (SRM).

Debian also launched its Long Term Support (LTS) project since Debian 6 (Debian Squeeze). For each Debian release, it will receive two years of extra security updates provided by LTS Team after its End Of Life (EOL). However, no point releases will be made. Now each Debian release can receive 5 years of security support in total.

### Security

The Debian project handles security through public disclosure. Debian security advisories are compatible with the Common Vulnerabilities and Exposures dictionary, are usually coordinated with other free software vendors and are published the same day a vulnerability is made public. There used to be a security audit project that focused on packages in the stable release looking for security bugs; Steve Kemp, who started the project, retired in 2011 but resumed his activities and applied to rejoin in 2014.

The *stable* branch is supported by the Debian security team; *oldstable* is supported for one year. Although Squeeze was not officially supported, Debian coordinated an effort to provide long-term support for IA-32 and x86-64 platforms, until February 2016, five years after the initial release. *Testing* is supported by the *testing* security team, but does not receive updates in as timely a manner as *stable*. *Unstable*'s security is left for the package maintainers.

The Debian project offers documentation and tools to harden a Debian installation both manually and automatically. AppArmor support is available and enabled by default since Buster. Debian provides an optional hardening wrapper, and does not harden all of its software by default using gcc features such as PIE and buffer overflow protection, unlike operating systems such as OpenBSD, but tries to build as many packages as possible with hardening flags.

In May 2008, a Debian developer discovered that the OpenSSL package distributed with Debian and derivatives such as Ubuntu made a variety of security keys vulnerable to a random number generator attack, since only 32,767 different keys were generated. The security weakness was caused by changes made in 2006 by another Debian developer in response to memory debugger warnings. The complete resolution procedure was cumbersome because patching the security hole was not enough; it involved regenerating all affected keys and certificates.

Recent versions of Debian have focused more on safer defaults. Debian 10 had AppArmor enabled by default, and Debian 11 improved Secure Boot support and included persistent system journaling. The project is also making all packages reproducible, which helps to ensure software integrity.

### Value

The cost of developing all of the packages included in Debian 5.0 Lenny (323 million lines of code) has been estimated to be about US$8 billion, using one method based on the COCOMO model. As of May 2024, Black Duck Open Hub estimated that the current codebase (74 million lines of code) would cost about US$1.6 billion to develop, using a different method based on the same model.


## Institutional users

Debian is used by several institutions, such as many universities, NGOs and other non-profit organizations (including the Wikimedia Foundation), and commercial companies. It has even been used in space, in laptops on board the International Space Station.

Debian has been very helpful to numerous government agencies in the public sector, such as in the city of Munich, which used a Debian-based distribution in its LiMux initiative for the government computer migration to Linux. Schools in Extremadura and Andalusia (Spain) also utilized Debian-based systems (gnuLinEx and Guadalinex, respectively) to develop digital skills and open-source computing in schools. There are many other cases of usage of Debian-based distributions in education, such as the deployment of Skolelinux/Debian Edu in Norwegian schools. In addition, other public administrations use Linux systems indirectly based on Debian, such as French Gendarmerie, which uses Ubuntu-derived GendBuntu distribution.
