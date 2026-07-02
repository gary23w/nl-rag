---
title: "The GNU Readline Library"
source: https://tiswww.case.edu/php/chet/readline/rltop.html
domain: readline-library
license: CC-BY-SA-4.0
tags: gnu readline, readline line editing, command-line editing library, interactive line editor
fetched: 2026-07-02
---

### The GNU Readline Library

#### Table of Contents

- Introduction
- Current Status
- Source Code Availability
- Distributions
- Documentation
- Reporting Bugs
- Other Resources
- Maintainer
- Translations

### Introduction

The GNU Readline library provides a set of functions for use by applications that allow users to edit command lines as they are typed in. Both Emacs and vi editing modes are available. The Readline library includes additional functions to maintain a list of previously-entered command lines, to recall and perhaps reedit those lines, and perform csh-like history expansion on previous commands.

The history facilities are also placed into a separate library, the History library, as part of the build process. The History library may be used without Readline in applications which desire its capabilities.

Readline is free software, distributed under the terms of the GNU General Public License, version 3. This means that if you want to use Readline in a program that you release or distribute to anyone, the program must be free software and have a GPL-compatible license. If you would like advice on making your license GPL-compatible, contact licensing@gnu.org. Current Status

The current version of readline is readline-8.3. (GPG signature).

You can get the current version with all official patches applied by cloning the main readline git repository (links at the bottom of the page) and checking out the master branch.

A snapshot of the current development sources (generally updated monthly or more often) is also available from the GNU git readline devel branch.

See the README file for more information.

See the CHANGES file for a list of changes and new features in Readline-8.3. Availability

The current version of readline may be retrieved from ftp.cwru.edu and from the master GNU ftp site and its many mirrors. This distribution file includes formatted copies of the readline documentation.

These files are signed with my GPG key.

Any patches for the current version are available from CWRU and ftp.gnu.org.

You can get the current version with all official patches applied by cloning the main readline git repository and checking out the master branch, and a snapshot of the current development sources (generally updated monthly or more often) is available from the GNU readline git devel branch.

The full set of commits is available at this link; and you can browse the full source tree here.

Previous Readline versions are available at ftp://ftp.gnu.org/gnu/readline. Distributions

Readline is shipped as a standard library on most GNU/Linux, FreeBSD, and OpenBSD systems. It's also available as a NetBSD package.

The OpenPKG project makes source RPMs of readline-8.2 available for a variety of Unix and Linux systems as a base part of the current release.

MacOS X users may obtain MacOS X packages for readline-8.2 from MacPorts, Homebrew, or Fink.

Solaris users can get precompiled versions of readline-7.0 from OpenCSW or the Unixpackages (subscription) site. Oracle ships readline-4.2 as a supported part of the Solaris 10 companion CD and readline-8.1 as a supported part of Solaris 11. The version of Solaris/Illumos distributed as OpenIndiana includes readline-8.2 as of June 2025.

AIX users can get sources and precompiled versions of readline-7.0 (as well as older readline releases) for various versions of AIX from perzl.org. IBM makes readline-8.2 available for AIX 5L through AIX 7.2 as part of the AIX toolbox for [GNU/]Linux applications. They use RPM format; you can get RPM for AIX from there, too.

HP-UX users can get readline-8.2 packages and source code from the Software Porting and Archive Center for HP-UX. It's even available on Minix.

If you are running Windows, I recommend that you use Cygwin, who currently ship readline-8.2 and older versions for x86_64, or, for a version that runs independently of Cygwin, see the mingw64-{i686,x86_64}-readline packages.

Microsoft offers its Windows Subsystem for Linux (WSL) as an installable add-on for Windows 10 and Windows 11. It's basically a separate packaged version of the Linux kernel that runs as a Windows service, and you can build and install readline-8.3 within that environment. Documentation

The documentation for the Readline and History libraries appears in the `doc' subdirectory. There are three texinfo files and two Unix-style manual pages describing the facilities available in the Readline and History libraries. The texinfo files include both user and programmer's manuals. The current manuals are: The GNU Readline Library The GNU History Library The GNU Readline User Interface Reporting Bugs

Bug reports for Readline should be sent to bug-readline@gnu.org, When reporting a bug, please include the following information: The version number and release status of Readline (e.g., 4.2-release) The machine and OS that it is running on A list of the compilation flags or the contents of `config.h', if appropriate a description of the bug a recipe for recreating the bug reliably a fix for the bug if you have one!

If you would like to contact the Readline maintainer directly, send mail to the bug-readline@gnu.org mailing list. You may subscribe to the mailing list at lists.gnu.org. Archives of bug-readline dating from November, 2006 are available from lists.gnu.org.

Since Readline is developed along with bash, the bug-bash@gnu.org mailing list (mirrored to the Usenet newsgroup gnu.bash.bug) often contains Readline bug reports and fixes.

Archives of bug-bash dating from December, 1999 are available from lists.gnu.org. Google Groups has an archive of gnu.bash.bug. Other Resources

Some files from the current distribution may be helpful. README: a file describing Readline CHANGES: a complete Readline change history NEWS: a file tersely listing the notable changes between the current and previous versions INSTALL: installation instructions rl.c is an example program that uses Readline to read a line of input from a user and echo it to the standard output, suitable for use by shell scripts. Maintainer

I am the current Readline maintainer. Please send additions and corrections to this page to chet.ramey@case.edu. Translations

Translate this page:

Chet Ramey

<

chet.ramey@case.edu

>

Last updated: Tue Jul 1 14:45:51 EDT 2025
