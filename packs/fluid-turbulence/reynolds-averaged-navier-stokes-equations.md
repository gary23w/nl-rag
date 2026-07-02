---
title: "Reynolds-averaged Navier–Stokes equations"
source: https://en.wikipedia.org/wiki/Reynolds-averaged_Navier%E2%80%93Stokes_equations
domain: fluid-turbulence
license: CC-BY-SA-4.0
tags: fluid turbulence, turbulence modeling, large eddy simulation, direct numerical simulation
fetched: 2026-07-02
---

# Reynolds-averaged Navier–Stokes equations

The **Reynolds-averaged Navier–Stokes equations** (**RANS equations**) are time-averaged equations of motion for fluid flow. The idea behind the equations is Reynolds decomposition, whereby an instantaneous quantity is decomposed into its time-averaged and fluctuating quantities, an idea first proposed by Osborne Reynolds. The RANS equations are primarily used to describe turbulent flows. These equations can be used with approximations based on knowledge of the properties of flow turbulence to give approximate time-averaged solutions to the Navier–Stokes equations. For a stationary flow of an incompressible Newtonian fluid, these equations can be written in Einstein notation in Cartesian coordinates as: $\rho {\bar {u}}_{j}{\frac {\partial {\bar {u}}_{i}}{\partial x_{j}}}=\rho {\bar {f}}_{i}+{\frac {\partial }{\partial x_{j}}}\left[-{\bar {p}}\delta _{ij}+\mu \left({\frac {\partial {\bar {u}}_{i}}{\partial x_{j}}}+{\frac {\partial {\bar {u}}_{j}}{\partial x_{i}}}\right)-\rho {\overline {u_{i}^{\prime }u_{j}^{\prime }}}\right].$

The left hand side of this equation represents the change in mean momentum of a fluid element owing to the unsteadiness in the mean flow and the convection by the mean flow. This change is balanced by the mean body force, the isotropic stress owing to the mean pressure field, the viscous stresses, and apparent stress $\left(-\rho {\overline {u_{i}^{\prime }u_{j}^{\prime }}}\right)$ owing to the fluctuating velocity field, generally referred to as the Reynolds stress. This nonlinear Reynolds stress term requires additional modeling to close the RANS equation for solving, and has led to the creation of many different turbulence models. The time-average operator ${\overline {.}}$ is a Reynolds operator.

## Derivation of RANS equations

The basic tool required for the derivation of the RANS equations from the instantaneous Navier–Stokes equations is the Reynolds decomposition. Reynolds decomposition refers to separation of the flow variable (like velocity u ) into the mean (time-averaged) component ( ${\overline {u}}$ ) and the fluctuating component ( $u^{\prime }$ ). Because the mean operator is a Reynolds operator, it has a set of properties. One of these properties is that the mean of the fluctuating quantity is equal to zero $({\bar {u'}})$ Some authors prefer using U instead of ${\bar {u}}$ for the mean term (since an overbar is sometimes used to represent a vector). In this case, the fluctuating term $u^{\prime }$ is represented instead by u . This is possible because the two terms do not appear simultaneously in the same equation. To avoid confusion, the notation u , ${\bar {u}}$ , and $u'$ will be used to represent the instantaneous, mean, and fluctuating terms, respectively.

The properties of Reynolds operators are useful in the derivation of the RANS equations. Using these properties, the Navier–Stokes equations of motion, expressed in tensor notation, are (for an incompressible Newtonian fluid): ${\frac {\partial u_{i}}{\partial x_{i}}}=0$ ${\frac {\partial u_{i}}{\partial t}}+u_{j}{\frac {\partial u_{i}}{\partial x_{j}}}=f_{i}-{\frac {1}{\rho }}{\frac {\partial p}{\partial x_{i}}}+\nu {\frac {\partial ^{2}u_{i}}{\partial x_{j}\partial x_{j}}}$ where $f_{i}$ is a vector representing external forces.

Next, each instantaneous quantity can be split into time-averaged and fluctuating components, and the resulting equation time-averaged, to yield:

${\frac {\partial {\bar {u}}_{i}}{\partial x_{i}}}=0$ ${\frac {\partial {\bar {u}}_{i}}{\partial t}}+{\bar {u}}_{j}{\frac {\partial {\bar {u}}_{i}}{\partial x_{j}}}+{\overline {u_{j}^{\prime }{\frac {\partial u_{i}^{\prime }}{\partial x_{j}}}}}={\bar {f}}_{i}-{\frac {1}{\rho }}{\frac {\partial {\bar {p}}}{\partial x_{i}}}+\nu {\frac {\partial ^{2}{\bar {u}}_{i}}{\partial x_{j}\partial x_{j}}}.$

The momentum equation can also be written as,

${\frac {\partial {\bar {u}}_{i}}{\partial t}}+{\bar {u}}_{j}{\frac {\partial {\bar {u}}_{i}}{\partial x_{j}}}={\bar {f}}_{i}-{\frac {1}{\rho }}{\frac {\partial {\bar {p}}}{\partial x_{i}}}+\nu {\frac {\partial ^{2}{\bar {u}}_{i}}{\partial x_{j}\partial x_{j}}}-{\frac {\partial {\overline {u_{i}^{\prime }u_{j}^{\prime }}}}{\partial x_{j}}}.$ On further manipulations this yields, $\rho {\frac {\partial {\bar {u}}_{i}}{\partial t}}+\rho {\bar {u}}_{j}{\frac {\partial {\bar {u}}_{i}}{\partial x_{j}}}=\rho {\bar {f}}_{i}+{\frac {\partial }{\partial x_{j}}}\left[-{\bar {p}}\delta _{ij}+2\mu {\bar {S}}_{ij}-\rho {\overline {u_{i}^{\prime }u_{j}^{\prime }}}\right]$

where, ${\bar {S}}_{ij}={\frac {1}{2}}\left({\frac {\partial {\bar {u}}_{i}}{\partial x_{j}}}+{\frac {\partial {\bar {u}}_{j}}{\partial x_{i}}}\right)$ is the mean rate of strain tensor.

Finally, since integration in time removes the time dependence of the resultant terms, the time derivative must be eliminated, leaving: $\rho {\bar {u}}_{j}{\frac {\partial {\bar {u}}_{i}}{\partial x_{j}}}=\rho {\bar {f_{i}}}+{\frac {\partial }{\partial x_{j}}}\left[-{\bar {p}}\delta _{ij}+2\mu {\bar {S}}_{ij}-\rho {\overline {u_{i}^{\prime }u_{j}^{\prime }}}\right].$

## Equations of Reynolds stress

The time evolution equation of Reynolds stress is given by: ${\frac {\partial {\overline {u_{i}^{\prime }u_{j}^{\prime }}}}{\partial t}}+{\bar {u}}_{k}{\frac {\partial {\overline {u_{i}^{\prime }u_{j}^{\prime }}}}{\partial x_{k}}}=-{\overline {u_{i}^{\prime }u_{k}^{\prime }}}{\frac {\partial {\bar {u}}_{j}}{\partial x_{k}}}-{\overline {u_{j}^{\prime }u_{k}^{\prime }}}{\frac {\partial {\bar {u}}_{i}}{\partial x_{k}}}+{\overline {{\frac {p^{\prime }}{\rho }}\left({\frac {\partial u_{i}^{\prime }}{\partial x_{j}}}+{\frac {\partial u_{j}^{\prime }}{\partial x_{i}}}\right)}}-{\frac {\partial }{\partial x_{k}}}\left({\overline {u_{i}^{\prime }u_{j}^{\prime }u_{k}^{\prime }}}+{\frac {\overline {p^{\prime }u_{i}^{\prime }}}{\rho }}\delta _{jk}+{\frac {\overline {p^{\prime }u_{j}^{\prime }}}{\rho }}\delta _{ik}-\nu {\frac {\partial {\overline {u_{i}^{\prime }u_{j}^{\prime }}}}{\partial x_{k}}}\right)-2\nu {\overline {{\frac {\partial u_{i}^{\prime }}{\partial x_{k}}}{\frac {\partial u_{j}^{\prime }}{\partial x_{k}}}}}$ This equation is very complicated. If ${\overline {u_{i}^{\prime }u_{j}^{\prime }}}$ is traced, turbulence kinetic energy is obtained. The last term $\nu {\overline {{\frac {\partial u_{i}^{\prime }}{\partial x_{k}}}{\frac {\partial u_{j}^{\prime }}{\partial x_{k}}}}}$ is turbulent dissipation rate. All RANS models are based on the above equation.

## Applications (RANS modelling)

- A model for testing performance was determined that, when combined with the vortex lattice (VLM) or boundary element method (BEM), RANS was found useful for modelling the flow of water between two contrary rotation propellers, where VLM or BEM are applied to the propellers and RANS is used for the dynamically fluxing inter-propeller state.
- The RANS equations have been widely utilized as a model for determining flow characteristics and assessing wind comfort in urban environments. This computational approach can be executed through direct calculations involving the solution of the RANS equations, or through an indirect method involving the training of machine learning algorithms using the RANS equations as a basis. The direct approach is more accurate than the indirect approach but it requires expertise in numerical methods and computational fluid dynamics (CFD), as well as substantial computational resources to handle the complexity of the equations.
