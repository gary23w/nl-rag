---
title: "Post-Newtonian expansion"
source: https://en.wikipedia.org/wiki/Post-Newtonian_expansion
domain: general-relativity-numerics
license: CC-BY-SA-4.0
tags: numerical relativity, einstein field equations, adm formalism, gravitational wave modeling
fetched: 2026-07-02
---

# Post-Newtonian expansion

In general relativity, **post-Newtonian expansions** (**PN** **expansions**) are used for finding an approximate solution of Einstein field equations for the metric tensor. The approximations are expanded in small parameters that express orders of deviations from Newton's law of universal gravitation. This allows approximations to Einstein's equations to be made in the case of weak fields. Higher-order terms can be added to increase accuracy, but for strong fields sometimes it is preferable to solve the complete equations numerically. This method is a common mark of effective field theories. In the limit, when the small parameters are equal to 0, the post-Newtonian expansion reduces to Newton's law of gravity.

## Applicable range

The post-Newtonian methods require both low speed masses and weak gravitational fields. These requirements are fully met in all solar-system tests of general relativity. The high velocities that generate gravitational radiation or the large fields between binary compact objects like pairs of black holes are not adequately modeled by post-Newtonian expansion. Cosmological models are based on different physical assumptions and do not benefit from this approximation method.

## Expansion in 1/*c*2

The **post-Newtonian approximations** are expansions in a small parameter, which is the ratio of the velocity of the matter that creates the gravitational field, to the speed of light, which in this case is more precisely called the *speed of gravity*. In the limit, when the fundamental speed of gravity becomes infinite, the post-Newtonian expansion reduces to Newton's law of gravity. A systematic study of post-Newtonian expansions within hydrodynamic approximations was developed by Subrahmanyan Chandrasekhar and his colleagues in the 1960s.

## Expansion in *h*

Another approach is to expand the equations of general relativity in a power series in the deviation of the metric from its value in the absence of gravity.

$h_{\alpha \beta }=g_{\alpha \beta }-\eta _{\alpha \beta }\,.$

To this end, one must choose a coordinate system in which the eigenvalues of $h_{\alpha \beta }\eta ^{\beta \gamma }\,$ all have absolute values less than 1.

For example, if one goes one step beyond linearized gravity to get the expansion to the second order in *h*:

$g^{\mu \nu }\approx \eta ^{\mu \nu }-\eta ^{\mu \alpha }h_{\alpha \beta }\eta ^{\beta \nu }+\eta ^{\mu \alpha }h_{\alpha \beta }\eta ^{\beta \gamma }h_{\gamma \delta }\eta ^{\delta \nu }\,.$

${\sqrt {-g}}\approx 1+{\tfrac {1}{2}}h_{\alpha \beta }\eta ^{\beta \alpha }+{\tfrac {1}{8}}h_{\alpha \beta }\eta ^{\beta \alpha }h_{\gamma \delta }\eta ^{\delta \gamma }-{\tfrac {1}{4}}h_{\alpha \beta }\eta ^{\beta \gamma }h_{\gamma \delta }\eta ^{\delta \alpha }\,.$

Expansions based only on the metric, independently from the speed, are called post-Minkowskian expansions (PM expansions).

0PN

1PN

2PN

3PN

4PN

5PN

6PN

7PN

1PM

( 1

+

$v^{2}$

+

$v^{4}$

+

$v^{6}$

+

$v^{8}$

+

$v^{10}$

+

$v^{12}$

+

$v^{14}$

+

...)

$G^{1}$

2PM

( 1

+

$v^{2}$

+

$v^{4}$

+

$v^{6}$

+

$v^{8}$

+

$v^{10}$

+

$v^{12}$

+

...)

$G^{2}$

3PM

( 1

+

$v^{2}$

+

$v^{4}$

+

$v^{6}$

+

$v^{8}$

+

$v^{10}$

+

...)

$G^{3}$

4PM

( 1

+

$v^{2}$

+

$v^{4}$

+

$v^{6}$

+

$v^{8}$

+

...)

$G^{4}$

5PM

( 1

+

$v^{2}$

+

$v^{4}$

+

$v^{6}$

+

...)

$G^{5}$

6PM

( 1

+

$v^{2}$

+

$v^{4}$

+

...)

$G^{6}$

Comparison table of powers used for PN and PM approximations in the case of two non-rotating bodies.

0PN corresponds to the case of Newton's theory of gravitation. 0PM (not shown) corresponds to the Minkowski flat space.

## Uses

The first use of a PN expansion (to first order) was made by Albert Einstein in calculating the perihelion precession of Mercury's orbit. Today, Einstein's calculation is recognized as a common example of applications of PN expansions, solving the general relativistic two-body problem, which includes the emission of gravitational waves.

## Newtonian gauge

In general, the perturbed metric can be written as

$ds^{2}=a^{2}(\tau )\left[(1+2A)d\tau ^{2}-2B_{i}dx^{i}d\tau -\left(\delta _{ij}+h_{ij}\right)dx^{i}dx^{j}\right]$

where A , $B_{i}$ and $h_{ij}$ are functions of space and time. $h_{ij}$ can be decomposed as

$h_{ij}=2C\delta _{ij}+\partial _{i}\partial _{j}E-{\frac {1}{3}}\delta _{ij}\Box ^{2}E+\partial _{i}{\hat {E}}_{j}+\partial _{j}{\hat {E}}_{i}+2{\tilde {E}}_{ij}$

where $\Box$ is the d'Alembert operator, E is a scalar, ${\hat {E}}_{i}$ is a vector and ${\tilde {E}}_{ij}$ is a traceless tensor. Then the Bardeen potentials are defined as

$\Psi \equiv A+H(B-E'),+(B+E')',\quad \Phi \equiv -C-H(B-E')+{\frac {1}{3}}\Box E$

where H is the Hubble constant and a prime represents differentiation with respect to conformal time $\tau \,$ .

Taking $B=E=0$ (i.e. setting $\Phi \equiv -C$ and $\Psi \equiv A$ ), the Newtonian gauge is

$ds^{2}=a^{2}(\tau )\left[(1+2\Psi )d\tau ^{2}-(1-2\Phi )\delta _{ij}dx^{i}dx^{j}\right]\,$

.

Note that in the absence of anisotropic stress, $\Phi =\Psi$ .

A useful non-linear extension of this is provided by the non-relativistic gravitational fields.
