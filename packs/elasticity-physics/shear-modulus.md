---
title: "Shear modulus"
source: https://en.wikipedia.org/wiki/Shear_modulus
domain: elasticity-physics
license: CC-BY-SA-4.0
tags: elasticity theory, hooke's law, young's modulus, shear modulus
fetched: 2026-07-02
---

# Shear modulus

In solid mechanics, the **shear modulus** or **modulus of rigidity**, denoted by *G*, or sometimes *S* or *μ*, is a measure of the elastic shear stiffness of a material and is defined as the ratio of shear stress to shear strain: ${\begin{aligned}G&:={\frac {\tau _{xy}}{\gamma _{xy}}}={\frac {\frac {F}{A}}{\frac {\Delta x}{l}}}={\frac {Fl}{A\Delta x}}\\\tau _{xy}&={\frac {F}{A}}\\\gamma _{xy}&={\frac {\Delta x}{l}}\end{aligned}}$ where ${\textstyle \tau _{xy}}$ is the shear stress, ${\textstyle \gamma _{xy}}$ is the shear strain, ${\textstyle F}$ is the force, ${\textstyle A}$ is the area, ${\textstyle \Delta x}$ is the traverse displacement, ${\textstyle l}$ is the initial length or height.

The derived SI unit of shear modulus is the pascal (Pa), although it is usually expressed in gigapascals (GPa) or in thousand pounds per square inch (ksi). Its dimensional form is M1L−1T−2, replacing *force* by *mass* times *acceleration*.

## Explanation

| Material | Typical values for shear modulus (GPa) (at room temperature) |
|---|---|
| Diamond, SC (111) | 478.0 |
| Diamond, SC (100) | 443 |
| Steel | 79.3 |
| Iron | 52.5 |
| Copper | 44.7 |
| Titanium | 41.4 |
| Glass | 26.2 |
| Aluminium | 25.5 |
| Polyethylene | 0.117 |
| Rubber | 0.0006 |
| Granite | 24 |
| Shale | 1.6 |
| Limestone | 24 |
| Chalk | 3.2 |
| Sandstone | 0.4 |
| Wood | 4 |

The shear modulus is one of several quantities for measuring the stiffness of materials. All of them arise in the generalized Hooke's law:

- Young's modulus *E* describes the material's strain response to uniaxial stress in the direction of this stress (like pulling on the ends of a wire or putting a weight on top of a column, with the wire getting longer and the column losing height).
- Poisson's ratio *ν* describes the response in the directions orthogonal to this uniaxial stress (the wire getting thinner and the column thicker).
- The bulk modulus *K* describes the material's response to (uniform) hydrostatic pressure (like the pressure at the bottom of the ocean or a deep swimming pool).
- The **shear modulus** *G* describes the material's response to shear stress (like cutting it with dull scissors).

These moduli are not independent, and for isotropic materials they are connected via the equations $E=2G(1+\nu )=3K(1-2\nu )$

The shear modulus is concerned with the deformation of a solid when it experiences a force perpendicular to one of its surfaces while its opposite face experiences an opposing force (such as friction). In the case of an object shaped like a rectangular prism, it will deform into a parallelepiped. Anisotropic materials such as wood, paper and also essentially all single crystals exhibit differing material response to stress or strain when tested in different directions. In this case, one may need to use the full tensor-expression of the elastic constants, rather than a single scalar value.

One possible definition of a fluid would be a material with zero shear modulus.

## Shear waves

In homogeneous and isotropic solids, there are two kinds of waves, pressure waves and shear waves. The velocity of a shear wave, $(v_{s})$ is controlled by the shear modulus,

$v_{s}={\sqrt {\frac {G}{\rho }}}$

where

G is the shear modulus

$\rho$

is the solid's

density

.

## Shear modulus of metals

The shear modulus of metals is usually observed to decrease with increasing temperature. At high pressures, the shear modulus also appears to increase with the applied pressure. Correlations between the melting temperature, vacancy formation energy, and the shear modulus have been observed in many metals.

Several models exist that attempt to predict the shear modulus of metals (and possibly that of alloys). Shear modulus models that have been used in plastic flow computations include:

1. the Varshni–Chen–Gray model developed by Y. P. Varshni and used in conjunction with the mechanical threshold stress (MTS) plastic flow stress model.
2. the Steinberg–Cochran–Guinan (SCG) shear modulus model developed by M. W. Guinan and D. J. Steinberg and used in conjunction with the Steinberg-Cochran-Guinan-Lund (SCGL) flow stress model.
3. the Nadal–Le Poac (NP) shear modulus model by Marie-Hélène Nadal and Philippe Le Poac that uses Lindemann theory to determine the temperature dependence and the SCG model for pressure dependence of the shear modulus.

### Varshni–Chen–Gray model

The Varshni–Chen–Gray model (sometimes referred to as the Varshni equation) has the form:

$\mu (T)=\mu _{0}-{\frac {D}{\exp(T_{0}/T)-1}}$

where $\mu _{0}$ is the shear modulus at $T=0K$ , and D and $T_{0}$ are material constants.

### SCG model

The Steinberg–Cochran–Guinan (SCG) shear modulus model is pressure dependent and has the form

$\mu (p,T)=\mu _{0}+{\frac {\partial \mu }{\partial p}}{\frac {p}{\eta ^{\frac {1}{3}}}}+{\frac {\partial \mu }{\partial T}}(T-300);\quad \eta :={\frac {\rho }{\rho _{0}}}$

where, μ0 is the shear modulus at the reference state (*T* = 300 K, *p* = 0, η = 1), *p* is the pressure, and *T* is the temperature.

### NP model

The Nadal–Le Poac (NP) shear modulus model is a modified version of the SCG model. The empirical temperature dependence of the shear modulus in the SCG model is replaced with an equation based on Lindemann melting theory. The NP shear modulus model has the form:

$\mu (p,T)={\frac {1}{{\mathcal {J}}\left({\hat {T}}\right)}}\left[\left(\mu _{0}+{\frac {\partial \mu }{\partial p}}{\frac {p}{\eta ^{\frac {1}{3}}}}\right)\left(1-{\hat {T}}\right)+{\frac {\rho }{Cm}}~T\right];\quad C:={\frac {\left(6\pi ^{2}\right)^{\frac {2}{3}}}{3}}f^{2}$

where

${\mathcal {J}}({\hat {T}}):=1+\exp \left[-{\frac {1+1/\zeta }{1+\zeta /\left(1-{\hat {T}}\right)}}\right]\quad {\text{for}}\quad {\hat {T}}:={\frac {T}{T_{m}}}\in [0,6+\zeta ],$

and μ0 is the shear modulus at absolute zero and ambient pressure, ζ is an area, *m* is the atomic mass, and *f* is the Lindemann constant.

## Shear relaxation modulus

The **shear relaxation modulus** $G(t)$ is the time-dependent generalization of the shear modulus G :

$G=\lim _{t\to \infty }G(t)$

.
