---
title: "The Dhall configuration language"
source: https://dhall-lang.org/
domain: dhall-config
license: CC-BY-SA-4.0
tags: dhall config, dhall language, total functional configuration, typed config language
fetched: 2026-07-02
---

# The Dhall configuration language

Maintainable configuration files

Dhall is a programmable configuration language that you can think of as: JSON + functions + types + imports

# Don't repeat yourself

Struggling with configuration drift? Create a single source of truth you can reference everywhere.

> "Configuration drift occurs when a standardized group of IT resources, be they virtual servers, standard router configurations in VNF deployments, or any other deployment group that is built from a standard template, diverge in configuration over time. … The Infrastructure as Code methodology from DevOps is designed to combat Configuration Drift and other infrastructure management problems."

Create a single authoritative configuration file:

… that you can read directly into several languages or convert to other file formats (including YAML or JSON).

Supported integrations

# Fearlessly refactor

Need to clean up a big mess? Move fast without breaking things by leaning on Dhall's tooling.

Refactoring something mission-critical? Use Dhall's support for semantic hashes to guarantee that many types of refactors are behavior-preserving

What if you intend to make a change? Use a semantic diff to verify that you changed what you expected to:

Did you inherit a messy configuration? Use the type system and integrated editor support to navigate more effectively.

VSCode plugin

# Safety first

Sick of Turing-complete configuration languages? Dhall is a total programming language that forbids arbitrary side effects.

We take language security seriously so that your Dhall programs never fail, hang, crash, leak secrets, or compromise your system.

The language aims to support safely importing and evaluating untrusted Dhall code, even code authored by malicious users. We treat the inability to do so as a specification bug.

Safety guarantees

# Use programming language features

Hold your configuration files to the same standard of quality as the rest of your code. "Configuration bugs, not code bugs, are the most common cause I've seen of really bad outages. … As with error handling, I'm often told that it's obvious that config changes are scary, but it's not so obvious that most companies test and stage config changes like they do code changes." Configs are code are configs are code https://t.co/fVBs7T7P3j— Charity Majors (@mipsytipsy) October 17, 2019 Configuration testing is quite underrated in an industry where the majority of work is becoming configuration.— JBD (@rakyll) September 26, 2019 Get started

This work is licensed under a Creative Commons Attribution 4.0 International License.
