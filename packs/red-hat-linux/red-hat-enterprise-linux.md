---
title: "Red Hat Enterprise Linux"
source: https://en.wikipedia.org/wiki/Red_Hat_Enterprise_Linux
domain: red-hat-linux
license: CC-BY-SA-4.0
tags: red hat enterprise linux, yum package manager, dnf tool, centos rebuild
fetched: 2026-07-02
---

# Red Hat Enterprise Linux

**Red Hat Enterprise Linux** (**RHEL**) is a commercial Linux distribution developed by Red Hat. Red Hat Enterprise Linux is released in server versions for x86-64, Power ISA, ARM64, and IBM Z and a desktop version for x86-64. Fedora Linux and CentOS Stream serve as its upstream sources. All of Red Hat's official support and training, together with the Red Hat Certification Program, focuses on the Red Hat Enterprise Linux platform.

The first version of Red Hat Enterprise Linux to bear the name originally came onto the market as "Red Hat Linux Advanced Server". In 2003, Red Hat rebranded Red Hat Linux Advanced Server to "Red Hat Enterprise Linux AS" and added two more variants, Red Hat Enterprise Linux ES and Red Hat Enterprise Linux WS.

As Red Hat Enterprise Linux is heavily based on open-source software and its source code is available to the public, it is used as the basis for several third-party derivatives, including the commercial Oracle Linux and the community-supported Rocky Linux and AlmaLinux. Prior to June 2023, Red Hat published a sub-set of Red Hat Enterprise Linux's source code to the public in the form of modified build artifacts. Today, the complete source code for the major-version branch is available in the form of the CentOS Stream repositories. Source code for other release branches remains available to customers in the form of unmodified build artifacts.

## Variants

A Red Hat Enterprise Linux Server subscription is available at no cost for development purposes. Developers need to register for the Red Hat Developer Program and agree to its license terms. The free developer subscription was announced on March 31, 2016, and updated in January 2021 with less restrictive terms.

There are also "Academic" editions of the Desktop and Server variants. They are offered to schools and students, are less expensive, and are provided with Red Hat technical support as an optional extra. Web support based on the number of customer contacts can be purchased separately.

It is often assumed the branding ES, AS, and WS stand for "Entry-level Server", "Advanced Server" and "Work Station", respectively.

In Red Hat Enterprise Linux 5 there are new editions that substitute former Red Hat Enterprise Linux AS/ES/WS/Desktop:

- Red Hat Enterprise Linux Advanced Platform (former AS)
- Red Hat Enterprise Linux (former ES) (limited to two CPUs)
- Red Hat Enterprise Linux Desktop with Workstation and Multi-OS option
- Red Hat Enterprise Linux Desktop with Workstation option (former WS)
- Red Hat Enterprise Linux Desktop with Multi-OS option
- Red Hat Enterprise Linux Desktop (former Desktop)

Red Hat had also announced its Red Hat Global Desktop Linux edition "for emerging markets".

RHEL 4, 3, and prior releases had four variants:

- Red Hat Enterprise Linux AS for mission-critical/enterprise computer systems.
- Red Hat Enterprise Linux ES for supported network servers
- Red Hat Enterprise Linux WS for technical power user enterprise desktops for high-performance computing
- Red Hat Desktop for multiple deployments of single-user desktops for enterprises.

## Relationship with Fedora Linux

The Fedora Project provides the following explanation:

> Fedora is a free distribution and community project and upstream for Red Hat Enterprise Linux. Fedora is a general purpose system that gives Red Hat and the rest of its contributor community the chance to innovate rapidly with new technologies. Red Hat Enterprise Linux is a commercial enterprise operating system and has its own set of test phases including alpha and beta releases which are separate and distinct from Fedora development.

Originally, Red Hat sold boxed versions of Red Hat Linux directly to consumers and business through phone support. The Fedora Project began in 2002 as a set of community supported packages for Red Hat Linux. However, the six month release cycle of Red Hat Linux was too disruptive for business users and Red Hat wanted a more reliable revenue stream. In 2002 Red Hat began releasing Red Hat Enterprise Linux based on Red Hat Linux, but with a much more conservative release cycle and a subscription based support program. A year later, Red Hat discontinued the Red Hat Linux product line, merging it with the Fedora community packages and releasing the resulting Fedora distribution for free.

Fedora serves as the primary upstream for future major releases of RHEL: RHEL source code repositories are forked off the Fedora repository, and released after a substantial stabilization and quality assurance effort. The major-version stable release branch is built and released by the CentOS project under the name CentOS Stream. Each minor version of RHEL is a branch of CentOS Stream that gets ongoing bug fixes and security updates.

For example, CentOS Stream 9 was forked from Fedora in March, 2021 (shortly before the Fedora 34 release) and available on public mirrors in September, 2021. RHEL 9.0 was released in May, 2022.

The Fedora Project lists the following lineages for older Red Hat Enterprise releases:

- Red Hat Linux 6.2/7 to Red Hat Linux Enterprise Edition 6.2E
- Red Hat Linux 7.2, 7.2A to Red Hat Enterprise Linux 2.1
- Red Hat Linux 9 to Red Hat Enterprise Linux 3
- Fedora Core 3 to Red Hat Enterprise Linux 4
- Fedora Core 6 to Red Hat Enterprise Linux 5
- Fedora 12, 13 to Red Hat Enterprise Linux 6
- Fedora 19, 20 to Red Hat Enterprise Linux 7
- Fedora 28 to Red Hat Enterprise Linux 8
- Fedora 34 to CentOS Stream 9 to Red Hat Enterprise Linux 9
- Fedora 40 to CentOS Stream 10 to Red Hat Enterprise Linux 10

In addition, the Fedora project publishes a set of packages for RHEL called the Extra Packages for Enterprise Linux (EPEL). EPEL packages can be expected to work in RHEL, but it is up to willing community members to maintain the packages and back port any upstream changes. As such, packages "may come and go" during the ten-year lifespan of the RHEL release and Red Hat support plans do not include resolving issues caused by EPEL packages.

## Derivatives

Red Hat Enterprise Linux is derived from free and open source software. Until 2015, Red Hat made the source code to its enterprise distribution publicly available through its FTP website, though the inclusion of Red Hat trademarks prevented direct redistribution of the software. In 2015, Red Hat began publishing de-branded source code via git repositories on git.centos.org. Several groups used the source code to compile their own derivatives, typically with changes including the removal of any references to Red Hat's trademarks and pointing the update systems to non-Red Hat servers. Groups which have undertaken this include AlmaLinux, CentOS, MIRACLE LINUX, Oracle Linux, CloudLinux OS, Rocky Linux, Scientific Linux, StartCom Enterprise Linux, Pie Box Enterprise Linux, X/OS, Lineox, and Bull's XBAS for high-performance computing.

In 2023, Red Hat replaced the process that published code to git.centos.org in favor of the CentOS Stream git repositories. As required by its open-source licenses, the code for branched releases remains available to customers and developers, but the customer contract allows Red Hat to drop any customer who provides third-parties with access to subscription services, discouraging them from publishing source code artifacts. This led to AlmaLinux, one of the RHEL derivative Linux distributions, moving away from "1:1 bug for bug" compatibility to "application binary interface (ABI) compatible", while Oracle, SUSE, and CIQ (the company behind Rocky Linux) collaborated to form the Open Enterprise Linux Association (OpenELA) in order to provide "open and free Enterprise Linux (EL) source code".

Derivatives of Red Hat Enterprise Linux are free but do not get any commercial support or consulting services from Red Hat and lack software, hardware or security certifications from Red Hat. They also do not get access to Red Hat services like Red Hat Network.

Unusually, Red Hat took steps to obfuscate their changes to the Linux kernel for RHEL 6.0 by not publicly providing the patch files for their changes in the source tarball, and only releasing the finished product in source form. Speculation suggested that the move was made to affect Oracle's competing rebuild and support services, which further modifies the distribution. This practice however, still complies with the GNU GPL since source code is defined as "[the] preferred form of the work for making modifications to it", and the distribution still complies with this definition. Red Hat's CTO Brian Stevens later confirmed the change, stating that certain information (such as patch information) would now only be provided to paying customers to make the Red Hat product more competitive against the growing number of companies offering support for products based on RHEL. CentOS developers had no objections to the change since they do not make any changes to the kernel beyond what is provided by Red Hat. Their competitor Oracle announced in November 2012 that they were releasing a *RedPatch* service, which allows public view of the RHEL kernel changes, broken down by patch.

A number of commercial vendors use Red Hat Enterprise Linux as a base for the operating system in their products. Two of the best known are the Console Operating System in VMware ESX Server and Oracle Linux.

## Version history and timeline

Source:

### Naming convention

Each release is given a codename which is selected by a vote of the developers. The codenames don't have a specific pattern (unlike Ubuntu or Debian).

### RHEL 10

Red Hat Enterprise Linux 10 beta was made available in December 2024.

RHEL 10 was officially announced on May 20, 2025 (2025-05-20), at the Red Hat Summit, and uses Linux kernel 6.12.0-55.9.1.el10_0. This release has the codename *Coughlan*.

- Red Hat Enterprise Linux 10.0, May 20, 2025 (2025-05-20), uses Linux kernel 6.12.0-55.9.1.el10_0
  - 10.1, November 12, 2025 (2025-11-12)
    - kernel 6.12.0-124.8.1.el10_1
  - 10.2, May 20, 2026 (2026-05-20)
    - kernel 6.12.0-211.16.1.el10_2

### RHEL 9

Red Hat Enterprise Linux 9 was announced at Red Hat Summit on May 10, 2022, and was officially released on May 17, 2022 (2022-05-17). In this version of the system introduced a Linux Kernel 5.14.0 and Gnome 40.

RHEL 9 was the first to be based on CentOS Stream, itself based on Fedora Linux, while historically RHEL was based directly on Fedora Linux.

The first beta for Red Hat Enterprise Linux 9 (*Plow*), based on Fedora Linux 34, was released on November 3, 2021.

Red Hat Enterprise Linux 9 (*Plow*) was released on May 18, 2022. The name *Plow* was the Appalachian Trail nickname for Tim Burke, one of the founders of RHEL and retired leader of RHEL engineering.

- Red Hat Enterprise Linux 9.0, May 17, 2022 (2022-05-17), uses Linux kernel 5.14.0-70.13.1.el9_0
  - 9.1, November 15, 2022 (2022-11-15)
    - kernel 5.14.0-162.6.1.el9_1
  - 9.2, May 10, 2023 (2023-05-10)
    - kernel 5.14.0-284.11.1.el9_2
  - 9.3, November 7, 2023 (2023-11-07)
    - kernel 5.14.0-362.8.1.el9_3
  - 9.4, April 30, 2024 (2024-04-30)
    - kernel 5.14.0-427.13.1.el9_4
  - 9.5, November 13, 2024 (2024-11-13)
    - kernel 5.14.0-503.11.1.el9_5
  - 9.6, May 20, 2025 (2025-05-20)
    - kernel 5.14.0-570.17.1.0.1.el9_6
  - 9.7, November 12, 2025 (2025-11-12)
    - kernel 5.14.0-611.5.1.el9_7
  - 9.8, May 20, 2026 (2026-05-20)
    - kernel 5.14.0-687.10.1.el9_8

### RHEL 8

Red Hat Enterprise Linux 8 (*Ootpa*) is based on Fedora 28, upstream Linux kernel 4.18, GCC 8.2, glibc 2.28, systemd 239, GNOME 3.28, and the switch to Wayland. The first beta was announced on November 14, 2018. Red Hat Enterprise Linux 8 was officially released on May 7, 2019 (2019-05-07).

With Release 8 of Red Hat Enterprise Linux, IBM has completed transition of POWER8 and POWER9 servers to little-endian mode.

The name *Ootpa* was a tribute to Larry Troan. His son, Eric Troan was Red Hat's first head engineer and his username was *ewt*, so his father was given the name *ewt's pa*, pronounced *Ootpa*.

- Red Hat Enterprise Linux 8.0, May 7, 2019 (2019-05-07), uses Linux kernel 4.18.0-80
  - 8.1, November 5, 2019 (2019-11-05), uses Linux kernel 4.18.0-147
    - GNOME rebased to 3.32
  - 8.2, April 28, 2020 (2020-04-28)
    - kernel 4.18.0-193
  - 8.3, November 3, 2020 (2020-11-03)
    - kernel 4.18.0-240
  - 8.4, May 18, 2021 (2021-05-18)
    - kernel 4.18.0-305
  - 8.5, November 9, 2021 (2021-11-09)
    - kernel 4.18.0-348
  - 8.6, May 10, 2022 (2022-05-10)
    - kernel 4.18.0-372.9.1
  - 8.7, November 9, 2022 (2022-11-09)
    - kernel 4.18.0-425.3.1
  - 8.8, May 16, 2023 (2023-05-16)
    - kernel 4.18.0-477.10.1.el8_8
  - 8.9, November 14, 2023 (2023-11-14)
    - kernel 4.18.0-513.5.1.el8_9
  - 8.10, May 22, 2024 (2024-05-22)
    - kernel 4.18.0-553.el8_10

### RHEL 7

Red Hat Enterprise Linux 7 (*Maipo*) is based on Fedora 18 and Fedora 19, upstream Linux kernel 3.10, systemd 208 (updated to 219 in RHEL 7.2), and GNOME 3.8 (rebased to GNOME 3.28 in RHEL 7.6) The first beta was announced on 11 December 2013, and a release candidate was made available on 15 April 2014. On June 10, 2014 (2014-06-10) Red Hat Enterprise Linux 7 was officially released.

- Red Hat Enterprise Linux 7.0 (*Maipo*), June 9, 2014 (2014-06-09), uses Linux kernel 3.10.0-123
  - 7.1, March 5, 2015 (2015-03-05)
    - kernel 3.10.0-229
  - 7.2, November 19, 2015 (2015-11-19)
    - kernel 3.10.0-327
    - systemd updated to 219
    - Fedora rebased to 21
    - GNOME rebased to 3.14
  - 7.3, November 3, 2016 (2016-11-03)
    - kernel 3.10.0-514
  - 7.4, July 18, 2017 (2017-07-18)
    - kernel 3.10.0-693
    - Fedora rebased to 25
    - GNOME rebased to 3.22
  - 7.5, April 10, 2018 (2018-04-10)
    - kernel 3.10.0-862
    - Fedora rebased to 27
    - GNOME rebased to 3.26
  - 7.6, October 30, 2018 (2018-10-30)
    - kernel 3.10.0-957
    - Fedora rebased to 28
    - GNOME rebased to 3.28
  - 7.7, August 6, 2019 (2019-08-06)
    - kernel 3.10.0-1062
    - GNOME remains as 3.28
  - 7.8, March 31, 2020 (2020-03-31)
    - kernel 3.10.0-1127
    - GNOME remains as 3.28
  - 7.9, September 29, 2020 (2020-09-29)
    - kernel 3.10.0-1160
  - 7, ***Extended Life-cycle Support*** (ELS) Start Date July 1, 2024 (2024-07-01)
    - aka added ELS entitlement until ELS end Date June 30, 2028 (2028-06-30)

### RHEL 6

Red Hat Enterprise Linux 6 was forked from Fedora 10 and contains many backported features from Fedora 11 and Fedora 12.

- Red Hat Enterprise Linux 6 (*Santiago*), November 9, 2010 (2010-11-09), uses Linux kernel 2.6.32-71
  - 6.1, May 19, 2011 (2011-05-19) (kernel 2.6.32-131.0.15)
  - 6.2, December 6, 2011 (2011-12-06) (kernel 2.6.32-220)
  - 6.3, June 20, 2012 (2012-06-20) (kernel 2.6.32-279)
  - 6.4, February 21, 2013 (2013-02-21) (kernel 2.6.32-358)
  - 6.5, November 21, 2013 (2013-11-21) (kernel 2.6.32-431)
  - 6.6, October 14, 2014 (2014-10-14) (kernel 2.6.32-504)
  - 6.7, July 22, 2015 (2015-07-22) (kernel 2.6.32-573)
  - 6.8, May 10, 2016 (2016-05-10) (kernel 2.6.32-642)
  - 6.9, March 21, 2017 (2017-03-21) (kernel 2.6.32-696)
  - 6.10, June 19, 2018 (2018-06-19) (kernel 2.6.32-754)
  - 6 ELS +, ***Extended Life-cycle Support*** (ELS) Start Date November 30, 2020 (2020-11-30)
    - aka added ELS entitlement until ELS end Date June 30, 2024 (2024-06-30)

### RHEL 5

Red Hat Enterprise Linux 5 has forked with Fedora Core 6.

- Red Hat Enterprise Linux 5 (*Tikanga*), March 15, 2007 (2007-03-15), uses Linux kernel 2.6.18-8
  - 5.1, November 7, 2007 (2007-11-07) (kernel 2.6.18-53)
  - 5.2, May 21, 2008 (2008-05-21) (kernel 2.6.18-92)
  - 5.3, January 20, 2009 (2009-01-20) (kernel 2.6.18-128)
  - 5.4, September 2, 2009 (2009-09-02) (kernel 2.6.18-164)
  - 5.5, March 30, 2010 (2010-03-30) (kernel 2.6.18-194)
  - 5.6, January 13, 2011 (2011-01-13) (kernel 2.6.18-238)
  - 5.7, July 21, 2011 (2011-07-21) (kernel 2.6.18-274)
  - 5.8, February 20, 2012 (2012-02-20) (kernel 2.6.18-308)
  - 5.9, January 7, 2013 (2013-01-07) (kernel 2.6.18-348)
  - 5.10, October 1, 2013 (2013-10-01) (kernel 2.6.18-371)
  - 5.11, September 16, 2014 (2014-09-16) (kernel 2.6.18-398)
  - 5.11+, ***Extended Life-cycle Support*** (ELS) Start Date March 31, 2017 (2017-03-31)
    - aka added ELS entitlement until ELS end Date November 30, 2020 (2020-11-30)

### RHEL 4

RHEL 4 introduced Linux kernel 2.6 versions and extended attributes on ext2 and ext3 file systems.

- Red Hat Enterprise Linux 4 (*Nahant*), February 15, 2005 (2005-02-15), uses Linux kernel 2.6.9-5
  - Update 1, June 8, 2005 (2005-06-08) (kernel 2.6.9-11)
  - Update 2, October 5, 2005 (2005-10-05) (kernel 2.6.9-22)
  - Update 3, March 12, 2006 (2006-03-12) (kernel 2.6.9-34)
  - Update 4, August 10, 2006 (2006-08-10) (kernel 2.6.9-42)
  - Update 5, May 1, 2007 (2007-05-01) (kernel 2.6.9-55)
  - Update 6, November 15, 2007 (2007-11-15) (kernel 2.6.9-67)
  - Update 7, July 29, 2008 (2008-07-29) (kernel 2.6.9-78)
  - Update 8, May 19, 2009 (2009-05-19) (kernel 2.6.9-89)
  - Update 9, February 16, 2011 (2011-02-16) (kernel 2.6.9-100)

### RHEL 3

- Red Hat Enterprise Linux 3 (*Taroon*), October 22, 2003 (2003-10-22), uses Linux kernel 2.4.21-4
  - Update 1, January 16, 2004 (2004-01-16) (kernel 2.4.21-9)
  - Update 2, May 12, 2004 (2004-05-12) (kernel 2.4.21-15)
  - Update 3, September 3, 2004 (2004-09-03) (kernel 2.4.21-20)
  - Update 4, December 12, 2004 (2004-12-12) (kernel 2.4.21-27)
  - Update 5, May 18, 2005 (2005-05-18) (kernel 2.4.21-32)
  - Update 6, September 28, 2005 (2005-09-28) (kernel 2.4.21-37)
  - Update 7, March 17, 2006 (2006-03-17) (kernel 2.4.21-40)
  - Update 8, July 20, 2006 (2006-07-20) (kernel 2.4.21-47)
  - Update 9, June 20, 2007 (2007-06-20) (kernel 2.4.21-50)

### RHEL 2.1

- Red Hat Enterprise Linux 2.1 AS (*Pensacola*), March 23, 2002 (2002-03-23), uses Linux kernel 2.4.9-e.3
  - Update 1, February 14, 2003 (2003-02-14) (kernel 2.4.9-e.12)
  - Update 2, March 29, 2003 (2003-03-29) (kernel 2.4.9-e.24)
  - Update 3, December 19, 2003 (2003-12-19) (kernel 2.4.9-e.34)
  - Update 4, April 21, 2004 (2004-04-21) (kernel 2.4.9-e.40)
  - Update 5, August 18, 2004 (2004-08-18) (kernel 2.4.9-e.49)
  - Update 6, December 13, 2004 (2004-12-13) (kernel 2.4.9-e.57)
  - Update 7, April 28, 2005 (2005-04-28)
- Red Hat Enterprise Linux 2.1 ES (*Panama*), May 2003

## Product life cycle

The life cycle of Red Hat Enterprise Linux is at least seven years for versions 3 and 4, and spans at least 10 years for versions 5, 6, 7, 8 and 9. The life cycle comprises several phases of varying length with different degrees of support. During the first phase ("Production 1"), Red Hat provides full support and updates software and hardware drivers. In later phases ("Production 2" and "Production 3"), only security and other important fixes are provided and support for new hardware is gradually reduced.

In the last years of the support lifecycle (after seven years for version 4 and earlier, and after 10 years for version 5 and later), critical and security-related fixes are only provided to customers who pay an additional subscription ("Extended Lifecycle Support Add-On"), which is available until the End of Extended Lifecycle Support date for each version as shown in the table below. This covers a limited number of packages. Red Hat only supports major version upgrades from version n to version n+1.

| RHEL version | Last minor release | Release date | End of Full Support | End of Maintenance Support 1 (RHEL 5, 6, 7) | End of Maintenance Support (RHEL 8, 9, 10), Maintenance Support 2 (RHEL 5, 6, 7) (product retirement) | End of Extended Lifecycle Support |
|---|---|---|---|---|---|---|
| Unsupported: 2.1 | U-7 | 26 March 2002 (AS) 1 May 2003 (ES) | 30 November 2004 | 31 May 2005 | 31 May 2009 | —N/a |
| Unsupported: 3 | U-9 | 23 October 2003 | 20 July 2006 | 30 June 2007 | 31 October 2010 | 30 January 2014 |
| Unsupported: 4 | U-9 | 14 February 2005 | 31 March 2009 | 16 February 2011 | 29 February 2012 | 31 March 2017 |
| Unsupported: 5 | 5.11 | 15 March 2007 | 8 January 2013 | 31 January 2014 | 31 March 2017 | 30 November 2020 |
| Unsupported: 6 | 6.10 | 10 November 2010 | 10 May 2016 | 10 May 2017 | 30 November 2020 | 30 June 2024 |
| Supported: 7 | 7.9 | 10 June 2014 | 6 August 2019 | 6 August 2020 | 30 June 2024 | 31 May 2029 |
| Supported: 8 | 8.10 | 7 May 2019 | May 2024 | —N/a | May 2029 | 31 May 2031 |
| Supported: 9 | 9.8 | 08 Nov 2022 | May 2027 | —N/a | May 2032 | 31 May 2034 |
| Latest version: 10 | 10.2 | 13 May 2025 | May 2030 | —N/a | May 2035 | 31 May 2037 |
| **Legend:**UnsupportedSupported**Latest version**Preview versionFuture version |   |   |   |   |   |   |

### Kernel backporting

To maintain a stable application binary interface (ABI), Red Hat does not update the kernel version, but instead backports new features to the same kernel version with which a particular version of RHEL has been released. New features are backported throughout the Production 1 phase of the RHEL lifecycle. Consequently, RHEL may use a Linux kernel with a dated version number, yet the kernel is up-to-date regarding not only security fixes, but also certain features. One specific example is the SO_REUSEPORT socket option which was added to Linux kernel 3.9, and was subsequently backported and became available since RHEL 6.5, which uses version 2.6.32 of the Linux kernel.

## Extended Update Support (EUS) / Z Tree

The Extended Update Support (EUS) allows an organization / company to choose when they change to a new minor version. For the first 6 months of the EUS channel / yum repo, features may be added, but then the channel is locked down so that only bug and security fixes are patched. The organization / company then has 24 months to move to a new EUS branch. EUS allows the organization / company to stay on a minor version if required by a third-party application which is only tested with a particular minor version of RHEL, such as Oracle Database, IBM Db2, IBM Cloud Orchestrator, Hortonworks. There may also be extra costs associated with using the EUS repos/channels depending on the agreement the organization / company has with Red Hat. For more information on what is Included/Excluded from the EUS see.

### Note

- The EUS update mechanism for using older minor version branches is not available to CentOS, Oracle Linux and Scientific Linux, as Red Hat do not publish source packages for rebuilding. As such, projects clearly state to ensure users run on the latest available minor version within a supported major release.

### Updates

In general one can move from z streams to the next version of the z stream.

- The 7.4.z EUS channel after the release of 7.4.
- The 7.5.z EUS channel after the release of 7.5.

Any 7.y.z EUS channel where y is greater than 1. The standard base channel for Red Hat Enterprise Linux 7, which is the most recent minor release aka rhel 7Y where y is the latest greatest.

One can not go back in time, aka 7.5.z to 7.4.z and will NOT be supported.

### RHEL 6

Red Hat Enterprise Linux 6 was forked from Fedora 12 and contains many backported features from Fedora 13 and 14.

- Red Hat Enterprise Linux 6 (*Santiago*), 10 November 2010, uses Linux kernel 2.6.32-71
  - 6.7, also termed Update 7, July 22, 2015 (2015-07-22) (kernel 2.6.32-573)
    - 1st Day of EUS Window July 22, 2015 (2015-07-22)
    - Last Day of EUS Window July 31, 2017 (2017-07-31)
  - Note: There were no more EUS for Rhel6 after 6.7

### RHEL 7

Red Hat Enterprise Linux 7 (*Maipo*) is based on Fedora 19, upstream Linux kernel 3.10, 10 June 2014, uses Linux kernel 3.10.0-123

- 7.1, also termed Update 1, March 5, 2015 (2015-03-05) (kernel 3.10.0-229)
  - 1st Day of EUS Window March 5, 2015 (2015-03-05)
  - Last Day of EUS Window March 31, 2017 (2017-03-31)
- 7.2, also termed Update 2, November 19, 2015 (2015-11-19) (kernel 3.10.0-327)
  - 1st Day of EUS Window November 19, 2015 (2015-11-19)
  - Last Day of EUS Window November 30, 2017 (2017-11-30)
- 7.3, also termed Update 3, November 3, 2016 (2016-11-03) (kernel 3.10.0-514)
  - 1st Day of EUS Window November 3, 2016 (2016-11-03)
  - Last Day of EUS Window November 30, 2018 (2018-11-30)
  - Features may be updated
- 7.4, also termed Update 4, August 1, 2017 (2017-08-01) (kernel 3.10.0-693)
  - 1st Day of EUS Window August 1, 2017 (2017-08-01)
  - Last Day of EUS Window August 31, 2019 (2019-08-31)
- 7.5, also termed Update 5, April 10, 2018 (2018-04-10) (kernel 3.10.0-862)
  - 1st Day of EUS Window April 10, 2018 (2018-04-10)
  - Last Day of EUS Window April 30, 2020 (2020-04-30)
- 7.6, also termed Update 6, October 30, 2018 (2018-10-30) (kernel 3.10.0-957)
  - 1st Day of EUS Window October 30, 2018 (2018-10-30)
  - Last Day of EUS Window May 31, 2021 (2021-05-31)
- 7.7, also termed Update 7, August 6, 2019 (2019-08-06) (kernel 3.10.0-1062)
  - 1st Day of EUS Window August 6, 2019 (2019-08-06)
  - Last Day of EUS Window August 30, 2021 (2021-08-30)
- 7.8, also termed Update 8
  - Released on March 31, 2020 (2020-03-31)
- 7.9, also termed Update 9 is the final RHEL 7 release
  - Released on September 30, 2020 (2020-09-30)

### RHEL 8

Red Hat Enterprise Linux 8 (*Ootpa*) is based on Fedora 28, upstream Linux kernel 4.18, systemd 239, and GNOME 3.28. The first beta was announced on November 14, 2018. Red Hat Enterprise Linux 8 was officially released on May 7, 2019.

For RHEL 8, the update schedule is approximately:

- 8.0 - 6 Month Minor Release (kernel 4.18.0-80)
  - 1st Day of Support Window May 7, 2019 (2019-05-07)
- 8.1 - 6 Month Minor Release with Extended Support and Update Services for SAP Solutions (kernel 4.18.0-147)
  - 1st Day of Support Window November 5, 2019 (2019-11-05)
- 8.2 - 6 Month Minor Release with Extended Support and Update Services for SAP Solutions (kernel 4.18.0-193)
  - 1st Day of Support Window April 28, 2020 (2020-04-28)
- 8.3 - 6 Month Minor Release (kernel 4.18.0-240)
  - 1st Day of Support Window November 3, 2020 (2020-11-03)
- 8.4 - 6 Month Minor Release with Extended Support and Update Services for SAP Solutions (kernel 4.18.0-305)
  - 1st Day of Support Window May 18, 2021 (2021-05-18)
- 8.5 - 6 Month Minor Release (kernel 4.18.0-348)
  - 1st Day of Support Window November 9, 2021 (2021-11-09)
- 8.6 - 6 Month Minor Release with Extended Support and Update Services for SAP Solutions (kernel 4.18.0-372.9.1)
  - 1st Day of Support Window May 10, 2022 (2022-05-10)
- 8.7 - 6 Month Minor Release (kernel 4.18.0-425.3.1)
  - 1st Day of Support Window November 9, 2022 (2022-11-09)
- 8.8 - 6 Month Minor Release with Extended Support and Update Services for SAP Solutions (kernel 4.18.0-477.10.1.el8_8)
  - 1st Day of Support Window May 16, 2023 (2023-05-16)

#### RHEL 8 application streams

In addition to normal OS updates, RHEL 8 also maintains application streams to allow for certain applications to be supported and updated independent of the base OS and to match the maintenance stream of the application vendor. Each application stream will be supported from two to five years with new versions only available during the Red Hat Enterprise Linux Full Support Phase. These apps should be expected to be updated frequently with shorter lifecycles than the base OS packages.

Packages currently offered as streams

- authd 1.4.4 (through May 2021)
- container-tools 1 (through May 2021)
- dotnet 2.1 (through Aug 2021)
- git 2.18 (through May 2021)
- httpd 2.4 (through May 2024)
- Identity Management DL1 (through May 2024)
- mariadb 10.3 (through May 2023)
- maven 3.5 (through May 2022)
- mercurial 4.8 (through May 2022)
- mysql 8 (through Apr 2023)
- nginx 1.14 (through May 2021)
- nodejs 10 (through Apr 2021)
- openjdk 1.8.0 (through Jun 2023)
- openjdk 11 (through Oct 2024)
- perl 5.24 (through May 2021)
- php 7.2 (through May 2021)
- postgresql 10 (through May 2024)
- postgresql 9.6 (through Nov 2021)
- python 2.7 (through Jun 2024)
- redis 5 (through May 2022)
- ruby 2.5 (through Feb 2021)
- scala 2.1 (through May 2022)
- swig 3 (through May 2022)
- varnish 6 (through May 2022)

### RHEL 9

**Red Hat Enterprise Linux 9** (RHEL 9) is a commercial open-source operating system developed by Red Hat for enterprise environments. It is built from the open-source Fedora distribution and aims to provide a stable, secure, and enterprise-grade platform. RHEL 9, released in May 2022, introduces several new features and improvements, especially tailored for cloud-native development, security, automation, and performance enhancements.

#### Key features

1. **Kernel and Performance** RHEL 9 is based on the Linux kernel 5.14, offering improved performance and hardware support. It also features enhanced performance tuning tools for administrators to optimize workloads on modern architectures.
2. **Security Enhancements** RHEL 9 includes advanced security measures such as the Integrity Measurement Architecture (IMA), which ensures system integrity. It also incorporates OpenSSL 3.0 for updated cryptography and enhanced security policies. By default, SSH root password login is disabled to encourage the use of key-based authentication. SELinux continues to play a crucial role in enforcing strict security policies.
3. **Automation and Management** The integration with Ansible allows for more streamlined automation and configuration management across systems. The Cockpit web console has also been improved, offering new features for managing containers, networking, and storage.
4. **Cloud and Container Support** RHEL 9 is designed for cloud-native environments, with strong support for containers and hybrid cloud infrastructures. It is optimized to work seamlessly with Red Hat OpenShift, a Kubernetes-based platform, and supports containerization through tools like Podman. It also includes AppStreams, which provide curated packages for developers, ensuring access to the latest runtimes and frameworks.
5. **Networking and Storage** Enhanced NetworkManager features and support for NVMe over Fabrics improve performance and scalability for modern networking and storage configurations.

#### Use cases

RHEL 9 is suitable for a wide range of enterprise applications across industries such as financial services, healthcare, and government. It is used in both on-premises and cloud environments, with strong support for multi-cloud and hybrid cloud deployments

#### Support lifecycle

RHEL 9 follows Red Hat's 10-year support lifecycle, which includes full support for the first five years, followed by maintenance support for the remaining five years.
