---
title: "Euler–Lagrange equation"
source: https://en.wikipedia.org/wiki/Euler%E2%80%93Lagrange_equation
domain: lagrangian-mechanics
license: CC-BY-SA-4.0
tags: lagrangian mechanics, principle of least action, generalized coordinates, calculus of variations
fetched: 2026-07-02
---

# Euler–Lagrange equation

In the calculus of variations and classical mechanics, the **Euler–Lagrange equations** are a system of second-order ordinary differential equations whose solutions are stationary points of the given action functional. The equations were discovered in the 1750s by Swiss mathematician Leonhard Euler and Italian mathematician Joseph-Louis Lagrange.

Because a differentiable functional is stationary at its local extrema, the Euler–Lagrange equation is useful for solving optimization problems in which, given some functional, one seeks the function minimizing or maximizing it. This is analogous to Fermat's theorem in calculus, stating that at any point where a differentiable function attains a local extremum its derivative is zero. In Lagrangian mechanics, according to Hamilton's principle of stationary action, the evolution of a physical system is described by the solutions to the Euler equation for the action of the system. In this context Euler equations are usually called **Lagrange equations**. In classical mechanics, it is equivalent to Newton's laws of motion; indeed, the Euler–Lagrange equations will produce the same equations as Newton's Laws. This is particularly useful when analyzing systems whose force vectors are particularly complicated. It has the advantage that it takes the same form in any system of generalized coordinates, and it is better suited to generalizations. In classical field theory there is an analogous equation to calculate the dynamics of a field.

## History

The Euler–Lagrange equation was developed in the 1750s by Euler and Lagrange in connection with their studies of the tautochrone problem. This is the problem of determining a curve on which a weighted particle will fall to a fixed point in a fixed amount of time, independent of the starting point.

Lagrange solved this problem in 1755 and sent the solution to Euler. Both further developed Lagrange's method and applied it to mechanics, which led to the formulation of Lagrangian mechanics. Their correspondence ultimately led to the calculus of variations, a term coined by Euler himself in 1766.

## Statement

Let $(X,L)$ be a real dynamical system with n degrees of freedom. Here X is the configuration space and $L=L(t,{\boldsymbol {q}}(t),{\boldsymbol {v}}(t))$ the *Lagrangian*, i.e. a smooth real-valued function such that ${\boldsymbol {q}}(t)\in X,$ and ${\boldsymbol {v}}(t)={\dot {\boldsymbol {q}}}(t)$ is an n -dimensional "vector of speed", where ${\dot {\boldsymbol {q}}}(t)$ is the time derivative of ${\boldsymbol {q}}(t)$ . (For those familiar with differential geometry, X is a smooth manifold, and $L\colon {\mathbb {R} }_{t}\times TX\to {\mathbb {R} },$ where $TX$ is the tangent bundle of X ).

Let ${\cal {P}}(a,b,{\boldsymbol {x}}_{a},{\boldsymbol {x}}_{b})$ be the set of smooth paths ${\boldsymbol {q}}:[a,b]\to X$ for which ${\boldsymbol {q}}(a)={\boldsymbol {x}}_{a}$ and ${\boldsymbol {q}}(b)={\boldsymbol {x}}_{b}$ .

The action functional $S\colon {\cal {P}}(a,b,{\boldsymbol {x}}_{a},{\boldsymbol {x}}_{b})\to \mathbb {R}$ is defined via $S[{\boldsymbol {q}}]=\int _{a}^{b}L(t,{\boldsymbol {q}}(t),{\dot {\boldsymbol {q}}}(t))\,dt.$

A path ${\boldsymbol {q}}\in {\cal {P}}(a,b,{\boldsymbol {x}}_{a},{\boldsymbol {x}}_{b})$ is a stationary point of S if and only if

${\frac {\partial L}{\partial q^{i}}}(t,{\boldsymbol {q}}(t),{\dot {\boldsymbol {q}}}(t))-{\frac {\mathrm {d} }{\mathrm {d} t}}{\frac {\partial L}{\partial {\dot {q}}^{i}}}(t,{\boldsymbol {q}}(t),{\dot {\boldsymbol {q}}}(t))=0,\quad i=1,\dots ,n.$

When we say stationary point, we mean a stationary point of S with respect to any small perturbation in ${\boldsymbol {q}}$ . See proofs below for more rigorous detail.

Derivation of the one-dimensional Euler–Lagrange equation

The derivation of the one-dimensional Euler–Lagrange equation is one of the classic proofs in mathematics. It relies on the fundamental lemma of calculus of variations.

We wish to find a function f which satisfies the boundary conditions $f(a)=A$ , $f(b)=B$ , and which extremizes the functional $J[f]=\int _{a}^{b}L(x,f(x),f'(x))\,\mathrm {d} x\ .$

We assume that L is twice continuously differentiable. A weaker assumption can be used, but the proof becomes more difficult.

If f extremizes the functional subject to the boundary conditions, then any slight perturbation of f that preserves the boundary values must either increase J (if f is a minimizer) or decrease J (if f is a maximizer).

Let $f+\varepsilon \eta$ be the result of such a perturbation $\varepsilon \eta$ of f , where $\varepsilon$ is small and $\eta$ is a differentiable function satisfying $\eta (a)=\eta (b)=0$ . Then define $\Phi (\varepsilon )=J[f+\varepsilon \eta ]=\int _{a}^{b}L(x,f(x)+\varepsilon \eta (x),f'(x)+\varepsilon \eta '(x))\,\mathrm {d} x\ .$

We now wish to calculate the total derivative of $\Phi$ with respect to *ε*. ${\begin{aligned}{\frac {\mathrm {d} \Phi }{\mathrm {d} \varepsilon }}&={\frac {\mathrm {d} }{\mathrm {d} \varepsilon }}\int _{a}^{b}L(x,f(x)+\varepsilon \eta (x),f'(x)+\varepsilon \eta '(x))\,\mathrm {d} x\\&=\int _{a}^{b}{\frac {\mathrm {d} }{\mathrm {d} \varepsilon }}L(x,f(x)+\varepsilon \eta (x),f'(x)+\varepsilon \eta '(x))\,\mathrm {d} x\\&=\int _{a}^{b}\left[\eta (x){\frac {\partial L}{\partial {f}}}(x,f(x)+\varepsilon \eta (x),f'(x)+\varepsilon \eta '(x))+\eta '(x){\frac {\partial L}{\partial f'}}(x,f(x)+\varepsilon \eta (x),f'(x)+\varepsilon \eta '(x))\right]\mathrm {d} x\ .\end{aligned}}$

The third line follows from the fact that x does not depend on $\varepsilon$ , i.e. ${\frac {\mathrm {d} x}{\mathrm {d} \varepsilon }}=0$ .

When $\varepsilon =0$ , $\Phi$ has an extremum value, so that $\left.{\frac {\mathrm {d} \Phi }{\mathrm {d} \varepsilon }}\right|_{\varepsilon =0}=\int _{a}^{b}\left[\eta (x){\frac {\partial L}{\partial f}}(x,f(x),f'(x))+\eta '(x){\frac {\partial L}{\partial f'}}(x,f(x),f'(x))\,\right]\,\mathrm {d} x=0\ .$

The next step is to use integration by parts on the second term of the integrand, yielding $\int _{a}^{b}\left[{\frac {\partial L}{\partial f}}(x,f(x),f'(x))-{\frac {\mathrm {d} }{\mathrm {d} x}}{\frac {\partial L}{\partial f'}}(x,f(x),f'(x))\right]\eta (x)\,\mathrm {d} x+\left[\eta (x){\frac {\partial L}{\partial f'}}(x,f(x),f'(x))\right]_{a}^{b}=0\ .$

Using the boundary conditions $\eta (a)=\eta (b)=0$ , $\int _{a}^{b}\left[{\frac {\partial L}{\partial f}}(x,f(x),f'(x))-{\frac {\mathrm {d} }{\mathrm {d} x}}{\frac {\partial L}{\partial f'}}(x,f(x),f'(x))\right]\eta (x)\,\mathrm {d} x=0\,.$

Applying the fundamental lemma of calculus of variations now yields the Euler–Lagrange equation ${\frac {\partial L}{\partial f}}(x,f(x),f'(x))-{\frac {\mathrm {d} }{\mathrm {d} x}}{\frac {\partial L}{\partial f'}}(x,f(x),f'(x))=0\,.$

Alternative derivation of the one-dimensional Euler–Lagrange equation

Given a functional $J=\int _{a}^{b}L(t,y(t),y'(t))\,\mathrm {d} t$ on $C^{1}([a,b])$ with the boundary conditions $y(a)=A$ and $y(b)=B$ , we proceed by approximating the extremal curve by a polygonal line with n segments and passing to the limit as the number of segments grows arbitrarily large.

Divide the interval $[a,b]$ into n equal segments with endpoints $t_{0}=a,t_{1},t_{2},\ldots ,t_{n}=b$ and let $\Delta t=t_{k}-t_{k-1}$ . Rather than a smooth function $y(t)$ we consider the polygonal line with vertices $(t_{0},y_{0}),\ldots ,(t_{n},y_{n})$ , where $y_{0}=A$ and $y_{n}=B$ . Accordingly, our functional becomes a real function of $n-1$ variables given by $J(y_{1},\ldots ,y_{n-1})\approx \sum _{k=0}^{n-1}L\left(t_{k},y_{k},{\frac {y_{k+1}-y_{k}}{\Delta t}}\right)\Delta t.$

Extremals of this new functional defined on the discrete points $t_{0},\ldots ,t_{n}$ correspond to points where ${\frac {\partial J(y_{1},\ldots ,y_{n})}{\partial y_{m}}}=0.$

Note that change of $y_{m}$ affects L not only at m but also at m-1 for the derivative of the 3rd argument. $L({\text{3rd argument}})\left({\frac {y_{m+1}-(y_{m}+\Delta y_{m})}{\Delta t}}\right)=L\left({\frac {y_{m+1}-y_{m}}{\Delta t}}\right)-{\frac {\partial L}{\partial y'}}{\frac {\Delta y_{m}}{\Delta t}}$ $L\left({\frac {(y_{m}+\Delta y_{m})-y_{m-1}}{\Delta t}}\right)=L\left({\frac {y_{m}-y_{m-1}}{\Delta t}}\right)+{\frac {\partial L}{\partial y'}}{\frac {\Delta y_{m}}{\Delta t}}$

Evaluating the partial derivative gives ${\frac {\partial J}{\partial y_{m}}}=L_{y}\left(t_{m},y_{m},{\frac {y_{m+1}-y_{m}}{\Delta t}}\right)\Delta t+L_{y'}\left(t_{m-1},y_{m-1},{\frac {y_{m}-y_{m-1}}{\Delta t}}\right)-L_{y'}\left(t_{m},y_{m},{\frac {y_{m+1}-y_{m}}{\Delta t}}\right).$

Dividing the above equation by $\Delta t$ gives ${\frac {\partial J}{\partial y_{m}\Delta t}}=L_{y}\left(t_{m},y_{m},{\frac {y_{m+1}-y_{m}}{\Delta t}}\right)-{\frac {1}{\Delta t}}\left[L_{y'}\left(t_{m},y_{m},{\frac {y_{m+1}-y_{m}}{\Delta t}}\right)-L_{y'}\left(t_{m-1},y_{m-1},{\frac {y_{m}-y_{m-1}}{\Delta t}}\right)\right],$ and taking the limit as $\Delta t\to 0$ of the right-hand side of this expression yields $L_{y}-{\frac {\mathrm {d} }{\mathrm {d} t}}L_{y'}=0.$

The left hand side of the previous equation is the functional derivative $\delta J/\delta y$ of the functional J . A necessary condition for a differentiable functional to have an extremum on some function is that its functional derivative at that function vanishes, which is granted by the last equation.

## Example

A standard example is finding the real-valued function *y*(*x*) on the interval [*a*, *b*], such that *y*(*a*) = *c* and *y*(*b*) = *d*, for which the path length along the curve traced by *y* is as short as possible.

${\text{s}}=\int _{a}^{b}{\sqrt {\mathrm {d} x^{2}+\mathrm {d} y^{2}}}=\int _{a}^{b}{\sqrt {1+y'^{2}}}\,\mathrm {d} x,$

the integrand function being ${\textstyle L(x,y,y')={\sqrt {1+y'^{2}}}}$ .

The partial derivatives of *L* are:

${\frac {\partial L(x,y,y')}{\partial y'}}={\frac {y'}{\sqrt {1+y'^{2}}}}\quad {\text{and}}\quad {\frac {\partial L(x,y,y')}{\partial y}}=0.$

By substituting these into the Euler–Lagrange equation, we obtain

${\begin{aligned}{\frac {\mathrm {d} }{\mathrm {d} x}}{\frac {y'(x)}{\sqrt {1+(y'(x))^{2}}}}&=0\\{\frac {y'(x)}{\sqrt {1+(y'(x))^{2}}}}&=C={\text{constant}}\\\Rightarrow y'(x)&={\frac {C}{\sqrt {1-C^{2}}}}=:A\\\Rightarrow y(x)&=Ax+B\end{aligned}}$

that is, the function must have a constant first derivative, and thus its graph is a straight line.

## Canonical momenta and constants of motion

The **conjugate momentum** *pk* for a generalized coordinate *qk* is defined by the equation $p_{k}\ {\overset {\mathrm {def} }{=}}\ {\frac {\partial L}{\partial {\dot {q}}_{k}}}.$

An important special case of the Euler–Lagrange equation occurs when *L* does not contain a generalized coordinate *qk* explicitly, ${\frac {\partial L}{\partial q_{k}}}=0\quad \Rightarrow \quad {\frac {d}{dt}}{\frac {\partial L}{\partial {\dot {q}}_{k}}}=0\quad \Rightarrow \quad {\frac {dp_{k}}{dt}}=0\,,$ that is, the conjugate momentum is a *constant of the motion*.

In such cases, the coordinate *qk* is called a **cyclic coordinate**. For example, if we use polar coordinates t, r, θ to describe the planar motion of a particle, and if *L* does not depend on θ, the conjugate momentum is the conserved angular momentum.

## Generalizations

### Single function of single variable with higher derivatives

The stationary values of the functional

$I[f]=\int _{x_{0}}^{x_{1}}{\mathcal {L}}(x,f,f',f'',\dots ,f^{(k)})~\mathrm {d} x~;~~f':={\cfrac {\mathrm {d} f}{\mathrm {d} x}},~f'':={\cfrac {\mathrm {d} ^{2}f}{\mathrm {d} x^{2}}},~f^{(k)}:={\cfrac {\mathrm {d} ^{k}f}{\mathrm {d} x^{k}}}$

can be obtained from the Euler–Lagrange equation

${\cfrac {\partial {\mathcal {L}}}{\partial f}}-{\cfrac {\mathrm {d} }{\mathrm {d} x}}\left({\cfrac {\partial {\mathcal {L}}}{\partial f'}}\right)+{\cfrac {\mathrm {d} ^{2}}{\mathrm {d} x^{2}}}\left({\cfrac {\partial {\mathcal {L}}}{\partial f''}}\right)-\dots +(-1)^{k}{\cfrac {\mathrm {d} ^{k}}{\mathrm {d} x^{k}}}\left({\cfrac {\partial {\mathcal {L}}}{\partial f^{(k)}}}\right)=0$

under fixed boundary conditions for the function itself as well as for the first $k-1$ derivatives (i.e. for all $f^{(i)},i\in \{0,...,k-1\}$ ). The endpoint values of the highest derivative $f^{(k)}$ remain flexible.

### Several functions of single variable with single derivative

If the problem involves finding several functions ( $f_{1},f_{2},\dots ,f_{m}$ ) of a single independent variable ( x ) that define an extremum of the functional

$I[f_{1},f_{2},\dots ,f_{m}]=\int _{x_{0}}^{x_{1}}{\mathcal {L}}(x,f_{1},f_{2},\dots ,f_{m},f_{1}',f_{2}',\dots ,f_{m}')~\mathrm {d} x~;~~f_{i}':={\cfrac {\mathrm {d} f_{i}}{\mathrm {d} x}}$

then the corresponding Euler–Lagrange equations are

${\begin{aligned}{\frac {\partial {\mathcal {L}}}{\partial f_{i}}}-{\frac {\mathrm {d} }{\mathrm {d} x}}\left({\frac {\partial {\mathcal {L}}}{\partial f_{i}'}}\right)=0;\quad i=1,2,...,m\end{aligned}}$

### Single function of several variables with single derivative

A multi-dimensional generalization comes from considering a function on n variables. If $\Omega$ is some surface, then

$I[f]=\int _{\Omega }{\mathcal {L}}(x_{1},\dots ,x_{n},f,f_{1},\dots ,f_{n})\,\mathrm {d} \mathbf {x} \,\!~;~~f_{j}:={\cfrac {\partial f}{\partial x_{j}}}$

is extremized only if *f* satisfies the partial differential equation

${\frac {\partial {\mathcal {L}}}{\partial f}}-\sum _{j=1}^{n}{\frac {\partial }{\partial x_{j}}}\left({\frac {\partial {\mathcal {L}}}{\partial f_{j}}}\right)=0.$

When *n* = 2 and functional ${\mathcal {I}}$ is the energy functional, this leads to the soap-film minimal surface problem.

### Several functions of several variables with single derivative

If there are several unknown functions to be determined and several variables such that

$I[f_{1},f_{2},\dots ,f_{m}]=\int _{\Omega }{\mathcal {L}}(x_{1},\dots ,x_{n},f_{1},\dots ,f_{m},f_{1,1},\dots ,f_{1,n},\dots ,f_{m,1},\dots ,f_{m,n})\,\mathrm {d} \mathbf {x} \,\!~;~~f_{i,j}:={\cfrac {\partial f_{i}}{\partial x_{j}}}$

the system of Euler–Lagrange equations is

${\begin{aligned}{\frac {\partial {\mathcal {L}}}{\partial f_{1}}}-\sum _{j=1}^{n}{\frac {\partial }{\partial x_{j}}}\left({\frac {\partial {\mathcal {L}}}{\partial f_{1,j}}}\right)&=0_{1}\\{\frac {\partial {\mathcal {L}}}{\partial f_{2}}}-\sum _{j=1}^{n}{\frac {\partial }{\partial x_{j}}}\left({\frac {\partial {\mathcal {L}}}{\partial f_{2,j}}}\right)&=0_{2}\\\vdots \qquad \vdots \qquad &\quad \vdots \\{\frac {\partial {\mathcal {L}}}{\partial f_{m}}}-\sum _{j=1}^{n}{\frac {\partial }{\partial x_{j}}}\left({\frac {\partial {\mathcal {L}}}{\partial f_{m,j}}}\right)&=0_{m}.\end{aligned}}$

### Single function of two variables with higher derivatives

If there is a single unknown function *f* to be determined that is dependent on two variables *x*1 and *x*2 and if the functional depends on higher derivatives of *f* up to *n*-th order such that

${\begin{aligned}I[f]&=\int _{\Omega }{\mathcal {L}}(x_{1},x_{2},f,f_{1},f_{2},f_{11},f_{12},f_{22},\dots ,f_{22\dots 2})\,\mathrm {d} \mathbf {x} \\&\qquad \quad f_{i}:={\cfrac {\partial f}{\partial x_{i}}}\;,\quad f_{ij}:={\cfrac {\partial ^{2}f}{\partial x_{i}\partial x_{j}}}\;,\;\;\dots \end{aligned}}$

then the Euler–Lagrange equation is

${\begin{aligned}{\frac {\partial {\mathcal {L}}}{\partial f}}&-{\frac {\partial }{\partial x_{1}}}\left({\frac {\partial {\mathcal {L}}}{\partial f_{1}}}\right)-{\frac {\partial }{\partial x_{2}}}\left({\frac {\partial {\mathcal {L}}}{\partial f_{2}}}\right)+{\frac {\partial ^{2}}{\partial x_{1}^{2}}}\left({\frac {\partial {\mathcal {L}}}{\partial f_{11}}}\right)+{\frac {\partial ^{2}}{\partial x_{1}\partial x_{2}}}\left({\frac {\partial {\mathcal {L}}}{\partial f_{12}}}\right)+{\frac {\partial ^{2}}{\partial x_{2}^{2}}}\left({\frac {\partial {\mathcal {L}}}{\partial f_{22}}}\right)\\&-\dots +(-1)^{n}{\frac {\partial ^{n}}{\partial x_{2}^{n}}}\left({\frac {\partial {\mathcal {L}}}{\partial f_{22\dots 2}}}\right)=0\end{aligned}}$

which can be represented shortly as:

${\frac {\partial {\mathcal {L}}}{\partial f}}+\sum _{j=1}^{n}\sum _{\mu _{1}\leq \ldots \leq \mu _{j}}(-1)^{j}{\frac {\partial ^{j}}{\partial x_{\mu _{1}}\dots \partial x_{\mu _{j}}}}\left({\frac {\partial {\mathcal {L}}}{\partial f_{\mu _{1}\dots \mu _{j}}}}\right)=0$

wherein $\mu _{1}\dots \mu _{j}$ are indices that span the number of variables, that is, here they go from 1 to 2. Here summation over the $\mu _{1}\dots \mu _{j}$ indices is only over $\mu _{1}\leq \mu _{2}\leq \ldots \leq \mu _{j}$ in order to avoid counting the same partial derivative multiple times, for example $f_{12}=f_{21}$ appears only once in the previous equation.

### Several functions of several variables with higher derivatives

If there are *p* unknown functions *f*i to be determined that are dependent on *m* variables *x*1 ... *x*m and if the functional depends on higher derivatives of the *f*i up to *n*-th order such that

${\begin{aligned}I[f_{1},\ldots ,f_{p}]&=\int _{\Omega }{\mathcal {L}}(x_{1},\ldots ,x_{m};f_{1},\ldots ,f_{p};f_{1,1},\ldots ,f_{p,m};f_{1,11},\ldots ,f_{p,mm};\ldots ;f_{p,1\ldots 1},\ldots ,f_{p,m\ldots m})\,\mathrm {d} \mathbf {x} \\&\qquad \quad f_{i,\mu }:={\cfrac {\partial f_{i}}{\partial x_{\mu }}}\;,\quad f_{i,\mu _{1}\mu _{2}}:={\cfrac {\partial ^{2}f_{i}}{\partial x_{\mu _{1}}\partial x_{\mu _{2}}}}\;,\;\;\dots \end{aligned}}$

where $\mu _{1}\dots \mu _{j}$ are indices that span the number of variables, that is they go from 1 to m. Then the Euler–Lagrange equation is

${\frac {\partial {\mathcal {L}}}{\partial f_{i}}}+\sum _{j=1}^{n}\sum _{\mu _{1}\leq \ldots \leq \mu _{j}}(-1)^{j}{\frac {\partial ^{j}}{\partial x_{\mu _{1}}\dots \partial x_{\mu _{j}}}}\left({\frac {\partial {\mathcal {L}}}{\partial f_{i,\mu _{1}\dots \mu _{j}}}}\right)=0$

where the summation over the $\mu _{1}\dots \mu _{j}$ is avoiding counting the same derivative $f_{i,\mu _{1}\mu _{2}}=f_{i,\mu _{2}\mu _{1}}$ several times, just as in the previous subsection. This can be expressed more compactly as

$\sum _{j=0}^{n}\sum _{\mu _{1}\leq \ldots \leq \mu _{j}}(-1)^{j}\partial _{\mu _{1}\ldots \mu _{j}}^{j}\left({\frac {\partial {\mathcal {L}}}{\partial f_{i,\mu _{1}\dots \mu _{j}}}}\right)=0$

### Field theories

## Generalization to manifolds

Let M be a smooth manifold, and let $C^{\infty }([a,b])$ denote the space of smooth functions $f\colon [a,b]\to M$ . Then, for functionals $S\colon C^{\infty }([a,b])\to \mathbb {R}$ of the form

$S[f]=\int _{a}^{b}(L\circ {\dot {f}})(t)\,\mathrm {d} t$

where $L\colon TM\to \mathbb {R}$ is the Lagrangian, the statement $\mathrm {d} S_{f}=0$ is equivalent to the statement that, for all $t\in [a,b]$ , each coordinate frame trivialization $(x^{i},X^{i})$ of a neighborhood of ${\dot {f}}(t)$ yields the following $\dim M$ equations:

$\forall i:{\frac {\mathrm {d} }{\mathrm {d} t}}{\frac {\partial L}{\partial X^{i}}}{\bigg |}_{{\dot {f}}(t)}={\frac {\partial L}{\partial x^{i}}}{\bigg |}_{{\dot {f}}(t)}.$

Euler–Lagrange equations can also be written in a coordinate-free form as

${\mathcal {L}}_{\Delta }\theta _{L}=dL$

where $\theta _{L}$ is the canonical momenta 1-form corresponding to the Lagrangian L . The vector field generating time translations is denoted by $\Delta$ and the Lie derivative is denoted by ${\mathcal {L}}$ . One can use local charts $(q^{\alpha },{\dot {q}}^{\alpha })$ in which $\theta _{L}={\frac {\partial L}{\partial {\dot {q}}^{\alpha }}}dq^{\alpha }$ and $\Delta :={\frac {d}{dt}}={\dot {q}}^{\alpha }{\frac {\partial }{\partial q^{\alpha }}}+{\ddot {q}}^{\alpha }{\frac {\partial }{\partial {\dot {q}}^{\alpha }}}$ and use coordinate expressions for the Lie derivative to see equivalence with coordinate expressions of the Euler Lagrange equation. The coordinate free form is particularly suitable for geometrical interpretation of the Euler Lagrange equations.
