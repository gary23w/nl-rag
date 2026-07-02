---
title: "Rolling release"
source: https://en.wikipedia.org/wiki/Rolling_release
domain: deployment-strategies
license: CC-BY-SA-4.0
tags: deployment strategy, rolling update release, recreate strategy, zero downtime rollout
fetched: 2026-07-02
---

# Rolling release

**Rolling release**, also known as **rolling update** or continuous delivery, is a concept in software development of frequently delivering updates to applications. This is in contrast to a *standard* or *point release* development model which uses software versions which replace the previous version.

A rolling release model is different from a staged or "staggered" rollout, in which an update is gradually made available to an increasing percentage of users for testing or bandwidth reasons.

An example of a rolling release would be Arch Linux, where new packages and updates roll in constantly, and significant changes to the distribution may occur at any time by the developers. This is in contrast to Ubuntu Linux, which has biannual releases, with the only major changes after a release being security updates or significant bug fixes.

## Model

Rolling release development models are one of many types of software release life cycles. Although a rolling release model can be used in the development of any piece or collection of software, it is most often seen in use by Linux distributions, notable examples being GNU Guix System, Arch Linux, Gentoo Linux, Nobara Linux (since version 41), openSUSE Tumbleweed, PCLinuxOS, Solus, SparkyLinux, and Void Linux. Some modern Distributed SQL databases such as YugabyteDB also support this feature.

A rolling release is typically implemented using small and frequent updates. However, simply having updates does not automatically mean that a piece of software is using a rolling release cycle; for this, the philosophy of developers must be to work with one code branch as opposed to discrete versions. When the rolling release is employed as the development model, software updates are typically delivered to users by a package manager on the user's personal computer, accessing through the internet a remote software repository (often via a download mirror) stored on an internet file server.
