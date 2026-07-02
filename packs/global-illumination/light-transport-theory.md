---
title: "Light transport theory"
source: https://en.wikipedia.org/wiki/Light_transport_theory
domain: global-illumination
license: CC-BY-SA-4.0
tags: global illumination, radiosity rendering, photon mapping, indirect lighting
fetched: 2026-07-02
---

# Light transport theory

**Light transport theory** deals with the mathematics behind calculating the energy transfers between media that affect visibility. This article is currently specific to light transport in rendering processes such as global illumination and high dynamic range imaging (HDRI).

## Light

### Light transport

The amount of light transported is measured by **flux density**, or luminous flux per unit area on the point of the surface at which it is measured.

### Light transport equation

Light transport describes the propagation of visible electromagnetic energy in macroscopic environments.

The mathematical theory underpinning light transport can be described by the Hamiltonian approach.

The light transport equation can be stated using the Poisson brackets as:

${\dot {l}}=\{H,l\}$

where H is the Hamiltonian and l is the light energy density.

For light, the Hamiltonian has the form:

$H={\frac {c}{n(p)}}||p||$ .

In such a form, the light transport equation is identical to the phase space Liouville equation.

## Radiometry and energy transfer

Radiometry is the science of measuring electromagnetic radiation, including visible light. It forms the foundation of light transport theory, which models how light interacts with surfaces, volumes, and media.

- **Energy Transfer Models**: Light interacts with media through absorption, reflection, and transmission. These processes are governed by the rendering equation, which models the distribution of light in a scene.

## Geometric models

### Hemisphere

Given a surface S, a hemisphere H can be projected onto S to calculate the amount of incoming and outgoing light. If a point P is selected at random on the surface S, the amount of incoming and outgoing light can be calculated by its projection onto the hemisphere.

### Hemicube

The **hemicube model** works similarly to the hemisphere model, except that a hemicube is projected instead of a hemisphere. The similarity is only conceptual; the actual calculation, done through numerical integration, has a different form factor.

## Wave-particle duality

Light transport theory incorporates both **wave-based** and **particle-based** descriptions of light. While wave-based models rely on the principles of Maxwell's equations, particle models use ray optics and Monte Carlo methods to simulate light paths.

- **Monte Carlo Ray Tracing**: A stochastic method used in light transport simulations to compute global illumination. This method leverages randomness to estimate solutions to the rendering equation, particularly in complex scenes with multiple light interactions.

## Advanced models

**Bidirectional reflectance distribution function (BRDF)**

The BRDF models how light is reflected on an opaque surface. It is defined as the ratio of reflected radiance in a given direction to the incident irradiance. BRDFs are crucial in light transport theory for simulating realistic material behavior.

**Participating media**

Light transport within volumes (e.g., fog, smoke, or translucent objects) is modeled using the radiative transfer equation (RTE). Participating media are integral to achieving photorealism in scenes involving volumetric light effects.

## Applications in rendering

Rendering converts a model into an image either by simulating a method, such as light transport, to get physically accurate photorealistic images, or by applying some kind of style as non-photorealistic rendering (NPR). The two basic operations in light transport are transport (how much light gets from one place to another) and scattering (how surfaces interact with light).

### Global illumination

Global illumination simulates all light interactions in a scene, including indirect lighting. It employs light transport theory to compute effects such as color bleeding and soft shadows.

### Non-photorealistic rendering (NPR)

Unlike photorealistic rendering, non-photorealistic rendering (NPR) uses light transport models to stylize images, often prioritizing artistic intent over physical accuracy.
