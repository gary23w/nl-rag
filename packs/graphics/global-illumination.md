---
title: "Global illumination"
source: https://en.wikipedia.org/wiki/Global_illumination
domain: graphics
license: CC-BY-SA-4.0
tags: computer graphics, rasterization, ray tracing, shader, graphics pipeline, texture mapping
fetched: 2026-07-02
---

# Global illumination

Rendering without global illumination. Areas that lie outside of the ceiling lamp's direct light lack definition. For example, the lamp's housing appears completely uniform. Without the ambient light added into the render, it would appear uniformly black.

Rendering with global illumination. Light is reflected by surfaces, and colored light transfers from one surface to another. Notice how color from the red wall and green wall (not visible) reflects onto other surfaces in the scene. Also notable is the

caustic

projected onto the red wall from light passing through the glass sphere.

**Global illumination** (**GI**), or **indirect illumination**, refers to a group of algorithms used in 3D computer graphics meant to add more realistic lighting to 3D scenes. Such algorithms take into account not only the light that comes directly from a light source (*direct illumination*), but also subsequent "bounces" where light rays are reflected by other surfaces in the scene (*indirect illumination*).

The term "global illumination" was first used by Turner Whitted in his paper "An improved illumination model for shaded display", to differentiate between illumination calculations at a local scale (using geometric information directly, such as in Phong shading), a microscopic scale (extending local geometry with microfacet detail), and a global scale, including not only the geometry itself but also the visibility of every other object in the scene. Theoretically, reflections, refractions, transparency, and shadows are all examples of global illumination, because when simulating them, one object affects the rendering of another (as opposed to an object being affected only by a direct source of light). In practice, however, only the simulation of diffuse inter-reflection or caustics is called global illumination, especially in real-time settings.

## Algorithms

Global illumination is a key aspect to the realism of a 3D scene. Naive 3D lighting will only take into account direct light, meaning any light which radiates off a light source and bounces directly into the virtual camera. Shadows will appear completely dark, due to light not interacting with any other surface before it reaches the camera. As this is not what occurs in real life, we perceive the resulting image as incomplete. Applying full global illumination allows for the missing effects that makes an image feel more natural. However, global illumination is computationally more expensive and consequently much slower to generate.

Most algorithms, especially those focusing on real-time solutions, model diffuse inter-reflection exclusively, which is a very important part of global illumination; however, some also model indirect specular reflections, refraction, and indirect shadowing, which allows for a closer approximation of the reality and produces more appealing images. The algorithms used to calculate the distribution of light energy between surfaces of a scene are closely related to heat transfer simulations performed using finite-element methods in engineering design.

Radiosity, ray tracing, beam tracing, cone tracing, path tracing, Metropolis light transport and photon mapping are all examples of algorithms used for global illumination in offline settings, some of which may be used together to yield results that trade between accuracy and speed, depending on the implementation.

## Real-time applications

Achieving accurate computation of global illumination in real-time remains difficult. On one end, the diffuse inter-reflection component of global illumination is sometimes approximated by an "ambient" term in the lighting equation, which is also called "ambient lighting" or "ambient color" in 3D software. Though this method is one of the cheapest ways to simulate indirect lighting, when used alone it does not provide an adequately realistic effect. Ambient lighting is known to "flatten" shadows in 3D scenes, making the overall visual effect more bland. Beyond ambient lighting, techniques which trace the path of light accurately have historically been either too slow for consumer hardware or limited to static and precomputed environments. A classic real-time approach is precomputed radiance transfer, which precomputes light transport so that low-frequency lighting can be changed in real time while preserving effects such as soft shadows and interreflections, but its original form generally assumed fixed geometry and could not vary lighting and view simultaneously in real time. This proves problematic, as most applications allow for input from a user that can affect their surroundings, and the precalculation steps may introduce constraints upon the artists. Consequently, research has been dedicated to finding a balance between adequate performance, accurate visual results, and interactivity.

Starting with Nvidia's RTX 20 series, consumer graphics hardware has been extended to allow for ray tracing computations to be performed in real time through hardware acceleration. This has allowed for further improvements, as applications can now harness the power of this acceleration to provide not only precise lighting results, but the ability to affect said lighting dynamically. Some content that has taken advantage of this capability includes Cyberpunk 2077, Indiana Jones and the Great Circle, and Alan Wake 2, among others.

For an overview of the current state of real-time global illumination, see or.

## Procedure

Algorithms which attempt to simulate global illumination are numerical approximations of the rendering equation. Well-known algorithms for computing global illumination include path tracing, photon mapping and radiosity. The following approaches can be distinguished here:

- Inversion: $L=(1-T)^{-1}L^{e}\,$
  - Not applied in practice
- Expansion: $L=\sum _{i=0}^{\infty }T^{i}L^{e}$
  - Bi-directional approach: Photon mapping + Distributed ray tracing, Bi-directional path tracing, Metropolis light transport
- Iteration: $L_{n}tl_{e}+=L^{(n-1)}$
  - Radiosity

A full overview can be found in.

## List of methods

| Method | Application | Description/Notes |
|---|---|---|
| Ray tracing | Offline/Real-time | The process of tracing a set of virtual paths (rays) from one point in space to another, testing for intersections with geometry. Ray tracing is useful as it can imitate the way light physically travels in the real world. Several variants exist for solving problems related to sampling, aliasing, and soft shadows, such as Distributed ray tracing, cone tracing, and beam tracing. |
| Path tracing | Offline | An extension to ray tracing that uses the Monte Carlo method of sampling to approximate a solution to the rendering equation. This makes path tracing unbiased. Variants include bi-directional path tracing and energy redistribution path tracing. |
| Photon mapping | Offline | Rays from both the camera and each light source are traced around the scene and connected to produce plausible radiance. It provides consistent results, but is biased. Variants include progressive photon mapping and stochastic progressive photon mapping. |
| Radiosity | Offline | A finite element method approach to the rendering equation, dividing the scene into patches and computing the radiosity between each patch. It is good for precomputations, but assumes completely diffuse geometries. Improved versions include instant radiosity and bidirectional instant radiosity, both of which use virtual point lights (VPLs) instead of patches. |
| Lightcuts | Offline | A method of improving performance when computing the contribution of several light sources at a surface, by clustering lights into a light tree and selectively choosing the appropriate "cut" for each point. Enhanced variants include multidimensional lightcuts and bidirectional lightcuts. |
| Point based global illumination | Offline | Point based global illumination (PBGI) discretizes the scene into a point-cloud which contains radiance information for the surface a point lies on. It has been extensively used in movie animations for its relative speed and lack of noise compared to per-pixel calculations like path tracing. |
| Metropolis light transport | Offline | Builds upon bi-directional path tracing using the Metropolis-Hastings algorithm, exploring paths adjacent to ones which have already been found. It remains unbiased, while usually converging faster than path tracing. An extension was introduced called multiplexed metropolis light transport. |
| Image-based lighting | Real-time | Image-based lighting (IBL) can refer to a number of different effects. Usually, it refers to an approximate method of global illumination through the use of high-dynamic-range images (HDRIs), also known as environment maps, which encompass the entire scene and light surfaces based on their normal direction. IBL has also been used to describe image proxies, or image-based reflections, which represent surfaces as flat image planes to improve the appearance of reflections. They have been used in games such as Remember Me and Thief (2014), as well as the Unreal Engine 3 Samaritan demo. |
| Ambient occlusion | Real-time | An approximate solution to global illumination that shades the areas of a scene most likely to be occluded by another object. It describes how "exposed" a point in the scene is to incoming light, and has been useful to improve realism for a comparatively low cost as opposed to indirect light. The effect can be reproduced through alterations to other methods, such as VXGI or SSGI. |
| Irradiance volumes | Real-time | Irradiance volumes encode global illumination results in evenly spaced points in 3D space (probes) for rendering of static scenes. Dynamic surfaces can be lit based on their position inside the volume and their normal direction. Initially used cubemaps to store irradiance at each probe, but was later improved by compressing into spherical harmonics (SH). |
| Light propagation volumes | Real-time | The light propagation volume (LPV) approximately achieves global illumination in real-time with lattices and spherical harmonics to represent the spatial and angular distribution of light in the scene. The technique was later expanded to include approximate occlusion and specular indirect lighting, as well as farther coverage through the nesting of multiple lattices with decreasing resolution. It was used in earlier versions of CryEngine and Unreal Engine. |
| Voxel-based solutions | Real-time | Voxel-based techniques use a discretization of the scene into a volume to simplify lighting calculations. Solutions in this category might store varying information, such as geometric occupancy only, or the material properties of underlying surfaces, etc. Examples include compressed radiance caching volumes, voxel cone tracing, sparse voxel octrees, and VXGI. Voxel cone tracing was used and improved in The Tomorrow Children, where the technique provided the entirety of the lighting in the game. |
| Precomputed probe solutions | Real-time | Extensions of the irradiance volume that simulate global illumination of dynamic light sources by relighting the scene based on non-lighting information, such as geometry or visibility, precomputed in a "baking" stage beforehand. Examples of this technique include deferred radiance transfer volumes and a successor used in *Tom Clancy's The Division*. |
| Screen-space global illumination | Real-time | Screen-space global illumination (SSGI) methods use the information visible to the screen, usually through the use of an already existing G-Buffer, to approximate indirect lighting. Variants exist for ambient occlusion (SSAO), for which the technique was initially developed, and specular reflections (SSR). The most common approach is screen-space ray marching. Additional techniques include screen space directional occlusion, "deep" buffers, and horizon-based visibility bitmasks. |
| Dynamic Diffuse Global Illumination | Real-time | Unlike precomputed probe solutions, Dynamic Diffuse Global Illumination (DDGI) uses probes to calculate both lighting and geometric information in real time, using hardware-accelerated ray tracing to approximate geometry. An offshoot of this technique uses SDF primitives to represent a scene and reflective shadow maps to sample lights, improving on performance by removing the hardware requirement and better approximating occlusions, at the cost of manual setup. |
| Global Illumination Based on Surfels | Real-time | A technique created by Electronic Arts' SEED group that discretizes the scene with surface elements, "surfels", in real time, and uses them to accumulate the result of light calculations done through hardware ray tracing. It borrows from the ideas of point based global illumination. It is currently integrated into the Frostbite engine. |
| Lumen | Real-time | A full global illumination solution that relies on an advanced screen-space radiance caching method, alongside an SDF volume representation of objects, to provide accurate and stable indirect lighting, shadowing, and reflections within a fully dynamic scene. Screen probes use importance sampling techniques to intelligently distribute rays, and distant lighting uses a world space probe fallback. It is integrated into Unreal Engine 5. |
