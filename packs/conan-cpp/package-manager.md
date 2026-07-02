---
title: "Package manager"
source: https://en.wikipedia.org/wiki/Package_manager
domain: conan-cpp
license: CC-BY-SA-4.0
tags: conan cpp, c++ packages, package manager, dependency management
fetched: 2026-07-02
---

# Package manager

A **package manager**, or **package management system**, is software that supports installing, upgrading, configuring, and removing software for the host system in a consistent manner.

A package manager deals with *packages*, distributions of software and data in archive files. Packages contain metadata, such as the software's name, description of its purpose, version number, vendor, checksum (usually a cryptographic hash function), and a list of dependencies necessary for the software to run properly. Upon installation, metadata is stored in a local package database. Package managers typically maintain a database of software dependencies and version information to prevent software mismatches and missing prerequisites. They work closely with software repositories, binary repository managers, and app stores.

Package managers are designed to eliminate the need for manual installs and updates. This can be particularly useful for large enterprises whose operating systems (OSes) typically consist of hundreds or even tens of thousands of distinct packages.

## History

An early package manager was SMIT (and its backend install) from IBM AIX. SMIT was introduced with AIX 3.0 in 1989. Package managers like dpkg have existed as early as 1994. Early package managers, from around 1994, had no automatic dependency resolution but could already simplify the process of adding and removing software from a running system.

By around 1995, beginning with CPAN, package managers began handling package repository downloads, and dependency resolution and installation as needed, making it easier to install, uninstall and update software.

## Functions

A software package is an archive file containing a computer program as well as necessary metadata for its deployment. The program may be in source code that has to be compiled and built first. Package metadata include the software's description, version number, and dependencies.

Package managers are charged with the task of finding, installing, maintaining or uninstalling packages upon the user's command. Typical functions of a package management system include:

- Using file archivers to extract package archives
- Ensuring the integrity and authenticity of the package by verifying their checksums and digital certificates, respectively
- Looking up, downloading, installing, or updating existing software from a software repository or app store
- Grouping packages by function to reduce user confusion
- Managing dependencies to ensure a package is installed with all the packages it requires, and avoiding *dependency hell*

### Challenges with shared libraries

Computer systems that rely on dynamic library linking, instead of static library linking, share executable libraries of machine instructions across packages and applications. In these systems, conflicting relationships between different packages requiring different versions of libraries results in a situation called *dependency hell*. On Microsoft Windows systems, this is also called *DLL hell* when working with dynamically-linked libraries.

Modern package managers have mostly solved these problems by allowing parallel installation of multiple library versions (e.g. OPENSTEP's *Framework* system), a dependency of any kind (e.g. *slots* in Gentoo Portage), and even packages compiled with different compiler versions (e.g. dynamic libraries built by the Glasgow Haskell Compiler, where a stable ABI does not exist), in order to enable other packages to specify which version they are linked or installed against.

### Front-ends for locally-compiled packages

System administrators may install and maintain software using tools other than package managers. For example, a local administrator may download unpackaged source code, compile it, and install it. This may cause the local system to fall out of synchronization with the package manager's database. The local administrator will be required to take additional measures, such as manually managing some dependencies or integrating the changes into the package manager.

There are tools to ensure that locally-compiled packages are integrated with the package management. For operating systems based on .deb and .rpm files as well as Slackware Linux, there is CheckInstall, and for recipe-based systems such as Gentoo Linux and hybrid systems such as Arch Linux, it is possible to write a recipe first, which then ensures that the package fits into the local package database.

### Maintenance of configuration

Upgrades of configuration files may be particularly troublesome. Since package managers, at least on Unix systems, originated as extensions of file archivers, they can usually only overwrite or retain configuration files, rather than apply rules to them. There are exceptions to this that usually apply to kernel configuration (which, if broken, will render the computer unusable after a restart). Problems can be caused if the configuration file format changes; for instance, if the old file does not explicitly disable new options that should be disabled. Some package managers, such as Debian's dpkg, allow configuration during installation. In other situations, packages are installed with the default configuration, which is then overwritten, for example in headless installations to a large number of computers. This kind of pre-configured installation is also supported by dpkg.

### Repositories

To give users more control over the software they allow to be installed on their systems, and sometimes due to legal or convenience reasons on the distributors' side, packages are often downloaded from software repositories.

### Upgrade suppression

When a user is upgrading a package with package management software, it is customary for them to be presented with the actions to be executed (usually the list of packages to be upgraded, and possibly the old and new version numbers), and allow them to either accept the upgrade in bulk, or select individual packages for upgrading. Many package managers can be configured to never upgrade certain packages, or to upgrade them only when critical vulnerabilities or instabilities are found in the previous version, as defined by the packager of the software. This process is called *upgrade suppression*, or *version pinning*. For instance, to prevent upgrades to the OpenOffice program:

- yum supports upgrade suppression with the syntax `exclude=openoffice*`
- pacman with `IgnorePkg= openoffice` (to suppress upgrading openoffice in both cases)
- dpkg and dselect support partial suppression through the *hold* flag in package selections
- APT extends the *hold* flag through a pinning mechanism, and users can also blacklist a package
- aptitude uses *hold* and *forbid* flags:
  - *hold*: prevents a package from being **upgraded or changed** during installs/upgrades
  - *forbid*: prevents a package from being **installed** or **reinstalled**
- portage supports suppression through the package.mask configuration file

### Cascading package removal

Some of the more advanced package management features offer *cascading package removal*, in which all packages that depend on the target package and all packages that only it depends on are also removed.

### Comparison of commands

Although commands are specific to each package manager, they are translatable to a large extent, as most package managers offer similar functions. The Arch Linux wiki offers an extensive overview of commands.

${

PKG

}

or

%PKG%

is the package name.

Action

APT

DNF

Pacman

Zypper

portage

WinGet

Homebrew

Nix

XBPS

Install package

apt

install

${

PKG

}

dnf

install

${

PKG

}

pacman

-S

${

PKG

}

zypper

install

${

PKG

}

emerge

${

PKG

}

winget install

%PKG%

brew

install

${

PKG

}

nix-env

-i

${

PKG

}

xbps-install

${

PKG

}

Remove package

apt

remove

${

PKG

}

dnf

remove

${

PKG

}

pacman

-R

${

PKG

}

zypper

remove

${

PKG

}

emerge

-C

${

PKG

}

or

emerge

--unmerge

${

PKG

}

winget uninstall

%PKG%

brew

uninstall

${

PKG

}

nix-env

-e

${

PKG

}

xbps-remove

${

PKG

}

Update software database

apt

update

— (automatic)

pacman

-Sy

zypper

refresh

emerge

--sync

— (automatic)

brew

update

nix-channel

--upgrade

xbps-install

-S

Show updatable packages

apt

list

--upgradable

dnf

check-update

pacman

-Qu

zypper

list-updates

emerge

-avtuDN

--with-bdeps

=

y

@world

or

emerge

-u

--pretend

@world

(

-D

is shorthand for

--deep

and

-u

is shorthand for

--update

.)

winget upgrade

brew

outdated

```mw
nix-channel --upgrade && \
nix-env -u && \
nix-collect-garbage
```

./xbps-src

update-check

${

PKG

}

(requires void-packages repository)

Update all

apt

upgrade

dnf

upgrade

pacman

-Syu

zypper

update

emerge

-u

-D

--with-bdeps

=

y

@world

winget upgrade --all

brew

upgrade

nix-env

-u

&&

nix-collect-garbage

xbps-install

-Su

Show unused dependencies

apt

autoremove

--dry-run

dnf

repoquery

--unneeded

pacman

-Qdt

zypper

packages

--unneeded

emerge

-caD

or

emerge

--depclean

--pretend

—

N/a

brew

autoremove

--dry-run

—

N/a

xbps-remove

-o

Delete unused dependencies

apt

autoremove

dnf

autoremove

pacman

-Rsn

$(

pacman

-Qdtq

)

zypper

remove

-u

emerge

--depclean

—

N/a

brew

autoremove

&&

brew

cleanup

nix-collect-garbage

-d

xbps-remove

-of

Remove package and unused dependencies

apt-get

remove

--auto-remove

${

PKG

}

dnf

remove

${

PKG

}

pacman

-Rs

${

PKG

}

zypper

remove

-u

${

PKG

}

emerge

-c

${

PKG

}

or

emerge

--depclean

${

PKG

}

winget uninstall

%PKG%

```mw
brew uninstall ${PKG} && brew autoremove
```

nix-env

-e

${

PKG

}

&&

nix-env

-u

xbps-remove

-R

${

PKG

}

## Prevalence

Linux distributions oriented to binary packages rely heavily on package management systems as their primary means of managing and maintaining software. Mobile operating systems such as Android (Linux-based) and iOS (Unix-based) rely almost exclusively on their respective vendors' app stores and thus use their own dedicated package management systems.

## Similar programs and platforms

### Installers

A package manager is often called an *install manager*, which can lead to a confusion between package managers and installers. The differences include:

| Criterion | Package manager | Installer |
|---|---|---|
| Shipped with | Usually, the operating system | Each computer program |
| Location of installation information | One central installation database | It is entirely at the discretion of the installer. It could be a file within the app's folder, or among the operating system's files and folders. At best, they may register themselves with an uninstallers list without exposing installation information. |
| Scope of maintenance | Potentially all packages on the system | Only the product with which it was bundled |
| Developed by | One package manager vendor | Multiple installer vendors |
| Package format | A handful of well-known formats | There could be as many formats as the number of apps |
| Package format compatibility | Can be consumed as long as the package manager supports it. Either newer versions of the package manager keep supporting it or the user does not upgrade the package manager. | The installer is always compatible with its archive format, if it uses any. However, installers, like all computer programs, may be affected by software rot. |
|   |   |   |

### Build automation utilities

Most software configuration management systems treat building software and deploying software as separate, independent steps. A build automation utility typically takes human-readable source code files already on a computer, and automates the process of converting them into an executable package on the same or a remote computer. Later, a package manager typically running on another computer downloads the pre-built executable and installs it.

However, both kinds of tools have many commonalities:

- Topological sorting of the dependency graph used in a package manager to handle dependencies between binary components is also used in a build manager to handle dependencies between source components.
- Many makefiles support not only building executables, but also installing them with `make install`.
- Every package manager for a source-based distribution – such as Portage, Sorcery, or Homebrew – supports converting source code to binary executables and installing it.

A few tools, such as Maak and A-A-P, are designed to handle both building and deployment, and can be used as either build automation utilities, package managers, or both.

### App stores

App stores can also be considered application-level package managers (without the ability to install all levels of programs). Unlike traditional package managers, app stores are designed to enable payment for the software itself (instead of for software development), and may only offer monolithic packages with no dependencies or dependency resolution. They are usually limited in their management functionality, due to focusing on ease-of-use over power or emergence, and are common in commercial operating systems and smart devices.

Package managers also often have only human-reviewed code. Many app stores, such as Google Play and Apple's App Store, mainly screen apps using automated tools only; malware can pass these tests by detecting when the app is being tested, and delaying malicious activity. There are exceptions: the npm package database, for instance, relies entirely on post-publication review of its code, while the Debian package database has an extensive human review process before any package goes into the main database. The XZ Utils backdoor used years of trust-building to insert a backdoor, which was nonetheless caught while in the testing database.

## Common package managers and formats

### Universal package manager

Also known as binary repository manager, it is a software tool designed to optimize the download and storage of binary files, artifacts and packages used and produced in the software development process. These package managers aim to standardize the way enterprises treat all package types. They give users the ability to apply security and compliance metrics across all artifact types. Universal package managers have been referred to as being at the center of a DevOps toolchain.

### Package formats

Each package manager relies on the format and metadata of the packages in its repository. That is, package managers need groups of files to be bundled along with appropriate metadata, such as dependencies. Often, a core set of utilities manages the basic installation from these packages and multiple package managers use these utilities to provide additional functionality.

For example, yum relies on rpm as a backend. Yum extends the functionality of rpm by adding features such as simple configuration for maintaining a network of systems. As another example, the Synaptic Package Manager provides a graphical user interface by using the Advanced Packaging Tool (apt) library, which in turn relies on dpkg for core functionality.

Alien is a program that converts between different Linux package formats, supporting conversion between Linux Standard Base (LSB) compliant .rpm packages, .deb, Stampede (.slp), Solaris (.pkg) and Slackware (.tgz, .txz, .tbz, .tlz) packages.

For mobile operating systems, Google Play uses the Android application package (APK) package format while Microsoft Store uses the APPX and XAP formats. Both Google Play and Microsoft Store have eponymous package managers.

### Free and open source software systems

By the nature of free and open-source software (FOSS), packages under similar and compatible licenses are available on a number of operating systems. These packages can be combined and distributed using configurable packaging systems to handle many permutations of software and manage version-specific dependencies and conflicts. Some managers of FOSS packages are released as FOSS themselves. One typical difference between package management in proprietary operating systems, such as Mac OS X and Windows, and those in free and open source software, such as Linux, is that free and open source software systems permit third-party packages to also be installed and upgraded through the same mechanism, whereas the package managers of Mac OS X and Windows will only upgrade software provided by Apple and Microsoft, respectively (with the exception of some third party drivers in Windows). The ability to continuously upgrade third-party software is typically added by adding the URL of the corresponding repository to the package management's configuration file.

### Application-level package managers

Besides system-level application managers, there are add-on package managers for operating systems with limited capabilities and for programming languages in which developers need the latest libraries.

Unlike system-level package managers, application-level package managers focus on a small part of the software system. They typically reside within a directory tree that is not maintained by the system-level manager, such as c:\cygwin or /opt/sw. This may not be the case for managers that deal with programming libraries, leading to possible conflicts, as both managers may claim to own a file and may break upgrades.

## Impact

Ian Murdock commented that package management is "the single biggest advancement Linux has brought to the industry", that it blurs the boundaries between operating systems and applications, and that it makes it "easier to push new innovations [...] into the marketplace and [...] evolve the OS".

There is also a conference for package manager developers known as PackagingCon. It was established in 2021 with the aim to understand different approaches to package management.
