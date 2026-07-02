---
title: "Open Container Initiative"
source: https://en.wikipedia.org/wiki/Open_Container_Initiative
domain: kata-containers
license: CC-BY-SA-4.0
tags: kata lightweight virtual machine, hardware virtualized container, vm isolated container runtime, micro vm workload isolation
fetched: 2026-07-02
---

# Open Container Initiative

The **Open Container Initiative** (**OCI**) is a Linux Foundation project, started in June 2015 by Docker, CoreOS, and the maintainers of appc (short for "App Container") to design open standards for operating system-level virtualization (containers). At launch, OCI was focused on Linux containers and subsequent work has extended it to other operating systems.

## Specifications

There are currently three OCI specifications in development and use: the *Runtime Specification* (runtime-spec), the *Image Specification* (image-spec), and the *Distribution Specification* (distribution-spec).

The OCI organization includes the development of **runc**, which is the reference implementation of the runtime-spec, a container runtime that implements their specification and serves as a basis for other higher-level tools. runc was first released in July 2015 as version 0.0.1 and it reached version 1.0.0 on June 22, 2021.

The OCI Image Format Project was split out from the Runtime Project into its own specification on March 23, 2016. The image-spec is a software shipping container image format spec (OCI Image Format) that reached version 1.0.0 on July 19, 2017.

The OCI Distribution Spec Project defines the distribution-spec, an API protocol to facilitate and standardize the distribution of content. The distribution-spec was created on March 8, 2018, from a Proposal for a JSON Registry API V2.1. The distribution-spec reached version 1.0.0 on April 26, 2021.
