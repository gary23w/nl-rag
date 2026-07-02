---
title: "Navier–Stokes equations (part 1/2)"
source: https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_equations
domain: continuum-mechanics
license: CC-BY-SA-4.0
tags: continuum mechanics, stress tensor, constitutive equation, deformation gradient
fetched: 2026-07-02
part: 1/2
---

# Navier–Stokes equations

The **Navier–Stokes equations** (/nævˈjeɪ ˈstoʊks/ *nav-YAY STOHKS*) describe the motion of viscous fluids. This system of partial differential equations was named after Claude-Louis Navier and George Gabriel Stokes, who developed them over a few decades of progressive work, from 1822 (Navier) to 1842–1850 (Stokes). Siméon Denis Poisson independently achieved the same results.

The Navier–Stokes equations mathematically express momentum balance for Newtonian fluids and make use of the conservation of mass. They are sometimes accompanied by an equation of state relating pressure, temperature and density. They arise from applying Newton's second law to fluid motion, together with the assumption that the stress in the fluid is the sum of a diffusing viscous term (proportional to the gradient of velocity) and a pressure term—hence describing *viscous flow*. The Navier–Stokes equations generalize the Euler equations in that the latter model only considers inviscid flow.

The Navier–Stokes equations are of great scientific and engineering interest because they may be used to model a wide variety of scenarios. In their full or simplified forms, they can assist in the design of aircraft and cars, the study of blood flow, the design of power stations, the analysis of pollution, and many other problems. Coupled with Maxwell's equations, they comprise the fundamentals of magnetohydrodynamics.

The Navier–Stokes equations are also of great interest in a purely mathematical sense. Despite their wide range of practical uses, the conjecture that they have smooth (meaning infinitely differentiable) or bounded solutions in three dimensions has not yet been proven. This is called the Navier–Stokes existence and smoothness problem. The Clay Mathematics Institute has called this one of the seven most important open problems in mathematics and has offered a $1 million prize for a solution or a counterexample.


## Flow velocity

The solution of the equations is a flow velocity. It is a vector field—to every point in a fluid, at any moment in a time interval, it gives a vector whose direction and magnitude are those of the velocity of the fluid at that point in space and at that moment in time. It is studied in three spatial dimensions and one time dimension, and higher-dimensional analogues are studied in both pure and applied mathematics. Once the velocity field is calculated, other quantities of interest, such as pressure or temperature, may be found using dynamical equations and relations. This is different from what one normally sees in classical mechanics, where solutions are typically trajectories of the position of a particle or deflection of a continuum. Studying velocity instead of position makes more sense for a fluid, although for visualization purposes, one can compute various trajectories. In particular, the streamlines of a vector field, interpreted as flow velocity, are the paths along which a massless fluid particle would travel. These paths are the integral curves whose derivative at each point is equal to the vector field, and they can represent visually the behavior of the vector field at a point in time.


## General continuum equations

The Navier–Stokes momentum equation can be derived as a particular form of the Cauchy momentum equation, whose general convective form is: ${\frac {\mathrm {D} \mathbf {u} }{\mathrm {D} t}}={\frac {1}{\rho }}\nabla \cdot {\boldsymbol {\sigma }}+\mathbf {a} .$ By setting the Cauchy stress tensor ${\textstyle {\boldsymbol {\sigma }}}$ to be the sum of a viscosity term ${\textstyle {\boldsymbol {\tau }}}$ (the deviatoric stress) and a pressure term ${\textstyle -p\mathbf {I} }$ (volumetric stress), we arrive at:

Cauchy momentum equation

(convective form)

$\rho {\frac {\mathrm {D} \mathbf {u} }{\mathrm {D} t}}=-\nabla p+\nabla \cdot {\boldsymbol {\tau }}+\rho \,\mathbf {a}$

where

- ${\textstyle {\frac {\mathrm {D} }{\mathrm {D} t}}}$ is the material derivative, defined as ${\textstyle {\frac {\partial }{\partial t}}+\mathbf {u} \cdot \nabla }$ ,
- ${\textstyle \rho }$ is the (mass) density,
- ${\textstyle \mathbf {u} }$ is the flow velocity,
- ${\textstyle \nabla \cdot \,}$ is the divergence,
- ${\textstyle p}$ is the pressure,
- ${\textstyle t}$ is time,
- ${\textstyle {\boldsymbol {\tau }}}$ is the deviatoric stress tensor, which has order 2,
- ${\textstyle \mathbf {a} }$ represents body accelerations acting on the continuum, for example gravity, inertial accelerations, electrostatic accelerations, and so on.

In this form, it is apparent that in the assumption of an inviscid fluid – no deviatoric stress – Cauchy equations reduce to the Euler equations.

Assuming conservation of mass, with the known properties of divergence and gradient we can use the mass continuity equation, which represents the mass per unit volume of a homogenous fluid with respect to space and time (i.e., material derivative ${\textstyle {\frac {\mathbf {D} }{\mathbf {Dt} }}}$ ) of any finite volume ( ${\textstyle \mathbf {V} }$ ) to represent the change of velocity in fluid media: ${\begin{aligned}&{\frac {\mathbf {D} m}{\mathbf {Dt} }}=\iiint \limits _{V}\left({\frac {\mathbf {D} \rho }{\mathbf {Dt} }}+\rho (\nabla \cdot \mathbf {u} )\right)\,dV\\[5pt]&{\frac {\mathbf {D} \rho }{\mathbf {Dt} }}+\rho (\nabla \cdot \mathbf {u} )={\frac {\partial \rho }{\partial t}}+(\nabla \rho )\cdot \mathbf {u} +\rho (\nabla \cdot \mathbf {u} )={\frac {\partial \rho }{\partial t}}+\nabla \cdot (\rho \mathbf {u} )=0\end{aligned}}$ where

- ${\textstyle {\frac {\mathrm {D} m}{\mathrm {D} t}}}$ is the material derivative of mass per unit volume (density, $\rho$ ),
- ${\textstyle \iiint \limits _{V}{\bigl (}F(x_{1},x_{2},x_{3},t){\bigr )}\,dV}$ is the mathematical operation for the integration throughout the volume ( ${\textstyle V}$ ),
- ${\textstyle {\frac {\partial }{\partial t}}}$ is the partial derivative mathematical operator,
- ${\textstyle \nabla \cdot \mathbf {u} \,}$ is the divergence of the flow velocity ( $\mathbf {u}$ ), which is a scalar field,
- ${\textstyle \nabla \rho \,}$ is the gradient of density ( $\rho$ ), which is the vector derivative of a scalar field,

to arrive at the conservation form of the equations of motion. This is often written:

Cauchy momentum equation

(conservation form)

${\frac {\partial }{\partial t}}(\rho \,\mathbf {u} )+\nabla \cdot (\rho \,\mathbf {u} \otimes \mathbf {u} )=-\nabla p+\nabla \cdot {\boldsymbol {\tau }}+\rho \,\mathbf {a}$

where ${\textstyle \otimes }$ is the outer product of the flow velocity ( ${\textstyle \mathbf {u} }$ ): $\mathbf {u} \otimes \mathbf {u} =\mathbf {u} \mathbf {u} ^{\mathsf {T}}$

The left side of the equation describes acceleration, and may be composed of time-dependent and convective components (also the effects of non-inertial coordinates if present). The right side of the equation is in effect a summation of hydrostatic effects, the divergence of deviatoric stress and body forces (such as gravity).

All non-relativistic balance equations, such as the Navier–Stokes equations, can be derived by beginning with the Cauchy equations and specifying the stress tensor through a constitutive relation. By expressing the deviatoric (shear) stress tensor in terms of viscosity and the fluid velocity gradient, and assuming constant viscosity, the above Cauchy equations will lead to the Navier–Stokes equations below.

### Convective acceleration

A significant feature of the Cauchy equation and consequently all other continuum equations (including Euler and Navier–Stokes) is the presence of convective acceleration: the effect of acceleration of a flow with respect to space. While individual fluid particles indeed experience time-dependent acceleration, the convective acceleration of the flow field is a spatial effect, one example being fluid speeding up in a nozzle.


## Compressible flow

Remark: here, the deviatoric stress tensor is denoted ${\textstyle {\boldsymbol {\tau }}}$ as it was in the general continuum equations and in the incompressible flow section.

The compressible momentum Navier–Stokes equation results from the following assumptions on the Cauchy stress tensor:

- the stress is **Galilean invariant**: it does not depend directly on the flow velocity, but only on spatial derivatives of the flow velocity. So the stress variable is the tensor gradient ${\textstyle \nabla \mathbf {u} }$ , or more simply the rate-of-strain tensor: ${\textstyle {\boldsymbol {\varepsilon }}\left(\nabla \mathbf {u} \right)\equiv {\frac {1}{2}}\nabla \mathbf {u} +{\frac {1}{2}}\left(\nabla \mathbf {u} \right)^{\mathsf {T}}}$
- the deviatoric stress is **linear** in this variable: ${\textstyle {\boldsymbol {\sigma }}({\boldsymbol {\varepsilon }})=-p\mathbf {I} +\mathbf {C} :{\boldsymbol {\varepsilon }}}$ , where ${\textstyle p}$ is independent on the strain rate tensor, ${\textstyle \mathbf {C} }$ is the fourth-order tensor representing the constant of proportionality, called the viscosity or elasticity tensor, and : is the double-dot product.
- the fluid is assumed to be isotropic, as with gases and simple liquids, and consequently ${\textstyle \mathbf {C} }$ is an isotropic tensor; furthermore, since the deviatoric stress tensor is symmetric, by Helmholtz decomposition it can be expressed in terms of two scalar Lamé parameters, the second viscosity ${\textstyle \lambda }$ and the dynamic viscosity ${\textstyle \mu }$ , as it is usual in linear elasticity: **Linear stress constitutive equation**  *(expression similar to the one for elastic solid)* ${\boldsymbol {\sigma }}({\boldsymbol {\varepsilon }})=-p\mathbf {I} +\lambda \operatorname {tr} ({\boldsymbol {\varepsilon }})\mathbf {I} +2\mu {\boldsymbol {\varepsilon }}$ where ${\textstyle \mathbf {I} }$ is the identity tensor, and ${\textstyle \operatorname {tr} ({\boldsymbol {\varepsilon }})}$ is the trace of the rate-of-strain tensor. So this decomposition can be explicitly defined as: ${\boldsymbol {\sigma }}=-p\mathbf {I} +\lambda (\nabla \cdot \mathbf {u} )\mathbf {I} +\mu \left(\nabla \mathbf {u} +(\nabla \mathbf {u} )^{\mathsf {T}}\right).$

Since the trace of the rate-of-strain tensor in three dimensions is the divergence (i.e. rate of expansion) of the flow: $\operatorname {tr} ({\boldsymbol {\varepsilon }})=\nabla \cdot \mathbf {u} .$

Given this relation, and since the trace of the identity tensor in three dimensions is three: $\operatorname {tr} ({\boldsymbol {I}})=3.$

the trace of the stress tensor in three dimensions becomes: $\operatorname {tr} ({\boldsymbol {\sigma }})=-3p+(3\lambda +2\mu )\nabla \cdot \mathbf {u} .$

So by alternatively decomposing the stress tensor into **isotropic** and **deviatoric** parts, as usual in fluid dynamics: ${\boldsymbol {\sigma }}=-\left[p-\left(\lambda +{\tfrac {2}{3}}\mu \right)\left(\nabla \cdot \mathbf {u} \right)\right]\mathbf {I} +\mu \left(\nabla \mathbf {u} +\left(\nabla \mathbf {u} \right)^{\mathsf {T}}-{\tfrac {2}{3}}\left(\nabla \cdot \mathbf {u} \right)\mathbf {I} \right)$

Introducing the bulk viscosity ${\textstyle \zeta }$ , $\zeta \equiv \lambda +{\tfrac {2}{3}}\mu ,$

we arrive at the linear constitutive equation in the form usually employed in thermal hydraulics:

Linear stress constitutive equation

(expression used for fluids)

${\boldsymbol {\sigma }}=-{\bigl [}p-\zeta (\nabla \cdot \mathbf {u} ){\bigr ]}\mathbf {I} +\mu \left[\nabla \mathbf {u} +(\nabla \mathbf {u} )^{\mathsf {T}}-{\tfrac {2}{3}}(\nabla \cdot \mathbf {u} )\mathbf {I} \right]$

which can also be arranged in the other usual form: ${\boldsymbol {\sigma }}=-p\mathbf {I} +\mu \left(\nabla \mathbf {u} +(\nabla \mathbf {u} )^{\mathsf {T}}\right)+\left(\zeta -{\tfrac {2}{3}}\mu \right)(\nabla \cdot \mathbf {u} )\mathbf {I} .$

Note that in the compressible case the pressure is no more proportional to the isotropic stress term, since there is the additional bulk viscosity term: $p=-{\tfrac {1}{3}}\operatorname {tr} ({\boldsymbol {\sigma }})+\zeta (\nabla \cdot \mathbf {u} )$

and the deviatoric stress tensor ${\boldsymbol {\sigma }}'$ is still coincident with the shear stress tensor ${\boldsymbol {\tau }}$ (i.e. the deviatoric stress in a Newtonian fluid has no normal stress components), and it has a compressibility term in addition to the incompressible case, which is proportional to the shear viscosity:

${\boldsymbol {\sigma }}'={\boldsymbol {\tau }}=\mu \left[\nabla \mathbf {u} +(\nabla \mathbf {u} )^{\mathsf {T}}-{\tfrac {2}{3}}(\nabla \cdot \mathbf {u} )\mathbf {I} \right]$

Both bulk viscosity ${\textstyle \zeta }$ and dynamic viscosity ${\textstyle \mu }$ need not be constant – in general, they depend on two thermodynamics variables if the fluid contains a single chemical species, say for example, pressure and temperature. Any equation that makes explicit one of these transport coefficient in the conservation variables is called an equation of state.

The most general of the Navier–Stokes equations become

Navier–Stokes momentum equation

(convective form)

$\rho {\frac {\mathrm {D} \mathbf {u} }{\mathrm {D} t}}=\rho \left({\frac {\partial \mathbf {u} }{\partial t}}+(\mathbf {u} \cdot \nabla )\mathbf {u} \right)=-\nabla p+\nabla \cdot \left(\mu \left[\nabla \mathbf {u} +(\nabla \mathbf {u} )^{\mathsf {T}}-{\tfrac {2}{3}}(\nabla \cdot \mathbf {u} )\mathbf {I} \right]\right)+\nabla [\zeta (\nabla \cdot \mathbf {u} )]+\rho \mathbf {a} .$

in index notation, the equation can be written as

Navier–Stokes momentum equation

(index notation)

$\rho \left({\frac {\partial u_{i}}{\partial t}}+u_{k}{\frac {\partial u_{i}}{\partial x_{k}}}\right)=-{\frac {\partial p}{\partial x_{i}}}+{\frac {\partial }{\partial x_{k}}}\left[\mu \left({\frac {\partial u_{i}}{\partial x_{k}}}+{\frac {\partial u_{k}}{\partial x_{i}}}-{\tfrac {2}{3}}\delta _{ik}{\frac {\partial u_{l}}{\partial x_{l}}}\right)\right]+{\frac {\partial }{\partial x_{i}}}\left(\zeta {\frac {\partial u_{\ell }}{\partial x_{\ell }}}\right)+\rho a_{i}.$

The corresponding equation in conservation form can be obtained by considering that, given the mass continuity equation, the left side is equivalent to:

$\rho {\frac {\mathrm {D} \mathbf {u} }{\mathrm {D} t}}={\frac {\partial }{\partial t}}(\rho \mathbf {u} )+\nabla \cdot (\rho \mathbf {u} \otimes \mathbf {u} )$

to give finally:

Navier–Stokes momentum equation

(conservative form)

${\frac {\partial }{\partial t}}(\rho \mathbf {u} )+\nabla \cdot \left(\rho \mathbf {u} \otimes \mathbf {u} +[p-\zeta (\nabla \cdot \mathbf {u} )]\mathbf {I} -\mu \left[\nabla \mathbf {u} +(\nabla \mathbf {u} )^{\mathsf {T}}-{\tfrac {2}{3}}(\nabla \cdot \mathbf {u} )\mathbf {I} \right]\right)=\rho \mathbf {a} .$

Apart from its dependence of pressure and temperature, the second viscosity coefficient also depends on the process, that is to say, the second viscosity coefficient is not just a material property. Example: in the case of a sound wave with a definitive frequency that alternatively compresses and expands a fluid element, the second viscosity coefficient depends on the frequency of the wave. This dependence is called the *dispersion*. In some cases, the second viscosity ${\textstyle \zeta }$ can be assumed to be constant in which case, the effect of the volume viscosity ${\textstyle \zeta }$ is that the mechanical pressure is not equivalent to the thermodynamic pressure: as demonstrated below. ${\begin{aligned}&\nabla \cdot (\nabla \cdot \mathbf {u} )\mathbf {I} =\nabla (\nabla \cdot \mathbf {u} ),\\&{\bar {p}}\equiv p-\zeta \,\nabla \cdot \mathbf {u} ,\end{aligned}}$ However, this difference is usually neglected most of the time (that is whenever we are not dealing with processes such as sound absorption and attenuation of shock waves, where second viscosity coefficient becomes important) by explicitly assuming ${\textstyle \zeta =0}$ . The assumption of setting ${\textstyle \zeta =0}$ is called as the **Stokes hypothesis**. The validity of Stokes hypothesis can be demonstrated for monoatomic gas both experimentally and from the kinetic theory; for other gases and liquids, Stokes hypothesis is generally incorrect. With the Stokes hypothesis, the Navier–Stokes equations become

Navier–Stokes momentum equation

(convective form, Stokes hypothesis)

$\rho {\frac {\mathrm {D} \mathbf {u} }{\mathrm {D} t}}=\rho \left({\frac {\partial \mathbf {u} }{\partial t}}+(\mathbf {u} \cdot \nabla )\mathbf {u} \right)=-\nabla p+\nabla \cdot \left(\mu \left[\nabla \mathbf {u} +(\nabla \mathbf {u} )^{\mathsf {T}}-{\tfrac {2}{3}}(\nabla \cdot \mathbf {u} )\mathbf {I} \right]\right)+\rho \mathbf {a} .$

If the dynamic $\mu$ and bulk $\zeta$ viscosities are assumed to be uniform in space, the equations in convective form can be simplified further. By computing the divergence of the stress tensor, since the divergence of tensor ${\textstyle \nabla \mathbf {u} }$ is ${\textstyle \nabla ^{2}\mathbf {u} }$ and the divergence of tensor ${\textstyle \left(\nabla \mathbf {u} \right)^{\mathsf {T}}}$ is ${\textstyle \nabla \left(\nabla \cdot \mathbf {u} \right)}$ , one finally arrives to the compressible Navier–Stokes momentum equation:

Navier–Stokes momentum equation

with uniform shear and bulk viscosities

(convective form)

${\frac {D\mathbf {u} }{Dt}}=-{\frac {1}{\rho }}\nabla p+\nu \,\nabla ^{2}\mathbf {u} +\left({\tfrac {1}{3}}\nu +\xi \right)\,\nabla (\nabla \cdot \mathbf {u} )+\mathbf {a} .$

where ${\textstyle {\frac {\mathrm {D} }{\mathrm {D} t}}}$ is the material derivative. ${\textstyle \nu ={\frac {\mu }{\rho }}}$ is the shear kinematic viscosity and ${\textstyle \xi ={\frac {\zeta }{\rho }}}$ is the bulk kinematic viscosity. The left-hand side changes in the conservation form of the Navier–Stokes momentum equation. By bringing the operator on the flow velocity on the left side, one also has:

Navier–Stokes momentum equation

with uniform shear and bulk viscosities

(convective form)

$\left({\frac {\partial }{\partial t}}+\mathbf {u} \cdot \nabla -\nu \,\nabla ^{2}-\left({\tfrac {1}{3}}\nu +\xi \right)\,\nabla (\nabla \cdot )\right)\mathbf {u} =-{\frac {1}{\rho }}\nabla p+\mathbf {a} .$

The convective acceleration term can also be written as $\mathbf {u} \cdot \nabla \mathbf {u} =(\nabla \times \mathbf {u} )\times \mathbf {u} +{\tfrac {1}{2}}\nabla \mathbf {u} ^{2},$ where the vector ${\textstyle (\nabla \times \mathbf {u} )\times \mathbf {u} }$ is known as the Lamb vector.

For the special case of an incompressible flow, the pressure constrains the flow so that the volume of fluid elements is constant: isochoric flow resulting in a solenoidal velocity field with ${\textstyle \nabla \cdot \mathbf {u} =0}$ .


## Incompressible flow

The incompressible momentum Navier–Stokes equation results from the following assumptions on the Cauchy stress tensor:

- the stress is **Galilean invariant**: it does not depend directly on the flow velocity, but only on spatial derivatives of the flow velocity. So the stress variable is the tensor gradient ${\textstyle \nabla \mathbf {u} }$ .
- the fluid is assumed to be isotropic, as with gases and simple liquids, and consequently ${\textstyle {\boldsymbol {\tau }}}$ is an isotropic tensor; furthermore, since the deviatoric stress tensor can be expressed in terms of the dynamic viscosity ${\textstyle \mu }$ : **Stokes' stress constitutive equation**  *(expression used for incompressible elastic solids)* ${\boldsymbol {\tau }}=2\mu {\boldsymbol {\varepsilon }}$ where ${\boldsymbol {\varepsilon }}={\tfrac {1}{2}}\left(\mathbf {\nabla u} +\mathbf {\nabla u} ^{\mathsf {T}}\right)$ is the rate-of-strain tensor. So this decomposition can be made explicit as: **Stokes's stress constitutive equation**  *(expression used for incompressible viscous fluids)* ${\boldsymbol {\tau }}=\mu \left[\nabla \mathbf {u} +(\nabla \mathbf {u} )^{\mathsf {T}}\right]$

This is constitutive equation is also called the **Newtonian law of viscosity**. Dynamic viscosity μ need not be constant – in incompressible flows it can depend on density and on pressure. Any equation that makes explicit one of these transport coefficient in the conservative variables is called an equation of state.

The divergence of the deviatoric stress in case of uniform viscosity is given by: $\nabla \cdot {\boldsymbol {\tau }}=2\mu \nabla \cdot {\boldsymbol {\varepsilon }}=\mu \nabla \cdot \left(\nabla \mathbf {u} +\nabla \mathbf {u} ^{\mathsf {T}}\right)=\mu \,\nabla ^{2}\mathbf {u}$ because ${\textstyle \nabla \cdot \mathbf {u} =0}$ for an incompressible fluid.

Incompressibility rules out density and pressure waves like sound or shock waves, so this simplification is not useful if these phenomena are of interest. The incompressible flow assumption typically holds well with all fluids at low Mach numbers (say up to about Mach 0.3), such as for modelling air winds at normal temperatures. the incompressible Navier–Stokes equations are best visualized by dividing for the density:

Incompressible

Navier–Stokes equations

with uniform viscosity

(convective form)

${\frac {D\mathbf {u} }{Dt}}={\frac {\partial \mathbf {u} }{\partial t}}+(\mathbf {u} \cdot \nabla )\mathbf {u} =\nu \,\nabla ^{2}\mathbf {u} -{\frac {1}{\rho }}\nabla p+{\frac {1}{\rho }}\mathbf {f}$

where ${\textstyle \nu ={\frac {\mu }{\rho }}}$ is called the kinematic viscosity. By isolating the fluid velocity, one can also state:

Incompressible

Navier–Stokes equations

with constant viscosity

(alternative convective form)

$\left({\frac {\partial }{\partial t}}+\mathbf {u} \cdot \nabla -\nu \,\nabla ^{2}\right)\mathbf {u} =-{\frac {1}{\rho }}\nabla p+{\frac {1}{\rho }}\mathbf {f} .$

If the density is constant throughout the fluid domain, or, in other words, if all fluid elements have the same density, ${\textstyle \rho }$ , then we have

Incompressible

Navier–Stokes equations with constant density and viscosity

(convective form)

${\frac {D\mathbf {u} }{Dt}}=\nu \,\nabla ^{2}\mathbf {u} -\nabla {\frac {p}{\rho }}+{\frac {1}{\rho }}\mathbf {f} ,$

where ${\textstyle {\frac {p}{\rho }}}$ is called the unit pressure head.

In incompressible flows, the pressure field satisfies the Poisson equation,

$\nabla ^{2}p=-\rho {\frac {\partial u_{i}}{\partial x_{k}}}{\frac {\partial u_{k}}{\partial x_{i}}}=-\rho {\frac {\partial ^{2}u_{i}u_{k}}{\partial x_{k}x_{i}}},$

which is obtained by taking the divergence of the momentum equations.

A laminar flow example

Velocity profile (laminar flow): $u_{x}=u(y),\quad u_{y}=0,\quad u_{z}=0$ for the x-direction, simplify the Navier–Stokes equation: $0=-{\frac {\mathrm {d} P}{\mathrm {d} x}}+\mu \left({\frac {\mathrm {d} ^{2}u}{\mathrm {d} y^{2}}}\right)$

Integrate twice to find the velocity profile with boundary conditions $y=h,\ u=0$ ; $y=-h,\ u=0$ : $u={\frac {1}{2\mu }}{\frac {\mathrm {d} P}{\mathrm {d} x}}y^{2}+Ay+B$

From this equation, substitute in the two boundary conditions to get two equations: ${\begin{aligned}0&={\frac {1}{2\mu }}{\frac {\mathrm {d} P}{\mathrm {d} x}}h^{2}+Ah+B\\0&={\frac {1}{2\mu }}{\frac {\mathrm {d} P}{\mathrm {d} x}}h^{2}-Ah+B\end{aligned}}$

Add and solve for B : $B=-{\frac {1}{2\mu }}{\frac {\mathrm {d} P}{\mathrm {d} x}}h^{2}$

Substitute and solve for A : $A=0$

Finally this gives the velocity profile: $u={\frac {1}{2\mu }}{\frac {\mathrm {d} P}{\mathrm {d} x}}\left(y^{2}-h^{2}\right)$

It is well worth observing the meaning of each term (compare to the Cauchy momentum equation):

$\overbrace {{\vphantom {\frac {}{}}}\underbrace {\frac {\partial \mathbf {u} }{\partial t}} _{\text{Variation}}+\underbrace {{\vphantom {\frac {}{}}}(\mathbf {u} \cdot \nabla )\mathbf {u} } _{\begin{smallmatrix}{\text{Convective}}\\{\text{acceleration}}\end{smallmatrix}}} ^{\text{Inertia (per volume)}}=\overbrace {{\vphantom {\frac {\partial }{\partial }}}\underbrace {{\vphantom {\frac {}{}}}-\nabla w} _{\begin{smallmatrix}{\text{Internal}}\\{\text{source}}\end{smallmatrix}}+\underbrace {{\vphantom {\frac {}{}}}\nu \nabla ^{2}\mathbf {u} } _{\text{Diffusion}}} ^{\text{Divergence of stress}}+\underbrace {{\vphantom {\frac {}{}}}\mathbf {g} } _{\begin{smallmatrix}{\text{External}}\\{\text{source}}\end{smallmatrix}}.$

The higher-order term, namely the shear stress divergence ${\textstyle \nabla \cdot {\boldsymbol {\tau }}}$ , has simply reduced to the vector Laplacian term ${\textstyle \mu \nabla ^{2}\mathbf {u} }$ . This Laplacian term can be interpreted as the difference between the velocity at a point and the mean velocity in a small surrounding volume. This implies that – for a Newtonian fluid – viscosity operates as a *diffusion of momentum*, in much the same way as the heat conduction. In fact neglecting the convection term, incompressible Navier–Stokes equations lead to a vector diffusion equation (namely Stokes equations), but in general the convection term is present, so incompressible Navier–Stokes equations belong to the class of convection–diffusion equations.

In the usual case of an external field being a conservative field: $\mathbf {g} =-\nabla \varphi$ by defining the hydraulic head: $h\equiv w+\varphi$

one can finally condense the whole source in one term, arriving to the incompressible Navier–Stokes equation with conservative external field: ${\frac {\partial \mathbf {u} }{\partial t}}+(\mathbf {u} \cdot \nabla )\mathbf {u} -\nu \,\nabla ^{2}\mathbf {u} =-\nabla h.$

The incompressible Navier–Stokes equations with uniform density and viscosity and conservative external field is the **fundamental equation of hydraulics**. The domain for these equations is commonly a 3 or fewer dimensional Euclidean space, for which an orthogonal coordinate reference frame is usually set to explicit the system of scalar partial differential equations to be solved. In 3-dimensional orthogonal coordinate systems are 3: Cartesian, cylindrical, and spherical. Expressing the Navier–Stokes vector equation in Cartesian coordinates is quite straightforward and not much influenced by the number of dimensions of the euclidean space employed, and this is the case also for the first-order terms (like the variation and convection ones) also in non-cartesian orthogonal coordinate systems. But for the higher order terms (the two coming from the divergence of the deviatoric stress that distinguish Navier–Stokes equations from Euler equations) some tensor calculus is required for deducing an expression in non-cartesian orthogonal coordinate systems. A special case of the fundamental equation of hydraulics is the Bernoulli's equation.

The incompressible Navier–Stokes equation is composite, the sum of two orthogonal equations, ${\begin{aligned}{\frac {\partial \mathbf {u} }{\partial t}}&=\Pi ^{S}\left(-(\mathbf {u} \cdot \nabla )\mathbf {u} +\nu \,\nabla ^{2}\mathbf {u} \right)+\mathbf {f} ^{S}\\\rho ^{-1}\,\nabla p&=\Pi ^{I}\left(-(\mathbf {u} \cdot \nabla )\mathbf {u} +\nu \,\nabla ^{2}\mathbf {u} \right)+\mathbf {f} ^{I}\end{aligned}}$ where ${\textstyle \Pi ^{S}}$ and ${\textstyle \Pi ^{I}}$ are solenoidal and irrotational projection operators satisfying ${\textstyle \Pi ^{S}+\Pi ^{I}=1}$ , and ${\textstyle \mathbf {f} ^{S}}$ and ${\textstyle \mathbf {f} ^{I}}$ are the non-conservative and conservative parts of the body force. This result follows from the Helmholtz theorem (also known as the fundamental theorem of vector calculus). The first equation is a pressureless governing equation for the velocity, while the second equation for the pressure is a functional of the velocity and is related to the pressure Poisson equation.

The explicit functional form of the projection operator in 3D is found from the Helmholtz theorem: $\Pi ^{S}\,\mathbf {F} (\mathbf {r} )={\frac {1}{4\pi }}\nabla \times \int {\frac {\nabla ^{\prime }\times \mathbf {F} (\mathbf {r} ')}{|\mathbf {r} -\mathbf {r} '|}}\,\mathrm {d} V',\quad \Pi ^{I}=1-\Pi ^{S}$ with a similar structure in 2D. Thus the governing equation is an integro-differential equation similar to Coulomb's and Biot–Savart's law, not convenient for numerical computation.

An equivalent weak or variational form of the equation, proved to produce the same velocity solution as the Navier–Stokes equation, is given by, $\left(\mathbf {w} ,{\frac {\partial \mathbf {u} }{\partial t}}\right)=-{\bigl (}\mathbf {w} ,\left(\mathbf {u} \cdot \nabla \right)\mathbf {u} {\bigr )}-\nu \left(\nabla \mathbf {w} :\nabla \mathbf {u} \right)+\left(\mathbf {w} ,\mathbf {f} ^{S}\right)$

for divergence-free test functions ${\textstyle \mathbf {w} }$ satisfying appropriate boundary conditions. Here, the projections are accomplished by the orthogonality of the solenoidal and irrotational function spaces. The discrete form of this is eminently suited to finite element computation of divergence-free flow, as we shall see in the next section. There, one will be able to address the question, "How does one specify pressure-driven (Poiseuille) problems with a pressureless governing equation?".

The absence of pressure forces from the governing velocity equation demonstrates that the equation is not a dynamic one, but rather a kinematic equation where the divergence-free condition serves the role of a conservation equation. This would seem to refute the frequent statements that the incompressible pressure enforces the divergence-free condition.

### Weak form of the incompressible Navier–Stokes equations

#### Strong form

Consider the incompressible Navier–Stokes equations for a Newtonian fluid of constant density ${\textstyle \rho }$ in a domain $\Omega \subset \mathbb {R} ^{d}\quad (d=2,3)$ with boundary $\partial \Omega =\Gamma _{D}\cup \Gamma _{N},$ being ${\textstyle \Gamma _{D}}$ and ${\textstyle \Gamma _{N}}$ portions of the boundary where respectively a Dirichlet and a Neumann boundary condition is applied ( ${\textstyle \Gamma _{D}\cap \Gamma _{N}=\emptyset }$ ): ${\begin{cases}\rho {\dfrac {\partial \mathbf {u} }{\partial t}}+\rho (\mathbf {u} \cdot \nabla )\mathbf {u} -\nabla \cdot {\boldsymbol {\sigma }}(\mathbf {u} ,p)=\mathbf {f} &{\text{ in }}\Omega \times (0,T)\\\nabla \cdot \mathbf {u} =0&{\text{ in }}\Omega \times (0,T)\\\mathbf {u} =\mathbf {g} &{\text{ on }}\Gamma _{D}\times (0,T)\\{\boldsymbol {\sigma }}(\mathbf {u} ,p){\hat {\mathbf {n} }}=\mathbf {h} &{\text{ on }}\Gamma _{N}\times (0,T)\\\mathbf {u} (0)=\mathbf {u} _{0}&{\text{ in }}\Omega \times \{0\}\end{cases}}$ ${\textstyle \mathbf {u} }$ is the fluid velocity, ${\textstyle p}$ the fluid pressure, ${\textstyle \mathbf {f} }$ a given forcing term, ${\hat {\mathbf {n} }}$ the outward directed unit normal vector to ${\textstyle \Gamma _{N}}$ , and ${\textstyle {\boldsymbol {\sigma }}(\mathbf {u} ,p)}$ the viscous stress tensor defined as: ${\boldsymbol {\sigma }}(\mathbf {u} ,p)=-p\mathbf {I} +2\mu {\boldsymbol {\varepsilon }}(\mathbf {u} ).$ Let ${\textstyle \mu }$ be the dynamic viscosity of the fluid, ${\textstyle \mathbf {I} }$ the second-order identity tensor and ${\textstyle {\boldsymbol {\varepsilon }}(\mathbf {u} )}$ the strain-rate tensor defined as: ${\boldsymbol {\varepsilon }}(\mathbf {u} )={\tfrac {1}{2}}\left(\left(\nabla \mathbf {u} \right)+\left(\nabla \mathbf {u} \right)^{\mathsf {T}}\right).$ The functions ${\textstyle \mathbf {g} }$ and ${\textstyle \mathbf {h} }$ are given Dirichlet and Neumann boundary data, while ${\textstyle \mathbf {u} _{0}}$ is the initial condition. The first equation is the momentum balance equation, while the second represents the mass conservation, namely the continuity equation. Assuming constant dynamic viscosity, using the vectorial identity $\nabla \cdot \left(\nabla \mathbf {f} \right)^{\mathsf {T}}=\nabla (\nabla \cdot \mathbf {f} )$ and exploiting mass conservation, the divergence of the total stress tensor in the momentum equation can also be expressed as: ${\begin{aligned}\nabla \cdot {\boldsymbol {\sigma }}(\mathbf {u} ,p)&=\nabla \cdot \left(-p\mathbf {I} +2\mu {\boldsymbol {\varepsilon }}(\mathbf {u} )\right)\\&=-\nabla p+2\mu \nabla \cdot {\boldsymbol {\varepsilon }}(\mathbf {u} )\\&=-\nabla p+2\mu \nabla \cdot \left[{\tfrac {1}{2}}\left(\left(\nabla \mathbf {u} \right)+\left(\nabla \mathbf {u} \right)^{\mathsf {T}}\right)\right]\\&=-\nabla p+\mu \left(\Delta \mathbf {u} +\nabla \cdot \left(\nabla \mathbf {u} \right)^{\mathsf {T}}\right)\\&=-\nabla p+\mu {\bigl (}\Delta \mathbf {u} +\nabla \underbrace {(\nabla \cdot \mathbf {u} )} _{=0}{\bigr )}=-\nabla p+\mu \,\Delta \mathbf {u} .\end{aligned}}$ Moreover, note that the Neumann boundary conditions can be rearranged as: ${\boldsymbol {\sigma }}(\mathbf {u} ,p){\hat {\mathbf {n} }}={\bigl (}-p\mathbf {I} +2\mu {\boldsymbol {\varepsilon }}(\mathbf {u} ){\bigr )}{\hat {\mathbf {n} }}=-p{\hat {\mathbf {n} }}+\mu {\frac {\partial {\boldsymbol {u}}}{\partial {\hat {\mathbf {n} }}}}.$

#### Weak form

In order to find the weak form of the Navier–Stokes equations, firstly, consider the momentum equation $\rho {\frac {\partial \mathbf {u} }{\partial t}}-\mu \Delta \mathbf {u} +\rho (\mathbf {u} \cdot \nabla )\mathbf {u} +\nabla p=\mathbf {f}$ multiply it for a test function ${\textstyle \mathbf {v} }$ , defined in a suitable space ${\textstyle V}$ , and integrate both members with respect to the domain ${\textstyle \Omega }$ : $\int \limits _{\Omega }\rho {\frac {\partial \mathbf {u} }{\partial t}}\cdot \mathbf {v} -\int \limits _{\Omega }\mu \Delta \mathbf {u} \cdot \mathbf {v} +\int \limits _{\Omega }\rho (\mathbf {u} \cdot \nabla )\mathbf {u} \cdot \mathbf {v} +\int \limits _{\Omega }\nabla p\cdot \mathbf {v} =\int \limits _{\Omega }\mathbf {f} \cdot \mathbf {v}$ Counter-integrating by parts the diffusive and the pressure terms and by using Gauss's theorem: ${\begin{aligned}-\int \limits _{\Omega }\mu \Delta \mathbf {u} \cdot \mathbf {v} &=\int \limits _{\Omega }\mu \nabla \mathbf {u} \cdot \nabla \mathbf {v} -\int \limits _{\partial \Omega }\mu {\frac {\partial \mathbf {u} }{\partial {\hat {\mathbf {n} }}}}\cdot \mathbf {v} \\\int \limits _{\Omega }\nabla p\cdot \mathbf {v} &=-\int \limits _{\Omega }p\nabla \cdot \mathbf {v} +\int \limits _{\partial \Omega }p\mathbf {v} \cdot {\hat {\mathbf {n} }}\end{aligned}}$

Using these relations, one gets: $\int \limits _{\Omega }\rho {\dfrac {\partial \mathbf {u} }{\partial t}}\cdot \mathbf {v} +\int \limits _{\Omega }\mu \nabla \mathbf {u} \cdot \nabla \mathbf {v} +\int \limits _{\Omega }\rho (\mathbf {u} \cdot \nabla )\mathbf {u} \cdot \mathbf {v} -\int \limits _{\Omega }p\nabla \cdot \mathbf {v} =\int \limits _{\Omega }\mathbf {f} \cdot \mathbf {v} +\int \limits _{\partial \Omega }\left(\mu {\frac {\partial \mathbf {u} }{\partial {\hat {\mathbf {n} }}}}-p{\hat {\mathbf {n} }}\right)\cdot \mathbf {v} \quad \forall \mathbf {v} \in V.$ In the same fashion, the continuity equation is multiplied for a test function ${\textstyle q}$ belonging to a space ${\textstyle Q}$ and integrated in the domain ${\textstyle \Omega }$ : $\int \limits _{\Omega }q\nabla \cdot \mathbf {u} =0.\quad \forall q\in Q.$ The space functions are chosen as follows: ${\begin{aligned}V=\left[H_{0}^{1}(\Omega )\right]^{d}&=\left\{\mathbf {v} \in \left[H^{1}(\Omega )\right]^{d}:\quad \mathbf {v} =\mathbf {0} {\text{ on }}\Gamma _{D}\right\},\\Q&=L^{2}(\Omega )\end{aligned}}$ Considering that the test function ${\textstyle \mathbf {v} }$ vanishes on the Dirichlet boundary and considering the Neumann condition, the integral on the boundary can be rearranged as: $\int \limits _{\partial \Omega }\left(\mu {\frac {\partial \mathbf {u} }{\partial {\hat {\mathbf {n} }}}}-p{\hat {\mathbf {n} }}\right)\cdot \mathbf {v} =\underbrace {\int \limits _{\Gamma _{D}}\left(\mu {\frac {\partial \mathbf {u} }{\partial {\hat {\mathbf {n} }}}}-p{\hat {\mathbf {n} }}\right)\cdot \mathbf {v} } _{\mathbf {v} =\mathbf {0} {\text{ on }}\Gamma _{D}\ }+\int \limits _{\Gamma _{N}}\underbrace {{\vphantom {\int \limits _{\Gamma _{N}}}}\left(\mu {\frac {\partial \mathbf {u} }{\partial {\hat {\mathbf {n} }}}}-p{\hat {\mathbf {n} }}\right)} _{=\mathbf {h} {\text{ on }}\Gamma _{N}}\cdot \mathbf {v} =\int \limits _{\Gamma _{N}}\mathbf {h} \cdot \mathbf {v} .$ Having this in mind, the weak formulation of the Navier–Stokes equations is expressed as: ${\begin{aligned}&{\text{find }}\mathbf {u} \in L^{2}\left(\mathbb {R} ^{+}\;\left[H^{1}(\Omega )\right]^{d}\right)\cap C^{0}\left(\mathbb {R} ^{+}\;\left[L^{2}(\Omega )\right]^{d}\right){\text{ such that: }}\\[5pt]&\quad {\begin{cases}\displaystyle \int \limits _{\Omega }\rho {\dfrac {\partial \mathbf {u} }{\partial t}}\cdot \mathbf {v} +\int \limits _{\Omega }\mu \nabla \mathbf {u} \cdot \nabla \mathbf {v} +\int \limits _{\Omega }\rho (\mathbf {u} \cdot \nabla )\mathbf {u} \cdot \mathbf {v} -\int \limits _{\Omega }p\nabla \cdot \mathbf {v} =\int \limits _{\Omega }\mathbf {f} \cdot \mathbf {v} +\int \limits _{\Gamma _{N}}\mathbf {h} \cdot \mathbf {v} \quad \forall \mathbf {v} \in V,\\\displaystyle \int \limits _{\Omega }q\nabla \cdot \mathbf {u} =0\quad \forall q\in Q.\end{cases}}\end{aligned}}$

### Discrete velocity

With partitioning of the problem domain and defining basis functions on the partitioned domain, the discrete form of the governing equation is $\left(\mathbf {w} _{i},{\frac {\partial \mathbf {u} _{j}}{\partial t}}\right)=-{\bigl (}\mathbf {w} _{i},\left(\mathbf {u} \cdot \nabla \right)\mathbf {u} _{j}{\bigr )}-\nu \left(\nabla \mathbf {w} _{i}:\nabla \mathbf {u} _{j}\right)+\left(\mathbf {w} _{i},\mathbf {f} ^{S}\right).$

It is desirable to choose basis functions that reflect the essential feature of incompressible flow – the elements must be divergence-free. While the velocity is the variable of interest, the existence of the stream function or vector potential is necessary by the Helmholtz theorem. Further, to determine fluid flow in the absence of a pressure gradient, one can specify the difference of stream function values across a 2D channel, or the line integral of the tangential component of the vector potential around the channel in 3D, the flow being given by Stokes' theorem. Discussion will be restricted to 2D in the following.

We further restrict discussion to continuous Hermite finite elements which have at least first-derivative degrees-of-freedom. With this, one can draw a large number of candidate triangular and rectangular elements from the plate-bending literature. These elements have derivatives as components of the gradient. In 2D, the gradient and curl of a scalar are clearly orthogonal, given by the expressions, ${\begin{aligned}\nabla \varphi &=\left({\frac {\partial \varphi }{\partial x}},\,{\frac {\partial \varphi }{\partial y}}\right)^{\mathsf {T}},\\[5pt]\nabla \times \varphi &=\left({\frac {\partial \varphi }{\partial y}},\,-{\frac {\partial \varphi }{\partial x}}\right)^{\mathsf {T}}.\end{aligned}}$

Adopting continuous plate-bending elements, interchanging the derivative degrees-of-freedom and changing the sign of the appropriate one gives many families of stream function elements.

Taking the curl of the scalar stream function elements gives divergence-free velocity elements. The requirement that the stream function elements be continuous assures that the normal component of the velocity is continuous across element interfaces, all that is necessary for vanishing divergence on these interfaces.

Boundary conditions are simple to apply. The stream function is constant on no-flow surfaces, with no-slip velocity conditions on surfaces. Stream function differences across open channels determine the flow. No boundary conditions are necessary on open boundaries, though consistent values may be used with some problems. These are all Dirichlet conditions.

The algebraic equations to be solved are simple to set up, but of course are non-linear, requiring iteration of the linearized equations.

Similar considerations apply to three-dimensions, but extension from 2D is not immediate because of the vector nature of the potential, and there exists no simple relation between the gradient and the curl as was the case in 2D.

### Pressure recovery

Recovering pressure from the velocity field is easy. The discrete weak equation for the pressure gradient is, $(\mathbf {g} _{i},\nabla p)=-{\bigl (}\mathbf {g} _{i},\left(\mathbf {u} \cdot \nabla \right)\mathbf {u} _{j}{\bigr )}-\nu \left(\nabla \mathbf {g} _{i}:\nabla \mathbf {u} _{j}\right)+\left(\mathbf {g} _{i},\mathbf {f} ^{I}\right)$

where the test/weight functions are irrotational. Any conforming scalar finite element may be used. However, the pressure gradient field may also be of interest. In this case, one can use scalar Hermite elements for the pressure. For the test/weight functions ${\textstyle \mathbf {g} _{i}}$ one would choose the irrotational vector elements obtained from the gradient of the pressure element.


## Non-inertial frame of reference

The rotating frame of reference introduces some interesting pseudo-forces into the equations through the material derivative term. Consider a stationary inertial frame of reference ${\textstyle K}$  , and a non-inertial frame of reference ${\textstyle K'}$ , which is translating with velocity ${\textstyle \mathbf {U} (t)}$ and rotating with angular velocity ${\textstyle \Omega (t)}$ with respect to the stationary frame. The Navier–Stokes equation observed from the non-inertial frame then becomes

Navier–Stokes momentum equation in non-inertial frame

${\begin{aligned}\rho \left({\frac {\partial \mathbf {u} }{\partial t}}+(\mathbf {u} \cdot \nabla )\mathbf {u} \right)=&-\nabla p+\nabla \cdot \left(\mu \left[\nabla \mathbf {u} +(\nabla \mathbf {u} )^{\mathsf {T}}-{\tfrac {2}{3}}(\nabla \cdot \mathbf {u} )\mathbf {I} \right]\right)+\nabla [\zeta (\nabla \cdot \mathbf {u} )]+\rho \mathbf {f} \\&-\rho \left[2\mathbf {\Omega } \times \mathbf {u} +\mathbf {\Omega } \times (\mathbf {\Omega } \times \mathbf {x} )+{\frac {\mathrm {d} \mathbf {U} }{\mathrm {d} t}}+{\frac {\mathrm {d} \mathbf {\Omega } }{\mathrm {d} t}}\times \mathbf {x} \right]\end{aligned}}$

Here ${\textstyle \mathbf {x} }$ and ${\textstyle \mathbf {u} }$ are measured in the non-inertial frame. The first term in the parenthesis represents Coriolis acceleration, the second term is due to centrifugal acceleration, the third is due to the linear acceleration of ${\textstyle K'}$ with respect to ${\textstyle K}$ and the fourth term is due to the angular acceleration of ${\textstyle K'}$ with respect to ${\textstyle K}$ .


## Other equations

The Navier–Stokes equations are strictly a statement of the balance of momentum. To fully describe fluid flow, more information is needed, how much depending on the assumptions made. This additional information may include boundary data (no-slip, capillary surface, etc.), conservation of mass, balance of energy, and/or an equation of state.

### Continuity equation for incompressible fluid

Regardless of the flow assumptions, a statement of the conservation of mass is generally necessary. This is achieved through the mass continuity equation, as discussed above in the "General continuum equations" within this article, as follows: ${\begin{aligned}{\frac {\mathbf {D} m}{\mathbf {Dt} }}&={\iiint \limits _{V}}\left({{\frac {\mathbf {D} \rho }{\mathbf {Dt} }}+\rho (\nabla \cdot \mathbf {u} )}\right)dV\\{\frac {\mathbf {D} \rho }{\mathbf {Dt} }}+\rho (\nabla \cdot {\mathbf {u} })&={\frac {\partial \rho }{\partial t}}+({\nabla \rho })\cdot {\mathbf {u} }+{\rho }(\nabla \cdot \mathbf {u} )={\frac {\partial \rho }{\partial t}}+\nabla \cdot ({\rho \mathbf {u} })=0\end{aligned}}$ A fluid media for which the density $\rho$ is constant is called *incompressible*. Therefore, the rate of change of $\rho$ with respect to time ${\textstyle {\frac {\partial \rho }{\partial t}}}$ and the gradient of density ${\textstyle \nabla \rho }$ are equal to zero. In this case the general equation of continuity, ${\textstyle {\frac {\partial \rho }{\partial t}}+\nabla \cdot ({\rho \mathbf {u} })=0}$ , reduces to: $\rho (\nabla {\cdot }{\mathbf {u} })=0$ Furthermore, assuming that $\rho \neq 0$ means that the right-hand side of the equation (zero) is divisible by density $\rho$ . Therefore, the continuity equation for an incompressible fluid reduces further to: $(\nabla {\cdot {\mathbf {u} }})=0$ This relationship, ${\textstyle (\nabla {\cdot {\mathbf {u} }})=0}$ , identifies that the divergence of the flow velocity vector $\mathbf {u}$ is equal to zero, which means that for an incompressible fluid the flow velocity field is a solenoidal vector field or a divergence-free vector field. Note that this relationship can be expanded upon due to its uniqueness with the vector Laplace operator $\nabla ^{2}\mathbf {u} =\nabla (\nabla \cdot \mathbf {u} )-\nabla \times (\nabla \times \mathbf {u} )$ , and vorticity ${\boldsymbol {\omega }}=\nabla \times \mathbf {u}$ which is now expressed like so, for an incompressible fluid: $\nabla ^{2}\mathbf {u} =-{\bigl (}\nabla \times (\nabla \times \mathbf {u} ){\bigr )}=-(\nabla \times {\boldsymbol {\omega }})$
