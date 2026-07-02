---
title: "Large eddy simulation"
source: https://en.wikipedia.org/wiki/Large_eddy_simulation
domain: computational-fluid-dynamics
license: CC-BY-SA-4.0
tags: computational fluid dynamics, finite volume method, turbulence modeling, reynolds number
fetched: 2026-07-02
---

# Large eddy simulation

**Large eddy simulation** (**LES**) is a mathematical model for turbulence used in computational fluid dynamics. It was initially proposed in 1963 by Joseph Smagorinsky to simulate atmospheric air currents, and first explored by Deardorff (1970). LES is currently applied in a wide variety of engineering applications, including combustion, acoustics, and simulations of the atmospheric boundary layer.

The simulation of turbulent flows by numerically solving the Navier–Stokes equations requires resolving a very wide range of time and length scales, all of which affect the flow field. Such a resolution can be achieved with direct numerical simulation (DNS), but DNS is computationally expensive, and its cost prohibits simulation of practical engineering systems with complex geometry or flow configurations, such as turbulent jets, pumps, vehicles, and landing gear.

The principal idea behind LES is to reduce the computational cost by ignoring the smallest length scales, which are the most computationally expensive to resolve, via low-pass filtering of the Navier–Stokes equations. Such a low-pass filtering, which can be viewed as a time- and spatial-averaging, effectively removes small-scale information from the numerical solution. This information is not irrelevant, however, and its effect on the flow field must be modelled, a task which is an active area of research for problems in which small-scales can play an important role, such as near-wall flows, reacting flows, and multiphase flows.

## Filter definition and properties

An LES filter can be applied to a spatial and temporal field $\phi ({\boldsymbol {x}},t)$ and perform a spatial filtering operation, a temporal filtering operation, or both. The filtered field, denoted with a bar, is defined as:

${\overline {\phi ({\boldsymbol {x}},t)}}=\displaystyle {\int _{-\infty }^{\infty }}\int _{-\infty }^{\infty }\phi ({\boldsymbol {r}},\tau )G({\boldsymbol {x}}-{\boldsymbol {r}},t-\tau )d\tau d{\boldsymbol {r}}$

where G is the filter convolution kernel. This can also be written as:

${\overline {\phi }}=G\star \phi .$

The filter kernel G has an associated cutoff length scale $\Delta$ and cutoff time scale $\tau _{c}$ . Scales smaller than these are eliminated from ${\overline {\phi }}$ . Using the above filter definition, any field $\phi$ may be split up into a filtered and sub-filtered (denoted with a prime) portion, as

$\phi ={\bar {\phi }}+\phi ^{\prime }.$

It is important to note that the large eddy simulation filtering operation does not satisfy the properties of a Reynolds operator.

## Filtered governing equations

The governing equations of LES are obtained by filtering the partial differential equations governing the flow field $\rho {\boldsymbol {u}}({\boldsymbol {x}},t)$ . There are differences between the incompressible and compressible LES governing equations, which lead to the definition of a new filtering operation.

### Incompressible flow

For incompressible flow, the continuity equation and Navier–Stokes equations are filtered, yielding the filtered incompressible continuity equation,

${\frac {\partial {\bar {u}}_{i}}{\partial x_{i}}}=0$

and the filtered Navier–Stokes equations,

${\frac {\partial {\bar {u}}_{i}}{\partial t}}+{\frac {\partial }{\partial x_{j}}}\left({\overline {u_{i}u_{j}}}\right)=-{\frac {1}{\rho }}{\frac {\partial {\overline {p}}}{\partial x_{i}}}+\nu {\frac {\partial }{\partial x_{j}}}\left({\frac {\partial {\bar {u}}_{i}}{\partial x_{j}}}+{\frac {\partial {\bar {u}}_{j}}{\partial x_{i}}}\right)=-{\frac {1}{\rho }}{\frac {\partial {\overline {p}}}{\partial x_{i}}}+2\nu {\frac {\partial }{\partial x_{j}}}{\bar {S}}_{ij},$

where ${\bar {p}}$ is the filtered pressure field and ${\bar {S}}_{ij}$ is the rate-of-strain tensor evaluated using the filtered velocity. The nonlinear filtered advection term ${\overline {u_{i}u_{j}}}$ is the chief cause of difficulty in LES modeling. It requires knowledge of the unfiltered velocity field, which is unknown, so it must be modeled. The analysis that follows illustrates the difficulty caused by the nonlinearity, namely, that it causes interaction between large and small scales, preventing separation of scales.

The filtered advection term can be split up, following Leonard (1975), as:

${\overline {u_{i}u_{j}}}=\tau _{ij}+{\overline {u}}_{i}{\overline {u}}_{j}$

where $\tau _{ij}$ is the residual stress tensor, so that the filtered Navier-Stokes equations become

${\frac {\partial {\bar {u}}_{i}}{\partial t}}+{\frac {\partial }{\partial x_{j}}}\left({\overline {u}}_{i}{\overline {u}}_{j}\right)=-{\frac {1}{\rho }}{\frac {\partial {\overline {p}}}{\partial x_{i}}}+2\nu {\frac {\partial }{\partial x_{j}}}{\bar {S}}_{ij}-{\frac {\partial \tau _{ij}}{\partial x_{j}}}$

with the residual stress tensor $\tau _{ij}$ grouping all unclosed terms. Leonard decomposed this stress tensor as $\tau _{ij}=L_{ij}+C_{ij}+R_{ij}$ and provided physical interpretations for each term. $L_{ij}={\overline {{\bar {u}}_{i}{\bar {u}}_{j}}}-{\overline {\bar {u}}}_{i}{\overline {\bar {u}}}_{j}$ , the Leonard tensor, represents interactions among large scales, $R_{ij}={\overline {u_{i}^{\prime }u_{j}^{\prime }}}-{\overline {u_{i}}}^{\prime }{\overline {u_{j}}}^{\prime }$ , the Reynolds stress-like term, represents interactions among the sub-filter scales (SFS), and $C_{ij}={\overline {{\bar {u}}_{i}u_{j}^{\prime }}}+{\overline {{\bar {u}}_{j}u_{i}^{\prime }}}-{\overline {\bar {u}}}_{i}{\overline {u_{j}^{\prime }}}-{\overline {\bar {u}}}_{j}{\overline {u_{i}^{\prime }}}$ , the Clark tensor, represents cross-scale interactions between large and small scales. Modeling the unclosed term $\tau _{ij}$ is the task of sub-grid scale (SGS) models. This is made challenging by the fact that the subgrid stress tensor $\tau _{ij}$ must account for interactions among all scales, including filtered scales with unfiltered scales.

The filtered governing equation for a passive scalar $\phi$ , such as mixture fraction or temperature, can be written as

${\frac {\partial {\overline {\phi }}}{\partial t}}+{\frac {\partial }{\partial x_{j}}}\left({\overline {u}}_{j}{\overline {\phi }}\right)={\frac {\partial {\overline {J_{\phi }}}}{\partial x_{j}}}+{\frac {\partial q_{j}}{\partial x_{j}}}$

where $J_{\phi }$ is the diffusive flux of $\phi$ , and $q_{j}$ is the sub-filter flux for the scalar $\phi$ . The filtered diffusive flux ${\overline {J_{\phi }}}$ is unclosed, unless a particular form is assumed for it, such as a gradient diffusion model $J_{\phi }=D_{\phi }{\frac {\partial \phi }{\partial x_{i}}}$ . $q_{j}$ is defined analogously to $\tau _{ij}$ ,

$q_{j}={\bar {\phi }}{\overline {u}}_{j}-{\overline {\phi u_{j}}}$

and can similarly be split up into contributions from interactions between various scales. This sub-filter flux also requires a sub-filter model.

#### Derivation

Using Einstein notation, the Navier–Stokes equations for an incompressible fluid in Cartesian coordinates are

${\frac {\partial u_{i}}{\partial x_{i}}}=0$

${\frac {\partial u_{i}}{\partial t}}+{\frac {\partial u_{i}u_{j}}{\partial x_{j}}}=-{\frac {1}{\rho }}{\frac {\partial p}{\partial x_{i}}}+\nu {\frac {\partial ^{2}u_{i}}{\partial x_{j}\partial x_{j}}}.$

Filtering the momentum equation results in

${\overline {\frac {\partial u_{i}}{\partial t}}}+{\overline {\frac {\partial u_{i}u_{j}}{\partial x_{j}}}}=-{\overline {{\frac {1}{\rho }}{\frac {\partial p}{\partial x_{i}}}}}+{\overline {\nu {\frac {\partial ^{2}u_{i}}{\partial x_{j}\partial x_{j}}}}}.$

If we assume that filtering and differentiation commute, then

${\frac {\partial {\bar {u}}_{i}}{\partial t}}+{\overline {\frac {\partial u_{i}u_{j}}{\partial x_{j}}}}=-{\frac {1}{\rho }}{\frac {\partial {\bar {p}}}{\partial x_{i}}}+\nu {\frac {\partial ^{2}{\bar {u}}_{i}}{\partial x_{j}\partial x_{j}}}.$

This equation models the changes in time of the filtered variables ${\bar {u}}_{i}$ . Since the unfiltered variables $u_{i}$ are not known, it is impossible to directly calculate ${\overline {\frac {\partial u_{i}u_{j}}{\partial x_{j}}}}$ . However, the quantity ${\frac {\partial {\bar {u}}_{i}{\bar {u}}_{j}}{\partial x_{j}}}$ is known. A substitution is made:

${\frac {\partial {\bar {u}}_{i}}{\partial t}}+{\frac {\partial {\bar {u}}_{i}{\bar {u}}_{j}}{\partial x_{j}}}=-{\frac {1}{\rho }}{\frac {\partial {\bar {p}}}{\partial x_{i}}}+\nu {\frac {\partial ^{2}{\bar {u}}_{i}}{\partial x_{j}\partial x_{j}}}-\left({\overline {\frac {\partial u_{i}u_{j}}{\partial x_{j}}}}-{\frac {\partial {\bar {u}}_{i}{\bar {u}}_{j}}{\partial x_{j}}}\right).$

Let $\tau _{ij}={\overline {u_{i}u_{j}}}-{\bar {u}}_{i}{\bar {u}}_{j}$ . The resulting set of equations are the LES equations:

${\frac {\partial {\bar {u}}_{i}}{\partial t}}+{\bar {u}}_{j}{\frac {\partial {\bar {u}}_{i}}{\partial x_{j}}}=-{\frac {1}{\rho }}{\frac {\partial {\bar {p}}}{\partial x_{i}}}+\nu {\frac {\partial ^{2}{\bar {u}}_{i}}{\partial x_{j}\partial x_{j}}}-{\frac {\partial \tau _{ij}}{\partial x_{j}}}.$

### Compressible governing equations

For the governing equations of compressible flow, each equation, starting with the conservation of mass, is filtered. This gives:

${\frac {\partial {\overline {\rho }}}{\partial t}}+{\frac {\partial {\overline {u_{i}\rho }}}{\partial x_{i}}}=0$

which results in an additional sub-filter term. However, it is desirable to avoid having to model the sub-filter scales of the mass conservation equation. For this reason, Favre proposed a density-weighted filtering operation, called Favre filtering, defined for an arbitrary quantity $\phi$ as:

${\tilde {\phi }}={\frac {\overline {\rho \phi }}{\overline {\rho }}}$

which, in the limit of incompressibility, becomes the normal filtering operation. This makes the conservation of mass equation:

${\frac {\partial {\overline {\rho }}}{\partial t}}+{\frac {\partial {\overline {\rho }}{\tilde {u}}_{i}}{\partial x_{i}}}=0.$

This concept can then be extended to write the Favre-filtered momentum equation for compressible flow. Following Vreman:

${\frac {\partial {\overline {\rho }}{\tilde {u}}_{i}}{\partial t}}+{\frac {\partial {\overline {\rho }}{\tilde {u}}_{i}{\tilde {u}}_{j}}{\partial x_{j}}}+{\frac {\partial {\overline {p}}}{\partial x_{i}}}-{\frac {\partial {\tilde {\sigma }}_{ij}}{\partial x_{j}}}=-{\frac {\partial {\overline {\rho }}\tau _{ij}^{r}}{\partial x_{j}}}+{\frac {\partial }{\partial x_{j}}}\left({\overline {\sigma }}_{ij}-{\tilde {\sigma }}_{ij}\right)$

where $\sigma _{ij}$ is the shear stress tensor, given for a Newtonian fluid by:

$\sigma _{ij}=2\mu (T)S_{ij}-{\frac {2}{3}}\mu (T)\delta _{ij}S_{kk}$

and the term ${\frac {\partial }{\partial x_{j}}}\left({\overline {\sigma }}_{ij}-{\tilde {\sigma }}_{ij}\right)$ represents a sub-filter viscous contribution from evaluating the viscosity $\mu (T)$ using the Favre-filtered temperature ${\tilde {T}}$ . The subgrid stress tensor for the Favre-filtered momentum field is given by

$\tau _{ij}^{r}={\widetilde {u_{i}\cdot u_{j}}}-{\tilde {u}}_{i}{\tilde {u}}_{j}$

By analogy, the Leonard decomposition may also be written for the residual stress tensor for a filtered triple product ${\overline {\rho \phi \psi }}$ . The triple product can be rewritten using the Favre filtering operator as ${\overline {\rho }}{\widetilde {\phi \psi }}$ , which is an unclosed term (it requires knowledge of the fields $\phi$ and $\psi$ , when only the fields ${\tilde {\phi }}$ and ${\tilde {\psi }}$ are known). It can be broken up in a manner analogous to ${\overline {u_{i}u_{j}}}$ above, which results in a sub-filter stress tensor ${\overline {\rho }}\left({\widetilde {\phi \psi }}-{\tilde {\phi }}{\tilde {\psi }}\right)$ . This sub-filter term can be split up into contributions from three types of interactions: the Leondard tensor $L_{ij}$ , representing interactions among resolved scales; the Clark tensor $C_{ij}$ , representing interactions between resolved and unresolved scales; and the Reynolds tensor $R_{ij}$ , which represents interactions among unresolved scales.

### Filtered kinetic energy equation

In addition to the filtered mass and momentum equations, filtering the kinetic energy equation can provide additional insight. The kinetic energy field can be filtered to yield the total filtered kinetic energy:

${\overline {E}}={\frac {1}{2}}{\overline {u_{i}u_{i}}}$

and the total filtered kinetic energy can be decomposed into two terms: the kinetic energy of the filtered velocity field $E_{f}$ ,

$E_{f}={\frac {1}{2}}{\overline {u_{i}}}\,{\overline {u_{i}}}$

and the residual kinetic energy $k_{r}$ ,

$k_{r}={\frac {1}{2}}{\overline {u_{i}u_{i}}}-{\frac {1}{2}}{\overline {u_{i}}}\,{\overline {u_{i}}}={\frac {1}{2}}\tau _{ii}^{r}$

such that ${\overline {E}}=E_{f}+k_{r}$ .

The conservation equation for $E_{f}$ can be obtained by multiplying the filtered momentum transport equation by ${\overline {u_{i}}}$ to yield:

${\frac {\partial E_{f}}{\partial t}}+{\overline {u_{j}}}{\frac {\partial E_{f}}{\partial x_{j}}}+{\frac {1}{\rho }}{\frac {\partial {\overline {u_{i}}}{\bar {p}}}{\partial x_{i}}}+{\frac {\partial {\overline {u_{i}}}\tau _{ij}^{r}}{\partial x_{j}}}-2\nu {\frac {\partial {\overline {u_{i}}}{\bar {S}}_{ij}}{\partial x_{j}}}=-\epsilon _{f}-\Pi$

where $\epsilon _{f}=2\nu {\bar {S}}_{ij}{\bar {S}}_{ij}$ is the dissipation of kinetic energy of the filtered velocity field by viscous stress, and $\Pi =-\tau _{ij}^{r}{\bar {S}}_{ij}$ represents the sub-filter scale (SFS) dissipation of kinetic energy.

The terms on the left-hand side represent transport, and the terms on the right-hand side are sink terms that dissipate kinetic energy.

The $\Pi$ SFS dissipation term is of particular interest, since it represents the transfer of energy from large resolved scales to small unresolved scales. On average, $\Pi$ transfers energy from large to small scales. However, instantaneously $\Pi$ can be positive *or* negative, meaning it can also act as a source term for $E_{f}$ , the kinetic energy of the filtered velocity field. The transfer of energy from unresolved to resolved scales is called **backscatter** (and likewise the transfer of energy from resolved to unresolved scales is called **forward-scatter**).

## Numerical methods for LES

Large eddy simulation involves the solution to the discrete filtered governing equations using computational fluid dynamics. LES resolves scales from the domain size L down to the filter size $\Delta$ , and as such a substantial portion of high wave number turbulent fluctuations must be resolved. This requires either high-order numerical schemes, or fine grid resolution if low-order numerical schemes are used. Chapter 13 of Pope addresses the question of how fine a grid resolution $\Delta x$ is needed to resolve a filtered velocity field ${\overline {u}}({\boldsymbol {x}})$ . Ghosal found that for low-order discretization schemes, such as those used in finite volume methods, the truncation error can be the same order as the subfilter scale contributions, unless the filter width $\Delta$ is considerably larger than the grid spacing $\Delta x$ . While even-order schemes have truncation error, they are non-dissipative, and because subfilter scale models are dissipative, even-order schemes will not affect the subfilter scale model contributions as strongly as dissipative schemes.

### Filter implementation

The filtering operation in large eddy simulation can be implicit or explicit. Implicit filtering recognizes that the subfilter scale model will dissipate in the same manner as many numerical schemes. In this way, the grid, or the numerical discretization scheme, can be assumed to be the LES low-pass filter. While this takes full advantage of the grid resolution, and eliminates the computational cost of calculating a subfilter scale model term, it is difficult to determine the shape of the LES filter that is associated with some numerical issues. Additionally, truncation error can also become an issue.

In explicit filtering, an LES filter is applied to the discretized Navier–Stokes equations, providing a well-defined filter shape and reducing the truncation error. However, explicit filtering requires a finer grid than implicit filtering, and the computational cost increases with $(\Delta x)^{4}$ . Chapter 8 of Sagaut (2006) covers LES numerics in greater detail.

## Boundary conditions of large eddy simulations

Inlet boundary conditions affect the accuracy of LES significantly, and the treatment of inlet conditions for LES is a complicated problem. Theoretically, a good boundary condition for LES should contain the following features:

(1) providing accurate information of flow characteristics, i.e. velocity and turbulence;

(2) satisfying the Navier-Stokes equations and other physics;

(3) being easy to implement and adjust to different cases.

Currently, methods of generating inlet conditions for LES are broadly divided into two categories classified by Tabor et al.:

The first method for generating turbulent inlets is to synthesize them according to particular cases, such as Fourier techniques, principle orthogonal decomposition (POD) and vortex methods. The synthesis techniques attempt to construct turbulent field at inlets that have suitable turbulence-like properties and make it easy to specify parameters of the turbulence, such as turbulent kinetic energy and turbulent dissipation rate. In addition, inlet conditions generated by using random numbers are computationally inexpensive. However, one serious drawback exists in the method. The synthesized turbulence does not satisfy the physical structure of fluid flow governed by Navier-Stokes equations.

The second method involves a separate and precursor calculation to generate a turbulent database which can be introduced into the main computation at the inlets. The database (sometimes named as ‘library’) can be generated in a number of ways, such as cyclic domains, pre-prepared library, and internal mapping. However, the method of generating turbulent inflow by precursor simulations requires large calculation capacity.

Researchers examining the application of various types of synthetic and precursor calculations have found that the more realistic the inlet turbulence, the more accurate LES predicts results.

## Modeling unresolved scales

To discuss the modeling of unresolved scales, first the unresolved scales must be classified. They fall into two groups: **resolved sub-filter scales** (SFS), and **sub-grid scales**(SGS).

The resolved sub-filter scales represent the scales with wave numbers larger than the cutoff wave number $k_{c}$ , but whose effects are dampened by the filter. Resolved sub-filter scales only exist when filters non-local in wave-space are used (such as a box or Gaussian filter). These resolved sub-filter scales must be modeled using filter reconstruction.

Sub-grid scales are any scales that are smaller than the cutoff filter width $\Delta$ . The form of the SGS model depends on the filter implementation. As mentioned in the Numerical methods for LES section, if implicit LES is considered, no SGS model is implemented and the numerical effects of the discretization are assumed to mimic the physics of the unresolved turbulent motions.

### Sub-grid scale models

Without a universally valid description of turbulence, empirical information must be utilized when constructing and applying SGS models, supplemented with fundamental physical constraints such as Galilean invariance . Two classes of SGS models exist; the first class is **functional models** and the second class is **structural models**. Some models may be categorized as both.

#### Functional (eddy–viscosity) models

Functional models are simpler than structural models, focusing only on dissipating energy at a rate that is physically correct. These are based on an artificial eddy viscosity approach, where the effects of turbulence are lumped into a turbulent viscosity. The approach treats dissipation of kinetic energy at sub-grid scales as analogous to molecular diffusion. In this case, the deviatoric part of $\tau _{ij}$ is modeled as:

$\tau _{ij}^{r}-{\frac {1}{3}}\tau _{kk}\delta _{ij}=-2\nu _{\mathrm {t} }{\bar {S}}_{ij}$

where $\nu _{\mathrm {t} }$ is the turbulent eddy viscosity and ${\bar {S}}_{ij}={\frac {1}{2}}\left({\frac {\partial {\bar {u}}_{i}}{\partial x_{j}}}+{\frac {\partial {\bar {u}}_{j}}{\partial x_{i}}}\right)$ is the rate-of-strain tensor.

Based on dimensional analysis, the eddy viscosity must have units of $\left[\nu _{\mathrm {t} }\right]={\frac {\mathrm {m^{2}} }{\mathrm {s} }}$ . Most eddy viscosity SGS models model the eddy viscosity as the product of a characteristic length scale and a characteristic velocity scale.

##### Smagorinsky–Lilly model

The first SGS model developed was the Smagorinsky–Lilly SGS model, which was developed by Smagorinsky and used in the first LES simulation by Deardorff. It models the eddy viscosity as:

$\nu _{\mathrm {t} }=C\Delta ^{2}{\sqrt {2{\bar {S}}_{ij}{\bar {S}}_{ij}}}=C\Delta ^{2}\left|{\bar {S}}\right|$

where $\Delta$ is the grid size and C is a constant.

This method assumes that the energy production and dissipation of the small scales are in equilibrium - that is, $\epsilon =\Pi$ .

##### The Dynamic Model (Germano et al. and beyond)

Germano et al. identified a number of studies using the Smagorinsky model that each found different values for the Smagorinsky constant C for different flow configurations. In an attempt to formulate a more universal approach to SGS models, Germano et al. proposed a dynamic Smagorinsky model, which utilized two filters: a grid LES filter, denoted ${\overline {f}}$ , and a test LES filter, denoted ${\hat {f}}$ for any turbulent field f . The test filter is larger in size than the grid filter and adds an additional smoothing of the turbulence field over the already smoothed fields represented by the LES. Applying the test filter to the LES equations (which are obtained by applying the "grid" filter to Navier-Stokes equations) results in a new set of equations that are identical in form but with the SGS stress $\tau _{ij}={\overline {u_{i}u_{j}}}-{\bar {u}}_{i}{\bar {u}}_{j}$ replaced by $T_{ij}={\widehat {\overline {u_{i}u_{j}}}}-{\hat {\bar {u}}}_{i}{\hat {\bar {u}}}_{j}$ . Germano *et* al. noted that even though neither $\tau _{ij}$ nor $T_{ij}$ can be computed exactly because of the presence of unresolved scales, there is an exact relation connecting these two tensors. This relation, known as the Germano identity is $L_{ij}=T_{ij}-{\hat {\tau }}_{ij}.$ Here $L_{ij}={\widehat {{\bar {u}}_{i}{\bar {u}}_{j}}}-{\widehat {{\bar {u}}_{i}}}{\widehat {{\bar {u}}_{j}}}$ can be explicitly evaluated as it involves only the filtered velocities and the operation of test filtering. The significance of the identity is that if one assumes that turbulence is self similar so that the SGS stress at the grid and test levels have the same form $\tau _{ij}-(\tau _{kk}/3)\delta _{ij}=-2C\Delta ^{2}|{\bar {S}}_{ij}|{\bar {S}}_{ij}$ and $T_{ij}-(T_{kk}/3)\delta _{ij}=-2C{\hat {\Delta }}^{2}|{\hat {\bar {S}}}_{ij}|{\hat {\bar {S}}}_{ij}$ , then the Germano identity provides an equation from which the Smagorinsky coefficient C (which is no longer a 'constant') can potentially be determined. [Inherent in the procedure is the assumption that the coefficient C is invariant of scale (see review )]. In order to do this, two additional steps were introduced in the original formulation. First, one assumed that even though C was in principle variable, the variation was sufficiently slow that it can be moved out of the filtering operation ${\widehat {C(.)}}=C{\widehat {(.)}}$ . Second, since C was a scalar, the Germano identity was contracted with a second rank tensor (the rate of strain tensor was chosen) to convert it to a scalar equation from which C could be determined. Lilly found a less arbitrary and therefore more satisfactory approach for obtaining C from the tensor identity. He noted that the Germano identity required the satisfaction of nine equations at each point in space (of which only five are independent) for a single quantity C . The problem of obtaining C was therefore over-determined. He proposed therefore that C be determined using a least square fit by minimizing the residuals. This results in

$C={\frac {L_{ij}m_{ij}}{m_{kl}m_{kl}}}.$

Here

$m_{ij}=\alpha _{ij}-{\widehat {\beta }}_{ij}$

and for brevity $\alpha _{ij}=-2{\hat {\Delta }}^{2}|{\hat {\bar {S}}}|{\hat {\bar {S}}}_{ij}$ , $\beta _{ij}=-2\Delta ^{2}|{\bar {S}}|{\bar {S}}_{ij}$ Initial attempts to implement the model in LES simulations proved unsuccessful. First, the computed coefficient was not at all "slowly varying" as assumed and varied as much as any other turbulent field. Secondly, the computed C could be positive as well as negative. The latter fact in itself should not be regarded as a shortcoming as a priori tests using filtered DNS fields have shown that the local subgrid dissipation rate $-\tau _{ij}{\bar {S}}_{ij}$ in a turbulent field is almost as likely to be negative as it is positive even though the integral over the fluid domain is always positive representing a net dissipation of energy in the large scales. A slight preponderance of positive values as opposed to strict positivity of the eddy-viscosity results in the observed net dissipation. This so-called "backscatter" of energy from small to large scales indeed corresponds to negative C values in the Smagorinsky model. Nevertheless, the Germano-Lilly formulation was found not to result in stable calculations. An ad hoc measure was adopted by averaging the numerator and denominator over homogeneous directions (where such directions exist in the flow)

$C={\frac {\left\langle L_{ij}m_{ij}\right\rangle }{\left\langle m_{kl}m_{kl}\right\rangle }}.$

When the averaging involved a large enough statistical sample that the computed C was positive (or at least only rarely negative) stable calculations were possible. Simply setting the negative values to zero (a procedure called "clipping") with or without the averaging also resulted in stable calculations. Meneveau proposed an averaging over Lagrangian fluid trajectories with an exponentially decaying "memory". This can be applied to problems lacking homogeneous directions and can be stable if the effective time over which the averaging is done is long enough and yet not so long as to smooth out spatial inhomogenieties of interest.

Lilly's modification of the Germano method followed by a statistical averaging or synthetic removal of negative viscosity regions seems ad hoc, even if it could be made to "work". An alternate formulation of the least square minimization procedure known as the "Dynamic Localization Model" (DLM) was suggested by Ghosal et al. In this approach one first defines a quantity

$E_{ij}=L_{ij}-T_{ij}+{\hat {\tau }}_{ij}$

with the tensors $\tau _{ij}$ and $T_{ij}$ replaced by the appropriate SGS model. This tensor then represents the amount by which the subgrid model fails to respect the Germano identity at each spatial location. In Lilly's approach, C is then pulled out of the hat operator

${\widehat {C(.)}}=C{\widehat {(.)}}$

making $E_{ij}$ an algebraic function of C which is then determined by requiring that $E_{ij}E_{ij}$ considered as a function of C have the least possible value. However, since the C thus obtained turns out to be just as variable as any other fluctuating quantity in turbulence, the original assumption of the constancy of C cannot be justified a posteriori. In the DLM approach one avoids this inconsistency by not invoking the step of removing C from the test filtering operation. Instead, one defines a global error over the entire flow domain by the quantity

$E[C]=\int E_{ij}E_{ij}dV$

where the integral ranges over the whole fluid volume. This global error $E[C(x,y,z,t)]$ is then a functional of the spatially varying function $C(x,y,z,t)$ (here the time instant, t , is fixed and therefore appears just as a parameter) which is determined so as to minimize this functional. The solution to this variational problem is that C must satisfy a Fredholm integral equation of the second kind

$C({\boldsymbol {x}})=f({\boldsymbol {x}})+\int K({\boldsymbol {x}},{\boldsymbol {y}})C({\boldsymbol {y}})d{\boldsymbol {y}}$

where the functions $K({\boldsymbol {x}},{\boldsymbol {y}})$ and $f({\boldsymbol {x}})$ are defined in terms of the resolved fields $L_{ij},\alpha _{ij},\beta _{ij}$ and are therefore known at each time step and the integral ranges over the whole fluid domain. The integral equation is solved numerically by an iteration procedure and convergence was found to be generally rapid if used with a pre-conditioning scheme. Even though this variational approach removes an inherent inconsistency in Lilly's approach, the $C(x,y,z,t)$ obtained from the integral equation still displayed the instability associated with negative viscosities. This can be resolved by insisting that $E[C]$ be minimized subject to the constraint $C(x,y,z,t)\geq 0$ . This leads to an equation for C that is nonlinear

$C({\boldsymbol {x}})=\left[f({\boldsymbol {x}})+\int K({\boldsymbol {x}},{\boldsymbol {y}})C({\boldsymbol {y}})d{\boldsymbol {y}}\right]_{+}$

Here the suffix + indicates the "positive part of" that is, $x_{+}=(x+|x|)/2$ . Even though this superficially looks like "clipping" it is not an ad hoc scheme but a bonafide solution of the constrained variational problem. This DLM(+) model was found to be stable and yielded excellent results for forced and decaying isotropic turbulence, channel flows and a variety of other more complex geometries. If a flow happens to have homogeneous directions (let us say the directions x and z) then one can introduce the ansatz $C=C(y,t)$ . The variational approach then immediately yields Lilly's result with averaging over homogeneous directions without any need for ad hoc modifications of a prior result.

One shortcoming of the DLM(+) model was that it did not describe backscatter which is known to be a real "thing" from analyzing DNS data. Two approaches were developed to address this. In one approach due to Carati et al. a fluctuating force with amplitude determined by the fluctuation-dissipation theorem is added in analogy to Landau's theory of fluctuating hydrodynamics. In the second approach, one notes that any "backscattered" energy appears in the resolved scales only at the expense of energy in the subgrid scales. The DLM can be modified in a simple way to take into account this physical fact so as to allow for backscatter while being inherently stable. This k-equation version of the DLM, DLM(k) replaces $\Delta |{\bar {S}}|$ in the Smagorinsky eddy viscosity model by ${\sqrt {k}}$ as an appropriate velocity scale. The procedure for determining C remains identical to the "unconstrained" version except that the tensors $\alpha _{ij}=-2{\hat {\Delta }}{\sqrt {K}}{\hat {\bar {S}}}_{ij}$ , $\beta _{ij}=-2{\hat {\Delta }}{\sqrt {k}}{\bar {S}}_{ij}$ where the sub-test scale kinetic energy K is related to the subgrid scale kinetic energy k by $K=k+L_{ii}/2$ (follows by taking the trace of the Germano identity). To determine k we now use a transport equation

${\frac {\partial k}{\partial t}}+u_{j}{\frac {\partial k}{\partial x_{j}}}=-\tau _{ij}{\bar {S}}_{ij}-{\frac {C_{*}}{\Delta }}k^{3/2}+{\frac {\partial }{\partial x_{j}}}\left(D\Delta {\sqrt {k}}{\frac {\partial k}{\partial x_{j}}}\right)+\nu {\frac {\partial ^{2}k}{\partial x_{j}\partial x_{j}}}$

where $\nu$ is the kinematic viscosity and $C_{*},D$ are positive coefficients representing kinetic energy dissipation and diffusion respectively. These can be determined following the dynamic procedure with constrained minimization as in DLM(+). This approach, though more expensive to implement than the DLM(+) was found to be stable and resulted in good agreement with experimental data for a variety of flows tested. Furthermore, it is mathematically impossible for the DLM(k) to result in an unstable computation as the sum of the large scale and SGS energies is non-increasing by construction. Both of these approaches incorporating backscatter works well. They yield models that are slightly less dissipative with somewhat improved performance over the DLM(+). The DLM(k) model additionally yields the subgrid kinetic energy, which may be a physical quantity of interest. These improvements are achieved at a somewhat increased cost in model implementation.

The Dynamic Model originated at the 1990 Summer Program of the Center for Turbulence Research (CTR) at Stanford University. A series of "CTR-Tea" seminars celebrated the 30th Anniversary Archived 2022-10-30 at the Wayback Machine of this important milestone in turbulence modeling.
