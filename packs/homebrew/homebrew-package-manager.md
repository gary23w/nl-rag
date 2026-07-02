---
title: "Homebrew (package manager)"
source: https://en.wikipedia.org/wiki/Homebrew_(package_manager)
domain: homebrew
license: CC-BY-SA-4.0
tags: homebrew macos, package manager, formula cookbook, unix packages
fetched: 2026-07-02
---

# Homebrew (package manager)

**Homebrew** is a free and open-source software package management system that simplifies the installation of software on Apple's operating system, macOS, as well as Linux. The name is intended to suggest the idea of building software on the Mac depending on the user's taste. Originally written by Max Howell, the package manager has gained popularity in the Ruby on Rails community and earned praise for its extensibility. Homebrew uses a beer-themed naming convention for its features; for example, third-party repositories are called "taps", and binary packages are called "bottles". It has been recommended for its ease of use as well as its integration into the command-line interface. Homebrew is a member of the Open Source Collective, and is run entirely by unpaid volunteers.

Homebrew has made extensive use of GitHub to expand the support of several packages through user contributions. In 2010, Homebrew was the third-most-forked repository on GitHub. In 2012, Homebrew had the largest number of new contributors on GitHub. In 2013, Homebrew had both the largest number of contributors and issues closed of any project on GitHub.

Homebrew has spawned several sub-projects such as Linuxbrew, a Linux port now officially merged into Homebrew; Homebrew Cask, which builds upon Homebrew and focuses on the installation of GUI applications; and "taps" dedicated to specific areas or programming languages like PHP.

## History

Homebrew was written by Max Howell in 2009. In March 2013, Homebrew successfully completed a Kickstarter campaign to raise funds for servers to test and build formulae and managed to raise £14,859. On December 13, 2013, the Homebrew repository migrated from Howell's GitHub account to its own project account. In February 2015, due to downtime at SourceForge which resulted in binaries being unavailable, Homebrew moved their hosting to Bintray. On September 21, 2016, Homebrew version 1.0.0 was released. In January 2019, Linuxbrew was merged back into Homebrew, adding beta support for Linux and the Windows Subsystem for Linux to the Homebrew feature set. On February 2, 2019, Homebrew version 2.0.0 was released. On September 21, 2020, Homebrew version 2.5.2 was released with support for bottle taps (binary package repositories) via GitHub Releases. Version 3.0.0 was released almost exactly two years after 2.0.0, on February 5, 2021, and added official support for Macs with Apple silicon. As of February 2021, Homebrew is maintained by a team of 34 people. On April 12, 2021, Homebrew version 3.1.0 was released completing their migration of bottles (binary packages) to GitHub Packages before the May 1, 2021 shutdown of Bintray as previously announced by JFrog. On February 16, 2023, Homebrew version 4.0.0 was released which defaults to fetching Homebrew-maintained formulae from hosted JSON files rather than local Git-cloned taps.

## Implementation

Homebrew is written in the Ruby programming language and targets the version of Ruby that comes installed with the macOS operating system. By default, it is installed into `/usr/local` on Intel-based machines and `/opt/homebrew` on Apple silicon. The installation consists of a Git repository that enables users to update Homebrew by pulling an updated repository from GitHub. The package manager builds software from source using "formulae", Ruby scripts constructed with the Homebrew domain-specific language (DSL) for managing dependencies, downloading source files, and configuring and compiling software. Binary packages called "bottles" provide pre-built formulae with default options.

Homebrew does not honor the default privileges of `/usr/local`; directory ownership is changed from root with group permissions for the wheel group to the installing user and the "admin" group. Specifically, the mode changes from `drwxr-xr-x root wheel` to `drwxrwxr-x myuser admin`. All files, not just the directories, have their ownership changed by the installer. This is considered by some as a major security flaw.

## Data collection

Homebrew collects installation, build error, and operating system version statistics via InfluxDB. As of Homebrew 4.0.23, no data is collected via Google Analytics. Users can view analytics data from the last 30, 90, and 365 days on the Homebrew website.

It is possible to opt out of data collection with the command `brew analytics off`.

## Operating system support

Homebrew typically supports macOS versions for which Apple still releases security updates, *i.e.*, the current major version of macOS as well as the two previous (major) versions. As of June 2026 this included macOS 14 Sonoma, macOS 15 Sequoia, macOS 26 Tahoe, and MacOS 27 Golden Gate.

## Version history

| Version | Released | Latest MacOS | Minimum MacOS | Short Blog Description |
|---|---|---|---|---|
| 6.0.0 | 2026-06-11 | Tahoe (27) |   | New tap trust security mechanism, sandboxing on Linux, initial support for macOS 27 (Golden Gate). |
| 5.0 | 2025-11-12 | Tahoe (26) | Sonoma (14) | download concurrency by default, **official support for Linux ARM64/AArch64**, timescales for deprecating macOS Intel and removing macOS Gatekeeper bypass behaviours. |
| 4.6.0 | 2025-08-05 | Sequoia (15) | Ventura (13) | opt-in concurrent downloads with `HOMEBREW_DOWNLOAD_CONCURRENCY`, preliminary macOS 26 (Tahoe) support and a built-in `brew mcp-server`. |
| 4.5.0 | 2025-04-29 | major improvements to `brew bundle`/`services`, preliminary Linux support for casks, official Support Tiers, Tier 2 ARM64 Linux support, Ruby 3.4 and several deprecations. |   |   |
| 4.4.0 | 2024-10-01 | `INSTALL_RECEIPT.json` files for casks, macOS Monterey (12) deprecation and various other deprecations. |   |   |
| 4.3.0 | 2024-05-14 | Sonoma (14) | Monterey (12) | SBOM support, initial bottle attestation verification, new command analytics and uninstall autoremove by default. |
| 4.2.0 | 2023-12-18 | major performance upgrades (e.g. using Ruby 3.1, upgrading fewer dependencies), `.env` file configuration and macOS Sonoma support. |   |   |
| 4.1.0 | 2023-07-20 | Ventura (13) | Big Sur (11) | significant improvements to the security/reliability/performance/usability of Homebrew 4.0.0's new JSON API, the completion of the migration of analytics from Google Analytics in the US to InfluxDB in the EU and groundwork for later macOS Sonoma (14) support. |
| 4.0.0 | 2023-02-16 | Enables significantly faster Homebrew-maintained tap updates by migrating from Git-cloned taps to JSON downloads. |   |   |
| 3.6.0 | 2022-09-07 | preliminary macOS Ventura support, the need for `--eval-all`/`HOMEBREW_EVAL_ALL` and a migration to Ubuntu 22.04 as our CI platform. |   |   |
| 3.5.0 | 2022-06-06 | Monterey (12) | Catalina (10.15) | improved `brew update` behaviour |
| 3.4.0 | 2022-02-28 | `HOMEBREW_NO_ENV_HINTS` to hide configuration suggestions, `brew services` supported on `systemd` on Linux, `brew install --overwrite` and Homebrew beginning the process to leave the SFC. |   |   |
| 3.3.0 | 2021-10-25 | migration from Homebrew/linuxbrew-core to Homebrew/homebrew-core for all Homebrew on Linux users, the official support of macOS Monterey (and, as usual, dropping the support for Mojave due to us only supporting 3 macOS versions) and the addition of an opt-in `HOMEBREW_INSTALL_FROM_API` flag to avoid needing to have Homebrew/homebrew-core or Homebrew/homebrew-cask repositories tapped/cloned locally. |   |   |
| 3.2.0 | 2021-06-21 | ~Monterey (12) | 10.10+ (unknown) | `brew install` now upgrades outdated formulae by default and basic macOS 12 (Monterey) support. |
| 3.1.0 | 2021-04-12 | Big Sur (11) | migration of our bottles (binary packages) to GitHub Packages. |   |
| 3.0.0 | 2021-02-05 | **official Apple Silicon support** and a new bottle format in formulae. |   |   |
| 2.7.0 | 2020-12-21 | API deprecations. |   |   |
| 2.6.0 | 2020-12-01 | macOS Big Sur support on Intel, `brew` commands replacing all `brew cask` commands, the beginnings of macOS M1/Apple Silicon/ARM support and API deprecations. |   |   |
| 2.5.0 | 2020-09-08 | Catalina (10.15) | Yosemite (10.10) | better `brew cask` integration, license support and API deprecations. |
| 2.4.0 | 2020-06-11 | dropping macOS Mavericks support, the deprecation of `devel` versions and `brew audit` speedups. |   |   |
| 2.3.0 | 2020-05-29 | Mavericks (10.9) | GitHub Actions CI usage, fetching resources before installation, Docker image improvements and the deprecation of `brew install` from URLs. |   |
| 2.2.0 | 2019-11-27 | macOS Catalina support, performance increases and better Homebrew on Linux ecosystem integration. |   |   |
| 2.1.0 | 2019-04-04 | Mojave (10.14) | casks on https://formulae.brew.sh, search on Homebrew sites and better Docker support. |   |
| 2.0.0 | 2019-02-02 | **official support for Linux and Windows 10 (with Windows Subsystem for Linux)**, `brew cleanup` running automatically, no more options in Homebrew/homebrew-core, and removal of support for OS X Mountain Lion (10.8) and older. |   |   |
| 1.9.0 | 2019-01-09 | Mountain Lion (10.8) and older | **Linux support**, (optional) automatic `brew cleanup` and providing bottles (binary packages) to more Homebrew users. |   |
| 1.8.0 | 2018-10-23 | official Mojave support, linkage auto-repair on `brew upgrade`, `brew info` displaying analytics data and quarantining Cask's downloads. |   |   |
| 1.7.0 | 2018-07-15 | ~Mojave (10.14) | fixes for macOS 10.14 Mojave's developer beta, Homebrew Formulae's JSON analytics and formulae APIs and various formula API deprecations. |   |
| 1.6.0 | 2018-04-09 | ? | `brew install python` installing Python 3, the deprecation of Homebrew/homebrew-php and various formula API deprecations. |   |
| 1.5.0 | 2018-01-19 | deprecations of formula APIs and some Homebrew organisation formula taps. |   |   |
| 1.4.0 | 2017-12-11 | Homebrew filters environment variables. |   |   |
| 1.3.0 | 2017-07-31 | `brew install python` no longer installs a `python` binary without manual `PATH` additions and instead installs a `python2` binary. This avoids overriding the system `python` binary by default when installing Python as a dependency. It also paves the way to eventually have `python` be Python 3.x. |   |   |
| 1.2.0 | 2017-05-01 | most Homebrew taps (package repositories) in the Homebrew GitHub organisation have been deprecated and the currently buildable software moved into Homebrew/homebrew-core. This will improve the quality and availability of all their software. |   |   |
| 1.1.0 | 2016-11-07 | We've had a great response to Homebrew 1.0.0 and been iterating on our work there. That 1.1.0 follows 1.0.9 is a happy coincidence due to breaking changes; in the future we may have a e.g. 1.1.10. |   |   |
| 1.0.0 | 2016-09-21 | In the seven years since Homebrew was created by @mxcl our community has grown to almost 6000 unique contributors, a wide-reaching third-party "tap" ecosystem and thousands of packages. |   |   |
