---
title: "Docs"
source: https://reproducible-builds.org/docs/
domain: reproducible-builds
license: CC-BY-SA-4.0
tags: reproducible build determinism, bit for bit build reproducibility, deterministic compilation, build environment normalization
fetched: 2026-07-02
---

# Documentation

Getting reproducible builds for your software or distribution might be easier than you think.

However, it might require small changes to your build system and a strategy on how to enable others to recreate an environment in which the builds can be reproduced.

## Introduction

- Which problems do Reproducible Builds Solve?
- Definitions
- History
- Why reproducible builds?
- Making plans
- Academic publications

## Achieve deterministic builds

- Commandments of reproducible builds
- Reproducibility Quickstart Guide

## Managing variance

- Variations in the build environment
- SOURCE_DATE_EPOCH
- Deterministic build systems
- Volatile inputs can disappear
- Stable order for inputs
- Stripping of unreproducible information
- Value initialization
- Version information
- Timestamps
- Timezones
- Locales
- Archive metadata
- Stable order for outputs
- Randomness
- Build path
- System images
- Rust
- JVM
- Helm

## Define a build environment

- What's in a build environment?
- Recording the build environment
- Definition strategies
- Proprietary operating systems

## Distribute the environment

- Building from source
- Virtual machine drivers
- Formal definition

## Verification

- Cryptographic checksums
- Embedded signatures
- Sharing certifications

## Specifications

- SOURCE_DATE_EPOCH
- BUILD_PATH_PREFIX_MAP (WIP)
