---
title: "Metal (API)"
source: https://en.wikipedia.org/wiki/Metal_(API)
domain: metal-compute
license: CC-BY-SA-4.0
tags: metal api, compute kernel, gpu computing, shader program
fetched: 2026-07-02
---

# Metal (API)

**Metal** is a low-level, low-overhead hardware-accelerated 3D graphic and compute shader API created by Apple, debuting in iOS 8. Metal combines functions similar to OpenGL and OpenCL in one API. It is intended to improve performance by offering low-level access to the GPU hardware for apps on iOS, iPadOS, macOS, tvOS and visionOS (though not watchOS). It is similar to low-level APIs on other platforms such as Vulkan and DirectX 12.

Metal is an object-oriented API that can be invoked using the Swift, Objective-C or C++17 programming languages. Full-blown GPU execution is controlled via the Metal Shading Language.

## Features

Metal aims to provide low-overhead access to the GPU. Commands are encoded beforehand and then submitted to the GPU for asynchronous execution. The application controls when to wait for the execution to complete thus allowing application developers to increase throughput by encoding other commands while commands are executed on the GPU or save power by explicitly waiting for GPU execution to complete. Additionally, command encoding is CPU independent thus applications can encode commands to each CPU thread independently. Lastly, render states are pre-computed beforehand, allowing the GPU driver to know in advance how to configure and optimize the render pipeline before command execution.

Metal improves the capabilities of GPGPU programming by using compute shaders. Metal uses a specific shading language based on C++14, implemented using Clang and LLVM.

Metal allows application developers to create Metal resources such as buffers and textures. Resources can be allocated on the CPU, GPU, or both and provides facilities to update and synchronize allocated resources. Metal can also enforce a resource's state during a command encoder's lifetime.

On macOS, Metal can provide application developers the discretion to specify which GPU to execute. Application developers can choose between the low-power integrated GPU of the CPU, the discrete GPU (on certain MacBooks and Macs) or an external GPU connected through Thunderbolt. Application developers also have the preference on how GPU commands are executed on which GPUs and provides suggestion on which GPU a certain command is most efficient to execute (commands to render a scene can be executed by the discrete GPU while post-processing and display can be handled by the integrated GPU).

### Metal Performance Shaders

Metal Performance Shaders is a highly optimized library of graphics functions that can help application developers achieve great performance at the same time decrease work on maintaining GPU family specific functions. It provides functions including:

- Image filtering algorithms
- Neural network processing
- Advanced math operations
- Ray tracing

## History

Metal has been available since June 2, 2014 on iOS devices powered by Apple A7 or later, and since June 8, 2015 on Macs (2012 models or later) running OS X El Capitan.

On June 5, 2017, at WWDC, Apple announced the second version of Metal, to be supported by macOS High Sierra, iOS 11 and tvOS 11. Metal 2 is not a separate API from Metal and is supported by the same hardware. Metal 2 enables more efficient profiling and debugging in Xcode, accelerated machine learning, lower CPU workload, support for virtual reality on macOS, and specificities of the Apple A11 GPU, in particular.

At the 2020 WWDC, Apple announced the migration of the Mac to Apple silicon. Macs using Apple silicon will feature Apple GPUs with a feature set combining what was previously available on macOS and iOS, and will be able to take advantage of features tailored to the tile based deferred rendering (TBDR) architecture of Apple GPUs.

At the 2022 WWDC, Apple announced the third version of Metal (Metal 3), which would debut with the release of macOS Ventura, iOS 16 and iPadOS 16. Metal 3 introduces the MetalFX upscaling framework, which renders complex scenes in less time per frame with high-performance upscaling and anti-aliasing, mesh shaders support. Also announced possibility to use C/C++ for Metal API.

At the 2023 WWDC, Apple announced a brand new toolkit called the Game Porting Toolkit to port Windows 10/11-based games. It includes an environment to test binaries, translation layers from HLSL to MSL, and Metal-cpp bindings. Jeremy Sandmel announced a new Game Mode for macOS Sonoma, and Hideo Kojima announced *Death Stranding* for the macOS App Store.

At the 2024 WWDC, Apple announced Game Porting Toolkit 2, along with the release of new games such as *Control: Ultimate Edition*, *Frostpunk 2*, and *Assassin's Creed Shadows* for macOS.

At the 2025 WWDC, Apple announced Metal 4, a new version of the API featuring a unified command encoder system, support for neural rendering, and new technologies such as MetalFX Frame Interpolation and a ray tracing denoiser.

## Supported GPUs

The first version of Metal supports the following hardware and software:

- Apple A7 SoC or later with iOS 8 or later
- Apple M1 SoC or later with macOS 11 or later
- Intel Processor with Intel HD and Iris Graphics Ivy Bridge series or later with OS X 10.11 or later
- AMD Graphics with GCN or RDNA architecture with OS X 10.11 or later
- NVIDIA Graphics with Kepler architecture with OS X 10.11 to macOS 11 operating system
- NVIDIA Graphics with Maxwell architecture or Pascal architecture with OS X 10.11 to macOS 10.13 operating system

The second version of Metal supports the following hardware and software:

- Apple A7 SoC or later with iOS 11 or later
- Apple M1 SoC or later with macOS 11 or later
- Intel Processor with Intel HD and Iris Graphics Skylake series or later with macOS 10.13 or later
- AMD Graphics with GCN or RDNA architecture with macOS 10.13 or later

The third version of Metal supports the following hardware and software:

- Apple A13 or later with iOS 16, iPadOS 16
- Apple A14 or later with iOS 16, iPadOS 16 or later
- Apple M1 SoC or later with iPadOS 16 or later
- Apple M1 SoC or later with macOS 13 or later
- Intel Processor with Intel UHD 630 or Iris Plus (Kaby Lake or later) with macOS 13 or later
- AMD Graphics with RDNA architecture (5000 and 6000 series) and Pro Vega (5th generation GCN architecture)

The fourth version of Metal supports the following hardware and software:

- Apple A14 or later with iOS 26, iPadOS 26 or later
- Apple M1 SoC or later with iPadOS 26, macOS 26 or later

## Adoption

According to Apple, more than 148,000 applications use Metal directly, and 1.7 million use it through high-level frameworks, as of June 2017. macOS games using Metal for rendering are listed below.

| Title | Developer (macOS version) | Game engine | MacOS release date (OpenGL/DirectX) | Metal-based release date | Metal support notes |
|---|---|---|---|---|---|
| *Ark: Survival Evolved* | Studio Wildcard | Unreal Engine 4 |   | 29 August 2017 |   |
| *Assassin's Creed Shadows* | Ubisoft Quebec | Ubisoft Anvil |   | 20 March 2025 |   |
| *ARMA 3* | Virtual Programming | Real Virtuality | 31 August 2015 |   | Metal support in beta since 17 September 2017 |
| *Baldur's Gate III* | Larian Studios | Divinity Engine 4.0 |   | 22 September 2023 | Metal support in early access since 6 October 2020 |
| *Ballistic Overkill* | Aquiris Game Studio | Unity Engine 5 |   | 28 March 2017 |   |
| *Batman: Arkham City* | Feral Interactive | Unreal Engine 3 | 18 October 2013 |   | Metal support since 21 February 2019 with v1.2 |
| *Batman: The Enemy Within* | Telltale Games | Telltale Tool |   | 8 August 2017 |   |
| *BattleTech* | Harebrained Schemes | Unity Engine 5 |   | 24 April 2018 |   |
| *Bioshock Remastered* | Feral Interactive | Unreal Engine 2.5 |   | 22 August 2017 |   |
| *Bioshock 2 Remastered* | Feral Interactive | Unreal Engine 2.5 |   | 22 October 2020 |   |
| *Cyberpunk 2077* | CD Projekt | REDengine 4 |   | 17 July 2025 | Support for Metal 4 |
| *Cities: Skylines* | Paradox Interactive | Unity Engine 5 | 10 March 2015 |   | Metal support since 18 May 2017 |
| *Civilization VI* | Aspyr Media | LORE | 24 October 2016 |   | Metal support since 5 April 2019 |
| *Company of Heroes 2* | Feral Interactive | Essence Engine 3 | 21 January 2015 |   | Metal support since 19 October 2018 |
| *Control: Ultimate Edition* | Remedy Entertainment | Northlight Engine |   | 26 March 2025 |   |
| *Dead Island 2* | Dambuster Studios | Unreal Engine 4 |   | 24 July 2025 |   |
| *Deus Ex: Mankind Divided* | Feral Interactive | Dawn Engine |   | 12 December 2017 |   |
| *DiRT Rally* | Feral Interactive | EGO Engine 2.5 |   | 16 November 2017 |   |
| *Divinity: Original Sin II* | Larian Studios | Divinity Engine 2 |   | 31 January 2019 |   |
| *Dota 2* | Valve | Source 2 | 18 July 2013 |   | MoltenVK was announced on 26 February 2018. The option to use this became available on 31 May 2018. |
| *The Elder Scrolls Online* | Zenimax Online Studios | *N/A* | 4 April 2014 | 22 October 2018 | OpenGL Renderer replaced with Vulkan via MoltenVK wrapper (translates Vulkan API calls to Metal) in patch 4.2.5 |
| *Empire: Total War* | Feral Interactive | TW Engine 3 | 4 March 2009 |   | Metal support since 16 December 2019 |
| *EVE Online* | CCP Games | *N/A* | 6 November 2007 | 14 October 2021 | Previously available on macOS via DirectX 9.0 from November 2007 until February 2009; native macOS version using Metal released 14 November 2021 |
| *Everspace* | Rockfish | Unreal Engine 4 |   | 26 May 2017 |   |
| *F1 2016* | Feral Interactive | EGO Engine 4.0 |   | 6 April 2017 |   |
| *F1 2017* | Feral Interactive | EGO Engine 4.0 |   | 25 August 2017 |   |
| *Fortnite* | Epic Games | Unreal Engine 4 |   | 25 July 2017 |   |
| *Frostpunk* | 11 Bit Studios | Liquid Engine |   | 24 February 2021 |   |
| *Frostpunk 2* | 11 Bit Studios | Unreal Engine 5 |   | 20 September 2024 |   |
| *Gravel* | Virtual Programming | Unreal Engine 4 |   | 20 January 2019 |   |
| *Guardians of the Galaxy: The Telltale Series* | Telltale Games | Telltale Tool |   | 18 April 2017 |   |
| *Headlander* | Double Fine Productions | Buddha Engine |   | 18 November 2016 |   |
| *Heroes of the Storm* | Blizzard Entertainment | SC2 Engine | 2 June 2015 |   | Metal support in beta since 24 January 2017 (temporarily removed on 29 November 2017 until ?) |
| *Hitman* | Feral Interactive | Glacier 2 |   | 20 June 2017 |   |
| Hollow Knight | Team Cherry | Unity Engine |   | 11 April 2017 |   |
| Hollow Knight: Silksong | Team Cherry | Unity Engine |   | 4 September 2025 |   |
| *Life Is Strange: Before the Storm* | Feral Interactive | Unity Engine |   | 13 September 2018 |   |
| *Life Is Strange 2* | Feral Interactive | Unreal Engine 4 |   | 2019 |   |
| *Mafia III* | Aspyr Media | Illusion Engine |   | 11 May 2017 |   |
| *Medieval II: Total War* | Feral Interactive | TW Engine 2 | 17 December 2015 |   | Metal support since 25 October 2018 |
| *Micro Machines World Series* | Virtual Programming | Unity Engine 5 |   | 30 June 2017 |   |
| *Minecraft: Story Mode - Season Two* | Telltale Games | Telltale Tool |   | 11 July 2017 |   |
| *MXGP3* | Virtual Programming | Unreal Engine 4 |   | 23 November 2018 |   |
| *Napoleon: Total War* | Feral Interactive | TW Engine 3 | 2 July 2013 |   | Metal support since 25 October 2019 with v1.2 |
| *Obduction* | Cyan Worlds | Unreal Engine 4 |   | 29 March 2017 |   |
| *Observer* | Bloober Team | Unreal Engine 4 |   | 24 October 2017 |   |
| *Quake II* | id Software | Quake II engine |   | 9 February 2019 | A port using MoltenVK was released as vkQuake2. |
| *Refunct* | Dominique Grieshofer | Unreal Engine 4 |   | 5 September 2016 |   |
| *Resident Evil 2* | Capcom | RE Engine |   | 10 December 2024 |   |
| *Resident Evil 3* | Capcom | RE Engine |   | 18 March 2025 |   |
| *Resident Evil 4* | Capcom | RE Engine |   | 20 December 2023 |   |
| *Resident Evil Village* | Capcom | RE Engine |   | 28 October 2022 | First macOS game with MetalFX support |
| *Rise of the Tomb Raider* | Feral Interactive | Foundation Engine |   | 12 April 2018 |   |
| *Shadow of the Tomb Raider* | Feral Interactive | Foundation Engine |   | 2019 |   |
| *Sid Meier's Railroads!* | Feral Interactive | Gamebryo | 1 November 2012 |   | Metal support since 18 December 2018 |
| *The Sims 3* | Maxis Redwood Shores | The Sims 3 Engine | 2 June 2009 | 28 October 2020 |   |
| *The Sims 4* | Maxis | SmartSim | 17 February 2015 |   | Metal support added 12 November 2019 |
| *Sky: Children of the Light* | Thatgamecompany | *N/A* |   | 18 July 2019 | Native Metal support added since pre-global live in November 2017 |
| *Starcraft* | Blizzard Entertainment | Modified Warcraft II engine | 20 November 2001 |   | Metal support since 2 July 2020 with v1.23.5 |
| *StarCraft II* | Blizzard Entertainment | SC2 Engine | 27 July 2010 |   | Metal support in beta since 24 January 2017 |
| *Tomb Raider* | Feral Interactive | Foundation Engine | 17 January 2014 |   | Metal support with v1.2 in July 2019 |
| *Total War: Rome Remastered* | Feral Interactive | TW Engine 2 |   | 29 April 2021 |   |
| *Total War: Shogun 2* | Feral Interactive | TW Engine 3 | 31 July 2014 |   | Metal support since 4 October 2019 |
| *Total War: Shogun 2: Fall of the Samurai* | Feral Interactive | TW Engine 3 | 18 December 2014 |   | Metal support since 4 October 2019 |
| *Total War: Three Kingdoms* | Feral Interactive | TW Engine 3 |   | 23 May 2019 |   |
| *Total War: Warhammer* | Feral Interactive | TW Engine 3 |   | 19 April 2017 |   |
| *Total War: Warhammer II* | Feral Interactive | TW Engine 3 |   | 20 November 2018 |   |
| *Total War Saga: Thrones of Britannia* | Feral Interactive | TW Engine 3 |   | 24 May 2018 |   |
| *Total War Saga: Troy* | Feral Interactive | TW Engine 3 |   | 13 August 2020 |   |
| Transport Fever 2 | Urban Games | *N/A* |   | 23 February 2021 | Metal support using MoltenVK and OpenGL |
| *Universe Sandbox* | Giant Army | Unity Engine 5 | TBA |   | Metal support in beta since June 2017 |
| *Unreal Tournament* | Epic Games | Unreal Engine 4 | Cancelled |   | Metal support since January 2017 |
| *War Thunder* | Gaijin Entertainment | Dagor Engine 4 | 1 November 2012 |   | Metal support added 24 May 2017 (removed in ? 2018 and reintroduced 27 August 2020) |
| *Warhammer 40,000: Dawn of War III* | Feral Interactive | Essence Engine 4 |   | 9 June 2017 |   |
| *The Witness* | Thekla, Inc | Thekla Engine |   | 8 March 2017 |   |
| *World of Warcraft* | Blizzard Entertainment | WoW Engine | 23 November 2004 |   | Metal support since August 2016 |
| *X-Plane 11* | Laminar Research | *N/A* | 30 May 2017 |   | Metal support in beta since 2 April 2020 |
