---
title: "Proton (software)"
source: https://en.wikipedia.org/wiki/Proton_(software)
domain: proton-gaming
license: CC-BY-SA-4.0
tags: proton compatibility tool, steam deck, wine gaming layer, dxvk translation
fetched: 2026-07-02
---

# Proton (software)

**Proton** is a compatibility layer that allows Windows software (primarily video games) to run on Linux-based operating systems. Proton is developed by Valve in cooperation with developers from CodeWeavers. It is a collection of software and libraries combined with a patched version of Wine to improve performance and compatibility with Windows games. Proton is designed for integration into the Steam client as "Steam Play". It is officially distributed through the client, although third-party forks can be manually installed.

## Overview

Proton was initially released on 21 August 2018. Upon release, Valve announced a list of 27 games that were tested and certified to perform like their native Windows counterparts without requiring end-user tweaking. These include *Doom* (2016), *Quake*, and *Final Fantasy VI*.

Proton incorporates several libraries that improve 3D performance. These include Direct3D-to-Vulkan translation layers, namely DXVK for Direct3D 8, 9, 10 and 11, and VKD3D-Proton for Direct3D 12. A separate library known as D9VK handled Direct3D 9 support until it was merged into DXVK in December 2019.

## Compatibility

Proton generally has better compatibility than upstream Wine due to additional patches and components, such as esync, fshack, and VKD3D-Proton, that Wine has not accepted. Many Windows games beyond the official compatibility list work with Proton, albeit unofficially. The user can optionally force use of Proton for a specific game, even if a Linux version already exists. This may be done when a game's native Linux support is lacking or unstable.

### ProtonDB

ProtonDB is an unofficial community website that collects and displays crowdsourced data describing the compatibility of a given title with Proton, on a rating scale from "Borked" (doesn't work) to "Platinum" (works perfectly). The site is inspired by the WineHQ AppDB, which also collects and displays crowdsourced compatibility reports and uses a similar rating system.
