---
title: "Meshfree methods"
source: https://en.wikipedia.org/wiki/Meshfree_methods
domain: smoothed-particle-hydrodynamics
license: CC-BY-SA-4.0
tags: smoothed-particle hydrodynamics, meshfree methods, fluid simulation, multiphase flow
fetched: 2026-07-02
---

# Meshfree methods

In the field of numerical analysis, **meshfree methods** are those that do not require connection between nodes of the simulation domain, i.e. a mesh, but are rather based on interaction of each node with all its neighbors. As a consequence, original extensive properties such as mass or kinetic energy are no longer assigned to mesh elements but rather to the single nodes. Meshfree methods enable the simulation of some otherwise difficult types of problems, at the cost of extra computing time and programming effort. The absence of a mesh allows Lagrangian simulations, in which the nodes can move according to the velocity field.

## Motivation

Numerical methods such as the finite difference method, finite-volume method, and finite element method were originally defined on meshes of data points. In such a mesh, each point has a fixed number of predefined neighbors, and this connectivity between neighbors can be used to define mathematical operators like the derivative. These operators are then used to construct the equations to simulate—such as the Euler equations or the Navier–Stokes equations.

But in simulations where the material being simulated can move around (as in computational fluid dynamics) or where large deformations of the material can occur (as in simulations of plastic materials), the connectivity of the mesh can be difficult to maintain without introducing error into the simulation. If the mesh becomes tangled or degenerate during simulation, the operators defined on it may no longer give correct values. The mesh may be recreated during simulation (a process called remeshing), but this can also introduce error, since all the existing data points must be mapped onto a new and different set of data points. Meshfree methods are intended to remedy these problems. Meshfree methods are also useful for:

- Simulations where creating a useful mesh from the geometry of a complex 3D object may be especially difficult or require human assistance
- Simulations where nodes may be created or destroyed, such as in cracking simulations
- Simulations where the problem geometry may move out of alignment with a fixed mesh, such as in bending simulations
- Simulations containing nonlinear material behavior, discontinuities or singularities

## Example

In a traditional finite difference simulation, the domain of a one-dimensional simulation would be some function $u(x,t)$ , represented as a mesh of data values $u_{i}^{n}$ at points $x_{i}$ , where

$i=0,1,2...$

$n=0,1,2...$

$x_{i+1}-x_{i}=h\ \forall i$

$t_{n+1}-t_{n}=k\ \forall n$

We can define the derivatives that occur in the equation being simulated using some finite difference formulae on this domain, for example

${\partial u \over \partial x}={u_{i+1}^{n}-u_{i-1}^{n} \over 2h}$

and

${\partial u \over \partial t}={u_{i}^{n+1}-u_{i}^{n} \over k}$

Then we can use these definitions of $u(x,t)$ and its spatial and temporal derivatives to write the equation being simulated in finite difference form, then simulate the equation with one of many finite difference methods.

In this simple example, the steps (here the spatial step h and timestep k ) are constant along all the mesh, and the left and right mesh neighbors of the data value at $x_{i}$ are the values at $x_{i-1}$ and $x_{i+1}$ , respectively. Generally in finite differences one can allow very simply for steps variable along the mesh, but all the original nodes should be preserved and they can move independently only by deforming the original elements. If even only two of all the nodes change their order, or even only one node is added to or removed from the simulation, that creates a defect in the original mesh and the simple finite difference approximation can no longer hold.

Smoothed-particle hydrodynamics (SPH), one of the oldest meshfree methods, solves this problem by treating data points as physical particles with mass and density that can move around over time, and carry some value $u_{i}$ with them. SPH then defines the value of $u(x,t)$ between the particles by

$u(x,t_{n})=\sum _{i}m_{i}{\frac {u_{i}^{n}}{\rho _{i}}}W(|x-x_{i}|)$

where $m_{i}$ is the mass of particle i , $\rho _{i}$ is the density of particle i , and W is a kernel function that operates on nearby data points and is chosen for smoothness and other useful qualities. By linearity, we can write the spatial derivative as

${\partial u \over \partial x}=\sum _{i}m_{i}{\frac {u_{i}^{n}}{\rho _{i}}}{\partial W(|x-x_{i}|) \over \partial x}$

Then we can use these definitions of $u(x,t)$ and its spatial derivatives to write the equation being simulated as an ordinary differential equation, and simulate the equation with one of many numerical methods. In physical terms, this means calculating the forces between the particles, then integrating these forces over time to determine their motion.

The advantage of SPH in this situation is that the formulae for $u(x,t)$ and its derivatives do not depend on any adjacency information about the particles; they can use the particles in any order, so it doesn't matter if the particles move around or even exchange places.

One disadvantage of SPH is that it requires extra programming to determine the nearest neighbors of a particle. Since the kernel function W only returns nonzero results for nearby particles within twice the "smoothing length" (because we typically choose kernel functions with compact support), it would be a waste of effort to calculate the summations above over every particle in a large simulation. So typically SPH simulators require some extra code to speed up this nearest neighbor calculation.

## History

One of the earliest meshfree methods is smoothed particle hydrodynamics, presented in 1977. Libersky *et al.* were the first to apply SPH in solid mechanics. The main drawbacks of SPH are inaccurate results near boundaries and tension instability that was first investigated by Swegle.

In the 1990s a new class of meshfree methods emerged based on the Galerkin method. This first method called the diffuse element method (DEM), pioneered by Nayroles et al., utilized the MLS approximation in the Galerkin solution of partial differential equations, with approximate derivatives of the MLS function. Thereafter Belytschko pioneered the Element Free Galerkin (EFG) method, which employed MLS with Lagrange multipliers to enforce boundary conditions, higher order numerical quadrature in the weak form, and full derivatives of the MLS approximation which gave better accuracy. Around the same time, the reproducing kernel particle method (RKPM) emerged, the approximation motivated in part to correct the kernel estimate in SPH: to give accuracy near boundaries, in non-uniform discretizations, and higher-order accuracy in general. Notably, in a parallel development, the Material point methods were developed around the same time which offer similar capabilities. Material point methods are widely used in the movie industry to simulate large deformation solid mechanics, such as snow in the movie Frozen. RKPM and other meshfree methods were extensively developed by Chen, Liu, and Li in the late 1990s for a variety of applications and various classes of problems. During the 1990s and thereafter several other varieties were developed including those listed below.

## List of methods and acronyms

The following numerical methods are generally considered to fall within the general class of "meshfree" methods. Acronyms are provided in parentheses.

- Smoothed particle hydrodynamics (SPH) (1977)
- Diffuse element method (DEM) (1992)
- Dissipative particle dynamics (DPD) (1992)
- Element-free Galerkin method (EFG / EFGM) (1994)
- Reproducing kernel particle method (RKPM) (1995)
- Finite point method (FPM) (1996)
- Finite pointset method (FPM) (1998)
- hp-clouds
- Natural element method (NEM)
- Material point method (MPM)
- Meshless local Petrov Galerkin (MLPG) (1998)
- Generalized-strain mesh-free (GSMF) formulation (2016)
- Moving particle semi-implicit (MPS)
- Generalized finite difference method (GFDM)
- Particle-in-cell (PIC)
- Moving particle finite element method (MPFEM)
- Finite cloud method (FCM)
- Boundary node method (BNM)
- Meshfree moving Kriging interpolation method (MK)
- Boundary cloud method (BCM)
- Method of fundamental solutions (MFS)
- Method of particular solution (MPS)
- Method of finite spheres (MFS)
- Discrete vortex method (DVM)
- Reproducing Kernel Particle Method (RKPM) (1995)
- Generalized/Gradient Reproducing Kernel Particle Method (2011)
- Finite mass method (FMM) (2000)
- Smoothed point interpolation method (S-PIM) (2005).
- Meshfree local radial point interpolation method (RPIM).
- Local radial basis function collocation Method (LRBFCM)
- Viscous vortex domains method (VVD)
- Cracking Particles Method (CPM) (2004)
- Discrete least squares meshless method (DLSM) (2006)
- Immersed Particle Method (IPM) (2006)
- Optimal Transportation Meshfree method (OTM) (2010)
- Repeated replacement method (RRM) (2012)
- Radial basis integral equation method
- Least-square collocation meshless method (2001)
- Exponential Basis Functions method (EBFs) (2010)

Related methods:

- Moving least squares (MLS) – provide general approximation method for arbitrary set of nodes
- Partition of unity methods (PoUM) – provide general approximation formulation used in some meshfree methods
- Continuous blending method (enrichment and coupling of finite elements and meshless methods) – see Huerta & Fernández-Méndez (2000)
- eXtended FEM, Generalized FEM (XFEM, GFEM) – variants of FEM (finite element method) combining some meshless aspects
- Smoothed finite element method (S-FEM) (2007)
- Gradient smoothing method (GSM) (2008)
- Advancing front node generation (AFN)
- Local maximum-entropy (LME) – see Arroyo & Ortiz (2006)
- Space-Time Meshfree Collocation Method (STMCM) – see Netuzhylov (2008), Netuzhylov & Zilian (2009)
- Meshfree Interface-Finite Element Method (MIFEM) (2015) - a hybrid finite element-meshfree method for numerical simulation of phase transformation and multiphase flow problems

## Recent development

The primary areas of advancement in meshfree methods are to address issues with essential boundary enforcement, numerical quadrature, and contact and large deformations. The common weak form requires strong enforcement of the essential boundary conditions, yet meshfree methods in general lack the Kronecker delta property. This make essential boundary condition enforcement non-trivial, at least more difficult than the Finite element method, where they can be imposed directly. Techniques have been developed to overcome this difficulty and impose conditions strongly. Several methods have been developed to impose the essential boundary conditions weakly, including Lagrange multipliers, Nitche's method, and the penalty method.

As for quadrature, nodal integration is generally preferred which offers simplicity, efficiency, and keeps the meshfree method free of any mesh (as opposed to using Gauss quadrature, which necessitates a mesh to generate quadrature points and weights). Nodal integration however, suffers from numerical instability due to underestimation of strain energy associated with short-wavelength modes, and also yields inaccurate and non-convergent results due to under-integration of the weak form. One major advance in numerical integration has been the development of a stabilized conforming nodal integration (SCNI) which provides a nodal integration method which does not suffer from either of these problems. The method is based on strain-smoothing which satisfies the first order patch test. However, it was later realized that low-energy modes were still present in SCNI, and additional stabilization methods have been developed. This method has been applied to a variety of problems including thin and thick plates, poromechanics, convection-dominated problems, among others. More recently, a framework has been developed to pass arbitrary-order patch tests, based on a Petrov–Galerkin method.

One recent advance in meshfree methods aims at the development of computational tools for automation in modeling and simulations. This is enabled by the so-called weakened weak (W2) formulation based on the G space theory. The W2 formulation offers possibilities to formulate various (uniformly) "soft" models that work well with triangular meshes. Because a triangular mesh can be generated automatically, it becomes much easier in re-meshing and hence enables automation in modeling and simulation. In addition, W2 models can be made soft enough (in uniform fashion) to produce upper bound solutions (for force-driving problems). Together with stiff models (such as the fully compatible FEM models), one can conveniently bound the solution from both sides. This allows easy error estimation for generally complicated problems, as long as a triangular mesh can be generated. Typical W2 models are the Smoothed Point Interpolation Methods (or S-PIM). The S-PIM can be node-based (known as NS-PIM or LC-PIM), edge-based (ES-PIM), and cell-based (CS-PIM). The NS-PIM was developed using the so-called SCNI technique. It was then discovered that NS-PIM is capable of producing upper bound solution and volumetric locking free. The ES-PIM is found superior in accuracy, and CS-PIM behaves in between the NS-PIM and ES-PIM. Moreover, W2 formulations allow the use of polynomial and radial basis functions in the creation of shape functions (it accommodates the discontinuous displacement functions, as long as it is in G1 space), which opens further rooms for future developments. The W2 formulation has also led to the development of combination of meshfree techniques with the well-developed FEM techniques, and one can now use triangular mesh with excellent accuracy and desired softness. A typical such a formulation is the so-called smoothed finite element method (or S-FEM). The S-FEM is the linear version of S-PIM, but with most of the properties of the S-PIM and much simpler.

It is a general perception that meshfree methods are much more expensive than the FEM counterparts. The recent study has found however, some meshfree methods such as the S-PIM and S-FEM can be much faster than the FEM counterparts.

The S-PIM and S-FEM works well for solid mechanics problems. For CFD problems, the formulation can be simpler, via strong formulation. A Gradient Smoothing Methods (GSM) has also been developed recently for CFD problems, implementing the gradient smoothing idea in strong form. The GSM is similar to [FVM], but uses gradient smoothing operations exclusively in nested fashions, and is a general numerical method for PDEs.

Nodal integration has been proposed as a technique to use finite elements to emulate a meshfree behaviour. However, the obstacle that must be overcome in using nodally integrated elements is that the quantities at nodal points are not continuous, and the nodes are shared among multiple elements.
