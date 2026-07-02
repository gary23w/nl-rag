---
title: "Cusp form"
source: https://en.wikipedia.org/wiki/Cusp_form
domain: modular-forms
license: CC-BY-SA-4.0
tags: modular form, modular group, eisenstein series, hecke operator
fetched: 2026-07-02
---

# Cusp form

In number theory, a **cusp form** is a particular kind of modular form with zero constant coefficient in its Fourier series expansion.

## Introduction

A cusp form is distinguished in the case of modular forms for the modular group by the vanishing of the constant coefficient *a*0 in the Fourier series expansion (see *q*-expansion)

$\sum a_{n}q^{n}.$

This Fourier expansion exists as a consequence of the presence in the modular group's action on the upper half-plane via the transformation

$z\mapsto z+1.$

For other groups, there may be some translation through several units, in which case the Fourier expansion is in terms of a different parameter. In all cases, though, the limit as *q* → 0 is the limit in the upper half-plane as the imaginary part of *z* → ∞. Taking the quotient by the modular group, this limit corresponds to a cusp of a modular curve (in the sense of a point added for compactification). So, the definition amounts to saying that a cusp form is a modular form that vanishes at a cusp. In the case of other groups, there may be several cusps, and the definition becomes a modular form vanishing at *all* cusps. This may involve several expansions.

## Dimension

The dimensions of spaces of cusp forms are, in principle, computable via the Riemann–Roch theorem. For example, the Ramanujan tau function *τ*(*n*) arises as the sequence of Fourier coefficients of the cusp form of weight 12 for the modular group, with *a*1 = 1. The space of such forms has dimension 1, which means this definition is possible; and that accounts for the action of Hecke operators on the space being by scalar multiplication (Mordell's proof of Ramanujan's identities). Explicitly it is the **modular discriminant**

$\Delta (z,q),$

which represents (up to a normalizing constant) the discriminant of the cubic on the right side of the Weierstrass equation of an elliptic curve; and the 24-th power of the Dedekind eta function. The Fourier coefficients here are written $\tau (n)$ and called 'Ramanujan's tau function', with the normalization *τ*(1) = 1.

## Petersson inner product

The fact that cusp forms decay at the cusps, rather than merely being holomorphic there as the case with more general modular forms, means that there is an invariant inner product on the cusp forms of weight k , given by $\langle f,g\rangle _{k}=\int _{\Gamma \setminus {\mathcal {H}}}f(z){\overline {g(z)}}y^{k}{\frac {dx\,dy}{y^{2}}}.$ Cuspidality is what is required to make this integral finite.

More generally, the integral remains finite if f is a cusp form and g is a modular form, both of weight k . With respect to this inner product, there is an orthogonal decomposition $M_{k}(\Gamma )=E_{k}(\Gamma )\oplus S_{k}(\Gamma )$ where $M_{k}(\Gamma )$ is the space of modular forms, $S_{k}(\Gamma )$ the space of cusp forms, and $E_{k}(\Gamma )$ is the space of Eisenstein series, all of weight k .

In the larger picture of automorphic forms, the cusp forms are complementary to Eisenstein series, in a *discrete spectrum*/*continuous spectrum*, or *discrete series representation*/*induced representation* distinction typical in different parts of spectral theory. That is, Eisenstein series can be 'designed' to take on given values at cusps. There is a large general theory, depending though on the quite intricate theory of parabolic subgroups, and corresponding cuspidal representations.

Consider $P=MU$ a standard parabolic subgroup of some reductive group G (over $\mathbb {A}$ , the adele ring), an automorphic form $\phi$ on $U(\mathbb {A} )M(k)\backslash G$ is called cuspidal if for all parabolic subgroups $P'$ such that $P_{0}\subset P'\subsetneq P$ we have $\phi _{P'}=0$ , where $P_{0}$ is the standard minimal parabolic subgroup. The notation $\phi _{P}$ for $P=MU$ is defined as $\phi _{P}(g)=\int _{U(k)\backslash U(\mathbb {A} )}\phi (ug)du$ .
