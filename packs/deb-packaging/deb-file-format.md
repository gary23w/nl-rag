---
title: "deb (file format)"
source: https://en.wikipedia.org/wiki/Deb_(file_format)
domain: deb-packaging
license: CC-BY-SA-4.0
tags: debian package format, dpkg tool, apt repository, package signing
fetched: 2026-07-02
---

# deb (file format)

**deb** is the format, as well as filename extension of the software package format for Debian and its derivatives.

## Design

Debian packages are standard Unix ar archives that include two tar archives. One archive holds the control information and another contains the installable data.

dpkg provides the basic functionality for installing and manipulating Debian packages. Generally end users don't manage packages directly with dpkg but instead use the APT package management software or other APT front-ends such as aptitude (nCurses) and synaptic (GTK).

Debian packages can be converted into other package formats and vice versa using alien, and created from source code using checkinstall or the Debian Package Maker.

Some core Debian packages are available as **udeb**s ("micro debs"), and are typically used only for bootstrapping a Debian installation. Although these files use the *udeb* filename extension, they adhere to the same structure specification as ordinary *deb* files. However, unlike their *deb* counterparts, *udeb* packages contain only essential functional files. In particular, documentation files are normally omitted. *udeb* packages are not installable on a standard Debian system, but are used in Debian-Installer.

## Implementation

Prior to Debian 0.93, a package consisted of a file header and two concatenated gzip archives. Since Debian 0.93, a deb package is implemented as an ar archive. This archive contains three files in a specific order:

1. **debian-binary** - A text file named `debian-binary` containing a single line giving the package format version number. (`2.0` for current versions of Debian).
2. **control archive** - A tar archive named `control.tar` contains the maintainer scripts and the package meta-information (package name, version, dependencies and maintainer). Compressing the archive with gzip or xz and zstd is supported. The file extension changes to indicate the compression method.
3. **data archive** - A tar archive named `data.tar` contains the actual installable files. Compressing the archive with gzip, bzip2, lzma or xz and zstd is supported. The file extension changes to indicate the compression method.

### Control archive

The control archive contents can include the following files:

- **control** contains a brief description of the package as well as other information such as its dependencies.
- **md5sums** contains MD5 checksums of all files in the package in order to detect corrupt or incomplete files.
- **conffiles** lists the files of the package that should be treated as configuration files. Configuration files are not overwritten during an update unless specified.
- **preinst**, **postinst**, **prerm** and **postrm** are optional scripts that are executed before or after installing or removing the package.
- **config** is an optional script that supports the debconf configuration mechanism.
- **shlibs** list of shared library dependencies.

### Signed packages

Debian-based distributions support OpenPGP signature verification of signed Debian packages, but most (if not all) have this feature disabled by default. Instead packages are verified by signing the repository metadata (i.e. Release files). The metadata files in turn include checksums for the repository files as a means to verify authenticity of the files. Currently there are two different implementations for signing individual packages. The first is done via the debsigs / debsig-verify toolset, which is supported by dpkg. The second is done through the dpkg-sig program which is not supported by dpkg, so the packages have to be manually checked with the dpkg-sig program. Both formats add new sections to the ar archive to store the signature information, but the formats are not compatible with one another. Neither of the modifications to the package format are listed in the official Debian handbook or man page about the binary package format.

## Adoption

- Debian packages are used in distributions based on Debian, such as, Linux Mint (LMDE), KDE neon, Ubuntu and many others.
- Fink, a port of dpkg and APT to macOS, uses deb packages.
- Nexenta OS, a discontinued OS based on OpenSolaris, included Debian package management software and the use of deb packages.
- Debian GNU/kFreeBSD, an OS that uses a GNU based userland and the FreeBSD kernel.
- Debian GNU/Hurd.
- Some jailbroken iOS devices (iPhones, iPads and iPods).
- Ipkg and Opkg, which both use .ipk packages that resemble Debian's dpkg
- Termux, which is a GNU environment for Android.
