---
title: "Multiple-scale analysis"
source: https://en.wikipedia.org/wiki/Multiple-scale_analysis
domain: perturbation-theory
license: CC-BY-SA-4.0
tags: perturbation theory, method of averaging, multiple-scale analysis, adiabatic theorem
fetched: 2026-07-02
---

# Multiple-scale analysis

In mathematics and physics, **multiple-scale analysis** (also called the **method of multiple scales**) comprises techniques used to construct uniformly valid approximations to the solutions of perturbation problems, both for small as well as large values of the independent variables. This is done by introducing fast-scale and slow-scale variables for an independent variable, and subsequently treating these variables, fast and slow, as if they are independent. In the solution process of the perturbation problem thereafter, the resulting additional freedom – introduced by the new independent variables – is used to remove (unwanted) secular terms. The latter puts constraints on the approximate solution, which are called **solvability conditions**.

Mathematics research from about the 1980s proposes that coordinate transforms and invariant manifolds provide a sounder support for multiscale modelling (for example, see center manifold and slow manifold).

## Example: undamped Duffing equation

### Differential equation and energy conservation

As an example for the method of multiple-scale analysis, consider the undamped and unforced Duffing equation: ${\frac {d^{2}y}{dt^{2}}}+y+\varepsilon y^{3}=0,$ $y(0)=1,\qquad {\frac {dy}{dt}}(0)=0,$ which is a second-order ordinary differential equation describing a nonlinear oscillator. A solution *y*(*t*) is sought for small values of the (positive) nonlinearity parameter 0 < *ε* ≪ 1. The undamped Duffing equation is known to be a Hamiltonian system: ${\frac {dp}{dt}}=-{\frac {\partial H}{\partial q}},\qquad {\frac {dq}{dt}}=+{\frac {\partial H}{\partial p}},\quad {\text{ with }}\quad H={\tfrac {1}{2}}p^{2}+{\tfrac {1}{2}}q^{2}+{\tfrac {1}{4}}\varepsilon q^{4},$ with *q* = *y*(*t*) and *p* = *dy*/*dt*. Consequently, the Hamiltonian *H*(*p*, *q*) is a conserved quantity, a constant, equal to *H0* = ⁠1/2⁠ + ⁠1/4⁠ *ε* for the given initial conditions. This implies that both *q* and *p* have to be bounded: $\left|q\right|\leq {\sqrt {1+{\tfrac {1}{2}}\varepsilon }}\quad {\text{ and }}\quad \left|p\right|\leq {\sqrt {1+{\tfrac {1}{2}}\varepsilon }}\qquad {\text{ for all }}t.$ The bound on q is found by equating H with p = 0 to H0: ${\tfrac {1}{2}}q^{2}+{\tfrac {1}{4}}\varepsilon q^{4}={\tfrac {1}{2}}+{\tfrac {1}{4}}\varepsilon$ , and then dropping the q4 term. This is indeed an upper bound on |q|, though keeping the q4 term gives a smaller bound with a more complicated formula.

### Straightforward perturbation-series solution

A regular perturbation-series approach to the problem proceeds by writing ${\textstyle y(t)=y_{0}(t)+\varepsilon y_{1}(t)+{\mathcal {O}}(\varepsilon ^{2})}$ and substituting this into the undamped Duffing equation. Matching powers of ${\textstyle \varepsilon }$ gives the system of equations ${\begin{aligned}{\frac {d^{2}y_{0}}{dt^{2}}}+y_{0}&=0,\\{\frac {d^{2}y_{1}}{dt^{2}}}+y_{1}&=-y_{0}^{3}.\end{aligned}}$

Solving these subject to the initial conditions yields $y(t)=\cos(t)+\varepsilon \left[{\tfrac {1}{32}}\cos(3t)-{\tfrac {1}{32}}\cos(t)-\underbrace {{\tfrac {3}{8}}\,t\,\sin(t)} _{\text{secular}}\right]+{\mathcal {O}}(\varepsilon ^{2}).$

Note that the last term between the square braces is secular: it grows without bound for large |*t*|. In particular, for $t=O(\varepsilon ^{-1})$ this term is *O*(1) and has the same order of magnitude as the leading-order term. Because the terms have become disordered, the series is no longer an asymptotic expansion of the solution.

### Method of multiple scales

To construct a solution that is valid beyond $t=O(\epsilon ^{-1})$ , the method of *multiple-scale analysis* is used. Introduce the slow scale *t*1: $t_{1}=\varepsilon t$ and assume the solution *y*(*t*) is a perturbation-series solution dependent both on *t* and *t*1, treated as: $y(t)=Y_{0}(t,t_{1})+\varepsilon Y_{1}(t,t_{1})+\cdots .$

So: ${\begin{aligned}{\frac {dy}{dt}}&=\left({\frac {\partial Y_{0}}{\partial t}}+{\frac {dt_{1}}{dt}}{\frac {\partial Y_{0}}{\partial t_{1}}}\right)+\varepsilon \left({\frac {\partial Y_{1}}{\partial t}}+{\frac {dt_{1}}{dt}}{\frac {\partial Y_{1}}{\partial t_{1}}}\right)+\cdots \\&={\frac {\partial Y_{0}}{\partial t}}+\varepsilon \left({\frac {\partial Y_{0}}{\partial t_{1}}}+{\frac {\partial Y_{1}}{\partial t}}\right)+{\mathcal {O}}(\varepsilon ^{2}),\end{aligned}}$ using *dt*1/*dt* = *ε*. Similarly: ${\frac {d^{2}y}{dt^{2}}}={\frac {\partial ^{2}Y_{0}}{\partial t^{2}}}+\varepsilon \left(2{\frac {\partial ^{2}Y_{0}}{\partial t\,\partial t_{1}}}+{\frac {\partial ^{2}Y_{1}}{\partial t^{2}}}\right)+{\mathcal {O}}(\varepsilon ^{2}).$

Then the zeroth- and first-order problems of the multiple-scales perturbation series for the Duffing equation become: ${\begin{aligned}{\frac {\partial ^{2}Y_{0}}{\partial t^{2}}}+Y_{0}&=0,\\{\frac {\partial ^{2}Y_{1}}{\partial t^{2}}}+Y_{1}&=-Y_{0}^{3}-2\,{\frac {\partial ^{2}Y_{0}}{\partial t\,\partial t_{1}}}.\end{aligned}}$

### Solution

The zeroth-order problem has the general solution: $Y_{0}(t,t_{1})=A(t_{1})\,e^{+it}+A^{\ast }(t_{1})\,e^{-it},$ with *A*(*t*1) a complex-valued amplitude to the zeroth-order solution *Y*0(*t*, *t*1) and *i*2 = −1. Now, in the first-order problem the forcing in the right hand side of the differential equation is $\left[-3\,A^{2}\,A^{\ast }-2\,i\,{\frac {dA}{dt_{1}}}\right]\,e^{+it}-A^{3}\,e^{+3it}+c.c.$ where *c.c.* denotes the complex conjugate of the preceding terms. The occurrence of *secular terms* can be prevented by imposing on the – yet unknown – amplitude *A*(*t*1) the *solvability condition* $-3\,A^{2}\,A^{\ast }-2\,i\,{\frac {dA}{dt_{1}}}=0.$

The solution to the solvability condition, also satisfying the initial conditions *y*(0) = 1 and *dy*/*dt*(0) = 0, is: $A={\tfrac {1}{2}}\,\exp \left({\tfrac {3}{8}}\,i\,t_{1}\right).$

As a result, the approximate solution by the multiple-scales analysis is $y(t)=\cos \left[\left(1+{\tfrac {3}{8}}\,\varepsilon \right)t\right]+{\mathcal {O}}(\varepsilon ),$ using *t*1 = *εt* and valid for *εt* = O(1). This agrees with the nonlinear frequency changes found by employing the Lindstedt–Poincaré method.

This new solution is valid until $t=O(\epsilon ^{-2})$ . Higher-order solutions – using the method of multiple scales – require the introduction of additional slow scales, i.e., *t*2 = *ε*2 *t*, *t*3 = *ε*3 *t*, etc. However, this introduces possible ambiguities in the perturbation series solution, which require a careful treatment (see Kevorkian & Cole 1996; Bender & Orszag 1999).

### Coordinate transform to amplitude/phase variables

Alternatively, modern approaches derive these sorts of models using coordinate transforms, like in the method of normal forms, as described next.

A solution $y\approx r\cos \theta$ is sought in new coordinates $(r,\theta )$ where the amplitude $r(t)$ varies slowly and the phase $\theta (t)$ varies at an almost constant rate, namely $d\theta /dt\approx 1.$ Straightforward algebra finds the coordinate transform $y=r\cos \theta +{\frac {1}{32}}\varepsilon r^{3}\cos 3\theta +{\frac {1}{1024}}\varepsilon ^{2}r^{5}(-21\cos 3\theta +\cos 5\theta )+{\mathcal {O}}(\varepsilon ^{3})$ transforms Duffing's equation into the pair that the radius is constant $dr/dt=0$ and the phase evolves according to ${\frac {d\theta }{dt}}=1+{\frac {3}{8}}\varepsilon r^{2}-{\frac {15}{256}}\varepsilon ^{2}r^{4}+{\mathcal {O}}(\varepsilon ^{3}).$

That is, Duffing's oscillations are of constant amplitude r but have different frequencies $d\theta /dt$ depending upon the amplitude.

More difficult examples are better treated using a time-dependent coordinate transform involving complex exponentials (as also invoked in the previous multiple time-scale approach). A web service will perform the analysis for a wide range of examples.
