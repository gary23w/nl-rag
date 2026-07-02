---
title: "Functional equation"
source: https://en.wikipedia.org/wiki/Functional_equation
domain: functional-equations
license: CC-BY-SA-4.0
tags: functional equation, cauchy functional equation, recurrence relation, generating function
fetched: 2026-07-02
---

# Functional equation

In mathematics, a **functional equation** is, in the broadest meaning, an equation in which one or several functions appear as unknowns. So, differential equations and integral equations are functional equations. However, a more restricted meaning is often used, where a *functional equation* is an equation that relates several values of the same function. For example, the logarithm functions are essentially characterized by the *logarithmic functional equation* ⁠ $\log(xy)=\log(x)+\log(y)$ ⁠.

If the domain of the unknown function is supposed to be the natural numbers, the function is generally viewed as a sequence, and, in this case, a functional equation (in the narrower meaning) is called a recurrence relation. Thus the term *functional equation* is used mainly for real functions and complex functions. Moreover a smoothness condition is often assumed for the solutions, since without such a condition, most functional equations have highly irregular solutions. For example, the gamma function is a function that satisfies the functional equation $f(x+1)=xf(x)$ and the initial value $f(1)=1.$ There are many functions that satisfy these conditions, but the gamma function is the unique one that is meromorphic in the whole complex plane, and logarithmically convex for x real and positive (Bohr–Mollerup theorem).

## Examples

- Recurrence relations can be seen as functional equations in functions over the integers or natural numbers, in which the differences between terms' indexes can be seen as an application of the shift operator. For example, the recurrence relation defining the Fibonacci numbers, $F_{n}=F_{n-1}+F_{n-2}$ , where $F_{0}=0$ and $F_{1}=1$
- $f(x+P)=f(x)$ , which characterizes the periodic functions
- $f(x)=f(-x)$ , which characterizes the even functions, and likewise $f(x)=-f(-x)$ , which characterizes the odd functions
- $f(f(x))=g(x)$ , which characterizes the functional square roots of a function g
- $f(x+y)=f(x)+f(y)$ (Cauchy's functional equation), satisfied by linear maps. The equation may, contingent on the axiom of choice, also have other pathological nonlinear solutions, whose existence can be proven with a Hamel basis for the real numbers
- $f(x+y)=f(x)f(y),$ satisfied by all exponential functions. Like Cauchy's additive functional equation, this too may have pathological, discontinuous solutions
- $f(xy)=f(x)+f(y)$ , satisfied by all logarithmic functions and, over coprime integer arguments, additive functions
- $f(xy)=f(x)f(y)$ , satisfied by all power functions and, over coprime integer arguments, multiplicative functions
- $f(x+y)+f(x-y)=2[f(x)+f(y)]$ (quadratic equation or parallelogram law)
- $f((x+y)/2)=(f(x)+f(y))/2$ (Jensen's functional equation)
- $g(x+y)+g(x-y)=2[g(x)g(y)]$ (d'Alembert's functional equation)
- $f(h(x))=h(x+1)$ (Abel equation)
- $f(h(x))=cf(x)$ (Schröder's equation).
- $f(h(x))=(f(x))^{c}$ (Böttcher's equation).
- $f(h(x))=h'(x)f(x)$ (Julia's equation).
- $f(xy)=\sum g_{l}(x)h_{l}(y)$ (Levi-Civita),
- $f(x+y)=f(x)g(y)+f(y)g(x)$ (sine addition formula and hyperbolic sine addition formula),
- $g(x+y)=g(x)g(y)-f(y)f(x)$ (cosine addition formula),
- $g(x+y)=g(x)g(y)+f(y)f(x)$ (hyperbolic cosine addition formula).
- The commutative and associative laws are functional equations. In its familiar form, the associative law is expressed by writing the binary operation in infix notation, $(a\circ b)\circ c=a\circ (b\circ c),$ but if we write *f*(*a*, *b*) instead of *a* ○ *b* then the associative law looks more like a conventional functional equation, $f(f(a,b),c)=f(a,f(b,c)).$
- The functional equation $f(s)=2^{s}\pi ^{s-1}\sin \left({\frac {\pi s}{2}}\right)\Gamma (1-s)f(1-s)$ is satisfied by the Riemann zeta function. The capital Γ denotes the gamma function.
- The gamma function is the unique solution of the following system of three equations:
  - $f(x)={f(x+1) \over x}$
  - $f(y)f\left(y+{\frac {1}{2}}\right)={\frac {\sqrt {\pi }}{2^{2y-1}}}f(2y)$
  - $f(z)f(1-z)={\pi \over \sin(\pi z)}$           (Euler's reflection formula)
- The functional equation $f\left({az+b \over cz+d}\right)=(cz+d)^{k}f(z)$ where *a*, *b*, *c*, *d* are integers satisfying $ad-bc=1$ , i.e. ${\begin{vmatrix}a&b\\c&d\end{vmatrix}}$ = 1, defines f to be a modular form of order k.

One feature that all of the examples listed above have in common is that, in each case, two or more known functions (sometimes multiplication by a constant, sometimes addition of two variables, sometimes the identity function) are inside the argument of the unknown functions to be solved for.

When it comes to asking for *all* solutions, it may be the case that conditions from mathematical analysis should be applied; for example, in the case of the *Cauchy equation* mentioned above, the solutions that are continuous functions are the 'reasonable' ones, while other solutions that are not likely to have practical application can be constructed (by using a Hamel basis for the real numbers as vector space over the rational numbers). The Bohr–Mollerup theorem is another well-known example.

### Involutions

The involutions are characterized by the functional equation $f(f(x))=x$ . These appear in Babbage's functional equation (1820),

$f(f(x))=1-(1-x)=x\,.$

Other involutions, and solutions of the equation, include

- $f(x)=a-x\,,$
- $f(x)={\frac {a}{x}}\,,$ and
- $f(x)={\frac {b-x}{1+cx}}~,$

which includes the previous three as special cases or limits.

## Solution

In dynamic programming a variety of successive approximation methods are used to solve Bellman's functional equation, including methods based on fixed point iterations.
