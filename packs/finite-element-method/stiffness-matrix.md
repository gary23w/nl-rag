---
title: "Stiffness matrix"
source: https://en.wikipedia.org/wiki/Stiffness_matrix
domain: finite-element-method
license: CC-BY-SA-4.0
tags: finite element method, galerkin method, stiffness matrix, weak formulation
fetched: 2026-07-02
---

# Stiffness matrix

In the finite element method for the numerical solution of elliptic partial differential equations, the **stiffness matrix** is a matrix that represents the system of linear equations that must be solved in order to ascertain an approximate solution to the differential equation.

## The stiffness matrix for the Poisson problem

For simplicity, we will first consider the Poisson problem

$-\nabla ^{2}u=f$

on some domain Ω, subject to the boundary condition *u* = 0 on the boundary of Ω. To discretize this equation by the finite element method, one chooses a set of *basis functions* {*φ*1, …, *φn*} defined on Ω which also vanish on the boundary. One then approximates

$u\approx u^{h}=u_{1}\varphi _{1}+\cdots +u_{n}\varphi _{n}.$

The coefficients *u*1, *u*2, …, *un* are determined so that the error in the approximation is orthogonal to each basis function φi:

$\int _{\Omega }\varphi _{i}\cdot f\,dx=-\int _{\Omega }\varphi _{i}\nabla ^{2}u^{h}\,dx=-\sum _{j}\left(\int _{\Omega }\varphi _{i}\nabla ^{2}\varphi _{j}\,dx\right)\,u_{j}=\sum _{j}\left(\int _{\Omega }\nabla \varphi _{i}\cdot \nabla \varphi _{j}\,dx\right)u_{j}.$

as a consequence of the homogenous Dirichlet boundary conditions. The **stiffness matrix** is the n-element square matrix **A** defined by

$\mathbf {A} _{ij}=\int _{\Omega }\nabla \varphi _{i}\cdot \nabla \varphi _{j}\,dx.$

By defining the *load vector* **F** with components ${\textstyle \mathbf {F} _{i}=\int _{\Omega }\varphi _{i}f\,dx,}$ the coefficients ui are determined by the linear system **Au** = **F**. The stiffness matrix is symmetric, i.e. **A***ij* = **A***ji*, so all its eigenvalues are real. Moreover, it is a strictly positive-definite matrix, so that the system **Au** = **F** always has a unique solution. (For other problems, these nice properties will be lost.)

Note that the stiffness matrix will be different depending on the computational grid used for the domain and what type of finite element is used. For example, the stiffness matrix when piecewise quadratic finite elements are used will have more degrees of freedom than piecewise linear elements.

## The stiffness matrix for other problems

Determining the stiffness matrix for other PDEs follows essentially the same procedure, but it can be complicated by the choice of boundary conditions. As a more complex example, consider the elliptic equation

$-\sum _{k,l}{\frac {\partial }{\partial x_{k}}}\left(a^{kl}{\frac {\partial u}{\partial x_{l}}}\right)=f$

where $\mathbf {A} (x)=a^{kl}(x)$ is a positive-definite matrix defined for each point x in the domain. We impose the Robin boundary condition

$-\sum _{k,l}\nu _{k}a^{kl}{\frac {\partial u}{\partial x_{l}}}=c(u-g),$

where νk is the component of the unit outward normal vector ν in the k-th direction. The system to be solved is

$\sum _{j}\left(\sum _{k,l}\int _{\Omega }a^{kl}{\frac {\partial \varphi _{i}}{\partial x_{k}}}{\frac {\partial \varphi _{j}}{\partial x_{l}}}dx+\int _{\partial \Omega }c\varphi _{i}\varphi _{j}\,ds\right)u_{j}=\int _{\Omega }\varphi _{i}f\,dx+\int _{\partial \Omega }c\varphi _{i}g\,ds,$

as can be shown using an analogue of Green's identity. The coefficients ui are still found by solving a system of linear equations, but the matrix representing the system is markedly different from that for the ordinary Poisson problem.

In general, to each scalar elliptic operator L of order 2*k*, there is associated a bilinear form B on the Sobolev space Hk, so that the weak formulation of the equation *Lu* = *f* is

$B[u,v]=(f,v)$

for all functions v in Hk. Then the stiffness matrix for this problem is

$\mathbf {A} _{ij}=B[\varphi _{j},\varphi _{i}].$

## Practical assembly of the stiffness matrix

In order to implement the finite element method on a computer, one must first choose a set of basis functions and then compute the integrals defining the stiffness matrix. Usually, the domain Ω is discretized by some form of mesh generation, wherein it is divided into non-overlapping triangles or quadrilaterals, which are generally referred to as elements. The basis functions are then chosen to be polynomials of some order within each element, and continuous across element boundaries. The simplest choices are piecewise linear for triangular elements and piecewise bilinear for rectangular elements.

The **element stiffness matrix** **A**[*k*] for element Tk is the matrix

$\mathbf {A} _{ij}^{[k]}=\int _{T_{k}}\nabla \varphi _{i}\cdot \nabla \varphi _{j}\,dx.$

The element stiffness matrix is zero for most values of i and j, for which the corresponding basis functions are zero within Tk. The full stiffness matrix **A** is the sum of the element stiffness matrices. In particular, for basis functions that are only supported locally, the stiffness matrix is sparse.

For many standard choices of basis functions, i.e. piecewise linear basis functions on triangles, there are simple formulas for the element stiffness matrices. For example, for piecewise linear elements, consider a triangle with vertices (*x*1, *y*1), (*x*2, *y*2), (*x*3, *y*3), and define the 2×3 matrix

$\mathbf {D} =\left[{\begin{matrix}x_{3}-x_{2}&x_{1}-x_{3}&x_{2}-x_{1}\\y_{3}-y_{2}&y_{1}-y_{3}&y_{2}-y_{1}\end{matrix}}\right].$

Then the element stiffness matrix is

$\mathbf {A} ^{[k]}={\frac {\mathbf {D} ^{\mathsf {T}}\mathbf {D} }{4\operatorname {area} (T)}}.$

When the differential equation is more complicated, say by having an inhomogeneous diffusion coefficient, the integral defining the element stiffness matrix can be evaluated by Gaussian quadrature.

The condition number of the stiffness matrix depends strongly on the quality of the numerical grid. In particular, triangles with small angles in the finite element mesh induce large eigenvalues of the stiffness matrix, degrading the solution quality.
