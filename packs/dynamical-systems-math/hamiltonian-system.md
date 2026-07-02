---
title: "Hamiltonian system"
source: https://en.wikipedia.org/wiki/Hamiltonian_system
domain: dynamical-systems-math
license: CC-BY-SA-4.0
tags: dynamical system, phase space, bifurcation theory, lyapunov stability
fetched: 2026-07-02
---

# Hamiltonian system

A **Hamiltonian system** is a dynamical system governed by Hamilton's equations. In physics, this dynamical system describes the evolution of a physical system such as a planetary system or an electron in an electromagnetic field. These systems can be studied in both Hamiltonian mechanics and dynamical systems theory.

## Overview

Informally, a Hamiltonian system is a mathematical formalism developed by William Rowan Hamilton to describe the evolution equations of a physical system. The advantage of this description is that it gives important insights into the dynamics, even if the initial value problem cannot be solved analytically. One example is the planetary movement of three bodies: while there is no closed-form solution to the general problem, Henri Poincaré showed for the first time that it exhibits deterministic chaos.

Formally, a Hamiltonian system is a dynamical system characterised by the scalar function $H({\boldsymbol {q}},{\boldsymbol {p}},t)$ , also known as the Hamiltonian. The state of the system, ${\boldsymbol {r}}$ , is described by the generalized coordinates ${\boldsymbol {p}}$ and ${\boldsymbol {q}}$ , corresponding to generalized momentum and position respectively. Both ${\boldsymbol {p}}$ and ${\boldsymbol {q}}$ are real-valued vectors with the same dimension *N*. Thus, the state is completely described by the 2*N*-dimensional vector

${\boldsymbol {r}}=({\boldsymbol {q}},{\boldsymbol {p}})$

and the evolution equations are given by Hamilton's equations:

${\begin{aligned}&{\frac {d{\boldsymbol {p}}}{dt}}=-{\frac {\partial H}{\partial {\boldsymbol {q}}}},\\[5pt]&{\frac {d{\boldsymbol {q}}}{dt}}=+{\frac {\partial H}{\partial {\boldsymbol {p}}}}.\end{aligned}}$

The trajectory ${\boldsymbol {r}}(t)$ is the solution of the initial value problem defined by Hamilton's equations and the initial condition ${\boldsymbol {r}}(t=0)={\boldsymbol {r}}_{0}\in \mathbb {R} ^{2N}$ .

## Time-independent Hamiltonian systems

If the Hamiltonian is not explicitly time-dependent, i.e. if $H({\boldsymbol {q}},{\boldsymbol {p}},t)=H({\boldsymbol {q}},{\boldsymbol {p}})$ , then the Hamiltonian does not vary with time at all:

| derivation ${\frac {dH}{dt}}={\frac {\partial H}{\partial {\boldsymbol {p}}}}\cdot {\frac {d{\boldsymbol {p}}}{dt}}+{\frac {\partial H}{\partial {\boldsymbol {q}}}}\cdot {\frac {d{\boldsymbol {q}}}{dt}}+{\frac {\partial H}{\partial t}}$ ${\frac {dH}{dt}}={\frac {\partial H}{\partial {\boldsymbol {p}}}}\cdot \left(-{\frac {\partial H}{\partial {\boldsymbol {q}}}}\right)+{\frac {\partial H}{\partial {\boldsymbol {q}}}}\cdot {\frac {\partial H}{\partial {\boldsymbol {p}}}}+0=0$ |
|---|

and thus the Hamiltonian is a constant of motion, whose constant equals the total energy of the system: $H=E$ . Examples of such systems are the undamped pendulum, the harmonic oscillator, and dynamical billiards.

### Example

An example of a time-independent Hamiltonian system is the harmonic oscillator. Consider the system defined by the coordinates ${\boldsymbol {p}}=m{\dot {x}}$ and ${\boldsymbol {q}}=x$ . Then the Hamiltonian is given by

$H={\frac {p^{2}}{2m}}+{\frac {kq^{2}}{2}}.$

The Hamiltonian of this system does not depend on time and thus the energy of the system is conserved.

## Symplectic structure

One important property of a Hamiltonian dynamical system is that it has a symplectic structure. Writing

$\nabla _{\boldsymbol {r}}H({\boldsymbol {r}})={\begin{bmatrix}{\frac {\partial H({\boldsymbol {q}},{\boldsymbol {p}})}{\partial {\boldsymbol {q}}}}\\{\frac {\partial H({\boldsymbol {q}},{\boldsymbol {p}})}{\partial {\boldsymbol {p}}}}\\\end{bmatrix}}$

the evolution equation of the dynamical system can be written as

${\frac {d{\boldsymbol {r}}}{dt}}=M_{N}\nabla _{\boldsymbol {r}}H({\boldsymbol {r}})$

where

$M_{N}={\begin{bmatrix}0&I_{N}\\-I_{N}&0\\\end{bmatrix}}$

and *I**N* is the *N*×*N* identity matrix.

One important consequence of this property is that an infinitesimal phase-space volume is preserved. A corollary of this is Liouville's theorem, which states that on a Hamiltonian system, the phase-space volume of a closed surface is preserved under time evolution.

${\begin{aligned}{\frac {d}{dt}}\oint _{\partial V}d{\boldsymbol {r}}&=\oint _{\partial V}{\frac {d{\boldsymbol {r}}}{dt}}\cdot d{\hat {\boldsymbol {n}}}_{\partial V}\\&=\oint _{\partial V}\left(M_{N}\nabla _{\boldsymbol {r}}H({\boldsymbol {r}})\right)\cdot d{\hat {\boldsymbol {n}}}_{\partial V}\\&=\int _{V}\nabla _{\boldsymbol {r}}\cdot \left(M_{N}\nabla _{\boldsymbol {r}}H({\boldsymbol {r}})\right)\,dV\\&=\int _{V}\sum _{i=1}^{N}\sum _{j=1}^{N}\left({\frac {\partial ^{2}H}{\partial q_{i}\partial p_{j}}}-{\frac {\partial ^{2}H}{\partial p_{i}\partial q_{j}}}\right)\,dV\\&=0\end{aligned}}$

where the third equality comes from the divergence theorem.

## Hamiltonian chaos

Certain Hamiltonian systems exhibit chaotic behavior. When the evolution of a Hamiltonian system is highly sensitive to initial conditions, and the motion appears random and erratic, the system is said to exhibit Hamiltonian chaos.

### Origins

The concept of chaos in Hamiltonian systems has its roots in the works of Henri Poincaré, who in the late 19th century made pioneering contributions to the understanding of the three-body problem in celestial mechanics. Poincaré showed that even a simple gravitational system of three bodies could exhibit complex behavior that could not be predicted over the long term. His work is considered to be one of the earliest explorations of chaotic behavior in physical systems.

### Characteristics

Hamiltonian chaos is characterized by the following features:

**Sensitivity to Initial Conditions**: A hallmark of chaotic systems, small differences in initial conditions can lead to vastly different trajectories. This is known as the butterfly effect.

**Mixing**: Over time, the phases of the system become uniformly distributed in phase space.

**Recurrence**: Though unpredictable, the system eventually revisits states that are arbitrarily close to its initial state, known as Poincaré recurrence.

Hamiltonian chaos is also associated with the presence of *chaotic invariants* such as the Lyapunov exponent and Kolmogorov–Sinai entropy, which quantify the rate at which nearby trajectories diverge and the complexity of the system, respectively.

### Applications

Hamiltonian chaos is prevalent in many areas of physics, particularly in classical mechanics and statistical mechanics. For instance, in plasma physics, the behavior of charged particles in a magnetic field can exhibit Hamiltonian chaos, which has implications for nuclear fusion and astrophysical plasmas. Moreover, in quantum mechanics, Hamiltonian chaos is studied through quantum chaos, which seeks to understand the quantum analogs of classical chaotic behavior. Hamiltonian chaos also plays a role in astrophysics, where it is used to study the dynamics of star clusters and the stability of galactic structures.

## Examples

- Dynamical billiards
- Planetary systems, more specifically, the n-body problem.
- Canonical general relativity
