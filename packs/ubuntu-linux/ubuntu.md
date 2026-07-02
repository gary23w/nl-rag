---
title: "Ubuntu"
source: https://en.wikipedia.org/wiki/Ubuntu
domain: ubuntu-linux
license: CC-BY-SA-4.0
tags: ubuntu linux, canonical company, ubuntu release, long-term support
fetched: 2026-07-02
---

# Ubuntu

**Ubuntu** (/ʊˈbʊntuː/ ⓘ *uu-BUUN-too*) is a Linux distribution based on Debian and composed primarily of free and open-source software. Developed by the British company Canonical and a community of contributors under a meritocratic governance model, Ubuntu is released in multiple official editions: *Desktop*, *Server*, and *Core* for IoT and robotic devices.

Ubuntu is published on a six-month release cycle, with long-term support (LTS) versions issued every two years. Canonical provides security updates and support until each release reaches its designated end-of-life (EOL), with optional extended support available through the Ubuntu Pro and Expanded Security Maintenance (ESM) services.

Ubuntu can be installed directly on hardware or run within a virtual machine. It is widely used for cloud computing, with integration support for platforms such as OpenStack. It is also one of the most popular Linux distributions for general desktop use, supported by extensive online communities such as Ask Ubuntu, and has spawned numerous community-maintained variants.

The name "Ubuntu" comes from the Nguni philosophy of **ubuntu**, which translates roughly as "humanity to others" or "I am what I am because of who we all are".

## History

In April 2004, Mark Shuttleworth invited a dozen Debian developers to his London flat, where they brainstormed and laid out the distinguishing features of what would become Ubuntu. Shuttleworth chose the "Ubuntu" name for his South African roots and to emphasize community. To fund the project, Shuttleworth created Canonical Ltd. to employ the developers using his fortune from selling Thawte to Verisign. For the first year, the company had no physical offices and employees used online platforms to coordinate, fostering transparency. The group set a six-month deadline and decided only to announce Ubuntu during its first release—October 2004: "Warty Warthog".

On 8 July 2005, Shuttleworth and Canonical launched the newly-created Ubuntu Foundation and provided initial funding of US$10 million. The purpose of the foundation is to ensure the support and development for all future versions of Ubuntu. Mark Shuttleworth described the foundation's goal as to ensure the continuity of the Ubuntu project.

On 12 March 2009, Ubuntu announced developer support for third-party cloud management platforms, such as those used at Amazon EC2.

In 2011, Ubuntu's default desktop was changed from GNOME 2 to the in-house Unity instead of GNOME 3.

In 2014, Canonical announced Snappy Ubuntu Core, an immutable OS designed for use in embedded systems, along with its new package manager named "Snappy" derived from the Ubuntu Phone project. By the release of Ubuntu 16.04, the package management system was renamed "Snap" and supported desktop apps, becoming an alternative to Flatpak.

After nearly 6.5 years, the default desktop was changed back to GNOME 3 in 2017, upon the release of version 17.10. Ubuntu, since version 16.04.5, requires a 2 GB or larger installation medium. The last release of Ubuntu available on a minimal CD was 18.04. 32-bit x86 processors were supported up to Ubuntu 18.04. It was decided to support "legacy software", i.e. select 32-bit i386 packages, for Ubuntu 19.10 (since out of support) and 20.04 LTS.

In 2022, Ubuntu consolidated its extended security maintenance and hardening services into the Ubuntu Pro subscriptions, including LivePatch, a feature that allows devices to perform select security updates without reboots, available free-of-charge for personal use on up to five machines.

In June 2023, Canonical announced Ubuntu Core Desktop, an immutable desktop OS, completely made of snap packages like Ubuntu Core and slated for release along Ubuntu 24.04 LTS. Its release was indefinitely delayed, as the vision for major advantages had not yet been fully realized.

After a rise in the popularity of cryptocurrency scam packages, the Snap Store started requiring manual approval for new applications in March 2024.

On 9 August 2024, Ubuntu announced a change in policy to always use the latest upstream version of the Linux kernel at the time of each Ubuntu release, even if the kernel code has not seen a stable release and is still in release candidate status.

Support for the X11 windowing system was dropped in favour of the alternative Wayland with Ubuntu version 25.10 in 2025, which shipped with GNOME 49 which had made the change.

## Features

Ubuntu is built on Debian's architecture and infrastructure, and comprises Linux server, desktop, and discontinued phone and tablet operating system versions. As of version 24.10, a default installation of Ubuntu contains a minimal selection of software, namely a web browser (Firefox), and basic GNOME utilities (including the desktop). Many additional software packages are accessible from the built-in Ubuntu Software (previously Ubuntu Software Center), as well as any other APT-based package management tools. Many additional software packages that are no longer installed by default, such as Evolution, GIMP, Pidgin, and Synaptic, are still accessible in the repositories and installable by the main tool or by any other APT-based package management tool. Cross-distribution snap packages and Flatpaks are also available, that both allow installing software, such as some of Microsoft's software, in most of the major Linux operating systems (such as any currently supported Ubuntu version and in Fedora). The default file manager is GNOME Files, formerly called Nautilus.

All of the application software installed by default is free software. In addition, Ubuntu redistributes some hardware drivers that are available only in binary format, but such packages are clearly marked in the restricted component.

Current long-term support (LTS) releases are supported for five years, and are released every two years. Since the release of Ubuntu 6.06, every fourth release receives long-term support. Long-term support includes updates for new hardware, security patches, and updates to the 'Ubuntu stack' (cloud computing infrastructure). The first LTS releases were supported for three years on the desktop and five years on the server; since Ubuntu 12.04 LTS, desktop support for LTS releases was increased to five years as well. LTS releases get regular point releases with support for new hardware and integration of all the updates published in that series to date.

Ubuntu packages are based on Debian's unstable branch, which are synchronized every six months. Both distributions use Debian's package management tools (e.g. APT and GNOME Software) and deb format of packages. Debian and Ubuntu packages are not necessarily binary compatible with each other, however, some packages may need to be rebuilt from source to be used in Ubuntu. Many Ubuntu developers are also maintainers of key packages within Debian. Ubuntu cooperates with Debian by pushing changes back to Debian, although there has been criticism that this does not happen often enough. Ian Murdock, the founder of Debian, had expressed concern about Ubuntu packages potentially diverging too far from Debian to remain compatible. Before release, packages are imported from Debian unstable continuously and merged with Ubuntu-specific modifications. At some point during the release process, the Debian Import Freeze is implemented. This prevents the automatic import of packages from Debian without an explicit request from a developer. In combination with other freezes, this helps packagers ensure that frozen features interoperate well together.

All official Ubuntu packages are available from hundreds of mirrors worldwide. As of 30 March 2025, there were a total of 617 Ubuntu mirrors operating.

## Security

Ubuntu aims to be secure by default. User programs run with low privileges and cannot corrupt the operating system or other users' files. For increased security, the sudo tool is used to assign temporary privileges for performing administrative tasks, which allows the root account to remain locked and helps prevent inexperienced users from inadvertently making catastrophic system changes or opening security holes. Polkit is also being widely implemented into the desktop.

Most network ports are closed by default to prevent hacking. A built-in firewall, Uncomplicated Firewall, allows end-users who install network servers to control access. A GUI is available to configure it. Ubuntu compiles its packages using GCC features such as PIE and buffer overflow protection to harden its software. These extra features greatly increase security at the performance expense of 0.01% in 64-bit.

Ubuntu also supports full disk encryption, as well as encryption of the home and private directories.

## Installation

The system requirements vary among Ubuntu products. For the Ubuntu desktop release 22.04 LTS (and still for 24.04.3), a PC with at least 2 GHz dual-core processor, 4 GB of RAM and 25 GB of free disk space is recommended. For less powerful computers, there are other Ubuntu distributions such as Lubuntu and Xubuntu. Ubuntu also supports the ARM architecture. It is also available on Power ISA, while older PowerPC architecture was at one point unofficially supported, and now newer Power ISA CPUs (POWER8) are supported. The x86-64 ("AMD64") architecture is also officially supported.

Live images are the typical way for users to assess and subsequently install Ubuntu. These can be downloaded as a disk image (.iso) and subsequently burnt to a DVD or USB flash drive and then booted. Other methods include running the live version via Ventoy, UNetbootin, Universal USB Installer, or Startup Disk Creator (a pre-installed tool on Ubuntu, available on machines already running the OS) directly from a USB drive (making, respectively, a live DVD or live USB medium). Running Ubuntu in this way is slower than running it from a hard drive, but does not alter the computer unless specifically instructed by the user. If the user chooses to boot the live image rather than execute an installer at boot time, there is still the option to then use the Ubuntu Desktop Installer once booted into the live environment. The Ubuntu Desktop Installer replaced the former Ubiquity installer since Ubuntu 23.04. Disk images of all current and past versions are available for download at the Ubuntu web site.

Additionally, USB flash drive installations can be used to boot Ubuntu and Kubuntu in a way that allows permanent saving of user settings and portability of the USB-installed system between physical machines (however, the computers' BIOS must support booting from USB). In newer versions of Ubuntu, the Ubuntu Live USB creator can be used to install Ubuntu on a USB drive (with or without a live CD or DVD). Creating a bootable USB drive with persistence is as simple as dragging a slider to determine how much space to reserve for persistence; for this, Ubuntu employs casper.

## Package classification and support

Ubuntu divides most software into four domains to reflect differences in licensing and the degree of support available. Some unsupported applications receive updates from community members known as "Masters of the Universe" (MOTU). Before January 2023, community supported free software in *Universe* repository received no updates at all from Canonical Ltd. Since 26 January 2023, customers of the Ubuntu Pro subscription service—which is free for personal use—can get Canonical-supported updates also for packages in *Universe* repository.

|   | Free software | Non-free software |
|---|---|---|
| Officially supported by Canonical | Main | Restricted |
| Community supported/Third party | Universe | Multiverse |

Free software includes software that has met the Ubuntu licensing requirements, which roughly correspond to the Debian Free Software Guidelines. Exceptions, however, include firmware, in the Main category, because although some firmware is not allowed to be modified, its distribution is still permitted.

Non-free software is usually unsupported (Multiverse), but some exceptions (Restricted) are made for important non-free software and/or software potentially illegal in some territories. Supported non-free software includes device drivers that can be used to run Ubuntu on some current hardware, such as binary-only graphics card drivers. The level of support in the Restricted category is more limited than that of Main, because the developers may not have access to the source code. It is intended that Main and Restricted should contain all software needed for a complete desktop environment.

In addition to the above, in which the software does not receive new features after an initial release, *Ubuntu Backports* is an officially recognised repository for backporting newer software from later versions of Ubuntu.

The *-updates* repository provides stable release updates (SRU) of Ubuntu and are generally installed through update-manager. Each release is given its own *-updates* repository (e.g. intrepid-updates). The repository is supported by Canonical Ltd. for packages in main and restricted, and by the community for packages in universe and multiverse. All updates to the repository must meet certain requirements and go through the *-proposed* repository before being made available to the public.

In addition to the *-updates* repository, the unstable *-proposed* repository contains uploads that must be confirmed before being copied into *-updates*. All updates must go through this process to ensure that the patch does truly fix the bug and there is no risk of regression.

Canonical previously hosted a partner repository that let vendors of proprietary software deliver their products to Ubuntu users at no cost through the same familiar tools for installing and upgrading software. The software in the partner repository was officially supported with security and other important updates by its respective vendors. Canonical supported the packaging of the software for Ubuntu and provided guidance to vendors. However, in anticipation for the release of Ubuntu 22.04 LTS Canonical closed the partner repository, as the only package still hosted in it was Adobe Flash, which would not be released with 22.04. Ubuntu developer Steve Langasek said in a development mailing list that he felt the "Snap Store has matured to the point that I believe it supersedes the partner archive".

### Package Archives

A *Personal Package Archive* (PPA) is a software repository for uploading source packages to be built and published as an Advanced Packaging Tool (APT) repository by Canonical's Launchpad service. While the term is used exclusively within Ubuntu, Canonical, envisions adoption beyond the Ubuntu community.

### Third-party software

Some third-party software that does not limit distribution is included in Ubuntu's multiverse component. The package *ubuntu-restricted-extras* additionally contains software that may be legally restricted, including support for DVD playback, Microsoft TrueType core fonts, many common audio/video codecs, and unrar, an unarchiver for files compressed in the RAR file format.

Additionally, third-party application suites are available for download via Ubuntu Software and the Snap store, including many games such as Braid, Minecraft and Oil Rush, software for DVD playback and media codecs.

## Releases

| Version | Code name | Release date | General support until | Security support (ESM) until |
|---|---|---|---|---|
| 18.04 LTS | Bionic Beaver | 2018-04-26 | Unsupported: 2023-05-31 | Supported: 2028-04 |
| 20.04 LTS | Focal Fossa | 2020-04-23 | Unsupported: 2025-05-29 | Supported: 2030-04 |
| 22.04 LTS | Jammy Jellyfish | 2022-04-21 | Supported: 2027-06-01 | Supported: 2032-04 |
| 24.04 LTS | Noble Numbat | 2024-04-25 | Supported: 2029-05 | Supported: 2034-04 |
| 25.10 | Questing Quokka | 2025-10-09 | Supported: 2026-07 | - |
| 26.04 LTS | Resolute Raccoon | 2026-04-23 | Latest version: 2031-05 | Latest version: 2036-05 |
| 26.10 | Stonking Stingray | 2026-10-15 | Preview version: 2027-07 | - |
| **Legend:**UnsupportedSupported**Latest version**Preview versionFuture version |   |   |   |   |

Ubuntu follows a time-based release cycle, issuing new versions every six months. Each standard release receives nine months of free support, including security updates and high-impact bug fixes.

Every fourth release, occurring in the second quarter of even-numbered years, is designated a long-term support (LTS) release. LTS releases receive five years of free support, with the option to extend support up to ten years through the Expanded Security Maintenance (ESM) program, available through the Ubuntu Pro subscriptions, which are free for personal use.

Ubuntu version numbers reflect the year and month of release. For example, Ubuntu 4.10 was released in October 2004.

Each release also has an alliterative code name, typically consisting of an adjective and an animal (e.g., "Bionic Beaver"). Releases are often referred to by the adjective alone.

Ubuntu releases are typically scheduled about one month after corresponding GNOME releases.

## Variants

Ubuntu Desktop (formally named as Ubuntu Desktop Edition, and simply called Ubuntu) is the variant officially recommended for most users. It is designed for desktop and laptop PCs and is officially supported by Canonical. Variants are distinguished simply by each featuring a different desktop environment, or, in the case of Ubuntu Server, no desktop. LXQt and Xfce are often recommended for use with older PCs that may have less memory and processing power available.

### Official distributions

Most Ubuntu editions and flavours simply install a different set of default packages compared to the standard Ubuntu Desktop. Since they share the same package repositories, all of the same software is available for each of them. Ubuntu Core is the sole exception as it only has access to packages in the Snap Store.

| Distribution | Logo | Description |
|---|---|---|
| Edubuntu | (Edubuntu logo) | Edubuntu, formerly Ubuntu Education Edition, is a flavour of Ubuntu that has been modified for education. It is designed for preschool, primary, secondary and tertiary educations through the installation of different packages. |
| Kubuntu | (Kubuntu logo) | An Ubuntu flavour using the KDE interface instead of the GNOME (and Unity) interface used by Ubuntu Desktop. |
| Lubuntu | (Lubuntu logo) | Lubuntu is an Ubuntu flavour that is "lighter, less resource hungry and more energy-efficient", using the LXQt desktop environment (used LXDE before 18.10). |
| Ubuntu Core |   | An Ubuntu edition focused on IoT and embedded systems. It has no graphical interface, and only allows access over SSH. Unlike other variants, it does not use the traditional apt package manager but relies entirely on Snap packages. It is designed to be configured via *model assertions* which are text documents defining which Snap packages and configurations apply to the OS image. |
| Ubuntu Budgie | (Ubuntu Budgie logo) | An Ubuntu flavour using Budgie. |
| Ubuntu Cinnamon | (Ubuntu Cinnamon logo) | An Ubuntu flavour using Linux Mint's Cinnamon desktop. Formerly known as Ubuntu Cinnamon Remix. |
| Ubuntu Kylin | (Ubuntu Kylin logo) | An Ubuntu flavour aimed at the Chinese market. |
| Ubuntu MATE | (Ubuntu MATE logo) | An Ubuntu flavour using MATE, a desktop environment forked from the now-defunct GNOME 2 code base, with an emphasis on the desktop metaphor. |
| Ubuntu Server | (Ubuntu logo) | Ubuntu has a server edition that uses the same APT repositories as the Ubuntu Desktop Edition. The differences between them are the absence of an X Window environment in a default installation of the server edition (although one can easily be installed, including GNOME, KDE, Unity or Xfce), and some alterations to the installation process. The server edition uses a screen-mode, character-based interface for the installation, instead of a graphical installation process. This enables installation on machines with a serial or "dumb terminal" interface without graphics support. The server edition (like the desktop version) supports hardware virtualization and can be run in a virtual machine, either inside a host operating system or in a hypervisor, such as VMware ESXi, Oracle, Citrix XenServer, Microsoft Hyper-V, QEMU, a Kernel-based Virtual Machine, or any other IBM PC compatible emulator or virtualiser. AppArmor security module for the Linux kernel is used by default on key software packages, and the firewall is extended to common services used by the operating system. Runs on all major (64-bit) architectures – x86-64, ARM v7, ARM64, POWER8 and later, IBM System z mainframes via LinuxONE, and has initial support for RISC-V. SPARC is no longer commercially supported nor are Ubuntu (Server) versions for 32-bit x86. Supports ZFS, a file system with snapshot capabilities, since Ubuntu 16.04 LTS. Has LXD, a hypervisor to manage LXC Linux containers. Includes the first production release of DPDK for line-speed kernel networking. Uses the latest long-term release Linux kernel and systemd service manager. Is certified as a guest on AWS, Microsoft Azure, Joyent, IBM and HP Cloud. Netplan support (available since Ubuntu 16.04 LTS) snap package manager LVM encryption support Ubuntu pre-installs software such as Tomcat, PostgreSQL, Docker, Puppet, Python, PHP, LXD, NGINX, and MySQL. |
| Ubuntu Studio | (Ubuntu Studio logo) | Based on Ubuntu, providing open-source applications for multimedia creation aimed at the audio, video and graphic editors. This release uses the KDE Plasma 5 desktop environment; previous releases used Xfce. |
| Ubuntu Unity | (Ubuntu Unity logo) | An Ubuntu flavour using Unity 7. |
| Xubuntu | (Xubuntu logo) | An Ubuntu flavour using Xfce. Xubuntu is intended for use on less-powerful computers or those who seek a highly efficient desktop environment on faster systems, and uses mostly GTK applications. |

Ubuntu had some official distributions that have been discontinued, such as Gobuntu; including some previously supported by Canonical, like Ubuntu Touch, that is now maintained by volunteers (UBports Community).

### Unofficial distributions

Alongside the official flavours are those that are unofficial. These are still in the process of becoming recognised as official flavours by Canonical.

| Distribution | Logo | Description |
|---|---|---|
| UbuntuDDE | (UbuntuDDE logo) | An unofficial Ubuntu flavour using Deepin Desktop Environment. |
| Ubuntu Sway | (Ubuntu Sway logo) | An unofficial Ubuntu flavour using Sway Window Manager. |
| Ubuntu Web |   | An unofficial Ubuntu flavour using GNOME Desktop Environment, with the focus on web applications. |
| Ubuntu Asahi |   | An unofficial project porting Asahi Linux to Ubuntu, for use on Apple Silicon Macs. |

### Cloud computing

Ubuntu offers Ubuntu Cloud Images which are pre-installed disk images that have been customised by Ubuntu engineering to run on cloud-platforms such as Amazon EC2, OpenStack, Microsoft Azure and LXC. Ubuntu is also prevalent on VPS platforms such as DigitalOcean.

Ubuntu has support for OpenStack, with Eucalyptus to OpenStack migration tools added by Canonical. Ubuntu 11.10 added focus on OpenStack as the Ubuntu's preferred IaaS offering, though Eucalyptus is also supported. Another major focus is Canonical Juju for provisioning, deploying, hosting, managing, and orchestrating enterprise data centre infrastructure services, by, with, and for the Ubuntu Server.

## Adoption and reception

Ubuntu was awarded the Reader Award for best Linux distribution at the 2005 LinuxWorld Conference and Expo in London, received favourable reviews in online and print publications, and has won InfoWorld's 2007 Bossie Award for *Best Open Source Client OS*. In early 2008, *PC World* named Ubuntu the "best all-around Linux distribution available today", though it criticized the lack of an integrated desktop effects manager. Chris DiBona, the program manager for open-source software at Google, said "I think Ubuntu has captured people's imaginations around the Linux desktop," and "If there is a hope for the Linux desktop, it would be them". As of January 2009, almost half of Google's 20,000 employees used Goobuntu, a slightly modified version of Ubuntu. In 2012, *ZDNet* reported that Ubuntu was still Google's desktop of choice. In March 2016, Matt Hartley picked a list of best Linux distributions for *Datamation*; he chose Ubuntu as number one.

In 2008, Jamie Hyneman, co-host of the American television series *MythBusters*, advocated Linux (giving the example of Ubuntu) as a solution to software bloat. Other celebrity users of Ubuntu include science fiction writer Cory Doctorow and actor Stephen Fry.

In January 2014, the UK's authority for computer security, CESG, reported that Ubuntu 12.04 LTS was "the only operating system that passes as many as 9 out of 12 requirements without any significant risks", though it was unclear if any other Linux distributions were tested.

### Installed base

As Ubuntu is distributed freely and historically, there was no registration process (still optional), Ubuntu usage can only be roughly estimated. In 2015, Canonical's Ubuntu Insights page stated, "Ubuntu now has over 40 million desktop users and counting".

W3Techs Web Technology Surveys estimated in November 2020 that:

- Ubuntu is by far the most popular Linux distribution for running web servers; of the websites they analyse it is "used by 47.3% of all the websites who use Linux", and Ubuntu alone powers more websites than Microsoft Windows, which powers 28.2% of all websites, or 39% of the share Unix has (which includes Linux and thus Ubuntu). All Linux/Unix distributions in total power well over twice the number of hosts as Windows for websites based on W3Techs numbers. Ubuntu and Debian only (which Ubuntu is based on, with the same package manager and thus administered the same way) make up 65% of all Linux distributions for web serving use; the usage of Ubuntu surpassed Debian (for such server use) in May 2016.
- Ubuntu is the most popular Linux distribution among the top 1,000 sites and gains around 500 of the top 10 million websites per day.

W3Techs analyses the top 10 million websites only.

Wikimedia Foundation data (based on user agent) for September 2013 shows that Ubuntu generated the most page requests to Wikimedia sites, including Wikipedia, among recognizable Linux distributions.

As of October 2025, Ubuntu 22.04 is used in Microsoft NDv5, a Microsoft's Azure cloud computer, its fastest one (of 7 Azure supercomputers, all running on Ubuntu), still fastest ever Microsoft computer, currently 5th fastest, previously in November 2024, 3rd fastest supercomputer on the TOP500 list (only then beaten by the then only two exaflop computers; is itself half an exaflop, only the then top 3 were that powerful). Other supercomputers running Ubuntu also rank high on the list e.g. NVIDIA's Selene supercomputer still ranks highly, and was fifth-fastest one in the world in November 2022 after an upgrade from seventh place, where it entered the list in June. Another Nvidia-based supercomputer using Ubuntu previously topped the Green500 list (it and the next one was also Ubuntu-based), a list which is a reordering of former list, ordered by power-efficiency. On the TOP500 list, that supercomputer was ranked 170nd (and many Ubuntu-based rank higher than that).

### Large-scale deployments

The public sector has also adopted Ubuntu. As of January 2009, the Ministry of Education and Science of North Macedonia deployed more than 180,000 Ubuntu-based classroom desktops, and has encouraged every student in the country to use Ubuntu-powered computer workstations; the Spanish school system has 195,000 Ubuntu desktops. The French police, having already started using open-source software in 2005 by replacing Microsoft Office with OpenOffice.org, decided to transition to Ubuntu from Windows XP after the release of Windows Vista in 2006. By March 2009, the Gendarmerie Nationale had already switched 5,000 workstations to Ubuntu. Based on the success of that transition, it planned to switch 15,000 more over by the end of 2009 and to have switched all 90,000 workstations over by 2015 (GendBuntu project). Lt. Colonel Guimard announced that the move was very easy and allowed for a 70% saving on the IT budget without having to reduce its capabilities. In 2011, Ubuntu 10.04 was adopted by the Indian justice system.

In 2004, the city of Munich, Germany, started the LiMux project, and later forked Kubuntu 10.04 LTS for use on the city's computers. After originally planning to migrate 12,000 desktop computers to LiMux, it was announced in December 2013 that the project had completed successfully with the migration of 14,800 out of 15,500 desktop computers, but still keeping about 5,000 Windows clients for unported applications. In February 2017 the majority coalition decided, against heavy protest from the opposition, to evaluate the migration back to Windows, after Microsoft had decided to move its company headquarters to Munich. Governing Mayor Dieter Reiter cited lack of compatibility with systems outside of the administrative sector, such as requiring a governmental mail server to send e-mails to his personal smartphone, as reasons for the return, but has been criticised for evaluating administrative IT based on private and business standards. In May 2020, the recently elected Alliance 90/The Greens party and the Social Democrat party negotiated a new coalition agreement, stating: "Where it is technologically and financially possible, the city will emphasize open standards and free open-source licensed software".

In March 2012, the government of Iceland launched a project to get all public institutions using free and open-source software. Already, several government agencies and schools have adopted Ubuntu. The government cited cost savings as a big factor for the decision, and also stated that open-source software avoids vendor lock-in. A 12-month project was launched to migrate the biggest public institutions in Iceland to using open-source software, and help ease the migration for others. US president Barack Obama's successful campaign for re-election in 2012 used Ubuntu in its IT department. In August 2014, the city of Turin, Italy, announced its migration from Windows XP to Ubuntu for the 8,300 desktop computers used by the municipality, becoming the first city in Italy to adopt Ubuntu.

Starting in 2008, the Wikimedia Foundation, the non-profit organization behind Wikipedia, switched from multiple different Linux operating systems to Ubuntu (in 2019, it switched again, from Ubuntu to Debian).

During the 2010s, some Tesla Model S owners, discovered via little hack that the touchscreen computer for entertainment and navigation assistance, runs on an adapted version of Ubuntu.

### 32-bit "deprecation" controversy

In June 2019, Canonical announced that they would be deprecating support for 32-bit applications and libraries in Ubuntu 19.10.

Because Steam's Linux client depends on these 32-bit libraries, Valve announced that they would no longer be supporting Ubuntu. After uproar from the Linux gaming community, Canonical backtracked on this decision and decided to support select 32-bit libraries. As a result, Valve decided that Steam would support Ubuntu 19.10 again.

Wine needs most of the same 32-bit library packages that the Steam package depends on, and more, to enable its version of WoW64 to run 32-bit Windows applications. The parts of Wine that would continue to function without 32-bit libraries would be limited to the subset of Windows applications that have a 64-bit version, removing decades of Windows compatibility. In Canonical's statement on bringing back the libraries, they mentioned using "container technology" in the future to make sure that Wine continues to function.

### Conformity with European data privacy law

Soon after being introduced in 2012, doubts emerged on the conformance of the *shopping lens* (a feature that displays Amazon suggestions in the searching tool Unity Dash) with the European Data Protection Directive. A petition was later signed and delivered to Canonical demanding various modifications to the feature to clearly frame it within European law. Canonical did not reply.

In 2013, a formal complaint on the shopping lens was filed with the Information Commissioner's Office (ICO), the UK data privacy office. Almost one year later, the ICO ruled in favour of Canonical, considering the various improvements introduced to the feature conformed with the Data Protection Directive. According to European rules, this ruling is automatically effective in the entirety of the European Union. However, the ruling also made clear that at the time of introduction the feature was not legal, among other things, since it was missing a privacy policy statement.

### System terminal advertising controversies

Ubuntu has integrated increasing quantities of advertising into the operating system's terminal, leading to multiple controversies with its user base.

In 2017, Canonical placed a message regarding HBO's Silicon Valley in the MOTD file, causing the message to be shown whenever a terminal session started. Over the following years, more messages would be placed into the MOTD.

In 2022, ads for Ubuntu's premium service, Ubuntu Advantage, were introduced into the apt system update utility. This move caused controversy in the user community, with some users considering advertising a fair business model to support development, while other users found the inclusion inappropriate and annoying.

## Local communities (LoCos)

To reach out to users who are less technical, and to foster a sense of community around the distribution, Local Communities, better known as "LoCos", have been established throughout the world. Originally, each country had one LoCo Team. However, in some areas, most notably the United States and Canada, each state or province may establish a team. A LoCo Council approves teams based upon their efforts to aid in either the development or the promotion of Ubuntu.

## Hardware vendor support

Ubuntu has received broad support from hardware vendors, with several manufacturers offering computers pre-installed with the operating system. Canonical collaborates with original equipment manufacturers (OEMs) to certify and support Ubuntu on a variety of devices, primarily targeting enterprise and developer markets.

Major OEMs such as Dell, Lenovo, and HP have offered laptops and desktops with Ubuntu as an alternative to Windows, often through online configuration options or regional sales channels. Ubuntu is also offered on the IBM Z series of mainframes.

Smaller vendors such as System76 and OnLogic also ship systems with Ubuntu pre-installed, sometimes offering firmware customization or support options through Canonical.

## Windows interoperability

Many Windows applications can be run on Ubuntu, much like in other Linux distributions, using the Wine compatibility layer, which can be managed via frontends such as Bottles.

Steam has a Windows compatibility layer called Proton, and it has derivatives such as GE-Proton.

Multiple Windows virtual machines can also be installed by KVM/QEMU and Virt-Manager. Graphics settings are easiest in QXL/SPICE mode. For 3D accelerated graphics performance, there is a third-party VirGL driver or GPU Full Passthrough mode.

In a networked environment, file sharing between Ubuntu Linux and Windows is possible by Samba client/server software. Host Ubuntu Linux and the guest Windows virtual machines are also virtually networked in KVM, so file sharing between the host and virtual guest machines can also be done by the Samba in the KVM environment.

RDP server of GNOME Remote Desktop and Remmina client software is used for remote desktop connection between Ubuntu Linux and the other OSs.

In March 2016, Microsoft announced that it would support the Ubuntu userland on top of the Windows 10 kernel by implementing the Linux system calls as a subsystem. At the time, it was focused on command-line tools like Bash and was aimed at software developers. WSL was made available with Windows 10, version 1709. As of 2019, other Linux distributions are also supported.

In 2019, Microsoft announced the new WSL 2 subsystem that includes a Linux kernel, that Canonical announced will have "full support for Ubuntu". By this time, it was possible to run graphical Linux apps on Windows. In 2021, Microsoft went on to add out-of-the-box support for graphical Linux apps, through the WSLg project.

In May 2021, Microsoft extended its Threat and Vulnerability Management solution, which was a Windows-only solution thus far, to support Ubuntu, RHEL, and CentOS. Starting with version 6, PowerShell runs on Ubuntu and can manage both Windows and Ubuntu computers remotely from either platforms.
