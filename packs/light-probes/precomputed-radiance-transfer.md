---
title: "Precomputed Radiance Transfer"
source: https://en.wikipedia.org/wiki/Precomputed_Radiance_Transfer
domain: light-probes
license: CC-BY-SA-4.0
tags: light probe capture, spherical harmonic lighting, irradiance probe, precomputed radiance transfer
fetched: 2026-07-02
---

# Precomputed Radiance Transfer

**Precomputed Radiance Transfer** (**PRT**) is a computer graphics technique used to render a scene in real time with complex light interactions being precomputed to save time. Radiosity methods can be used to determine the diffuse lighting of the scene, however PRT offers a method to dynamically change the lighting environment.

In essence, PRT computes the illumination of a point as a linear combination of incident irradiance. An efficient method must be used to encode this data, such as spherical harmonics.

When spherical harmonics are used to approximate the light transport function, only low-frequency effects can be handled with a reasonable number of parameters. Ren Ng et al. extended this work to handle higher frequency shadows by replacing spherical harmonics with non-linear wavelets.

## Capabilities and limitations

PRT is useful when an expensive light-transport simulation can be run offline and reused at run time. This allows effects such as soft shadows, interreflections and subsurface scattering to be included without changing the cost of the run-time shader for each added light in the environment. Standard PRT also has important restrictions: objects are usually assumed to be rigid, global effects are not preserved between independently moving objects, and low-order spherical harmonic lighting produces soft low-frequency shadows rather than sharp high-frequency detail.

## Local deformable PRT and applications

Local, deformable PRT extends the technique to deforming models by focusing on nearby surface details such as bumps and wrinkles, using zonal harmonics that can be rotated more cheaply than spherical harmonics. Sloan, Luna and Snyder demonstrated the method for real-time soft shadows, interreflections and subsurface scattering on deforming objects.

PRT and related spherical-harmonic lighting have also appeared in game and graphics-library workflows. In *Halo 3*, Bungie described storing incoming lighting at surface points as spherical-harmonic vectors and using PRT lighting as part of the game's global-illumination pipeline. Direct3D 9's D3DX utility library included a PRT engine, compressed buffers and texture workflows for generating and representing transfer vectors.

Teemu Mäki-Patola gives a clear introduction to the topic based on the work of Peter-Pike Sloan et al. At SIGGRAPH 2005, a detailed course on PRT was given.
