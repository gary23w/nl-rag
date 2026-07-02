---
title: "Software repository"
source: https://en.wikipedia.org/wiki/Software_repository
domain: homebrew-macos
license: CC-BY-SA-4.0
tags: homebrew package manager, macports tool, formula recipe, ruby language
fetched: 2026-07-02
---

# Software repository

A **software repository**, or **repo** for short, is a storage location for software packages. Often a table of contents is also stored, along with metadata. A software repository is typically managed by source or version control, or repository managers. Package managers allow automatically installing and updating repositories, sometimes called "packages".

## Overview

Many software publishers and other organizations maintain servers on the Internet for this purpose, either free of charge or for a subscription fee. Repositories may be solely for particular programs, such as CPAN for the Perl programming language, or for an entire operating system. Operators of such repositories typically provide a package management system, tools intended to search for, install and otherwise manipulate software packages from the repositories. For example, many Linux distributions use Advanced Packaging Tool (APT), commonly found in Debian based distributions, or Yellowdog Updater, Modified (yum) found in Red Hat based distributions. There are also multiple independent package management systems, such as pacman, used in Arch Linux and equo, found in Sabayon Linux.

As software repositories are designed to include useful packages, major repositories are designed to be malware free. If a computer is configured to use a digitally signed repository from a reputable vendor, and is coupled with an appropriate permissions system, this significantly reduces the threat of malware to these systems. As a side effect, many systems that have these abilities do not need anti-malware software such as antivirus software.

Most major Linux distributions have many repositories around the world that mirror the main repository.

At client side, a package manager helps installing from and updating the repositories.

## Package management system vs. package development process

A package management system is different from a package development process.

A typical use of a package management system is to facilitate the integration of code from possibly different sources into a coherent stand-alone operating unit. Thus, a package management system might be used to produce a distribution of Linux, possibly a distribution tailored to a specific restricted application.

A package development process, by contrast, is used to manage the co-development of code and documentation of a collection of functions or routines with a common theme, producing thereby a package of software functions that typically will not be complete and usable by themselves. A good package development process will help users conform to good documentation and coding practices, integrating some level of unit testing.

## Selected repositories

The following table lists a few languages with repositories for contributed software. The "Autochecks" column describes the routine checks done.

Very few people have the ability to test their software under multiple operating systems with different versions of the core code and with other contributed packages they may use. For the R programming language, the Comprehensive R Archive Network (CRAN) runs tests routinely.

To understand how this is valuable, imagine a situation with two developers, Sally and John. Sally contributes a package A. Sally only runs the current version of the software under one version of Microsoft Windows, and has only tested it in that environment. At more or less regular intervals, CRAN tests Sally's contribution under a dozen combinations of operating systems and versions of the core R language software. If one of them generates an error, she gets that error message. With luck, that error message details may provide enough input to allow enable a fix for the error, even if she cannot replicate it with her current hardware and software. Next, suppose John contributes to the repository a package B that uses a package A. Package B passes all the tests and is made available to users. Later, Sally submits an improved version of A, which breaks B. The autochecks make it possible to provide information to John so he can fix the problem.

This example exposes both a strength and a weakness in the R contributed-package system: CRAN supports this kind of automated testing of contributed packages, but packages contributed to CRAN need not specify the versions of other contributed packages that they use. Procedures for requesting specific versions of packages exist, but contributors might not use those procedures.

Beyond this, a repository such as CRAN running regular checks of contributed packages actually provides an extensive if *ad hoc* test suite for development versions of the core language. If Sally (in the example above) gets an error message she does not understand or thinks is inappropriate, especially from a development version of the language, she can (and often does with R) ask the core development-team for the language for help. In this way, the repository can contribute to improving the quality of the core language software.

| Language, purpose | Package development process | Repository | Install methods | Collaborative development platform | Autochecks |
|---|---|---|---|---|---|
| C/C++ |   | vcpkg |   |   |   |
|   | Conan |   |   |   |   |
| Common Lisp |   | Quicklisp |   |   |   |
| D | DUB | dlang.org | dub add <package> |   |   |
| Dart | Flutter | pub.dev | flutter pub get <package> |   |   |
| Fortran |   | Fortran Package Manager (fpm) |   |   |   |
| Go | go | pkg.go.dev | go get <package> | GitHub |   |
| Haskell | Common Architecture for Building Applications and Libraries | Hackage | cabal (software) |   |   |
| Java, Kotlin, Scala, Groovy, Clojure, etc. |   | Maven | Maven, Apache Ivy, Gradle, sbt |   |   |
| JavaScript, TypeScript, Node.js | node | npm registry | npm install <package> yarn add <package> |   |   |
|   | Bower | bower install <package> |   |   |   |
| Julia |   |   |   |   |   |
| .NET | NuGet | NuGet | dotnet add package <package> |   |   |
| Ocaml |   | OPAM |   |   |   |
| Perl |   | CPAN | PPM | ActiveState |   |
| PHP | PEAR, Composer | PECL, Packagist | composer require <package> pear install <package> |   |   |
| PowerShell |   | PowerShell Gallery | PSResourceGet |   |   |
| Python | Setuptools, Poetry | PyPI | pip, EasyInstall, PyPM, Poetry, uv |   |   |
|   | Conda |   |   |   |   |
| R | R CMD check process | CRAN | install.packages remotes | GitHub | Often on 12 platforms or combinations of different versions of R (devel, prerel, patched, release) on different operating systems (different versions of Linux, Windows, macOS, and Solaris). |
| Ruby | RubyGems | RubyGems | RubyGems, Bundler |   |   |
| Rust | Cargo | crates.io | Cargo |   |   |
| Swift |   | Swift Package Manager |   |   |   |
| TeX, LaTeX |   | CTAN |   |   |   |

(Parts of this table were copied from a "List of Top Repositories by Programming Language" on Stack Overflow)

Notable repositories with limited scope include:

- Netlib, mainly mathematical routines for Fortran and C, historically one of the first open software repositories;
- Boost, a strictly curated collection of high-quality libraries for C++; some code developed in Boost later became part of the C++ standard library.

## Package managers

Package managers help manage repositories and the distribution of them. If a repository is updated, a package manager will usually allow a user to update that repository through the manager. It also helps to manage things such as dependencies between other repositories. Examples of managers include:

| Package manager | Description |
|---|---|
| npm | Manager for Node.js |
| pip | Installer for Python |
| APT | Manager for Debian |
| Homebrew | Installer for macOS, allows installing packages that Apple did not |
| vcpkg | Manager for C, C++ |
| yum and DNF | Manager for Fedora, Red Hat Enterprise Linux |
| Pacman | Manager for Arch Linux |
| Composer | Manager for PHP |

## Repository managers

In an enterprise environment, a software repository is usually used to store artifacts, or to mirror external repositories which may be inaccessible due to security restrictions. Such repositories may provide additional functionality, like access control, versioning, security checks for uploaded software, cluster functionality etc. and typically support a variety of formats in one package, so as to cater for all the needs in an enterprise, and thus aiming to provide a single point of truth. One example is Sonatype Nexus Repository.

At server side, a software repository is typically managed by source control or repository managers. Some of the repository managers allow to aggregate other repository location into one URL and provide a caching proxy. When doing continuous builds many artifacts are produced and often centrally stored, so automatically deleting the ones which are not released is important.

### Relationship to continuous integration

As part of the development lifecycle, source code is continuously being built into binary artifacts using continuous integration. This may interact with a binary repository manager much like a developer would by getting artifacts from the repositories and pushing builds there. Tight integration with CI servers enables the storage of important metadata such as:

- Which user triggered the build (whether manually or by committing to revision control)
- Which modules were built
- Which sources were used (commit id, revision, branch)
- Dependencies used
- Environment variables
- Packages installed

#### Artifacts and packages

Artifacts and packages inherently mean different things. Artifacts are simply an output or collection of files (ex. JAR, WAR, DLLS, RPM etc.) and one of those files may contain metadata (e.g. POM file). Whereas packages are a single archive file in a well-defined format (ex. NuGet) that contain files appropriate for the package type (ex. DLL, PDB). Many artifacts result from builds but other types are crucial as well. Packages are essentially one of two things: a library or an application.

Compared to source files, binary artifacts are often larger by orders of magnitude, they are rarely deleted or overwritten (except for rare cases such as snapshots or nightly builds), and they are usually accompanied by much metadata such as id, package name, version, license and more.

Metadata describes a binary artifact, is stored and specified separately from the artifact itself, and can have several additional uses. The following table shows some common metadata types and their uses:

| Metadata type | Used for |
|---|---|
| Versions available | Upgrading and downgrading automatically |
| Dependencies | Specify other artifacts that the current artifact depends on |
| Downstream dependencies | Specify other artifacts that depend on the current artifact |
| License | Legal compliance |
| Build date and time | Traceability |
| Documentation | Provide offline availability for contextual documentation in IDEs |
| Approval information | Traceability |
| Metrics | Code coverage, compliance to rules, test results |
| User-created metadata | Custom reports and processes |
