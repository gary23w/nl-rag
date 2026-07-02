---
title: "PhysX"
source: https://en.wikipedia.org/wiki/PhysX
domain: physx
license: CC-BY-SA-4.0
tags: physx engine, nvidia physx, gpu physics, physx rigid body
fetched: 2026-07-02
---

# PhysX

**PhysX** is an open-source realtime physics engine middleware SDK developed by Nvidia as part of the Nvidia GameWorks software suite.

Initially, video games supporting PhysX were meant to be accelerated by PhysX PPU (expansion cards designed by Ageia). However, after Ageia's acquisition by Nvidia, dedicated PhysX cards have been discontinued in favor of the API being run on CUDA-enabled GeForce GPUs. In both cases, hardware acceleration allowed for the offloading of certain physics calculations from the CPU, allowing it to perform other tasks instead.

PhysX and other middleware physics engines are used in many video games today because they allow game developers to save development time by not having to write their own code that implements classical mechanics (Newtonian physics) to do, for example, soft body dynamics.

## History

### NovodeX Physics

What is known today as PhysX originated as a physics simulation engine called NovodeX. NovodeX was a real-time middleware physics engine developed by **NovodeX AG** in the early 2000s, and initially released in 2002 commercially. While the name NovodeX is largely historical bygone product today, the core technology it introduced fundamentally reshaped game development and real-time physics in video games, serving as the direct architectural foundation for the industry-standard **PhysX** engine today.

**Origins And Market Context**

The engine was created by **NovodeX AG**, a Swiss technology group founded in 2001 by researchers and engineers from ETH Zurich (Swiss Federal Institute of Technology).

During the 2001–2003 window, the physics middleware market was highly competitive but technologically fragmented/limited. Developers looking to implement rigid-body dynamics had to choose between highly expensive commercial packages like Havok, middleware tightly coupled to specific physics engines like MathEngine’s Karma (used in Unreal Engine 2), or open-source solutions like the Open Dynamics Engine (ODE) which required significant manual integration.

NovodeX entered this landscape with a solver that prioritized extreme mathematical precision and forward-thinking hardware scaling. NovodeX was designed specifically to handle massive stacks of rigid bodies and complex ragdoll constraints without them collapsing.

On March 1, 2004, the second iteration of NovodeX Physics was released for commercial use.

**Technical Features**

NovodeX Physics stood out as a remarkably dependable tool for calculating game physics at the time. NovodeX was programmed entirely in the standard C++ format, it was specially built to tap into the power of multi-core processors and multithreading technology. Because of this flexible, forward-thinking design, the software could easily adapt to different hardware limitations, and this meant it could have ran smoothly on ordinary Windows PC's of the time, just as well as it did on 6th-generation consoles like the original Xbox, Nintendo GameCube, and PlayStation 2.

Rather than a single large block of code, NovodeX was a highly modular engine by design. The software was distributed under three distinct licenses such as Steel Rigid Body Physics, Granite Brittle Fracture, and the NovodeX Personal Edition, and its architecture was divided into five distinct sub-components:

- **The Foundation SDK:** This was the bedrock of the engine. It did not function by itself but instead, it supplied the core mathematical framework that every other module required to run.
- **The Collision SDK:** A flexible 3D detection library. Studios had the option to pair it natively with NovodeX's own rigid body systems or decouple it to use alongside external, third-party physics pipelines.
- **The Rigid Body SDK:** This module handled the actual physical simulation. It calculated the math behind momentum, velocity, acceleration, friction, energy, and constraints. While it relied heavily on the Foundation SDK, developers weren't locked into the native collision system and could substitute their own detection libraries if needed.
- **The Substance SDK:** This SDK was deigned for a more complex material simulation, this standalone component utilized the method (FEM) to model solid volumetric matter and environments. To function properly, it had to be paired with the Foundation math as well as active collision and rigid body systems (whether native to NovodeX itself or a third-party software).

To help artists actually get assets or props into the simulation, the NovodeX toolkit provided standard export plugins for popular 3D software of the era, including 3d modelling software like 3ds Max and MilkShape 3D. It also featured a browser and a specialized utility called "Tetmake," which was used specifically to generate meshes which were required by the Substance SDK.

Along with the main engine, the team released a separate sandbox tool called NovodeX Rocket. This user-friendly standalone program allowed designers to quickly test out some new game ideas, and instead of forcing them to write complex C++ code from scratch, it provided a custom scripting language (PSCL) and a built-in framework (ODF) so they could easily build and experiment with game physics.

**Unreal Engine 3 Integration**

The major turning point for NovodeX occurred during the development of **Unreal Engine 3** which launched in 2004. Epic Games had previously relied on MathEngine Karma to drive rigid-body dynamics, ragdolls and vehicles in Unreal Engine 2. However, as Karma was starting to show its age and the demands for next-generation physics grew, Epic began searching for a replacement for their next engine.

On April 2, 2004, Epic Games officially partnered with NovodeX AG, integrating the NovodeX physics solver natively into the Unreal Engine 3 pipeline. This integration effectively marked the end of Karma in the Unreal ecosystem and instantly established NovodeX as the prominent AAA physics engine.

## The Ageia Acquisition

In 2004, a fabless semiconductor company named **Ageia** was developing a dedicated hardware expansion card called the Physics Processing Unit (PPU). For this specific project Ageia needed a modern software API to interface with their hardware. Ageia recognized the superiority of the engine's multi-threaded architecture, and eventually acquired NovodeX AG. At the time of acquisition, the NovodeX Physics engine was at version 2.3

Following the acquisition, Ageia took the existing NovodeX codebase and rebranded it as Ageia **PhysX SDK**. The Swiss development team was retained, and continuing to build upon the original NovodeX solver to add hardware acceleration, fluid dynamics, and soft-body physics.. Ageia would also acquire Meqon in 2005 to integrate into the PhysX engine.

NovodeX is a prime example of a university research project turning into a massive success for the video game industry. In 2008, NVIDIA bought the company eventually acquired Ageia and updated the software so it could run directly on NVIDIA's graphics cards, which turned it into what is now called the PhysX engine. Today, whether a game is built in Unity, Unreal Engine, or by a AAA studio, the in-game physics are still driven by the same mathematics of the original NovodeX back in 2002-2004.

In 2008, Ageia was itself acquired by graphics technology manufacturer Nvidia. Nvidia started enabling PhysX hardware acceleration on its line of GeForce graphics cards and eventually dropped support for Ageia PPUs.

Nvidia PhysX SDK 3.0 was released in May 2011 and represented a significant rewrite of the SDK, bringing improvements such as more efficient multithreading and a unified code base for all supported platforms.

At GDC 2015, Nvidia made the source code for PhysX available on GitHub, but required registration at developer.nvidia.com. The proprietary SDK was provided to developers for free for both commercial and non-commercial use on Windows, Linux, macOS, iOS and Android platforms.

On December 3, 2018, PhysX was made open source under a 3-clause BSD license, but this change applied only to computer and mobile platforms.

On November 8, 2022, the open source release was updated to PhysX 5, under the same 3-clause BSD license.

In February 2025, support for 32-bit CUDA applications was deprecated for the GeForce RTX 50 series, rendering GPU-accelerated PhysX nonfunctional in 32-bit titles. This resulted in GPU PhysX options to be processed by the CPU when enabled, causing a degradation in performance, in titles such as *Mirror's Edge* and *Borderlands 2*.

On December 4th 2025, support for select games with 32-Bit GPU-Accelerated PhysX options was implemented by Nvidia.

## Features

The PhysX engine and SDK are available for Microsoft Windows, macOS, Linux, PlayStation 3, PlayStation 4, Xbox 360, Xbox One, Wii, iOS and Android.

PhysX is a multi-threaded physics simulation SDK. It supports rigid body dynamics, soft body dynamics (like cloth simulation, including tearing and pressurized cloth), ragdolls and character controllers, vehicle dynamics, particles and volumetric fluid simulation.

## Hardware acceleration

### PPU

A physics processing unit (PPU) is a processor specially designed to alleviate the calculation burden on the CPU, specifically calculations involving physics. PhysX PPUs were offered to consumers in the forms of PCI or PCIe cards by ASUS, BFG Technologies, Dell and ELSA Technology.

Beginning with version 2.8.3 of the PhysX SDK, support for PPU cards was dropped, and PPU cards are no longer manufactured. The last incarnation of PhysX PPU standalone card designed by Ageia had roughly the same PhysX performance as a dedicated 9800GTX.

### GPU

After Nvidia's acquisition of Ageia, PhysX development turned away from PPU expansion cards and focused instead on the GPGPU capabilities of modern GPUs.

Modern GPUs are very efficient at manipulating and displaying computer graphics, and their highly parallel structure makes them more effective than general-purpose CPUs for accelerating physical simulations using PhysX.

Any CUDA-ready GeForce graphics card (8-series or later GPU with a minimum of 32 cores and a minimum of 256 MB dedicated graphics memory) can take advantage of PhysX without the need to install a dedicated PhysX card.

## APEX

Nvidia APEX technology is a multi-platform scalable dynamics framework build around the PhysX SDK. It was first introduced in *Mafia II* in August 2010. Nvidia's APEX comprises the following modules: APEX Destruction, APEX Clothing, APEX Particles, APEX Turbulence, APEX ForceField and formerly APEX Vegetation which was suspended in 2011.

From version 1.4.1 APEX SDK is deprecated.

## Nvidia FleX

FleX is a particle based simulation technique for real-time visual effects. Traditionally, visual effects are made using a combination of elements created using specialized solvers for rigid bodies, fluids, clothing, etc. Because FleX uses a unified particle representation for all object types, it enables new effects where different simulated substances can interact with each other seamlessly. Such unified physics solvers are a staple of the offline computer graphics world, where tools such as Autodesk Maya's nCloth, and Softimage's Lagoa are widely used. The goal for FleX is to use the power of GPUs to bring the capabilities of these offline applications to real-time computer graphics.

## Criticism from Real World Technologies

On July 5, 2010, Real World Technologies published an analysis of the PhysX architecture. According to this analysis, most of the code used in PhysX applications at the time was based on x87 instructions without any multithreading optimization. This could cause significant performance drops when running PhysX code on the CPU. The article suggested that a PhysX rewrite using SSE instructions may substantially lessen the performance discrepancy between CPU PhysX and GPU PhysX.

In response to the Real World Technologies analysis, Mike Skolones, product manager of PhysX, said that SSE support had been left behind because most games are developed for consoles first and then ported to the PC. As a result, modern computers run these games faster and better than the consoles even with little or no optimization. Senior PR manager of Nvidia, Bryan Del Rizzo, explained that multithreading had already been available with CPU PhysX 2.x and that it had been up to the developer to make use of it. He also stated that automatic multithreading and SSE would be introduced with version 3 of the PhysX SDK.

PhysX SDK 3.0 was released in May 2011 and represented a significant rewrite of the SDK, bringing improvements such as more efficient multithreading and a unified code base for all supported platforms.

## Usage

### PhysX in video games

PhysX technology is used by game engines such as Unreal Engine (version 3 onwards), Unity, Gamebryo, Vision (version 6 onwards), Instinct Engine, Panda3D, Diesel, Torque, HeroEngine, and BigWorld.

As one of the handful of major physics engines, it is used in many games, such as *The Witcher 3: Wild Hunt*, *Warframe*, *Killing Floor 2*, *Batman: Arkham Knight*, *Planetside 2,*and *Borderlands 2*. Most of these games use the CPU to process the physics simulations.

Video games with optional support for hardware-accelerated PhysX often include additional effects such as tearable cloth, dynamic smoke or simulated particle debris.

### PhysX in other software

Other software with PhysX support includes:

- Active Worlds (AW), a 3D virtual reality platform with its client running on Windows
- Amazon Lumberyard, a 3D game development engine developed by Amazon
- Autodesk 3ds Max, Autodesk Maya and Autodesk Softimage, computer animation suites
- DarkBASIC Professional (with DarkPHYSICS upgrade), a programming language targeted at game development
- DX Studio, an integrated development environment for creating interactive 3D graphics
- ForgeLight, a game engine developed by the former Sony Online Entertainment.
- Futuremark's 3DMark06 and Vantage benchmarking tools
- Microsoft Robotics Studio, an environment for robot control and simulation
- Nvidia's SuperSonic Sled and Raging Rapids Ride, technology demos
- OGRE (via the NxOgre wrapper), an open source rendering engine
- The Physics Abstraction Layer, a physical simulation API abstraction system (it provides COLLADA and Scythe Physics Editor support for PhysX)
- Rayfire, a plug-in for Autodesk 3ds Max that allows fracturing and other physics simulations
- The Physics Engine Evaluation Lab, a tool designed to evaluate, compare and benchmark physics engines.
- Unreal Engine game development software by Epic Games. Unreal Engine 4.26 and onwards has officially deprecated PhysX.
- Unity by Unity ApS. Unity's Data-Oriented Technology Stack does not use PhysX.
