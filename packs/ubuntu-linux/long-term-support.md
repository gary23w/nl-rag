---
title: "Long-term support"
source: https://en.wikipedia.org/wiki/Long-term_support
domain: ubuntu-linux
license: CC-BY-SA-4.0
tags: ubuntu linux, canonical company, ubuntu release, long-term support
fetched: 2026-07-02
---

# Long-term support

**Long-term support** (**LTS**) is a product lifecycle management policy in which a stable release of computer software is maintained for a longer period of time than the standard edition. The term is typically reserved for open-source software, where it describes a software edition that is supported for months or years longer than the software's standard edition. This is often called an **extended-support release**.

*Short-term support* (STS) is a term that distinguishes the support policy for the software's standard edition. STS software has a comparatively short life cycle, and may be afforded new features that are omitted from the LTS edition to avoid potentially compromising the stability or compatibility of the LTS release.

## Characteristics

LTS applies the tenets of reliability engineering to the software development process and software release life cycle. Long-term support extends the period of software maintenance; it also alters the type and frequency of software updates (patches) to reduce the risk, expense, and disruption of software deployment, while prioritizing the dependability of the software. It does not necessarily imply technical support.

At the beginning of a long-term support period, the software developers impose a feature freeze: They make patches to correct software bugs and vulnerabilities, but do not introduce new features that may cause regression. The software maintainer either distributes patches individually, or packages them in maintenance releases, point releases, or service packs. At the conclusion of the support period, the product either reaches end-of-life, or receives a reduced level of support for a period of time (e.g., high-priority security patches only).

## Rationale

Before upgrading software, a decision-maker might consider the risk and cost of the upgrade.

As software developers add new features and fix software bugs, they may introduce new bugs or break old functionality. When such a flaw occurs in software, it is called a *regression*. Two ways that a software publisher or maintainer can reduce the risk of regression are to release major updates less frequently, and to allow users to test an alternate, updated version of the software. LTS software applies these two risk-reduction strategies. The LTS edition of the software is published in parallel with the STS (short-term support) edition. Since major updates to the STS edition are published more frequently, it offers LTS users a preview of changes that might be incorporated into the LTS edition when those changes are judged to be of sufficient quality.

While using older versions of software may avoid the risks associated with upgrading, it may introduce the risk of losing support for the old software. Long-term support addresses this by assuring users and administrators that the software will be maintained for a specific period of time, and that updates selected for publication will carry a significantly reduced risk of regression. The maintainers of LTS software only publish updates that either have low IT risk or that reduce IT risk (such as security patches). Patches for LTS software are published with the understanding that installing them is less risky than not installing them.

## Software with separate LTS versions

This table only lists software that have a specific LTS version in addition to a normal release cycle. Many projects, such as CentOS, provide a long period of support for every release.

| Software | Software type | Date of first LTS release | LTS period | STS period | Notes |
|---|---|---|---|---|---|
| Blender | Computer graphics | 3 June 2020 (2020-06-03) (v2.83) | 2 years |   |   |
| ChromeOS | Operating system | March 2022 | 6 months | 4 weeks | Chrome Enterprise and Education Help Center on Long-term Support (LTS) on ChromeOS |
| Collabora Online | Office Suite | 2 June 2016 (2016-06-02) | 1 year | Varies | Web-based, enterprise-ready edition of LibreOffice, its STS is typically a month. |
| Collabora Online for Desktop | Office Suite | 11 May 2013 (2013-05-11) | 3 years |   | For Windows, macOS and Linux, enterprise-ready edition of LibreOffice. "LTS support for 3 years as standard, with up to 5 years if required." Collabora Online for Mobile (Android, iOS and ChromeOS) have no LTS they receive rolling updates, their STS is a bit longer than Collabora Online. |
| Debian GNU/Linux | Linux distribution | 1 June 2014 | 5 years | 3 years | LTS (no cost) is provided by "a separate group of volunteers and companies interested in making it a success." Partial paid (for some versions) Extended long-term support (ELTS), for 2 extra years over the 5 of LTS, provided by Freexian. |
| Deno | Runtime system | November 2024 (v2.1) | 6 months | 4 weeks |   |
| Django | Application framework | 23 March 2012 (2012-03-23) (v1.4) | 3 years | 16 months |   |
| Firefox | Web browser | 31 January 2012 (2012-01-31) (v10.0) | 1 year | 4 weeks | Mozilla's LTS term is "Extended Support Release" (ESR) (see Firefox#Extended Support Release). |
| Joomla | CMS | January 2008 (2008-01) (v1.5) | 2 years, 3 months | 7 months | Since Joomla! is a web application, long-term support also implies support for legacy web browsers. |
| Laravel | Application framework | 9 June 2015 (2015-06-09) (v5.1) | 3 years | 1 year | For LTS releases, bug fixes are provided for 2 years and security fixes are provided for 3 years. For general releases, bug fixes are provided for 6 months and security fixes are provided for 1 year. |
| Linux kernel | Kernel | 11 October 2008 (2008-10-11) (v2.6.27) | Varies, 6, 10+ years | Varies | Linux kernel v2.6.16 and v2.6.27, were unofficially supported in LTS fashion before a 2011 working group in the Linux Foundation started a formal Long Term Support Initiative. The LTS support period was increased to 6 years; Linux kernel 4.4 will have 6 years of support before being taken over by the "Civil Infrastructure Platform" (CIP) project that plans to maintain it for a minimum of 10 years under "SLTS (Super Long Term Support)" (the CIP has only, for now, decided to maintain for 64-bit x86-64 and 32-bit ARM; while 64-bit ARM hardware support is also planned). "The use cases CIP project is targeting have a life cycle of between 25 and 50 years." and the CIP envisions 15+ years of support. |
| Linux Mint | Linux distribution | 8 June 2008 (2008-06-08) | 5 years | 6 months | As of version 13 the LTS period increased from three years to five, since Linux Mint derives from Ubuntu. Version 16 was the last non-LTS version. |
| Java | Virtual machine and runtime environment | Varies by distributor | Varies by distributor | 6 months | Java itself has no notion of support. OpenJDK, the Java reference implementation, publishes a new feature release very six months that usually receives two quarterly updates. The OpenJDK Updates Project maintains some versions (11, 13, 15, 17, 21, 25) for much longer (source only). Distributions with varying levels of support are available from many vendors (OpenJDK § OpenJDK builds). |
| Moodle | LMS | 12 May 2014 (v2.7) | 3 years | 18 months |   |
| Matomo | Web analytics | 3 February 2016 (2016-02-03) (v2.16) | ≥12 months | ~4 weeks |   |
| Node.js | Runtime system | 12 October 2015 (2015-10-12) (v4.2.0) | 18 months | 12 months |   |
| Symfony | Application framework | June 2013 (2013-06) | 3 years | 8 months |   |
| Tiki-wiki | Wiki/CMS | May 2009 (Tiki3) | 5 years | 6 months | Every third version is a Long Term Support (LTS) version. |
| Trisquel 7.0 | Linux distribution | 2014-11-04 | 5 years | 1 year | Linux-libre (kernel) 3.13, GNOME fallback 3.12 and Abrowser or GNU IceCat |
| TYPO3 | CMS | January 2011 (2011-01) (v4.5 LTS) | 3 years (min.) | Varies | TYPO3 is a web application stewarded by the TYPO3 Association. |
| Ubuntu | Linux distribution | 1 June 2006 (2006-06-01) (Ubuntu 6.06 LTS) | 5 years, 10 years with ESM, 12 years with Legacy Support | 9 months1 | A new LTS version is released every two years. From 2006 through 2011, LTS support for the desktop was for approximately two years, and for servers five, but LTS versions are now supported for five years for both. Extended Security Maintenance (ESM) is available for an additional 5 years on Ubuntu 14.04 and subsequent LTS releases and Legacy Support for a further 2 years beyond ESM. |
| Windows 10 | Operating system | 29 July 2015 (2015-07-29) (v10.0.10240) | 10 years | 18 months (previously 8–12 months) | The Long-Term Servicing Channel (LTSC) (previously Long-Term Servicing Branch) releases of Windows 10 are supported for 10 years for mission critical machines. The LTSC release gets monthly security updates; the updates to the LTSC release bring little to no feature changes. Every 2–3 years, a new major LTSC release is published, but businesses may opt to stay on their current LTSC version until its end-of-life. The LTSC release is available only for businesses running the Windows 10 Enterprise edition. Regular consumers on the Semi-Annual Channel (SAC) get new versions of the operating system approximately every six months (previously every four months) while business customers get upgraded to new versions of SAC approximately four months after Microsoft released the SAC release for regular consumers (previously a separate release is done approximately every eight months). |
| Windows 11 | Operating system | 5 October 2021 (2021-10-05) (v10.0.22000.258) | 3 years (Enterprise and Education editions) | 2 years | "Windows 11 feature updates will release in the second half of the calendar year and will come with 24 months of support for Home, Pro, Pro for Workstations, and Pro Education editions. Windows 11 will come with 36 months of support for Enterprise and Education editions." |
| Zabbix | Network monitoring software | 21 May 2012 (2.0) | 5 years | 6 months | Dot-zero versions (3.0, 4.0, 5.0, etc) are LTS releases that have "Full support" for three years, and "Limited support" (e.g., security update) for an addition two, for a total of five years. Standard releases (5.2, 5.4, etc) are released every six months and are only supported until the next software release (plus an extra month for security fixes). |

1.

^

The support period for Ubuntu's parent distribution,

Debian

, is one year after the release of the next stable version.

Since Debian 6.0 "Squeeze", LTS support (bug fixes and security patches) was added to all version releases.

The total LTS support time is generally around 5 years for every version.

Due to the irregular release cycle of Debian, support times might vary from that average

and the LTS support is done not by the Debian team but by a separate group of volunteers.
