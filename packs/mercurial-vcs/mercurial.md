---
title: "Mercurial"
source: https://en.wikipedia.org/wiki/Mercurial
domain: mercurial-vcs
license: CC-BY-SA-4.0
tags: mercurial vcs, distributed version control, hg repository, changeset history
fetched: 2026-07-02
---

# Mercurial

**Mercurial** is a distributed revision control tool for software developers. It is supported on Microsoft Windows, Linux, and other Unix-like systems, such as FreeBSD and macOS.

Mercurial's major design goals include high performance and scalability, decentralization, fully distributed collaborative development, robust handling of both plain text and binary files, and advanced branching and merging capabilities, while remaining conceptually simple. It includes an integrated web-interface. Mercurial has also taken steps to ease the transition for users of other version control systems, particularly Subversion. Mercurial is primarily a command-line driven program, but graphical user interface extensions are available, e.g. TortoiseHg, and several IDEs offer support for version control with Mercurial. All of Mercurial's operations are invoked as arguments to its driver program `hg` (a reference to Hg – the chemical symbol of the element mercury).

Olivia Mackall originated Mercurial and served as its lead developer until late 2016. Mercurial is released as free software under the GPL-2.0-or-later license. It is mainly implemented using the Python programming language, but includes a binary diff implementation written in C.

## History

Mackall first announced Mercurial on 19 April 2005. The impetus for this was the announcement earlier that month by Bitmover that they were withdrawing the free version of BitKeeper because of the development of SourcePuller.

BitKeeper had been used for the version control requirements of the Linux kernel project. Mackall decided to write a distributed version control system as a replacement for use with the Linux kernel. This project started a few days after the now well-known Git project was initiated by Linus Torvalds with similar aims.

The Linux kernel project decided to use Git rather than Mercurial, but Mercurial is now used by many other projects (see below).

In an answer on the Mercurial mailing list, Olivia Mackall explained how the name "Mercurial" was chosen:

> Shortly before the first release, I read an article about the ongoing Bitkeeper debacle that described Larry McVoy as mercurial (in the sense of 'fickle'). Given the multiple meanings, the convenient abbreviation, and the good fit with my pre-existing naming scheme (see my email address), it clicked instantly. Mercurial is thus named in Larry's honor. I do not know if the same is true of Git.

High-profile projects such as the OpenJDK have used Mercurial in the past, though the OpenJDK no longer does as of Java 16.

## Design

Mercurial uses SHA-1 hashes to identify revisions. For repository access via a network, Mercurial uses an HTTP-based protocol that seeks to reduce round-trip requests, new connections, and data transferred. Mercurial can also work over SSH where the protocol is very similar to the HTTP-based protocol. By default it uses a 3-way merge before calling external merge tools.

## Usage

Figure 1 shows some of the most important operations in Mercurial and their relations to Mercurial's concepts.

## Adoption

Although Mercurial was not selected to manage the Linux kernel sources, it was adopted by several organizations. Facebook is using the Rust programming language to write Mononoke, a Mercurial server specifically designed to support large multi-project repositories.

In 2013, Facebook adopted Mercurial and began work on scaling it to handle their large, unified code repository.

Google also uses Mercurial client as a front-end on their cloud-based 'Piper' monorepo back-end.

Bitbucket announced that its web-based version control services would end support for Mercurial in June 2020 (then extended to July 2020), explaining that "less than 1% of new projects use it, and developer surveys indicated that 90% of developers use Git".

Xen used Mercurial for many years, but moved to Git in 2013.

Mozilla used Mercurial for many years, but started moving to end support for Mercurial in favor of Git in 2023.

## Mercurial servers and repository management

- Heptapod, a GitLab fork for Mercurial by Octobus
- Kallithea, a GPLv3 fork of RhodeCode
- Phabricator by Phacility
- RhodeCode by RhodeCode Inc.

### Source code hosting

The following websites provide free source code hosting for Mercurial repositories:

- Bitbucket by Atlassian (gone as of July 2020)
- Codebase
- GNU Savannah by FSF
- Heptapod
- OSDN (seems dysfunctional as of December 2024)
- Perforce
- Puszcza (a sister site to GNU Savannah, hosted in Ukraine)
- SourceForge
- SourceHut
- TuxFamily

Mercurial website mentions some other forges.

### Open source projects using Mercurial

Some projects using the Mercurial distributed RCS:

- GNU Multi-Precision Library
- GNU Octave
- LEMON
- LiquidFeedback
- Orthanc
- Pidgin
- RhodeCode
- Roundup
- Tryton
- XEmacs
- Xine
- eric

### Open source projects formerly using Mercurial

- Mozilla 2007-2023
- Xen ?-2013
- OpenJDK
