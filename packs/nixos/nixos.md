---
title: "NixOS"
source: https://en.wikipedia.org/wiki/NixOS
domain: nixos
license: CC-BY-SA-4.0
tags: nixos distribution, declarative linux distribution, reproducible system configuration, immutable operating system
fetched: 2026-07-02
---

# NixOS

**NixOS** is a Linux distribution built around the Nix package manager. Unlike traditional Linux distributions, NixOS is configured using a functional language that describes the system configuration. It generates complete system profiles, enabling reproducible deployments, atomic upgrades, and system rollbacks.

NixOS relies on the Nixpkgs collection of package definitions and the Nix expression language for declaring packages and system options. It is free and open-source software under the MIT License.

## History

Nix as a package manager originated in 2003 as a research project by Eelco Dolstra at Utrecht University under the supervision of Eelco Visser. Dolstra’s 2006 doctoral thesis, The Purely Functional Software Deployment Model, describes a declarative and functional approach to software deployment and lays out the design of the Nix package manager.

The first NixOS prototype was created by Armijn Hemel in 2006 as part of his Master's thesis *NixOS: The Nix Based Operating System*, which explored applying Nix and its principles to a Linux distribution. Hemel demonstrated the application of package management, system services, kernel management, and other principles that defined NixOS. After continued development, NixOS issued its first stable release, version 13.10, in 2013.

The NixOS Foundation, a Dutch non-profit established in 2015, supports the development and community infrastructure of NixOS and related Nix projects.

## Release version history

| Version | Name | Date |
|---|---|---|
| Unsupported: 13.10 | Aardvark | December 1, 2013 |
| Unsupported: 14.04 | Baboon | May 30, 2014 |
| Unsupported: 14.12 | Caterpillar | January 30, 2015 |
| Unsupported: 15.09 | Dingo | October 30, 2015 |
| Unsupported: 16.03 | Emu | May 1, 2016 |
| Unsupported: 16.09 | Flounder | October 3, 2016 |
| Unsupported: 17.03 | Gorilla | May 31, 2017 |
| Unsupported: 17.09 | Hummingbird | October 2, 2017 |
| Unsupported: 18.03 | Impala | April 4, 2018 |
| Unsupported: 18.09 | Jellyfish | October 6, 2018 |
| Unsupported: 19.03 | Koi | April 10, 2019 |
| Unsupported: 19.09 | Loris | October 9, 2019 |
| Unsupported: 20.03 | Markhor | April 20, 2020 |
| Unsupported: 20.09 | Nightingale | October 27, 2020 |
| Unsupported: 21.05 | Okapi | June 1, 2021 |
| Unsupported: 21.11 | Porcupine | November 30, 2021 |
| Unsupported: 22.05 | Quokka | May 30, 2022 |
| Unsupported: 22.11 | Raccoon | December 1, 2022 |
| Unsupported: 23.05 | Stoat | May 31, 2023 |
| Unsupported: 23.11 | Tapir | November 29, 2023 |
| Unsupported: 24.05 | Uakari | May 31, 2024 |
| Unsupported: 24.11 | Vicuña | November 30, 2024 |
| Unsupported: 25.05 | Warbler | May 23, 2025 |
| Supported: 25.11 | Xantusia | November 30, 2025 |
| Latest version: 26.05 | Yarara | May 30, 2026 |
| Future version: 26.11 | Zokor |   |
| **Legend:**UnsupportedSupported**Latest version**Preview versionFuture version |   |   |

Since 2021, NixOS publishes stable releases twice per year, near the ends of May and November. Prior to the first stable release in 2013, major versions were numbered semantically, up to release 0.2.

In addition to the stable release, NixOS maintains a rolling, unstable release following the main development branch.

## Features

### Declarative configuration model

In NixOS, the entire operating system—including the kernel, applications, system packages, and configuration files—is built by the Nix Package manager from a definition in the Nix language. Building a new version will not overwrite previous versions.

A NixOS system is configured by specifying the desired state in a Nix expression file, typically `/etc/nixos/configuration.nix`. The following example configures the bootloader and enables the OpenSSH daemon:

```mw
{
  boot.loader.grub.device = "/dev/sda";
  fileSystems."/".device = "/dev/sda1";
  services.openssh.enable = true;
}
```

Changes may be built and activated with the `nixos-rebuild` command, which evaluates the configuration, builds the necessary derivations, and produces a new system generation.

### Atomic upgrades and rollbacks

Configurations in Nix are evaluated as pure, declarative expressions. Given the same inputs (such as the Nixpkgs revision and configuration files), evaluation is deterministic and produces the same build plan, independent of the machine's prior state.

Upgrades and configuration changes to NixOS systems are applied transactionally. New system generations are activated atomically, so that previous generations are retained and may be rolled back. If an upgrade is interrupted (for example, by power failure), the system remains consistent and will boot either the old or the new configuration.

If, after a system update, the new configuration is undesirable, it may be rolled back by switching to a previous generation (`nixos-rebuild switch --rollback`). New generations are automatically added to the system bootloader and may be selected prior to boot. Rollbacks are lightweight operations that switch system references to different store paths.

### Reproducible system configurations

NixOS uses a declarative configuration model that allows system configurations to be reproduced on different machines. By sharing a configuration file with a target machine, users can generate an equivalent system, including the kernel, applications, and system services. Components not managed by the package manager, such as user data, are not affected by this process.

### Multi-user package management

In addition to the system-wide profile, every normal user in a NixOS system has a profile in which they can install packages without special privileges. In the Nix store, multiple versions of a package may coexist, allowing different users to have alternate versions of the same package installed in their respective profiles, or share an identical version.

Nix’s security model restricts what unprivileged users can influence. Prebuilt binaries may be fetched from binary caches that are explicitly trusted by the system configuration, otherwise packages are built locally in a sandbox. Without special privileges, users cannot pass options that would introduce impurities into builds or use untrusted caches.

### Nix-shell

The nix-shell command starts an interactive shell based on a Nix expression. It allows developers to work with isolated sets of dependencies without affecting the system globally.

### Experimental features

#### Nix command

The `nix` command provides a redesigned command-line interface for the Nix package manager, intended to replace the traditional `nix-env`, `nix-build`, and related commands. It introduces a more consistent syntax and improved user experience with commands such as `nix build`, `nix develop`, and `nix run`. The goal was to simplify common operations and provide better functionality through a unified command structure.

#### Flakes

Flakes provide a standard structure for Nix expressions that explicitly declare dependencies and outputs. Each flake contains a flake.nix file that specifies its inputs (dependencies, external flakes, repositories) and outputs (packages, NixOS configurations, and development environments). Flakes use a lock file to keep exact versions of dependencies to ensure that evaluations remain reproducible over time. The feature provides a standardized way to define, manage, and share Nix expressions, while making it easier to create and maintain reproducible systems.

## Implementation

### The Nix store

Installed packages are stored in a read-only directory known as the Nix store, commonly located at `/nix/store`. Packages in the store are identified by a cryptographic hash of all input used for their build. This system is also used to manage configuration files, ensuring that newer configurations do not overwrite older ones.

An implication of these principles is that NixOS does not follow the Filesystem Hierarchy Standard. The only exceptions are that a /bin/sh symlink is created to the version of bash in the Nix store (e.g. `/nix/store/s/5rnfzla9kcx4mj5zdc7nlnv8na1najvg-bash-4.3.43/`), and while NixOS does have an /etc directory to keep system-wide configuration files, most files in that directory are symlinks to generated files in the Nix store, such as `/nix/store/s2sjbl85xnrc18rl4fhn56irkxqxyk4p-sshd_config`. By not using global directories such as /bin, Nix allows multiple versions of a package to coexist, avoiding package conflicts sometimes known as "dependency hell".

This also means that AppImage executables cannot be run directly as they expect certain libraries to exist on certain paths. This can be worked around by running them through an interpreter.

Nix maintains consistency between the running system and its logical specification by rebuilding packages as needed. When the kernel is modified, external kernel modules are automatically rebuilt. Similarly, updates to libraries trigger rebuilds of all system packages that depend on them, including those with static linking.

### Source-based model with binary cache

The Nix build language used by NixOS specifies how to build all packages from source. This makes it easy to adapt the system to user needs and create new packages. To avoid long and intensive builds from source, the package manager automatically downloads pre-built binaries from a cache server known as a "substituter" when they are available. It is possible to disable substitutions and force building from source by passing `--option substitute false` to a build. Changing any of the build options from the defaults will also cause packages to be built from source. This gives the flexibility of a source-based package management model, with the efficiency of a binary model.

## Reception

Jesse Smith, reviewing NixOS 15.09 for DistroWatch Weekly in 2015, wrote:

> I very much like the way NixOS takes the worry out of upgrading packages by placing each change in its own "generation" and I found, from the end user's point of view, NixOS worked just the same as any other Linux distribution. Setting up NixOS is not for beginners, and I do not think NixOS is intended to be used as a general purpose desktop operating system. But what NixOS does do is give us a useful playground in which to examine the Nix package manager and I think this is very interesting technology which deserves further exploration and adoption by additional distributions.

A 2022 review of NixOS 21.11 "Porcupine" in Full Circle concluded:

> Overall NixOS Gnome 21.11 impresses as serious, neat and elegant. If you are a fan of the unmodified Gnome desktop, then you will find a lot to like here. The downside of this distribution is the steep learning curve for package management, including updates and the like. No matter which distribution you come from, you will have much to learn to be able to make Nix work well for you on the command-line.

NixOS 22.11 "Raccoon" reviewed by Liam Proven at The Register:

> Compared to reports of NixOS from just two or three years ago, we found it was very simple to get it installed and working. This suggests that the tools are maturing well and reaching a certain level of polish, but from a first-time perspective we have no prior baseline to compare against. This is very much not a traditional distro, or even a traditional Unix, but it works and we can see the appeal.

NixOS 23.11 "Tapir" reviewed by Jesse Smith at DistroWatch:

> NixOS is a rare gem in that I don't think I ran into any errors while I was using it. The distribution was stable, it worked well with my hardware, and I didn't run into a single issue while running it. I feel NixOS is well worth a try, especially if you're a system administrator and want to deploy (or maintain) identical distributions across multiple machines.

## Community

### Wiki

An official NixOS wiki was launched in 2011, but was shut down in 2016 due to spam. An unofficial wiki at nixos.wiki was later started by the community to fill in the documentation gap. On 1 April 2024, the official wiki was revived at wiki.nixos.org, using contents migrated from the unofficial nixos.wiki.

### French government

The French government's Interministerial Products Operator (OPI) department of DINUM (Interministerial Directorate for Digital Affairs) is developing **Sécurix**, a secure, reproducible operating system base built on NixOS. This is part of a plan to require all French ministries to create a strategy by autumn 2026 to adopt non-American tech for PC operating systems, collaboration tools, antivirus software, artificial intelligence, databases, virtualization, and network equipment.
