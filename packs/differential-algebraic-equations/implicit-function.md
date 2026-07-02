---
title: "Implicit function"
source: https://en.wikipedia.org/wiki/Implicit_function
domain: differential-algebraic-equations
license: CC-BY-SA-4.0
tags: differential-algebraic equations, backward differentiation formula, method of lines, runge-kutta methods
fetched: 2026-07-02
---

# Implicit function

In mathematics, an **implicit equation** is a relation of the form $R(x_{1},\dots ,x_{n})=0,$ where R is a function of several variables (often a polynomial). For example, the implicit equation of the unit circle is $x^{2}+y^{2}-1=0.$

An **implicit function** is a function that is defined by an implicit equation, that relates one of the variables, considered as the value of the function, with the others considered as the arguments. For example, the equation $x^{2}+y^{2}-1=0$ of the unit circle defines y as an implicit function of x, $y={\sqrt {1-x^{2}}}$ , assuming −1 ≤ *x* ≤ 1 and y is restricted to nonnegative values. Some equations do not admit an explicit solution.

The implicit function theorem provides conditions under which some kinds of implicit equations define implicit functions, namely those that are obtained by equating to zero multivariable functions that are continuously differentiable.

## Examples

### Inverse functions

A common type of implicit function is an inverse function. Not all functions have a unique inverse function. If g is a function of x that has a unique inverse, then the inverse function of g, called *g*−1, is the unique function giving a solution of the equation

$y=g(x)$

for x in terms of y. This solution can then be written as

$x=g^{-1}(y)\,.$

Defining *g*−1 as the inverse of g is an implicit definition. For some functions g, *g*−1(*y*) can be written out explicitly as a closed-form expression — for instance, if *g*(*x*) = 2*x* − 1, then *g*−1(*y*) = ⁠1/2⁠(*y* + 1). However, this is often not possible, or only by introducing a new notation (as in the product log example below).

Intuitively, an inverse function is obtained from g by interchanging the roles of the dependent and independent variables.

**Example:** The product log is an implicit function giving the solution for x of the equation *y* − *xe**x* = 0.

### Algebraic functions

An **algebraic function** is a function that satisfies a polynomial equation whose coefficients are themselves polynomials. For example, an algebraic function in one variable x gives a solution for y of an equation

$a_{n}(x)y^{n}+a_{n-1}(x)y^{n-1}+\cdots +a_{0}(x)=0\,,$

where the coefficients *ai*(*x*) are polynomial functions of x. This algebraic function can be written as the right side of the solution equation *y* = *f*(*x*). Written like this, f is a multi-valued implicit function.

Algebraic functions play an important role in mathematical analysis and algebraic geometry. A simple example of an algebraic function is given by the left side of the unit circle equation:

$x^{2}+y^{2}-1=0\,.$

Solving for y gives an explicit solution:

$y=\pm {\sqrt {1-x^{2}}}\,.$

But even without specifying this explicit solution, it is possible to refer to the implicit solution of the unit circle equation as *y* = *f*(*x*), where f is the multi-valued implicit function.

While explicit solutions can be found for equations that are quadratic, cubic, and quartic in y, the same is not in general true for quintic and higher degree equations, such as

$y^{5}+2y^{4}-7y^{3}+3y^{2}-6y-x=0\,.$

Nevertheless, one can still refer to the implicit solution *y* = *f*(*x*) involving the multi-valued implicit function f.

## Caveats

Not every equation *R*(*x*, *y*) = 0 implies a graph of a single-valued function, the circle equation being one prominent example. Another example is an implicit function given by *x* − *C*(*y*) = 0 where C is a cubic polynomial having a "hump" in its graph. Thus, for an implicit function to be a *true* (single-valued) function it might be necessary to use just part of the graph. An implicit function can sometimes be successfully defined as a true function only after "zooming in" on some part of the x-axis and "cutting away" some unwanted function branches. Then an equation expressing y as an implicit function of the other variables can be written.

The defining equation *R*(*x*, *y*) = 0 can also have other pathologies. For example, the equation *x* = 0 does not imply a function *f*(*x*) giving solutions for y at all; it is a vertical line. In order to avoid a problem like this, various constraints are frequently imposed on the allowable sorts of equations or on the domain. The implicit function theorem provides a uniform way of handling these sorts of pathologies.

## Implicit differentiation

In calculus, implicit differentiation is a method for finding the derivative of a function that is defined by an equation rather than by an explicit formula. If an equation such as

$F(x,y)=0$

defines y as a function of x , at least locally, implicit differentiation treats y as a function $y(x)$ and differentiates both sides of the equation with respect to x . The method is an application of the chain rule.

Implicit differentiation is useful when solving explicitly for one variable is inconvenient, produces several branches, or is not possible in elementary terms. For example, the circle $x^{2}+y^{2}=1$ cannot be represented globally as the graph of a single function $y=f(x)$ , but its upper and lower arcs can each be differentiated implicitly.

The method allows for the computation of the tangent line approximation to $y(x)$ , given only the function F and the point $(x_{0},y_{0})$ at which the approximation is made, so that no other knowledge of the functional dependence of y on x is needed. Tangent approximations to surfaces and higher-dimensional manifolds given by an equation or system of equations can be found by similar methods.

## Implicit function theorem

Let *R*(*x*, *y*) be a differentiable function of two variables, and (*a*, *b*) be a pair of real numbers such that *R*(*a*, *b*) = 0. If ⁠∂*R*/∂*y*⁠ ≠ 0, then *R*(*x*, *y*) = 0 defines an implicit function that is differentiable in some small enough neighbourhood of (*a*, *b*); in other words, there is a differentiable function f that is defined and differentiable in some neighbourhood of a, such that *R*(*x*, *f*(*x*)) = 0 for x in this neighbourhood.

The condition ⁠∂*R*/∂*y*⁠ ≠ 0 means that (*a*, *b*) is a regular point of the implicit curve of implicit equation *R*(*x*, *y*) = 0 where the tangent is not vertical.

In a less technical language, implicit functions exist and can be differentiated, if the curve has a non-vertical tangent.

## In algebraic geometry

Consider a relation of the form *R*(*x*1, …, *x**n*) = 0, where R is a multivariable polynomial. The set of the values of the variables that satisfy this relation is called an implicit curve if *n* = 2 and an **implicit surface** if *n* = 3. The implicit equations are the basis of algebraic geometry, whose basic subjects of study are the simultaneous solutions of several implicit equations whose left-hand sides are polynomials. These sets of simultaneous solutions are called affine algebraic sets.

## In differential equations

The solutions of differential equations generally appear expressed by an implicit function.

## Applications in economics

### Marginal rate of substitution

In economics, when the level set *R*(*x*, *y*) = 0 is an indifference curve for the quantities x and y consumed of two goods, the absolute value of the implicit derivative ⁠*dy*/*dx*⁠ is interpreted as the marginal rate of substitution of the two goods: how much more of y one must receive in order to be indifferent to a loss of one unit of x.

### Marginal rate of technical substitution

Similarly, sometimes the level set *R*(*L*, *K*) is an isoquant showing various combinations of utilized quantities L of labor and K of physical capital each of which would result in the production of the same given quantity of output of some good. In this case the absolute value of the implicit derivative ⁠*dK*/*dL*⁠ is interpreted as the marginal rate of technical substitution between the two factors of production: how much more capital the firm must use to produce the same amount of output with one less unit of labor.

### Optimization

Often in economic theory, some function such as a utility function or a profit function is to be maximized with respect to a choice vector x even though the objective function has not been restricted to any specific functional form. The implicit function theorem guarantees that the first-order conditions of the optimization define an implicit function for each element of the optimal vector *x** of the choice vector x. When profit is being maximized, typically the resulting implicit functions are the labor demand function and the supply functions of various goods. When utility is being maximized, typically the resulting implicit functions are the labor supply function and the demand functions for various goods.

Moreover, the influence of the problem's parameters on *x** — the partial derivatives of the implicit function — can be expressed as total derivatives of the system of first-order conditions found using total differentiation.
