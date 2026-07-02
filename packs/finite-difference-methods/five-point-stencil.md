---
title: "Five-point stencil"
source: https://en.wikipedia.org/wiki/Five-point_stencil
domain: finite-difference-methods
license: CC-BY-SA-4.0
tags: finite difference method, crank-nicolson method, upwind scheme, von neumann stability analysis
fetched: 2026-07-02
---

# Five-point stencil

In numerical analysis, given a square grid in one or two dimensions, the **five-point stencil** of a point in the grid is a stencil made up of the point itself together with its four "neighbors". It is used to write finite difference approximations to derivatives at grid points. It is an example of numerical differentiation.

## In one dimension

In one dimension, if the spacing between points in the grid is *h*, then the five-point stencil of a point *x* in the grid is

$\{x-2h,x-h,x,x+h,x+2h\}.$

### 1D first derivative

The first derivative of a function *f* of a real variable at a point *x* can be approximated using a five-point stencil as:

$f'(x)\approx {\frac {-f(x+2h)+8f(x+h)-8f(x-h)+f(x-2h)}{12h}}$

The center point *f*(*x*) itself is not involved, only the four neighboring points.

#### Derivation

This formula can be obtained by writing out the four Taylor series of $f(x\pm h)$ and $f(x\pm 2h)$ at the point a , up to terms of *h*3 (or up to terms of *h*5 to get an error estimation as well), evaluating each series at $a=x\mp h$ and $a=x\mp 2h$ respectively (to get everything in common terms of $f^{(k)}(x)$ ), and solving this system of four equations to get *f* ′(*x*). Actually, we have at points *x* + *h* and *x* − *h*:

$f(x\pm h)=f(x)\pm hf'(x)+{\frac {h^{2}}{2}}f''(x)\pm {\frac {h^{3}}{6}}f^{(3)}(x)+O_{1\pm }(h^{4}).\qquad (E_{1\pm }).$

Evaluating $(E_{1+})-(E_{1-})$ gives us

$f(x+h)-f(x-h)=2hf'(x)+{\frac {h^{3}}{3}}f^{(3)}(x)+O_{1}(h^{4}).\qquad (E_{1}).$

The residual term O1(*h*4) should be of the order of *h*5 instead of *h*4 because if the terms of *h*4 had been written out in (*E*1+) and (*E*1−), it can be seen that they would have canceled each other out by *f*(*x* + *h*) − *f*(*x* − *h*). But for this calculation, it is left like that since the order of error estimation is not treated here (cf below).

Similarly, we have

$f(x\pm 2h)=f(x)\pm 2hf'(x)+{\frac {4h^{2}}{2!}}f''(x)\pm {\frac {8h^{3}}{3!}}f^{(3)}(x)+O_{2\pm }(h^{4}).\qquad (E_{2\pm })$

and $(E_{2+})-(E_{2-})$ gives us

$f(x+2h)-f(x-2h)=4hf'(x)+{\frac {8h^{3}}{3}}f^{(3)}(x)+O_{2}(h^{5}).\qquad (E_{2}).$

In order to eliminate the terms of *ƒ*(3)(*x*), calculate 8 × (*E*1) − (*E*2)

$8f(x+h)-8f(x-h)-f(x+2h)+f(x-2h)=12hf'(x)+O(h^{5})$

thus giving the formula as above. Note: the coefficients of f in this formula, (8, -8,-1,1), represent a specific example of the more general Savitzky–Golay filter.

#### Error estimate

The error in this approximation is of order *h* 4. That can be seen from the expansion

${\frac {-f(x+2h)+8f(x+h)-8f(x-h)+f(x-2h)}{12h}}=f'(x)-{\frac {1}{30}}f^{(5)}(x)h^{4}+O(h^{5})$

which can be obtained by expanding the left-hand side in a Taylor series. Alternatively, apply Richardson extrapolation to the central difference approximation to $f'(x)$ on grids with spacing 2*h* and *h*.

### 1D higher-order derivatives

The centered difference formulas for five-point stencils approximating second, third, and fourth derivatives are

${\begin{aligned}f''(x)&\approx {\frac {-f(x+2h)+16f(x+h)-30f(x)+16f(x-h)-f(x-2h)}{12h^{2}}}\\[1ex]f^{(3)}(x)&\approx {\frac {f(x+2h)-2f(x+h)+2f(x-h)-f(x-2h)}{2h^{3}}}\\[1ex]f^{(4)}(x)&\approx {\frac {f(x+2h)-4f(x+h)+6f(x)-4f(x-h)+f(x-2h)}{h^{4}}}\end{aligned}}$

The errors in these approximations are *O*(*h*4), *O*(*h*2) and *O*(*h*2) respectively.

### Relationship to Lagrange interpolating polynomials

As an alternative to deriving the finite difference weights from the Taylor series, they may be obtained by differentiating the Lagrange polynomials

$\ell _{j}(\xi )=\prod _{i=0,\,i\neq j}^{k}{\frac {\xi -x_{i}}{x_{j}-x_{i}}},$

where the interpolation points are

$x_{0}=x-2h,\quad x_{1}=x-h,\quad x_{2}=x,\quad x_{3}=x+h,\quad x_{4}=x+2h.$

Then, the quartic polynomial $p_{4}(x)$ interpolating *f*(*x*) at these five points is

$p_{4}(x)=\sum _{j=0}^{4}f(x_{j})\ell _{j}(x)$

and its derivative is

$p_{4}'(x)=\sum _{j=0}^{4}f(x_{j})\ell '_{j}(x).$

So, the finite difference approximation of *f* ′(*x*) at the middle point *x* = *x*2 is

$f'(x_{2})=\ell _{0}'(x_{2})f(x_{0})+\ell _{1}'(x_{2})f(x_{1})+\ell _{2}'(x_{2})f(x_{2})+\ell _{3}'(x_{2})f(x_{3})+\ell _{4}'(x_{2})f(x_{4})+O(h^{4})$

Evaluating the derivatives of the five Lagrange polynomials at *x* = *x*2 gives the same weights as above. This method can be more flexible as the extension to a non-uniform grid is quite straightforward.

## In two dimensions

In two dimensions, if for example the size of the squares in the grid is *h* by *h*, the five point stencil of a point (*x*, *y*) in the grid is

$\{(x-h,y),(x,y),(x+h,y),(x,y-h),(x,y+h)\},$

forming a pattern that is also called a quincunx. This stencil is often used to approximate the Laplacian of a function of two variables:

$\nabla ^{2}f(x,y)\approx {\frac {f(x-h,y)+f(x+h,y)+f(x,y-h)+f(x,y+h)-4f(x,y)}{h^{2}}}.$

The error in this approximation is *O*(*h* 2), which may be explained as follows:

From the 3 point stencils for the second derivative of a function with respect to x and y:

${\begin{aligned}{\frac {\partial ^{2}f}{\partial x^{2}}}&={\frac {f\left(x+\Delta x,y\right)+f\left(x-\Delta x,y\right)-2f(x,y)}{\Delta x^{2}}}-2{\frac {f^{(4)}(x,y)}{4!}}\Delta x^{2}+\cdots \\[1ex]{\frac {\partial ^{2}f}{\partial y^{2}}}&={\frac {f\left(x,y+\Delta y\right)+f\left(x,y-\Delta y\right)-2f(x,y)}{\Delta y^{2}}}-2{\frac {f^{(4)}(x,y)}{4!}}\Delta y^{2}+\cdots \end{aligned}}$

If we assume $\Delta x=\Delta y=h$ :

${\begin{aligned}\nabla ^{2}f&={\frac {\partial ^{2}f}{\partial x^{2}}}+{\frac {\partial ^{2}f}{\partial y^{2}}}\\[1ex]&={\frac {f\left(x+h,y\right)+f\left(x-h,y\right)+f\left(x,y+h\right)+f\left(x,y-h\right)-4f(x,y)}{h^{2}}}-4{\frac {f^{(4)}(x,y)}{4!}}h^{2}+\cdots \\[1ex]&={\frac {f\left(x+h,y\right)+f\left(x-h,y\right)+f\left(x,y+h\right)+f\left(x,y-h\right)-4f(x,y)}{h^{2}}}+O\left(h^{2}\right)\\\end{aligned}}$
