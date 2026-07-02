---
title: "Perturbation (astronomy)"
source: https://en.wikipedia.org/wiki/Perturbation_(astronomy)
domain: celestial-mechanics-physics
license: CC-BY-SA-4.0
tags: celestial mechanics, orbital mechanics, kepler's laws, three-body problem
fetched: 2026-07-02
---

# Perturbation (astronomy)

In astronomy, **perturbation** is the complex motion of a massive body subjected to forces other than the gravitational attraction of a single other massive body. The other forces can include a third (fourth, fifth, etc.) body, resistance, as from an atmosphere, and the off-center attraction of an oblate or otherwise misshapen body.

## Introduction

The study of perturbations began with the first attempts to predict planetary motions in the sky. In ancient times the causes were unknown. Isaac Newton, at the time he formulated his laws of motion and of gravitation, applied them to the first analysis of perturbations, recognizing the complex difficulties of their calculation. Many of the great mathematicians since then have given attention to the various problems involved; throughout the 18th and 19th centuries there was demand for accurate tables of the position of the Moon and planets for marine navigation.

The complex motions of gravitational perturbations can be broken down. The hypothetical motion that the body follows under the gravitational effect of one other body only is a conic section, and can be described in geometrical terms. This is called a two-body problem, or an unperturbed Keplerian orbit. The differences between that and the actual motion of the body are perturbations due to the additional gravitational effects of the remaining body or bodies. If there is only one other significant body then the perturbed motion is a three-body problem; if there are multiple other bodies it is an n‑body problem. A general analytical solution (a mathematical expression to predict the positions and motions at any future time) exists for the two-body problem; when more than two bodies are considered analytic solutions exist only for special cases. Even the two-body problem becomes insoluble if one of the bodies is irregular in shape.

Most systems that involve multiple gravitational attractions present one primary body which is dominant in its effects (for example, a star, in the case of the star and its planet, or a planet, in the case of the planet and its satellite). The gravitational effects of the other bodies can be treated as perturbations of the hypothetical unperturbed motion of the planet or satellite around its primary body.

## Mathematical analysis

### General perturbations

In methods of **general perturbations**, general differential equations, either of motion or of change in the orbital elements, are solved analytically, usually by series expansions. The result is usually expressed in terms of algebraic and trigonometric functions of the orbital elements of the body in question and the perturbing bodies. This can be applied generally to many different sets of conditions, and is not specific to any particular set of gravitating objects. Historically, general perturbations were investigated first. The classical methods are known as *variation of the elements*, *variation of parameters* or *variation of the constants of integration*. In these methods, it is considered that the body is always moving in a conic section, however the conic section is constantly changing due to the perturbations. If all perturbations were to cease at any particular instant, the body would continue in this (now unchanging) conic section indefinitely; this conic is known as the osculating orbit and its orbital elements at any particular time are what are sought by the methods of general perturbations.

General perturbations takes advantage of the fact that in many problems of celestial mechanics, the two-body orbit changes rather slowly due to the perturbations; the two-body orbit is a good first approximation. General perturbations is applicable only if the perturbing forces are about one order of magnitude smaller, or less, than the gravitational force of the primary body. In the Solar System, this is usually the case; Jupiter, the second largest body, has a mass of about ⁠1/ 1000 ⁠ that of the Sun.

General perturbation methods are preferred for some types of problems, as the source of certain observed motions are readily found. This is not necessarily so for special perturbations; the motions would be predicted with similar accuracy, but no information on the configurations of the perturbing bodies (for instance, an orbital resonance) which caused them would be available.

### Special perturbations

In methods of **special perturbations**, numerical datasets, representing values for the positions, velocities and accelerative forces on the bodies of interest, are made the basis of numerical integration of the differential equations of motion. In effect, the positions and velocities are perturbed directly, and no attempt is made to calculate the curves of the orbits or the orbital elements.

Special perturbations can be applied to any problem in celestial mechanics, as it is not limited to cases where the perturbing forces are small. Once applied only to comets and minor planets, special perturbation methods are now the basis of the most accurate machine-generated planetary ephemerides of the great astronomical almanacs. Special perturbations are also used for modeling an orbit with computers.

#### Cowell's formulation

Cowell's formulation (so named for Philip H. Cowell, who, with A.C.D. Cromellin, used a similar method to predict the return of Halley's comet) is perhaps the simplest of the special perturbation methods. In a system of $\ n\$ mutually interacting bodies, this method mathematically solves for the Newtonian forces on body $\ i\$ by summing the individual interactions from the other j bodies:

$\mathbf {\ddot {r}} _{i}=\sum _{\underset {j\neq i}{j=1}}^{n}\ G\ m_{j}{\frac {\ (\mathbf {r} _{j}-\mathbf {r} _{i})\ }{\ \|\mathbf {r} _{j}-\mathbf {r} _{i}\|^{3}}}$

where $\ \mathbf {\ddot {r}} _{i}\$ is the acceleration vector of body i , G is the gravitational constant, $\ m_{j}\$ is the mass of body j , $\ \mathbf {r} _{i}\$ and $\ \mathbf {r} _{j}\$ are the position vectors of objects $\ i\$ and $\ j\$ respectively, and $\ r_{ij}\equiv \|\mathbf {r} _{j}-\mathbf {r} _{i}\|\$ is the distance from object i to object $\ j\$ , all vectors being referred to the barycenter of the system. This equation is resolved into components in $\ x\ ,$ $\ y\ ,$ and $\ z\ ,$ and these are integrated numerically to form the new velocity and position vectors. This process is repeated as many times as necessary. The advantage of Cowell's method is ease of application and programming. A disadvantage is that when perturbations become large in magnitude (as when an object makes a close approach to another) the errors of the method also become large. However, for many problems in celestial mechanics, this is never the case. Another disadvantage is that in systems with a dominant central body, such as the Sun, it is necessary to carry many significant digits in the arithmetic because of the large difference in the forces of the central body and the perturbing bodies, although with high precision numbers built into modern computers this is not as much of a limitation as it once was.

#### Encke's method

Encke's method begins with the osculating orbit as a reference and integrates numerically to solve for the variation from the reference as a function of time. Its advantages are that perturbations are generally small in magnitude, so the integration can proceed in larger steps (with resulting lesser errors), and the method is much less affected by extreme perturbations. Its disadvantage is complexity; it cannot be used indefinitely without occasionally updating the osculating orbit and continuing from there, a process known as *rectification*. Encke's method is similar to the general perturbation method of variation of the elements, except the rectification is performed at discrete intervals rather than continuously.

Letting ${\boldsymbol {\rho }}$ be the radius vector of the osculating orbit, $\mathbf {r}$ the radius vector of the perturbed orbit, and $\delta \mathbf {r}$ the variation from the osculating orbit,

| $\delta \mathbf {r} =\mathbf {r} -{\boldsymbol {\rho }}$ , and the equation of motion of $\delta \mathbf {r}$ is simply |   | 1 |
|---|---|---|

| $\delta {\ddot {\mathbf {r} }}=\mathbf {\ddot {r}} -{\boldsymbol {\ddot {\rho }}}$ . |   | 2 |
|---|---|---|

$\mathbf {\ddot {r}}$ and ${\boldsymbol {\ddot {\rho }}}$ are just the equations of motion of $\mathbf {r}$ and ${\boldsymbol {\rho }},$

| $\mathbf {\ddot {r}} =\mathbf {a} _{\text{per}}-{\mu \over r^{3}}\mathbf {r}$ for the perturbed orbit and |   | 3 |
|---|---|---|

| ${\boldsymbol {\ddot {\rho }}}=-{\mu \over \rho ^{3}}{\boldsymbol {\rho }}$ for the unperturbed orbit, |   | 4 |
|---|---|---|

where $\mu =G(M+m)$ is the gravitational parameter with M and m the masses of the central body and the perturbed body, $\mathbf {a} _{\text{per}}$ is the perturbing acceleration, and r and $\rho$ are the magnitudes of $\mathbf {r}$ and ${\boldsymbol {\rho }}$ .

Substituting from equations (**3**) and (**4**) into equation (**2**),

| $\delta {\ddot {\mathbf {r} }}=\mathbf {a} _{\text{per}}+\mu \left({{\boldsymbol {\rho }} \over \rho ^{3}}-{\mathbf {r} \over r^{3}}\right),$ |   | 5 |
|---|---|---|

which, in theory, could be integrated twice to find $\delta \mathbf {r}$ . Since the osculating orbit is easily calculated by two-body methods, ${\boldsymbol {\rho }}$ and $\delta \mathbf {r}$ are accounted for and $\mathbf {r}$ can be solved. In practice, the quantity in the brackets, ${{\boldsymbol {\rho }} \over \rho ^{3}}-{\mathbf {r} \over r^{3}}$ , is the difference of two nearly equal vectors, and further manipulation is necessary to avoid the need for extra significant digits. Encke's method was more widely used before the advent of modern computers, when much orbit computation was performed on mechanical calculating machines.

## Periodic nature

In the Solar System, many of the disturbances of one planet by another are periodic, consisting of small impulses each time a planet passes another in its orbit. This causes the bodies to follow motions that are periodic or quasi-periodic – such as the Moon in its strongly perturbed orbit, which is the subject of lunar theory. This periodic nature led to the discovery of Neptune in 1846 as a result of its perturbations of the orbit of Uranus.

On-going mutual perturbations of the planets cause long-term quasi-periodic variations in their orbital elements, most apparent when two planets' orbital periods are nearly in sync. For instance, five orbits of Jupiter (59.31 years) is nearly equal to two of Saturn (58.91 years). This causes large perturbations of both, with a period of 918 years, the time required for the small difference in their positions at conjunction to make one complete circle, first discovered by Laplace. Venus currently has the orbit with the least eccentricity, i.e. it is the closest to circular, of all the planetary orbits. In 25,000 years' time, Earth will have a more circular (less eccentric) orbit than Venus. It has been shown that long-term periodic disturbances within the Solar System can become chaotic over very long time scales; under some circumstances one or more planets can cross the orbit of another, leading to collisions.

The orbits of many of the minor bodies of the Solar System, such as comets, are often heavily perturbed, particularly by the gravitational fields of the gas giants. While many of these perturbations are periodic, others are not, and these in particular may represent aspects of chaotic motion. For example, in April 1996, Jupiter's gravitational influence caused the period of Comet Hale–Bopp's orbit to decrease from 4,206 to 2,380 years, a change that will not revert on any periodic basis.
