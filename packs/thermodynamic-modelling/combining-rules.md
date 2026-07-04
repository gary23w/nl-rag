---
title: "Combining rules"
source: https://en.wikipedia.org/wiki/Combining_rules
domain: thermodynamic-modelling
license: CC-BY-SA-4.0
tags: thermodynamic modelling
fetched: 2026-07-04
---

# Combining rules

In computational chemistry and molecular dynamics, the **combination rules** or **combining rules** are equations that provide the interaction energy between two dissimilar non-bonded atoms, usually for the part of the potential representing the van der Waals interaction. In the simulation of mixtures, the choice of combining rules can sometimes affect the outcome of the simulation.

## Combining rules for the Lennard-Jones potential

The Lennard-Jones Potential is a mathematically simple model for the interaction between a pair of atoms or molecules. One of the most common forms is

$V_{LJ}=4\varepsilon \left[\left({\frac {\sigma }{r}}\right)^{12}-\left({\frac {\sigma }{r}}\right)^{6}\right]$

where *ε* is the depth of the potential well, *σ* is the finite distance at which the inter-particle potential is zero, *r* is the distance between the particles. The potential reaches a minimum, of depth *ε*, when *r* = 21/6σ ≈ 1.122σ.

### Lorentz-Berthelot rules

The Lorentz rule was proposed by H. A. Lorentz in 1881:

$\sigma _{ij}={\frac {\sigma _{ii}+\sigma _{jj}}{2}}$

The Lorentz rule is only analytically correct for hard sphere systems. Intuitively, since $\sigma _{i},\sigma _{j}$ loosely reflect the radii of particle i and j respectively, their averages can be said to be the effective radii between the two particles at which point repulsive interactions become severe.

The Berthelot rule (Daniel Berthelot, 1898) is given by:

$\epsilon _{ij}={\sqrt {\epsilon _{ii}\epsilon _{jj}}}$

.

Physically, this arises from the fact that $\epsilon$ is related to the induced dipole interactions between two particles. Given two particles with instantaneous dipole $\mu _{i},\mu _{j}$ respectively, their interactions correspond to the products of $\mu _{i},\mu _{j}$ . An arithmetic average of $\epsilon _{i}$ and $\epsilon _{j}$ will not however, result in the average of the two dipole products, but the average of their logarithms would be.

These rules are the most widely used and are the default in many molecular simulation packages, but are not without failings.

### Waldman-Hagler rules

The Waldman-Hagler rules are given by:

$r_{ij}^{0}=\left({\frac {(r_{i}^{0})^{6}+(r_{j}^{0})^{6}}{2}}\right)^{1/6}$

and

$\epsilon _{ij}=2{\sqrt {\epsilon _{i}\cdot \epsilon _{j}}}\left({\frac {(r_{i}^{0})^{3}\cdot (r_{j}^{0})^{3}}{(r_{i}^{0})^{6}+(r_{j}^{0})^{6}}}\right)$

### Fender-Halsey

The Fender-Halsey combining rule is given by

$\epsilon _{ij}={\frac {2\epsilon _{i}\epsilon _{j}}{\epsilon _{i}+\epsilon _{j}}}$

### Kong rules

The Kong rules for the Lennard-Jones potential are given by:

$\epsilon _{ij}\sigma _{ij}^{6}=\left(\epsilon _{ii}\sigma _{ii}^{6}\epsilon _{jj}\sigma _{jj}^{6}\right)^{1/2}$

$\epsilon _{ij}\sigma _{ij}^{12}=\left[{\frac {(\epsilon _{ii}\sigma _{ii}^{12})^{1/13}+(\epsilon _{jj}\sigma _{jj}^{12})^{1/13}}{2}}\right]^{13}$

### Others

Many others have been proposed, including those of Tang and Toennies Pena, Hudson and McCoubrey and Sikora (1970).

## Combining rules for other potentials

### Good-Hope rule

The Good-Hope rule for Mie–Lennard‐Jones or Buckingham potentials is given by:

$\sigma _{ij}={\sqrt {\sigma _{ii}\sigma _{jj}}}$

### Hogervorst rules

The Hogervorst rules for the Exp-6 potential are:

$\epsilon _{12}={\frac {2\epsilon _{11}\epsilon _{22}}{\epsilon _{11}+\epsilon _{22}}}$

and

$\alpha _{12}={\frac {1}{2}}(\alpha _{11}+\alpha _{22})$

### Kong-Chakrabarty rules

The Kong-Chakrabarty rules for the Exp-6 potential are:

$\left[{\frac {\epsilon _{12}\alpha _{12}e^{\alpha _{12}}}{(\alpha _{12}-6)\sigma _{12}}}\right]^{2\sigma _{12}/\alpha _{12}}=\left[{\frac {\epsilon _{11}\alpha _{11}e^{\alpha _{11}}}{(\alpha _{11}-6)\sigma _{11}}}\right]^{\sigma _{11}/\alpha _{11}}\left[{\frac {\epsilon _{22}\alpha _{22}e^{\alpha _{22}}}{(\alpha _{22}-6)\sigma _{22}}}\right]^{\sigma _{22}/\alpha _{22}}$

${\frac {\sigma _{12}}{\alpha _{12}}}={\frac {1}{2}}\left({\frac {\sigma _{11}}{\alpha _{11}}}+{\frac {\sigma _{22}}{\alpha _{22}}}\right)$

and

${\frac {\epsilon _{12}\alpha _{12}\sigma _{12}^{6}}{(\alpha _{12}-6)}}=\left[{\frac {\epsilon _{11}\alpha _{11}\sigma _{11}^{6}}{(\alpha _{11}-6)}}{\frac {\epsilon _{22}\alpha _{22}\sigma _{22}^{6}}{(\alpha _{22}-6)}}\right]^{\frac {1}{2}}$

Other rules for that have been proposed for the Exp-6 potential are the Mason-Rice rules and the Srivastava and Srivastava rules (1956).

## Equations of state

Industrial equations of state have similar mixing and combining rules. These include the van der Waals one-fluid mixing rules

$a_{mix}=\sum _{i}\sum _{j}y_{i}y_{j}a_{ij}$

$b_{mix}=\sum _{i}y_{i}b_{i}$

and the van der Waals combining rule, which introduces a binary interaction parameter $k_{ij}$ ,

$a_{ij}={\sqrt {a_{ii}a_{jj}}}(1-k_{ij})$

.

There is also the Huron-Vidal mixing rule, and the more complex Wong-Sandler mixing rule, which equates excess Helmholtz free energy at infinite pressure between an equation of state and an activity coefficient model (and thus with liquid excess Gibbs free energy).
