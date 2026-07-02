---
title: "Ray marching"
source: https://en.wikipedia.org/wiki/Ray_marching
domain: screen-space-reflections
license: CC-BY-SA-4.0
tags: screen space reflections, ssr rendering, screen space raymarching, reflection rendering
fetched: 2026-07-02
---

# Ray marching

**Ray marching** is a class of rendering methods for 3D computer graphics where rays are traversed iteratively, effectively dividing each ray into smaller ray segments, sampling some function at each step. For example, in volume ray casting the function would access data points from a 3D scan. In Sphere tracing, the function estimates a distance to step next. Ray marching is also used in physics simulations as an alternative to ray tracing where analytic solutions of the trajectories of light or sound waves are solved. Ray marching for computer graphics often takes advantage of SDFs to determine a maximum safe step-size, while this is less common in physics simulations a similar adaptive step method can be achieved using adaptive Runge-Kutta methods.

The technique dates back to at least the 1980s; the 1989 paper "Hypertexture" by Ken Perlin contains an early example of a ray marching method.

## Distance-aided ray marching

### Sphere tracing

In **sphere tracing**, or **sphere-assisted ray marching** an intersection point is approximated between the ray and a surface defined by a signed distance function (SDF). The SDF is evaluated for each iteration in order to be able take as large steps as possible without missing any part of the surface. A threshold is used to cancel further iteration when a point has reached that is close enough to the surface. As powerful GPU hardware became more widely available, this method was popularized by the demoscene and Inigo Quilez, co-creator of Shadertoy.

For simple scenes with basic 3D shapes, ray marching does not have many benefits over ray tracing (which finds intersections without marching through the space). Strengths of SDF ray marching are, for example, when morphing shapes, approximating soft shadows, repetition of geometry, and algorithmically defined scenes.

Signed distance functions exist for many primitive 3D shapes. They can be combined using mathematical operations like modulo and booleans to form more complex surfaces. For instance, taking the modulus of an SDF's input coordinates tiles its volume across all of space, and taking the maximum of two SDFs gives their volumes' surface of intersection. Because SDFs can be defined for many fractals, sphere tracing is often used for 3D fractal rendering.

### Cube-assisted

A similar technique to sphere-assisted ray marching, the use of cubes and taxicab distance can be used to render voxel volumes.

## Volumetric ray marching

In volumetric ray marching, each ray is traced so that color and/or density can be sampled along the ray and then be combined into a final pixel color. This is often used for example when rendering clouds or 3D medical scans.

## Deferred shading

When rendering screen space effects, such as screen space reflection (SSR) and screen space shadows, rays are traced using G-buffers, where depth and surface normal data is stored per each 2D pixel.
