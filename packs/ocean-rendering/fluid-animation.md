---
title: "Fluid animation"
source: https://en.wikipedia.org/wiki/Fluid_animation
domain: ocean-rendering
license: CC-BY-SA-4.0
tags: ocean rendering, gerstner wave ocean, fft ocean simulation, ocean water surface
fetched: 2026-07-02
---

# Fluid animation

**Fluid animation** refers to computer graphics techniques for generating realistic animations of fluids such as water and smoke. Fluid animations are typically focused on emulating the qualitative visual behavior of a fluid, with less emphasis placed on rigorously correct physical results, although they often still rely on approximate solutions to the Euler equations or Navier–Stokes equations that govern real fluid physics. Fluid animation can be performed with different levels of complexity, ranging from time-consuming, high-quality animations for films, or visual effects, to simple and fast animations for real-time animations like computer games.

## Relationship to computational fluid dynamics

Fluid animation differs from computational fluid dynamics (CFD) in that fluid animation is used primarily for visual effects, whereas computational fluid dynamics is used to study the behavior of fluids in a scientifically rigorous way.

## Development

The development of fluid animation techniques based on the Navier–Stokes equations began in 1996, when Nick Foster and Dimitris Metaxas implemented solutions to 3D Navier-Stokes equations in a computer graphics context, basing their work on a scientific CFD paper by Harlow and Welch from 1965. Up to that point, a variety of simpler methods had primarily been used, including ad-hoc particle systems, lower dimensional techniques such as height fields, and semi-random turbulent noise fields.

In 1999, Jos Stam published the "Stable Fluids" method, which exploited a semi-Lagrangian advection technique and implicit integration of viscosity to provide unconditionally stable behaviour. This allowed for much larger time steps and therefore faster simulations. This general technique was extended by Ronald Fedkiw and co-authors to handle more realistic smoke and fire, as well as complex 3D water simulations using variants of the level-set method.

Some notable academic researchers in this area include Jerry Tessendorf, James F. O'Brien, Ron Fedkiw, Mark Carlson, Greg Turk, Robert Bridson, Ken Museth, and Jos Stam.

## Software

Many 3D computer graphics programs implement fluid animation techniques. RealFlow is a standalone commercial package that has been used to produce visual effects in movies, television shows, commercials, and games. RealFlow implements a fluid-implicit particle (FLIP; an extension of the Particle-in-cell method) solver, a hybrid grid, and a particle method that allows for advanced features such as foam and spray. Maya and Houdini are two other commercial 3D computer graphics programs that allow for fluid animation.

Blender is an open-source 3D computer graphics program that utilized a particle-based Lattice Boltzmann method for animating fluids until the integration of the open-source mantaflow project in 2020 with a wide range of Navier-Stokes solver variants.
