---
title: "Fixed-point iteration"
source: https://en.wikipedia.org/wiki/Fixed-point_iteration
domain: fixed-point-iteration
license: CC-BY-SA-4.0
tags: fixed-point iteration, banach fixed-point theorem, contraction mapping, anderson acceleration
fetched: 2026-07-02
---

# Fixed-point iteration

In numerical analysis, **fixed-point iteration** is a method of computing fixed points of a function.

More specifically, given a function f defined on the real numbers with real values and given a point $x_{0}$ in the domain of f , the fixed-point iteration is $x_{n+1}=f(x_{n}),\,n=0,1,2,\dots$ which gives rise to the sequence $x_{0},x_{1},x_{2},\dots$ of iterated function applications $x_{0},f(x_{0}),f(f(x_{0})),\dots$ which is hoped to converge to a point $x_{\text{fix}}$ . If f is continuous, then one can prove that the obtained $x_{\text{fix}}$ is a fixed point of f , i.e., $f(x_{\text{fix}})=x_{\text{fix}}.$

More generally, the function f can be defined on any metric space with values in that same space.

## Examples

- A first simple and useful example is the Babylonian method for computing the square root of *a* > 0, which consists in taking $f(x)={\frac {1}{2}}\left({\frac {a}{x}}+x\right)$ , i.e. the mean value of x and *a*/*x*, to approach the limit $x={\sqrt {a}}$ (from whatever starting point $x_{0}\gg 0$ ). This is a special case of Newton's method quoted below.
- The fixed-point iteration $x_{n+1}=\cos x_{n}\,$ converges to the unique fixed point of the function $f(x)=\cos x\,$ for any starting point $x_{0}.$ This example does satisfy (at the latest after the first iteration step) the assumptions of the Banach fixed-point theorem. Hence, the error after n steps satisfies $|x_{n}-x|\leq {q^{n} \over 1-q}|x_{1}-x_{0}|=Cq^{n}$ (where we can take $q=0.85$ , if we start from $x_{0}=1$ .) When the error is less than a multiple of $q^{n}$ for some constant *q*, we say that we have linear convergence. The Banach fixed-point theorem allows one to obtain fixed-point iterations with linear convergence.
- The requirement that *f* is continuous is important, as the following example shows. The iteration $x_{n+1}={\begin{cases}{\frac {x_{n}}{2}},&x_{n}\neq 0\\1,&x_{n}=0\end{cases}}$ converges to 0 for all values of $x_{0}$ . However, 0 is *not* a fixed point of the function $f(x)={\begin{cases}{\frac {x}{2}},&x\neq 0\\1,&x=0\end{cases}}$ as this function is *not* continuous at $x=0$ , and in fact has no fixed points.

## Attracting fixed points

An *attracting fixed point* of a function *f* is a fixed point *x*fix of *f* with a neighborhood *U* of "close enough" points around *x*fix such that for any value of x in *U*, the fixed-point iteration sequence $x,\ f(x),\ f(f(x)),\ f(f(f(x))),\dots$ is contained in *U* and converges to *x*fix. The basin of attraction of *x*fix is the largest such neighborhood *U*.

The natural cosine function ("natural" means in radians, not degrees or other units) has exactly one fixed point, and that fixed point is attracting. In this case, "close enough" is not a stringent criterion at all—to demonstrate this, start with *any* real number and repeatedly press the *cos* key on a calculator (checking first that the calculator is in "radians" mode). It eventually converges to the Dottie number (about 0.739085133), which is a fixed point. That is where the graph of the cosine function intersects the line $y=x$ .

Not all fixed points are attracting. For example, 0 is a fixed point of the function *f*(*x*) = 2*x*, but iteration of this function for any value other than zero rapidly diverges. We say that the fixed point of $f(x)=2x$ is repelling.

An attracting fixed point is said to be a *stable fixed point* if it is also Lyapunov stable.

A fixed point is said to be a *neutrally stable fixed point* if it is Lyapunov stable but not attracting. The center of a linear homogeneous differential equation of the second order is an example of a neutrally stable fixed point.

Multiple attracting points can be collected in an *attracting fixed set*.

### Banach fixed-point theorem

The Banach fixed-point theorem gives a sufficient condition for the existence of attracting fixed points. A contraction mapping function f defined on a complete metric space has precisely one fixed point, and the fixed-point iteration is attracted towards that fixed point for any initial guess $x_{0}$ in the domain of the function. Common special cases are that (1) f is defined on the real line with real values and is Lipschitz continuous with Lipschitz constant $L<1$ , and (2) the function *f* is continuously differentiable in an open neighbourhood of a fixed point *x*fix, and $|f'(x_{\text{fix}})|<1$ .

Although there are other fixed-point theorems, this one in particular is very useful because not all fixed-points are attractive. When constructing a fixed-point iteration, it is very important to make sure it converges to the fixed point. We can usually use the Banach fixed-point theorem to show that the fixed point is attractive.

### Attractors

Attracting fixed points are a special case of a wider mathematical concept of attractors. Fixed-point iterations are a discrete dynamical system on one variable. Bifurcation theory studies dynamical systems and classifies various behaviors such as attracting fixed points, periodic orbits, or strange attractors. An example system is the logistic map.

## Iterative methods

In computational mathematics, an iterative method is a mathematical procedure that uses an initial value to generate a sequence of improving approximate solutions for a class of problems, in which the n-th approximation is derived from the previous ones. Convergent fixed-point iterations are mathematically rigorous formalizations of iterative methods.

### Iterative method examples

- Newton's method is a root-finding algorithm for finding roots of a given differentiable function ⁠ $f(x)$ ⁠. The iteration is ${\textstyle x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}.}$ If we write ${\textstyle g(x)=x-{\frac {f(x)}{f'(x)}}}$ , we may rewrite the Newton iteration as the fixed-point iteration ${\textstyle x_{n+1}=g(x_{n})}$ . If this iteration converges to a fixed point $x_{\text{fix}}$ of g, then ${\textstyle x_{\text{fix}}=g(x_{\text{fix}})=x_{\text{fix}}-{\frac {f(x_{\text{fix}})}{f'(x_{\text{fix}})}}}$ , so ${\textstyle f(x_{\text{fix}})/f'(x_{\text{fix}})=0,}$ therefore $f(x_{\text{fix}})=0$ , that is, $x_{\text{fix}}$ is a *root* of f . Under the assumptions of the Banach fixed-point theorem, the Newton iteration, framed as a fixed-point method, demonstrates at least linear convergence. More detailed analysis shows quadratic convergence, i.e., ${\textstyle |x_{n}-x_{\text{fix}}|<Cq^{2^{n}}}$ , under certain circumstances.
- Halley's method is similar to Newton's method when it works correctly, but its error is $|x_{n}-x_{\text{fix}}|<Cq^{3^{n}}$ (cubic convergence). In general, it is possible to design methods that converge with speed $Cq^{k^{n}}$ for any $k\in \mathbb {N}$ . As a general rule, the higher the k, the less stable it is, and the more computationally expensive it gets. For these reasons, higher order methods are typically not used.
- Runge–Kutta methods and numerical ordinary differential equation solvers in general can be viewed as fixed-point iterations. Indeed, the core idea when analyzing the A-stability of ODE solvers is to start with the special case $y'=ay$ , where a is a complex number, and to check whether the ODE solver converges to the fixed point $y_{\text{fix}}=0$ whenever the real part of a is negative.
- The Picard–Lindelöf theorem, which shows that ordinary differential equations have solutions, is essentially an application of the Banach fixed-point theorem to a special sequence of functions which forms a fixed-point iteration, constructing the solution to the equation. Solving an ODE in this way is called **Picard iteration**, **Picard's method**, or the **Picard iterative process**.
- The iteration capability in Excel can be used to find solutions to the Colebrook equation to an accuracy of 15 significant figures.
- Some of the "successive approximation" schemes used in dynamic programming to solve Bellman's functional equation are based on fixed-point iterations in the space of the return function.
- The cobweb model of price theory corresponds to the fixed-point iteration of the composition of the supply function and the demand function.

### Convergence acceleration

The speed of convergence of the iteration sequence can be increased by using a convergence acceleration method such as Anderson acceleration and Aitken's delta-squared process. The application of Aitken's method to fixed-point iteration is known as Steffensen's method, and it can be shown that Steffensen's method yields a rate of convergence that is at least quadratic.

## Chaos game

The term *chaos game* refers to a method of generating the fixed point of any iterated function system (IFS). Starting with any point *x*0, successive iterations are formed as *x**k*+1 = *f**r*(*x**k*), where *f**r* is a member of the given IFS randomly selected for each iteration. Hence the chaos game is a randomized fixed-point iteration. The chaos game allows plotting the general shape of a fractal such as the Sierpinski triangle by repeating the iterative process a large number of times. More mathematically, the iterations converge to the fixed point of the IFS. Whenever *x*0 belongs to the attractor of the IFS, all iterations *x**k* stay inside the attractor and, with probability 1, form a dense set in the latter.
