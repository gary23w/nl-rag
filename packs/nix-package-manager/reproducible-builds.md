---
title: "Reproducible builds"
source: https://en.wikipedia.org/wiki/Reproducible_builds
domain: nix-package-manager
license: CC-BY-SA-4.0
tags: nix package manager, reproducible builds, functional package management, declarative packaging
fetched: 2026-07-02
---

# Reproducible builds

**Reproducible builds**, also known as **deterministic compilation**, is a process of building software which ensures the resulting binary code can be reproduced. Source code compiled deterministically will always output the same binary.

Reproducible builds can act as part of a chain of trust; the source code can be signed, and deterministic compilation can prove that the binary was compiled from trusted source code. Verified reproducible builds provide a strong countermeasure against attacks where binaries do not match their source code, e.g., because an attacker has inserted malicious code into a binary. This is a relevant attack; attackers sometimes attack binaries but not the source code, e.g., because they can only change the distributed binary or to evade detection since it is the source code that developers normally review and modify. In a survey of 17 experts, reproducible builds had a very high utility rating from 58.8% participants, but also a high-cost rating from 70.6%. Various efforts are being made to modify software development tools to reduce these costs.

## Methods

For the compilation process to be deterministic, the input to the compiler must be the same, regardless of the build environment used. This typically involves normalizing variables that may change, such as order of input files, timestamps, locales, and paths.

Additionally, the compilers must not introduce non-determinism themselves. This sometimes happens when using hash tables with a random hash seed value. It can also happen when using the address of variables because that varies from address space layout randomization (ASLR).

Build systems, such as Bazel, GNU Guix, and Gitian, can be used to automate deterministic build processes.

## History

The GNU Project used reproducible builds in the early 1990s. Changelogs from 1992 indicate the ongoing effort.

One of the older projects to promote reproducible builds is the Bitcoin project with Gitian, and later, GNU Guix. In 2013, the Tor (anonymity network) project started using Gitian for their reproducible builds.

Starting in 2011, a reproducible Java build system was developed for the decentralized peer-to-peer FOSS project DirectDemocracyP2P. The concepts of the system's application to automated updates recommendation support was first presented in April 2013 at Decentralized Coordination. A treatise focusing on the implementation details of the reproducible Java compilation tool itself was published in 2015.

In July 2013, the Debian project started implementing reproducible builds across its entire package archive. By July 2017, more than 90% of the packages in the repository were proven to build reproducibly.

In November 2018, the Reproducible Builds project joined the Software Freedom Conservancy.

F-Droid uses reproducible builds to provide a guarantee that distributed APKs use the claimed free source code.

The Tails portable operating system uses reproducible builds and explains to others how to verify their distribution.

NixOS claims 100% build reproducibility as of June 2021 for their minimal ISO releases.

As of May 2020, Arch Linux is working on making all official packages reproducible.

As of March 2025, Debian live images for Bookworm are reproducible.

The FreeBSD operating system builds reproducibly and without root access since October 2025.

## Challenges

According to the Reproducible Builds project, timestamps are "the biggest source of reproducibility issues. Many build tools record the current date and time... and most archive formats will happily record modification times on top of their own timestamps." They recommend that "it is better to use a date that is relevant to the source code instead of the build: old software can always be built later" if it is reproducible. They identify several ways to modify build processes to do this:

- Set the SOURCE_DATE_EPOCH environment variable to the number of seconds since January 1, 1970, using something from the source code. Tools that support this environment variable will use its value (when set) instead of the current date and time.
- Post-process output to remove timestamps or normalize them. The tool strip-nondeterminism can often help do this.
- Use a library like libfaketime to intercept requests for the current time of day and provide a controlled response.

In some cases other changes must be made to make a build process reproducible. For example, some data structures do not guarantee a stable order in each execution. A typical solution is to modify the build process to specify a sorted output from those structures.
