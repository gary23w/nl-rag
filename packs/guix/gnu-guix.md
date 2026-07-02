---
title: "GNU Guix"
source: https://en.wikipedia.org/wiki/GNU_Guix
domain: guix
license: CC-BY-SA-4.0
tags: gnu guix, functional package management, reproducible builds, declarative system
fetched: 2026-07-02
---

# GNU Guix

**GNU Guix** (/ɡiːks/; portmanteau of Guile and Nix) is a functional programming cross-platform package manager and a tool to instantiate and manage Unix-like operating systems, inspired by the Nix package manager. Configuration and package recipes are written in Guile Scheme. GNU Guix is the default package manager of the GNU Guix System distribution.

Differing from traditional package managers, Guix (like Nix) uses a purely functional programming deployment model where software is installed into unique directories generated through cryptographic hash functions. All dependencies for each software are included in the input of each hash. This solves the problem of dependency hell, allowing multiple versions of the same software to coexist which makes packages portable and reproducible. Performing scientific computations in a Guix setup has been proposed as a promising response to the replication crisis.

The development of GNU Guix is intertwined with the GNU Guix System, an installable operating system distribution using the Linux-libre kernel and the GNU Shepherd init system.

## General features

Guix packages are defined through functional Guile Scheme APIs designed for package management. Dependencies are tracked directly in this language through special values named "derivations" which are evaluated by the Guix daemon lazily. Guix keeps track of these references automatically so that installed packages can be garbage collected when no other package depends on them, at the cost of greater storage needs, all upgrades in Guix are guaranteed to be atomic and can be rolled back.

The roll-back feature of Guix is inherited from the design of Nix and is rarely found in other package managers, since it requires an unorthodox approach to how the system should function (see MicroOS). However, the Guix package manager, like Nix, can be used on many distributions like Debian and Parabola. This also enables multiple users to safely install software on the same system without administrator privileges.

Compared to traditional package managers, Guix package stores can grow considerably bigger and therefore require more bandwidth; although compared to container solutions (like Docker) that are also commonly employed to solve dependency hell, Guix is leaner and conforms to practices like don't repeat yourself and single source of truth. If the user chooses to build everything from source, an even larger amount of storage space and bandwidth is required.

## The store

Inherited from the design of Nix, most of the content of the package manager is kept in a directory */gnu/store* where only the Guix daemon has write-access. This is achieved via specialised bind mounts, where the Store as a file system is mounted read only, prohibiting interference even from the root user, while the Guix daemon remounts the Store as read/writable in its own private namespace. Guix talks with this daemon to build things or fetch substitutes which are all kept in the store. Users are discouraged from ever manually touching the store by re-mounting it as writable since this defeats the whole purpose of the store.

### Garbage collection

Guix - like Nix - has built-in garbage collection facilities to help prune *dead* store items and keep the *live* ones.

## Package definitions

This is an example of a package definition for the hello-package:

```mw
(use-modules
  (guix packages)
  (guix download)
  (guix build-system gnu)
  (guix licenses))

(define-public hello
  (package
   (name "hello")
   (version "2.10")
   (source (origin
            (method url-fetch)
            (uri (string-append "mirror://gnu/hello/hello-" version
                                ".tar.gz"))
            (sha256
             (base32
              "0ssi1wpaf7plaswqqjwigppsg5fyh99vdlb9kzl7c9lng89ndq1i"))))
   (build-system gnu-build-system)
   (synopsis "Hello, GNU world: An example GNU package")
   (description
    "GNU Hello prints the message \"Hello, world!\" and then exits.  It
 serves as an example of standard GNU coding practices.  As such, it supports
 command-line arguments, multiple languages, and so on.")
   (home-page "https://www.gnu.org/software/hello/")
   (license gpl3+)))
```

It is written using Guile. The package recipes can easily be inspected (running e.g. guix edit hello) and changed in Guix, making the system transparent and very easy to modify.

## Transactional upgrades

Inherited from the design of Nix, all manipulation of store items is independent of each other, and the directories of the store begin with a base32-encoded hash of the source code of the derivation along with its inputs.

## Profiles

Guix package uses profiles generations, which are a collection of symbolic links (also known as "symlinks") to specific store items together comprising what the user has installed into the profile. Every time a package is installed or removed, a new generation will be built. For example, the profile of a user who only installed GNU Hello contains links to the store item which holds the version of hello installed with the currently used Guix. On version `c087a90e06d7b9451f802323e24deb1862a21e0f` of Guix, this corresponds to the item: `/gnu/store/md2plii4g5sk66wg9cgwc964l3xwhrm9-hello-2.10` (built from the recipe above).

In addition to symbolic links, each profile that Guix builds also contains a union of all the info-manuals, and the man pages, icons, fonts, etc., so a user can browse documentation and have access to all the icons and fonts installed. The default symbolic links to profile generations are stored under `/var/guix`.

### Multiple user profiles

The user can create any number of profiles by invoking guix package -p PROFILE-NAME COMMAND. A new directory with the profile-name as well as profile-generation-symlinks will then be created in the current directory.

## Roll-back

Guix package enables instantaneous roll-back to a previous profile generation via changing the symlink to an earlier profile generation. Profiles are also stored in the store e.g. this item is a profile containing hello above: /gnu/store/b4wipjlsapvnijmbawl7sh76087vpl4n-profile (built and activated when running guix install hello).

## Shell environment

Guix shell enables the user to easily enter an environment where all the necessary packages for development of software are present without clogging up the user's default profile with dependencies for multiple projects.

E.g., running guix shell --development hello enters a throw-away environment where everything needed to compile *hello* on Guix is present (GNU Compiler Collection (GCC), Guile, etc.).

Without the --development flag, only the package *hello* would be installed and not its build-dependencies. This supplants the guix environment command, which installs the dependencies of a package by default, as it was considered more intuitive for the command to install the specified packages by default and only install development dependencies with a flag.

### Persistent development environment

If a user wants a persistent gc-rooted environment that is not garbage collected on the next run of the Guix garbage collector they can create a root: e.g. running guix shell --root=hello-root --development hello enters an environment where everything needed to compile Guix is present and registered as a root in the current directory (by symlinking to the items in the store).

## Pack

Guix pack enables the user to bundle together store items and output them as either a Docker binary image, a relocatable tarball, a Debian package file, a RPM package file, an AppImage or a SquashFS binary.

## Graph

The Guix graph feature enables the user to view different graphs of the packages and their dependencies.

## Third-party channels

Guix allows the user to specify additional channels for package definitions.

This feature can also be used to install non-free software and firmware that cannot be packaged in the main project.

## GNU Guix System (operating system)

**GNU Guix System** or **Guix System** (formerly named **GuixSD**) is a rolling release, free and open source Linux distribution built on Guix, similar to how NixOS is built on Nix. It enables a declarative programming operating system configuration and allows system upgrades that the user can roll back. It uses the GNU Shepherd init system and the Linux-libre kernel, with the support of the GNU Hurd kernel under development. On February 3, 2015, the Free Software Foundation added the distribution to its list of endorsed free Linux distributions.

### Architecture support

Central processing unit (CPU) architecture support includes:

- IA-32
- x86-64
- ARMv7
- AArch64
- POWER9
- RISC-V 64
- MIPS64

### System services

System services, which are defined in the Guile Scheme, enable the user to declaratively compose the configuration of daemons and background services and specify configurations. This enables the user, within a single configuration file or modularized configuration, to configure the whole operating system (e.g., to have a Tor proxy, an ssh server, and a webserver serving guix-web via nginx on a specific port at bootup). They can:

- generate files in the filesystem (needed by some applications e.g. files in */etc*)
- run any code for setting up daemons
- create specific user and group accounts (e.g. a database user for PostgreSQL)

### GNU Shepherd init system

The GNU Guix System uses the *GNU Daemon Shepherd*, formerly known as *Daemon managing Daemons* (dmd), as its init system, which is developed in tandem with Guix and is written and configurable in Guile. It supplies user-space functionality asynchronously as services, which under Shepherd are generic functions and object data types which it uses to extend the base operating system in a defined way. In contrast to systemd, a userspace shepherd process runs as the user. Central to the Shepherd model of user space initialization is the concept of the *extension*, a form of composability whereby services are designed to be layered onto other services, augmenting them with more elaborate or specialized behaviours as desired. This expresses the instantiation-based dependency relationships found in many modern init systems, making the system modular, but also allows services to interact variadically with other services in arbitrary ways, e.g. a service that extends two other services, *requiring* only one to be present, but readily extending the second one if it is later instantiated without the need for any further reconfiguration or setup.

Shepherd also provides *virtual services* which allow dynamic dispatch over a class of related service objects, such as all those which instantiate a mail transfer agent (MTA) for the system. A system governed via the Shepherd daemon can represent its user space as a directed acyclic graph, with the "system-service," which is responsible for early phases of booting up the system and initializing it, as its root, and all subsequently initialized services as extensions to system-service functionality, either directly or transitively over other services.

It is intended to be highly programmable by the system administrator using Guile Scheme, but it can also be used to manage per-user profiles of unprivileged daemons and services. Its services and configuration are stored uniformly as object-oriented Scheme code, and while a core set of services are provided with the basic GNU Guix System, arbitrary new services can be flexibly declared, and through Guile's object system, GOOPS, existing services can be redefined at the user's discretion by asking the Shepherd to dynamically rewrite services in specified ways on instantiation.

GNU Shepherd was originally designed to work with GNU Hurd, and was later adopted by GNU Guix System.

### Roll-back

Similar to the roll-back feature of Nix, if a system update leaves users with a broken system, users can easily roll back individual packages as well as the whole system state with a single command, `guix package --roll-back`. This means that the kind of stable channel that is very common in other Linux distributions is no longer needed for users who are willing to report a bug and wait a few minutes, when trying to update via *guix pull*. This is accomplished by a combination of Guix's functional package manager, which treats each package and system configuration as an immutable and reproducible entity, and the generation system which maintains a history of system configurations as "generations." These generations are stored as separate profiles, which allows the user to roll back to any previous configuration, and these generations can be shown with `guix package --list-generations`.

### Reception

Jesse Smith from DistroWatch Weekly reviewed GNU Guix System 0.15.0 (then named GuixSD), and said, "GuixSD has a package manager that I like", but criticized the limited hardware support and its limited documentation. The documentation has since then been expanded and improved with videos and a cookbook in six languages with tutorials, how-to guides and examples.

## Reproducible scientific workflows

One area where Guix aims to improve over traditional package managers is in the field of reproducible scientific workflows, mainly in *high-performance computing*. In this way, Guix would offer a way to share a reproducible computational environment, i.e., Guix using a recipe for a given scientific software and environment would provide all the information needed to uniquely describe the dependency tree to build and run that software. This would not be easy to achieve, for example, in other mixed systems with several package managers for each programming language. However, this only provides a necessary but insufficient condition for scientific workflows to be reproducible, as it is necessary to incorporate data collection and processing into the workflow. If this is added as part of the Guix recipe, it could satisfy the strict reproducibility requirements.

## History

The project began in June 2012 by Ludovic Courtès, one of the GNU Guile hackers.

The GNU Project announced in November 2012 the first release of GNU Guix, a functional package manager inspired by Nix that provides, among other things, Guile Scheme application programming interfaces (APIs).

On August 20, 2015, it was announced that Guix had been ported to GNU Hurd.

## Releases

The project has no fixed release schedule and has until now released approximately every 6 months.

The project migrated away from GNU Savannah to Codeberg on May 25th 2025.

### Version history

| Version | Announcement | Supported architectures | Packages |
|---|---|---|---|
| 0.1 (alpha) | *Courtès, Ludovic (18 January 2013). "GNU Guix 0.1 released (alpha)".* | i686x86-64 | ~150 |
| 0.2 (alpha) | *Courtès, Ludovic (12 May 2013). "GNU Guix 0.2 released (alpha)".* | ~400 |   |
| 0.3 | *Courtès, Ludovic (17 Jul 2013). "GNU Guix 0.3 released".* | ~430 |   |
| 0.4 | *Courtès, Ludovic (27 Sep 2013). "GNU Guix 0.4 released".* | ~490 |   |
| 0.5 | *Courtès, Ludovic (11 Dec 2013). "GNU Guix 0.5 released".* | ~600 |   |
| 0.6 | *Courtès, Ludovic (9 Apr 2014). "GNU Guix 0.6 released".* | ~691 |   |
| 0.7 | *Courtès, Ludovic (25 Jul 2014). "GNU Guix 0.7 released".* | ~825 |   |
| 0.8 | *Courtès, Ludovic (18 Nov 2014). "GNU Guix 0.8 released".* | i686x86-64mips64el | ~987 |
| 0.8.1 | *Courtès, Ludovic (29 Jan 2015). "GNU Guix 0.8.1 released".* | i686x86-64mips64elarmv7 | ~1,151 |
| 0.8.2 | *Courtès, Ludovic (14 May 2015). "GNU Guix 0.8.2 released".* | ~1,869 |   |
| 0.8.3 | *Courtès, Ludovic (22 Jul 2015). "GNU Guix 0.8.3 released".* | ~2,048 |   |
| 0.9.0 | *Courtès, Ludovic (5 Nov 2015). "GNU Guix 0.9.0 released".* | ~2,591 |   |
| 0.10.0 | *Courtès, Ludovic (29 Mar 2016). "GNU Guix & GuixSD 0.10.0 released".* | ~3,230 |   |
| 0.11.0 | *Courtès, Ludovic (3 Aug 2016). "GNU Guix & GuixSD 0.11.0 released".* | ~3,714 |   |
| 0.12.0 | *Wurmus, Ricardo (21 December 2016). "GNU Guix & GuixSD 0.12.0 released".* | ~4,567 |   |
| 0.13.0 | *Courtès, Ludovic (22 May 2017). "GNU Guix & GuixSD 0.13.0 released".* | i686x86-64mips64elarmv7aarch64 | ~5,407 |
| 0.14.0 | *Courtès, Ludovic (7 Dec 2017). "GNU Guix & GuixSD 0.14.0 released".* | ~6,618 |   |
| 0.15.0 | *Courtès, Ludovic (6 Jul 2018). "GNU Guix & GuixSD 0.15.0 released".* | ~7,857 |   |
| 0.16.0 | *Courtès, Ludovic (6 Dec 2018). "GNU Guix & GuixSD 0.16.0 released".* | ~8,715 |   |
| 1.0.0 | *Courtès, Ludovic (2 May 2019). "GNU Guix 1.0.0 released".* | ~9,712 |   |
| 1.0.1 | *Courtès, Ludovic (19 May 2019). "GNU Guix 1.0.1 released".* | ~9,771 |   |
| 1.1.0 | *Courtès, Ludovic (15 April 2020). "GNU Guix 1.1.0 released".* | i686x86-64armv7aarch64 | ~13,161 |
| 1.2.0 | *Courtès, Ludovic (23 November 2020). "GNU Guix 1.2.0 released".* | ~15,333 |   |
| 1.3.0 | *Courtès, Ludovic (11 May 2021). "GNU Guix 1.3.0 released".* | i686x86-64powerpc64learmv7aarch64 | ~17,262 |
| 1.4.0 | *Courtès, Ludovic (19 December 2022). "GNU Guix 1.4.0 released".* | i686x86-64powerpc64learmv7aarch64 | ~22,000 |
| 1.5.0 | *Courtès, Ludovic (23 January 2026). "GNU Guix 1.5.0 released".* | i686x86-64powerpc64learmv7aarch64riscv64 | ~34,000 |
