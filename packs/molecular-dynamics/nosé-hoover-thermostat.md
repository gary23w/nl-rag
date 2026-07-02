---
title: "Nosé–Hoover thermostat"
source: https://en.wikipedia.org/wiki/Nos%C3%A9%E2%80%93Hoover_thermostat
domain: molecular-dynamics
license: CC-BY-SA-4.0
tags: molecular dynamics, force field chemistry, lennard-jones potential, periodic boundary conditions
fetched: 2026-07-02
---

# Nosé–Hoover thermostat

The **Nosé–Hoover thermostat** is a deterministic algorithm for constant-temperature molecular dynamics simulations. It was originally developed by Shuichi Nosé and was improved further by William G. Hoover. Although the heat bath of Nosé–Hoover thermostat consists of only one imaginary particle, simulation systems achieve realistic constant-temperature condition (canonical ensemble). Therefore, the Nosé–Hoover thermostat has been commonly used as one of the most accurate and efficient methods for constant-temperature molecular dynamics simulations.

## Introduction

In classical molecular dynamics, simulations are done in the microcanonical ensemble; a number of particles, volume, and energy have a constant value. In experiments, however, the temperature is generally controlled instead of the energy. The ensemble of this experimental condition is called a canonical ensemble. Importantly, the canonical ensemble is different from microcanonical ensemble from the viewpoint of statistical mechanics. Several methods have been introduced to keep the temperature constant while using the microcanonical ensemble. Popular techniques to control temperature include velocity rescaling, the Andersen thermostat, the Nosé–Hoover thermostat, Nosé–Hoover chains, the Berendsen thermostat and Langevin dynamics.

The central idea is to simulate in such a way that we obtain a canonical ensemble, where we fix the particle number N , the volume V and the temperature T . This means that these three quantities are fixed and do not fluctuate. The temperature of the system is connected to the average kinetic energy via the equation:

$\langle E_{\mathrm {kin} }\rangle ={\frac {3}{2}}Nk_{\mathrm {B} }T.$

Although the temperature and the average kinetic energy are fixed, the instantaneous kinetic energy fluctuates (and with it the velocities of the particles).

## Description

In the approach of Nosé, a Hamiltonian with an extra degree of freedom for heat bath, *s*, is introduced;

${\mathcal {H}}(P,R,p_{s},s)=\sum _{i}{\frac {\mathbf {p} _{i}^{2}}{2ms^{2}}}+{\frac {1}{2}}\sum _{ij,i\not =j}U\left(\mathbf {r_{i}} -\mathbf {r_{j}} \right)+{\frac {p_{s}^{2}}{2Q}}+gkT\ln \left(s\right),$

where *g* is the number of independent momentum degrees of freedom of the system, *R* and *P* represent all coordinates $\mathbf {r_{i}}$ and $\mathbf {p_{i}}$ and *Q* is a parameter which determines the timescale on which the rescaling occurs. Improper choice of *Q* can lead to ineffective thermostatting or the introduction of nonphysical temperature oscillations. The coordinates *R*, *P* and *t* in this Hamiltonian are virtual. They are related to the real coordinates as follows:

$R'=R,~P'={\frac {P}{s}}~{\text{and}}~t'=\int ^{t}{\frac {\mathrm {d} \tau }{s}}$ ,

where the coordinates with an accent are the real coordinates. The ensemble average of the above Hamiltonian at $g=3N$ is equal to the canonical ensemble average.

Hoover (1985) used the phase-space continuity equation, a generalized Liouville equation, to establish what is now known as the Nosé–Hoover thermostat. This approach does not require the scaling of the time (or, in effect, of the momentum) by *s*. The Nosé–Hoover algorithm is nonergodic for a single harmonic oscillator. In simple terms, it means that the algorithm fails to generate a canonical distribution for a single harmonic oscillator. This feature of the Nosé–Hoover algorithm has prompted the development of newer thermostatting algorithms—the kinetic moments method that controls the first two moments of the kinetic energy, Bauer–Bulgac–Kusnezov scheme, Nosé–Hoover chains, etc. Using a similar method, other techniques like the Braga–Travis configurational thermostat and the Patra–Bhattacharya full phase thermostat have been proposed.
