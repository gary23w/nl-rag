---
title: "Havok (software)"
source: https://en.wikipedia.org/wiki/Havok_(software)
domain: physx
license: CC-BY-SA-4.0
tags: physx engine, nvidia physx, gpu physics, physx rigid body
fetched: 2026-07-02
---

# Havok (software)

**Havok** is a middleware software suite developed by the Irish company Havok (originally **Telekynesis Research Limited**). Havok provides physics engine, navigation, and cloth simulation components that can be integrated into video game engines.

In 2007, Intel acquired Havok Inc. In 2008, Havok was honored at the 59th Annual Technology & Engineering Emmy Awards for advancing the development of physics engines in electronic entertainment. In 2015, Microsoft acquired Havok.

## History

Telekynesis Research Limited was founded in 1998 by two university students Hugh Reynolds and Steven Collins of the computer science department in Trinity College, Dublin who would form the studio based in Dublin, Ireland. The software was originally named **Omniate** initially, but was then renamed to Havok (Named after the Marvel X-Men character).

Version 1.0 of the Havok SDK was unveiled at the Game Developers Conference (GDC) in March 2000.

### Ipion Virtual Physics

In 1999, a German-software company based in Munich had developed their own physics engine called **Ipion Virtual Physics**, it was a real-time middleware physics engine developed in the late 1990s by the German software company Ipion Software. Designed for the simulation of rigid body dynamics in video games and interactive media, it was a significant early competitor in the physics middleware market along with MathEngine. In June 2000, Ipion was acquired by Havok, and its core technologies were subsequently integrated into the **Havok Physics** engine.

Ipion was founded in 1998. The development of the Virtual Physics engine was led by chief architect Oliver Strunk and a decentralized team of engineers across Germany. Developed in C++, the engine was built with cross-platform compatibility in mind, supporting Microsoft Windows, Linux, Solaris, and the PlayStation 2 console.

On June 8, 2000, the Irish company Havok acquired Ipion. This merger transformed the Ipion team into Havok's Munich office, marking the company's third international location after Dublin and Palo Alto. The acquisition was a pivotal moment in the industry, as the sophisticated algorithms of the Ipion Virtual Physics SDK became the technological foundation for Havok's 1.5 release and beyond.

Ipion was noted for its advanced handling of complex physical interactions for the era. Its architecture included:

- **Collision Detection:** A multi-phase system that optimized performance by utilizing bounding volumes before proceeding to detailed geometric checks.
- **Constraint Systems:** The SDK allowed developers to define kinematic pairs with specific degrees of freedom. This included native support for complex joints such as ball-and-socket and hinge joints.
- **Dynamic Controllers:** Beyond simple impulses, the engine allowed for persistent forces through various "controllers," enabling simulations of magnets, springs, and customized user-defined forces.
- **Pipeline Integration:** While the SDK did not include proprietary 3D exporters, it was uniquely compatible with the *Quake II* .BSP file format, allowing developers to integrate physics directly into established level design pipelines.

At the time of its commercial peak, the Ipion SDK was licensed for approximately $50,000 to $60,000 per project. The software package provided developers with a 76-page technical manual and a comprehensive C++ library.

Ipion's most visible legacy is found in the 3DMark 2001 SE benchmark. The software's "Game 4" and "Physics Feature" tests utilized the Ipion engine to demonstrate high-end hardware capabilities through complex rigid body simulations. It was also utilized in several retail titles, including the 2001 racing game *Route 66* (known internationally as *USA Racer*). Following the Havok merger, the Ipion name was phased out, though its influence persists in modern physics simulations through its direct contribution to the Havok engine.

It is also famously used in *Half-Life 2*, albeit heavily modified by Valve as VPhysics (VPhysics uses custom proprietary code from Valve, with additional Havok code for constraints and memory optimized partial polytype). *Half-Life 2* is lauded as one of the early licensees of a real-time physics middleware such as the Ipion Virtual Physics early in its development cycle at the start of the millennium.

### Notable credits using IVP

- Amapi3D (3D Modelling Software)
- Virtools
- Harley-Davidson: Race Across America (1999)
- Harley-Davidson: Wheels of Freedom (2000)
- Autobahnraser 3 (2000)
- Top Gear Dare Devil (2000)
- Kawasaki Fantasy Motocross (2001)
- Europaraser
- Open Kart (2001)

- *3DMark 2001 SE* (Benchmark)
- *USA Racer* (2001) (*Route 66 and A2 Racer Goes USA! in other regions)*
- Counter-Strike: Source (2004)
- Half-Life Source (2004)
- *Half-Life 2* (2004)
- Day Of Defeat: Source (2005)
- Garry's Mod (2006)

The first game to utilize Havok was a game released in 1999 called London Racer developed by Davilex Games which had a long partnership with Havok/IVP.

## Products

The Havok middleware suite consists of the following modules:

- **Havok Physics**: Originally from Ipion Software (Ipion Virtual Physics), it is designed primarily for video games, and allows for real-time collision and dynamics of rigid bodies in three dimensions. It provides multiple types of dynamic constraints between rigid bodies (e.g. for ragdoll physics), and has a highly optimized collision detection library. By using dynamical simulation, Havok Physics allows for more realistic virtual worlds in games. The company was developing a specialized version of Havok Physics called Havok FX that made use of ATI and Nvidia GPUs for physics simulations, but the goal of GPU acceleration did not materialize until several years later.
- **Havok Navigation**: In 2009, Havok released Havok AI, which provides advanced pathfinding capabilities for games. Havok AI provides navigation mesh generation, pathfinding and path following for video game environments. In 2024, this product was renamed to Havok Navigation.
- **Havok Cloth**: Released in 2008, Havok Cloth deals with efficient simulation of character garments and soft body dynamics.
- **Havok Destruction (discontinued)**: Also released in 2008, Havok Destruction provides tools for creation of destructible and deformable rigid body environments.
- **Havok Animation Studio (discontinued)**: Havok Animation Studio is formally known as Havok Behavior and Havok Animation. Havok Behavior is a runtime SDK for controlling game character animation at a high level using finite-state machines. Havok Animation provides efficient playback and compression of character animations in games, and features such as inverse kinematics.
- **Havok Script (discontinued)**: Havok Script is a Lua-compatible virtual machine designed for video game development. It is shipped as part of the Havok Script Studio.
- **Havok Vision Engine** **(discontinued):** In 2011, Havok acquired German game engine development company Trinigy and their Vision Engine and toolset.

## Supported platforms

The Havok SDK is multi-platform by nature and is always updated to run on the majority of the latest platforms. Licensees are given access to most of the C/C++ source-code, giving them the freedom to customize the engine's features, or port it to different platforms although some libraries are only provided in binary format. In March 2011, Havok showed off a version of the Havok physics engine designed for use with the Sony Xperia Play, or more specifically, Android 2.3. During Microsoft's BUILD 2012 conference, Havok unveiled a full technology suite for Windows 8, Windows RT, Windows Phone 8 and later Windows 10.

As of February 2023, Havok supports 18 targets across 10 platforms. These platforms include: Windows, Linux, Xbox Series S/X, PlayStation 5, iOS, Nintendo Switch and Android.

## Prebuilt engines

### Unity

In 2019, Unity and Havok signed a partnership to build a complete physics solution for DOTS-based projects in Unity. This was completed and released as production ready in December 2022.

### Unreal Engine

Havok maintains integrations for all of their products to Epic's Unreal Engine. Havok Physics can be used to replace the inbuilt physics engine (Chaos Physics) at an engine level, while Havok Navigation is a stand-alone plugin, and Havok Cloth is a separate tool that works alongside the engine.

### Babylon.js

In April 2023, Babylon.js 6.0 was released with a physics implementation by Havok. This implementation was released as a WASM plugin and involved an overhaul of the Babylon.js Physics API.

## Usage

### Video games

The first game to use Havok Physics was *London Racer* in 1999 by Davilex Games. In 2023, Havok products were used in twelve of the top twenty best selling video games in the United States.

### Other software

Havok can also be found in:

- Futuremark's 3DMark2001 and 03 benchmarking tools
- a plug-in for Maya animation software
- Valve's Source game engine uses VPhysics, which is a physics engine modified from Havok
- Havok addons in 3D Studio Max
- Adobe Shockwave

Havok supplies tools (the "Havok Content Tools") for export of assets for use with all Havok products from Autodesk 3ds Max, Autodesk Maya, and (formerly) Autodesk Softimage. Havok was also used in the virtual world *Second Life*, with all physics handled by its online simulator servers, rather than by the users' client computers. An upgrade to Havok version 4 was released in April 2008 and an upgrade to version 7 started in June 2010. *Second Life* resident Emilin Nakamori constructed a weight-driven, pendulum-regulated mechanical clock functioning entirely by Havok Physics in March 2019.

## Pricing and Licensing

In 2025, Havok introduced a new pricing model targeting smaller and indie game developers, offering access to Havok Physics and Havok Navigation for a one-time, per-title fee.

## Historic Pages

- Wayback Machine
- Team
- **Ipion Virtual Physics Engine**
- Havok Buys Ipion
- Havok and Ipion head for the top
