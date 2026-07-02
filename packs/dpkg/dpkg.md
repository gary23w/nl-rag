---
title: "dpkg"
source: https://en.wikipedia.org/wiki/Dpkg
domain: dpkg
license: CC-BY-SA-4.0
tags: dpkg debian, debian packages, package manager, deb archive
fetched: 2026-07-02
---

# dpkg

**dpkg** is the software at the base of the package management system in the free operating system Debian and its many derivatives. `dpkg` is used to install, remove, and provide information about .deb packages.

`dpkg` (Debian Package) itself is a low-level tool. Advanced Package Tool (APT), a higher-level tool, is more commonly used than `dpkg` as it can fetch packages from remote locations and deal with complex package relations, such as dependency resolution. Frontends for APT, like aptitude (ncurses) and synaptic (GTK), are used for their user-friendly interfaces.

The Debian package *dpkg* provides the `dpkg` program, and several other programs needed for runtime functioning of the packaging system, including `dpkg-deb`, `dpkg-split`, `dpkg-query`, `dpkg-statoverride`, `dpkg-divert` and `dpkg-trigger`. It also includes the programs such as `update-alternatives` and `start-stop-daemon`. The Debian package "dpkg-dev" includes the many build tools described below.

## History

The first attempt at a package management system for Linux was possibly the development of StopAlop by Greg Wettstein at the Roger Maris Cancer Center in Fargo, North Dakota. It provided inspiration to create dpkg. dpkg was originally created by Ian Murdock in January 1994 as a Shell script. Matt Welsh, Carl Streeter and Ian Murdock then rewrote it in Perl, and then later the main part was rewritten in C by Ian Jackson in 1994. The name *dpkg* was originally a shortening of *Debian package*, but the meaning of that phrase has evolved significantly, as dpkg the software is orthogonal to the deb package format and the Debian Policy Manual which defines how Debian packages behave in Debian.

## Development tools

dpkg-dev contains a series of development tools needed to unpack, build, and upload Debian source code packages. These include:

- *dpkg-source* packs and unpacks the source files of a Debian package.
- *dpkg-gencontrol* reads the information from an unpacked Debian tree source and generates a binary package control package, creating an entry for this in Debian/files.
- *dpkg-shlibdeps* calculates the dependencies of runs with respect to libraries.
- *dpkg-genchanges* reads the information from an unpacked Debian tree source that once constructed creates a control file (.changes).
- *dpkg-buildpackage* is a control script that can be used to construct the package automatically.
- *dpkg-distaddfile* adds a file input to debian/files.
- *dpkg-parsechangelog* reads the changes file (changelog) of an unpacked Debian tree source and creates a conveniently prepared output with the information for those changes.

## dselect

The dpkg source package also contains *dselect*, a frontend software.

## install-info

The `install-info` program used to be included in the dpkg software package, but was later removed as it became developed and distributed separately, as part of GNU Texinfo.

## wpkg

*wpkg* was created as a dpkg look-alike that would run under the Microsoft Windows operating system. It retained .deb file format compatibility. It subsequently evolved to include functionality similar to parts of the APT suite, improved repository management, distribution management and was ported to Linux and Unix-like systems. As of March 2024, the most recent release of the software was in 2015.
