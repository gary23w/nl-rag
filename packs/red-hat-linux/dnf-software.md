---
title: "DNF (software)"
source: https://en.wikipedia.org/wiki/DNF_(software)
domain: red-hat-linux
license: CC-BY-SA-4.0
tags: red hat enterprise linux, yum package manager, dnf tool, centos rebuild
fetched: 2026-07-02
---

# DNF (software)

**DNF** (abbreviation for **Dandified YUM**) is a package manager for Red Hat-based Linux distributions and derivatives. DNF was introduced in Fedora 18 in 2013 as a replacement for yum; it has been the default package manager since Fedora 22 in 2015 and Red Hat Enterprise Linux 8 in 2019 and is also an alternative package manager for Mageia. DNF performs package management tasks on top of RPM, and supporting libraries.

## Usage

The DNF package manager works similarly to other package managers. Its core usage works very similarly to the Apt Package Manager, such as `install`, `remove`, and `upgrade`.

Usage for basic command is as follows:

`sudo dnf list`

`sudo dnf search <pattern>`

`sudo dnf info <package_name>`

`sudo dnf install <package_name>`

`sudo dnf remove <package_name>`

`sudo dnf upgrade`

`sudo dnf distro-sync`

## History

Perceived deficiencies of yum (which DNF is intended to address) include poor performance, high memory usage, and the slowness of its iterative dependency resolution. DNF uses libsolv, an external dependency resolver (developed by openSUSE).

DNF was originally written in Python, but in 2016, efforts were under way to port it to C and move most functionality from Python code into the new libdnf library. In 2018, the DNF team announced the decision to move libdnf from C to C++. libdnf is already used by PackageKit, a Linux distribution-agnostic package system abstraction library, even though the library doesn't have most of DNF's features.

Since the launch of Fedora Linux 41, DNF5 is the new default packaging tool. This release features new performance enhancements, updated terminal output, and fully integrated modularity.

## Adoption

DNF has been the default command-line package manager for Fedora since version 22, which was released in May 2015. The libdnf library is used as a package backend in PackageKit, which offers a graphical user interface (GUI). Later, dnfdragora was developed for Fedora 27 as another alternative graphical front-end of DNF. DNF has also been available as an alternate package manager for Mageia Linux since version 6 and may become the default sometime in the future.

In Red Hat Enterprise Linux, and by extension, AlmaLinux and Rocky Linux, yum is an alias for dnf.
