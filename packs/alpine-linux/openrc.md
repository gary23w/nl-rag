---
title: "OpenRC"
source: https://en.wikipedia.org/wiki/OpenRC
domain: alpine-linux
license: CC-BY-SA-4.0
tags: alpine linux, musl libc, busybox utilities, openrc init
fetched: 2026-07-02
---

# OpenRC

**OpenRC** is a dependency-based init system for Unix-like computer operating systems. It was created by Roy Marples, a NetBSD developer who was also active in the Gentoo project.

## Adoption

OpenRC is the default init system or process supervisor for:

- Alpine Linux
- ArchBang
- Calculate Linux
- Funtoo
- Gentoo Linux
- Hyperbola GNU/Linux-libre
- Maemo Leste
- Nitrux

OpenRC is available as an init system or process supervisor for:

- Artix Linux
- Devuan
- Parabola GNU/Linux-libre
- Arch Linux (available through the Arch User Repository)
- postmarketOS
- Debian

## Design

OpenRC is made up of several modular components, the main ones being an init (optional), the core dependency management system, and a daemon supervisor (optional). It is written in C and POSIX-compliant shell, making it usable on BSD and Linux systems.

The core part of OpenRC handles dependency management and init script parsing. OpenRC works by scanning the runlevels, building a dependency graph, then starting the needed service scripts. It exits once the scripts have been started. By default, OpenRC uses a modified version of start-stop-daemon for daemon management.

Init scripts share similarities with scripts used in sysvinit, but offer several features to simplify their creation. Scripts are assumed to have `start()`, `stop()` and `status()`; and the system uses variables already declared to create the default functions. The depend function is used to declare dependencies to other services that would be done with LSB headers in sysvinit. Configuration and mechanism are separated with configuration files in the conf.d directory and init files in the init.d directory.

openrc-init first appeared in version 0.25 as an optional replacement for `/sbin/init`. This can replace Gentoo Linux's default init system, sysvinit.

Supervise-daemon first appeared in version 0.21 giving OpenRC supervision capabilities. It can be enabled in the init script for supervise-daemon to start and monitor a daemon. Several other daemon supervisors are supported, including runit and s6.

## Features

- Portable between Linux, FreeBSD, and NetBSD
- Parallel service startup (off by default)
- Dependency-based boot-up
- Process segregation through cgroups
- Per-service resource limits (ulimit)
- Separation of code and configuration (init.d / conf.d)
- Extensible startup scripts
- Stateful init scripts (*has it started already?*)
- Complex init scripts to start multiple components (Samba [smbd and nmbd], NFS [nfsd, portmap, etc.])
- Automatic dependency calculation and service ordering
- Modular architecture and separation of optional components (cron, syslog)
- Expressive and flexible network handling (including VPN, bridges, etc.)
- Verbose debug mode
- User services
