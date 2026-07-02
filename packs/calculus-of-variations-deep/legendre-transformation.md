---
title: "Legendre transformation"
source: https://en.wikipedia.org/wiki/Legendre_transformation
domain: calculus-of-variations-deep
license: CC-BY-SA-4.0
tags: calculus of variations, euler-lagrange equation, beltrami identity, hamilton principle
fetched: 2026-07-02
---

# Legendre transformation

In mathematics, the **Legendre transformation** (or **Legendre transform**), first introduced by Adrien-Marie Legendre in 1787 when studying the minimal surface problem, is an involutive transformation on real-valued functions that are convex on a real variable. Specifically, if a real-valued multivariable function is convex on one of its independent real variables, then the Legendre transform with respect to this variable is applicable to the function.

In physical problems, the Legendre transform is used to convert functions of one quantity (such as position, pressure, or temperature) into functions of the conjugate quantity (momentum, volume, and entropy, respectively). In this way, it is commonly used in classical mechanics to derive the Hamiltonian formalism out of the Lagrangian formalism (or vice versa) and in thermodynamics to derive the thermodynamic potentials, as well as in the solution of differential equations of several variables.

For sufficiently smooth functions on the real line, the Legendre transform $f^{*}$ of a function f can be specified, up to an additive constant, by the condition that the functions' first derivatives are inverse functions of each other. This can be expressed as ${\frac {df}{dx}}=\left({\frac {df^{*}}{dx}}\right)^{-1}~$ in Leibniz's notation.

The generalization of the Legendre transformation to affine spaces and non-convex functions is known as the convex conjugate (also called the Legendre–Fenchel transformation), which can be used to construct a function's convex hull.

## Definition

### Definition in one-dimensional real space

Let $I\subset \mathbb {R}$ be an interval, and $f:I\to \mathbb {R}$ a convex function; then the *Legendre transform* *of* f is the function $f^{*}:I^{*}\to \mathbb {R}$ defined by $f^{*}(x^{*})=\sup _{x\in I}(x^{*}x-f(x)),\ \ \ \ I^{*}=\left\{x^{*}\in \mathbb {R} :\sup _{x\in I}(x^{*}x-f(x))<\infty \right\}$ where ${\textstyle \sup }$ denotes the supremum over I , e.g., ${\textstyle x}$ in ${\textstyle I}$ is chosen such that ${\textstyle x^{*}x-f(x)}$ is maximized at each ${\textstyle x^{*}}$ , or ${\textstyle x^{*}}$ is such that $x^{*}x-f(x)$ has a bounded value throughout ${\textstyle I}$ (e.g., when $f(x)$ is a linear function).

The function $f^{*}$ is called the convex conjugate function of f . For historical reasons (rooted in analytic mechanics), the conjugate variable is often denoted p , instead of $x^{*}$ . If the convex function f is defined on the whole line and is everywhere differentiable, then $f^{*}(p)=\sup _{x\in I}(px-f(x))=\left(px-f(x)\right)|_{x=(f')^{-1}(p)}$ can be interpreted as the negative of the y -intercept of the tangent line to the graph of f that has slope p .

### Definition in *n*-dimensional real space

The generalization to convex functions $f:X\to \mathbb {R}$ on a convex set $X\subset \mathbb {R} ^{n}$ is straightforward: $f^{*}:X^{*}\to \mathbb {R}$ has domain $X^{*}=\left\{x^{*}\in \mathbb {R} ^{n}:\sup _{x\in X}(\langle x^{*},x\rangle -f(x))<\infty \right\}$ and is defined by $f^{*}(x^{*})=\sup _{x\in X}(\langle x^{*},x\rangle -f(x)),\quad x^{*}\in X^{*}~,$ where $\langle x^{*},x\rangle$ denotes the dot product of $x^{*}$ and x .

The Legendre transformation is an application of the duality relationship between points and lines. The functional relationship specified by f can be represented equally well as a set of $(x,y)$ points, or as a set of tangent lines specified by their slope and intercept values.

### Understanding the Legendre transform in terms of derivatives

For a differentiable convex function f on the real line with the first derivative $f'$ and its inverse $(f')^{-1}$ , the Legendre transform of f , $f^{*}$ , can be specified, up to an additive constant, by the condition that the functions' first derivatives are inverse functions of each other, i.e., $f'=((f^{*})')^{-1}$ and $(f^{*})'=(f')^{-1}$ .

To see this, first note that if f as a convex function on the real line is differentiable and ${\overline {x}}$ is a critical point of the function of $x\mapsto p\cdot x-f(x)$ , then the supremum is achieved at ${\textstyle {\overline {x}}}$ (by convexity, see the first figure in this Wikipedia page). Therefore, the Legendre transform of f is $f^{*}(p)=p\cdot {\overline {x}}-f({\overline {x}})$ .

Then, suppose that the first derivative $f'$ is invertible and let the inverse be $g=(f')^{-1}$ . Then for each ${\textstyle p}$ , the point $g(p)$ is the unique critical point ${\textstyle {\overline {x}}}$ of the function $x\mapsto px-f(x)$ (i.e., ${\overline {x}}=g(p)$ ) because $f'(g(p))=p$ and the function's first derivative with respect to x at $g(p)$ is $p-f'(g(p))=0$ . Hence we have $f^{*}(p)=p\cdot g(p)-f(g(p))$ for each ${\textstyle p}$ . By differentiating with respect to ${\textstyle p}$ , we find $(f^{*})'(p)=g(p)+p\cdot g'(p)-f'(g(p))\cdot g'(p).$ Since $f'(g(p))=p$ this simplifies to $(f^{*})'(p)=g(p)=(f')^{-1}(p)$ . In other words, *$(f^{*})'$ and $f'$ are inverses to each other*.

In general, if $h'=(f')^{-1}$ as the inverse of $f',$ then $h'=(f^{*})'$ so integration gives $f^{*}=h+c$ , where c is a constant.

In practical terms, given $f(x),$ the parametric plot of $xf'(x)-f(x)$ versus $f'(x)$ amounts to the graph of $f^{*}(p)$ versus $p.$

In some cases (e.g., thermodynamic potentials, below), a non-standard requirement is used, amounting to an alternative definition of *f* * with a *minus sign*, $f(x)-f^{*}(p)=xp.$

### Definition in physical contexts

In analytical mechanics and thermodynamics, the Legendre transformation is usually defined as follows: suppose f is a function of x ; then we have

$df={\frac {df}{dx}}dx.$

Performing the Legendre transformation on this function means that we take $p={\frac {df}{dx}}$ as the independent variable, so that the above expression can be written as

$df=p\,dx,$

and according to the product rule $d(uv)=u\,dv+v\,du,$ we then have

$d\left(xp-f\right)=x\,dp+p\,dx-df=x\,dp,$

and taking $f^{*}=xp-f,$ we have $df^{*}=x\,dp,$ which means

${\frac {df^{*}}{dp}}=x.$

When f is a function of n variables $x_{1},x_{2},\cdots ,x_{n}$ , then we can perform the Legendre transformation on each one or several variables: we have

$df=p_{1}\,dx_{1}+p_{2}\,dx_{2}+\cdots +p_{n}\,dx_{n},$

where $p_{i}={\frac {\partial f}{\partial x_{i}}}.$ Then if we want to perform the Legendre transformation on, e.g. $x_{1}$ , then we take $p_{1}$ together with $x_{2},\cdots ,x_{n}$ as independent variables, and with Leibniz's rule we have

$d(x_{1}p_{1}-f)=x_{1}\,dp_{1}-p_{2}\,dx_{2}-\cdots -p_{n}\,dx_{n}.$

So for the function $\varphi (p_{1},x_{2},\cdots ,x_{n})=x_{1}p_{1}-f(x_{1},x_{2},\cdots ,x_{n}),$ we have

${\frac {\partial \varphi }{\partial p_{1}}}=x_{1},\quad {\frac {\partial \varphi }{\partial x_{2}}}=-p_{2},\quad \cdots ,\quad {\frac {\partial \varphi }{\partial x_{n}}}=-p_{n}.$

We can also do this transformation for variables $x_{2},\cdots ,x_{n}$ . If we do it to all the variables, then we have

$d\varphi =x_{1}\,dp_{1}+x_{2}\,dp_{2}+\cdots +x_{n}\,dp_{n}$ where $\varphi =x_{1}p_{1}+x_{2}p_{2}+\cdots +x_{n}p_{n}-f.$

In analytical mechanics, people perform this transformation on variables ${\dot {q}}_{1},{\dot {q}}_{2},\cdots ,{\dot {q}}_{n}$ of the Lagrangian $L(q_{1},\cdots ,q_{n},{\dot {q}}_{1},\cdots ,{\dot {q}}_{n})$ to get the Hamiltonian:

$H(q_{1},\cdots ,q_{n},p_{1},\cdots ,p_{n})=\sum _{i=1}^{n}p_{i}{\dot {q}}_{i}-L(q_{1},\cdots ,q_{n},{\dot {q}}_{1}\cdots ,{\dot {q}}_{n}).$

In thermodynamics, this transformation is applied to variables according to the type of thermodynamic system desired; for example, starting from the energy representation cardinal function of state, the internal energy $U(S,V)$ , we have

$dU=T\,dS-p\,dV,$

so we can perform the Legendre transformation on either or both of $S,V$ to yield

${\begin{aligned}dH&=d(U+pV)\ \ \ \ \ \ \ \ \ \ =\ \ \ \ T\,dS+V\,dp\\dF&=d(U-TS)\ \ \ \ \ \ \ \ \ \ =-S\,dT-p\,dV\\dG&=d(U-TS+pV)=-S\,dT+V\,dp,\end{aligned}}$

and each of these three expressions has a physical meaning.

This definition of the Legendre transformation is the one originally introduced by Legendre in his work in 1787, and is still applied by physicists nowadays. Indeed, this definition is mathematically rigorous if we treat all the variables and functions defined above (for example, $f,x_{1},\cdots ,x_{n},p_{1},\cdots ,p_{n},$ ) as differentiable functions defined on an open set of $\mathbb {R} ^{n}$ or on a differentiable manifold, and $df,dx_{i},dp_{i}$ their differentials (which are treated as cotangent vectors in the context of differentiable manifolds). This definition is equivalent to the modern mathematicians' definition as long as f is differentiable and convex for the variables $x_{1},x_{2},\cdots ,x_{n}.$

## Properties

- The Legendre transform of a convex function, of which double derivative values are all positive, is also a convex function of which double derivative values are all positive.*Proof.* Let us show this with a doubly differentiable function $f(x)$ with all positive double derivative values and with a bijective (invertible) derivative. For a fixed p , let ${\bar {x}}$ maximize or make the function $px-f(x)$ bounded over x . Then the Legendre transformation of f is $f^{*}(p)=p{\bar {x}}-f({\bar {x}})$ , thus, $f'({\bar {x}})=p$ by the maximizing or bounding condition ${\frac {d}{dx}}(px-f(x))=p-f'(x)=0$ . Note that ${\bar {x}}$ depends on p . (This can be visually shown in the 1st figure of this page above.) Thus ${\bar {x}}=g(p)$ where $g\equiv (f')^{-1}$ , meaning that g is the inverse of $f'$ that is the derivative of f (so $f'(g(p))=p$ ). Note that g is also differentiable with the following derivative (Inverse function rule), ${\frac {dg(p)}{dp}}={\frac {1}{f''(g(p))}}~.$ Thus, the Legendre transformation $f^{*}(p)=pg(p)-f(g(p))$ is the composition of differentiable functions, hence it is differentiable. Applying the product rule and the chain rule with the found equality ${\bar {x}}=g(p)$ yields ${\frac {d(f^{*})}{dp}}=g(p)+\left(p-f'(g(p))\right)\cdot {\frac {dg(p)}{dp}}=g(p),$ giving ${\frac {d^{2}(f^{*})}{dp^{2}}}={\frac {dg(p)}{dp}}={\frac {1}{f''(g(p))}}>0,$ so $f^{*}$ is convex with its double derivatives are all positive.
- The Legendre transformation is an involution, i.e., $f^{**}=f~$ . *Proof.* By using the above identities as $f'({\bar {x}})=p$ , ${\bar {x}}=g(p)$ , $f^{*}(p)=p{\bar {x}}-f({\bar {x}})$ and its derivative $(f^{*})'(p)=g(p)$ , ${\begin{aligned}f^{**}(y)&{}=\left(y\cdot {\bar {p}}-f^{*}({\bar {p}})\right)|_{(f^{*})'({\bar {p}})=y}\\[5pt]&{}=g({\bar {p}})\cdot {\bar {p}}-f^{*}({\bar {p}})\\[5pt]&{}=g({\bar {p}})\cdot {\bar {p}}-({\bar {p}}g({\bar {p}})-f(g({\bar {p}})))\\[5pt]&{}=f(g({\bar {p}}))\\[5pt]&{}=f(y)~.\end{aligned}}$ Note that this derivation does not require the condition to have all positive values in double derivative of the original function f .

## Identities

As shown above, for a convex function $f(x)$ , with $x={\bar {x}}$ maximizing or making $px-f(x)$ bounded at each p to define the Legendre transform $f^{*}(p)=p{\bar {x}}-f({\bar {x}})$ and with $g\equiv (f')^{-1}$ , the following identities hold.

- $f'({\bar {x}})=p$ ,
- ${\bar {x}}=g(p)$ ,
- $(f^{*})'(p)=g(p)$ .

## Examples

### Example 1

Consider the exponential function $f(x)=e^{x},$ which has the domain $I=\mathbb {R}$ . From the definition, the Legendre transform is $f^{*}(x^{*})=\sup _{x\in \mathbb {R} }(x^{*}x-e^{x}),\quad x^{*}\in I^{*}$ where $I^{*}$ remains to be determined. To evaluate the supremum, compute the derivative of $x^{*}x-e^{x}$ with respect to x and set equal to zero: ${\frac {d}{dx}}(x^{*}x-e^{x})=x^{*}-e^{x}=0.$ The second derivative $-e^{x}$ is negative everywhere, so the maximal value is achieved at $x=\ln(x^{*})$ . Thus, the Legendre transform is $f^{*}(x^{*})=x^{*}\ln(x^{*})-e^{\ln(x^{*})}=x^{*}(\ln(x^{*})-1)$ and has domain $I^{*}=(0,\infty ).$ This illustrates that the domains of a function and its Legendre transform can be different.

To find the Legendre transformation of the Legendre transformation of f , $f^{**}(x)=\sup _{x^{*}\in \mathbb {R} }(xx^{*}-x^{*}(\ln(x^{*})-1)),\quad x\in I,$ where a variable x is intentionally used as the argument of the function $f^{**}$ to show the involution property of the Legendre transform as $f^{**}=f$ . We compute ${\begin{aligned}0&={\frac {d}{dx^{*}}}{\big (}xx^{*}-x^{*}(\ln(x^{*})-1){\big )}=x-\ln(x^{*})\end{aligned}}$ thus the maximum occurs at $x^{*}=e^{x}$ because the second derivative ${\frac {d^{2}}{{dx^{*}}^{2}}}f^{**}(x)=-{\frac {1}{x^{*}}}<0$ over the domain of $f^{**}$ as $I^{*}=(0,\infty ).$ As a result, $f^{**}$ is found as ${\begin{aligned}f^{**}(x)&=xe^{x}-e^{x}(\ln(e^{x})-1)=e^{x},\end{aligned}}$ thereby confirming that $f=f^{**},$ as expected.

### Example 2

Let *f*(*x*) = *cx*2 be defined on **R**, where *c* > 0 is a fixed constant.

For *x** fixed, the function of x, *x***x* − *f*(*x*) = *x***x* − *cx*2 has the first derivative *x** − 2*cx* and second derivative −2*c*; there is one stationary point at *x* = *x**/2*c*, which is always a maximum.

Thus, *I** = **R** and $f^{*}(x^{*})={\frac {{x^{*}}^{2}}{4c}}~.$

The first derivatives of *f*, 2*cx*, and of *f* *, *x**/(2*c*), are inverse functions to each other. Clearly, furthermore, $f^{**}(x)={\frac {1}{4(1/4c)}}x^{2}=cx^{2}~,$ namely *f* ** = *f*.

### Example 3

Let *f*(*x*) = *x*2 for *x* ∈ (*I* = [2, 3]).

For *x** fixed, *x***x* − *f*(*x*) is continuous on I compact, hence it always takes a finite maximum on it; it follows that the domain of the Legendre transform of f is *I** = **R**.

The stationary point at *x* = *x**/2 (found by setting that the first derivative of *x***x* − *f*(*x*) with respect to x equal to zero) is in the domain [2, 3] if and only if 4 ≤ *x** ≤ 6. Otherwise the maximum is taken either at *x* = 2 or *x* = 3 because the second derivative of *x***x* − *f*(*x*) with respect to x is negative as $-2$ ; for a part of the domain $x^{*}<4$ the maximum that *x***x* − *f*(*x*) can take with respect to $x\in [2,3]$ is obtained at $x=2$ while for $x^{*}>6$ it becomes the maximum at $x=3$ . Thus, it follows that $f^{*}(x^{*})={\begin{cases}2x^{*}-4,&x^{*}<4\\{\frac {{x^{*}}^{2}}{4}},&4\leq x^{*}\leq 6,\\3x^{*}-9,&x^{*}>6.\end{cases}}$

### Example 4

The function *f*(*x*) = *cx* is convex, for every x (strict convexity is not required for the Legendre transformation to be well defined). Clearly *x***x* − *f*(*x*) = (*x** − *c*)*x* is never bounded from above as a function of x, unless *x** − *c* = 0. Hence *f** is defined on *I** = {*c*} and *f**(*c*) = 0. (The definition of the Legendre transform requires the existence of the supremum, that requires upper bounds.)

One may check involutivity: of course, *x***x* − *f**(*x**) is always bounded as a function of *x**∈{*c*}, hence *I*** = **R**. Then, for all x one has $\sup _{x^{*}\in \{c\}}(xx^{*}-f^{*}(x^{*}))=xc,$ and hence *f* **(*x*) = *cx* = *f*(*x*).

### Example 5

As an example of a convex continuous function that is not everywhere differentiable, consider $f(x)=|x|$ . This gives $f^{*}(x^{*})=\sup _{x}(xx^{*}-|x|)=\max \left(\sup _{x\geq 0}x(x^{*}-1),\,\sup _{x\leq 0}x(x^{*}+1)\right),$ and thus $f^{*}(x^{*})=0$ on its domain $I^{*}=[-1,1]$ .

### Example 6: several variables

Let $f(x)=\langle x,Ax\rangle +c$ be defined on *X* = **R***n*, where A is a real, positive definite matrix.

Then f is convex, and $\langle p,x\rangle -f(x)=\langle p,x\rangle -\langle x,Ax\rangle -c,$ has gradient *p* − 2*Ax* and Hessian −2*A*, which is negative; hence the stationary point *x* = *A*−1*p*/2 is a maximum.

We have *X** = **R***n*, and $f^{*}(p)={\frac {1}{4}}\langle p,A^{-1}p\rangle -c.$

## Behavior of differentials under Legendre transforms

The Legendre transform is linked to integration by parts, *p dx* = *d*(*px*) − *x dp*.

Let *f*(*x*,*y*) be a function of two independent variables x and y, with the differential $df={\frac {\partial f}{\partial x}}\,dx+{\frac {\partial f}{\partial y}}\,dy=p\,dx+v\,dy.$

Assume that the function f is convex in x for all y, so that one may perform the Legendre transform on f in x, with p the variable conjugate to x (for information, there is a relation ${\frac {\partial f}{\partial x}}|_{\bar {x}}=p$ where ${\bar {x}}$ is a point in x maximizing or making $px-f(x,y)$ bounded for given p and y). Since the new independent variable of the transform with respect to f is p, the differentials *dx* and *dy* in df devolve to *dp* and *dy* in the differential of the transform, i.e., we build another function with its differential expressed in terms of the new basis *dp* and *dy*.

We thus consider the function *g*(*p*, *y*) = *f* − *px* so that $dg=df-p\,dx-x\,dp=-x\,dp+v\,dy$ $x=-{\frac {\partial g}{\partial p}}$ $v={\frac {\partial g}{\partial y}}.$

The function −*g*(*p*, *y*) is the Legendre transform of *f*(*x*, *y*), where only the independent variable x has been supplanted by p. This is widely used in thermodynamics, as illustrated below.

## Applications

### Analytical mechanics

A Legendre transform is used in classical mechanics to derive the Hamiltonian formulation from the Lagrangian formulation, and conversely. A typical Lagrangian has the form

$L(v,q)={\tfrac {1}{2}}\langle v,Mv\rangle -V(q),$ where $(v,q)$ are coordinates on **R***n* × **R***n*, M is a positive definite real matrix, and $\langle x,y\rangle =\sum _{j}x_{j}y_{j}.$

For every q fixed, $L(v,q)$ is a convex function of v , while $V(q)$ plays the role of a constant.

Hence the Legendre transform of $L(v,q)$ as a function of v is the Hamiltonian function, $H(p,q)={\tfrac {1}{2}}\langle p,M^{-1}p\rangle +V(q).$

In a more general setting, $(v,q)$ are local coordinates on the tangent bundle $T{\mathcal {M}}$ of a manifold ${\mathcal {M}}$ . For each q, $L(v,q)$ is a convex function of the tangent space *Vq*. The Legendre transform gives the Hamiltonian $H(p,q)$ as a function of the coordinates (*p*, *q*) of the cotangent bundle $T^{*}{\mathcal {M}}$ ; the inner product used to define the Legendre transform is inherited from the pertinent canonical symplectic structure. In this abstract setting, the Legendre transformation corresponds to the tautological one-form.

### Thermodynamics

The strategy behind the use of Legendre transforms in thermodynamics is to shift from a function that depends on a variable to a new (conjugate) function that depends on a new variable, the conjugate of the original one. The new variable is the partial derivative of the original function with respect to the original variable. The new function is the difference between the original function and the product of the old and new variables. Typically, this transformation is useful because it shifts the dependence of, e.g., the energy from an extensive variable to its conjugate intensive variable, which can often be controlled more easily in a physical experiment.

For example, the internal energy U is an explicit function of the *extensive variables* entropy S, volume V, and chemical composition Ni (e.g., $i=1,2,3,\ldots$ ) $U=U\left(S,V,\{N_{i}\}\right),$ which has a total differential $dU=T\,dS-P\,dV+\sum \mu _{i}\,dN_{i}$

where $T=\left.{\frac {\partial U}{\partial S}}\right\vert _{V,N_{i{\text{ for all }}i{\text{ values}}}},P=\left.-{\frac {\partial U}{\partial V}}\right\vert _{S,N_{i\ {\text{for all }}i{\text{ values}}}},\mu _{i}=\left.{\frac {\partial U}{\partial N_{i}}}\right\vert _{S,V,N_{j{\text{ for all }}j\neq i}}$ .

(Subscripts are not necessary by the definition of partial derivatives but left here for clarifying variables.) Stipulating some common reference state, by using the (non-standard) Legendre transform of the internal energy U with respect to volume V, the enthalpy H may be obtained as the following.

To get the (standard) Legendre transform ${\textstyle U^{*}}$ of the internal energy U with respect to volume V, the function ${\textstyle u\left(p,S,V,\{{{N}_{i}}\}\right)=pV-U}$ is defined first, then it shall be maximized or bounded by V. To do this, the condition ${\textstyle {\frac {\partial u}{\partial V}}=p-{\frac {\partial U}{\partial V}}=0\to p={\frac {\partial U}{\partial V}}}$ needs to be satisfied, so ${\textstyle U^{*}={\frac {\partial U}{\partial V}}V-U}$ is obtained. This approach is justified because U is a linear function with respect to V (so a convex function on V) by the definition of extensive variables. The non-standard Legendre transform here is obtained by negating the standard version, so ${\textstyle -U^{*}=H=U-{\frac {\partial U}{\partial V}}V=U+PV}$ .

H is definitely a state function as it is obtained by adding PV (P and V as state variables) to a state function ${\textstyle U=U\left(S,V,\{N_{i}\}\right)}$ , so its differential is an exact differential. Because of ${\textstyle dH=T\,dS+V\,dP+\sum \mu _{i}\,dN_{i}}$ and the fact that it must be an exact differential, $H=H(S,P,\{N_{i}\})$ .

The enthalpy is suitable for description of processes in which the pressure is controlled from the surroundings.

It is likewise possible to shift the dependence of the energy from the extensive variable of entropy, S, to the (often more convenient) intensive variable T, resulting in the Helmholtz and Gibbs free energies. The Helmholtz free energy A, and Gibbs free energy G, are obtained by performing Legendre transforms of the internal energy and enthalpy, respectively: ${\begin{aligned}A&=U-TS~,\\G&=H-TS=U+PV-TS~.\end{aligned}}$

The Helmholtz free energy is often the most useful thermodynamic potential when temperature and volume are controlled from the surroundings, while the Gibbs free energy is often the most useful when temperature and pressure are controlled from the surroundings.

### Variable capacitor

As another example from physics, consider a parallel conductive plate capacitor, in which the plates can move relative to one another. Such a capacitor would allow transfer of the electric energy which is stored in the capacitor into external mechanical work, done by the force acting on the plates. One may think of the electric charge as analogous to the "charge" of a gas in a cylinder, with the resulting mechanical force exerted on a piston.

Compute the force on the plates as a function of **x**, the distance which separates them. To find the force, compute the potential energy, and then apply the definition of force as the gradient of the potential energy function.

The electrostatic potential energy stored in a capacitor of the capacitance *C*(**x**) and a positive electric charge +*Q* or negative charge -*Q* on each conductive plate is (with using the definition of the capacitance as ${\textstyle C={\frac {Q}{V}}}$ ),

$U(Q,\mathbf {x} )={\frac {1}{2}}QV(Q,\mathbf {x} )={\frac {1}{2}}{\frac {Q^{2}}{C(\mathbf {x} )}},~$

where the dependence on the area of the plates, the dielectric constant of the insulation material between the plates, and the separation **x** are abstracted away as the capacitance *C*(**x**). (For a parallel plate capacitor, this is proportional to the area of the plates and inversely proportional to the separation.)

The force **F** between the plates due to the electric field created by the charge separation is then $\mathbf {F} (\mathbf {x} )=-{\frac {dU}{d\mathbf {x} }}~.$

If the capacitor is not connected to any electric circuit, then the *electric charges* on the plates remain constant and the voltage varies when the plates move with respect to each other, and the force is the negative gradient of the electrostatic potential energy as $\mathbf {F} (\mathbf {x} )={\frac {1}{2}}{\frac {dC(\mathbf {x} )}{d\mathbf {x} }}{\frac {Q^{2}}{{C(\mathbf {x} )}^{2}}}={\frac {1}{2}}{\frac {dC(\mathbf {x} )}{d\mathbf {x} }}V(\mathbf {x} )^{2}$

where ${\textstyle V(Q,\mathbf {x} )=V(\mathbf {x} )}$ as the charge is fixed in this configuration.

However, instead, suppose that the *voltage* between the plates *V* is maintained constant as the plate moves by connection to a battery, which is a reservoir for electric charges at a constant potential difference. Then the amount of *charges* ${\textstyle Q}$ *is a variable* instead of the voltage; ${\textstyle Q}$ and ${\textstyle V}$ are the Legendre conjugate to each other. To find the force, first compute the non-standard Legendre transform ${\textstyle U^{*}}$ with respect to ${\textstyle Q}$ (also with using ${\textstyle C={\frac {Q}{V}}}$ ),

$U^{*}=U-\left.{\frac {\partial U}{\partial Q}}\right|_{\mathbf {x} }\cdot Q=U-{\frac {1}{2C(\mathbf {x} )}}\left.{\frac {\partial Q^{2}}{\partial Q}}\right|_{\mathbf {x} }\cdot Q=U-QV={\frac {1}{2}}QV-QV=-{\frac {1}{2}}QV=-{\frac {1}{2}}V^{2}C(\mathbf {x} ).$

This transformation is possible because ${\textstyle U}$ is now a linear function of ${\textstyle Q}$ so is convex on it. The force now becomes the negative gradient of this Legendre transform, resulting in the same force obtained from the original function ${\textstyle U}$ , $\mathbf {F} (\mathbf {x} )=-{\frac {dU^{*}}{d\mathbf {x} }}={\frac {1}{2}}{\frac {dC(\mathbf {x} )}{d\mathbf {x} }}V^{2}.$

The two conjugate energies ${\textstyle U}$ and ${\textstyle U^{*}}$ happen to stand opposite to each other (their signs are opposite), only because of the linearity of the capacitance—except now *Q* is no longer a constant. They reflect the two different pathways of storing energy into the capacitor, resulting in, for instance, the same "pull" between a capacitor's plates.

### Probability theory

In large deviations theory, the *rate function* is defined as the Legendre transformation of the logarithm of the moment generating function of a random variable. An important application of the rate function is in the calculation of tail probabilities of sums of i.i.d. random variables, in particular in Cramér's theorem.

If $X_{n}$ are i.i.d. random variables, let $S_{n}=X_{1}+\cdots +X_{n}$ be the associated random walk and $M(\xi )$ the moment generating function of $X_{1}$ . For $\xi \in \mathbb {R}$ , $E[e^{\xi S_{n}}]=M(\xi )^{n}$ . Hence, by Markov's inequality, one has for $\xi \geq 0$ and $a\in \mathbb {R}$ $P(S_{n}/n>a)\leq e^{-n\xi a}M(\xi )^{n}=\exp[-n(\xi a-\Lambda (\xi ))]$ where $\Lambda (\xi )=\log M(\xi )$ . Since the left-hand side is independent of $\xi$ , we may take the infimum of the right-hand side, which leads one to consider the supremum of $\xi a-\Lambda (\xi )$ , i.e., the Legendre transform of $\Lambda$ , evaluated at $x=a$ .

### Microeconomics

Legendre transformation arises naturally in microeconomics in the process of finding the *supply* *S*(*P*) of some product given a fixed price *P* on the market knowing the cost function *C*(*Q*), i.e. the cost for the producer to make/mine/etc. *Q* units of the given product.

A simple theory explains the shape of the supply curve based solely on the cost function. Let us suppose the market price for a one unit of our product is *P*. For a company selling this good, the best strategy is to adjust the production *Q* so that its profit is maximized. We can maximize the profit ${\text{profit}}={\text{revenue}}-{\text{costs}}=PQ-C(Q)$ by differentiating with respect to *Q* and solving $P-C'(Q_{\text{opt}})=0.$

*Q*opt represents the optimal quantity *Q* of goods that the producer is willing to supply, which is indeed the supply itself: $S(P)=Q_{\text{opt}}(P)=(C')^{-1}(P).$

If we consider the maximal profit as a function of price, ${\text{profit}}_{\text{max}}(P)$ , we see that it is the Legendre transform of the cost function $C(Q)$ .

## Geometric interpretation

For a strictly convex function, the Legendre transformation can be interpreted as a mapping between the graph of the function and the family of tangents of the graph. (For a function of one variable, the tangents are well-defined at all but at most countably many points, since a convex function is differentiable at all but at most countably many points.)

The equation of a line with slope p and y -intercept b is given by $y=px+b$ . For this line to be tangent to the graph of a function f at the point $\left(x_{0},f(x_{0})\right)$ requires $f(x_{0})=px_{0}+b$ and $p=f'(x_{0}).$

Being the derivative of a strictly convex function, the function $f'$ is strictly monotone and thus injective. The second equation can be solved for ${\textstyle x_{0}=f^{\prime -1}(p),}$ allowing elimination of $x_{0}$ from the first, and solving for the y -intercept b of the tangent as a function of its slope $p,$ ${\textstyle b=f(x_{0})-px_{0}=f\left(f^{\prime -1}(p)\right)-p\cdot f^{\prime -1}(p)=-f^{\star }(p)}$ where $f^{\star }$ denotes the Legendre transform of $f.$

The family of tangent lines of the graph of f parameterized by the slope p is therefore given by ${\textstyle y=px-f^{\star }(p),}$ or, written implicitly, by the solutions of the equation $F(x,y,p)=y+f^{\star }(p)-px=0~.$

The graph of the original function can be reconstructed from this family of lines as the envelope of this family by demanding ${\frac {\partial F(x,y,p)}{\partial p}}=f^{\star \prime }(p)-x=0.$

Eliminating p from these two equations gives $y=x\cdot f^{\star \prime -1}(x)-f^{\star }\left(f^{\star \prime -1}(x)\right).$

Identifying y with $f(x)$ and recognizing the right side of the preceding equation as the Legendre transform of $f^{\star },$ yield ${\textstyle f(x)=f^{\star \star }(x)~.}$

## Legendre transformation in more than one dimension

For a differentiable real-valued function on an open convex subset U of **R***n* the Legendre conjugate of the pair (*U*, *f*) is defined to be the pair (*V*, *g*), where V is the image of U under the gradient mapping *Df*, and g is the function on V given by the formula $g(y)=\left\langle y,x\right\rangle -f(x),\qquad x=\left(Df\right)^{-1}(y)$ where $\left\langle u,v\right\rangle =\sum _{k=1}^{n}u_{k}\cdot v_{k}$

is the scalar product on **R***n*. The multidimensional transform can be interpreted as an encoding of the convex hull of the function's epigraph in terms of its supporting hyperplanes. This can be seen as consequence of the following two observations. On the one hand, the hyperplane tangent to the epigraph of f at some point $(\mathbf {x} ,f(\mathbf {x} ))\in U\times \mathbb {R}$ has normal vector $(\nabla f(\mathbf {x} ),-1)\in \mathbb {R} ^{n+1}$ . On the other hand, any closed convex set $C\in \mathbb {R} ^{m}$ can be characterized via the set of its supporting hyperplanes by the equations $\mathbf {x} \cdot \mathbf {n} =h_{C}(\mathbf {n} )$ , where $h_{C}(\mathbf {n} )$ is the support function of C . But the definition of Legendre transform via the maximization matches precisely that of the support function, that is, $f^{*}(\mathbf {x} )=h_{\operatorname {epi} (f)}(\mathbf {x} ,-1)$ . We thus conclude that the Legendre transform characterizes the epigraph in the sense that the tangent plane to the epigraph at any point $(\mathbf {x} ,f(\mathbf {x} ))$ is given explicitly by $\{\mathbf {z} \in \mathbb {R} ^{n+1}:\,\,\mathbf {z} \cdot \mathbf {x} =f^{*}(\mathbf {x} )\}.$

Alternatively, if X is a vector space and *Y* is its dual vector space, then for each point x of *X* and *y* of *Y*, there is a natural identification of the cotangent spaces T**Xx* with *Y* and T**Yy* with *X*. If f is a real differentiable function over *X*, then its exterior derivative, *df*, is a section of the cotangent bundle T**X* and as such, we can construct a map from *X* to *Y*. Similarly, if g is a real differentiable function over *Y*, then *dg* defines a map from *Y* to *X*. If both maps happen to be inverses of each other, we say we have a Legendre transform. The notion of the tautological one-form is commonly used in this setting.

When the function is not differentiable, the Legendre transform can still be extended, and is known as the Legendre-Fenchel transformation. In this more general setting, a few properties are lost: for example, the Legendre transform is no longer its own inverse (unless there are extra assumptions, like convexity).

## Legendre transformation on manifolds

Let ${\textstyle M}$ be a smooth manifold, let E and ${\textstyle \pi :E\to M}$ be a vector bundle on M and its associated bundle projection, respectively. Let ${\textstyle L:E\to \mathbb {R} }$ be a smooth function. We think of ${\textstyle L}$ as a Lagrangian by analogy with the classical case where ${\textstyle M=\mathbb {R} }$ , ${\textstyle E=TM=\mathbb {R} \times \mathbb {R} }$ and ${\textstyle L(x,v)={\frac {1}{2}}mv^{2}-V(x)}$ for some positive number ${\textstyle m\in \mathbb {R} }$ and function ${\textstyle V:M\to \mathbb {R} }$ .

As usual, the dual of ${\textstyle E}$ is denoted by ${\textstyle E^{*}}$ . The fiber of ${\textstyle \pi }$ over ${\textstyle x\in M}$ is denoted ${\textstyle E_{x}}$ , and the restriction of ${\textstyle L}$ to ${\textstyle E_{x}}$ is denoted by ${\textstyle L|_{E_{x}}:E_{x}\to \mathbb {R} }$ . The *Legendre transformation* of ${\textstyle L}$ is the smooth morphism $\mathbf {F} L:E\to E^{*}$ defined by ${\textstyle \mathbf {F} L(v)=d(L|_{E_{x}})_{v}\in E_{x}^{*}}$ , where ${\textstyle x=\pi (v)}$ . Here we use the fact that since ${\textstyle E_{x}}$ is a vector space, ${\textstyle T_{v}(E_{x})}$ can be identified with ${\textstyle E_{x}}$ . In other words, ${\textstyle \mathbf {F} L(v)\in E_{x}^{*}}$ is the covector that sends ${\textstyle w\in E_{x}}$ to the directional derivative ${\textstyle \left.{\frac {d}{dt}}\right|_{t=0}L(v+tw)\in \mathbb {R} }$ .

To describe the Legendre transformation locally, let ${\textstyle U\subseteq M}$ be a coordinate chart over which ${\textstyle E}$ is trivial. Picking a trivialization of ${\textstyle E}$ over ${\textstyle U}$ , we obtain charts ${\textstyle E_{U}\cong U\times \mathbb {R} ^{r}}$ and ${\textstyle E_{U}^{*}\cong U\times \mathbb {R} ^{r}}$ . In terms of these charts, we have ${\textstyle \mathbf {F} L(x;v_{1},\dotsc ,v_{r})=(x;p_{1},\dotsc ,p_{r})}$ , where $p_{i}={\frac {\partial L}{\partial v_{i}}}(x;v_{1},\dotsc ,v_{r})$ for all ${\textstyle i=1,\dots ,r}$ . If, as in the classical case, the restriction of ${\textstyle L:E\to \mathbb {R} }$ to each fiber ${\textstyle E_{x}}$ is strictly convex and bounded below by a positive definite quadratic form minus a constant, then the Legendre transform ${\textstyle \mathbf {F} L:E\to E^{*}}$ is a diffeomorphism. Suppose that ${\textstyle \mathbf {F} L}$ is a diffeomorphism and let ${\textstyle H:E^{*}\to \mathbb {R} }$ be the "Hamiltonian" function defined by $H(p)=p\cdot v-L(v),$ where ${\textstyle v=(\mathbf {F} L)^{-1}(p)}$ . Using the natural isomorphism ${\textstyle E\cong E^{**}}$ , we may view the Legendre transformation of ${\textstyle H}$ as a map ${\textstyle \mathbf {F} H:E^{*}\to E}$ . Then we have $(\mathbf {F} L)^{-1}=\mathbf {F} H.$

## Further properties

### Scaling properties

The Legendre transformation has the following scaling properties: For *a* > 0,

$f(x)=a\cdot g(x)\Rightarrow f^{\star }(p)=a\cdot g^{\star }\left({\frac {p}{a}}\right)$ $f(x)=g(a\cdot x)\Rightarrow f^{\star }(p)=g^{\star }\left({\frac {p}{a}}\right).$

It follows that if a function is homogeneous of degree r then its image under the Legendre transformation is a homogeneous function of degree s, where 1/*r* + 1/*s* = 1. (Since *f*(*x*) = *xr*/*r*, with *r* > 1, implies *f**(*p*) = *ps*/*s*.) Thus, the only monomial whose degree is invariant under Legendre transform is the quadratic.

### Behavior under translation

$f(x)=g(x)+b\Rightarrow f^{\star }(p)=g^{\star }(p)-b$ $f(x)=g(x+y)\Rightarrow f^{\star }(p)=g^{\star }(p)-p\cdot y$

### Behavior under inversion

$f(x)=g^{-1}(x)\Rightarrow f^{\star }(p)=-p\cdot g^{\star }\left({\frac {1}{p}}\right)$

### Behavior under linear transformations

Let *A* : **R***n* → **R***m* be a linear transformation. For any convex function f on **R***n*, one has $(Af)^{\star }=f^{\star }A^{\star }$ where *A** is the adjoint operator of A defined by $\left\langle Ax,y^{\star }\right\rangle =\left\langle x,A^{\star }y^{\star }\right\rangle ,$ and *Af* is the *push-forward* of f along A $(Af)(y)=\inf\{f(x):x\in X,Ax=y\}.$

A closed convex function f is symmetric with respect to a given set G of orthogonal linear transformations, $f(Ax)=f(x),\;\forall x,\;\forall A\in G$ if and only if *f** is symmetric with respect to G.

### Infimal convolution

The **infimal convolution** of two functions f and g is defined as

$\left(f\star _{\inf }g\right)(x)=\inf \left\{f(x-y)+g(y)\,|\,y\in \mathbf {R} ^{n}\right\}.$

Let *f*1, ..., *fm* be proper convex functions on **R***n*. Then

$\left(f_{1}\star _{\inf }\cdots \star _{\inf }f_{m}\right)^{\star }=f_{1}^{\star }+\cdots +f_{m}^{\star }.$

### Fenchel's inequality

For any function f and its convex conjugate *f* * *Fenchel's inequality* (also known as the *Fenchel–Young inequality*) holds for every *x* ∈ *X* and *p* ∈ *X**, i.e., *independent* *x*, *p* pairs, $\left\langle p,x\right\rangle \leq f(x)+f^{\star }(p).$
