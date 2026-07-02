---
title: "Kolmogorov microscales"
source: https://en.wikipedia.org/wiki/Kolmogorov_microscales
domain: fluid-turbulence
license: CC-BY-SA-4.0
tags: fluid turbulence, turbulence modeling, large eddy simulation, direct numerical simulation
fetched: 2026-07-02
---

# Kolmogorov microscales

In fluid dynamics, **Kolmogorov microscales** are the smallest scales in turbulent flow. At the Kolmogorov scale, viscosity dominates and the turbulence kinetic energy is dissipated into thermal energy. They are defined by

| Kolmogorov length scale | $\eta =\left({\frac {\nu ^{3}}{\varepsilon }}\right)^{1/4}$ |
|---|---|
| Kolmogorov time scale | $\tau _{\eta }={\sqrt {\frac {\nu }{\varepsilon }}}$ |
| Kolmogorov velocity scale | $u_{\eta }=\left(\nu \varepsilon \right)^{1/4}$ |

where

- ε is the average rate of dissipation of turbulence kinetic energy per unit mass, and
- ν is the kinematic viscosity of the fluid.

Typical values of the Kolmogorov length scale, for atmospheric motion in which the large eddies have length scales on the order of kilometers, range from 0.1 to 10 millimeters; for smaller flows such as in laboratory systems, η may be much smaller.

In 1941, Andrey Kolmogorov introduced the hypothesis that the smallest scales of turbulence are universal (similar for every turbulent flow) and that they depend only on ε and ν. The definitions of the Kolmogorov microscales can be obtained using this idea and dimensional analysis. Since the dimension of kinematic viscosity is length2/time, and the dimension of the energy dissipation rate per unit mass is length2/time3, the only combination that has the dimension of time is $\tau _{\eta }={\sqrt {\tfrac {\nu }{\varepsilon }}}$ which is the Kolmogorov time scale. Similarly, the Kolmogorov length scale is the only combination of ε and ν that has dimension of length.

Alternatively, the definition of the Kolmogorov time scale can be obtained from the inverse of the mean square strain rate tensor, $\tau _{\eta }={\tfrac {1}{\sqrt {2\langle E_{ij}E_{ij}\rangle }}},$ which also gives $\tau _{\eta }={\sqrt {\tfrac {\nu }{\varepsilon }}}$ using the definition of the energy dissipation rate per unit mass $\varepsilon =2\nu \langle E_{ij}E_{ij}\rangle .$ Then the Kolmogorov length scale can be obtained as the scale at which the Reynolds number (Re) is equal to 1,

$\mathrm {Re} ={\frac {UL}{\nu }}={\frac {(\eta /\tau _{\eta })\eta }{\nu }}=1.$

Kolmogorov's 1941 theory is a mean field theory since it assumes that the relevant dynamical parameter is the mean energy dissipation rate. In fluid turbulence, the energy dissipation rate fluctuates in space and time, so it is possible to think of the microscales as quantities that also vary in space and time. However, standard practice is to use mean field values since they represent the typical values of the smallest scales in a given flow. In 1961, Kolomogorov published a refined version of the similarity hypotheses that accounts for the log-normal distribution of the dissipation rate.
