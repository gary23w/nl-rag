---
title: "Mixed boundary condition"
source: https://en.wikipedia.org/wiki/Mixed_boundary_condition
domain: boundary-value-problems
license: CC-BY-SA-4.0
tags: boundary value problem, dirichlet boundary condition, neumann boundary condition, shooting method
fetched: 2026-07-02
---

# Mixed boundary condition

In mathematics, a **mixed boundary condition** for a partial differential equation defines a boundary value problem in which the solution of the given equation is required to satisfy different boundary conditions on disjoint parts of the boundary of the domain where the condition is stated. Precisely, in a mixed boundary value problem, the solution is required to satisfy a Dirichlet or a Neumann boundary condition in a mutually exclusive way on disjoint parts of the boundary.

For example, given a solution *u* to a partial differential equation on a domain Ω with boundary ∂Ω, it is said to satisfy a mixed boundary condition if, consisting ∂Ω of two disjoint parts, Γ 1 and Γ 2, such that ∂Ω = Γ 1 ∪ Γ 2, *u* verifies the following equations:

$\left.u\right|_{\Gamma _{1}}=u_{0}$

and

$\left.{\frac {\partial u}{\partial n}}\right|_{\Gamma _{2}}=g,$

where *u* 0 and *g* are given functions defined on those portions of the boundary.

The mixed boundary condition differs from the Robin boundary condition in that the latter requires a linear combination, possibly with pointwise variable coefficients, of the Dirichlet and the Neumann boundary value conditions to be satisfied on the whole boundary of a given domain.

## Historical note

> M. Wirtinger, dans une conversation privée, a attiré mon attention sur le probleme suivant: *déterminer une fonction u vérifiant l'équation de Laplace dans un certain domaine* (*D*) *étant donné, sur une partie* (*S*) *de la frontière, les valeurs périphériques de la fonction demandée et, sur le reste* (*S′*) *de la frontière du domaine considéré, celles de la dérivée suivant la normale*. Je me propose de faire connaitre une solution très générale de cet intéressant problème.

— Stanisław Zaremba, (Zaremba 1910, §1, p. 313).

The first boundary value problem satisfying a mixed boundary condition was solved by Stanisław Zaremba for the Laplace equation: according to himself, it was Wilhelm Wirtinger who suggested him to study this problem.
