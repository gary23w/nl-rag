---
title: "Quasiparticle"
source: https://en.wikipedia.org/wiki/Quasiparticle
domain: condensed-matter-physics
license: CC-BY-SA-4.0
tags: condensed matter physics, crystal structure, electronic band structure, fermi surface
fetched: 2026-07-02
---

# Quasiparticle

In condensed matter physics, a **quasiparticle** is a concept used to describe a collective behavior of a group of particles that can be treated as if they were a single particle. Formally, quasiparticles and **collective excitations** are closely related phenomena that arise when a microscopically complicated system such as a solid behaves as if it contained different weakly interacting particles in vacuum.

For example, as an electron travels through a semiconductor, its motion is disturbed in a complex way by its interactions with other electrons and with atomic nuclei. The electron behaves as though it has a different effective mass travelling unperturbed in vacuum. Such an electron is called an *electron quasiparticle*. In another example, the aggregate motion of electrons in the valence band of a semiconductor or a hole band in a metal behave as though the material instead contained positively charged quasiparticles called *electron holes*. Other quasiparticles or collective excitations include the *phonon*, a quasiparticle derived from the vibrations of atoms in a solid, and the *plasmon*, a particle derived from plasma oscillation.

These phenomena are typically called *quasiparticles* if they are related to fermions, and called *collective excitations* if they are related to bosons, although the precise distinction is not universally agreed upon. Thus, electrons and electron holes (fermions) are typically called *quasiparticles*, while phonons and plasmons (bosons) are typically called *collective excitations*.

The quasiparticle concept is important in condensed matter physics because it can simplify the many-body problem in quantum mechanics. The theory of quasiparticles was started by the Soviet physicist Lev Landau in the 1930s.

## Overview

### General introduction

Solids are made of only three kinds of particles: electrons, protons, and neutrons. None of these are quasiparticles; instead a quasiparticle is an *emergent phenomenon* that occurs inside the solid. Therefore, while it is quite possible to have a single particle (electron, proton, or neutron) floating in space, a quasiparticle can only exist inside interacting many-particle systems such as solids.

Motion in a solid is extremely complicated: Each electron and proton is pushed and pulled (by Coulomb's law) by all the other electrons and protons in the solid (which may themselves be in motion). It is these strong interactions that make it very difficult to predict and understand the behavior of solids (see many-body problem). On the other hand, the motion of a *non-interacting* classical particle is relatively simple; it would move in a straight line at constant velocity. This is the motivation for the concept of quasiparticles: The complicated motion of the *real* particles in a solid can be mathematically transformed into the much simpler motion of imagined quasiparticles, which behave more like non-interacting particles.

In summary, quasiparticles are a mathematical tool for simplifying the description of solids.

### Relation to many-body quantum mechanics

The principal motivation for quasiparticles is that it is almost impossible to *directly* describe every particle in a macroscopic system. For example, a barely visible (0.1mm) grain of sand contains around 1017 nuclei and 1018 electrons. Each of these attracts or repels every other by Coulomb's law. In principle, the Schrödinger equation predicts exactly how this system will behave. But the Schrödinger equation in this case is a partial differential equation (PDE) on a 3×1018-dimensional vector space—one dimension for each coordinate (x, y, z) of each particle. Directly and straightforwardly trying to solve such a PDE is impossible in practice. Solving a PDE on a 2-dimensional space is typically much harder than solving a PDE on a 1-dimensional space (whether analytically or numerically); solving a PDE on a 3-dimensional space is significantly harder still; and thus solving a PDE on a 3×1018-dimensional space is quite impossible by straightforward methods.

One simplifying factor is that the system as a whole, like any quantum system, has a ground state and various excited states with higher and higher energy above the ground state. In many contexts, only the "low-lying" excited states, with energy reasonably close to the ground state, are relevant. This occurs because of the Boltzmann distribution, which implies that very-high-energy thermal fluctuations are unlikely to occur at any given temperature.

Quasiparticles and collective excitations are a type of low-lying excited state. For example, a crystal at absolute zero is in the ground state, but if one phonon is added to the crystal (in other words, if the crystal is made to vibrate slightly at a particular frequency) then the crystal is now in a low-lying excited state. The single phonon is called an *elementary excitation*. More generally, low-lying excited states may contain any number of elementary excitations (for example, many phonons, along with other quasiparticles and collective excitations).

When the material is characterized as having "several elementary excitations", this statement presupposes that the different excitations can be combined. In other words, it presupposes that the excitations can coexist simultaneously and independently. This is never *exactly* true. For example, a solid with two identical phonons does not have exactly twice the excitation energy of a solid with just one phonon, because the crystal vibration is slightly anharmonic. However, in many materials, the elementary excitations are very *close* to being independent. Therefore, as a *starting point*, they are treated as free, independent entities, and then corrections are included via interactions between the elementary excitations, such as "phonon-phonon scattering".

Therefore, using quasiparticles / collective excitations, instead of analyzing 1018 particles, one needs to deal with only a handful of somewhat-independent elementary excitations. It is, therefore, an effective approach to simplify the many-body problem in quantum mechanics. This approach is not useful for *all* systems, however. For example, in strongly correlated materials, the elementary excitations are so far from being independent that it is not even useful as a starting point to treat them as independent.

### Distinction between quasiparticles and collective excitations

Usually, an elementary excitation is called a "quasiparticle" if it is a fermion and a "collective excitation" if it is a boson. However, the precise distinction is not universally agreed upon.

There is a difference in the way that quasiparticles and collective excitations are intuitively envisioned. A quasiparticle is usually thought of as being like a dressed particle: it is built around a real particle at its "core", but the behavior of the particle is affected by the environment. A standard example is the "electron quasiparticle": an electron in a crystal behaves as if it had an effective mass which differs from its real mass. On the other hand, a collective excitation is usually imagined to be a reflection of the aggregate behavior of the system, with no single real particle at its "core". A standard example is the phonon, which characterizes the vibrational motion of every atom in the crystal.

However, these two visualizations leave some ambiguity. For example, a magnon in a ferromagnet can be considered in one of two perfectly equivalent ways: (a) as a mobile defect (a misdirected spin) in a perfect alignment of magnetic moments or (b) as a quantum of a collective spin wave that involves the precession of many spins. In the first case, the magnon is envisioned as a quasiparticle, in the second case, as a collective excitation. However, both (a) and (b) are equivalent and correct descriptions. As this example shows, the intuitive distinction between a quasiparticle and a collective excitation is not particularly important or fundamental.

The problems arising from the collective nature of quasiparticles have also been discussed within the philosophy of science, notably in relation to the identity conditions of quasiparticles and whether they should be considered "real" by the standards of, for example, entity realism.

### Effect on bulk properties

By investigating the properties of individual quasiparticles, it is possible to obtain a great deal of information about low-energy systems, including the flow properties and heat capacity.

In the heat capacity example, a crystal can store energy by forming phonons, and/or forming excitons, and/or forming plasmons, etc. Each of these is a separate contribution to the overall heat capacity.

### History

The idea of quasiparticles originated in Lev Landau's theory of Fermi liquids, which was originally invented for studying liquid helium-3. For these systems a strong similarity exists between the notion of quasiparticle and dressed particles in quantum field theory. The dynamics of Landau's theory is defined by a kinetic equation of the mean-field type. A similar equation, the Vlasov equation, is valid for a plasma in the so-called plasma approximation. In the plasma approximation, charged particles are considered to be moving in the electromagnetic field collectively generated by all other particles, and hard collisions between the charged particles are neglected. When a kinetic equation of the mean-field type is a valid first-order description of a system, second-order corrections determine the entropy production, and generally take the form of a Boltzmann-type collision term, in which figure only "far collisions" between virtual particles. In other words, every type of mean-field kinetic equation, and in fact every mean-field theory, involves a quasiparticle concept.

## Common examples

This section contains most common examples of quasiparticles and collective excitations.

- In solids, an electron quasiparticle is an electron as affected by the other forces and interactions in the solid. The electron quasiparticle has the same charge and spin as a "normal" (elementary particle) electron, and like a normal electron, it is a fermion. However, its mass can differ substantially from that of a normal electron; see the article effective mass. Its electric field is also modified, as a result of electric field screening. In many other respects, especially in metals under ordinary conditions, these so-called Landau quasiparticles closely resemble familiar electrons; as Crommie's "quantum corral" showed, an STM can image their interference upon scattering.
- A hole is a quasiparticle consisting of the lack of an electron in a state; it is most commonly used in the context of empty states in the valence band of a semiconductor. A hole has the opposite charge of an electron.
- A phonon is a collective excitation associated with the vibration of atoms in a rigid crystal structure. It is a quantum of a sound wave.
- A magnon is a collective excitation associated with the electrons' spin structure in a crystal lattice. It is a quantum of a spin wave.
- In materials, a photon quasiparticle is a photon as affected by its interactions with the material. In particular, the photon quasiparticle has a modified relation between wavelength and energy (dispersion relation), as described by the material's index of refraction. It may also be termed a polariton, especially near a resonance of the material. For example, an exciton-polariton is a superposition of an exciton and a photon; a phonon-polariton is a superposition of a phonon and a photon.
- A plasmon is a collective excitation, which is the quantum of plasma oscillations (wherein all the electrons simultaneously oscillate with respect to all the ions).
- A polaron is a quasiparticle which comes about when an electron interacts with the polarization of its surrounding ions.
- An exciton is an electron and hole bound together.
