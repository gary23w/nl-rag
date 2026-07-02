---
title: "Functional (mathematics)"
source: https://en.wikipedia.org/wiki/Functional_(mathematics)
domain: calculus-of-variations
license: CC-BY-SA-4.0
tags: calculus of variations, euler-lagrange equation, principle of least action, isoperimetric inequality
fetched: 2026-07-02
---

# Functional (mathematics)

In mathematics, a **functional** is a certain type of function. The exact definition of the term varies depending on the subfield (and sometimes even the author).

- In linear algebra, it is synonymous with a linear form, which is a linear mapping from a vector space V into its field of scalars (that is, it is an element of the dual space $V^{*}$ )
- In functional analysis and related fields, it refers to a mapping from a space X into the field of real or complex numbers. In functional analysis, the term *linear functional* is a synonym of linear form; that is, it is a scalar-valued linear map. Depending on the author, such mappings may or may not be assumed to be linear, or to be defined on the whole space $X.$
- In computer science, it is synonymous with a higher-order function, which is a function that takes one or more functions as arguments or returns them.

This article is mainly concerned with the second concept, which arose in the early 18th century as part of the calculus of variations. The first concept, which is more modern and abstract, is discussed in detail in a separate article, under the name linear form. The third concept is detailed in the computer science article on higher-order functions.

In the case where the space X is a space of functions, the functional is a "function of a function", and some older authors actually define the term "functional" to mean "function of a function". However, the fact that X is a space of functions is not mathematically essential, so this older definition is no longer prevalent.

The term originates from the calculus of variations, where one searches for a function that minimizes (or maximizes) a given functional. A particularly important application in physics is search for a state of a system that minimizes (or maximizes) the action, or in other words the time integral of the Lagrangian.

## Details

### Duality

The mapping $x_{0}\mapsto f(x_{0})$ is a function, where $x_{0}$ is an argument of a function $f.$ At the same time, the mapping of a function to the value of the function at a point $f\mapsto f(x_{0})$ is a *functional*; here, $x_{0}$ is a parameter.

Provided that f is a linear function from a vector space to the underlying scalar field, the above linear maps are dual to each other, and in functional analysis both are called linear functionals.

### Definite integral

Integrals such as $f\mapsto I[f]=\int _{\Omega }H(f(x),f'(x),\ldots )\;\mu (\mathrm {d} x)$ form a special class of functionals. They map a function f into a real number, provided that H is real-valued. Examples include

- the area underneath the graph of a positive function f $f\mapsto \int _{x_{0}}^{x_{1}}f(x)\;\mathrm {d} x$
- $L^{p}$ norm of a function on a set E $f\mapsto \left(\int _{E}|f|^{p}\;\mathrm {d} x\right)^{1/p}$
- the arclength of a curve in 2-dimensional Euclidean space $f\mapsto \int _{x_{0}}^{x_{1}}{\sqrt {1+|f'(x)|^{2}}}\;\mathrm {d} x$

### Inner product spaces

Given an inner product space $X,$ and a fixed vector ${\vec {x}}\in X,$ the map defined by ${\vec {y}}\mapsto {\vec {x}}\cdot {\vec {y}}$ is a linear functional on $X.$ The set of vectors ${\vec {y}}$ such that ${\vec {x}}\cdot {\vec {y}}$ is zero is a vector subspace of $X,$ called the *null space* or *kernel* of the functional, or the orthogonal complement of ${\vec {x}},$ denoted $\{{\vec {x}}\}^{\perp }.$

For example, taking the inner product with a fixed function $g\in L^{2}([-\pi ,\pi ])$ defines a (linear) functional on the Hilbert space $L^{2}([-\pi ,\pi ])$ of square integrable functions on $[-\pi ,\pi ]:$ $f\mapsto \langle f,g\rangle =\int _{[-\pi ,\pi ]}{\bar {f}}g$

### Locality

If a functional's value can be computed for small segments of the input curve and then summed to find the total value, the functional is called local. Otherwise it is called non-local. For example: $F(y)=\int _{x_{0}}^{x_{1}}y(x)\;\mathrm {d} x$ is local while $F(y)={\frac {\int _{x_{0}}^{x_{1}}y(x)\;\mathrm {d} x}{\int _{x_{0}}^{x_{1}}(1+[y(x)]^{2})\;\mathrm {d} x}}$ is non-local. This occurs commonly when integrals occur separately in the numerator and denominator of an equation such as in calculations of center of mass.

## Functional equations

The traditional usage also applies when one talks about a functional equation, meaning an equation between functionals: an equation $F=G$ between functionals can be read as an 'equation to solve', with solutions being themselves functions. In such equations there may be several sets of variable unknowns, like when it is said that an *additive* map f is one *satisfying Cauchy's functional equation*: $f(x+y)=f(x)+f(y)\qquad {\text{ for all }}x,y.$

## Derivative and integration

Functional derivatives are used in Lagrangian mechanics. They are derivatives of functionals; that is, they carry information on how a functional changes when the input function changes by a small amount.

Richard Feynman used functional integrals as the central idea in his sum over the histories formulation of quantum mechanics. This usage implies an integral taken over some function space.
