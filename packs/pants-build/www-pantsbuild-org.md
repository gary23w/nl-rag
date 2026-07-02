---
title: "Pantsbuild"
source: https://www.pantsbuild.org/
domain: pants-build
license: CC-BY-SA-4.0
tags: pants build system, pants monorepo build, fine-grained build graph, polyglot build tool
fetched: 2026-07-02
---

# Pantsbuild

Skip to main content

# Pantsbuild: The ergonomic build system

Welcome to the Pants documentation hub!

Pants is a fast, scalable, user-friendly build system for codebases of all sizes. It's currently focused on Python, Go, Java, Scala, Kotlin, Shell, and Docker, with support for other languages and frameworks coming soon.

Here you'll find guides to help you get started with Pants, comprehensive documentation on how to configure, run and customize Pants, and information on how to get help from the Pants community.

## Why adopt the Pants build system?

A lot of effort has gone into making Pants easy to adopt, easy to use and easy to extend. We're super excited to bring Pants' distinctive features to Go, Java, Python, Scala, Kotlin, and Shell users:

### Much easier to adopt and maintain.

Pants requires very minimal BUILD file metadata/boilerplate. It uses a combination of static analysis and sensible defaults to infer most of that information on the fly. So your BUILD files can be very minimal — and even those can be generated and updated for you!

### Resistant to supply chain attacks.

Pants has out-of-the-box support for multiple dependency resolves and their corresponding lockfiles, so you can have hermetic, repeatable builds that are resilient to supply chain attacks, even in complex situations where you have multiple versions of the same dependencies in different parts of the codebase.

### Meets you where you are.

Pants operates, underneath it all, at the file level. So even if you have fine-grained dependency tangles (or even cycles!) that prevent you from creating modular BUILD targets and dependencies, Pants can work with that.

### Easy to extend.

Pants has a rich plugin API that uses idiomatic async Python 3, in case you need any customizations. In fact the built-in rules use that same API.

### Git-friendly.

Pants natively speaks git, so you can do things like "run all the tests affected by changes between main and my current branch".

### First-class Python.

You'll find no subsets like Starlark here. Pants empowers you with full support for Python.

## Pants is a multilingual multitool.

Pants supports Python, Docker, Go, Java, Kotlin, Pex, Protodoc, Scala, Shell, Thrift, Protobuf, Helm, many linting and formatting tools, packaging, coverage, and more. Learn more.

### Responsive community.

Pants community is welcoming, quick to answer questions, and genuinely interested in your thoughts and contributions. So come say hi on the Slack and tell us what you need next!

### Case studies.

Learn how others have handled the practical issues of migrating legacy codebases, from case studies by Astranis, IBM, iManage, and more.

### Enterprise quality.

Pants is trusted by organizations of all sizes, including Coinbase, IBM, Orca Security, Rippling, Slack, Salesforce, and many others
