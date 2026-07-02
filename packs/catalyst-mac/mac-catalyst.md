---
title: "macOS Catalina"
source: https://en.wikipedia.org/wiki/Mac_Catalyst
domain: catalyst-mac
license: CC-BY-SA-4.0
tags: mac catalyst, uikit on mac, ipad app port, apple platform bridge
fetched: 2026-07-02
---

# macOS Catalina

(Redirected from

Mac Catalyst

)

**macOS Catalina** (version 10.15) is the sixteenth major release of macOS, Apple's desktop operating system for Macintosh computers. It is the successor to macOS Mojave and was announced at WWDC 2019 on June 3, 2019 and released to the public on October 7, 2019. Catalina is the first version of macOS to support only 64-bit applications and the first to include Activation Lock. It is also the last version of macOS to have the major version number be 10.x; its successor, Big Sur, released on November 12, 2020, is version 11. In order to increase web compatibility, various web browsers, such as Safari, Chromium, and Firefox, still inform websites that they are running on Catalina version 10.15.7, regardless of the actual macOS version in use.

The operating system is named after Santa Catalina Island, which is located off the coast of southern California.

macOS Catalina is the final version of macOS that supports the Unibody MacBook Pro, as its successor, macOS Big Sur, drops support for its mid-2012 and final model.

## System requirements

All standard configuration Macs that supported macOS Mojave support macOS Catalina. 2010 to 2012 Mac Pros, which could run Mojave only with a GPU upgrade, are not supported. Catalina requires 4 GB of memory, an increase over the 2 GB required by Lion through Mojave.

- iMac (Late 2012 or later)
- iMac Pro (2017)
- MacBook (Early 2015 or later)
- MacBook Air (Mid 2012 or later)
- MacBook Pro (Mid 2012 or later)
- Mac Mini (Late 2012 or later)
- Mac Pro (Late 2013 or later)

It is unofficially possible to install macOS Catalina on many older Macintosh computers that are not officially supported by Apple. This requires using a patch to modify the install image.

## Changes

### System

#### Catalyst

Catalyst is a software-development tool that allows developers to write apps that can run on macOS, iOS and iPadOS. Apple demonstrated several ported apps, including Jira and Twitter (after the latter discontinued its macOS app in February 2018).

#### System extensions

An upgrade from Kexts. System extensions avoid the problems of Kexts. There are 3 kinds of System extensions: Network Extensions, Endpoint Security Extensions, and Driver Extensions. System extensions run in userspace, outside of the kernel. Catalina will be the last version of macOS to support legacy system extensions.

#### DriverKit

A replacement for IOKit device drivers, driver extensions are built using DriverKit. DriverKit is a new SDK with all-new frameworks based on IOKit, but updated and modernized. It is designed for building device drivers in userspace, outside of the kernel.

#### Gatekeeper

Mac apps, installer packages, and kernel extensions that are signed with a Developer ID must be notarized by Apple to run on macOS Catalina.

#### Activation Lock

Activation Lock prevents the unauthorized use and drive erasure of devices with an Apple T2 security chip (2018, 2019, and 2020 MacBook Pro; 2020 5K iMac; 2018 MacBook Air, iMac Pro; 2018 Mac Mini; 2019 Mac Pro).

#### Dedicated system volume

The system runs on its own read-only volume, separate from all other data on the Mac.

#### Voice control

Users can give detailed voice commands to applications. On-device machine processing is used to offer better navigation.

#### Sidecar

Sidecar allows a Mac to use an iPad (running iPadOS) as a wireless external display. With Apple Pencil, the device can also be used as a graphics tablet for software running on the computer. Sidecar requires a Mac with Intel Skylake CPUs and newer (such as the fourth-generation MacBook Pro), and an iPad that supports Apple Pencil.

#### Support for wireless game controllers

The Game Controller framework adds support for two major console game controllers: the PlayStation 4's DualShock 4 and the Xbox One controller.

#### Time Machine

A number of under-the-hood changes were made to Time Machine, macOS's backup software. One change was the manner in which backup data is stored on network-attached devices was changed, and this change is not backwards-compatible with earlier versions of macOS. Apple declined to document these changes, but some of them have been noted.

#### Pro Display XDR

macOS Catalina 10.15.2 adds compatibility with the Pro Display XDR and enables 6016×3384 output on the 2019 iMac and 2018 15-inch MacBook Pro.

### Applications

#### iTunes

iTunes is replaced by separate Music, Podcasts, TV and Books apps, in line with iOS. iOS device management is now conducted via Finder. The TV app on Mac supports Dolby Atmos, Dolby Vision, and HDR10 on MacBooks released in 2018 or later, while 4K HDR playback is supported on Macs released in 2018 or later when connected to a compatible display.

#### Find My

Find My Mac and the Find My Friends widget were merged into Find My.
