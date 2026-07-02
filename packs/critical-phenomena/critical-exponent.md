---
title: "Critical exponent"
source: https://en.wikipedia.org/wiki/Critical_exponent
domain: critical-phenomena
license: CC-BY-SA-4.0
tags: critical phenomena, critical exponent, renormalization group, ising model
fetched: 2026-07-02
---

# Critical exponent

**Critical exponents** describe the behavior of physical quantities near continuous phase transitions. It is believed, though not proven, that they are universal, i.e. they do not depend on the details of the physical system, but only on some of its general features. For instance, for ferromagnetic systems at thermal equilibrium, the critical exponents depend only on:

- the dimension of the system
- the range of the interaction
- the spin dimension

These properties of critical exponents are supported by experimental data. Analytical results can be theoretically achieved in mean field theory in high dimensions or when exact solutions are known such as the two-dimensional Ising model. The theoretical treatment in generic dimensions requires the renormalization group approach or, for systems at thermal equilibrium, the conformal bootstrap techniques. Phase transitions and critical exponents appear in many physical systems such as water at the critical point, in magnetic systems, in superconductivity, in percolation and in turbulent fluids. The critical dimension above which mean field exponents are valid varies with the systems and can even be infinite.

## Definition

The control parameter that drives phase transitions is often temperature but can also be other macroscopic variables like pressure or an external magnetic field. For simplicity, the following discussion works in terms of temperature; the translation to another control parameter is straightforward. The temperature at which the transition occurs is called the critical temperature *T*c. We want to describe the behavior of a physical quantity *f* in terms of a power law around the critical temperature; we introduce the reduced temperature

${\displaystyle \tau$

which is zero at the phase transition, and define the critical exponent k as:

$k\,{\stackrel {\text{def}}{=}}\,\lim _{\tau \to 0}{\frac {\log |f(\tau )|}{\log |\tau |}}$

This results in the power law we were looking for:

$f(\tau )=\tau ^{k}\,,\quad \tau \to 0$

It is important to remember that this represents the asymptotic behavior of the function *f*(*τ*) as *τ* → 0.

More generally one might expect

$f(\tau )=\tau ^{k}\left(1+b\tau ^{k_{1}}+\cdots \right)$

## Main exponents

Let us assume that the system at thermal equilibrium has two different phases characterized by an order parameter *Ψ*, which vanishes at and above *T*c.

Consider the disordered phase (*τ* > 0), ordered phase (*τ* < 0) and critical temperature (*τ* = 0) phases separately. Following the standard convention, the critical exponents related to the ordered phase are primed. It is also another standard convention to use superscript/subscript + (−) for the disordered (ordered) state. In general spontaneous symmetry breaking occurs in the ordered phase.

| *Ψ* | order parameter (e.g. ⁠*ρ* − *ρ*c/*ρ*c⁠ for the liquid–gas critical point, magnetization for the Curie point, etc.) |
|---|---|
| *τ* | reduced temperature minus 1, ⁠*T* − *T*c/*T*c⁠ |
| *f* | specific free energy |
| *C* | specific heat; −*T*⁠∂2*f*/∂*T*2⁠ |
| *J* | source field (e.g. ⁠*P* − *P*c/*P*c⁠ where *P* is the pressure and *P*c the critical pressure for the liquid-gas critical point, reduced chemical potential, the magnetic field *H* for the Curie point) |
| *χ* | the susceptibility, compressibility, etc.; ⁠∂*ψ*/∂*J*⁠ |
| *ξ* | correlation length |
| *d* | the number of spatial dimensions |
| ⟨*ψ*(*x*→) *ψ*(*y*→)⟩ | the correlation function |
| *r* | spatial distance |

The following entries are evaluated at *J* = 0 (except for the *δ* entry)

| Critical exponents for *τ* > 0 (disordered phase) Greek letter   relation   *α* *C* ∝ *τ*−*α* *γ* *χ* ∝ *τ*−*γ* *ν* *ξ* ∝ *τ*−*ν* | Critical exponents for *τ* < 0 (ordered phase) Greek letter relation *α*′ *C* ∝ (−*τ*)−*α*′ *β* *Ψ* ∝ (−*τ*)*β* *γ*′ *χ* ∝ (−*τ*)−*γ*′ *ν*′ *ξ* ∝ (−*τ*)−*ν*′ | Critical exponents for *τ* = 0 Greek letter relation *δ* *J* ∝ *Ψ**δ* *η* ⟨*ψ*(0) *ψ*(*r*)⟩ ∝ *r*−*d* + 2 − *η* |
|---|---|---|

The critical exponents can be derived from the specific free energy *f*(*J*,*T*) as a function of the source and temperature. The correlation length can be derived from the functional *F*[*J*;*T*]. In many cases, the critical exponents defined in the ordered and disordered phases are identical.

When the upper critical dimension is four, these relations are accurate close to the critical point in two- and three-dimensional systems. In four dimensions, however, the power laws are modified by logarithmic factors. These do not appear in dimensions arbitrarily close to but not exactly four, which can be used as a way around this problem.

## Mean field critical exponents of Ising-like systems

The classical Landau theory (also known as mean field theory) values of the critical exponents for a scalar field (of which the Ising model is the prototypical example) are given by

$\alpha =\alpha ^{\prime }=0\,,\quad \beta ={\tfrac {1}{2}}\,,\quad \gamma =\gamma ^{\prime }=1\,,\quad \delta =3$

If we add derivative terms turning it into a mean field Ginzburg–Landau theory, we get

$\eta =0\,,\quad \nu ={\tfrac {1}{2}}$

One of the major discoveries in the study of critical phenomena is that mean field theory of critical points is only correct when the space dimension of the system is higher than a certain dimension called the upper critical dimension which excludes the physical dimensions 1, 2 or 3 in most cases. The problem with mean field theory is that the critical exponents do not depend on the space dimension. This leads to a quantitative discrepancy below the critical dimensions, where the true critical exponents differ from the mean field values. It can even lead to a qualitative discrepancy at low space dimension, where a critical point in fact can no longer exist, even though mean field theory still predicts there is one. This is the case for the Ising model in dimension 1 where there is no phase transition. The space dimension where mean field theory becomes qualitatively incorrect is called the lower critical dimension.

## Experimental values

The most accurately measured value of *α* is −0.0127(3) for the phase transition of superfluid helium (the so-called lambda transition). The value was measured on a space shuttle to minimize pressure differences in the sample. This value is in a significant disagreement with the most precise theoretical determinations coming from high temperature expansion techniques, Monte Carlo methods and the conformal bootstrap.

Unsolved problem in physics

Explain the discrepancy between the experimental and theoretical determinations of the heat capacity critical exponent

α

for the

superfluid transition in Helium-4

.

More unsolved problems in physics

## Theoretical predictions

Critical exponents can be evaluated via Monte Carlo methods of lattice models. The accuracy of this first principle method depends on the available computational resources, which determine the ability to go to the infinite volume limit and to reduce statistical errors. Other techniques rely on theoretical understanding of critical fluctuations. The most widely applicable technique is the renormalization group. The conformal bootstrap is a more recently developed technique, which has achieved unsurpassed accuracy for the Ising critical exponents.

## Scaling functions

In light of the critical scalings, we can reexpress all thermodynamic quantities in terms of dimensionless quantities. Close enough to the critical point, everything can be reexpressed in terms of certain ratios of the powers of the reduced quantities. These are the scaling functions.

The origin of scaling functions can be seen from the renormalization group. The critical point is an infrared fixed point. In a sufficiently small neighborhood of the critical point, we may linearize the action of the renormalization group. This basically means that rescaling the system by a factor of *a* will be equivalent to rescaling operators and source fields by a factor of *a**Δ* for some *Δ*. So, we may reparameterize all quantities in terms of rescaled scale independent quantities.

## Scaling relations

It was believed for a long time that the critical exponents were the same above and below the critical temperature, e.g. *α* ≡ *α*′ or *γ* ≡ *γ*′. It has now been shown that this is not necessarily true: When a continuous symmetry is explicitly broken down to a discrete symmetry by irrelevant (in the renormalization group sense) anisotropies, then the exponents *γ* and *γ*′ are not identical.

Critical exponents are denoted by Greek letters. They fall into universality classes and obey the scaling and hyperscaling relations

${\begin{aligned}\nu d&=2-\alpha =2\beta +\gamma =\beta (\delta +1)=\gamma {\frac {\delta +1}{\delta -1}}\\2-\eta &={\frac {\gamma }{\nu }}=d{\frac {\delta -1}{\delta +1}}\end{aligned}}$

These equations imply that there are only two independent exponents, e.g., *ν* and *η*. All this follows from the theory of the renormalization group.

## Percolation theory

Phase transitions and critical exponents also appear in percolation processes where the concentration of "occupied" sites or links of a lattice are the control parameter of the phase transition (compared to temperature in classical phase transitions in physics). One of the simplest examples is Bernoulli percolation in a two dimensional square lattice. Sites are randomly occupied with probability p . A cluster is defined as a collection of nearest neighbouring occupied sites. For small values of p the occupied sites form only small local clusters. At the percolation threshold $p_{c}\approx 0.5927$ (also called critical probability) a spanning cluster that extends across opposite sites of the system is formed, and we have a second-order phase transition that is characterized by universal critical exponents. For percolation the universality class is different from the Ising universality class. For example, the correlation length critical exponent is $\nu =4/3$ for 2D Bernoulli percolation compared to $\nu =1$ for the 2D Ising model.

## Anisotropy

There are some anisotropic systems where the correlation length is direction dependent.

Directed percolation can be also regarded as anisotropic percolation. In this case the critical exponents are different and the upper critical dimension is 5.

## Multicritical points

More complex behavior may occur at multicritical points, at the border or on intersections of critical manifolds. They can be reached by tuning the value of two or more parameters, such as temperature and pressure.

## Static versus dynamic properties

The above examples exclusively refer to the static properties of a critical system. However dynamic properties of the system may become critical, too. Especially, the characteristic time, *τ*char, of a system diverges as *τ*char ∝ *ξ z*, with a *dynamical exponent* *z*. Moreover, the large *static universality classes* of equivalent models with identical static critical exponents decompose into smaller *dynamical universality classes*, if one demands that also the dynamical exponents are identical.

The equilibrium critical exponents can be computed from conformal field theory.

## Self-organized criticality

Critical exponents also exist for self organized criticality for dissipative systems.
