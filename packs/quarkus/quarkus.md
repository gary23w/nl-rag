---
title: "Quarkus"
source: https://en.wikipedia.org/wiki/Quarkus
domain: quarkus
license: CC-BY-SA-4.0
tags: quarkus framework, quarkus native, graalvm native, jakarta ee
fetched: 2026-07-02
---

# Quarkus

**Quarkus** is a Java framework optimised for resource efficiency and developer experience. Key technology components surrounding it are OpenJDK HotSpot and GraalVM. Quarkus provides developers with a unified reactive and imperative programming model to address a wider range of distributed application architectures.

## Version history

| Version | Date | Notes |
|---|---|---|
| 0.12 | March 20, 2019 | Initial release |
| 1.0 | Nov 2019 |   |
| 2.0 | Jun 2021 |   |
| 3.0.1 | Mar 2023 |   |
| 3.2.6 | Oct 2023 | LTS (3.2) |
| 2.16.12.Final | October 17, 2023 |   |
| 3.2.7.Final | October 19, 2023 |   |
| 3.5.0 | October 25, 2023 |   |
| 3.2.9.Final | November 17, 2023 |   |
| 3.6.0 | November 29, 2023 |   |
| 3.2.10.Final | Jan 2024 |   |
| 3.7.1 | Jan 2024 |   |
| 3.8.1 | Feb 2024 | LTS (3.8) |
| 3.10.0 | Apr 2024 |   |
| 3.13.0 | July 2024 |   |
| 3.15.2 | Nov 2024 | LTS (3.15) |
| 3.16.2 | Nov 2024 |   |
| 3.17.7 | Jan 2025 |   |
| 3.18.3 | Feb 2025 |   |
| 3.22.3 | May 2025 |   |
| 3.25.3 | Aug 2025 | LTS (3.20.2.1) |
| 3.28.1 | Sep 2025 | LTS (3.27.0) |
| 3.29.3 | Nov 2025 | LTS (3.27.1) |
| 3.30.6 | Jan 2026 |   |
| 3.34.1 | Mar 2026 | LTS (3.33.1) |
| 3.35.3 | May 2026 | LTS (3.33.2) |

## Distributions

### GraalVM Community Edition (CE) and GraalVM Enterprise Edition (EE)

GraalVM is a Java Virtual Machine for compiling and running applications written in different languages to a native machine binary. GraalVM Community Edition has varying support and licensing requirements.

### Mandrel

Mandrel is a downstream distribution of GraalVM CE, supporting the same capabilities to build native executables but based on the open source OpenJDK. Mandrel aims to make GraalVM easy to consume by Quarkus applications by only including GraalVM CE components that Quarkus needs. Red Hat began commercial support for using Mandrel to build native Quarkus applications since the Quarkus 1.7 release in October 2020.

## Design pillars

### Container first

Quarkus was designed around the container-first and Kubernetes-native philosophy, optimizing for low memory usage and fast startup times.

As much processing as possible is done at build time, including taking a closed-world assumption approach to building and running applications. This optimization means that, in most cases, all code that does not have an execution path at runtime isn't loaded into the JVM.

In Quarkus, classes used only at application startup are invoked at build time and not loaded into the runtime JVM. Quarkus also avoids reflection as much as possible, instead favoring static class binding. These design principles aim to reduce the size, and ultimately the memory footprint, of the application running on the JVM while also enabling Quarkus to be *natively-native*.

Quarkus' uses the native image capability of GraalVM to compile JVM bytecode to a native machine binary. GraalVM aggressively removes any unreachable code found within the application's source code as well as any of its dependencies. Combined with Linux containers and Kubernetes, a Quarkus application runs as a native Linux executable, eliminating the JVM.

### Built on standards

Quarkus rests on an ecosystem of technologies, standards, libraries, and APIs, including Contexts & Dependency Injection (CDI), Jax-rs, Java persistence api (JPA), Java Transaction API (JTA), Apache Camel, and Hibernate.

Quarkus is an Ahead-of-time compilation (AOT) platform, optimizing code for the JVM as well as compiling to native code for improved performance. All of the underlying technologies are AOT-enabled.
