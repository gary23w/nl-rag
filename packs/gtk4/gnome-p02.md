---
title: "GNOME (part 2/2)"
source: https://en.wikipedia.org/wiki/GNOME
domain: gtk4
license: CC-BY-SA-4.0
tags: gtk4 toolkit, gtk widgets, gnome application, libadwaita styling
fetched: 2026-07-02
part: 2/2
---

## GNOME OS

GNOME OS is an operating system designed to provide a streamlined, container-centric platform that serves as both an experimental testbed and a showcase for GNOME's user interface and application ecosystem.

Unlike many Linux distributions, GNOME OS is not based on other distributions such as Arch Linux, Debian, or Fedora Linux. It is built from the ground up using tools like BuildStream, Freedesktop SDK, and GNOME Build Meta, ensuring a clean and consistent environment tailored for GNOME development.

This approach allows GNOME OS to provide a standardized platform for developers to develop the latest GNOME software without the variability introduced by other distributions. While GNOME OS shares similarities with immutable distributions like Fedora Silverblue, it remains distinct in its purpose and design, focusing solely on the GNOME ecosystem.

### History

#### Origins and early vision (2010–2012)

The concept of GNOME OS began to take shape around 2010, with discussions and planning sessions focused on creating a more unified and cohesive system for GNOME. The vision was inspired by other platforms like Android, WebOS, and MeeGo, with the goal of designing an operating system that could offer a better experience for both users and developers.

In 2012, during the GUADEC conference held in A Coruña, a significant planning session, known as a Birds of a Feather (BoF) session, was conducted on July 30. This session brought together key members of the GNOME community to discuss and plan the future direction of GNOME OS. The discussions covered several critical areas, including application development, testing, core user experience (UX), pattern language, and support for touch and mobile devices.

#### GNOME Continuous — formative years (2013–2019)

Early OSTree-based build efforts were sometimes informally referred to as "**gnome-ostree**", but the continuous integration pipeline that emerged became known as **GNOME Continuous**, reflecting its primary role as a continuous integration and testing platform for GNOME. It was designed to provide a rolling-release environment where developers could test GNOME 3.x features and applications in isolation.

Technologically, GNOME Continuous adopted OSTree for atomic updates, allowing the system to roll back to previous states if updates failed, ensuring system stability. This technology was later popularized by Fedora Silverblue and other immutable Linux distributions.

Key milestones during this period include:

- 2013: OSTree matures and GNOME presents the idea publicly. OSTree development and the concept of an OSTree-based GNOME build pipeline were showcased at GUADEC 2013 and in contemporaneous OSTree releases, signaling the technical basis for a continuous build approach.
- 2014: First public builds of GNOME Continuous released, enabling developers to test GNOME 3.x.
- 2016: Integration with Flatpak, which introduced application sandboxing and cross-distribution compatibility, aligning with GNOME's vision for secure and portable applications.
- 2018: The GNOME project formalised build metadata and adopted gnome-build-meta, moving from prototype CI to structured upstream builds.

#### GNOME OS revival (2020–present)

GNOME OS first became publicly visible as a testable reference platform around 2020, when the project published a “GNOME OS Nightly” page offering downloadable images and instructions for running the system in virtual machines or on real hardware.

Since then the project has continued to evolve: in October 2024 Adrian Vovk published proposals to make GNOME OS more suitable for everyday use, and in mid-2025 the community launched initiatives to expand real-hardware testing and to revise update and dependency mechanisms (notably the “Summer of GNOME OS” program and discussion of stronger systemd dependencies).
