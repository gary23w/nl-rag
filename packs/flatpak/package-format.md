---
title: "Package format"
source: https://en.wikipedia.org/wiki/Package_format
domain: flatpak
license: CC-BY-SA-4.0
tags: flatpak sandbox, application sandboxing, ostree tree, freedesktop runtime
fetched: 2026-07-02
---

# Package format

**Package format** is a type of archive containing computer programs and additional metadata needed by package managers; an instance of this type of archive is called a **package**. While the archive file format itself may be unchanged, package formats carry additional metadata, such as a manifest file or certain directory layouts. Packages may contain either source code or executable files.

Packages may be converted from one type to another with software such as Alien.

## Software supply chain and security

Packages are an important component in managing the security and integrity of the software supply chain. Packages containing executables and configuration can be digitally signed to establish the integrity of running software and protect against tampering.

Package formats that support code signing include .deb (Debian), .msi (Microsoft Windows), .apk (Android) and .ipa (IOS, IPadOS).

## Common formats

### Specialized formats

| Format | Consumed by |
|---|---|
| AIR | Adobe AIR |
| Bottle | Homebrew |

### BSD-based formats

| Format | Consumed by |
|---|---|
| .ipa | IOS, IPadOS |
| Ports (BSD) | pkgsrc, FreeBSD, OpenBSD |
| PKG | macOS, iOS, PlayStation 3, Solaris, SunOS, UNIX System V, Symbian, BeOS, Apple Newton |

### Linux-based formats

| Format | Consumed by |
|---|---|
| AAB | Android |
| APK (Alpine) | Alpine Linux |
| APK (Android) | Android |
| AppImage | Linux distribution-agnostic |
| Deb | Debian and its derivatives, such as Raspberry Pi OS, Kali Linux, Ubuntu, and Linux Mint |
| ebuild | Gentoo Linux |
| eopkg | Solus |
| Nixpkg | Nix, NixOS, Home Manager |
| Portage | Gentoo Linux, ChromeOS |
| Flatpak | Linux distribution-agnostic |
| .app, .hap | HarmonyOS, OpenHarmony, Oniro OS and Linux based Unity Operating System |
| PISI | Pardus |
| .pkg.tar.zst | Arch Linux |
| PUP and PET | Puppy Linux (PUP format is deprecated since version 3.0) |
| RPM | Red Hat Enterprise Linux, Fedora, derivatives such as CentOS, and SUSE Linux Enterprise, openSUSE |
| Snap | Linux distribution-agnostic, mainly developed for Ubuntu |

### Windows formats

| Format | Consumed by |
|---|---|
| APPX and APPXBundle | Windows 8 and later, Windows Phone |
| Windows Installer package / MSI | Windows Installer on Microsoft Windows |

### Generic formats

Arch Linux's Pacman and Slackware use 'tar' archives with generic naming but specific internal structures.
