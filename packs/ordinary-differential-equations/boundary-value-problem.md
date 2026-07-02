---
title: "Boundary value problem"
source: https://en.wikipedia.org/wiki/Boundary_value_problem
domain: ordinary-differential-equations
license: CC-BY-SA-4.0
tags: ordinary differential equation, initial value problem, boundary value problem, laplace transform
fetched: 2026-07-02
---

# Boundary value problem

In the study of differential equations, a **boundary-value problem** is a differential equation subjected to constraints called **boundary conditions**. A solution to a boundary value problem is a solution to the differential equation which also satisfies the boundary conditions.

Boundary value problems arise in several branches of physics as any physical differential equation will have them. Problems involving the wave equation, such as the determination of normal modes, are often stated as boundary value problems. A large class of important boundary value problems are the Sturm–Liouville problems. The analysis of these problems, in the linear case, involves the eigenfunctions of a differential operator.

To be useful in applications, a boundary value problem should be well posed. This means that given the input to the problem there exists a unique solution, which depends continuously on the input. Much theoretical work in the field of partial differential equations is devoted to proving that boundary value problems arising from scientific and engineering applications are in fact well-posed.

Among the earliest boundary value problems to be studied is the Dirichlet problem, of finding the harmonic functions (solutions to Laplace's equation); the solution was given by the Dirichlet's principle.

## Explanation

Boundary value problems are similar to initial value problems. A boundary value problem has conditions specified at the extremes ("boundaries") of the independent variable in the equation whereas an initial value problem has all of the conditions specified at the same value of the independent variable (and that value is at the lower boundary of the domain, thus the term "initial" value). A **boundary value** is a data value that corresponds to a minimum or maximum input, internal, or output value specified for a system or component.

For example, if the independent variable is time over the domain [0,1], a boundary value problem would specify values for $y(t)$ at both $t=0$ and $t=1$ , whereas an initial value problem would specify a value of $y(t)$ and $y'(t)$ at time $t=0$ .

Finding the temperature at all points of an iron bar with one end kept at absolute zero and the other end at the freezing point of water would be a boundary value problem.

If the problem is dependent on both space and time, one could specify the value of the problem at a given point for all time or at a given time for all space.

Concretely, an example of a boundary value problem (in one spatial dimension) is

$y''(x)+y(x)=0$

to be solved for the unknown function $y(x)$ with the boundary conditions

$y(0)=0,\ y(\pi /2)=2.$

Without the boundary conditions, the general solution to this equation is

$y(x)=A\sin(x)+B\cos(x).$

From the boundary condition $y(0)=0$ one obtains

$0=A\cdot 0+B\cdot 1$

which implies that $B=0.$ From the boundary condition $y(\pi /2)=2$ one finds

$2=A\cdot 1$

and so $A=2.$ One sees that imposing boundary conditions allowed one to determine a unique solution, which in this case is

$y(x)=2\sin(x).$

## Types of boundary value problems

The 3 standard classes of conditions are Dirichlet, Neumann and Cauchy or Robin, with also mixed, boundary as infinity.

Summary of boundary conditions for the unknown function, y , constants $c_{0}$ and $c_{1}$ specified by the boundary conditions, and known scalar functions f and g specified by the boundary conditions.

| Name | Form on 1st part of boundary | Form on 2nd part of boundary |
|---|---|---|
| Dirichlet | $y=f$ |   |
| Neumann | ${\partial y \over \partial n}=f$ |   |
| Robin | $c_{0}y+c_{1}{\partial y \over \partial n}=f$ |   |
| Cauchy | both $y=f$ and ${\partial y \over \partial n}=g$ |   |
| Mixed | $y=f$ | $c_{0}y+c_{1}{\partial y \over \partial n}=g$ |

### Boundary value conditions

A type 1 boundary condition, Dirichlet boundary condition, specifies the value of the function itself. For example, if one end of an iron rod is held at absolute zero, then the value of the problem would be known at that point in space.

A type 2 boundary condition, Neumann boundary condition, specifies the value of the normal derivative of the function. For example, if there is a heater at one end of an iron rod, then energy would be added at a constant rate but the actual temperature would not be known.

A type 3 boundary condition is the Robin condition.

If the boundary has the form of a curve or surface that gives a value to the normal derivative and the variable itself then it is a Cauchy boundary condition.

A type 0 boundary condition has no physical boundary.

### Differential operators

Aside from the boundary condition, boundary value problems are also classified according to the type of differential operator involved. For an elliptic operator, one discusses elliptic boundary value problems. For a hyperbolic operator, one discusses hyperbolic boundary value problems. These categories are further subdivided into linear and various nonlinear types.

## Applications

### Electromagnetic potential

In electrostatics, a common problem is to find a function which describes the electric potential of a given region. If the region does not contain charge, the potential must be a solution to Laplace's equation (a so-called harmonic function). The boundary conditions in this case are the Interface conditions for electromagnetic fields. If there is no current density in the region, it is also possible to define a magnetic scalar potential using a similar procedure.
