---
title: "Introduction"
source: https://buck2.build/docs/
domain: buck2-build
license: CC-BY-SA-4.0
tags: buck2 build system, buck build tool, hermetic build graph, meta build system
fetched: 2026-07-02
---

# Introduction

Welcome to Buck2, a large scale, fast, reliable, and extensible build tool developed and used by Meta. Buck2 supports a variety of languages on many platforms.

Buck2's core is written in Rust. Starlark, which is a deterministic, immutable dialect of Python, is used to extend the Buck2 build system, enabling Buck2 to be language-agnostic. With Starlark, users can define their own custom rules.

Buck2 leverages the Bazel spec of Remote Build Execution as the primary means of parallelization and caching, which increases the importance of idempotency (no matter how many times an operation is performed, it yields the same result) and hermeticity (code is sealed off from the world), giving the right results, reliably.

Buck2 multi-language support includes C++, Python, Java, Kotlin, Go, Rust, Erlang, OCaml, and more.

The following sub-sections contain a list of links to key points in the Buck2 Documentation website that explain the advantages of using Buck2 for you and your team.

## Buck2 Documentation Website Links

### For end users

- Getting Started - how to get started with using Buck2.
- Benefits - the benefits of using Buck2.

### For people writing rules

- Writing Rules - how to write rules to support new languages.
- Build APIs - documentation for the APIs available when writing rules.
- Loading Data - How to load static data from JSON and TOML files in rules.
- Starlark Types - rules are written in Starlark (which is approximately Python), but our version adds types.

### For people integrating with Buck2

- Extending Buck via BXL - powerful Starlark scripts for introspection of Buck2's graphs.
- Buck2 change detector - tools for building a CI that only builds/tests what has changed in diff/PR.
- Buck2 GitHub actions installer - script to make GitHub CI with Buck2 easier.
- Reindeer - a set of tools for importing Rust crates from crates.io, git repos etc and generating a BUCK file for using them.
- ocaml-scripts - scripts to generate a BUCK file enabling the use of OCaml packages from an OPAM switch.
- Buckle - a launcher for Buck2 on a per-project basis. Enables a project or team to do seamless upgrades of their build system tooling.

### External articles about Buck2

- Introducing Buck2 - our initial introduction when we open sourced Buck2.
- Reddit AMA where the Buck2 team answered a number of questions.
- Using buck to build Rust projects - working through an initial small Rust project, by Steve Klabnik. Followed up by building from crates.io and updating Buck2.
- Awesome Buck2 is a collection of resources about Buck2.
- Buck2 Unboxing is a general review of Buck2 by Son Luong Ngoc.
- A tour around Buck2 gives an overview of Buck2 and how it differs from Bazel.

### External videos about Buck2

- Accelerating builds with Buck2 Neil talks about why Buck2 is fast.
- Buck2: optimizations & dynamic dependencies Neil and Chris talk about why Buck2 is fast and some of the advanced dependency features.
- Building Erlang with Buck2 Andreas talks about building WhatsApp with Buck2.
- antlir2: Deterministic image builds with Buck2 talks about layering a packaging system over Buck2.

### External projects using Buck2

- System Initiative build their DevOps product using Buck2, with their own custom prelude.
- Rust `cxx` library has examples and tests with a wide variety of build systems, including Buck2.
- `ocamlrep` library allows for interop between OCaml and Rust code, and can be built with Buck2.
- `buck2-nix` is an experiment to integrate Buck2, Sapling and Nix together in a harmonious way.

Feel free to send a PR adding your project.
