---
title: "fwupd"
source: https://en.wikipedia.org/wiki/Fwupd
domain: fwupd
license: CC-BY-SA-4.0
tags: fwupd, embedded systems
fetched: 2026-07-02
---

# fwupd

**fwupd** is an open-source daemon for managing the installation of firmware updates on Linux-based systems, developed by GNOME maintainer Richard Hughes. It is designed primarily for servicing the Unified Extensible Firmware Interface (UEFI) firmware on supported devices via EFI System Resource Table (ESRT) and UEFI Capsule, which is supported in Linux kernel 4.2 and later. Previously, the initiation of UEFI firmware updates within an operating system could, on most systems, only be performed using Microsoft Windows or DOS-specific software. ESRT allows the firmware to expose updatable components to the operating system, which can pass a UEFI capsule with updated firmware for processing and installation on the next boot. fwupd can also process other types of firmware update, for example SSD firmware. Updates can be exposed via a command line tool, or within graphical package managers (such as GNOME Software) via a D-Bus interface.

## Linux Vendor Firmware Service

The Linux Vendor Firmware Service (LVFS) provides resources and support for helping vendors package their firmware updates to support the use of this framework, and serves as an online repository for obtaining these updates. To provide a test case on systems where ESRT is not yet supported, fwupd is also able to update firmware on the ColorHug color calibrator.

## Adoption

Several Linux distributions use fwupd, including:

- Arch from 2017-06-13
- Debian 9 (Stretch) or newer
- Ubuntu 16.04 (Xenial) or newer
- Fedora 22 or newer
- RHEL and CentOS 7.4 or newer
- openSUSE 15.0 or newer

In December 2015, it was revealed that Hughes had been working with a Dell developer to test the system on actual hardware, and that its Dell Edge Gateway product will support firmware servicing via fwupd. Hughes reported that the company was also "considering expanding out the LVFS support to all new models supporting UEFI updates". In August 2018, Lenovo joined the project and provides update support for a wide range of their devices.

In September 2019, Acer joined the project, with initial support for their Aspire A315 model. Starting from December 2019, Google requires that firmware updates can be applied with fwupd for certified Chromebooks.
