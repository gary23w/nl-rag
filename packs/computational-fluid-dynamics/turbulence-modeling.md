---
title: "Turbulence modeling"
source: https://en.wikipedia.org/wiki/Turbulence_modeling
domain: computational-fluid-dynamics
license: CC-BY-SA-4.0
tags: computational fluid dynamics, finite volume method, turbulence modeling, reynolds number
fetched: 2026-07-02
---

# Turbulence modeling

In fluid dynamics, **turbulence modeling** is the construction and use of a mathematical model to predict the effects of turbulence. Turbulent flows are commonplace in most real-life scenarios. In spite of decades of research, there is no analytical theory to predict the evolution of these turbulent flows. The equations governing turbulent flows can only be solved directly for simple cases of flow. For most real-life turbulent flows, CFD simulations use turbulent models to predict the evolution of turbulence. These turbulence models are simplified constitutive equations that predict the statistical evolution of turbulent flows.

## Closure problem

The Navier–Stokes equations govern the velocity and pressure of a fluid flow. In a turbulent flow, each of these quantities may be decomposed into a mean part and a fluctuating part. Averaging the equations gives the Reynolds-averaged Navier–Stokes (RANS) equations, which govern the mean flow. However, the nonlinearity of the Navier–Stokes equations means that the velocity fluctuations still appear in the RANS equations, in the nonlinear term $-\rho {\overline {v_{i}^{\prime }v_{j}^{\prime }}}$ from the convective acceleration. This term is known as the Reynolds stress, $R_{ij}$ . Its effect on the mean flow is like that of a stress term, such as from pressure or viscosity.

To obtain equations containing only the mean velocity and pressure, we need to close the RANS equations by modelling the Reynolds stress term $R_{ij}$ as a function of the mean flow, removing any reference to the fluctuating part of the velocity. This is the *closure problem*.

## Eddy viscosity

Joseph Valentin Boussinesq was the first to attack the closure problem, by introducing the concept of eddy viscosity. In 1877 Boussinesq proposed relating the turbulence stresses to the mean flow to close the system of equations. Here the Boussinesq hypothesis is applied to model the Reynolds stress term. Note that a new proportionality constant $\nu _{t}>0$ , the *(kinematic) turbulence eddy viscosity*, has been introduced. Models of this type are known as eddy viscosity models (EVMs).

$-{\overline {v_{i}^{\prime }v_{j}^{\prime }}}=\nu _{t}\left({\frac {\partial {\overline {v_{i}}}}{\partial x_{j}}}+{\frac {\partial {\overline {v_{j}}}}{\partial x_{i}}}\right)-{\frac {2}{3}}k\delta _{ij}$ which can be written in shorthand as $-{\overline {v_{i}^{\prime }v_{j}^{\prime }}}=2\nu _{t}S_{ij}-{\tfrac {2}{3}}k\delta _{ij}$ where

- $S_{ij}$ is the mean rate of strain tensor
- $\nu _{t}$ is the (kinematic) turbulence eddy viscosity
- $k={\tfrac {1}{2}}{\overline {v_{i}'v_{i}'}}$ is the turbulence kinetic energy
- and $\delta _{ij}$ is the Kronecker delta.

In this model, the additional turbulence stresses are given by augmenting the molecular viscosity with an eddy viscosity. This can be a simple constant eddy viscosity (which works well for some free shear flows such as axisymmetric jets, 2-D jets, and mixing layers).

The Boussinesq hypothesis – although not explicitly stated by Boussinesq at the time – effectively consists of the assumption that the Reynolds stress tensor is aligned with the strain tensor of the mean flow (i.e.: that the shear stresses due to turbulence act in the same direction as the shear stresses produced by the averaged flow). It has since been found to be significantly less accurate than most practitioners would assume. Still, turbulence models which employ the Boussinesq hypothesis have demonstrated significant practical value. In cases with well-defined shear layers, this is likely due the dominance of streamwise shear components, so that considerable *relative* errors in flow-normal components are still negligible in *absolute* terms. Beyond this, most eddy viscosity turbulence models contain coefficients which are calibrated against measurements, and thus produce reasonably accurate overall outcomes for flow fields of similar type as used for calibration.

## Prandtl's mixing-length concept

Later, Ludwig Prandtl introduced the additional concept of the mixing length, along with the idea of a boundary layer. For wall-bounded turbulent flows, the eddy viscosity must vary with distance from the wall, hence the addition of the concept of a 'mixing length'. In the simplest wall-bounded flow model, the eddy viscosity is given by the equation: $\nu _{t}=\left|{\frac {\partial u}{\partial y}}\right|l_{m}^{2}$ where

- ${\frac {\partial u}{\partial y}}$ is the partial derivative of the streamwise velocity (u) with respect to the wall normal direction (y)
- $l_{m}$ is the mixing length.

This simple model is the basis for the "law of the wall", which is a surprisingly accurate model for wall-bounded, attached (not separated) flow fields with small pressure gradients.

More general turbulence models have evolved over time, with most modern turbulence models given by field equations similar to the Navier–Stokes equations.

## Smagorinsky model for the sub-grid scale eddy viscosity

Joseph Smagorinsky was the first who proposed a formula for the eddy viscosity in Large Eddy Simulation models, based on the local derivatives of the velocity field and the local grid size:

$\nu _{t}=\Delta x\Delta y{\sqrt {\left({\frac {\partial u}{\partial x}}\right)^{2}+\left({\frac {\partial v}{\partial y}}\right)^{2}+{\frac {1}{2}}\left({\frac {\partial u}{\partial y}}+{\frac {\partial v}{\partial x}}\right)^{2}}}$

In the context of Large Eddy Simulation, turbulence modeling refers to the need to parameterize the subgrid scale stress in terms of features of the filtered velocity field. This field is called subgrid-scale modeling.

## Spalart–Allmaras, *k*–ε and *k*–ω models

The Boussinesq hypothesis is employed in the Spalart–Allmaras (S–A), *k*–ε (*k*–epsilon), and *k*–ω (*k*–omega) models and offers a relatively low cost computation for the turbulence viscosity $\nu _{t}$ . The S–A model uses only one additional equation to model turbulence viscosity transport, while the *k*–ε and *k*–ω models use two.

## Common models

The following is a brief overview of commonly employed models in modern engineering applications.

- Spalart–Allmaras (S–A) The Spalart–Allmaras model is a one-equation model that solves a modelled transport equation for the kinematic eddy turbulent viscosity. The Spalart–Allmaras model was designed specifically for aerospace applications involving wall-bounded flows and has been shown to give good results for boundary layers subjected to adverse pressure gradients. It is also gaining popularity in turbomachinery applications.
- *k*–ε (*k*–epsilon) K-epsilon (k-ε) turbulence model is the most common model used in computational fluid dynamics (CFD) to simulate mean flow characteristics for turbulent flow conditions. It is a two-equation model which gives a general description of turbulence by means of two transport equations (PDEs). The original impetus for the K-epsilon model was to improve the mixing-length model, as well as to find an alternative to algebraically prescribing turbulent length scales in moderate to high complexity flows.
- *k*–ω (*k*–omega) In computational fluid dynamics, the k–omega (k–ω) turbulence model is a common two-equation turbulence model that is used as a closure for the Reynolds-averaged Navier–Stokes equations (RANS equations). The model attempts to predict turbulence by two partial differential equations for two variables, k and ω, with the first variable being the turbulence kinetic energy (k) while the second (ω) is the specific rate of dissipation (of the turbulence kinetic energy k into internal thermal energy).
- SST (Menter’s Shear Stress Transport) SST (Menter's shear stress transport) turbulence model is a widely used and robust two-equation eddy-viscosity turbulence model used in computational fluid dynamics. The model combines the k-omega turbulence model and K-epsilon turbulence model such that the k-omega is used in the inner region of the boundary layer and switches to the k-epsilon in the free shear flow.
- Reynolds stress equation model The Reynolds stress equation model (RSM), also referred to as second moment closure model, is the most complete classical turbulence modelling approach. Popular eddy-viscosity based models like the *k*–ε (*k*–epsilon) model and the *k*–ω (*k*–omega) models have significant shortcomings in complex engineering flows. This arises due to the use of the eddy-viscosity hypothesis in their formulation. For instance, in flows with high degrees of anisotropy, significant streamline curvature, flow separation, zones of recirculating flow or flows influenced by rotational effects, the performance of such models is unsatisfactory. In such flows, Reynolds stress equation models offer much better accuracy. Eddy viscosity based closures cannot account for the return to isotropy of turbulence, observed in decaying turbulent flows. Eddy-viscosity based models cannot replicate the behaviour of turbulent flows in the Rapid Distortion limit, where the turbulent flow essentially behaves like an elastic medium.
