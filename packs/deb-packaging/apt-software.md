---
title: "APT (software)"
source: https://en.wikipedia.org/wiki/APT_(software)
domain: deb-packaging
license: CC-BY-SA-4.0
tags: debian package format, dpkg tool, apt repository, package signing
fetched: 2026-07-02
---

# APT (software)

**Advanced Package Tool** (**APT**) is a free-software user interface that works with core libraries to handle the installation and removal of software on Debian and Debian-based Linux distributions. APT simplifies the process of managing software on Unix-like computer systems by automating the retrieval, configuration and installation of software packages, either from precompiled files or by compiling source code.

## Usage

APT is a collection of tools distributed in a package named *apt*. A significant part of APT is defined in a C++ library of functions; APT also includes command-line programs for dealing with packages, which use the library. Three such programs are `apt`, `apt-get` and `apt-cache`. They are commonly used in examples because they are simple and ubiquitous. The *apt* package is of "*important*" priority in all current Debian releases, and is therefore included in a default Debian installation. APT can be considered a front end to `dpkg`, friendlier than the older `dselect` front end. While `dpkg` performs actions on individual packages, APT manages relations (especially dependencies) between them, as well as sourcing and management of higher-level versioning decisions such as release tracking and Upgrade Suppression.

APT is often hailed as one of Debian's best features, which Debian developers attribute to the strict quality controls in Debian's policy.

A major feature of APT is the way it calls `dpkg` –it performs topological sorting of the list of packages to be installed or removed and calls `dpkg` in the best possible sequence. In some cases, it utilizes the `--force` options of `dpkg`. However, it only does this when it is unable to calculate how to avoid the reason `dpkg` requires the action to be forced.

### Installing software

The user indicates one or more packages to be installed. Each package name is phrased as just the name portion of the package, not a fully qualified filename (for instance, in a Debian system, `libc6` would be the argument provided, not `libc6_1.9.6-2.deb`). Notably, APT automatically gets and installs packages upon which the indicated package depends (if necessary). This was an original distinguishing characteristic of APT-based package management systems, as it avoided installation failure due to missing dependencies, a type of dependency hell.

Another distinction is the retrieval of packages from remote repositories. APT uses a location configuration file (`/etc/apt/sources.list`) to locate the desired packages, which might be available on the network or a removable storage medium, for example, and retrieve them, and also obtain information about available (but not installed) packages.

APT provides other command options to override decisions made by apt-get's conflict resolution system. One option is to force a particular version of a package. This can downgrade a package and render dependent software inoperable, so the user must be careful.

Finally, the `apt_preferences` mechanism allows the user to create an alternative installation policy for individual packages.

The user can specify packages using a POSIX regular expression.

APT searches its cached list of packages and lists the dependencies that must be installed or updated.

APT retrieves, configures and installs the dependencies automatically.

Triggers are the treatment of deferred actions.

### Update, upgrade and dist-upgrade

Usage modes of `apt` and `apt-get` that facilitate updating installed packages include:

- `update` is used to resynchronize the **package index** files from their sources. The lists of available packages are fetched from the location(s) specified in `/etc/apt/sources.list`. For example, when using a Debian archive, this command retrieves and scans the `Packages.gz` files, so that information about new and updated packages is available.
- `upgrade` is used to install the newest versions of all packages currently installed on the system from the sources enumerated in `/etc/apt/sources.list`. Packages currently installed with new versions available are retrieved and upgraded; under no circumstances are currently installed packages removed, or packages not already installed retrieved and installed. New versions of currently installed packages that cannot be upgraded without changing the install status of another package will be left at their current version.
- `full-upgrade` (`apt`) and `dist-upgrade` (`apt-get`), in addition to performing the function of `upgrade`, also intelligently handles changing dependencies with new versions of packages; `apt` and `apt-get` have a "smart" conflict resolution system, and will attempt to upgrade the most important packages at the expense of less important ones if necessary. The `/etc/apt/sources.list` file contains a list of locations from which to retrieve desired package files. aptitude has a smarter `dist-upgrade` feature called `full-upgrade`.

## Configuration and files

`/etc/apt` contains the APT configuration folders and files.

`apt-config` is the APT Configuration Query program. `apt-config dump` shows the configuration.

### Files

- `/etc/apt/sources.list`: Locations to fetch packages from.
- `/etc/apt/sources.list.d/`: Additional source list fragments.
- `/etc/apt/apt.conf`: APT configuration file.
- `/etc/apt/apt.conf.d/`: APT configuration file fragments.
- `/etc/apt/preferences.d/`: Directory with version preferences files. This is where "pinning" is specified, i.e. a preference to get certain packages from a separate source or from a different version of a distribution.
- `/var/cache/apt/archives/`: Storage area for retrieved package files.
- `/var/cache/apt/archives/partial/`: Storage area for package files in transit.
- `/var/lib/apt/lists/`: Storage area for state information for each package resource specified in `sources.list`
- `/var/lib/apt/lists/partial/`: Storage area for state information in transit.
