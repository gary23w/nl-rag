---
title: "DXVK"
source: https://en.wikipedia.org/wiki/DXVK
domain: proton-gaming
license: CC-BY-SA-4.0
tags: proton compatibility tool, steam deck, wine gaming layer, dxvk translation
fetched: 2026-07-02
---

# DXVK

**DXVK** is an open-source translation layer which converts Direct3D 8/9/10/11 calls to Vulkan. It is used by Proton/Steam for Linux, by Intel Windows drivers, VirtualBox 7.x, and it can be used to run Direct3D-based games under Windows using Vulkan. DXVK has been confirmed to support over 80% of Direct3D Windows games "near flawlessly".

## History

DXVK was first developed by Philip "doitsujin" Rebohle to support Direct3D 11 games only driven by frustration over poor compatibility and low performance of Wine's Direct3D 11 to OpenGL translation layer.

In 2018, the developer was sponsored by Valve to work on the project full-time in order to advance compatibility of the Linux version of Steam with Windows games.

In 2019, DXVK received Direct3D 9 support by merging with d9vk.

In November 2022, version 2.0 was released, introducing improvements to Direct3D 9 memory management, shader compilation, state cache, and support for Direct3D 11 feature level 12_1. Vulkan 1.3 support is now required.

Released on January 24, 2023, version 2.1 implemented HDR support and improved quality for certain old games.

Released on May 12, 2023, version 2.2 added D3D11On12 support.

Released on July 10, 2024, version 2.4 added support for Direct3D 8.

Released on November 11, 2024, version 2.5 features an overhauled memory and resource management which resulted in VRAM savings up to 1 GB in certain games. Direct3D 8 and 9 received support for software cursor.

In June 2026, DXVK 3.0 replaced its legacy DXBC shader translation code with `dxbc-spirv`, reducing memory use in some games and moving more shader compilation work off the application thread. The release also began requiring Vulkan 1.4-era driver support. Users of AMD RDNA 1.0 and RDNA 2.0 architectures on Windows are advised against using DXVK 3.0 because "Windows driver for these GPUs no longer receives feature updates, can only use the slow legacy binding model, and suffers from severe performance issues that are not seen on any other driver".

## Forks

D7VK is a DXVK fork that uses its D3D9 back-end to implement support for Direct3D 3, 5, 6 and 7. The project does not expect to be upstreamed or merged with the parent.

## Controversies

The use of Wine/DXVK has gotten users banned from some online gaming platforms because these layers have been classified as illegitimate by their anti-cheat systems.
