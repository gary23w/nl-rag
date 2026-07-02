---
title: "Finite volume method"
source: https://en.wikipedia.org/wiki/Finite_volume_method
domain: finite-volume-method
license: CC-BY-SA-4.0
tags: finite volume method, godunov scheme, riemann solver, flux limiter
fetched: 2026-07-02
---

# Finite volume method

The **finite volume method** (**FVM**) is a method for representing and evaluating partial differential equations in the form of algebraic equations. In the finite volume method, volume integrals in a partial differential equation that contain a divergence term are converted to surface integrals, using the divergence theorem. These terms are then evaluated as fluxes at the surfaces of each finite volume. Because the flux entering a given volume is identical to that leaving the adjacent volume, these methods are conservative. Another advantage of the finite volume method is that it is easily formulated to allow for unstructured meshes. The method is used in many computational fluid dynamics packages. "Finite volume" refers to the small volume surrounding each node point on a mesh.

Finite volume methods can be compared and contrasted with the finite difference methods, which approximate derivatives using nodal values, or finite element methods, which create local approximations of a solution using local data, and construct a global approximation by stitching them together. In contrast a finite volume method evaluates exact expressions for the *average* value of the solution over some volume, and uses this data to construct approximations of the solution within cells.

## Example

Consider a simple 1D advection problem:

| ${\frac {\partial \rho }{\partial t}}+{\frac {\partial f}{\partial x}}=0,\quad t\geq 0.$ |   | 1 |
|---|---|---|

Here, $\rho =\rho \left(x,t\right)$ represents the state variable and $f=f\left(\rho \left(x,t\right)\right)$ represents the flux or flow of $\rho$ . Conventionally, positive f represents flow to the right while negative f represents flow to the left. If we assume that equation (**1**) represents a flowing medium of constant area, we can sub-divide the spatial domain, x , into *finite volumes* or *cells* with cell centers indexed as i . For a particular cell, i , we can define the *volume average* value of ${\rho }_{i}\left(t\right)=\rho \left(x,t\right)$ at time ${t=t_{1}}$ and ${x\in \left[x_{i-1/2},x_{i+1/2}\right]}$ , as

| ${\bar {\rho }}_{i}\left(t_{1}\right)={\frac {1}{x_{i+1/2}-x_{i-1/2}}}\int _{x_{i-1/2}}^{x_{i+1/2}}\rho \left(x,t_{1}\right)\,dx,$ |   | 2 |
|---|---|---|

and at time $t=t_{2}$ as,

| ${\bar {\rho }}_{i}\left(t_{2}\right)={\frac {1}{x_{i+1/2}-x_{i-1/2}}}\int _{x_{i-1/2}}^{x_{i+1/2}}\rho \left(x,t_{2}\right)\,dx,$ |   | 3 |
|---|---|---|

where $x_{i-1/2}$ and $x_{i+1/2}$ represent locations of the upstream and downstream faces or edges respectively of the $i^{\text{th}}$ cell.

Integrating equation (**1**) in time, we have:

| $\rho \left(x,t_{2}\right)=\rho \left(x,t_{1}\right)-\int _{t_{1}}^{t_{2}}f_{x}\left(x,t\right)\,dt,$ |   | 4 |
|---|---|---|

where $f_{x}={\frac {\partial f}{\partial x}}$ .

To obtain the volume average of $\rho \left(x,t\right)$ at time $t=t_{2}$ , we integrate $\rho \left(x,t_{2}\right)$ over the cell volume, $\left[x_{i-1/2},x_{i+1/2}\right]$ and divide the result by $\Delta x_{i}=x_{i+1/2}-x_{i-1/2}$ , i.e.

| ${\bar {\rho }}_{i}\left(t_{2}\right)={\frac {1}{\Delta x_{i}}}\int _{x_{i-1/2}}^{x_{i+1/2}}\left\{\rho \left(x,t_{1}\right)-\int _{t_{1}}^{t_{2}}f_{x}\left(x,t\right)dt\right\}dx.$ |   | 5 |
|---|---|---|

We assume that $f\$ is well behaved and that we can reverse the order of integration. Also, recall that flow is normal to the unit area of the cell. Now, since in one dimension $f_{x}\triangleq \nabla \cdot f$ , we can apply the divergence theorem, i.e. $\oint _{v}\nabla \cdot fdv=\oint _{S}f\,dS$ , and substitute for the volume integral of the divergence with the values of $f(x)$ evaluated at the cell surface (edges $x_{i-1/2}$ and $x_{i+1/2}$ ) of the finite volume as follows:

| ${\bar {\rho }}_{i}\left(t_{2}\right)={\bar {\rho }}_{i}\left(t_{1}\right)-{\frac {1}{\Delta x_{i}}}\left(\int _{t_{1}}^{t_{2}}f_{i+1/2}dt-\int _{t_{1}}^{t_{2}}f_{i-1/2}dt\right).$ |   | 6 |
|---|---|---|

where $f_{i\pm 1/2}=f\left(x_{i\pm 1/2},t\right)$ .

We can therefore derive a *semi-discrete* numerical scheme for the above problem with cell centers indexed as i , and with cell edge fluxes indexed as $i\pm 1/2$ , by differentiating (**6**) with respect to time to obtain:

| ${\frac {d{\bar {\rho }}_{i}}{dt}}+{\frac {1}{\Delta x_{i}}}\left[f_{i+1/2}-f_{i-1/2}\right]=0,$ |   | 7 |
|---|---|---|

where values for the edge fluxes, $f_{i\pm 1/2}$ , can be reconstructed by interpolation or extrapolation of the cell averages. Equation (**7**) is *exact* for the volume averages; i.e., no approximations have been made during its derivation.

This method can also be applied to a 2D situation by considering the north and south faces along with the east and west faces around a node.

## General conservation law

We can also consider the general conservation law problem, represented by the following PDE,

| ${\frac {\partial \mathbf {u} }{\partial t}}+\nabla \cdot {\mathbf {f} }\left({\mathbf {u} }\right)={\mathbf {0} }.$ |   | 8 |
|---|---|---|

Here, $\mathbf {u}$ represents a vector of states and $\mathbf {f}$ represents the corresponding flux tensor. Again we can sub-divide the spatial domain into finite volumes or cells. For a particular cell, i , we take the volume integral over the total volume of the cell, $v_{i}$ , which gives,

| $\int _{v_{i}}{\frac {\partial \mathbf {u} }{\partial t}}\,dv+\int _{v_{i}}\nabla \cdot {\mathbf {f} }\left({\mathbf {u} }\right)\,dv={\mathbf {0} }.$ |   | 9 |
|---|---|---|

On integrating the first term to get the *volume average* and applying the *divergence theorem* to the second, this yields

| $v_{i}{{d{\mathbf {\bar {u}} }_{i}} \over dt}+\oint _{S_{i}}{\mathbf {f} }\left({\mathbf {u} }\right)\cdot {\mathbf {n} }\ dS={\mathbf {0} },$ |   | 10 |
|---|---|---|

where $S_{i}$ represents the total surface area of the cell and ${\mathbf {n} }$ is a unit vector normal to the surface and pointing outward. So, finally, we are able to present the general result equivalent to (**8**), i.e.

| ${{d{\mathbf {\bar {u}} }_{i}} \over {dt}}+{{1} \over {v_{i}}}\oint _{S_{i}}{\mathbf {f} }\left({\mathbf {u} }\right)\cdot {\mathbf {n} }\ dS={\mathbf {0} }.$ |   | 11 |
|---|---|---|

Again, values for the edge fluxes can be reconstructed by interpolation or extrapolation of the cell averages. The actual numerical scheme will depend upon problem geometry and mesh construction. MUSCL reconstruction is often used in high resolution schemes where shocks or discontinuities are present in the solution.

Finite volume schemes are conservative as cell averages change through the edge fluxes. In other words, *one cell's loss is always another cell's gain*!
