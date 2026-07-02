---
title: "CentOS"
source: https://en.wikipedia.org/wiki/CentOS
domain: red-hat-linux
license: CC-BY-SA-4.0
tags: red hat enterprise linux, yum package manager, dnf tool, centos rebuild
fetched: 2026-07-02
---

# CentOS

**CentOS** (/ˈsɛntɒs/, from **Community Enterprise Operating System**; also known as **CentOS Linux**) is a discontinued Linux distribution that provided a free and open-source community-supported computing platform, functionally compatible with its upstream source, Red Hat Enterprise Linux (RHEL). In January 2014, CentOS announced the official joining with Red Hat while staying independent from RHEL, under a new CentOS governing board.

The first CentOS release in May 2004, numbered as CentOS version 2, was forked from RHEL version 2.1AS. Since version 8, CentOS officially supports the x86-64, ARM64, and POWER8 architectures, and releases up to version 6 also supported the IA-32 architecture. As of December 2015, AltArch releases of CentOS 7 are available for the IA-32 architecture, Power ISA, and for the ARMv7hl and AArch64 variants of the ARM architecture. CentOS 8 was released on 24 September 2019.

In December 2020, Red Hat unilaterally terminated CentOS development in favor of CentOS Stream 9, a distribution positioned upstream of RHEL. In March 2021, CloudLinux (makers of CloudLinux OS) released a RHEL derivative called AlmaLinux. Later in May 2021, one of the CentOS founders (Gregory Kurtzer) created the competing Rocky Linux project as a successor to the original mission of CentOS.

## History

CentOS originated as a build of **CAOS Linux**, an RPM-based Linux distribution started by Gregory Kurtzer in 2002. Infiscale described its GravityOS as "[including] the small footprint of Caos", indicating a certain level of influence from the discontinued distribution.

In June 2006, David Parsley, the primary developer of Tao Linux (another RHEL clone), announced the retirement of Tao Linux and its rolling into CentOS development. Tao users migrated to the CentOS release via yum update.

In July 2009, it was reported in an open letter on the CentOS Project web site that one of CentOS's founders, Lance Davis, had disappeared in 2008. Davis had ceased contribution to the project, but continued to hold the registration for the CentOS domain and PayPal account. In August 2009, the CentOS team reportedly made contact with Davis and obtained the centos.info and centos.org domains.

In July 2010, CentOS overtook Debian to become the most popular Linux distribution for web servers, with almost 30% of all Linux web servers using it. Debian retook the lead in January 2012.

In January 2014, Red Hat announced that it would sponsor the CentOS Project, "helping to establish a platform well-suited to the needs of open source developers that integrate technologies in and around the operating system". As a result of these changes, ownership of CentOS trademarks was transferred to Red Hat, which now employs most of the CentOS head developers; however, they work as part of Red Hat's Open Source and Standards team, which operates separately from the Red Hat Enterprise Linux team. A new CentOS governing board was also established.

On 8 December 2020, the CentOS Project announced that the distribution would be discontinued at the end of 2021 in order to focus on CentOS Stream. The community's response to this announcement was overwhelmingly negative. Soon thereafter, Gregory Kurtzer (one of CentOS's founders) announced a new project to continue the original CentOS focus, which became known as Rocky Linux. CloudLinux created AlmaLinux to provide a community-supported successor to CentOS Linux, aiming for binary-compatibility with the current version of RHEL. A beta version of AlmaLinux was first released on February 1, 2021, and the first stable release of AlmaLinux was published on March 30, 2021. A beta version of Rocky Linux was released on April 30, 2021, and subsequently on June 21, 2021, the stable release of Rocky Linux 8.4 was released.

Following CentOS 7's end-of-life in June 2024, several commercial vendors began offering extended security support for organisations unable to migrate immediately. These include TuxCare's Extended Lifecycle Support, CloudLinux's ELS service, and MontaVista's MVShield, which provides continued CVE patching and technical support for CentOS 7.9 through at least 2029.

## Design

CentOS developers use Red Hat's source code to create a final product very similar to RHEL. Red Hat's branding and logos are changed because Red Hat does not allow them to be redistributed. CentOS is available free of charge. Technical support is primarily provided by the community via official mailing lists, web forums, and chat rooms.

The project is affiliated with Red Hat but aspires to be more public, open, and inclusive. While Red Hat employs most of the CentOS head developers, the CentOS Project itself relies on donations from users and organizational sponsors.

## Versioning and releases

### CentOS releases

CentOS version numbers for releases older than 7.0 have two parts, a major version and a minor version, which correspond to the major version and update set of Red Hat Enterprise Linux (RHEL) used to build a particular CentOS release. For example, CentOS 6.5 is built from the source packages of RHEL 6 update 5 (also known as RHEL version 6.5), which is a so-called "point release" of RHEL 6.

Starting with version 7.0, CentOS version numbers also include a third part that indicates the monthstamp of the source code the release is based on. For example, version number 7.0-1406 still maps this CentOS release to the zeroth update set of RHEL 7, while "1406" indicates that the source code this release is based on dates from June 2014. Using the monthstamp allows installation images to be reissued for (as of July 2014) oncoming container and cloud releases, while maintaining a connection to the related base release version.

Since mid-2006 and starting with RHEL version 4.4, which is formally known as Red Hat Enterprise Linux 4.0 update 4, Red Hat has adopted a version-naming convention identical to that used by CentOS (for example, RHEL 4.5 or RHEL 6.5).

On 10 September 2019 CentOS deferred CentOS 8.1 work for CentOS 7.7 since CentOS 7.x was in production and CentOS 8.x was not in production. Once CentOS 7.7 was released resources moved back to CentOS 8.0.

On 24 September 2019 CentOS officially released CentOS version 8.0. Since CentOS was discontinued at the end of 2021, its final release was version 8.5 (2021-11-16). In contrast, its RHEL counterpart continued to version 8.10 (as of 2024-09).

#### End-of-support schedule

According to the Red Hat Enterprise Linux (RHEL) life cycle, CentOS 5, 6 and 7 will be "maintained for up to 10 years" as it is based on RHEL. Previously, CentOS 4 had been supported for seven years.

| CentOS version | Release date | Full updates | Maintenance updates |
|---|---|---|---|
| 3 | 2004-03-19 | 2006-07-20 | 2010-10-31 |
| 4 | 2005-03-09 | 2009-03-31 | 2012-02-29 |
| 5 | 2007-04-12 | 2014-01-31 | 2017-03-31 |
| 6 | 2011-11-27 | 2017-05-10 | 2020-11-30 |
| 7 | 2014-07-07 | 2020-08-06 | 2024-06-30 |
| 8 | 2019-09-24 | 2021-12-31 |   |

#### Older version information

| CentOS version | Architectures | RHEL base | Kernel | CentOS release date | RHEL release date | Delay (days) |
|---|---|---|---|---|---|---|
| 2.1 | IA-32 | 2.1 | 2.4.9 | 2004-05-14 | 2002-05-17 | 728 |
| 3.1 | IA-32, x86-64, IA-64, s390, s390x | 3.1 | 2.4.21-15 | 2004-03-19 | 2003-10-23 | 148 |
| 3.3 | IA-32, x86-64, IA-64, s390, s390x | 3.3 | 2.4.21-20 | 2004-09-17 | 2004-09-03 | 14 |
| 3.4 | IA-32, x86-64, IA-64, s390, s390x | 3.4 | 2.4.21-27 | 2005-01-23 | 2004-12-12 | 42 |
| 3.5 | IA-32 | 3.5 | 2.4.21-32 | 2005-06-10 | 2005-05-18 | 23 |
| 3.6 | IA-32 | 3.6 | 2.4.21-37 | 2005-11-01 | 2005-09-28 | 34 |
| 3.7 | IA-32, x86-64, IA-64, s390, s390x | 3.7 | 2.4.21-40 | 2006-04-10 | 2006-03-17 | 23 |
| 3.8 | IA-32, x86-64 | 3.8 | 2.4.21-47 | 2006-08-25 | 2006-07-20 | 36 |
| 3.9 | IA-32, x86-64, IA-64, s390, s390x | 3.9 | 2.4.21-50 | 2007-07-26 | 2007-06-15 | 41 |
| 4.0 | IA-32, x86-64, various | 4.0 | 2.6.9-5 | 2005-03-09 | 2005-02-14 | 23 |
| 4.1 | IA-32, IA-64, s390 | 4.1 | 2.6.9-11 | 2005-06-12 | 2005-06-08 | 4 |
| 4.2 | IA-32, x86-64, IA-64, s390, s390x, alpha | 4.2 | 2.6.9-22 | 2005-10-13 | 2005-10-05 | 8 |
| 4.3 | IA-32, x86-64, IA-64, s390, s390x | 4.3 | 2.6.9-34 | 2006-03-21 | 2006-03-12 | 9 |
| 4.4 | IA-32, x86-64 | 4.4 | 2.6.9-42 | 2006-08-30 | 2006-08-10 | 20 |
| 4.5 | IA-32, x86-64, IA-64 | 4.5 | 2.6.9-55 | 2007-05-17 | 2007-05-01 | 16 |
| 4.6 | IA-32, x86-64, IA-64, Alpha, s390, s390x, PowerPC (beta), SPARC (beta) | 4.6 | 2.6.9-67 | 2007-12-16 | 2007-11-16 | 30 |
| 4.7 | IA-32, x86-64 | 4.7 | 2.6.9-78 | 2008-09-13 | 2008-07-24 | 51 |
| 4.8 | IA-32, x86-64 | 4.8 | 2.6.9-89 | 2009-08-21 | 2009-05-18 | 95 |
| 4.9 | IA-32, x86-64 | 4.9 | 2.6.9-100 | 2011-03-02 | 2011-02-16 | 14 |
| 5.0 | IA-32, x86-64 | 5.0 | 2.6.18-8 | 2007-04-12 | 2007-03-14 | 28 |
| 5.1 | IA-32, x86-64 | 5.1 | 2.6.18-53 | 2007-12-02 | 2007-11-07 | 25 |
| 5.2 | IA-32, x86-64 | 5.2 | 2.6.18-92 | 2008-06-24 | 2008-05-21 | 34 |
| 5.3 | IA-32, x86-64 | 5.3 | 2.6.18-128 | 2009-03-31 | 2009-01-20 | 69 |
| 5.4 | IA-32, x86-64 | 5.4 | 2.6.18-164 | 2009-10-21 | 2009-09-02 | 49 |
| 5.5 | IA-32, x86-64 | 5.5 | 2.6.18-194 | 2010-05-14 | 2010-03-31 | 44 |
| 5.6 | IA-32, x86-64 | 5.6 | 2.6.18-238 | 2011-04-08 | 2011-01-13 | 85 |
| 5.7 | IA-32, x86-64 | 5.7 | 2.6.18-274 | 2011-09-13 | 2011-07-21 | 54 |
| 5.8 | IA-32, x86-64 | 5.8 | 2.6.18-308 | 2012-03-07 | 2012-02-21 | 15 |
| 5.9 | IA-32, x86-64 | 5.9 | 2.6.18-348 | 2013-01-17 | 2013-01-07 | 10 |
| 5.10 | IA-32, x86-64 | 5.10 | 2.6.18-371 | 2013-10-19 | 2013-09-30 | 19 |
| 5.11 | IA-32, x86-64 | 5.11 | 2.6.18-398 | 2014-09-30 | 2014-09-16 | 14 |
| 6.0 | IA-32, x86-64 | 6.0 | 2.6.32-71 | 2011-07-10 | 2010-11-10 | 242 |
| 6.1 | IA-32, x86-64 | 6.1 | 2.6.32-131 | 2011-12-09 | 2011-05-19 | 204 |
| 6.2 | IA-32, x86-64 | 6.2 | 2.6.32-220 | 2011-12-20 | 2011-12-06 | 14 |
| 6.3 | IA-32, x86-64 | 6.3 | 2.6.32-279 | 2012-07-09 | 2012-06-21 | 18 |
| 6.4 | IA-32, x86-64 | 6.4 | 2.6.32-358 | 2013-03-09 | 2013-02-21 | 15 |
| 6.5 | IA-32, x86-64 | 6.5 | 2.6.32-431 | 2013-12-01 | 2013-11-21 | 10 |
| 6.6 | IA-32, x86-64 | 6.6 | 2.6.32-504 | 2014-10-28 | 2014-10-14 | 14 |
| 6.7 | IA-32, x86-64 | 6.7 | 2.6.32-573 | 2015-08-07 | 2015-07-22 | 16 |
| 6.8 | IA-32, x86-64 | 6.8 | 2.6.32-642 | 2016-05-25 | 2016-05-10 | 15 |
| 6.9 | IA-32, x86-64 | 6.9 | 2.6.32-696 | 2017-04-05 | 2017-03-21 | 15 |
| 6.10 | IA-32, x86-64 | 6.10 | 2.6.32-754 | 2018-07-03 | 2018-06-19 | 14 |

##### CentOS version 7

| CentOS version | Architectures | RHEL base | Kernel | CentOS release date | RHEL release date | Delay (days) |
|---|---|---|---|---|---|---|
| 7.0-1406 | x86-64 | 7.0 | 3.10.0-123 | 2014-07-07 | 2014-06-10 | 27 |
| 7.1-1503 | x86-64 | 7.1 | 3.10.0-229 | 2015-03-31 | 2015-03-05 | 26 |
| 7.2-1511 | x86-64 | 7.2 | 3.10.0-327 | 2015-12-14 | 2015-11-19 | 25 |
| 7.3-1611 | x86-64 | 7.3 | 3.10.0-514 | 2016-12-12 | 2016-11-03 | 39 |
| 7.4-1708 | x86-64 | 7.4 | 3.10.0-693 | 2017-09-13 | 2017-07-31 | 43 |
| 7.5-1804 | x86-64 | 7.5 | 3.10.0-862 | 2018-05-10 | 2018-04-10 | 31 |
| 7.6-1810 | x86-64 | 7.6 | 3.10.0-957 | 2018-12-03 | 2018-10-30 | 34 |
| 7.7-1908 | x86-64 | 7.7 | 3.10.0-1062 | 2019-09-17 | 2019-08-06 | 42 |
| 7.8-2003 | x86-64 | 7.8 | 3.10.0-1127 | 2020-04-27 | 2020-03-30 | 28 |
| 7.9-2009 | x86-64 | 7.9 | 3.10.0-1160 | 2020-11-12 | 2020-09-29 | 44 |

#### Latest version information

##### CentOS version 8

| CentOS version | Architectures | RHEL base | Kernel | CentOS release date | RHEL release date | Delay (days) |
|---|---|---|---|---|---|---|
| 8.0-1905 | x86-64, ppc64le, AArch64 | 8.0 | 4.18.0-80 | 2019-09-24 | 2019-05-07 | 140 |
| 8.1-1911 | 8.1 | 4.18.0-147 | 2020-01-15 | 2019-11-05 | 71 |   |
| 8.2-2004 | 8.2 | 4.18.0-193 | 2020-06-15 | 2020-04-28 | 48 |   |
| 8.3-2011 | 8.3 | 4.18.0-240 | 2020-12-07 | 2020-11-03 | 34 |   |
| 8.4-2105 | 8.4 | 4.18.0-305 | 2021-06-03 | 2021-05-18 | 16 |   |
| 8.5-2111 | 8.5 | 4.18.0-348 | 2021-11-16 | 2021-11-09 | 7 |   |

### AltArch releases

AltArch releases are released by the Alternative Architecture Special Interest Group (AltArch SIG) to support architectures that are not supported by the base CentOS releases.

| CentOS version | Architectures | RHEL base | CentOS release date |
|---|---|---|---|
| 7.1-1503 | AArch64 | 7.1 | 2015-08-04 |
| IA-32 | 2015-10-12 |   |   |
| 7.2-1511 | IA-32 | 7.2 | 2015-12-19 |
| ARMv7hl | 2015-12-19 |   |   |
| PowerPC64 (TechPreview) | 2015-12-19 |   |   |
| POWER8 (le) (TechPreview) | 2015-12-19 |   |   |
| 7.3-1611 | ARMv7hl | 7.3 | 2016-12-14 |
| POWER8 (le) | 2016-12-22 |   |   |
| AArch64 | 2017-01-04 |   |   |
| IA-32 | 2017-01-27 |   |   |
| 7.4-1708 | ARMv7hl | 7.4 | 2017-09-13 |
| POWER8 (le) | 2017-09-14 |   |   |
| POWER7 | 2017-09-14 |   |   |
| AArch64 | 2017-09-13 |   |   |
| IA-32 | 2017-10-12 |   |   |
| 7.5-1804 | ARMv7hl | 7.5 | 2018-05-10 |
| POWER8 LE | 2018-05-10 |   |   |
| POWER7 | 2018-05-10 |   |   |
| AArch64 | 2018-05-10 |   |   |
| IA-32 | 2018-05-10 |   |   |
| 7.6-1810 | ARMv7hl | 7.6 | 2018-12-03 |
| POWER8 (le) | 2018-12-03 |   |   |
| PowerPC9 | 2018-12-03 |   |   |
| AArch64 | 2018-12-03 |   |   |
| IA-32 | 2018-12-03 |   |   |
| 7.7-1908 | ARMv7hl | 7.7 | 2019-09-17 |
| POWER7 | 2019-09-17 |   |   |
| POWER8 (le) | 2019-09-17 |   |   |
| POWER9 | 2019-09-17 |   |   |
| AArch64 | 2019-09-17 |   |   |
| IA-32 | 2019-09-17 |   |   |

### Add-ons releases

Software Collections (SCL) is a CentOS repository that provides a set of programming languages, database servers, and various related packages. Provided software versions are either more recent than their equivalent versions included in the base CentOS distribution, or are made available as official CentOS packages for the first time. (See also the list of CentOS repositories below.)

Packages available from the SCL do not replace the default system tools provided with CentOS. Instead, a parallel set of tools is installed in the /opt directory, and can be optionally enabled per application by using supplied scl utility. For example, the default versions of Perl or MySQL remain those provided by the base CentOS installation.

| Add-on name | Architectures | Base CentOS version | CentOS release date | RHEL release date | Delay (days) |
|---|---|---|---|---|---|
| Software Collections (SCL) 1.0 | x86-64 | 6.4, 6.5 | 2014-02-19 | 2013-09-12 | 160 |
| Developer Toolset 2.0 | IA-32, x86-64 | 6.4 | —N/a | 2013-09-12 | —N/a |

### Releases without upstream equivalents

Some of the ISO images released by the CentOS Project have no direct upstream equivalents. They are created for specific purposes, such as for providing a live bootable image, or for providing a reduced-size installation medium. In addition to those listed below, there are also AltArch releases, which also have no direct upstream equivalents.

LiveCD and LiveDVD images contain a bootable compressed file system, created by a set of custom scripts using a kickstart configuration file. These live images can be also installed to hard disk, thus obtaining a fully functional CentOS installation. The set of packages installed that way on a hard disk can not be adjusted during the installation, as that is a simple transfer of the image existing on CD/DVD, to a hard disk. After booting from hard disk, yum can be used for adding or removing packages.

MinimalCD images contain a minimum of packages required for a functional installation, with no compromises in security or network usability. These minimal images use the standard CentOS installer with all of its regular features minus the selection of packages. Yum can be used after the installation is completed to add or remove packages.

| CentOS version | Release name | Architectures | RHEL base | CentOS release date |
|---|---|---|---|---|
| 4.7 | Server | IA-32, x86-64 | 4.7 | 2008-10-17 |
| 5.1 | Live CD | IA-32 | 5.1 | 2008-02-18 |
| 5.2 | Live CD | IA-32 | 5.2 | 2008-07-17 |
| 5.3 | Live CD | IA-32 | 5.3 | 2009-05-27 |
| 5.5 | Live CD | IA-32, x86-64 | 5.5 | 2010-05-14 |
| 5.6 | Live CD | IA-32, x86-64 | 5.6 | 2011-04-08 |
| 6.0 | Live CD | IA-32, x86-64 | 6.0 | 2011-07-25 |
| Live DVD | 2011-07-27 |   |   |   |
| Minimal CD | 2011-07-28 |   |   |   |
| 6.1 | Live CD | IA-32, x86-64 | 6.1 | 2011-12-09 |
| Live DVD | 2011-12-09 |   |   |   |
| Minimal CD | 2011-12-09 |   |   |   |
| 6.2 | Live CD | IA-32, x86-64 | 6.2 | 2011-12-20 |
| Live DVD | 2011-12-20 |   |   |   |
| Minimal CD | 2011-12-20 |   |   |   |
| 6.3 | Minimal CD | IA-32, x86-64 | 6.3 | 2012-07-09 |
| Live CD | 2012-07-15 |   |   |   |
| Live DVD | 2012-07-15 |   |   |   |
| 6.4 | Minimal CD | IA-32, x86-64 | 6.4 | 2013-03-09 |
| Live CD | 2013-05-22 |   |   |   |
| Live DVD | 2013-05-22 |   |   |   |
| 6.5 | Minimal CD | IA-32, x86-64 | 6.5 | 2013-12-01 |
| Live CD | 2013-12-01 |   |   |   |
| Live DVD | 2013-12-01 |   |   |   |
| 6.6 | Minimal CD | IA-32, x86-64 | 6.6 | 2014-10-28 |
| 6.7 | Minimal CD | IA-32, x86-64 | 6.7 | 2015-08-07 |
| Live CD | 2015-08-11 |   |   |   |
| Live DVD | 2013-08-11 |   |   |   |
| 6.8 | Minimal CD | IA-32, x86-64 | 6.8 | 2016-05-25 |
| Live CD | 2016-05-25 |   |   |   |
| Live DVD | 2016-05-25 |   |   |   |
| 6.9 | Minimal CD | IA-32, x86-64 | 6.9 | 2017-04-05 |
| Live DVD | 2017-04-05 |   |   |   |
| 6.10 | Minimal CD | IA-32, x86-64 | 6.10 | 2018-07-03 |
| Live DVD | 2018-07-03 |   |   |   |
| 7.0-1406 | Minimal | x86-64 | 7.0 | 2014-07-21 |
| Live CD | 2014-07-07 |   |   |   |
| Gnome Live | 2014-07-07 |   |   |   |
| KDE Live | 2014-07-07 |   |   |   |
| 7.1-1503 | Minimal | x86-64 | 7.1 | 2015-03-31 |
| Live CD | 2015-03-31 |   |   |   |
| Gnome Live | 2015-03-31 |   |   |   |
| KDE Live | 2015-03-31 |   |   |   |
| 7.2-1511 | Minimal | x86-64 | 7.2 | 2015-12-14 |
| Gnome Live | 2015-12-14 |   |   |   |
| KDE Live | 2015-12-14 |   |   |   |
| 7.3-1611 | Minimal | x86-64 | 7.3 | 2016-12-12 |
| Gnome Live | 2016-12-12 |   |   |   |
| KDE Live | 2016-12-12 |   |   |   |
| 7.4-1708 | Minimal | x86-64 | 7.4 | 2017-09-13 |
| Gnome Live | 2017-09-13 |   |   |   |
| KDE Live | 2017-09-13 |   |   |   |
| 7.5-1804 | Minimal | x86-64 | 7.5 | 2018-05-10 |
| Gnome Live | 2018-05-10 |   |   |   |
| KDE Live | 2018-05-10 |   |   |   |
| 7.6-1810 | Minimal | x86-64 | 7.6 | 2018-12-03 |
| Gnome Live | 2018-12-03 |   |   |   |
| KDE Live | 2018-12-03 |   |   |   |
| 7.7-1908 | Minimal | x86-64 | 7.7 | 2019-09-17 |
| Gnome Live | 2019-09-17 |   |   |   |
| KDE Live | 2019-09-17 |   |   |   |

## Special interest groups

Special interest groups (SIGs) are organized portions of the CentOS community that open paths for building specialized variants of CentOS, which fulfill specific sets of requirements. SIGs have the freedom to modify and enhance CentOS in various ways, including adding more cutting-edge software, rebuilding existing packages depending on the requirements, providing alternative desktop environments, or making CentOS available on otherwise unsupported architectures.

## Architectures

As of version 8, CentOS fully supports x86-64, POWER8 and 64-bit ARM architectures, while the following architectures are not supported:

- IA-32 in all variants, not supported since CentOS 7
- IA-32 without Physical Address Extension (PAE), not supported since CentOS 6
- IA-64 (Intel Itanium architecture), was supported in CentOS 3 and 4
- 32-bit PowerPC (Apple Macintosh and PowerMac running the G3 or G4 PowerPC processor), beta support was available in CentOS 4
- IBM Mainframe (eServer zSeries and S/390), not supported since CentOS 5
- Alpha, support was available in CentOS 4
- SPARC, beta support was available in CentOS 4

As of December 2015, AltArch releases of CentOS 7 are available for the ARMv7hl and AArch64 variants of the ARM architecture, and plans exist for supporting other variants of the ARM architecture. ARM support is a community effort coordinated through the AltArch SIG. AltArch releases of CentOS 7 are also available for the IA-32 architecture and Power ISA (POWER7 and POWER8 chips).

A Live CD version of CentOS is available at *mirror.centos.org*. A bootable Live USB image of CentOS can be created manually or with UNetbootin.

CentOS images are also available on Amazon's EC2 cloud, in form of prebuilt and already published Amazon Machine Images (AMIs).

## Repositories

There are three primary CentOS repositories (also known as channels), containing software packages that make up the main CentOS distribution:

- `base`: contains packages that form CentOS point releases, and gets updated when the actual point release is formally made available in form of ISO images.
- `updates`: contains packages that serve as security, bugfix or enhancement updates, issued between the regular update sets for point releases. Bugfix and enhancement updates released this way are only those unsuitable to be released through the `CentOS-Fasttrack` repository described below.
- `addons`: provides packages required for building the packages that make up the main CentOS distribution, but are not provided by the upstream.

The CentOS Project provides several additional repositories that contain software packages not provided by the default `base` and `updates` repositories. Those repositories include the following:

- `CentOS Extras`: contains packages that provide additional functionality to CentOS without breaking its upstream compatibility or updating the base components.
- `CentOSPlus`: contains packages that actually upgrade certain base CentOS components, changing CentOS so that it is not exactly like the upstream provider's content.
- `CentOS-Testing`: serves as a proving ground for packages on their way to `CentOSPlus` and `CentOS Extras`. Offered packages may or may not replace core CentOS packages, and are not guaranteed to work properly.
- `CentOS-Fasttrack`: contains bugfix and enhancement updates issued from time to time, between the regular update sets for point releases. The packages released this way serve as close candidates for the inclusion into the next point release. This repository does not provide security updates, and does not contain packages unsuitable for uncertain inclusion into point releases.
- `CR` (Continuous Release): makes generally available packages that will appear in the next point release of CentOS. The packages are made available on a testing and hotfix basis, until the actual point release is formally released in form of ISO images.
- `debuginfo`: Contains packages with debugging symbols generated when the primary packages were built.
- `contrib`: Contains packages contributed by CentOS users that do not overlap with any of the core distribution packages.
- `Software Collections`: Provides versions of software newer than those provided by the base distribution, see above for more details.

## CentOS Stream

**CentOS Stream** is a "continuously delivered distro that tracks just ahead of Red Hat Enterprise Linux (RHEL) development, positioned as a midstream between Fedora Linux and RHEL." which is designed for "anyone interested in participating and collaborating in the RHEL ecosystem".

Because prior CentOS releases were derived directly from RHEL (RHEL was essentially upstream of CentOS), Stream thus represents a change from prior CentOS releases, being situated between the upstream development in Fedora and the downstream development for RHEL. That said, CentOS Stream 9 and RHEL 9 started from the same codebase and thus CentOS Stream could reasonably be seen as "closer" to RHEL than Fedora.

The initial release, CentOS Stream 8, was released on 24 September 2019, at the same time as CentOS 8. As CentOS 8 became unsupported, The CentOS Project provided a simple means of converting from CentOS Linux 8 to CentOS Stream 8.
