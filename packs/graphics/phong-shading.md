---
title: "Phong shading"
source: https://en.wikipedia.org/wiki/Phong_shading
domain: graphics
license: CC-BY-SA-4.0
tags: computer graphics, rasterization, ray tracing, shader, graphics pipeline, texture mapping
fetched: 2026-07-02
---

# Phong shading

In 3D computer graphics, **Phong shading, Phong interpolation,** or **normal-vector interpolation shading** is an interpolation technique for surface shading invented by computer graphics pioneer Bui Tuong Phong. Phong shading interpolates surface normals across rasterized polygons and computes pixel colors based on the interpolated normals and a reflection model. *Phong shading* may also refer to the specific combination of Phong interpolation and the Phong reflection model.

## History

Phong shading and the Phong reflection model were developed at the University of Utah by Bui Tuong Phong, who published them in his 1973 Ph.D. dissertation and a 1975 paper. Phong's methods were considered radical at the time of their introduction, but have since become the *de facto* baseline shading method for many rendering applications. Phong's methods have proven popular due to their generally efficient use of computation time per rendered pixel.

## Phong interpolation

Phong shading improves upon Gouraud shading and provides a better approximation of the shading of a smooth surface. Phong shading assumes a smoothly varying surface normal vector. The Phong interpolation method works better than Gouraud shading when applied to a reflection model with small specular highlights such as the Phong reflection model.

The most serious problem with Gouraud shading occurs when specular highlights are found in the middle of a large polygon. Since these specular highlights are absent from the polygon's vertices and Gouraud shading interpolates based on the vertex colors, the specular highlight will be missing from the polygon's interior. This problem is fixed by Phong shading.

Unlike Gouraud shading, which interpolates colors across polygons, in Phong shading, a normal vector is linearly interpolated across the surface of the polygon from the polygon's vertex normals. The surface normal is interpolated and normalized at each pixel and then used in a reflection model, e.g. the Phong reflection model, to obtain the final pixel color. Phong shading is more computationally expensive than Gouraud shading since the reflection model must be computed at each pixel instead of at each vertex.

In modern graphics hardware, variants of this algorithm are implemented using pixel or fragment shaders.

## Phong reflection model

*Phong shading* may also refer to the specific combination of Phong interpolation and the Phong reflection model, which is an empirical model of local illumination. It describes the way a surface reflects light as a combination of the diffuse reflection of rough surfaces with the specular reflection of shiny surfaces. It is based on Bui Tuong Phong's informal observation that shiny surfaces have small intense specular highlights, while dull surfaces have large highlights that fall off more gradually. The reflection model also includes an *ambient* term to account for the small amount of light that is scattered about the entire scene.
