---
title: "Galerkin method"
source: https://en.wikipedia.org/wiki/Galerkin_method
domain: finite-element-method
license: CC-BY-SA-4.0
tags: finite element method, galerkin method, stiffness matrix, weak formulation
fetched: 2026-07-02
---

# Galerkin method

In mathematics, in the area of numerical analysis, **Galerkin methods** are a family of methods for converting a continuous operator problem, such as a differential equation, commonly in a weak formulation, to a discrete problem by applying linear constraints determined by finite sets of basis functions. They are named after the Soviet mathematician Boris Galerkin.

Often when referring to a Galerkin method, one also gives the name along with typical assumptions and approximation methods used:

- **Ritz–Galerkin method** (after Walther Ritz) typically assumes symmetric and positive-definite bilinear form in the weak formulation, where the differential equation for a physical system can be formulated via minimization of a quadratic function representing the system energy and the approximate solution is a linear combination of the given set of the basis functions.
- **Bubnov–Galerkin method** (after Ivan Bubnov) does not require the bilinear form to be symmetric and substitutes the energy minimization with orthogonality constraints determined by the same basis functions that are used to approximate the solution. In an operator formulation of the differential equation, Bubnov–Galerkin method can be viewed as applying an orthogonal projection to the operator.
- **Petrov–Galerkin method** (after Georgii I. Petrov) allows using basis functions for orthogonality constraints (called **test basis functions**) that are different from the basis functions used to approximate the solution. Petrov–Galerkin method can be viewed as an extension of Bubnov–Galerkin method, applying a projection that is not necessarily orthogonal in the operator formulation of the differential equation.

Examples of Galerkin methods are:

- the Galerkin method of weighted residuals, the most common method of calculating the global stiffness matrix in the finite element method,
- the boundary element method for solving integral equations,
- Krylov subspace methods.

## Linear equation in a Hilbert space

### Weak formulation of a linear equation

Let us introduce Galerkin's method with an abstract problem posed as a weak formulation on a Hilbert space V , namely,

find

$u\in V$

such that for all

$v\in V:a(u,v)=f(v)$

.

Here, $a(\cdot ,\cdot )$ is a bilinear form (the exact requirements on $a(\cdot ,\cdot )$ will be specified later) and f is a bounded linear functional on V .

### Galerkin dimension reduction

Choose a subspace $V_{n}\subset V$ of dimension *n* and solve the projected problem:

Find

$u_{n}\in V_{n}$

such that for all

$v_{n}\in V_{n},a(u_{n},v_{n})=f(v_{n})$

.

We call this the **Galerkin equation**. Notice that the equation has remained unchanged and only the spaces have changed. Reducing the problem to a finite-dimensional vector subspace allows us to numerically compute $u_{n}$ as a finite linear combination of the basis vectors in $V_{n}$ .

### Galerkin orthogonality

The key property of the Galerkin approach is that the error is orthogonal to the chosen subspaces. Since $V_{n}\subset V$ , we can use $v_{n}$ as a test vector in the original equation. Subtracting the two, we get the Galerkin orthogonality relation for the error, $\epsilon _{n}=u-u_{n}$ which is the error between the solution of the original problem, u , and the solution of the Galerkin equation, $u_{n}$

$a(\epsilon _{n},v_{n})=a(u,v_{n})-a(u_{n},v_{n})=f(v_{n})-f(v_{n})=0.$

### Matrix form of Galerkin's equation

Since the aim of Galerkin's method is the production of a linear system of equations, we build its matrix form, which can be used to compute the solution algorithmically.

Let $e_{1},e_{2},\ldots ,e_{n}$ be a basis for $V_{n}$ . Then, it is sufficient to use these in turn for testing the Galerkin equation, i.e.: find $u_{n}\in V_{n}$ such that

$a(u_{n},e_{i})=f(e_{i})\quad i=1,\ldots ,n.$

We expand $u_{n}$ with respect to this basis, $u_{n}=\sum _{j=1}^{n}u_{j}e_{j}$ and insert it into the equation above, to obtain

$a\left(\sum _{j=1}^{n}u_{j}e_{j},e_{i}\right)=\sum _{j=1}^{n}u_{j}a(e_{j},e_{i})=f(e_{i})\quad i=1,\ldots ,n.$

This previous equation is actually a linear system of equations $Au=f$ , where

$A_{ij}=a(e_{j},e_{i}),\quad f_{i}=f(e_{i}).$

#### Symmetry of the matrix

Due to the definition of the matrix entries, the matrix of the Galerkin equation is symmetric if and only if the bilinear form $a(\cdot ,\cdot )$ is symmetric.

## Analysis of Galerkin methods

Here, we will restrict ourselves to symmetric bilinear forms, that is

$a(u,v)=a(v,u).$

While this is not really a restriction of Galerkin methods, the application of the standard theory becomes much simpler. Furthermore, a Petrov–Galerkin method may be required in the nonsymmetric case.

The analysis of these methods proceeds in two steps. First, we will show that the Galerkin equation is a well-posed problem in the sense of Hadamard and therefore admits a unique solution. In the second step, we study the quality of approximation of the Galerkin solution $u_{n}$ .

The analysis will mostly rest on two properties of the bilinear form, namely

- Boundedness: for all $u,v\in V$ holds $a(u,v)\leq C\|u\|\,\|v\|$ for some constant $C>0$
- Ellipticity: for all $u\in V$ holds $a(u,u)\geq c\|u\|^{2}$ for some constant $c>0.$

By the Lax-Milgram theorem (see weak formulation), these two conditions imply well-posedness of the original problem in weak formulation. All norms in the following sections will be norms for which the above inequalities hold (these norms are often called an energy norm).

### Well-posedness of the Galerkin equation

Since $V_{n}\subset V$ , boundedness and ellipticity of the bilinear form apply to $V_{n}$ . Therefore, the well-posedness of the Galerkin problem is actually inherited from the well-posedness of the original problem.

### Quasi-best approximation (Céa's lemma)

The error $u-u_{n}$ between the original and the Galerkin solution admits the estimate

$\|u-u_{n}\|\leq {\frac {C}{c}}\inf _{v_{n}\in V_{n}}\|u-v_{n}\|.$

This means, that up to the constant $C/c$ , the Galerkin solution $u_{n}$ is as close to the original solution u as any other vector in $V_{n}$ . In particular, it will be sufficient to study approximation by spaces $V_{n}$ , completely forgetting about the equation being solved.

#### Proof

Since the proof is very simple and the basic principle behind all Galerkin methods, we include it here: by ellipticity and boundedness of the bilinear form (inequalities) and Galerkin orthogonality (equals sign in the middle), we have for arbitrary $v_{n}\in V_{n}$ :

$c\|u-u_{n}\|^{2}\leq a(u-u_{n},u-u_{n})=a(u-u_{n},u-v_{n})\leq C\|u-u_{n}\|\,\|u-v_{n}\|.$

Dividing by $c\|u-u_{n}\|$ and taking the infimum over all possible $v_{n}$ yields the lemma.

### Galerkin's best approximation property in the energy norm

For simplicity of presentation in the section above we have assumed that the bilinear form $a(u,v)$ is symmetric and positive-definite, which implies that it is a scalar product and the expression ${\textstyle \|u\|_{a}={\sqrt {a(u,u)}}}$ is actually a valid vector norm, called the *energy norm*. Under these assumptions one can easily prove in addition Galerkin's best approximation property in the energy norm.

Using Galerkin a-orthogonality and the Cauchy–Schwarz inequality for the energy norm, we obtain

$\|u-u_{n}\|_{a}^{2}=a(u-u_{n},u-u_{n})=a(u-u_{n},u-v_{n})\leq \|u-u_{n}\|_{a}\,\|u-v_{n}\|_{a}.$

Dividing by $\|u-u_{n}\|_{a}$ and taking the infimum over all possible $v_{n}\in V_{n}$ proves that the Galerkin approximation $u_{n}\in V_{n}$ is the best approximation in the energy norm within the subspace $V_{n}\subset V$ , i.e. $u_{n}\in V_{n}$ is nothing but the orthogonal, with respect to the scalar product $a(u,v)$ , projection of the solution u to the subspace $V_{n}$ .

## Galerkin method for stepped Structures

I. Elishakof, M. Amato, A. Marzani, P.A. Arvan, and J.N. Reddy studied the application of the Galerkin method to stepped structures. They showed that the generalized function, namely unit-step function, Dirac’s delta function, and the doublet function are needed for obtaining accurate results.

## History

The approach is usually credited to Boris Galerkin. The method was explained to the Western reader by Hencky and Duncan among others. Its convergence was studied by Mikhlin and Leipholz Its coincidence with Fourier method was illustrated by Elishakoff et al. Its equivalence to Ritz's method for conservative problems was shown by Singer. Gander and Wanner showed how Ritz and Galerkin methods led to the modern finite element method. One hundred years of method's development was discussed by Repin. Elishakoff, Kaplunov and Kaplunov show that the Galerkin’s method was not developed by Ritz, contrary to the Timoshenko’s statements.
