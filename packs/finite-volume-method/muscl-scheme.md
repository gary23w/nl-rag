---
title: "MUSCL scheme"
source: https://en.wikipedia.org/wiki/MUSCL_scheme
domain: finite-volume-method
license: CC-BY-SA-4.0
tags: finite volume method, godunov scheme, riemann solver, flux limiter
fetched: 2026-07-02
---

# MUSCL scheme

In the study of partial differential equations, the **MUSCL scheme** is a finite volume method that can provide highly accurate numerical solutions for a given system, even in cases where the solutions exhibit shocks, discontinuities, or large gradients. MUSCL stands for *Monotonic Upstream-centered Scheme for Conservation Laws* (van Leer, 1979), and the term was introduced in a seminal paper by Bram van Leer (van Leer, 1979). In this paper he constructed the first *high-order*, *total variation diminishing* (TVD) scheme where he obtained second order spatial accuracy.

The idea is to replace the piecewise constant approximation of Godunov's scheme by reconstructed states, derived from cell-averaged states obtained from the previous time-step. For each cell, slope limited, reconstructed left and right states are obtained and used to calculate fluxes at the cell boundaries (edges). These fluxes can, in turn, be used as input to a *Riemann solver*, following which the solutions are averaged and used to advance the solution in time. Alternatively, the fluxes can be used in *Riemann-solver-free* schemes, which are basically Rusanov-like schemes.

## Linear reconstruction

We will consider the fundamentals of the MUSCL scheme by considering the following simple first-order, scalar, 1D system, which is assumed to have a wave propagating in the positive direction,

$u_{t}+F_{x}\left(u\right)=0.\,$

Where u represents a state variable and F represents a flux variable.

The basic scheme of Godunov uses piecewise constant approximations for each cell, and results in a first-order upwind discretisation of the above problem with cell centres indexed as i . A semi-discrete scheme can be defined as follows,

${\frac {\mathrm {d} u_{i}}{\mathrm {d} t}}+{\frac {1}{\Delta x_{i}}}\left[F\left(u_{i}\right)-F\left(u_{i-1}\right)\right]=0.$

This basic scheme is not able to handle shocks or sharp discontinuities as they tend to become smeared. An example of this effect is shown in the diagram opposite, which illustrates a 1D advective equation with a step wave propagating to the right. The simulation was carried out with a mesh of 200 cells and used a 4th order Runge–Kutta time integrator (RK4).

To provide higher resolution of discontinuities, Godunov's scheme can be extended to use piecewise linear approximations of each cell, which results in a *central difference* scheme that is *second-order* accurate in space. The piecewise linear approximations are obtained from

$u\left(x\right)=u_{i}+{\frac {\left(x-x_{i}\right)}{\left(x_{i+1}-x_{i}\right)}}\left(u_{i+1}-u_{i}\right)\qquad \forall x\in (x_{i},x_{i+1}].$

Thus, evaluating fluxes at the cell edges we get the following semi-discrete scheme

${\frac {\mathrm {d} u_{i}}{\mathrm {d} t}}+{\frac {1}{\Delta x_{i}}}\left[F\left(u_{i+1/2}\right)-F\left(u_{i-1/2}\right)\right]=0,$

where $u_{i+1/2}$ and $u_{i-1/2}$ are the piecewise approximate values of cell edge variables, *i.e.*,

$u_{i+1/2}=0.5\left(u_{i}+u_{i+1}\right),$

$u_{i-1/2}=0.5\left(u_{i-1}+u_{i}\right).$

Although the above second-order scheme provides greater accuracy for smooth solutions, it is not a total variation diminishing (TVD) scheme and introduces spurious oscillations into the solution where discontinuities or shocks are present. An example of this effect is shown in the diagram opposite, which illustrates a 1D advective equation $\,u_{t}+u_{x}=0$ , with a step wave propagating to the right. This loss of accuracy is to be expected due to Godunov's theorem. The simulation was carried out with a mesh of 200 cells and used RK4 for time integration.

MUSCL based numerical schemes extend the idea of using a linear piecewise approximation to each cell by using *slope limited* left and right extrapolated states. This results in the following high resolution, TVD discretisation scheme,

${\frac {\mathrm {d} u_{i}}{\mathrm {d} t}}+{\frac {1}{\Delta x_{i}}}\left[F\left(u_{i+1/2}^{*}\right)-F\left(u_{i-1/2}^{*}\right)\right]=0.$

Which, alternatively, can be written in the more succinct form,

${\frac {\mathrm {d} u_{i}}{\mathrm {d} t}}+{\frac {1}{\Delta x_{i}}}\left[F_{i+1/2}^{*}-F_{i-1/2}^{*}\right]=0.$

The numerical fluxes $F_{i\pm 1/2}^{*}$ correspond to a nonlinear combination of first and second-order approximations to the continuous flux function.

The symbols $u_{i+1/2}^{*}$ and $u_{i-1/2}^{*}$ represent scheme dependent functions (of the limited extrapolated cell edge variables), *i.e.*,

$u_{i+1/2}^{*}=u_{i+1/2}^{*}\left(u_{i+1/2}^{L},u_{i+1/2}^{R}\right),u_{i-1/2}^{*}=u_{i-1/2}^{*}\left(u_{i-1/2}^{L},u_{i-1/2}^{R}\right),$

where, using downwind slopes:

$u_{i+1/2}^{L}=u_{i}+0.5\phi \left(r_{i}\right)\left(u_{i+1}-u_{i}\right),u_{i+1/2}^{R}=u_{i+1}-0.5\phi \left(r_{i+1}\right)\left(u_{i+2}-u_{i+1}\right),$

$u_{i-1/2}^{L}=u_{i-1}+0.5\phi \left(r_{i-1}\right)\left(u_{i}-u_{i-1}\right),u_{i-1/2}^{R}=u_{i}-0.5\phi \left(r_{i}\right)\left(u_{i+1}-u_{i}\right),$

and

$r_{i}={\frac {u_{i}-u_{i-1}}{u_{i+1}-u_{i}}}.$

The function $\phi \left(r_{i}\right)$ is a limiter function that limits the slope of the piecewise approximations to ensure the solution is TVD, thereby avoiding the spurious oscillations that would otherwise occur around discontinuities or shocks - see Flux limiter section. The limiter is equal to zero when $r\leq 0$ and is equal to unity when $r=1$ . Thus, the accuracy of a TVD discretization degrades to first order at local extrema, but tends to second order over smooth parts of the domain.

The algorithm is straight­forward to implement. Once a suitable scheme for $F_{i+1/2}^{*}$ has been chosen, such as the *Kurganov and Tadmor scheme* (see below), the solution can proceed using standard numerical integration techniques.

## Kurganov and Tadmor central scheme

A precursor to the *Kurganov and Tadmor* (KT) *central scheme*, (Kurganov and Tadmor, 2000), is the *Nessyahu and Tadmor* (NT) a staggered *central scheme*, (Nessyahu and Tadmor, 1990). It is a Riemann-solver-free, second-order, high-resolution scheme that uses MUSCL reconstruction. It is a fully discrete method that is straight­forward to implement and can be used on scalar and vector problems, and can be viewed as a Rusanov flux (also called the local Lax-Friedrichs flux) supplemented with high order reconstructions. The algorithm is based upon central differences with comparable performance to Riemann type solvers when used to obtain solutions for PDE's describing systems that exhibit high-gradient phenomena.

The KT scheme extends the NT scheme and has a smaller amount of numerical viscosity than the original NT scheme. It also has the added advantage that it can be implemented as either a *fully discrete* or *semi-discrete* scheme. Here we consider the semi-discrete scheme.

The calculation is shown below:

$F_{i-{\frac {1}{2}}}^{*}={\frac {1}{2}}\left\{\left[F\left(u_{i-{\frac {1}{2}}}^{R}\right)+F\left(u_{i-{\frac {1}{2}}}^{L}\right)\right]-a_{i-{\frac {1}{2}}}\left[u_{i-{\frac {1}{2}}}^{R}-u_{i-{\frac {1}{2}}}^{L}\right]\right\}.$

$F_{i+{\frac {1}{2}}}^{*}={\frac {1}{2}}\left\{\left[F\left(u_{i+{\frac {1}{2}}}^{R}\right)+F\left(u_{i+{\frac {1}{2}}}^{L}\right)\right]-a_{i+{\frac {1}{2}}}\left[u_{i+{\frac {1}{2}}}^{R}-u_{i+{\frac {1}{2}}}^{L}\right]\right\}.$

Where the *local propagation speed*, $a_{i\pm {\frac {1}{2}}}\$ , is the maximum absolute value of the eigenvalue of the Jacobian of $F\left(u\left(x,t\right)\right)$ over cells ${i},{i\pm 1}$ given by

$a_{i+{\frac {1}{2}}}\left(t\right)=\max \left[\rho \left({\frac {\partial F\left(u_{i+1/2}^{L}\left(t\right)\right)}{\partial u}}\right),\rho \left({\frac {\partial F\left(u_{i+1/2}^{R}\left(t\right)\right)}{\partial u}}\right),\right]$

and $\rho \left({\frac {\partial F\left(u\left(t\right)\right)}{\partial u}}\right)\$ represents the spectral radius of ${\frac {\partial F\left(u\left(t\right)\right)}{\partial u}}.$

Beyond these CFL related speeds, no characteristic information is required.

The above flux calculation is most frequently called *Lax-Friedrichs flux* (though it's worth mentioning that such flux expression does not appear in Lax, 1954 but rather on Rusanov, 1961).

An example of the effectiveness of using a high resolution scheme is shown in the diagram opposite, which illustrates the 1D advective equation $u_{t}+u_{x}=0\$ , with a step wave propagating to the right. The simulation was carried out on a mesh of 200 cells, using the Kurganov and Tadmor central scheme with Superbee limiter and used RK-4 for time integration. This simulation result contrasts extremely well against the above first-order upwind and second-order central difference results shown above. This scheme also provides good results when applied to sets of equations - see results below for this scheme applied to the Euler equations. However, care has to be taken in choosing an appropriate limiter because, for example, the Superbee limiter can cause unrealistic sharpening for some smooth waves.

The scheme can readily include diffusion terms, if they are present. For example, if the above 1D scalar problem is extended to include a diffusion term, we get

$u_{t}+F_{x}\left(u\right)=Q_{x}\left(u,u_{x}\right),$

for which Kurganov and Tadmor propose the following central difference approximation,

${\frac {\mathrm {d} u_{i}}{\mathrm {d} t}}=-{\frac {1}{\Delta x_{i}}}\left[F_{i+{\frac {1}{2}}}^{*}-F_{i-{\frac {1}{2}}}^{*}\right]+{\frac {1}{\Delta x_{i}}}\left[P_{i+{\frac {1}{2}}}-P_{i-{\frac {1}{2}}}\right].$

Where,

$P_{i+{\frac {1}{2}}}={\frac {1}{2}}\left[Q\left(u_{i},{\frac {u_{i+1}-u_{i}}{\Delta x_{i}}}\right)+Q\left(u_{i+1},{\frac {u_{i+1}-u_{i}}{\Delta x_{i}}}\right)\right],$

$P_{i-{\frac {1}{2}}}={\frac {1}{2}}\left[Q\left(u_{i-1},{\frac {u_{i}-u_{i-1}}{\Delta x_{i-1}}}\right)+Q\left(u_{i},{\frac {u_{i}-u_{i-1}}{\Delta x_{i-1}}}\right).\right]$

Full details of the algorithm (*full* and *semi-discrete* versions) and its derivation can be found in the original paper (Kurganov and Tadmor, 2000), along with a number of 1D and 2D examples. Additional information is also available in the earlier related paper by Nessyahu and Tadmor (1990).

**Note:** This scheme was originally presented by Kurganov and Tadmor as a 2nd order scheme based upon *linear extrapolation*. A later paper (Kurganov and Levy, 2000) demonstrates that it can also form the basis of a third order scheme. A 1D advective example and an Euler equation example of their scheme, using parabolic reconstruction (3rd order), are shown in the *parabolic reconstruction* and *Euler equation* sections below.

## Piecewise parabolic reconstruction

It is possible to extend the idea of linear extrapolation to higher-order reconstruction, and an example is shown in the diagram opposite. However, for this case the left and right states are estimated by interpolation of a second-order, upwind biased, difference equation. This results in a parabolic reconstruction scheme that is third-order accurate in space.

We follow the approach of Kermani (Kermani, et al., 2003), and present a third-order upwind biased scheme, where the symbols $u_{i+{\frac {1}{2}}}^{*}$ and $u_{i-{\frac {1}{2}}}^{*}$ again represent scheme dependent functions (of the limited reconstructed cell edge variables). But for this case they are based upon parabolically reconstructed states, *i.e.*,

$u_{i+{\frac {1}{2}}}^{*}=f\left(u_{i+{\frac {1}{2}}}^{L},u_{i+{\frac {1}{2}}}^{R}\right),\quad u_{i-{\frac {1}{2}}}^{*}=f\left(u_{i-{\frac {1}{2}}}^{L},u_{i-{\frac {1}{2}}}^{R}\right),$

and

$u_{i+{\frac {1}{2}}}^{L}=u_{i}+{\frac {\phi \left(r_{i}\right)}{4}}\left[\left(1-\kappa \right)\delta u_{i-{\frac {1}{2}}}+\left(1+\kappa \right)\delta u_{i+{\frac {1}{2}}}\right],$

$u_{i+{\frac {1}{2}}}^{R}=u_{i+1}-{\frac {\phi \left(r_{i+1}\right)}{4}}\left[\left(1-\kappa \right)\delta u_{i+{\frac {3}{2}}}+\left(1+\kappa \right)\delta u_{i+{\frac {1}{2}}}\right],$

$u_{i-{\frac {1}{2}}}^{L}=u_{i-1}+{\frac {\phi \left(r_{i-1}\right)}{4}}\left[\left(1-\kappa \right)\delta u_{i-{\frac {3}{2}}}+\left(1+\kappa \right)\delta u_{i-{\frac {1}{2}}}\right],$

$u_{i-{\frac {1}{2}}}^{R}=u_{i}-{\frac {\phi \left(r_{i}\right)}{4}}\left[\left(1-\kappa \right)\delta u_{i+{\frac {1}{2}}}+\left(1+\kappa \right)\delta u_{i-{\frac {1}{2}}}\right].$

Where $\kappa \$ = 1/3 and,

$\delta u_{i+{\frac {1}{2}}}=\left(u_{i+1}-u_{i}\right),\quad \delta u_{i-{\frac {1}{2}}}=\left(u_{i}-u_{i-1}\right),$

$\delta u_{i+{\frac {3}{2}}}=\left(u_{i+2}-u_{i+1}\right),\quad \delta u_{i-{\frac {3}{2}}}=\left(u_{i-1}-u_{i-2}\right),$

and the limiter function $\phi \left(r\right)\$ is the same as above.

Parabolic reconstruction is straight­forward to implement and can be used with the Kurganov and Tadmor scheme in lieu of the linear extrapolation shown above. This has the effect of raising the spatial solution of the KT scheme to 3rd order. It performs well when solving the Euler equations, see below. This increase in spatial order has certain advantages over 2nd order schemes for smooth solutions, however, for shocks it is more dissipative - compare diagram opposite with above solution obtained using the KT algorithm with linear extrapolation and Superbee limiter. This simulation was carried out on a mesh of 200 cells using the same KT algorithm but with parabolic reconstruction. Time integration was by RK-4, and the alternative form of van Albada limiter, $\phi _{va}(r)={\frac {2r}{1+r^{2}}}\$ , was used to avoid spurious oscillations.

## Example: 1D Euler equations

For simplicity we consider the 1D case without heat transfer and without body force. Therefore, in conservation vector form, the general Euler equations reduce to

${\frac {\partial \mathbf {U} }{\partial t}}+{\frac {\partial \mathbf {F} }{\partial x}}=0,$

where

$\mathbf {U} ={\begin{pmatrix}\rho \\\rho u\\E\end{pmatrix}}\qquad \mathbf {F} ={\begin{pmatrix}\rho u\\p+\rho u^{2}\\u(E+p)\end{pmatrix}},\qquad$

and where **${\mbox{U}}$** is a vector of states and **${\mbox{F}}$** is a vector of fluxes.

The equations above represent conservation of **mass**, **momentum**, and **energy**. There are thus three equations and four unknowns, $\rho$ (density) u (fluid velocity), p (pressure) and E (total energy). The total energy is given by,

$E=\rho e+{\frac {1}{2}}\rho u^{2},$

where $e\$ represents specific internal energy.

In order to close the system an equation of state is required. One that suits our purpose is

$p=\rho \left(\gamma -1\right)e,$

where $\gamma \$ is equal to the ratio of specific heats $\left[c_{p}/c_{v}\right]$ for the fluid.

We can now proceed, as shown above in the simple 1D example, by obtaining the left and right extrapolated states for each state variable. Thus, for density we obtain

$\rho _{i+{\frac {1}{2}}}^{*}=\rho _{i+{\frac {1}{2}}}^{*}\left(\rho _{i+{\frac {1}{2}}}^{L},\rho _{i+{\frac {1}{2}}}^{R}\right),\quad \rho _{i-{\frac {1}{2}}}^{*}=\rho _{i-{\frac {1}{2}}}^{*}\left(\rho _{i-{\frac {1}{2}}}^{L},\rho _{i-{\frac {1}{2}}}^{R}\right),$

where

$\rho _{i+{\frac {1}{2}}}^{L}=\rho _{i}+0.5\phi \left(r_{i}\right)\left(\rho _{i+1}-\rho _{i}\right),\quad \rho _{i+{\frac {1}{2}}}^{R}=\rho _{i+1}-0.5\phi \left(r_{i+1}\right)\left(\rho _{i+2}-\rho _{i+1}\right),$

$\rho _{i-{\frac {1}{2}}}^{L}=\rho _{i-1}+0.5\phi \left(r_{i-1}\right)\left(\rho _{i}-\rho _{i-1}\right),\quad \rho _{i-{\frac {1}{2}}}^{R}=\rho _{i}-0.5\phi \left(r_{i}\right)\left(\rho _{i+1}-\rho _{i}\right).$

Similarly, for momentum $\rho u$ , and total energy E . Velocity u , is calculated from momentum, and pressure p , is calculated from the equation of state.

Having obtained the limited extrapolated states, we then proceed to construct the edge fluxes using these values. With the edge fluxes known, we can now construct the semi-discrete scheme, *i.e.*,

${\frac {\mathrm {d} \mathbf {U} _{i}}{\mathrm {d} t}}=-{\frac {1}{\Delta x_{i}}}\left[\mathbf {F} _{i+{\frac {1}{2}}}^{*}-\mathbf {F} _{i-{\frac {1}{2}}}^{*}\right].$

The solution can now proceed by integration using standard numerical techniques.

The above illustrates the basic idea of the MUSCL scheme. However, for a practical solution to the Euler equations, a suitable scheme (such as the above KT scheme) also has to be chosen in order to define the function $\mathbf {F} _{i\pm {\frac {1}{2}}}^{*}$ .

The diagram opposite shows a 2nd order solution to G A Sod's shock tube problem (Sod, 1978) using the above high resolution Kurganov and Tadmor Central Scheme (KT) with Linear Extrapolation and Ospre limiter. This illustrates clearly demonstrates the effectiveness of the MUSCL approach to solving the Euler equations. The simulation was carried out on a mesh of 200 cells using Matlab code (Wesseling, 2001), adapted to use the KT algorithm and Ospre limiter. Time integration was performed by a 4th order SHK (equivalent performance to RK-4) integrator. The following initial conditions (SI units) were used:

- pressure left = 100000 [Pa];
- pressure right= 10000 [Pa];
- density left = 1.0 [kg/m3];
- density right = 0.125 [kg/m3];
- length = 20 [m];
- velocity left = 0 [m/s];
- velocity right = 0 [m/s];
- duration =0.01 [s];
- lambda = 0.001069 (Δt/Δx).

The diagram opposite shows a 3rd order solution to G A Sod's shock tube problem (Sod, 1978) using the above high resolution Kurganov and Tadmor Central Scheme (KT) but with parabolic reconstruction and van Albada limiter. This again illustrates the effectiveness of the MUSCL approach to solving the Euler equations. The simulation was carried out on a mesh of 200 cells using Matlab code (Wesseling, 2001), adapted to use the KT algorithm with Parabolic Extrapolation and van Albada limiter. The alternative form of van Albada limiter, $\phi _{va}(r)={\frac {2r}{1+r^{2}}}\$ , was used to avoid spurious oscillations. Time integration was performed by a 4th order SHK integrator. The same initial conditions were used.

Various other high resolution schemes have been developed that solve the Euler equations with good accuracy. Examples of such schemes are,

- the **Osher scheme**, and
- the **Liou-Steffen** AUSM (advection upstream splitting method) scheme.

More information on these and other methods can be found in the references below. An open source implementation of the Kurganov and Tadmor central scheme can be found in the external links below.
