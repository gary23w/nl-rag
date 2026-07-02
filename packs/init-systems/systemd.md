---
title: "systemd"
source: https://en.wikipedia.org/wiki/Systemd
domain: init-systems
license: CC-BY-SA-4.0
tags: init system, systemd manager, sysvinit scripts, process identifier
fetched: 2026-07-02
---

# systemd

**systemd** is a software suite for system and service management on Linux built to unify service configuration and behavior across Linux distributions. Its main component is an init system used to bootstrap user space and manage user processes. It also provides various daemons and utilities, including device management, login management, network connection management, and event logging. The name *systemd* adheres to the Unix convention of naming daemons by appending the letter *d,* and also plays on the French phrase *Système D* (a person's ability to quickly adapt and improvise in the face of problems).

In Linux distributions, systemd is used as a replacement for Sysvinit and other init systems. Since 2015, nearly all Linux distributions have adopted systemd. It has been praised by developers and users of distributions that adopted it for providing a stable, fast out-of-the-box solution for issues that had existed in the Linux space for years. At the time of its adoption, it was the only parallel boot and init system offering centralized management of processes, daemons, services, and mount points..

Critics of systemd contend it suffers from feature creep and has damaged interoperability across Unix-like operating systems (as it does not run on non-Linux Unix derivatives like BSD or Solaris). In addition, they contend systemd's large feature set creates a larger attack surface. This has led to the development of several minor Linux distributions replacing systemd with other init systems like SysVinit or OpenRC.

## History

Lennart Poettering and Kay Sievers, the software engineers then working for Red Hat who initially developed systemd, started a project to replace Linux's conventional System V init in 2010. An April 2010 blog post from Poettering, titled "Rethinking PID 1", introduced an experimental version of what would later become systemd. They sought to surpass the efficiency of the init daemon in several ways. They wanted to improve the software framework for expressing dependencies, to allow more processes to run concurrently or in parallel during system booting, and to reduce the computational overhead of the shell.

In May 2011, Fedora Linux became the first major Linux distribution to enable systemd by default, replacing Upstart. The reasoning at the time was that systemd provided extensive parallelization during startup, better management of processes and overall a saner, dependency-based approach to control of the system.

In October 2012, Arch Linux made systemd the default, switching from SysVinit. Developers had debated since August 2012 and concluded it was faster and had more features than SysVinit and that maintaining SysVinit was not worth the effort. Some thought the criticism of systemd was not based on actual shortcomings of the software but rather personal dislike of Poettering and a general opposition to change. Several complaints about systemd—including its use of D-bus, C instead of bash, and an optional on-disk journal format—were instead described as advantages by the Arch maintainers.

Between 2013 and 2014, the Debian Technical Committee engaged in a widely publicized debate on the mailing list about which init system to use as the default in Debian 8 before settling on systemd. Soon after, Debian developer Joey Hess, Technical Committee members Russ Allbery and Ian Jackson, and systemd package maintainer Tollef Fog Heen resigned from their positions, citing the extraordinary levels of stress caused by disputes on systemd integration within the Debian and FOSS community that rendered regular maintenance virtually impossible. Mark Shuttleworth announced soon afterwards that the Debian-based Ubuntu would use systemd to replace its old Upstart init system.

In August 2015, systemd started providing a login shell, callable via **machinectl shell**.

In September 2016, a security bug was discovered that allowed any unprivileged user to perform a denial-of-service attack against systemd. Rich Felker, developer of musl, stated that this bug reveals a major "system development design flaw". In 2017 another security bug was discovered in systemd-resolved, CVE-2017-9445, which "allows disruption of service" by a "malicious DNS server". Later in 2017, the Pwnie Awards gave author Lennart Poettering a "lamest vendor response" award due to his handling of the vulnerabilities.

## Design

Poettering describes systemd development as "never finished, never complete, but tracking progress of technology". In May 2014, Poettering further described systemd as unifying "pointless differences between distributions", by providing the following three general functions:

- A system and service manager (manages both the system, by applying various configurations, and its services)
- A software platform (serves as a basis for developing other software)
- The glue between applications and the kernel (provides various interfaces that expose functionalities provided by the kernel)

systemd includes features like on-demand starting of daemons, snapshot support, process tracking and Inhibitor Locks. It is not just the name of the init daemon but also refers to the entire software bundle around it, which, in addition to the systemd init daemon, includes the daemons journald, logind and networkd, and many other low-level components. In January 2013, Poettering described systemd not as one program, but rather a large software suite that includes 69 individual binaries. As an integrated software suite, systemd replaces the startup sequences and runlevels controlled by the traditional init daemon, along with the shell scripts executed under its control. systemd also integrates many other services that are common on Linux systems by handling user logins, the system console, device hotplugging (see udev), scheduled execution (replacing cron), logging, hostnames and locales.

Like the init daemon, systemd is a daemon that manages other daemons, which, including systemd itself, are background processes. systemd is the first daemon to start during booting and the last daemon to terminate during shutdown. The systemd daemon serves as the root of the user space's process tree; the first process (PID 1) has a special role on Unix systems, as it replaces the parent of a process when the original parent terminates. Therefore, the first process is particularly well suited for the purpose of monitoring daemons.

systemd executes elements of its startup sequence in parallel, which is theoretically faster than the traditional startup sequence approach. For inter-process communication (IPC), systemd makes Unix domain sockets and D-Bus available to the running daemons. The state of systemd itself can also be preserved in a snapshot for future recall.

### Core components and libraries

Following its integrated approach, systemd also provides replacements for various daemons and utilities, including the startup shell scripts, pm-utils, inetd, acpid, syslog, watchdog, cron and atd. systemd's core components include:

- systemd is a system and service manager for Linux operating systems.
- systemctl is a command to introspect and control the state of the systemd system and service manager. Not to be confused with sysctl.
- systemd-analyze may be used to determine system boot-up performance statistics and retrieve other state and tracing information from the system and service manager.

systemd tracks processes using the Linux kernel's cgroups subsystem instead of using process identifiers (PIDs); thus, daemons cannot "escape" systemd, not even by double-forking. systemd not only uses cgroups, but also augments them with systemd-nspawn and machinectl, two utility programs that facilitate the creation and management of Linux containers. Since version 205, systemd also offers ControlGroupInterface, which is an API to the Linux kernel cgroups. The Linux kernel cgroups are adapted to support kernfs, and are being modified to support a unified hierarchy.

### Ancillary components

Beside its primary purpose of providing a Linux init system, the systemd suite can provide additional functionality, including the following components:

**journald**

systemd-journald

is a daemon responsible for

event logging

, with append-only

binary files

serving as its

logfiles

. The

system administrator

may choose whether to log system events with

systemd-journald

,

syslog-ng

or

rsyslog

.

**libudev**

libudev

is the standard library for utilizing udev, which allows third-party applications to query udev resources.

**localed**

localed

manages the

system locale

and

keyboard layout

.

**logind**

systemd-logind

is a daemon that manages user logins and seats in various ways. It is an integrated login manager that offers

multiseat

improvements

and replaces

ConsoleKit

, which is no longer maintained.

For

X11 display managers

the switch to

logind

requires a minimal amount of porting.

It was integrated in systemd version 30.

**hostnamed**

hostnamed

manages the

system hostname

.

**homed**

homed

is a daemon that provides portable human-user accounts that are independent of current system configuration.

homed

moves various pieces of data such as UID/GID from various places across the filesystem into one file,

~/.identity

.

homed

manages the user's home directory in various ways such as a plain directory, a

btrfs

subvolume, a

Linux Unified Key Setup

volume, an fscrypt directory, or mounted from an

SMB

server.

**networkd**

networkd

is a daemon to handle the configuration of the network interfaces; in version 209, when it was first integrated, support was limited to statically assigned addresses and basic support for

bridging

configuration.

In July 2014, systemd version 215 was released, adding new features such as a

DHCP

server for

IPv4

hosts, and

VXLAN

support.

networkctl

may be used to review the state of the network links as seen by systemd-networkd.

Configuration of new interfaces has to be added under the /lib/systemd/network/ as a new file ending with .network extension.

**resolved**

provides network name resolution to local applications

**systemd-boot**

systemd-boot

is a boot manager, formerly known as

gummiboot

. Kay Sievers merged it into systemd with rev 220.

**systemd-bsod**

systemd-bsod

is an error reporter used to generate

Blue Screen of Death

.

**systemd-nspawn**

systemd-nspawn

may be used to run a command or OS in a namespace container.

**timedated**

systemd-timedated

is a daemon that can be used to control time-related settings, such as the system time, system

time zone

, or selection between

UTC

and local time-zone system clock. It is accessible through D-Bus.

It was integrated in systemd version 30.

**timesyncd**

timesyncd

is a client

NTP

daemon for synchronizing the system clock across the network.

**tmpfiles**

systemd-tmpfiles

is a utility that takes care of creation and clean-up of temporary files and directories. It is normally run once at startup and then in specified intervals.

**udevd**

udev

is a device manager for the

Linux kernel

, which handles the

/dev

directory and all

user space

actions when adding/removing devices, including

firmware

loading. In April 2012, the

source tree

for udev was

merged

into the systemd source tree.

In order to match the version number of udev, systemd maintainers bumped the version number directly from 44 to 183.

On 29 May 2014, support for firmware loading through udev was dropped from systemd, as it was decided that the kernel should be responsible for loading firmware.

### Configuration of systemd

systemd is configured exclusively via plain-text files although GUI tools such as systemd-manager are also available.

systemd records initialization instructions for each daemon in a configuration file (referred to as a "unit file") that uses a declarative language, replacing the traditionally used per-daemon startup shell scripts. The syntax of the language is inspired by .ini files.

Unit-file types include:

- .service
- .socket
- .device (automatically initiated by systemd)
- .mount
- .automount
- .swap
- .target
- .path
- .timer (which can be used as a cron-like job scheduler)
- .snapshot
- .slice (used to group and manage processes and resources)
- .scope (used to group worker processes, not intended to be configured via unit files)

## Adoption

| Linux distribution | Date added to software repository | Enabled by default? | Date released as default | Runs without? |
|---|---|---|---|---|
| Alpine Linux | N/A (not in repository) | No | N/A | Yes |
| Android | N/A (not in repository) | No | N/A | Yes |
| Arch Linux | January 2012 | Yes | October 2012 | Although Arch provides installation instructions for OpenRC and other init systems are available in the AUR, Arch officially supports only systemd. |
| antiX Linux | N/A (not in repository) | No | N/A | Yes |
| Artix Linux | N/A (not in repository) | No | N/A | Yes |
| CentOS | July 2014 | Yes | July 2014 (v7.0) | No |
| CoreOS | July 2013 | Yes | October 2013 (v94.0.0) | No |
| Debian | April 2012 | Yes | April 2015 (v8.0) | Jessie is the last release supporting installing without systemd. In bullseye, a number of alternative init systems are supported |
| Devuan | N/A (not in repository) | No | N/A | Yes |
| Fedora Linux | November 2010 (v14) | Yes | May 2011 (v15) | No |
| Gentoo Linux | July 2011 | Optional | N/A | Yes |
| GNU Guix System | N/A (not in repository) | No | N/A | Yes |
| Knoppix | N/A | No | N/A | Yes |
| Linux Mint | June 2016 (v18.0) | Yes | August 2018 (LMDE 3) | No |
| Mageia | January 2011 (v1.0) | Yes | May 2012 (v2.0) | No |
| Manjaro Linux | November 2013 | Yes | November 2013 | No |
| openSUSE | March 2011 (v11.4) | Yes | September 2012 (v12.2) | No |
| Parabola GNU/Linux-libre | January 2012 | Optional | N/A | Yes |
| Red Hat Enterprise Linux | June 2014 (v7.0) | Yes | June 2014 (v7.0) | No |
| Slackware | N/A (not in repository) | No | N/A | Yes |
| Solus | N/A | Yes | N/A | No |
| Source Mage | June 2011 | No | N/A | Yes |
| SUSE Linux Enterprise Server | October 2014 (v12) | Yes | October 2014 (v12) | No |
| Ubuntu | April 2013 (v13.04) | Yes | April 2015 (v15.04) | No, Upstart option removed in Yakkety (16.10) |
| Void Linux | June 2011, removed June 2015 | No | N/A | Yes |

While many distributions boot systemd by default, some allow other init systems to be used; in this case switching the init system is possible by installing the appropriate packages. A fork of Debian called Devuan was developed to avoid systemd and has reached version 5.0 for stable usage. In December 2019, the Debian project voted in favour of retaining systemd as the default init system for the distribution, but with support for "exploring alternatives".

### Integration with other software

In the interest of enhancing the interoperability between systemd and the GNOME desktop environment, systemd coauthor Lennart Poettering asked the GNOME Project to consider making systemd an external dependency of GNOME 3.2.

In November 2012, the GNOME Project concluded that basic GNOME functionality should not rely on systemd. However, GNOME 3.8 introduced a compile-time choice between the logind and ConsoleKit API, the former being provided at the time only by systemd. Ubuntu provided a separate logind binary, but systemd became a *de facto* dependency of GNOME for most Linux distributions, in particular since ConsoleKit is no longer actively maintained and upstream recommends the use of systemd-logind instead. The developers of Gentoo Linux also attempted to adapt these changes in OpenRC, but the implementation contained too many bugs, causing the distribution to mark systemd as a dependency of GNOME.

GNOME has further integrated logind. As of Mutter version 3.13.2, logind is a dependency for Wayland sessions.

## Reception

The design of systemd has ignited controversy within the free-software community. Critics regard systemd as overly complex and suffering from continued feature creep, arguing that its architecture violates the Unix philosophy. There is also concern that it forms a system of interlocked dependencies, thereby giving distribution maintainers little choice but to adopt systemd as more user-space software comes to depend on its components.

In a 2012 interview, Slackware's lead Patrick Volkerding expressed reservations about the systemd architecture, stating his belief that its design was contrary to the Unix philosophy of interconnected utilities with narrowly defined functionalities. As of August 2018, Slackware does not support or use systemd, but Volkerding has not ruled out the possibility of switching to it.

In January 2013, Lennart Poettering attempted to address concerns about systemd in a blog post called *The Biggest Myths*.

In February 2014, musl's Rich Felker opined that PID 1 is too special to be saddled with additional responsibilities, believing that PID 1 should only be responsible for starting the rest of the init system and reaping zombie processes, and that the additional functionality added by systemd can be provided elsewhere and unnecessarily increases the complexity and attack surface of PID 1.

In March 2014, Eric S. Raymond commented that systemd's design goals were prone to mission creep and software bloat. In April 2014, Linus Torvalds expressed reservations about the attitude of Kay Sievers, a key systemd developer, toward users and bug reports in regard to modifications to the Linux kernel submitted by Sievers. In late April 2014, a campaign to boycott systemd was launched, with a website listing various reasons against its adoption.

In an August 2014 article published in *InfoWorld*, Paul Venezia wrote about the systemd controversy and attributed the controversy to violation of the Unix philosophy, and to "enormous egos who firmly believe they can do no wrong". The article also characterizes the architecture of systemd as similar to that of svchost.exe, a critical system component in Microsoft Windows with a broad functional scope.

In a September 2014 ZDNet interview, prominent Linux kernel developer Theodore Ts'o expressed his opinion that the dispute over systemd's centralized design philosophy, more than technical concerns, indicates a dangerous general trend toward uniformizing the Linux ecosystem, alienating and marginalizing parts of the open-source community, and leaving little room for alternative projects. He cited similarities with the attitude he found in the GNOME project toward non-standard configurations. On social media, Ts'o also later compared the attitudes of Sievers and his co-developer, Lennart Poettering, to that of GNOME's developers.

## Forks and alternative implementations

Forks of systemd are closely tied to critiques of it outlined in the above section. Forks generally try to improve on at least one of portability (to other libcs and Unix-like systems), modularity, or size. A few forks have collaborated under the FreeInit banner.

### Forks of components

#### eudev

In 2012, the Gentoo Linux project created a fork of udev in order to avoid dependency on the systemd architecture. The resulting fork is called *eudev* and it makes udev functionality available without systemd. A stated goal of the project is to keep eudev independent of any Linux distribution or init system. In 2021, Gentoo announced that support of eudev would cease at the beginning of 2022. An independent group of maintainers have since taken up eudev.

#### elogind

Elogind is the systemd project's "logind", extracted to be a standalone daemon. It integrates with PAM to know the set of users that are logged into a system and whether they are logged in graphically, on the console, or remotely. Elogind exposes this information via the standard org.freedesktop.login1 D-Bus interface, as well as through the file system using systemd's standard /run/systemd layout. Elogind also provides "libelogind", which is a subset of the facilities offered by "libsystemd". There is a "libelogind.pc" pkg-config file as well.

### Alternatives to components

#### ConsoleKit2

ConsoleKit was forked in October 2014 by Xfce developers wanting its features to still be maintained and available on operating systems other than Linux. While not ruling out the possibility of reviving the original repository in the long term, the main developer considers ConsoleKit2 a temporary necessity until systembsd matures.

### Abandoned forks

#### Fork of components

##### LoginKit

LoginKit was an attempt to implement a logind (systemd-logind) shim, which would allow packages that depend on systemd-logind to work without dependency on a specific init system. The project has been defunct since February 2015.

##### systembsd

In 2014, a Google Summer of Code project named "systembsd" was started in order to provide alternative implementations of these APIs for OpenBSD. The original project developer began it in order to ease his transition from Linux to OpenBSD. Project development finished in July 2016.

The systembsd project did not provide an init replacement, but aimed to provide OpenBSD with compatible daemons for hostnamed, timedated, localed, and logind. The project did not create new systemd-like functionality, and was only meant to act as a wrapper over the native OpenBSD system. The developer aimed for systembsd to be installable as part of the ports collection, not as part of a base system, stating that "systemd and *BSD differ fundamentally in terms of philosophy and development practices."

##### notsystemd

Notsystemd intends to implement all systemd's features working on any init system. It was forked by the Parabola GNU/Linux-libre developers to build packages with their development tools without the necessity of having systemd installed to run systemd-nspawn. Development ceased in July 2018.

#### Fork including init system

##### uselessd

In 2014, *uselessd* was created as a lightweight fork of systemd. The project sought to remove features and programs deemed unnecessary for an init system, as well as address other perceived faults. Project development halted in January 2015.

uselessd supported the musl and μClibc libraries, so it may have been used on embedded systems, whereas systemd only supported glibc. The uselessd project had planned further improvements on cross-platform compatibility, as well as architectural overhauls and refactoring for the Linux build in the future.

##### InitWare

InitWare is a modular refactor of systemd, porting the system to BSD platforms without glibc or Linux-specific system calls. It is known to work on DragonFly BSD, FreeBSD, NetBSD, and GNU/Linux. Components considered unnecessary are dropped.

## All Systems Go!

All Systems Go! is the annual systemd conference, which is held in Berlin. The main topic is systemd but other Linux areas are covered as well, like TPM, DBus, desktop environment, containers, eBPF etc.
