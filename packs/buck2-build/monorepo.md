---
title: "Monorepo"
source: https://en.wikipedia.org/wiki/Monorepo
domain: buck2-build
license: CC-BY-SA-4.0
tags: buck2 build system, buck build tool, hermetic build graph, meta build system
fetched: 2026-07-02
---

# Monorepo

In version-control systems, a **monorepo** or **monorepository** ("mono" meaning 'single' and "repo" being short for 'repository') is a software-development strategy in which the code for a number of projects is stored in the same repository. This practice dates back to at least the early 2000s, when it was commonly called a shared codebase. Google, Meta, Microsoft, Uber, Airbnb, and Twitter all employ very large monorepos with varying strategies to scale build systems and version control software with a large volume of code and daily changes.

A related concept is a monolithic application, but whereas a monolith combines its sub-projects into one large project, a monorepo may contain multiple independent projects.

## Advantages

There are a number of potential advantages to a monorepo over individual repositories:

**Ease of code reuse**

Similar functionality or communication protocols can be abstracted into shared libraries and directly included by projects, without the need of a dependency

package manager

.

**Simplified dependency management**

In a multiple repository environment where multiple projects depend on a third-party dependency, that dependency might be downloaded or built multiple times. In a monorepo the build can be easily optimized, as referenced dependencies all exist in the same codebase.

**Atomic commits**

When projects that work together are contained in separate repositories, releases need to sync which versions of one project work with the other. And in large enough projects, managing compatible versions between dependencies can become

dependency hell

.

In a monorepo this problem can be negated, since developers may change multiple projects atomically.

**Large-scale code refactoring**

Since developers have access to the entire project, refactors can ensure that every piece of the project continues to function after a refactor.

**Collaboration across teams**

In a monorepo that uses source dependencies (dependencies that are compiled from source),

teams can improve projects being worked on by other teams. This leads to flexible

code ownership

.

## Limitations and disadvantages

**Loss of version information**

Although not required, some monorepo builds use one version number across all projects in the repository. This leads to a loss of per-project

semantic versioning

.

**Lack of per-project access control**

With split repositories, access to a repository can be granted based upon need. A monorepo allows read access to all software in the project, possibly presenting new security issues.

Note that there are versioning systems in which this limitation is not an issue. For example, when

Subversion

is used, it's possible to download any part of the repo (even a single directory), and path-based authorization can be used to restrict access to certain parts of a repository.

**More storage needed by default**

With split repositories, you fetch only the project you are interested in by default. With a monorepo, you

check out

all projects by default. This can take up a significant amount of storage space. While some versioning systems have a mechanism to do a partial checkout,

doing so defeats some of the advantages of a monorepo.

## Scalability challenges

Companies with large projects have come across hurdles with monorepos, specifically concerning build tools and version control systems. Google's monorepo, speculated to be the largest in the world, meets the classification of an ultra-large-scale system and must handle tens of thousands of contributions every day in a repository over 80 terabytes in size.

### Scaling version control software

Companies using or switching to existing version control software found that software could not efficiently handle the amount of data required for a large monorepo. Facebook and Microsoft chose to contribute to or fork existing version control software Mercurial and Git respectively, while Google eventually created their own version control system.

For more than ten years, Google had relied on Perforce hosted on a single machine. In 2005 Google's build servers could get locked up to 10 minutes at a time. Google improved this to 30 seconds–1 minute in 2010. Due to scaling issues, Google eventually developed its own in-house distributed version control system dubbed Piper.

Facebook ran into performance issues with the version control system Mercurial and made upstream contributions to the client, and in January 2014 made it faster than a competing solution in Git.

In May 2017 Microsoft announced that virtually all of its Windows engineers use a Git monorepo. In the transition, Microsoft made substantial upstream contributions to the Git client to remove unnecessary file access and improve handling of large files with Virtual File System for Git.

### Scaling build software

Few build tools work well in a monorepo, and flows where builds and continuous integration testing of the entire repository are performed upon check-in will cause performance problems. A build system that processes dependencies as a directed graph (such as Buck, Bazel, Please, or Pants) solves this by compartmentalizing each build or test to the active area of development.

Twitter began development of Pants in 2011, as both Facebook's Buck and Google's Bazel were closed-source at the time. Twitter open-sourced Pants in 2012 under the Apache 2.0 License.

Please is a Go-based build system; it was developed in 2016 by Thought Machine, whose developers were both inspired by Google's Bazel and dissatisfied with Facebook's Buck.
