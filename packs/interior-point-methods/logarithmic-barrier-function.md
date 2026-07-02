---
title: "Barrier function"
source: https://en.wikipedia.org/wiki/Logarithmic_barrier_function
domain: interior-point-methods
license: CC-BY-SA-4.0
tags: interior-point method, karmarkar algorithm, barrier function, ellipsoid method
fetched: 2026-07-02
---

# Barrier function

(Redirected from

Logarithmic barrier function

)

In constrained optimization, a field of mathematics, a **barrier function** is a continuous function whose value increases to infinity as its argument approaches the boundary of the feasible region of an optimization problem. Such functions are used to replace inequality constraints by a penalizing term in the objective function that is easier to handle. A barrier function is also called an **interior penalty function**, as it is a penalty function that forces the solution to remain within the interior of the feasible region.

The two most common types of barrier functions are inverse barrier functions and logarithmic barrier functions. Resumption of interest in logarithmic barrier functions was motivated by their connection with primal-dual interior point methods.

## Motivation

Consider the following constrained optimization problem:

minimize

f

(

x

)

subject to

x

≤

b

where b is some constant. If one wishes to remove the inequality constraint, the problem can be reformulated as

minimize

f

(

x

) +

c

(

x

)

,

where

c

(

x

) = ∞

if

x

>

b

, and zero otherwise.

This problem is equivalent to the first. It gets rid of the inequality, but introduces the issue that the penalty function c, and therefore the objective function *f*(*x*) + *c*(*x*), is discontinuous, preventing the use of calculus to solve it.

A barrier function, now, is a continuous approximation g to c that tends to infinity as x approaches b from below. Using such a function, a new optimization problem is formulated, viz.

minimize

f

(

x

) +

μ

g

(

x

)

where *μ* > 0 is a free parameter. This problem is not equivalent to the original, but as μ approaches zero, it becomes an ever-better approximation.

## Logarithmic barrier function

For logarithmic barrier functions, $g(x,b)$ is defined as $-\!\log(b-x)$ when $x<b$ and $\infty$ otherwise (in one dimension; see below for a definition in higher dimensions). This essentially relies on the fact that $\log t$ tends to negative infinity as t tends to 0.

This introduces a gradient to the function being optimized which favors less extreme values of x (in this case, values lower than b ), while having relatively low impact on the function away from these extremes.

Logarithmic barrier functions may be favored over less computationally expensive inverse barrier functions depending on the function being optimized.

### Higher dimensions

Extending to higher dimensions is simple, provided each dimension is independent. For each variable $x_{i}$ which should be limited to be strictly lower than $b_{i}$ , add $-\!\log(b_{i}-x_{i})$ .

### Formal definition

Minimize $\mathbf {c} ^{T}x$ subject to $\mathbf {a} _{i}^{T}x\leq b_{i},i=1,\ldots ,m$

Assume strictly feasible: $\{\mathbf {x} \mid Ax<b\}\neq \emptyset$

Define **logarithmic barrier** $g(x)={\begin{cases}\sum _{i=1}^{m}-\!\log(b_{i}-a_{i}^{T}x)&{\text{for }}Ax<b\\+\infty &{\text{otherwise}}\end{cases}}$
