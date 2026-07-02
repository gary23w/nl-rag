---
title: "BusyBox"
source: https://en.wikipedia.org/wiki/BusyBox
domain: apk-alpine-packaging
license: CC-BY-SA-4.0
tags: alpine package keeper, apk package format, musl libc, software repository
fetched: 2026-07-02
---

# BusyBox

**BusyBox** is an implementation of many Unix commands in a single executable file. It runs in many POSIX environments including Linux, Android, and FreeBSD, although many of the tools it provides are designed to work with interfaces provided by the Linux kernel. It was specifically created for embedded operating systems with very limited resources. The authors dubbed it "The Swiss Army knife of Embedded Linux", as the single executable replaces basic functions of more than 300 common commands. It is released as free software under the terms of the GNU General Public License v2, having not been moved to version 3.

## History

### Origins

Originally written by Bruce Perens in 1995 and declared complete for his intended usage in 1996, BusyBox initially aimed to put a complete bootable system on a single floppy disk that would serve both as a rescue disk and as an installer for the Debian distribution. Since that time, it has been extended to become the de facto standard core user space toolset for embedded Linux devices and Linux distribution installers. Since each Linux executable requires several kilobytes of overhead, having the BusyBox program combine over two hundred programs together often saves substantial disk space and system memory.

BusyBox was maintained by Enrique Zanardi and focused on the needs of the Debian boot-floppies installer system until early 1998, when Dave Cinege took it over for the Linux Router Project (LRP). Cinege made several additions, created a modularized build environment, and shifted BusyBox's focus into general high-level embedded systems. As LRP development slowed down in 1999, Erik Andersen, then of Lineo, Inc., took over the project and became the official maintainer between December 1999 and March 2006. During this time the Linux embedded marketplace exploded in growth, and BusyBox matured greatly, expanding both its user base and functionality. Rob Landley became the maintainer in 2005 until late 2006, then Denys Vlasenko took over as the current maintainer.

### GPLv2/GPLv3 controversies

In September 2006, after heavy discussions and controversies between project maintainer Rob Landley and Bruce Perens, the BusyBox project decided against adopting the GNU General Public License Version 3 (GPLv3), and announced an intent to have the BusyBox license be GPLv2-only.

Since October 2006, Denys Vlasenko has taken over maintainership of BusyBox from Rob Landley, who has started Toybox, also as a result of the license controversies.

#### GPL lawsuits

In late 2007, BusyBox also came to prominence for actively prosecuting violations of the terms of its license (the GPL) in the United States District Court for the Southern District of New York.

What was claimed to be the first US lawsuit over a GPL violation concerned the use of BusyBox in an embedded device. The lawsuit, case 07-CV-8205, was filed on September 20, 2007, by the Software Freedom Law Center (SFLC) on behalf of Andersen and Landley against Monsoon Multimedia Inc., after BusyBox code was discovered in a firmware upgrade and attempts to contact the company had apparently failed. The case was settled with release of the Monsoon version of the source and payment of an undisclosed amount of money to Andersen and Landley.

On November 21, 2007, the SFLC brought two similar lawsuits on behalf of Andersen and Landley against two more companies, Xterasys (case 07-CV-10455) and High-Gain Antennas (case 07-CV-10456). The Xterasys case was settled on December 17 for release of source code used and an undisclosed payment, and the High-Gain Antennas case on March 6, 2008, for active license compliance and an undisclosed payment. On December 7, 2007, a case was brought against Verizon Communications over its distribution of firmware for Actiontec routers; this case was settled March 17, 2008 on condition of license compliance, appointment of an officer to oversee future compliance with free software licenses, and payment of an undisclosed sum. Further suits were brought on June 9, 2008, against Bell Microproducts (case 08-CV-5270) and SuperMicro (case 08-CV-5269), with the Super Micro case being settled on July 23, 2008. BusyBox and Bell Microproducts also settled out of court on October 17.

On December 14, 2009, a new lawsuit was filed naming fourteen defendants including Best Buy, JVC, Samsung and others. In February 2010 Samsung released its LN52A650 TV firmware under GPLv2, which was used later as a reference by the SamyGO community project.

On about August 3, 2010, BusyBox won from Westinghouse a default judgement of triple damages of $90,000 and lawyers' costs and fees of $47,865, and possession of "presumably a lot of high-def TVs" as infringing equipment in the lawsuit Software Freedom Conservancy v. Best Buy, et al., the GPL infringement case noted in the paragraph above.

No other developers, including original author Bruce Perens and maintainer Dave Cinege, were represented in these actions or party to the settlements. On December 15, 2009, Perens released a statement expressing his unhappiness with some aspects of the legal situation, and in particular alleged that the current BusyBox developers "appear to have removed some of the copyright statements of other BusyBox developers, and appear to have altered license statements".

### Toybox controversy

Toybox was started early 2006 under the GPL-2.0-only license by former BusyBox maintainer Rob Landley as a result of the controversies around GPLv3/GPLv2 discussions. At the end of 2011 it was relicensed under the BSD-2-Clause license after the project went dormant. In March 2013, it was relicensed again under the 0BSD license. On January 11, 2012, Tim Bird, a Sony employee, suggested creating an alternative to BusyBox which would not be under the GNU General Public License. He suggested it be based on the dormant Toybox. In January 2012 the proposal of creating a BSD licensed alternative to the GPL licensed BusyBox project drew harsh criticism from Matthew Garrett for taking away the only relevant tool for copyright enforcement of the Software Freedom Conservancy group. The starter of BusyBox based lawsuits, Rob Landley, responded that this was intentional as he came to the conclusion that the lawsuits resulted not in the hoped for positive outcomes and he wanted to stop them "in whatever way I see fit".

## Features

BusyBox can be customized to provide a subset of over two hundred utilities. It can provide most of the utilities specified in the Single Unix Specification (SUS) plus many others that a user would expect to see on a Linux system. BusyBox uses the Almquist shell, also known as A Shell, ash and sh. An alternative for customization is the smaller 'hush' shell. "Msh" and "lash" used to be available.

As it is a complete bootstrap system, it will further replace the init daemon and udev (or the latter-day systemd) using itself to be called as *init* on startup and *mdev* at hotplug time.

The BusyBox website provides a full list of the utilities implemented.

### Single binary

Typical computer programs have a separate binary (executable) file for each application. BusyBox is a single binary, which is a conglomerate of many applications, each of which can be accessed by calling the single BusyBox binary with various names (supported by having a symbolic link or hard link for each different name) in a specific manner with appropriate arguments.

Sharing of the common code, along with routines written with size-optimization in mind, can make a BusyBox system use much less storage space than a system built with the corresponding full versions of the utilities replaced by BusyBox. Research that compared GNU, BusyBox, asmutils and Perl implementations of the standard Unix commands showed that in some situations BusyBox may perform faster than other implementations, but not always.

### Commands

The official BusyBox documentation lists an overview of the available commands and their command-line options.

- acpid
- adduser
- adjtimex
- ash
- ar
- arp — The Address Resolution Protocol (ARP)
- arping — Send ARP REQUEST to a neighbour host
- ash
- basename — Return non-directory portion of a pathname removing suffix.
- bc — calculator program
- beep
- blkid — Print type, label and UUID of filesystem on a block device or image.
- brctl
- bunzip2 — Decompress bzip2 files.
- bzcat — Decompress bzip2 files to stdout.
- bzip2 — Create bzip2 compressed files.
- cal — Print a calendar.
- cat — Print content of one or more files to stdout.
- catv
- chat
- chattr — Change file attributes on a Linux file system.
- chgrp — Change group of one or more files.
- chmod — Change mode of listed files.
- chown — Change owner of one or more files.
- chpasswd
- chpst
- chroot — Run command within a new root directory.
- chrt
- chvt
- cksum — For each file, output crc32 checksum value, length and name of file.
- clear — Clear the screen.
- cmp — Compare the contents of two files.
- comm — Select or reject lines common to two files.
- cp — Copy files.
- cpio — Copy files into and out of a "newc" format cpio archive.
- crond
- crontab
- cryptpw
- cut — Print selected parts of lines from each FILE to standard output.
- date — Set/get the current date/time.
- dc — desk calculator
- dd — Copy a file with converting and formatting.
- deallocvt
- delgroup
- deluser
- depmod
- devmem
- df — Print filesystem usage statistics.
- dhcprelay
- diff — Compare two files.
- dirname — Show directory portion of path.
- dnsd
- dnsdomainname
- dos2unix — Convert newline format from dos "\r\n" to unix "\n".
- dpkg
- du — Show disk usage, space consumed by files and directories.
- dumpkmap
- dumpleases
- echo — Display a specified line of text.
- ed
- eject
- env — Set the environment for command invocation, or list environment variables.
- envdir
- envuidgid
- expand — Expand tabs to spaces according to tabstops.
- expr
- fakeidentd
- false
- fbset
- fbsplash
- fdflush
- fdformat
- fdisk
- find
- findfs
- flash_lock
- flash_unlock
- fold
- free
- freeramdisk
- fsck.minix
- fsck
- fsync
- ftpd
- ftpget
- ftpput
- fuser
- getopt
- getty
- grep — Search for PATTERN in each FILE or standard input.
- gunzip — Compressed file expansion.
- gzip — File compression.
- hd
- hdparm
- head
- hexdump
- hostid
- hostname
- httpd — HTTP server daemon
- hush
- hwclock
- id
- ifconfig
- ifdown
- ifenslave
- ifplugd
- ifup
- inetd
- inotifyd
- insmod
- install
- ionice
- ip
- ipaddr
- ipcalc
- ipcrm
- ipcs
- iplink
- iproute
- iprule
- iptunnel
- kbd_mode
- kill — Send a signal to a process.
- killall
- klogd
- last
- length
- less
- linux32
- linux64
- linuxrc
- ln — Create a link named LINK_NAME or DIRECTORY to the specified TARGET.
- loadfont
- loadkmap
- logger
- login — Begin a new session on the system
- logname
- logread
- losetup
- lpd
- lpq
- lpr
- ls — List of files or folders
- lsattr
- lsmod
- lzmacat
- lzop
- lzopcat
- makemime
- man
- md5sum
- mdev — akin to udev
- mesg
- microcom
- mkdir — Create a folder
- mkdosfs
- mkfifo
- mkfs.minix
- mkfs.vfat
- mknod
- mkpasswd
- mkswap
- mktemp
- modprobe
- more — View FILE or standard input one screen-full at a time
- mount — Mount file systems
- mountpoint
- mt
- mv — move file
- nameif
- nc — networking Swiss army knife.
- netstat — Display networking information.
- nice
- nmeter
- nohup
- nslookup
- ntpc
- ntpsync
- nvram
- od
- openvt
- passwd
- patch
- pgrep
- pidof — List PIDs of all processes with names that match NAMEs
- ping6
- ping — Send ICMP ECHO_REQUEST packets to network hosts
- pipe_progress
- pivot_root
- pkill
- popmaildir
- printenv
- printf
- ps — Report process status
- pscan
- pwd — Print working directory
- raidautorun
- rdate
- rdev
- readlink
- readprofile
- reformime
- renice
- reset
- resize
- rm — Erase file
- rmdir — Remove directory
- rmmod
- route
- rpm
- rstats — Copyright of BusyBox
- rx
- script
- scriptreplay
- sed — Text stream editor
- sendmail
- seq
- setarch
- setconsole
- setfont
- sh
- sha1sum — Compute and check SHA-1 message digest
- sha256sum — Compute and check SHA-256 message digest
- sha512sum
- showkey
- slattach
- sleep — Suspend program execution for a specified time
- softlimit
- sort
- split
- stat
- strings
- stty — Change and print terminal line settings
- su — Execute commands with privileges of another user account
- sum — Checksum and count blocks in a file
- sv
- switch_root
- sync — Write all buffered file system blocks to disk
- tac — Concatenate and print files in reverse line order
- tail — Output last of file
- tar
- tee — Send output to multiple files
- test — Built-in evaluation
- time
- top
- touch — Update the last-modified date on the given FILE[s]
- tr — Translate or delete characters
- true
- tty
- udhcpc — Small DHCP client
- umount — Unmount file systems
- uname — Display system information
- uptime — Tell how long the system has been running.
- uudecode
- uuencode
- usleep — Pause for N [microseconds]
- vconfig — VLAN (802.1q) configuration program
- vlock — Virtual Console lock program
- vi — (visual) Edit FILE
- volname — Return volume name
- watch — Execute a program periodically
- watchdog — Software watchdog daemon
- wc — Word, line, and byte or character count
- which — Shows the full path of (shell) commands
- who — Display who is on the system
- whoami — Print effective userid
- xargs — Construct argument lists and invoke utility
- yes — to print a string repetitively
- zcat — Uncompress to stdout

## Examples

A command can be run by prefixing a command line with a path to the BusyBox executable. The following invokes the `ls` command:

/bin/busybox ls

Commonly, each command is exposed as a hard or symbolic link to the BusyBox executable. For example, if `/bin/ls` links to `/bin/busybox` then the program name command-line argument is "/bin/ls" and BusyBox treats it as the `ls` command.

## Appliances and reception

BusyBox is used by several operating systems running on embedded systems and is an essential component of distributions such as OpenWrt, OpenEmbedded (including the Yocto Project) and Buildroot. The Sharp Zaurus utilizes BusyBox extensively for ordinary Unix-like tasks performed on the system's shell.

BusyBox is also an essential component of VMware ESXi, Tiny Core Linux, SliTaz 5(Rolling), and Alpine Linux, none of which are embedded distributions.

It is necessary for several root applications on Android and is also preinstalled with some "1 Tap Root" solutions such as Kingo Root.
