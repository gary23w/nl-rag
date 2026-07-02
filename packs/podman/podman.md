---
title: "Podman"
source: https://en.wikipedia.org/wiki/Podman
domain: podman
license: CC-BY-SA-4.0
tags: podman containers, rootless containers, container engine, daemonless containers
fetched: 2026-07-02
---

# Podman

**Podman** (*pod manager*) is an open source Open Container Initiative (OCI)-compliant container management tool created by Red Hat used for handling containers, images, volumes, and pods on the Linux operating system, with support for macOS and Microsoft Windows via a virtual machine. Based on the libpod library, it offers APIs for the lifecycle management of containers, pods, images, and volumes. The API is identical to the Docker API. Podman Desktop provides an alternative to Docker Desktop.

## History

The first public release of Podman (v0.2) was released in 2018, version 1.0.0 of Podman was released on January 16th, 2019.

Version 1.0 of Podman Desktop was released on May 23, 2023.

In KubeCon 2024, Red Hat announced that it will contribute Podman and Podman Desktop to the Cloud Native Computing Foundation (CNCF), by that point, Podman Desktop had already been downloaded 1.5 million times, the projects were accepted into the CNCF on January 21, 2025.

### Adoption

In the 2025 Stack Overflow survey, among 20,070 survey respondents identifying as professionals, 10.9% said that they had used Podman in the past year, compared to 73.8% and 30.1% for Docker and Kubernetes respectively.

## Design

Podman is a "daemonless" tool, as opposed to other containerization systems like Docker, which uses a background service called *dockerd* to manage its containers, Podman relies on systemd for managing its container life cycles.

## Security

Podman lets containers run without root privileges (rootless), meaning they can be created, run, and managed by regular users without administrator rights by using Linux namespaces.
