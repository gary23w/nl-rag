---
title: "Basis function"
source: https://en.wikipedia.org/wiki/Basis_function
domain: finite-element-method
license: CC-BY-SA-4.0
tags: finite element method, galerkin method, stiffness matrix, weak formulation
fetched: 2026-07-02
---

# Basis function

In mathematics, a **basis function** is an element of a particular basis for a function space. Every function in the function space can be represented as a linear combination of basis functions. In finite-dimensional vector spaces this representation is purely algebraic and involves only finitely many basis functions, whereas in infinite-dimensional settings it typically takes the form of an infinite series whose convergence depends on the topology of the space.

In numerical analysis and approximation theory, basis functions are also called **blending functions,** because of their use in interpolation: In this application, a mixture of the basis functions provides an interpolating function (with the "blend" depending on the evaluation of the basis functions at the data points).

## Examples

### Monomial basis for *Cω*

The monomial basis for the vector space of analytic functions is given by $\{x^{n}\mid n\in \mathbb {N} \}.$

This basis is used in Taylor series, amongst others.

### Monomial basis for polynomials

The monomial basis also forms a basis for the vector space of polynomials. After all, every polynomial can be written as $a_{0}+a_{1}x^{1}+a_{2}x^{2}+\cdots +a_{n}x^{n}$ for some $n\in \mathbb {N}$ , which is a linear combination of monomials.

### Fourier basis for *L*2[0,1]

Sines and cosines form an (orthonormal) Schauder basis for square-integrable functions on a bounded domain. As a particular example, the collection $\{{\sqrt {2}}\sin(2\pi nx)\mid n\in \mathbb {N} \}\cup \{{\sqrt {2}}\cos(2\pi nx)\mid n\in \mathbb {N} \}\cup \{1\}$ forms a basis for *L*2[0,1].
