---
title: "Gradient noise"
source: https://en.wikipedia.org/wiki/Gradient_noise
domain: perlin-noise
license: CC-BY-SA-4.0
tags: perlin noise, simplex noise, gradient noise, value noise
fetched: 2026-07-02
---

# Gradient noise

**Gradient noise** is a type of noise commonly used as a procedural texture primitive in computer graphics. It is conceptually different from, and often confused with, value noise. This method consists of a creation of a lattice of random (or typically pseudorandom) gradients, dot products of which are then interpolated to obtain values in between the lattices. An artifact of some implementations of this noise is that the returned value at the lattice points is 0. Unlike the value noise, gradient noise has more energy in the high frequencies.

The first known implementation of a gradient noise function was Perlin noise, credited to Ken Perlin, who published the description of it in 1985. Later developments were Simplex noise and OpenSimplex noise.
