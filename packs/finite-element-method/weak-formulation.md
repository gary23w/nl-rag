---
title: "Weak formulation"
source: https://en.wikipedia.org/wiki/Weak_formulation
domain: finite-element-method
license: CC-BY-SA-4.0
tags: finite element method, galerkin method, stiffness matrix, weak formulation
fetched: 2026-07-02
---

# Weak formulation

**Weak formulations** are tools for the analysis of mathematical equations that permit the transfer of concepts of linear algebra to solve problems in other fields such as partial differential equations. In a weak formulation, equations or conditions are no longer required to hold absolutely (and this is not even well defined) and has instead *weak solutions* only with respect to certain "test vectors" or "test functions". In a **strong formulation**, the solution space is constructed such that these equations or conditions are already fulfilled.

The **Lax–Milgram theorem**, named after Peter Lax and Arthur Milgram who proved it in 1954, provides weak formulations for certain systems on Hilbert spaces.

## General concept

Let V be a Banach space, let $V'$ be the dual space of V , let $A\colon V\to V'$ be a linear map, and let $f\in V'$ . A vector $u\in V$ is a solution of the equation

$Au=f$

if and only if for all $v\in V$ ,

$(Au)(v)=f(v).$

A particular choice of v is called a *test vector* (in general) or a *test function* (if V is a function space).

To bring this into the generic form of a weak formulation, find $u\in V$ such that

$a(u,v)=f(v)\quad \forall v\in V,$

by defining the bilinear form

$a(u,v):=(Au)(v).$

## Example 1: linear system of equations

Now, let $V=\mathbb {R} ^{n}$ and $A:V\to V$ be a linear mapping. Then, the weak formulation of the equation

$Au=f$

involves finding $u\in V$ such that for all $v\in V$ the following equation holds:

$\langle Au,v\rangle =\langle f,v\rangle ,$

where $\langle \cdot ,\cdot \rangle$ denotes an inner product.

Since A is a linear mapping, it is sufficient to test with basis vectors, and we get

$\langle Au,e_{i}\rangle =\langle f,e_{i}\rangle ,\quad i=1,\ldots ,n.$

Actually, expanding $u=\sum _{j=1}^{n}u_{j}e_{j}$ , we obtain the matrix form of the equation

$\mathbf {A} \mathbf {u} =\mathbf {f} ,$

where $a_{ij}=\langle Ae_{j},e_{i}\rangle$ and $f_{i}=\langle f,e_{i}\rangle$ .

The bilinear form associated to this weak formulation is

$a(u,v)=\mathbf {v} ^{T}\mathbf {A} \mathbf {u} .$

## Example 2: Poisson's equation

To solve Poisson's equation

$-\nabla ^{2}u=f,$

on a domain $\Omega \subset \mathbb {R} ^{d}$ with $u=0$ on its boundary, and to specify the solution space V later, one can use the $L^{2}$ -scalar product

$\langle u,v\rangle =\int _{\Omega }uv\,dx$

to derive the weak formulation. Then, testing with differentiable functions v yields

$-\int _{\Omega }(\nabla ^{2}u)v\,dx=\int _{\Omega }fv\,dx.$

The left side of this equation can be made more symmetric by integration by parts using Green's identity and assuming that $v=0$ on $\partial \Omega$ :

$\int _{\Omega }\nabla u\cdot \nabla v\,dx=\int _{\Omega }fv\,dx.$

This is what is usually called the weak formulation of Poisson's equation. Functions in the solution space V must be zero on the boundary, and have square-integrable derivatives. The appropriate space to satisfy these requirements is the Sobolev space $H_{0}^{1}(\Omega )$ of functions with weak derivatives in $L^{2}(\Omega )$ and with zero boundary conditions, so $V=H_{0}^{1}(\Omega )$ .

The generic form is obtained by assigning

$a(u,v)=\int _{\Omega }\nabla u\cdot \nabla v\,dx$

and

$f(v)=\int _{\Omega }fv\,dx.$

## The Lax–Milgram theorem

This is a formulation of the **Lax–Milgram theorem** which relies on properties of the symmetric part of the bilinear form. It is not the most general form.

Let V be a real Hilbert space and $a(\cdot ,\cdot )$ a bilinear form on V , which is

1. bounded: $|a(u,v)|\leq C\|u\|\|v\|\,;$ and
2. coercive: $a(u,u)\geq c\|u\|^{2}\,.$

Then, for any bounded $f\in V'$ , there is a unique solution $u\in V$ to the equation

$a(u,v)=f(v)\quad \forall v\in V$

and it holds

$\|u\|\leq {\frac {1}{c}}\|f\|_{V'}\,.$

### Application to example 1

Here, application of the Lax–Milgram theorem is a stronger result than is needed.

- Boundedness: all bilinear forms on $\mathbb {R} ^{n}$ are bounded. In particular, we have $|a(u,v)|\leq \|A\|\,\|u\|\,\|v\|$
- Coercivity: this actually means that the real parts of the eigenvalues of A are not smaller than c . Since this implies in particular that no eigenvalue is zero, the system is solvable.

Additionally, this yields the estimate $\|u\|\leq {\frac {1}{c}}\|f\|,$ where c is the minimal real part of an eigenvalue of A .

### Application to example 2

Here, choose $V=H_{0}^{1}(\Omega )$ with the norm $\|v\|_{V}:=\|\nabla v\|,$

where the norm on the right is the $L^{2}$ -norm on $\Omega$ (this provides a true norm on V by the Poincaré inequality). But, we see that $|a(u,u)|=\|\nabla u\|^{2}$ and by the Cauchy–Schwarz inequality, $|a(u,v)|\leq \|\nabla u\|\,\|\nabla v\|$ .

Therefore, for any $f\in [H_{0}^{1}(\Omega )]'$ , there is a unique solution $u\in V$ of Poisson's equation and we have the estimate

$\|\nabla u\|\leq \|f\|_{[H_{0}^{1}(\Omega )]'}.$
