---
title: "YaST"
source: https://en.wikipedia.org/wiki/YaST
domain: opensuse
license: CC-BY-SA-4.0
tags: opensuse distribution, zypper package manager, yast tool, suse enterprise
fetched: 2026-07-02
---

# YaST

**YaST** (Yet another Setup Tool) is a Linux operating system setup and configuration tool.

YaST is featured in the openSUSE Linux distribution, as well as in SUSE's derived commercial distributions including SUSE Linux Enterprise. It is also part of the defunct United Linux.

YaST features tools that can configure many aspects of the system.

YaST was released first in April 1995. The first SuSE distribution that included YaST was released in May 1996. YaST was re-written in 1999 and included first in SuSE Linux 6.3 as only an installer. YaST2 was added to the desktop in SuSE Linux 6.4 and co-existed with YaST1 until YaST1's removal in SuSE Linux 8.0.

YaST was deprecated starting with openSUSE Leap 16 with the Qt interface removed, however, the ncurses interface is still available to download and use.

## Details

YaST is free and open-source software that SUSE has made available under the GNU General Public License (GPL) in 2004. It is a tool for administering and maintaining a SUSE Linux installation. It allows system administrators to install software, configure hardware, set up networks and servers, and more.

YaST also features two front ends: a graphical user interface (GUI) and a text-based user interface (TUI) (with ncurses). This is especially useful for non-GUI installations such as servers, for system administration over slow Internet connections, and for when one is unable to boot into a graphical X server but still need an advanced user interface to the package manager (for example, a novice user trying to downgrade an X.Org package to fix a graphical installation).

YaST offers package managing functions through the ZYpp project. The first ZYpp enabled package management YaST applications had performance problems and long start up times, but was improved in the 10.2 and 10.3 releases. Starting with openSUSE 11.0 alpha 3, ZYpp was integrated with the SAT solver project, making YaST and Zypper faster than other RPM Package Manager based systems.

YaST used to include SaX and SaX2, the Suse Advanced X configuration. SaX was re-written as SaX2 in SuSE Linux 6.4. SaX1 was removed in SuSE Linux 8.1 and SaX2 was removed from the YaST Control Center in openSUSE 11.2. SaX2 was removed completely in openSUSE 11.3. The GTK interface was removed in openSUSE Leap 42.1.

YaST often receives updates and improvements in Tumbleweed and between versions of Leap. openSUSE Leap 15.1, for example, saw improvements to the YaST interface for managing firewalls including the addition of an interface in the command line version of YaST. In this same release of openSUSE Leap, YaST now has an updated logo and improved partition management module.

YaST formerly used a bespoke scripting language named YCP; in OpenSUSE 13.1, YaST was rewritten in Ruby.

On openSUSE Leap 16 and SUSE Linux Enterprise Server 16, YaST was deprecated. The web-based Cockpit project was adopted to supplant the YaST Control Center, a web-based installer named Agama replaced the YaST installer, and Myrlyn was introduced as a new Qt-based ZYpp front end with no dependency on YaST, replaced YaST Software.

## AutoYaST

AutoYaST is a system for installing one or more openSUSE systems automatically without user intervention. AutoYaST installations are performed using a control file with installation and configuration data.

The profile of each current system is stored in `/root/autoyast.xml`.

## WebYaST

WebYaST is a web interface for YaST that can be used to check the status of the current machine. It can check on the installation of packages, shutdown or reboot the system, change some system settings (such as the time), and change the status of system services or daemons.

## YaST4Debian

The change of license of YaST from a previous rather restrictive license to the GPL in 2004 made it possible to port YaST to other Linux distributions. As a consequence of this, the project *YaST4Debian* was launched, which worked on a port of YaST to Debian.

The project, which was in contact with the YaST team of Novell/SuSE, reached some important milestones, such as the port of the modules *yast2-ncurses* and *yast2-qt*. Currently, the project is dormant, searching for a new voluntary project maintainer.
