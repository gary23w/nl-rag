---
title: "Getting Started"
source: https://www.dragonflydb.io/docs/getting-started
domain: dragonfly-db
license: CC-BY-SA-4.0
tags: dragonfly database, in-memory data store, redis alternative, key-value cache
fetched: 2026-07-02
---

# Getting Started

Use one of these options to get Dragonfly up and running quickly:

- Install Dragonfly with Docker
- Install Dragonfly with Docker Compose
- Install Dragonfly Kubernetes Operator
- Install on Kubernetes with Helm Chart
- Install from Binary
- Install using Linux Packages
- Get Started with Dragonfly Cloud

# Hardware Compatibility

Dragonfly is specifically optimized to operate in cloud environments. It is officially supported and certified for use on both x86_64 and arm64 architectures.

For x86_64 architectures, Dragonfly requires a minimum *sandybridge* architecture to function properly. To ensure compatibility and performance, Dragonfly undergoes continuous testing on various cloud platforms. These include Graviton2 instances in AWS cloud, as well as x86_64 based instances in both AWS and GCP clouds.

Furthermore, Dragonfly's regression tests, which can be found here, are continously run on Azure cloud via GitHub Actions. This helps guarantee the reliability and stability of the software.

# OS Compatibility

Dragonfly is compatible with Linux versions 4.14 or later. However, to achieve optimal performance, it is recommended to run Dragonfly on kernel version 5.10 or later. The Dragonfly build environment is based on Ubuntu 20.04.

# Benchmarking Dragonfly

Learn how to measure the performance of Dragonfly in a cloud environment.
