---
title: "Buck (software)"
source: https://en.wikipedia.org/wiki/Buck_(software)
domain: buck-build
license: CC-BY-SA-4.0
tags: buck build system, build system, incremental build, monorepo build
fetched: 2026-07-02
---

# Buck (software)

**Buck** is a multi-language build system developed and used by Meta Platforms, Inc. It was designed for building small, reusable modules consisting of code and resources within a monorepo. It supports many programming languages, including C++, Swift, Unix Shell, Java, Kotlin, Python, Lua, OCaml, Rust and Go. It can produce binary outputs for a variety of target platforms including iOS, Android, .NET, and Java virtual machine (VM) runtime systems. Licensing for Buck1 is under Apache License 2.0, while Buck2 is under either MIT or Apache 2.0.

Buck requires the explicit declaration of dependencies. Because all dependencies are explicit and Buck has a directed acyclic graph of all source files and build targets, Buck can perform incremental recompilation, only rebuilding targets downstream of files that have changed. Buck computes a key for each target that is a hash of the contents of the files it depends on. It stores a mapping from that key to the build target in a build cache.

## History

In 2013, Buck1 was released. One of the key features was the ability to share build results between multiple developers and continuous integration (CI), as Buck1 supports a HTTP Cache API.

In 2023, Buck2 was released, claiming that builds are 2x as fast as compared to Buck1. One of the largest changes from Buck1 is that the core is written in Rust instead of Java, and rules are written outside the core in Starlark (the language created for the Bazel build system).
