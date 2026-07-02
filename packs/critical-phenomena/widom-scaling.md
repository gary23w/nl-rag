---
title: "Widom scaling"
source: https://en.wikipedia.org/wiki/Widom_scaling
domain: critical-phenomena
license: CC-BY-SA-4.0
tags: critical phenomena, critical exponent, renormalization group, ising model
fetched: 2026-07-02
---

# Widom scaling

**Widom scaling** (after Benjamin Widom) is a hypothesis in statistical mechanics regarding the free energy of a magnetic system near its critical point which leads to the critical exponents becoming no longer independent so that they can be parameterized in terms of two values. The hypothesis can be seen to arise as a natural consequence of the block-spin renormalization procedure, when the block size is chosen to be of the same size as the correlation length.

Widom scaling is an example of universality.

## Definitions

The critical exponents $\alpha ,\alpha ',\beta ,\gamma ,\gamma '$ and $\delta$ are defined in terms of the behaviour of the order parameters and response functions near the critical point as follows

$M(t,0)\simeq (-t)^{\beta }$

, for

$t\uparrow 0$

$M(0,H)\simeq |H|^{1/\delta }\mathrm {sign} (H)$

, for

$H\rightarrow 0$

$\chi _{T}(t,0)\simeq {\begin{cases}(t)^{-\gamma },&{\textrm {for}}\ t\downarrow 0\\(-t)^{-\gamma '},&{\textrm {for}}\ t\uparrow 0\end{cases}}$

$c_{H}(t,0)\simeq {\begin{cases}(t)^{-\alpha }&{\textrm {for}}\ t\downarrow 0\\(-t)^{-\alpha '}&{\textrm {for}}\ t\uparrow 0\end{cases}}$

where

$t\equiv {\frac {T-T_{c}}{T_{c}}}$

measures the temperature relative to the critical point.

Near the critical point, Widom's scaling relation reads

$H(t)\simeq M|M|^{\delta -1}f(t/|M|^{1/\beta })$

.

where f has an expansion

$f(t/|M|^{1/\beta })\approx 1+{\rm {const}}\times (t/|M|^{1/\beta })^{\omega }+\dots$

,

with $\omega$ being Wegner's exponent governing the approach to scaling.

## Derivation

The scaling hypothesis is that near the critical point, the free energy $f(t,H)$ , in d dimensions, can be written as the sum of a slowly varying regular part $f_{r}$ and a singular part $f_{s}$ , with the singular part being a scaling function, i.e., a homogeneous function, so that

$f_{s}(\lambda ^{p}t,\lambda ^{q}H)=\lambda ^{d}f_{s}(t,H)\,$

Then taking the partial derivative with respect to *H* and the form of *M(t,H)* gives

$\lambda ^{q}M(\lambda ^{p}t,\lambda ^{q}H)=\lambda ^{d}M(t,H)\,$

Setting $H=0$ and $\lambda =(-t)^{-1/p}$ in the preceding equation yields

$M(t,0)=(-t)^{\frac {d-q}{p}}M(-1,0),$

for

$t\uparrow 0$

Comparing this with the definition of $\beta$ yields its value,

$\beta ={\frac {d-q}{p}}\equiv {\frac {\nu }{2}}(d-2+\eta ).$

Similarly, putting $t=0$ and $\lambda =H^{-1/q}$ into the scaling relation for *M* yields

$\delta ={\frac {q}{d-q}}\equiv {\frac {d+2-\eta }{d-2+\eta }}.$

Hence

${\frac {q}{p}}={\frac {\nu }{2}}(d+2-\eta ),~{\frac {1}{p}}=\nu .$

Applying the expression for the isothermal susceptibility $\chi _{T}$ in terms of *M* to the scaling relation yields

$\lambda ^{2q}\chi _{T}(\lambda ^{p}t,\lambda ^{q}H)=\lambda ^{d}\chi _{T}(t,H)\,$

Setting *H=0* and $\lambda =(t)^{-1/p}$ for $t\downarrow 0$ (resp. $\lambda =(-t)^{-1/p}$ for $t\uparrow 0$ ) yields

$\gamma =\gamma '={\frac {2q-d}{p}}\,$

Similarly for the expression for specific heat $c_{H}$ in terms of *M* to the scaling relation yields

$\lambda ^{2p}c_{H}(\lambda ^{p}t,\lambda ^{q}H)=\lambda ^{d}c_{H}(t,H)\,$

Taking *H=0* and $\lambda =(t)^{-1/p}$ for $t\downarrow 0$ (or $\lambda =(-t)^{-1/p}$ for $t\uparrow 0)$ yields

$\alpha =\alpha '=2-{\frac {d}{p}}=2-\nu d$

As a consequence of Widom scaling, not all critical exponents are independent but they can be parameterized by two numbers $p,q\in \mathbb {R}$ with the relations expressed as

$\alpha =\alpha '=2-\nu d,$

$\gamma =\gamma '=\beta (\delta -1)=\nu (2-\eta ).$

The relations are experimentally well verified for magnetic systems and fluids.
