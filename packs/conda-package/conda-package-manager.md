---
title: "Conda (package manager)"
source: https://en.wikipedia.org/wiki/Conda_(package_manager)
domain: conda-package
license: CC-BY-SA-4.0
tags: conda package, python environments, package manager, anaconda distribution
fetched: 2026-07-02
---

# Conda (package manager)

**Conda** is an open-source, cross-platform, language-agnostic package manager and environment management system. It was originally developed to solve package management challenges faced by Python data scientists, and today is a popular package manager for Python and R. At first, Anaconda Python distribution was developed by Anaconda Inc.; later, it was spun out as a separate package, released under the BSD license. The Conda package and environment manager is included in all versions of Anaconda, Miniconda, Miniforge and Anaconda Repository. Conda is a NumFOCUS affiliated project.

## Features

As a package manager, Conda allows users to install different versions of binary software packages and their required software dependencies appropriate for their computing platform from a software repository. Conda checks everything that has been installed, any version limitations that the user specifies (for example, the user wants a specific package to be at least version 2.1.3), and determines a set of versions for all requested packages and their dependencies that makes the total set compatible with one another. If there is no set of compatible dependencies, it will tell the user that the requested combination of software packages at the requested versions is not possible.

Secondly, Conda allows users to create such a set of software packages in isolation from the rest of the computing platform, in what Conda calls an *environment*. This allows the user to create various sets of software packages for different projects. When the users switches between those projects, they switch to the relevant environment, thereby avoiding the re-installation or removal of conflicting packages. To further facilitate the setup of such environments, Conda can also install Python, the interpreter for the software packages itself.

Conda is written in the Python programming language, but can manage projects containing code written in any language, including multi-language projects.

## Channels

Conda uses channels to obtain package metadata and versioning information. For example, Anaconda distribution uses Anaconda repository containing over 7500 packages as the default (called *defaults*) channel. However, in 2024, Anaconda distribution updated its licensing terms to require fees except for few specific cases. conda-forge is a popular open-source, community-run alternative that provides packages for a wide variety of software, whereas *Bioconda* is a specialized channel for packages related to bioinformatics and biomedical research. Conda also supports custom channels that can be self-hosted.
