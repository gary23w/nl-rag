---
title: "Numerical continuation"
source: https://en.wikipedia.org/wiki/Numerical_continuation
domain: continuation-methods
license: CC-BY-SA-4.0
tags: numerical continuation, homotopy continuation, bifurcation theory, predictor-corrector method
fetched: 2026-07-02
---

# Numerical continuation

**Numerical continuation** is a method of computing approximate solutions of a system of parameterized nonlinear equations,

$F(\mathbf {u} ,\lambda )=0.$

The parameter $\lambda$ is usually a real scalar and the *solution* $\mathbf {u}$ is an *n*-vector. For a fixed parameter value $\lambda$ , ${\textstyle F(\cdot ,\lambda )}$ maps Euclidean n-space into itself.

Often the original mapping F is from a Banach space into itself, and the Euclidean n-space is a finite-dimensional Banach space.

A steady state, or fixed point, of a parameterized family of flows or maps are of this form, and by discretizing trajectories of a flow or iterating a map, periodic orbits and heteroclinic orbits can also be posed as a solution of $F=0$ .

## Other forms

In some nonlinear systems, parameters are explicit. In others they are implicit, and the system of nonlinear equations is written

$F(\mathbf {u} )=0$

where $\mathbf {u}$ is an *n*-vector, and its image $F(\mathbf {u} )$ is an *n*−1 vector.

This formulation, without an explicit parameter space is not usually suitable for the formulations in the following sections, because they refer to parameterized autonomous nonlinear dynamical systems of the form:

$\mathbf {u} '=F(\mathbf {u} ,\lambda ).$

However, in an algebraic system there is no distinction between unknowns $\mathbf {u}$ and the parameters.

## Periodic motions

A periodic motion is a closed curve in phase space. That is, for some *period* T ,

$\mathbf {u} '=F(\mathbf {u} ,\lambda ),\,\mathbf {u} (0)=\mathbf {u} (T).$

The textbook example of a periodic motion is the undamped pendulum.

If the phase space is periodic in one or more coordinates, say $\mathbf {u} (t)=\mathbf {u} (t+\Omega )$ , with $\Omega$ a vector , then there is a second kind of periodic motions defined by

$\mathbf {u} '=\mathbf {F} (\mathbf {u} ,\lambda ),\,\mathbf {u} (0)=\mathbf {u} (T+N.\Omega )$

for every integer N .

The first step in writing an implicit system for a periodic motion is to move the period T from the boundary conditions to the ODE:

$\mathbf {u} '=T\mathbf {F} (\mathbf {u} ,\lambda ),\,\mathbf {u} (0)=\mathbf {u} (1+N.\Omega ).$

The second step is to add an additional equation, a *phase constraint*, that can be thought of as determining the period. This is necessary because any solution of the above boundary value problem can be shifted in time by an arbitrary amount (time does not appear in the defining equations—the dynamical system is called autonomous).

There are several choices for the phase constraint. If $\mathbf {u} _{0}(t)$ is a known periodic orbit at a parameter value $\lambda _{0}$ near $\lambda$ , then, Poincaré used

$\langle \mathbf {u} (0)-\mathbf {u} _{0}(0),\mathbf {F} (\mathbf {u} _{0}(0),\lambda _{0})\rangle =0.$

which states that $\mathbf {u}$ lies in a plane which is orthogonal to the tangent vector of the closed curve. This plane is called a *Poincaré section*.

For a general problem a better phase constraint is an integral constraint introduced by Eusebius Doedel, which chooses the phase so that the distance between the known and unknown orbits is minimized:

$\int _{0}^{1}\langle \mathbf {u} (t)-\mathbf {u} _{0}(t),\mathbf {F} (\mathbf {u} _{0}(t),\lambda _{0})\rangle dt=0.$

## Homoclinic and heteroclinic motions

## Definitions

### Solution component

A solution component $\Gamma (\mathbf {u} _{0},\lambda _{0})$ of the nonlinear system F is a set of points $(\mathbf {u} ,\lambda )$ which satisfy $F(\mathbf {u} ,\lambda )=0$ and are *connected* to the initial solution $(\mathbf {u} _{0},\lambda _{0})$ by a path of solutions $(\mathbf {u} (s),\lambda (s))$ for which $(\mathbf {u} (0),\lambda (0))=(\mathbf {u} _{0},\lambda _{0}),\,(\mathbf {u} (1),\lambda (1))=(\mathbf {u} ,\lambda )$ and $F(\mathbf {u} (s),\lambda (s))=0$ .

### Numerical continuation

A numerical continuation is an algorithm which takes as input a system of parametrized nonlinear equations and an initial solution $(\mathbf {u} _{0},\lambda _{0})$ , $F(\mathbf {u} _{0},\lambda _{0})=0$ , and produces a set of points on the solution component $\Gamma (\mathbf {u} _{0},\lambda _{0})$ .

### Regular point

A regular point of F is a point $(\mathbf {u} ,\lambda )$ at which the Jacobian of F is full rank $(n)$ .

Near a regular point the solution component is an isolated curve passing through the regular point (the implicit function theorem). In the figure above the point $(\mathbf {u} _{0},\lambda _{0})$ is a regular point.

### Singular point

A singular point of F is a point $(\mathbf {u} ,\lambda )$ at which the Jacobian of F is not full rank.

Near a singular point the solution component may not be an isolated curve passing through the regular point. The local structure is determined by higher derivatives of F . In the figure above the point where the two blue curves cross is a singular point.

In general solution components $\Gamma$ are branched curves. The branch points are singular points. Finding the solution curves leaving a singular point is called branch switching, and uses techniques from bifurcation theory (singularity theory, catastrophe theory).

For finite-dimensional systems (as defined above) the Lyapunov-Schmidt decomposition may be used to produce two systems to which the Implicit Function Theorem applies. The Lyapunov-Schmidt decomposition uses the restriction of the system to the complement of the null space of the Jacobian and the range of the Jacobian.

If the columns of the matrix $\Phi$ are an orthonormal basis for the null space of

$J=\left[{\begin{array}{cc}F_{x}&F_{\lambda }\\\end{array}}\right]$

and the columns of the matrix $\Psi$ are an orthonormal basis for the left null space of J , then the system $F(x,\lambda )=0$ can be rewritten as

$\left[{\begin{array}{l}(I-\Psi \Psi ^{T})F(x+\Phi \xi +\eta )\\\Psi ^{T}F(x+\Phi \xi +\eta )\\\end{array}}\right]=0,$

where $\eta$ is in the complement of the null space of J $(\Phi ^{T}\,\eta =0)$ .

In the first equation, which is parametrized by the null space of the Jacobian ( $\xi$ ), the Jacobian with respect to $\eta$ is non-singular. So the implicit function theorem states that there is a mapping $\eta (\xi )$ such that $\eta (0)=0$ and $(I-\Psi \Psi ^{T})F(x+\Phi \xi +\eta (\xi ))=0)$ . The second equation (with $\eta (\xi )$ substituted) is called the bifurcation equation (though it may be a system of equations).

The bifurcation equation has a Taylor expansion which lacks the constant and linear terms. By scaling the equations and the null space of the Jacobian of the original system a system can be found with non-singular Jacobian. The constant term in the Taylor series of the scaled bifurcation equation is called the algebraic bifurcation equation, and the implicit function theorem applied the bifurcation equations states that for each isolated solution of the algebraic bifurcation equation there is a branch of solutions of the original problem which passes through the singular point.

Another type of singular point is a turning point bifurcation, or saddle-node bifurcation, where the direction of the parameter $\lambda$ reverses as the curve is followed. The red curve in the figure above illustrates a turning point.

## Particular algorithms

### Natural parameter continuation

Most methods of solution of nonlinear systems of equations are iterative methods. For a particular parameter value $\lambda _{0}$ a mapping is repeatedly applied to an initial guess $\mathbf {u} _{0}$ . If the method converges, and is consistent, then in the limit the iteration approaches a solution of $F(\mathbf {u} ,\lambda _{0})=0$ .

*Natural parameter continuation* is a very simple adaptation of the iterative solver to a parametrized problem. The solution at one value of $\lambda$ is used as the initial guess for the solution at $\lambda +\Delta \lambda$ . With $\Delta \lambda$ sufficiently small the iteration applied to the initial guess should converge.

One advantage of natural parameter continuation is that it uses the solution method for the problem as a black box. All that is required is that an initial solution be given (some solvers used to always start at a fixed initial guess). There has been a lot of work in the area of large scale continuation on applying more sophisticated algorithms to black box solvers (see e.g. LOCA).

However, natural parameter continuation fails at turning points, where the branch of solutions turns round. So for problems with turning points, a more sophisticated method such as pseudo-arclength continuation must be used (see below).

### Simplicial or piecewise linear continuation

Simplicial Continuation, or Piecewise Linear Continuation (Allgower and Georg) is based on three basic results.

The first is

| If $F(x)$ maps $\mathbb {R} ^{n}$ into $\mathbb {R} ^{n-1}$ , there is a unique linear interpolant on an $(n-1)$ -dimensional simplex which agrees with the function values at the vertices of the simplex. |
|---|

The second result is:

| An $(n-1)$ -dimensional simplex can be tested to determine if the unique linear interpolant takes on the value 0 inside the simplex. |
|---|

Please see the article on piecewise linear continuation for details.

With these two operations this continuation algorithm is easy to state (although of course an efficient implementation requires a more sophisticated approach. See [B1]). An initial simplex is assumed to be given, from a reference simplicial decomposition of $\mathbb {R} ^{n}$ . The initial simplex must have at least one face which contains a zero of the unique linear interpolant on that face. The other faces of the simplex are then tested, and typically there will be one additional face with an interior zero. The initial simplex is then replaced by the simplex which lies across either face containing zero, and the process is repeated.

References: Allgower and Georg [B1] provides a crisp, clear description of the algotihm.

### Pseudo-arclength continuation

This method is based on the observation that the "ideal" parameterization of a curve is arclength. Pseudo-arclength is an approximation of the arclength in the tangent space of the curve. The resulting modified natural continuation method makes a step in pseudo-arclength (rather than $\lambda$ ). The iterative solver is required to find a point at the given pseudo-arclength, which requires appending an additional constraint (the pseudo-arclength constraint) to the n by $n+1$ Jacobian. It produces a square Jacobian, and if the stepsize is sufficiently small the modified Jacobian is full rank.

Pseudo-arclength continuation was independently developed by Edward Riks and Gerald Wempner for finite element applications in the late 1960s, and published in journals in the early 1970s by H.B. Keller. A detailed account of these early developments is provided in the textbook by M. A. Crisfield: Nonlinear Finite Element Analysis of Solids and Structures, Vol 1: Basic Concepts, Wiley, 1991. Crisfield was one of the most active developers of this class of methods, which are by now standard procedures of commercial nonlinear finite element programs.

The algorithm is a predictor-corrector method. The prediction step finds the point $(u,\lambda )=(u_{0},\lambda _{0})+\Delta s\cdot ({\dot {u}}_{0},{\dot {\lambda }}_{0})$ (in $\mathbb {R} ^{n+1}$ ) which is a step of size $\Delta s$ along the tangent vector $({\dot {u}}_{0},{\dot {\lambda }}_{0})$ . The prediction is corrected by searching in the direction transverse to the tangent vector. Usually, Newton's method is used to solve the nonlinear system

${\begin{array}{l}F(u,\lambda )=0\\{\dot {u}}_{0}(u-u_{0})+{\dot {\lambda }}_{0}(\lambda -\lambda _{0})=\Delta s\\\end{array}}$

with initial guess $(u,\lambda )=(u_{0},\lambda _{0})+\Delta s\cdot ({\dot {u}}_{0},{\dot {\lambda }}_{0})$ . The Jacobian of this system is the bordered matrix

$\left[{\begin{array}{cc}F_{u}&F_{\lambda }\\{\dot {u}}^{*}&{\dot {\lambda }}\\\end{array}}\right]$

At regular points, where the unmodified Jacobian is full rank, the tangent vector spans the null space of the top row of this new Jacobian. Appending the tangent vector as the last row can be seen as determining the coefficient of the null vector in the general solution of the Newton system (particular solution plus an arbitrary multiple of the null vector).

### Gauss–Newton continuation

This method is a variant of pseudo-arclength continuation. Instead of using the tangent at the initial point in the arclength constraint, the tangent at the current solution is used. This is equivalent to using the pseudo-inverse of the Jacobian in Newton's method, and allows longer steps to be made. [B17]

## Continuation in more than one parameter

The parameter $\lambda$ in the algorithms described above is a real scalar. Most physical and design problems generally have many more than one parameter. Higher-dimensional continuation refers to the case when $\lambda$ is a k-vector.

The same terminology applies. A **regular solution** is a solution at which the Jacobian is full rank $(n)$ . A singular solution is a solution at which the Jacobian is less than full rank.

A regular solution lies on a k-dimensional surface, which can be parameterized by a point in the tangent space (the null space of the Jacobian). This is again a straightforward application of the Implicit Function Theorem.

## Applications of numerical continuation techniques

Numerical continuation techniques have found a great degree of acceptance in the study of chaotic dynamical systems and various other systems which belong to the realm of catastrophe theory. The reason for such usage stems from the fact that various non-linear dynamical systems behave in a deterministic and predictable manner within a range of parameters which are included in the equations of the system. However, for a certain parameter value the system starts behaving chaotically and hence it became necessary to follow the parameter in order to be able to decipher the occurrences of when the system starts being non-predictable, and what exactly (theoretically) makes the system become unstable.

Analysis of parameter continuation can lead to more insights about stable/critical point bifurcations. Study of saddle-node, transcritical, pitch-fork, period doubling, Hopf, secondary Hopf (Neimark) bifurcations of stable solutions allows for a theoretical discussion of the circumstances and occurrences which arise at the critical points. Parameter continuation also gives a more dependable system to analyze a dynamical system as it is more stable than more interactive, time-stepped numerical solutions. Especially in cases where the dynamical system is prone to blow-up at certain parameter values (or combination of values for multiple parameters).

It is extremely insightful as to the presence of stable solutions (attracting or repelling) in the study of nonlinear differential equations where time stepping in the form of the Crank Nicolson algorithm is extremely time consuming as well as unstable in cases of nonlinear growth of the dependent variables in the system. The study of turbulence is another field where the Numerical Continuation techniques have been used to study the advent of turbulence in a system starting at low Reynolds numbers. Also, research using these techniques has provided the possibility of finding stable manifolds and bifurcations to invariant-tori in the case of the restricted three-body problem in Newtonian gravity and have also given interesting and deep insights into the behaviour of systems such as the Lorenz equations.

## Software

(Under Construction) See also The SIAM Activity Group on Dynamical Systems' list http://www.dynamicalsystems.org/sw/sw/

- AUTO: Computation of the solutions of Two Point Boundary Value Problems (TPBVPs) with integral constraints. https://sourceforge.net/projects/auto-07p/ Available on SourceForge.
- HOMCONT: Computation of homoclinic and heteroclinic orbits. Included in AUTO
- MATCONT: Matlab toolbox for numerical continuation and bifurcation [1]Available on SourceForge.
- DDEBIFTOOL: Computation of solutions of Delay Differential Equations. A MATLAB package. Available from K. U. Leuven
- PyCont: A Python toolbox for numerical continuation and bifurcation. Native Python algorithms for fixed point continuation, sophisticated interface to AUTO for other types of problem. Included as part of PyDSTool
- CANDYS/QA: Available from the Universität Potsdam [A16]
- MANPAK: Available from Netlib [A15]
- PDDE-CONT: http://seis.bris.ac.uk/~rs1909/pdde/
- multifario: http://multifario.sourceforge.net/
- LOCA: https://trilinos.org/packages/nox-and-loca/
- DSTool
- GAIO
- OSCILL8: Oscill8 is a dynamical systems tool that allows a user to explore high-dimensional parameter space of nonlinear ODEs using bifurcation analytic techniques. Available from SourceForge.
- MANLAB : Computation of equilibrium, periodic and quasi-periodic solution of differential equations using Fourier series (harmonic balance method) developments of the solution and Taylor series developments (asymptotic numerical method) of the solution branch. Available from LMA Marseille.
- BifurcationKit.jl : This Julia package aims at performing automatic bifurcation analysis of large dimensional equations F(u,λ)=0 where $\lambda \in \mathbb {R}$ by taking advantage of iterative methods, sparse formulation and specific hardwares (e.g. GPU). [2]
- COCO: Continuation Core and Toolboxes. Development platform and toolboxes for parameter continuation, e.g., bifurcation analysis of dynamical systems and constrained design optimization. Available from SourceForge

## Examples

This problem, of finding the points which *F* maps into the origin appears in computer graphics as the problems of drawing contour maps (n=2), or isosurface (n=3). The contour with value *h* is the set of all solution components of *F-h=0*
