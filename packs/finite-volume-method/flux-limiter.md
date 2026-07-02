---
title: "Flux limiter"
source: https://en.wikipedia.org/wiki/Flux_limiter
domain: finite-volume-method
license: CC-BY-SA-4.0
tags: finite volume method, godunov scheme, riemann solver, flux limiter
fetched: 2026-07-02
---

# Flux limiter

**Flux limiters** are used in high resolution schemes – numerical schemes used to solve problems in science and engineering, particularly fluid dynamics, described by partial differential equations (PDEs). They are used in high resolution schemes, such as the MUSCL scheme, to avoid the spurious oscillations (wiggles) that would otherwise occur with high order spatial discretization schemes due to shocks, discontinuities or sharp changes in the solution domain. Use of flux limiters, together with an appropriate high resolution scheme, make the solutions total variation diminishing (TVD).

Note that flux limiters are also referred to as **slope limiters** because they both have the same mathematical form, and both have the effect of limiting the solution gradient near shocks or discontinuities. In general, the term flux limiter is used when the limiter acts on system *fluxes*, and slope limiter is used when the limiter acts on system *states* (like pressure, velocity etc.).

## How they work

The main idea behind the construction of flux limiter schemes is to limit the spatial derivatives to realistic values – for scientific and engineering problems this usually means physically realisable and meaningful values. They are used in high resolution schemes for solving problems described by PDEs and only come into operation when sharp wave fronts are present. For smoothly changing waves, the flux limiters do not operate and the spatial derivatives can be represented by higher order approximations without introducing spurious oscillations. Consider the 1D semi-discrete scheme below,

${\frac {du_{i}}{dt}}+{\frac {1}{\Delta x_{i}}}\left[F\left(u_{i+{1}/{2}}\right)-F\left(u_{i-{1}/{2}}\right)\right]=0,$

where, $F\left(u_{i+{1}/{2}}\right)$ and $F\left(u_{i-1/2}\right)$ represent edge fluxes for the *i*-th cell. If these edge fluxes can be represented by *low* and *high* resolution schemes, then a flux limiter can switch between these schemes depending upon the gradients close to the particular cell, as follows,

$F\left(u_{i+1/2}\right)=f_{i+1/2}^{\text{low}}-\phi \left(r_{i}\right)\left(f_{i+1/2}^{\text{low}}-f_{i+1/2}^{\text{high}}\right),$ $F\left(u_{i-1/2}\right)=f_{i-1/2}^{\text{low}}-\phi \left(r_{i-1}\right)\left(f_{i-1/2}^{\text{low}}-f_{i-1/2}^{\text{high}}\right),$

where

- $f^{\text{low}}$ is the low resolution flux,
- $f^{\text{high}}$ is the high resolution flux,
- $\phi \ (r)$ is the flux limiter function, and
- r represents the ratio of successive gradients on the solution mesh, i.e., $r_{i}={\frac {u_{i}-u_{i-1}}{u_{i+1}-u_{i}}}.$

The limiter function is constrained to be greater than or equal to zero, i.e., $\phi \ (r)\geq 0$ . Therefore, when the limiter is equal to zero (sharp gradient, opposite slopes or zero gradient), the flux is represented by a *low resolution scheme*. Similarly, when the limiter is equal to 1 (smooth solution), it is represented by a *high resolution scheme*. The various limiters have differing switching characteristics and are selected according to the particular problem and solution scheme. No particular limiter has been found to work well for all problems, and a particular choice is usually made on a trial and error basis.

## Limiter functions

The following are common forms of flux/slope limiter function, $\phi (r)$ :

- **CHARM** [not 2nd order TVD] $\phi _{cm}(r)={\begin{cases}{\frac {r\left(3r+1\right)}{\left(r+1\right)^{2}}},&r>0,&\lim _{r\to \infty }\phi _{cm}(r)=3\\0\quad \quad \,,&r\leq 0\end{cases}}$
- **HCUS** [not 2nd order TVD] $\phi _{hc}(r)={\frac {1.5\left(r+\left|r\right|\right)}{\left(r+2\right)}};\quad \lim _{r\to \infty }\phi _{hc}(r)=3.$
- **HQUICK** [not 2nd order TVD] $\phi _{hq}(r)={\frac {2\left(r+\left|r\right|\right)}{\left(r+3\right)}};\quad \lim _{r\to \infty }\phi _{hq}(r)=4.$
- **Koren** – third-order accurate for sufficiently smooth data $\phi _{kn}(r)=\max \left[0,\min \left(2r,{\dfrac {(1+2r)}{3}},2\right)\right];\quad \lim _{r\to \infty }\phi _{kn}(r)=2.$
- **minmod** – symmetric $\phi _{mm}(r)=\max \left[0,\min \left(1,r\right)\right];\quad \lim _{r\to \infty }\phi _{mm}(r)=1.$
- **monotonized central (MC)** – symmetric $\phi _{mc}(r)=\max \left[0,\min \left(2r,0.5(1+r),2\right)\right];\quad \lim _{r\to \infty }\phi _{mc}(r)=2.$
- **Osher** $\phi _{os}(r)=\max \left[0,\min \left(r,\beta \right)\right],\quad \left(1\leq \beta \leq 2\right);\quad \lim _{r\to \infty }\phi _{os}(r)=\beta .$
- **ospre** – symmetric $\phi _{op}(r)={\frac {1.5\left(r^{2}+r\right)}{\left(r^{2}+r+1\right)}};\quad \lim _{r\to \infty }\phi _{op}(r)=1.5\,.$
- **smart** [not 2nd order TVD] $\phi _{sm}(r)=\max \left[0,\min \left(2r,\left(0.25+0.75r\right),4\right)\right];\quad \lim _{r\to \infty }\phi _{sm}(r)=4.$
- **superbee** – symmetric $\phi _{sb}(r)=\max \left[0,\min \left(2r,1\right),\min \left(r,2\right)\right];\quad \lim _{r\to \infty }\phi _{sb}(r)=2.$
- **Sweby** – symmetric $\phi _{sw}(r)=\max \left[0,\min \left(\beta r,1\right),\min \left(r,\beta \right)\right],\quad \left(1\leq \beta \leq 2\right);\quad \lim _{r\to \infty }\phi _{sw}(r)=\beta .$
- **UMIST** – symmetric $\phi _{um}(r)=\max \left[0,\min \left(2r,\left(0.25+0.75r\right),\left(0.75+0.25r\right),2\right)\right];\quad \lim _{r\to \infty }\phi _{um}(r)=2.$
- **van Albada 1** – symmetric $\phi _{va1}(r)={\frac {r^{2}+r}{r^{2}+1}};\quad \lim _{r\to \infty }\phi _{va1}(r)=1.$
- **van Albada 2** – alternative form [not 2nd order TVD] used on high spatial order schemes $\phi _{va2}(r)={\frac {2r}{r^{2}+1}};\quad \lim _{r\to \infty }\phi _{va2}(r)=0.$
- **van Leer** – symmetric $\phi _{vl}(r)={\frac {r+\left|r\right|}{1+\left|r\right|}};\quad \lim _{r\to \infty }\phi _{vl}(r)=2.$
- All the above limiters indicated as being *symmetric*, exhibit the following symmetry property, ${\frac {\phi \left(r\right)}{r}}=\phi \left({\frac {1}{r}}\right).$

This is a desirable property as it ensures that the limiting actions for forward and backward gradients operate in the same way.

Unless indicated to the contrary, the above limiter functions are second order TVD. This means that they are designed such that they pass through a certain region of the solution, known as the TVD region, in order to guarantee stability of the scheme. Second-order, TVD limiters satisfy at least the following criteria:

- $r\leq \phi (r)\leq 2r,\left(0\leq r\leq 1/2\right)\$ ,
- $r\leq \phi (r)\leq 1,\left(1/2\leq r\leq 1\right)\$ ,
- $\phi (1)=1\$ ,
- $1\leq \phi (r)\leq r,\left(1\leq r\leq 2\right)\$ ,
- $1\leq \phi (r)\leq 2,\left(r>2\right)\$ ,

The admissible limiter region for second-order TVD schemes is shown in the *Sweby Diagram* opposite, and plots showing limiter functions overlaid onto the TVD region are shown below. In this image, plots for the Osher and Sweby limiters have been generated using $\beta =1.5$ .

### Generalised minmod limiter

An additional limiter that has an interesting form is the van-Leer's one-parameter family of minmod limiters. It is defined as follows $\phi _{mg}(r,\theta )=\max \left(0,\min \left(\theta r,{\frac {1+r}{2}},\theta \right)\right),\quad \theta \in \left[1,2\right].$

**Note:** $\phi _{mg}$ is most dissipative for $\theta =1,$ when it reduces to $\phi _{mm},$ and is least dissipative for $\theta =2$ .
