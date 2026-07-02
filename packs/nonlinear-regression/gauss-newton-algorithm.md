---
title: "Gauss–Newton algorithm"
source: https://en.wikipedia.org/wiki/Gauss–Newton_algorithm
domain: nonlinear-regression
license: CC-BY-SA-4.0
tags: nonlinear regression, curve fitting, levenberg marquardt, gauss newton
fetched: 2026-07-02
---

# Gauss–Newton algorithm

The **Gauss–Newton algorithm** is used to solve non-linear least squares problems, which is equivalent to minimizing a sum of squared function values. It is an extension of Newton's method for finding a minimum of a non-linear function. Since a sum of squares must be nonnegative, the algorithm can be viewed as using Newton's method to iteratively approximate zeroes of the components of the sum, and thus minimizing the sum. In this sense, the algorithm is also an effective method for solving overdetermined systems of equations. It has the advantage that second derivatives, which can be challenging to compute, are not required.

Non-linear least squares problems arise, for instance, in non-linear regression, where parameters in a model are sought such that the model is in good agreement with available observations.

The method is named after the mathematicians Carl Friedrich Gauss and Isaac Newton, and first appeared in Gauss's 1809 work *Theoria motus corporum coelestium in sectionibus conicis solem ambientum*.

## Description

Given m functions ${\textbf {r}}=(r_{1},\ldots ,r_{m})$ (often called residuals) of n variables ${\boldsymbol {\beta }}=(\beta _{1},\ldots \beta _{n}),$ with $m\geq n,$ the Gauss–Newton algorithm iteratively finds the value of $\beta$ that minimize the sum of squares $S({\boldsymbol {\beta }})=\sum _{i=1}^{m}r_{i}({\boldsymbol {\beta }})^{2}.$

Starting with an initial guess ${\boldsymbol {\beta }}^{(0)}$ for the minimum, the method proceeds by the iterations ${\boldsymbol {\beta }}^{(s+1)}={\boldsymbol {\beta }}^{(s)}-\left(\mathbf {J_{r}} ^{\operatorname {T} }\mathbf {J_{r}} \right)^{-1}\mathbf {J_{r}} ^{\operatorname {T} }\mathbf {r} \left({\boldsymbol {\beta }}^{(s)}\right),$

where, if **r** and ***β*** are column vectors, the entries of the Jacobian matrix are $\left(\mathbf {J_{r}} \right)_{ij}={\frac {\partial r_{i}\left({\boldsymbol {\beta }}^{(s)}\right)}{\partial \beta _{j}}},$

and the symbol $^{\operatorname {T} }$ denotes the matrix transpose.

At each iteration, the update $\Delta ={\boldsymbol {\beta }}^{(s+1)}-{\boldsymbol {\beta }}^{(s)}$ can be found by rearranging the previous equation in the following two steps:

- $\Delta =-\left(\mathbf {J_{r}} ^{\operatorname {T} }\mathbf {J_{r}} \right)^{-1}\mathbf {J_{r}} ^{\operatorname {T} }\mathbf {r} \left({\boldsymbol {\beta }}^{(s)}\right)$
- $\mathbf {J_{r}} ^{\operatorname {T} }\mathbf {J_{r}} \Delta =-\mathbf {J_{r}} ^{\operatorname {T} }\mathbf {r} \left({\boldsymbol {\beta }}^{(s)}\right)$

With substitutions ${\textstyle A=\mathbf {J_{r}} ^{\operatorname {T} }\mathbf {J_{r}} }$ , $\mathbf {b} =-\mathbf {J_{r}} ^{\operatorname {T} }\mathbf {r} \left({\boldsymbol {\beta }}^{(s)}\right)$ , and $\mathbf {x} =\Delta$ , this turns into the conventional matrix equation of form $A\mathbf {x} =\mathbf {b}$ , which can then be solved in a variety of methods (see Notes).

If *m* = *n*, the iteration simplifies to

${\boldsymbol {\beta }}^{(s+1)}={\boldsymbol {\beta }}^{(s)}-\left(\mathbf {J_{r}} \right)^{-1}\mathbf {r} \left({\boldsymbol {\beta }}^{(s)}\right),$

which is a direct generalization of Newton's method in one dimension.

In data fitting, where the goal is to find the parameters ${\boldsymbol {\beta }}$ such that a given model function $\mathbf {f} (\mathbf {x} ,{\boldsymbol {\beta }})$ best fits some data points $(x_{i},y_{i})$ , the functions $r_{i}$ are the residuals: $r_{i}({\boldsymbol {\beta }})=y_{i}-f\left(x_{i},{\boldsymbol {\beta }}\right).$

Then, the Gauss–Newton method can be expressed in terms of the Jacobian $\mathbf {J_{f}} =-\mathbf {J_{r}}$ of the function $\mathbf {f}$ as ${\boldsymbol {\beta }}^{(s+1)}={\boldsymbol {\beta }}^{(s)}+\left(\mathbf {J_{f}} ^{\operatorname {T} }\mathbf {J_{f}} \right)^{-1}\mathbf {J_{f}} ^{\operatorname {T} }\mathbf {r} \left({\boldsymbol {\beta }}^{(s)}\right).$

Note that $\left(\mathbf {J_{f}} ^{\operatorname {T} }\mathbf {J_{f}} \right)^{-1}\mathbf {J_{f}} ^{\operatorname {T} }$ is the left pseudoinverse of $\mathbf {J_{f}}$ .
