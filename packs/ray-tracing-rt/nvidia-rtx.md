---
title: "Nvidia RTX"
source: https://en.wikipedia.org/wiki/Nvidia_RTX
domain: ray-tracing-rt
license: CC-BY-SA-4.0
tags: ray tracing, ray tracing hardware, rtx gpu, bvh acceleration
fetched: 2026-07-02
---

# Nvidia RTX

**Nvidia RTX** (also known as **Nvidia GeForce RTX** under the GeForce brand) is a professional visual computing platform created by Nvidia, used in mainstream PCs for gaming as well as being used in workstations for designing complex large-scale models in architecture and product design, scientific visualization, energy exploration, and film and video production (especially under the RTX PRO and formerly Quadro RTX brands).

Nvidia RTX features hardware-enabled real-time ray tracing. Historically, ray tracing had been reserved to non-real time applications (like CGI in visual effects for movies and in photorealistic renderings), with video games having to rely on direct lighting and precalculated indirect contribution for their rendering. RTX facilitates a new development in computer graphics of generating interactive images that react to lighting, shadows and reflections. RTX runs on Nvidia Volta-, Turing-, Ampere-, Ada Lovelace- and Blackwell-based GPUs, specifically utilizing the Tensor cores (and new RT cores on Turing and successors) on the architectures for ray-tracing acceleration.

In March 2019, Nvidia announced that selected GTX 10 series (Pascal) and GTX 16 series (Turing) cards would receive support for subsets of RTX technology in upcoming drivers, although functions and performance will be affected by their lack of dedicated hardware cores for ray tracing.

In October 2020, Nvidia announced Nvidia RTX A6000 as the first Ampere-architecture-based graphics card for use in professional workstations in the Nvidia RTX product line, replacing the former Quadro product line of professional graphics cards.

Nvidia worked with Microsoft to integrate RTX support with Microsoft's DirectX Raytracing API (DXR). RTX is currently available through Nvidia OptiX and for DirectX. For the Turing and Ampere architectures, it is also available for Vulkan.

## Components

In addition to ray tracing, RTX includes artificial intelligence integration, common asset formats, rasterization (CUDA) support, and simulation APIs. The components of RTX are:

- AI-accelerated features (NGX)
- Asset formats (USD and MDL)
- Rasterization including advanced shaders
- Raytracing via OptiX, Microsoft DXR and Vulkan
- Simulation tools:
  - CUDA 10
  - Flex
  - PhysX

## Features and software

### Ray tracing

In computer graphics, ray tracing generates an image by tracing rays cast through pixels of an image plane and simulating the effects of its encounters with virtual objects. This enables advanced effects that better reflect real-world optical properties, such as softer and more realistic shadows and reflections, as compared to traditional rasterization techniques which prioritize performance over accuracy.

Nvidia RTX achieves this through a combination of hardware and software acceleration. On a hardware level, RTX cards feature fixed-function "RT cores" that are designed to accelerate mathematical operations needed to simulate rays, such as bounding volume hierarchy traversal. The software implementation is open to individual application developers. As ray-tracing is still computationally intensive, many developers choose to take a hybrid rendering approach where certain graphical effects, such as shadows and reflections, are performed using ray-tracing, while the remaining scene is rendered using the more performant rasterization.

#### Optix

Nvidia OptiX is part of Nvidia DesignWorks. OptiX is a high-level, or "to-the-algorithm" API, meaning that it is designed to encapsulate the entire algorithm of which ray tracing is a part, not just the ray tracing itself. This is meant to allow the OptiX engine to execute the larger algorithm without application-side changes.

Aside from computer graphics rendering, OptiX also helps in optical and acoustical design, radiation and electromagnetic research, artificial intelligence queries and collision analysis.

### Chat with RTX

Chat with RTX is an AI-based assistant that runs locally on the user's Windows PC. It uses a large language model and requires an RTX 30, 40 or 50 series GPU with at least 8GB of VRAM. It can be downloaded from Nvidia's website.

### RTX Remix

RTX Remix is a game modding platform designed by Nvidia to remaster older titles by implementing modern technologies such as ray tracing, DLSS, and enhanced assets.

## List of Nvidia RTX cards

Nvidia has released many cards that support RTX, including the 20, 30, 40, and 50 series:

- Nvidia GeForce RTX 20 series
  - Nvidia GeForce RTX 2050
  - Nvidia GeForce RTX 2060
  - Nvidia GeForce RTX 2060 Super
  - Nvidia GeForce RTX 2070
  - Nvidia GeForce RTX 2070 Super
  - Nvidia GeForce RTX 2080
  - Nvidia GeForce RTX 2080 Super
  - Nvidia GeForce RTX 2080 Ti
  - Nvidia Titan RTX
- Nvidia GeForce RTX 30 series
  - Nvidia GeForce RTX 3050
  - Nvidia GeForce RTX 3050 Ti
  - Nvidia GeForce RTX 3060
  - Nvidia GeForce RTX 3060 Ti
  - Nvidia GeForce RTX 3070
  - Nvidia GeForce RTX 3070 Ti
  - Nvidia GeForce RTX 3080
  - Nvidia GeForce RTX 3080 Ti
  - Nvidia GeForce RTX 3090
  - Nvidia GeForce RTX 3090 Ti
- Nvidia GeForce RTX 40 series
  - Nvidia GeForce RTX 4050
  - Nvidia GeForce RTX 4060
  - Nvidia GeForce RTX 4060 Ti
  - Nvidia GeForce RTX 4070
  - Nvidia GeForce RTX 4070 Super
  - Nvidia GeForce RTX 4070 Ti
  - Nvidia GeForce RTX 4070 Ti Super
  - Nvidia GeForce RTX 4080
  - Nvidia GeForce RTX 4080 Super
  - Nvidia GeForce RTX 4090
  - Nvidia GeForce RTX 4090D
- Nvidia GeForce RTX 50 series
  - Nvidia GeForce RTX 5050
  - Nvidia GeForce RTX 5060
  - Nvidia GeForce RTX 5060 Ti
  - Nvidia GeForce RTX 5070
  - Nvidia GeForce RTX 5070 Ti
  - Nvidia GeForce RTX 5080
  - Nvidia GeForce RTX 5090
  - Nvidia GeForce RTX 5090D (v1/v2)
- Nvidia A series workstation cards
  - Nvidia RTX A400 4 GB
  - Nvidia RTX A1000 8 GB
  - Nvidia RTX A2000 6 GB/12 GB
  - Nvidia RTX A4000 16 GB
  - Nvidia RTX A4500 20 GB
  - Nvidia RTX A5000 24 GB
  - Nvidia RTX A5500 24 GB
  - Nvidia RTX A6000 48 GB
  - Nvidia RTX 5000 Ada Lovelace 32 GB
  - Nvidia RTX 6000 Ada Lovelace 48 GB
  - Nvidia RTX Pro 6000 Blackwell 96 GB
- Nvidia A series server cards
  - Nvidia A10
  - Nvidia A50
