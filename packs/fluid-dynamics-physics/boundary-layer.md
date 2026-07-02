---
title: "Boundary layer"
source: https://en.wikipedia.org/wiki/Boundary_layer
domain: fluid-dynamics-physics
license: CC-BY-SA-4.0
tags: fluid dynamics, reynolds number, boundary layer, compressible flow
fetched: 2026-07-02
---

# Boundary layer

In physics and fluid mechanics, a **boundary layer** is the thin layer of fluid in the immediate vicinity of a bounding surface formed by the fluid flowing along the surface. The fluid's interaction with the wall induces a no-slip boundary condition (zero velocity at the wall). The flow velocity then monotonically increases above the surface until it returns to the bulk flow velocity. The thin layer consisting of fluid whose velocity has not yet returned to the bulk flow velocity is called the velocity boundary layer.

The air next to a human is heated, resulting in gravity-induced convective airflow, which results in both a velocity and thermal boundary layer. A breeze disrupts the boundary layer, and hair and clothing protect it, making the human feel cooler or warmer. On an aircraft wing, the velocity boundary layer is the part of the flow close to the wing, where viscous forces distort the surrounding non-viscous flow. In the Earth's atmosphere, the atmospheric boundary layer is the air layer (~ 1 km) near the ground. It is affected by the surface; day-night heat flows caused by the sun heating the ground, moisture, or momentum transfer to or from the surface.

## Types of boundary layers

Laminar boundary layers can be loosely classified according to their structure and the circumstances under which they are created. The thin shear layer which develops on an oscillating body is an example of a Stokes boundary layer, while the Blasius boundary layer refers to the well-known similarity solution near an attached flat plate held in an oncoming unidirectional flow and Falkner–Skan boundary layer, a generalization of Blasius profile. When a fluid rotates and viscous forces are balanced by the Coriolis effect (rather than convective inertia), an Ekman layer forms. In the theory of heat transfer, a thermal boundary layer occurs. A surface can have multiple types of boundary layer simultaneously.

The viscous nature of airflow reduces the local velocities on a surface and is responsible for skin friction. The layer of air over the wing's surface that is slowed down or stopped by viscosity, is the boundary layer. There are two different types of boundary layer flow: laminar and turbulent.

**Laminar boundary layer flow**

The laminar boundary is a very smooth flow, while the turbulent boundary layer contains swirls or "eddies." The laminar flow creates less skin friction drag than the turbulent flow, but is less stable. Boundary layer flow over a wing surface begins as a smooth laminar flow. As the flow continues back from the leading edge, the laminar boundary layer increases in thickness.

**Turbulent boundary layer flow**

At some distance back from the leading edge, the smooth laminar flow breaks down and transitions to a turbulent flow. From a drag standpoint, it is advisable to have the transition from laminar to turbulent flow as far aft on the wing as possible, or have a large amount of the wing surface within the laminar portion of the boundary layer. The low energy laminar flow, however, tends to break down more suddenly than the turbulent layer.

## The Prandtl boundary layer concept

The aerodynamic boundary layer was first hypothesized by Ludwig Prandtl in a paper presented on August 12, 1904, at the third International Congress of Mathematicians in Heidelberg, Germany. It simplifies the equations of fluid flow by dividing the flow field into two areas: one inside the boundary layer, dominated by viscosity and creating the majority of drag experienced by the boundary body; and one outside the boundary layer, where viscosity can be neglected without significant effects on the solution. This allows a closed-form solution for the flow in both areas by making significant simplifications of the full Navier–Stokes equations. The same hypothesis is applicable to other fluids (besides air) with moderate to low viscosity such as water. For the case where there is a temperature difference between the surface and the bulk fluid, it is found that the majority of the heat transfer to and from a body takes place in the vicinity of the velocity boundary layer. This again allows the equations to be simplified in the flow field outside the boundary layer. The pressure distribution throughout the boundary layer in the direction normal to the surface (such as an airfoil) remains relatively constant throughout the boundary layer, and is the same as on the surface itself.

The thickness of the velocity boundary layer is normally defined as the distance from the solid body to the point at which the viscous flow velocity is 99% of the freestream velocity (the surface velocity of an inviscid flow). Displacement thickness is an alternative definition stating that the boundary layer represents a deficit in mass flow compared to inviscid flow with slip at the wall. It is the distance by which the wall would have to be displaced in the inviscid case to give the same total mass flow as the viscous case. The no-slip condition requires the flow velocity at the surface of a solid object be zero and the fluid temperature be equal to the temperature of the surface. The flow velocity will then increase rapidly within the boundary layer, governed by the boundary layer equations, below.

The thermal boundary layer thickness is similarly the distance from the body at which the temperature is 99% of the freestream temperature. The ratio of the two thicknesses is governed by the Prandtl number. If the Prandtl number is 1, the two boundary layers are the same thickness. If the Prandtl number is greater than 1, the thermal boundary layer is thinner than the velocity boundary layer. If the Prandtl number is less than 1, which is the case for air at standard conditions, the thermal boundary layer is thicker than the velocity boundary layer.

In high-performance designs, such as gliders and commercial aircraft, much attention is paid to controlling the behavior of the boundary layer to minimize drag. Two effects have to be considered. First, the boundary layer adds to the effective thickness of the body, through the displacement thickness, hence increasing the pressure drag. Secondly, the shear forces at the surface of the wing create skin friction drag.

At high Reynolds numbers, typical of full-sized aircraft, it is desirable to have a laminar boundary layer. This results in a lower skin friction due to the characteristic velocity profile of laminar flow. However, the boundary layer inevitably thickens and becomes less stable as the flow develops along the body, and eventually becomes turbulent, the process known as boundary layer transition. One way of dealing with this problem is to suck the boundary layer away through a porous surface (see Boundary layer suction). This can reduce drag, but is usually impractical due to its mechanical complexity and the power required to move the air and dispose of it. Natural laminar flow (NLF) techniques push the boundary layer transition aft by reshaping the airfoil or fuselage so that its thickest point is more aft and less thick. This reduces the velocities in the leading part and the same Reynolds number is achieved with a greater length.

At lower Reynolds numbers, such as those seen with model aircraft, it is relatively easy to maintain laminar flow. This gives low skin friction, which is desirable. However, the same velocity profile which gives the laminar boundary layer its low skin friction also causes it to be badly affected by adverse pressure gradients. As the pressure begins to recover over the rear part of the wing chord, a laminar boundary layer will tend to separate from the surface. Such flow separation causes a large increase in the pressure drag, since it greatly increases the effective size of the wing section. In these cases, it can be advantageous to deliberately trip the boundary layer into turbulence at a point prior to the location of laminar separation, using a turbulator. The fuller velocity profile of the turbulent boundary layer allows it to sustain the adverse pressure gradient without separating. Thus, although the skin friction is increased, overall drag is decreased. This is the principle behind the dimpling on golf balls, as well as vortex generators on aircraft. Special wing sections have also been designed which tailor the pressure recovery so laminar separation is reduced or even eliminated. This represents an optimum compromise between the pressure drag from flow separation and skin friction from induced turbulence.

When using half-models in wind tunnels, a peniche is sometimes used to reduce or eliminate the effect of the boundary layer.

## Boundary layer equations

The deduction of the **boundary layer equations** was one of the most important advances in fluid dynamics. Using an order of magnitude analysis, the well-known governing Navier–Stokes equations of viscous fluid flow can be greatly simplified within the boundary layer. Notably, the characteristic of the partial differential equations (PDE) becomes parabolic, rather than the elliptical form of the full Navier–Stokes equations. This greatly simplifies the solution of the equations. By making the boundary layer approximation, the flow is divided into an inviscid portion (which is easy to solve by a number of methods) and the boundary layer, which is governed by an easier to solve PDE. The continuity and Navier–Stokes equations for a two-dimensional steady incompressible flow in Cartesian coordinates are given by

${\partial u \over \partial x}+{\partial \upsilon \over \partial y}=0$

$u{\partial u \over \partial x}+\upsilon {\partial u \over \partial y}=-{1 \over \rho }{\partial p \over \partial x}+{\nu }\left({\partial ^{2}u \over \partial x^{2}}+{\partial ^{2}u \over \partial y^{2}}\right)$

$u{\partial \upsilon \over \partial x}+\upsilon {\partial \upsilon \over \partial y}=-{1 \over \rho }{\partial p \over \partial y}+{\nu }\left({\partial ^{2}\upsilon \over \partial x^{2}}+{\partial ^{2}\upsilon \over \partial y^{2}}\right)$

where u and $\upsilon$ are the velocity components, $\rho$ is the density, p is the pressure, and $\nu$ is the kinematic viscosity of the fluid at a point.

The approximation states that, for a sufficiently high Reynolds number the flow over a surface can be divided into an outer region of inviscid flow unaffected by viscosity (the majority of the flow), and a region close to the surface where viscosity is important (the boundary layer). Let u and $\upsilon$ be streamwise and transverse (wall normal) velocities respectively inside the boundary layer. Using scale analysis, it can be shown that the above equations of motion reduce within the boundary layer to become

$u{\partial u \over \partial x}+\upsilon {\partial u \over \partial y}=-{1 \over \rho }{\partial p \over \partial x}+{\nu }{\partial ^{2}u \over \partial y^{2}}$

${1 \over \rho }{\partial p \over \partial y}=0$

and if the fluid is incompressible (as liquids are under standard conditions):

${\partial u \over \partial x}+{\partial \upsilon \over \partial y}=0$

The order of magnitude analysis assumes the streamwise length scale significantly larger than the transverse length scale inside the boundary layer. It follows that variations in properties in the streamwise direction are generally much lower than those in the wall normal direction. Apply this to the continuity equation shows that $\upsilon$ , the wall normal velocity, is small compared with u the streamwise velocity.

Since the static pressure p is independent of y , then pressure at the edge of the boundary layer is the pressure throughout the boundary layer at a given streamwise position. The external pressure may be obtained through an application of Bernoulli's equation. Let U be the fluid velocity outside the boundary layer, where u and U are both parallel. This gives upon substituting for p the following result

$u{\partial u \over \partial x}+\upsilon {\partial u \over \partial y}=U{\frac {dU}{dx}}+{\nu }{\partial ^{2}u \over \partial y^{2}}$

For a flow in which the static pressure p also does not change in the direction of the flow

${\frac {dp}{dx}}=0$

so U remains constant.

Therefore, the equation of motion simplifies to become

$u{\partial u \over \partial x}+\upsilon {\partial u \over \partial y}={\nu }{\partial ^{2}u \over \partial y^{2}}$

These approximations are used in a variety of practical flow problems of scientific and engineering interest. The above analysis is for any instantaneous laminar or turbulent boundary layer, but is used mainly in laminar flow studies since the mean flow is also the instantaneous flow because there are no velocity fluctuations present. This simplified equation is a parabolic PDE and can be solved using a similarity solution often referred to as the Blasius boundary layer.

### Prandtl's transposition theorem

Prandtl observed that from any solution $u(x,y,t),\ v(x,y,t)$ which satisfies the boundary layer equations, further solution $u^{*}(x,y,t),\ v^{*}(x,y,t)$ , which is also satisfying the boundary layer equations, can be constructed by writing

$u^{*}(x,y,t)=u(x,y+f(x),t),\quad v^{*}(x,y,t)=v(x,y+f(x),t)-f'(x)u(x,y+f(x),t)$

where $f(x)$ is arbitrary. Since the solution is not unique from mathematical perspective, to the solution can be added any one of an infinite set of eigenfunctions as shown by Stewartson and Paul A. Libby.

### Von Kármán momentum integral

Von Kármán derived the integral equation by integrating the boundary layer equation across the boundary layer in 1921. The equation is

${\frac {\tau _{w}}{\rho U^{2}}}={\frac {1}{U^{2}}}{\frac {\partial }{\partial t}}(U\delta _{1})+{\frac {\partial \delta _{2}}{\partial x}}+{\frac {2\delta _{2}+\delta _{1}}{U}}{\frac {\partial U}{\partial x}}+{\frac {v_{w}}{U}}$

where

$\tau _{w}=\mu \left({\frac {\partial u}{\partial y}}\right)_{y=0},\quad v_{w}=v(x,0,t),\quad \delta _{1}=\int _{0}^{\infty }\left(1-{\frac {u}{U}}\right)\,dy,\quad \delta _{2}=\int _{0}^{\infty }{\frac {u}{U}}\left(1-{\frac {u}{U}}\right)\,dy$

$\tau _{w}$

is the wall shear stress,

$v_{w}$

is the suction/injection velocity at the wall,

$\delta _{1}$

is the displacement thickness and

$\delta _{2}$

is the momentum thickness.

Kármán–Pohlhausen Approximation

is derived from this equation.

### Energy integral

The energy integral was derived by Wieghardt.

${\frac {2\varepsilon }{\rho U^{3}}}={\frac {1}{U}}{\frac {\partial }{\partial t}}(\delta _{1}+\delta _{2})+{\frac {2\delta _{2}}{U^{2}}}{\frac {\partial U}{\partial t}}+{\frac {1}{U^{3}}}{\frac {\partial }{\partial x}}(U^{3}\delta _{3})+{\frac {v_{w}}{U}}$

where

$\varepsilon =\int _{0}^{\infty }\mu \left({\frac {\partial u}{\partial y}}\right)^{2}dy,\quad \delta _{3}=\int _{0}^{\infty }{\frac {u}{U}}\left(1-{\frac {u^{2}}{U^{2}}}\right)\,dy$

$\varepsilon$

is the energy dissipation rate due to viscosity across the boundary layer and

$\delta _{3}$

is the energy thickness.

### Von Mises transformation

For steady two-dimensional boundary layers, von Mises introduced a transformation which takes x and $\psi$ (stream function) as independent variables instead of x and y and uses a dependent variable $\chi =U^{2}-u^{2}$ instead of u . The boundary layer equation then become

${\frac {\partial \chi }{\partial x}}=\nu {\sqrt {U^{2}-\chi }}\,{\frac {\partial ^{2}\chi }{\partial \psi ^{2}}}$

The original variables are recovered from

$y=\int {\sqrt {U^{2}-\chi }}\,d\psi ,\quad u={\sqrt {U^{2}-\chi }},\quad v=u\int {\frac {\partial }{\partial x}}\left({\frac {1}{u}}\right)\,d\psi .$

This transformation is later extended to compressible boundary layer by von Kármán and HS Tsien.

### Crocco's transformation

For steady two-dimensional compressible boundary layer, Luigi Crocco introduced a transformation which takes x and u as independent variables instead of x and y and uses a dependent variable $\tau =\mu \partial u/\partial y$ (shear stress) instead of u . The boundary layer equation then becomes

${\begin{aligned}&\mu \rho u{\frac {\partial }{\partial x}}\left({\frac {1}{\tau }}\right)+{\frac {\partial ^{2}\tau }{\partial u^{2}}}-\mu {\frac {dp}{dx}}{\frac {\partial }{\partial u}}\left({\frac {1}{\tau }}\right)=0,\\[5pt]&{\text{if }}{\frac {dp}{dx}}=0,{\text{ then }}{\frac {\mu \rho }{\tau ^{2}}}{\frac {\partial \tau }{\partial x}}={\frac {1}{u}}{\frac {\partial ^{2}\tau }{\partial u^{2}}}.\end{aligned}}$

The original coordinate is recovered from

$y=\mu \int {\frac {du}{\tau }}.$

## Turbulent boundary layers

The treatment of turbulent boundary layers is far more difficult due to the time-dependent variation of the flow properties. One of the most widely used techniques in which turbulent flows are tackled is to apply Reynolds decomposition. Here the instantaneous flow properties are decomposed into a mean and fluctuating component with the assumption that the mean of the fluctuating component is always zero. Applying this technique to the boundary layer equations gives the full turbulent boundary layer equations not often given in literature:

${\partial {\overline {u}} \over \partial x}+{\partial {\overline {v}} \over \partial y}=0$

${\overline {u}}{\partial {\overline {u}} \over \partial x}+{\overline {v}}{\partial {\overline {u}} \over \partial y}=-{1 \over \rho }{\partial {\overline {p}} \over \partial x}+\nu \left({\partial ^{2}{\overline {u}} \over \partial x^{2}}+{\partial ^{2}{\overline {u}} \over \partial y^{2}}\right)-{\frac {\partial }{\partial y}}({\overline {u'v'}})-{\frac {\partial }{\partial x}}({\overline {u'^{2}}})$

${\overline {u}}{\partial {\overline {v}} \over \partial x}+{\overline {v}}{\partial {\overline {v}} \over \partial y}=-{1 \over \rho }{\partial {\overline {p}} \over \partial y}+\nu \left({\partial ^{2}{\overline {v}} \over \partial x^{2}}+{\partial ^{2}{\overline {v}} \over \partial y^{2}}\right)-{\frac {\partial }{\partial x}}({\overline {u'v'}})-{\frac {\partial }{\partial y}}({\overline {v'^{2}}})$

Using a similar order-of-magnitude analysis, the above equations can be reduced to leading order terms. By choosing length scales $\delta$ for changes in the transverse-direction, and L for changes in the streamwise-direction, with $\delta <<L$ , the x-momentum equation simplifies to:

${\overline {u}}{\partial {\overline {u}} \over \partial x}+{\overline {v}}{\partial {\overline {u}} \over \partial y}=-{1 \over \rho }{\partial {\overline {p}} \over \partial x}+{\nu }{\partial ^{2}{\overline {u}} \over \partial y^{2}}-{\frac {\partial }{\partial y}}({\overline {u'v'}}).$

This equation does not satisfy the no-slip condition at the wall. Like Prandtl did for his boundary layer equations, a new, smaller length scale must be used to allow the viscous term to become leading order in the momentum equation. By choosing $\eta <<\delta$ as the *y*-scale, the leading order momentum equation for this "inner boundary layer" is given by:

$0=-{1 \over \rho }{\partial {\overline {p}} \over \partial x}+{\nu }{\partial ^{2}{\overline {u}} \over \partial y^{2}}-{\frac {\partial }{\partial y}}({\overline {u'v'}}).$

In the limit of infinite Reynolds number, the pressure gradient term can be shown to have no effect on the inner region of the turbulent boundary layer. The new "inner length scale" $\eta$ is a viscous length scale, and is of order ${\frac {\nu }{u_{*}}}$ , with $u_{*}$ being the velocity scale of the turbulent fluctuations, in this case a friction velocity.

Unlike the laminar boundary layer equations, the presence of two regimes governed by different sets of flow scales (i.e. the inner and outer scaling) has made finding a universal similarity solution for the turbulent boundary layer difficult and controversial. To find a similarity solution that spans both regions of the flow, it is necessary to asymptotically match the solutions from both regions of the flow. Such analysis will yield either the so-called log-law or power-law.

Similar approaches to the above analysis has also been applied for thermal boundary layers, using the energy equation in compressible flows.

The additional term ${\overline {u'v'}}$ in the turbulent boundary layer equations is known as the Reynolds shear stress and is unknown a priori. The solution of the turbulent boundary layer equations therefore necessitates the use of a turbulence model, which aims to express the Reynolds shear stress in terms of known flow variables or derivatives. The lack of accuracy and generality of such models is a major obstacle in the successful prediction of turbulent flow properties in modern fluid dynamics.

A constant stress layer exists in the near wall region. Due to the damping of the vertical velocity fluctuations near the wall, the Reynolds stress term will become negligible and we find that a linear velocity profile exists. This is only true for the very near wall region.

## Heat and mass transfer

In 1928, the French engineer André Lévêque observed that convective heat transfer in a flowing fluid is affected only by the velocity values very close to the surface. For flows of large Prandtl number, the temperature/mass transition from surface to freestream temperature takes place across a very thin region close to the surface. Therefore, the most important fluid velocities are those inside this very thin region in which the change in velocity can be considered linear with normal distance from the surface. In this way, for

$u(y)=U\left[1-{\frac {(y-h)^{2}}{h^{2}}}\right]=U{\frac {y}{h}}\left[2-{\frac {y}{h}}\right]\;,$

when $y\rightarrow 0$ , then

$u(y)\approx 2U{\frac {y}{h}}=\theta y,$

where *θ* is the tangent of the Poiseuille parabola intersecting the wall. Although Lévêque's solution was specific to heat transfer into a Poiseuille flow, his insight helped lead other scientists to an exact solution of the thermal boundary-layer problem. Schuh observed that in a boundary-layer, *u* is again a linear function of *y*, but that in this case, the wall tangent is a function of *x*. He expressed this with a modified version of Lévêque's profile,

$u(y)=\theta (x)y.$

This results in a very good approximation, even for low $Pr$ numbers, so that only liquid metals with $Pr$ much less than 1 cannot be treated this way. In 1962, Kestin and Persen published a paper describing solutions for heat transfer when the thermal boundary layer is contained entirely within the momentum layer and for various wall temperature distributions. For the problem of a flat plate with a temperature jump at $x=x_{0}$ , they propose a substitution that reduces the parabolic thermal boundary-layer equation to an ordinary differential equation. The solution to this equation, the temperature at any point in the fluid, can be expressed as an incomplete gamma function. Schlichting proposed an equivalent substitution that reduces the thermal boundary-layer equation to an ordinary differential equation whose solution is the same incomplete gamma function. Analytic solutions can be derived with the time-dependent self-similar Ansatz for the incompressible boundary layer equations including heat conduction.

As is well known from several textbooks, heat transfer tends to decrease with the increase in the boundary layer. Recently, it was observed on a practical and large scale that wind flowing through a photovoltaic generator tends to "trap" heat in the PV panels under a turbulent regime due to the decrease in heat transfer. Despite being frequently assumed to be inherently turbulent, this accidental observation demonstrates that natural wind behaves in practice very close to an ideal fluid, at least in an observation resembling the expected behaviour in a flat plate, potentially reducing the difficulty in analysing this kind of phenomenon on a larger scale.

## Convective transfer constants from boundary layer analysis

Paul Richard Heinrich Blasius derived an exact solution to the above laminar boundary layer equations. The thickness of the boundary layer $\delta$ is a function of the Reynolds number for laminar flow.

$\delta \approx 5.0{x \over {\sqrt {Re}}}$

$\delta$

= the thickness of the boundary layer: the region of flow where the velocity is less than 99% of the far field velocity

$v_{\infty }$

;

x

is position along the semi-infinite plate, and

$Re$

is the Reynolds Number given by

$\rho v_{\infty }x/\mu$

(

$\rho =$

density and

$\mu =$

dynamic viscosity).

The Blasius solution uses boundary conditions in a dimensionless form:

${v_{x}-v_{S} \over v_{\infty }-v_{S}}={v_{x} \over v_{\infty }}={v_{y} \over v_{\infty }}=0$

at

$y=0$

${v_{x}-v_{S} \over v_{\infty }-v_{S}}={v_{x} \over v_{\infty }}=1$

at

$y=\infty$

and

$x=0$

Note that in many cases, the no-slip boundary condition holds that $v_{S}$ , the fluid velocity at the surface of the plate equals the velocity of the plate at all locations. If the plate is not moving, then $v_{S}=0$ . A much more complicated derivation is required if fluid slip is allowed.

In fact, the Blasius solution for laminar velocity profile in the boundary layer above a semi-infinite plate can be easily extended to describe Thermal and Concentration boundary layers for heat and mass transfer respectively. Rather than the differential x-momentum balance (equation of motion), this uses a similarly derived Energy and Mass balance:

Energy:         $v_{x}{\partial T \over \partial x}+v_{y}{\partial T \over \partial y}={k \over \rho C_{p}}{\partial ^{2}T \over \partial y^{2}}$

Mass:           $v_{x}{\partial c_{A} \over \partial x}+v_{y}{\partial c_{A} \over \partial y}=D_{AB}{\partial ^{2}c_{A} \over \partial y^{2}}$

For the momentum balance, kinematic viscosity $\nu$ can be considered to be the *momentum diffusivity*. In the energy balance this is replaced by thermal diffusivity $\alpha ={k/\rho C_{P}}$ , and by mass diffusivity $D_{AB}$ in the mass balance. In thermal diffusivity of a substance, k is its thermal conductivity, $\rho$ is its density and $C_{P}$ is its heat capacity. Subscript AB denotes diffusivity of species A diffusing into species B.

Under the assumption that $\alpha =D_{AB}=\nu$ , these equations become equivalent to the momentum balance. Thus, for Prandtl number $Pr=\nu /\alpha =1$ and Schmidt number $Sc=\nu /D_{AB}=1$ the Blasius solution applies directly.

Accordingly, this derivation uses a related form of the boundary conditions, replacing v with T or $c_{A}$ (absolute temperature or concentration of species A). The subscript S denotes a surface condition.

${v_{x}-v_{S} \over v_{\infty }-v_{S}}={T-T_{S} \over T_{\infty }-T_{S}}={c_{A}-c_{AS} \over c_{A\infty }-c_{AS}}=0$

at

$y=0$

${v_{x}-v_{S} \over v_{\infty }-v_{S}}={T-T_{S} \over T_{\infty }-T_{S}}={c_{A}-c_{AS} \over c_{A\infty }-c_{AS}}=1$

at

$y=\infty$

and

$x=0$

Using the streamline function Blasius obtained the following solution for the shear stress at the surface of the plate.

$\tau _{0}=\left({\partial v_{x} \over \partial y}\right)_{y=0}=0.332{v_{\infty } \over x}Re^{1/2}$

And via the boundary conditions, it is known that

${v_{x}-v_{S} \over v_{\infty }-v_{S}}={T-T_{S} \over T_{\infty }-T_{S}}={c_{A}-c_{AS} \over c_{A\infty }-c_{AS}}$

We are given the following relations for heat/mass flux out of the surface of the plate

$\left({\partial T \over \partial y}\right)_{y=0}=0.332{T_{\infty }-T_{S} \over x}Re^{1/2}$

$\left({\partial c_{A} \over \partial y}\right)_{y=0}=0.332{c_{A\infty }-c_{AS} \over x}Re^{1/2}$

So for $Pr=Sc=1$

$\delta =\delta _{T}=\delta _{c}={5.0x \over {\sqrt {Re}}}$

where $\delta _{T},\delta _{c}$ are the regions of flow where T and $c_{A}$ are less than 99% of their far field values.

Because the Prandtl number of a particular fluid is not often unity, German engineer E. Polhausen who worked with Ludwig Prandtl attempted to empirically extend these equations to apply for $Pr\neq 1$ . His results can be applied to $Sc$ as well. He found that for Prandtl number greater than 0.6, the thermal boundary layer thickness was approximately given by:

${\delta \over \delta _{T}}=Pr^{1/3}$

and therefore

${\delta \over \delta _{c}}=Sc^{1/3}$

From this solution, it is possible to characterize the convective heat/mass transfer constants based on the region of boundary layer flow. Fourier's law of conduction and Newton's Law of Cooling are combined with the flux term derived above and the boundary layer thickness.

${q \over A}=-k\left({\partial T \over \partial y}\right)_{y=0}=h_{x}(T_{S}-T_{\infty })$

$h_{x}=0.332{k \over x}Re_{x}^{1/2}Pr^{1/3}$

This gives the local convective constant $h_{x}$ at one point on the semi-infinite plane. Integrating over the length of the plate gives an average

$h_{L}=0.664{k \over x}Re_{L}^{1/2}Pr^{1/3}$

Following the derivation with mass transfer terms ( k = convective mass transfer constant, $D_{AB}$ = diffusivity of species A into species B, $Sc=\nu /D_{AB}$ ), the following solutions are obtained:

$k'_{x}=0.332{D_{AB} \over x}Re_{x}^{1/2}Sc^{1/3}$

$k'_{L}=0.664{D_{AB} \over x}Re_{L}^{1/2}Sc^{1/3}$

These solutions apply for laminar flow with a Prandtl/Schmidt number greater than 0.6.

## Naval architecture

Many of the principles that apply to aircraft also apply to ships, submarines, and offshore platforms, with water as the primary fluid of concern rather than air. As water is not an ideal fluid, ships moving in water experience resistance. The fluid particles cling to the hull of the ship due to the adhesive force between water and the ship, creating a boundary layer where the speed of flow of the fluid forms a small but steep speed gradient, with the fluid in contact with the ship ideally has a relative velocity of 0, and the fluid at the border of the boundary layer being the free-stream speed, or the relative speed of the fluid around the ship.

While the front of the ship faces normal pressure forces due to the fluid surrounding it, the aft portion sees a lower acting component of pressure due to the boundary layer. This leads to higher resistance due to pressure known as 'viscous pressure drag' or 'form drag'.

For ships, unlike aircraft, one deals with incompressible flows, where change in water density is negligible (a pressure rise close to 1000kPa leads to a change of only 2–3 kg/m3). This field of fluid dynamics is called hydrodynamics. A ship engineer designs for hydrodynamics first, and for strength only later. The boundary layer development, breakdown, and separation become critical because the high viscosity of water produces high shear stresses.

## Boundary layer turbine

This effect was exploited in the Tesla turbine, patented by Nikola Tesla in 1913. It is referred to as a bladeless turbine because it uses the boundary layer effect and not a fluid impinging upon the blades as in a conventional turbine. Boundary layer turbines are also known as cohesion-type turbine, bladeless turbine, and Prandtl layer turbine (after Ludwig Prandtl).

## Predicting transient boundary layer thickness in a cylinder using dimensional analysis

By using the transient and viscous force equations for a cylindrical flow you can predict the transient boundary layer thickness by finding the Womersley Number ( $N_{w}$ ).

Transient Force = $\rho vw$

Viscous Force = ${\mu v \over \delta _{1}^{2}}$

Setting them equal to each other gives:

$\rho vw={\mu v \over \delta _{1}^{2}}$

Solving for delta gives:

$\delta _{1}={\sqrt {\mu \over \rho w}}={\sqrt {\ v \over \ w}}$

In dimensionless form:

${L \over \delta _{1}}={L{\sqrt {w \over \ v}}}=N_{w}$

where $N_{w}$ = Womersley Number; $\rho$ = density; v = velocity; $w=$ frequency of oscillations; $\delta _{1}$ = length of transient boundary layer; $\mu$ = viscosity; L = characteristic length.

## Predicting convective flow conditions at the boundary layer in a cylinder using dimensional analysis

By using the convective and viscous force equations at the boundary layer for a cylindrical flow you can predict the convective flow conditions at the boundary layer by finding the dimensionless Reynolds Number ( $Re$ ).

Convective force: $\rho v^{2} \over \ L$

Viscous force: ${\mu v \over \delta _{2}^{2}}$

Setting them equal to each other gives:

${\rho v^{2} \over \ L}={\mu v \over \delta _{2}^{2}}$

Solving for delta gives:

$\delta _{2}={\sqrt {\mu L \over \rho v}}$

In dimensionless form:

${L \over \delta _{2}}={\sqrt {\rho vL \over \mu }}={\sqrt {Re}}$

where $Re$ = Reynolds Number; $\rho$ = density; v = velocity; $\delta _{2}$ = length of convective boundary layer; $\mu$ = viscosity; L = characteristic length.

## Boundary layer ingestion

Boundary layer ingestion promises an increase in aircraft fuel efficiency with an aft-mounted propulsor ingesting the slow fuselage boundary layer and re-energising the wake to reduce drag and improve propulsive efficiency. To operate in distorted airflow, the fan is heavier and its efficiency is reduced, and its integration is challenging. It is used in concepts like the Aurora D8 or the French research agency Onera's Nova, saving 5% in cruise by ingesting 40% of the fuselage boundary layer.

Airbus presented the Nautilius concept at the ICAS congress in September 2018: to ingest all the fuselage boundary layer, while minimizing the azimuthal flow distortion, the fuselage splits into two spindles with 13-18:1 bypass ratio fans. Propulsive efficiencies are up to 90% like counter-rotating open rotors with smaller, lighter, less complex and noisy engines. It could lower fuel burn by over 10% compared to a usual underwing 15:1 bypass ratio engine.
