---
title: "Ordinary differential equation"
source: https://en.wikipedia.org/wiki/Ordinary_differential_equation
domain: flow-matching
license: CC-BY-SA-4.0
tags: flow matching, continuous normalizing flow, optimal transport, generative ode
fetched: 2026-07-02
---

# Ordinary differential equation

In mathematics, an **ordinary differential equation** (**ODE**) is a differential equation (DE) dependent on only a single independent variable. As with any other DE, its unknown(s) consists of one (or more) function(s) and involves the derivatives of those functions. The term "ordinary" is used in contrast with *partial* differential equations (PDEs) which may be with respect to *more than* one independent variable, and, less commonly, in contrast with *stochastic* differential equations (SDEs) where the modeled process is random.

## Differential equations

A linear differential equation is a differential equation that is defined by a linear polynomial in the unknown function and its derivatives, that is an equation of the form

$a_{0}(x)y+a_{1}(x)y'+a_{2}(x)y''+\cdots +a_{n}(x)y^{(n)}+b(x)=0,$

where $a_{0}(x),\ldots ,a_{n}(x)$ and $b(x)$ are arbitrary differentiable functions that do not need to be linear, and $y',\ldots ,y^{(n)}$ are the successive derivatives of the unknown function y of the variable x .

Among ordinary differential equations, linear differential equations play a prominent role for several reasons. Most elementary and special functions that are encountered in physics and applied mathematics are solutions of linear differential equations (see Holonomic function). When physical phenomena are modeled with non-linear equations, they are generally approximated by linear differential equations for an easier solution. The few non-linear ODEs that can be solved explicitly are generally solved by transforming the equation into an equivalent linear ODE (see, for example Riccati equation).

Some ODEs can be solved explicitly in terms of known functions and integrals. When that is not possible, the equation for computing the Taylor series of the solutions may be useful. For applied problems, numerical methods for ordinary differential equations can supply an approximation of the solution.

## Background

Ordinary differential equations (ODEs) arise in many contexts of mathematics and social and natural sciences. Mathematical descriptions of change use differentials and derivatives. Various differentials, derivatives, and functions become related via equations, such that a differential equation is a result that describes dynamically changing phenomena, evolution, and variation. Often, quantities are defined as the rate of change of other quantities (for example, derivatives of displacement with respect to time), or gradients of quantities, which is how they enter differential equations.

Specific mathematical fields include geometry and analytical mechanics. Scientific fields include much of physics and astronomy (celestial mechanics), meteorology (weather modeling), chemistry (reaction rates), biology (infectious diseases, genetic variation), ecology and population modeling (population competition), economics (stock trends, interest rates and the market equilibrium price changes).

Many mathematicians have studied differential equations and contributed to the field, including Newton, Leibniz, the Bernoulli family, Riccati, Clairaut, d'Alembert, and Euler.

A simple example is Newton's second law of motion—the relationship between the displacement x and the time t of an object under the force F , is given by the differential equation

$m{\frac {\mathrm {d} ^{2}x(t)}{\mathrm {d} t^{2}}}=F(x(t))\,$

which constrains the motion of a particle of constant mass m . In general, F is a function of the position $x(t)$ of the particle at time t . The unknown function $x(t)$ appears on both sides of the differential equation, and is indicated in the notation $F(x(t))$ .

## Definitions

In what follows, y is a dependent variable representing an unknown function $y=f(x)$ of the independent variable x . The notation for differentiation varies depending upon the author and upon which notation is most useful for the task at hand. In this context, the Leibniz's notation ${\frac {dy}{dx}},{\frac {d^{2}y}{dx^{2}}},\ldots ,{\frac {d^{n}y}{dx^{n}}}$ is more useful for differentiation and integration, whereas Lagrange's notation $y',y'',\ldots ,y^{(n)}$ is more useful for representing higher-order derivatives compactly, and Newton's notation $({\dot {y}},{\ddot {y}},{\overset {...}{y}})$ is often used in physics for representing derivatives of low order with respect to time.

### General definition

Given F , a function of x , y , and derivatives of y . Then an equation of the form

$F\left(x,y,y',\ldots ,y^{(n-1)}\right)=y^{(n)}$

is called an *explicit ordinary differential equation of order n*.

More generally, an *implicit* ordinary differential equation of order n takes the form:

$F\left(x,y,y',y'',\ \ldots ,\ y^{(n)}\right)=0$

There are further classifications:

***Autonomous***

A differential equation is

autonomous

if it does not depend on the variable

x

.

***Linear***

A differential equation is

linear

if

F

can be written as a

linear combination

of the derivatives of

y

; that is, it can be rewritten as

$y^{(n)}=\sum _{i=0}^{n-1}a_{i}(x)y^{(i)}+r(x)$

where

$a_{i}(x)$

and

$r(x)$

are continuous functions of

x

.

The function

$r(x)$

is called the

source term

, leading to further classification.

***Non-linear***

A differential equation that is not linear.

### System of ODEs

A number of coupled differential equations form a system of equations. If $\mathbf {y}$ is a vector whose elements are functions; $\mathbf {y} (x)=[y_{1}(x),y_{2}(x),\ldots ,y_{m}(x)]$ , and $\mathbf {F}$ is a vector-valued function of $\mathbf {y}$ and its derivatives, then

$\mathbf {y} ^{(n)}=\mathbf {F} \left(x,\mathbf {y} ,\mathbf {y} ',\mathbf {y} '',\ldots ,\mathbf {y} ^{(n-1)}\right)$

is an *explicit system of ordinary differential equations* of *order* n and *dimension* m . In column vector form:

${\begin{pmatrix}y_{1}^{(n)}\\y_{2}^{(n)}\\\vdots \\y_{m}^{(n)}\end{pmatrix}}={\begin{pmatrix}f_{1}\left(x,\mathbf {y} ,\mathbf {y} ',\mathbf {y} '',\ldots ,\mathbf {y} ^{(n-1)}\right)\\f_{2}\left(x,\mathbf {y} ,\mathbf {y} ',\mathbf {y} '',\ldots ,\mathbf {y} ^{(n-1)}\right)\\\vdots \\f_{m}\left(x,\mathbf {y} ,\mathbf {y} ',\mathbf {y} '',\ldots ,\mathbf {y} ^{(n-1)}\right)\end{pmatrix}}$

These are not necessarily linear. The *implicit* analogue is:

$\mathbf {F} \left(x,\mathbf {y} ,\mathbf {y} ',\mathbf {y} '',\ldots ,\mathbf {y} ^{(n)}\right)={\boldsymbol {0}}$

where ${\boldsymbol {0}}=(0,0,\ldots ,0)$ is the zero vector. In matrix form

${\begin{pmatrix}f_{1}(x,\mathbf {y} ,\mathbf {y} ',\mathbf {y} '',\ldots ,\mathbf {y} ^{(n)})\\f_{2}(x,\mathbf {y} ,\mathbf {y} ',\mathbf {y} '',\ldots ,\mathbf {y} ^{(n)})\\\vdots \\f_{m}(x,\mathbf {y} ,\mathbf {y} ',\mathbf {y} '',\ldots ,\mathbf {y} ^{(n)})\end{pmatrix}}={\begin{pmatrix}0\\0\\\vdots \\0\end{pmatrix}}$

For a system of the form $\mathbf {F} \left(x,\mathbf {y} ,\mathbf {y} '\right)={\boldsymbol {0}}$ , some sources also require that the Jacobian matrix ${\frac {\partial \mathbf {F} (x,\mathbf {u} ,\mathbf {v} )}{\partial \mathbf {v} }}$ be non-singular in order to call this an implicit ODE [system]; an implicit ODE system satisfying this Jacobian non-singularity condition can be transformed into an explicit ODE system. In the same sources, implicit ODE systems with a singular Jacobian are termed differential algebraic equations (DAEs). This distinction is not merely one of terminology; DAEs have fundamentally different characteristics and are generally more involved to solve than (nonsingular) ODE systems. Presumably for additional derivatives, the Hessian matrix and so forth are also assumed non-singular according to this scheme, although note that any ODE of order greater than one can be (and usually is) rewritten as system of ODEs of first order, which makes the Jacobian singularity criterion sufficient for this taxonomy to be comprehensive at all orders.

The behavior of a system of ODEs can be visualized through the use of a phase portrait.

### Solutions

Given a differential equation

$F\left(x,y,y',\ldots ,y^{(n)}\right)=0$

a function $u:I\subset \mathbb {R} \to \mathbb {R}$ , where I is an interval, is called a *solution* or integral curve for F , if u is n -times differentiable on I , and

$F(x,u,u',\ \ldots ,\ u^{(n)})=0\quad x\in I.$

Given two solutions $u:J\subset \mathbb {R} \to \mathbb {R}$ and $v:I\subset \mathbb {R} \to \mathbb {R}$ , u is called an *extension* of v if $I\subset J$ and

$u(x)=v(x)\quad x\in I.\,$

A solution that has no extension is called a *maximal solution*. A solution defined on all of $\mathbb {R}$ is called a *global solution*.

A *general solution* of an n th-order equation is a solution containing n arbitrary independent constants of integration. A *particular solution* is derived from the general solution by setting the constants to particular values, often chosen to fulfill set 'initial conditions or boundary conditions'. A singular solution is a solution that cannot be obtained by assigning definite values to the arbitrary constants in the general solution.

In the context of linear ODE, the terminology *particular solution* can also refer to any solution of the ODE (not necessarily satisfying the initial conditions), which is then added to the *homogeneous* solution (a general solution of the homogeneous ODE), which then forms a general solution of the original ODE. This is the terminology used in the guessing method section in this article, and is frequently used when discussing the method of undetermined coefficients and variation of parameters.

### Solutions of finite duration

For non-linear autonomous ODEs it is possible under some conditions to develop solutions of finite duration, meaning here that from its own dynamics, the system will reach the value zero at an ending time and stays there in zero forever after. These finite-duration solutions can't be analytical functions on the whole real line, and because they will be non-Lipschitz functions at their ending time, they are not included in the uniqueness theorem of solutions of Lipschitz differential equations.

As example, the equation:

$y'=-{\text{sgn}}(y){\sqrt {|y|}},\,\,y(0)=1$

Admits the finite duration solution:

$y(x)={\frac {1}{4}}\left(1-{\frac {x}{2}}+\left|1-{\frac {x}{2}}\right|\right)^{2}$

## Theories

### Singular solutions

The theory of singular solutions of ordinary and partial differential equations was a subject of research from the time of Leibniz, but only since the middle of the nineteenth century has it received special attention. A valuable but little-known work on the subject is that of Houtain (1854). Darboux (from 1873) was a leader in the theory, and in the geometric interpretation of these solutions he opened a field worked by various writers, notably Casorati and Cayley. To the latter is due (1872) the theory of singular solutions of differential equations of the first order as accepted circa 1900.

### Reduction to quadratures

The primitive attempt in dealing with differential equations had in view a reduction to quadratures, that is, expressing the solutions in terms of known function and their integrals. This is possible for linear equations with constant coefficients, it appeared in the 19th century that this is generally impossible in other cases. Hence, analysts began the study (for their own) of functions that are solutions of differential equations, thus opening a new and fertile field. Cauchy was the first to appreciate the importance of this view. Thereafter, the real question was no longer whether a solution is possible by quadratures, but whether a given differential equation suffices for the definition of a function, and, if so, what are the characteristic properties of such functions.

### Fuchsian theory

Two memoirs by Fuchs inspired a novel approach, subsequently elaborated by Thomé and Frobenius. (WHO?)Collet was a prominent contributor beginning in 1869. His method for integrating a non-linear system was communicated to Bertrand in 1868. Clebsch (1873) attacked the theory along lines parallel to those in his theory of Abelian integrals. As the latter can be classified according to the properties of the fundamental curve that remains unchanged under a rational transformation, Clebsch proposed to classify the transcendent functions defined by differential equations according to the invariant properties of the corresponding surfaces $f=0$ under rational one-to-one transformations.

### Lie's theory

From 1870, Sophus Lie's work put the theory of differential equations on a better foundation. He showed that the integration theories of the older mathematicians can, using Lie groups, be referred to a common source, and that ordinary differential equations that admit the same infinitesimal transformations present comparable integration difficulties. He also emphasized the subject of transformations of contact.

Lie's group theory of differential equations has been certified, namely: (1) that it unifies the many ad hoc methods known for solving differential equations, and (2) that it provides powerful new ways to find solutions. The theory has applications to both ordinary and partial differential equations.

A general solution approach uses the symmetry property of differential equations, the continuous infinitesimal transformations of solutions to solutions (Lie theory). Continuous group theory, Lie algebras, and differential geometry are used to understand the structure of linear and non-linear (partial) differential equations for generating integrable equations, to find its Lax pairs, recursion operators, Bäcklund transform, and finally finding exact analytic solutions to DE.

Symmetry methods have been applied to differential equations that arise in mathematics, physics, engineering, and other disciplines.

### Sturm–Liouville theory

Sturm–Liouville theory is a theory of a special type of second-order linear ordinary differential equation. Their solutions are based on eigenvalues and corresponding eigenfunctions of linear operators defined via second-order homogeneous linear equations. The problems are identified as Sturm–Liouville problems (SLP) and are named after J. C. F. Sturm and J. Liouville, who studied them in the mid-1800s. SLPs have an infinite number of eigenvalues, and the corresponding eigenfunctions form a complete, orthogonal set, which makes orthogonal expansions possible. This is a key idea in applied mathematics, physics, and engineering. SLPs are also useful in the analysis of certain partial differential equations.

## Existence and uniqueness of solutions

There are several theorems that establish existence and uniqueness of solutions to initial value problems involving ODEs both locally and globally. The two main theorems are

| Theorem | Assumption | Conclusion |
|---|---|---|
| Peano existence theorem | F continuous | local existence only |
| Picard–Lindelöf theorem | F Lipschitz continuous | local existence and uniqueness |

In their basic form both of these theorems only guarantee local results, though the latter can be extended to give a global result, for example, if the conditions of Grönwall's inequality are met.

Also, uniqueness theorems like the Lipschitz one above do not apply to DAE systems, which may have multiple solutions stemming from their (non-linear) algebraic part alone.

### Local existence and uniqueness theorem simplified

The theorem can be stated simply as follows. For the equation and initial value problem: $y'=F(x,y)\,,\quad y_{0}=y(x_{0})$ if F and $\partial F/\partial y$ are continuous in a closed rectangle $R=[x_{0}-a,x_{0}+a]\times [y_{0}-b,y_{0}+b]$ in the $x-y$ plane, where a and b are real (symbolically: $a,b\in \mathbb {R}$ ) and $\times$ denotes the Cartesian product, square brackets denote closed intervals, then there is an interval $I=[x_{0}-h,x_{0}+h]\subset [x_{0}-a,x_{0}+a]$ for some $h\in \mathbb {R}$ where *the* solution to the above equation and initial value problem can be found. That is, there is a solution and it is unique. Since there is no restriction on F to be linear, this applies to non-linear equations that take the form $F(x,y)$ , and it can also be applied to systems of equations.

### Global uniqueness and maximum domain of solution

When the hypotheses of the Picard–Lindelöf theorem are satisfied, then local existence and uniqueness can be extended to a global result. More precisely:

For each initial condition $(x_{0},y_{0})$ there exists a unique maximum (possibly infinite) open interval

$I_{\max }=(x_{-},x_{+}),x_{\pm }\in \mathbb {R} \cup \{\pm \infty \},x_{0}\in I_{\max }$

such that any solution that satisfies this initial condition is a restriction of the solution that satisfies this initial condition with domain $I_{\max }$ .

In the case that $x_{\pm }\neq \pm \infty$ , there are exactly two possibilities

- explosion in finite time: $\limsup _{x\to x_{\pm }}\|y(x)\|\to \infty$
- leaves domain of definition: $\lim _{x\to x_{\pm }}y(x)\ \in \partial {\bar {\Omega }}$

where $\Omega$ is the open set in which F is defined, and $\partial {\bar {\Omega }}$ is its boundary.

Note that the maximum domain of the solution

- is always an interval (to have uniqueness)
- may be smaller than $\mathbb {R}$
- may depend on the specific choice of $(x_{0},y_{0})$ .

**Example.**

$y'=y^{2}$

This means that $F(x,y)=y^{2}$ , which is $C^{1}$ and therefore locally Lipschitz continuous, satisfying the Picard–Lindelöf theorem.

Even in such a simple setting, the maximum domain of solution cannot be all $\mathbb {R}$ since the solution is

$y(x)={\frac {y_{0}}{(x_{0}-x)y_{0}+1}}$

which has maximum domain:

${\begin{cases}\mathbb {R} &y_{0}=0\\[4pt]\left(-\infty ,x_{0}+{\frac {1}{y_{0}}}\right)&y_{0}>0\\[4pt]\left(x_{0}+{\frac {1}{y_{0}}},+\infty \right)&y_{0}<0\end{cases}}$

This shows clearly that the maximum interval may depend on the initial conditions. The domain of y could be taken as being $\mathbb {R} \setminus (x_{0}+1/y_{0}),$ but this would lead to a domain that is not an interval, so that the side opposite to the initial condition would be disconnected from the initial condition, and therefore not uniquely determined by it.

The maximum domain is not $\mathbb {R}$ because

$\lim _{x\to x_{\pm }}\|y(x)\|\to \infty ,$

which is one of the two possible cases according to the above theorem.

## Reduction of order

Differential equations are usually easier to solve if the order of the equation can be reduced.

### Reduction to a first-order system

Any explicit differential equation of order n ,

$F\left(x,y,y',y'',\ \ldots ,\ y^{(n-1)}\right)=y^{(n)}$

can be written as a system of n first-order differential equations by defining a new family of unknown functions

$y_{i}=y^{(i-1)}.\!$

for $i=1,2,\ldots ,n$ . The n -dimensional system of first-order coupled differential equations is then

${\begin{array}{rcl}y_{1}'&=&y_{2}\\y_{2}'&=&y_{3}\\&\vdots &\\y_{n-1}'&=&y_{n}\\y_{n}'&=&F(x,y_{1},\ldots ,y_{n}).\end{array}}$

more compactly in vector notation:

$\mathbf {y} '=\mathbf {F} (x,\mathbf {y} )$

where

$\mathbf {y} =(y_{1},\ldots ,y_{n}),\quad \mathbf {F} (x,y_{1},\ldots ,y_{n})=(y_{2},\ldots ,y_{n},F(x,y_{1},\ldots ,y_{n})).$

## Summary of exact solutions

Some differential equations have solutions that can be written in an exact and closed form. Several important classes are given here.

In the table below, $P(x)$ , $Q(x)$ , $P(y)$ , $Q(y)$ , and $M(x,y)$ , $N(x,y)$ are any integrable functions of x , y ; b and c are real given constants; $C_{1},C_{2},\ldots$ are arbitrary constants (complex in general). The differential equations are in their equivalent and alternative forms that lead to the solution through integration.

In the integral solutions, $\lambda$ and $\varepsilon$ are dummy variables of integration (the continuum analogues of indices in summation), and the notation $\int ^{x}F(\lambda )\,d\lambda$ just means to integrate $F(\lambda )$ with respect to $\lambda$ , then *after* the integration substitute $\lambda =x$ , without adding constants (explicitly stated).

### Separable equations

| Differential equation | Solution method | General solution |
|---|---|---|
| First-order, separable in x and y (general case, see below for special cases) ${\begin{aligned}P_{1}(x)Q_{1}(y)+P_{2}(x)Q_{2}(y)\,{\frac {dy}{dx}}&=0\\P_{1}(x)Q_{1}(y)\,dx+P_{2}(x)Q_{2}(y)\,dy&=0\end{aligned}}$ | Separation of variables (divide by $P_{2}Q_{1}$ ). | $\int ^{x}{\frac {P_{1}(\lambda )}{P_{2}(\lambda )}}\,d\lambda +\int ^{y}{\frac {Q_{2}(\lambda )}{Q_{1}(\lambda )}}\,d\lambda =C$ |
| First-order, separable in x ${\begin{aligned}{\frac {dy}{dx}}&=F(x)\\dy&=F(x)\,dx\end{aligned}}$ | Direct integration. | $y=\int ^{x}F(\lambda )\,d\lambda +C$ |
| First-order, autonomous, separable in y ${\begin{aligned}{\frac {dy}{dx}}&=F(y)\\dy&=F(y)\,dx\end{aligned}}$ | Separation of variables (divide by F ). | $x=\int ^{y}{\frac {d\lambda }{F(\lambda )}}+C$ |
| First-order, separable in x and y ${\begin{aligned}P(y){\frac {dy}{dx}}+Q(x)&=0\\P(y)\,dy+Q(x)\,dx&=0\end{aligned}}$ | Integrate throughout. | $\int ^{y}P(\lambda )\,d\lambda +\int ^{x}Q(\lambda )\,d\lambda =C$ |

### General first-order equations

| Differential equation | Solution method | General solution |
|---|---|---|
| First-order, homogeneous ${\frac {dy}{dx}}=F\left({\frac {y}{x}}\right)$ | Set *y = ux*, then solve by separation of variables in *u* and *x*. | $\ln(Cx)=\int ^{y/x}{\frac {d\lambda }{F(\lambda )-\lambda }}$ |
| First-order, separable ${\begin{aligned}yM(xy)+xN(xy)\,{\frac {dy}{dx}}&=0\\yM(xy)\,dx+xN(xy)\,dy&=0\end{aligned}}$ | Separation of variables (divide by $xy$ ). | $\ln(Cx)=\int ^{xy}{\frac {N(\lambda )\,d\lambda }{\lambda [N(\lambda )-M(\lambda )]}}$ If $N=M$ , the solution is $xy=C$ . |
| Exact differential, first-order ${\begin{aligned}M(x,y){\frac {dy}{dx}}+N(x,y)&=0\\M(x,y)\,dy+N(x,y)\,dx&=0\end{aligned}}$ where ${\frac {\partial M}{\partial y}}={\frac {\partial N}{\partial x}}$ | Integrate throughout. | ${\begin{aligned}F(x,y)&=\int ^{x}M(\lambda ,y)\,d\lambda +\int ^{y}Y(\lambda )\,d\lambda \\&=\int ^{y}N(x,\lambda )\,d\lambda +\int ^{x}X(\lambda )\,d\lambda =C\end{aligned}}$ where $Y(y)=N(x,y)-{\frac {\partial }{\partial y}}\int ^{x}M(\lambda ,y)\,d\lambda$ and $X(x)=M(x,y)-{\frac {\partial }{\partial x}}\int ^{y}N(x,\lambda )\,d\lambda$ |
| Inexact differential, first-order ${\begin{aligned}M(x,y){\frac {dy}{dx}}+N(x,y)&=0\\M(x,y)\,dy+N(x,y)\,dx&=0\end{aligned}}$ where ${\frac {\partial M}{\partial y}}\neq {\frac {\partial N}{\partial x}}$ | Integration factor $\mu (x,y)$ satisfying ${\frac {\partial (\mu M)}{\partial y}}={\frac {\partial (\mu N)}{\partial x}}$ | If $\mu (x,y)$ can be found in a suitable way, then ${\begin{aligned}F(x,y)=&\int ^{x}\mu (\lambda ,y)M(\lambda ,y)\,d\lambda +\int ^{y}Y(\lambda )\,d\lambda \\=&\int ^{y}\mu (x,\lambda )N(x,\lambda )\,d\lambda +\int ^{x}X(\lambda )\,d\lambda =C\end{aligned}}$ where $Y(y)=N(x,y)-{\frac {\partial }{\partial y}}\int ^{x}\mu (\lambda ,y)M(\lambda ,y)\,d\lambda$ and $X(x)=M(x,y)-{\frac {\partial }{\partial x}}\int ^{y}\mu (x,\lambda )N(x,\lambda )\,d\lambda$ |

### General second-order equations

| Differential equation | Solution method | General solution |
|---|---|---|
| Second-order, autonomous ${\frac {d^{2}y}{dx^{2}}}=F(y)$ | Multiply both sides of equation by $2{\frac {dy}{dx}}$ , substitute $2{\frac {dy}{dx}}{\frac {d^{2}y}{dx^{2}}}={\frac {d}{dx}}\left({\frac {dy}{dx}}\right)^{2}=2{\frac {dy}{dx}}F(y)$ , then integrate twice. | $x=\pm \int ^{y}{\frac {d\lambda }{\sqrt {2\int ^{\lambda }F(\varepsilon )\,d\varepsilon +C_{1}}}}+C_{2}$ |

### Linear to the nth order equations

| Differential equation | Solution method | General solution |
|---|---|---|
| First-order, linear, inhomogeneous, function coefficients ${\frac {dy}{dx}}+P(x)y=Q(x)$ | Integrating factor: $e^{\int ^{x}P(\lambda )\,d\lambda }.$ | $y=e^{-\int ^{x}P(\lambda )\,d\lambda }\left[\int ^{x}e^{\int ^{\lambda }P(\varepsilon )\,d\varepsilon }Q(\lambda )\,d\lambda +C\right]$ |
| Second-order, linear, inhomogeneous, function coefficients ${\frac {d^{2}y}{dx^{2}}}+2p(x){\frac {dy}{dx}}+\left(p(x)^{2}+p'(x)\right)y=q(x)$ | Integrating factor: $e^{\int ^{x}P(\lambda )\,d\lambda }$ | $y=e^{-\int ^{x}P(\lambda )\,d\lambda }\left[\int ^{x}\left(\int ^{\xi }e^{\int ^{\lambda }P(\varepsilon )\,d\varepsilon }Q(\lambda )\,d\lambda \right)d\xi +C_{1}x+C_{2}\right]$ |
| Second-order, linear, inhomogeneous, constant coefficients ${\frac {d^{2}y}{dx^{2}}}+b{\frac {dy}{dx}}+cy=r(x)$ | Complementary function $y_{c}$ : assume $y_{c}(x)=e^{\alpha x}$ , substitute and solve polynomial in $\alpha$ , to find the linearly independent functions $e^{\alpha _{j}x}$ . Particular integral $y_{p}$ : in general the method of variation of parameters, though for very simple $r(x)$ inspection may work. | $y=y_{c}+y_{p}$ If $b^{2}>4c$ , then $y_{c}=C_{1}e^{-{\frac {x}{2}}\,\left(b+{\sqrt {b^{2}-4c}}\right)}+C_{2}e^{-{\frac {x}{2}}\,\left(b-{\sqrt {b^{2}-4c}}\right)}$ If $b^{2}=4c$ , then $y_{c}=(C_{1}x+C_{2})e^{-{\frac {bx}{2}}}$ If $b^{2}<4c$ , then $y_{c}=e^{-{\frac {bx}{2}}}\left[C_{1}\sin \left(x\,{\frac {\sqrt {4c-b^{2}}}{2}}\right)+C_{2}\cos \left(x\,{\frac {\sqrt {4c-b^{2}}}{2}}\right)\right]$ |
| n th-order, linear, inhomogeneous, constant coefficients $\sum _{j=0}^{n}b_{j}{\frac {d^{j}y}{dx^{j}}}=r(x)$ | Complementary function $y_{c}$ : assume $y_{c}(x)=e^{\alpha x}$ , substitute and solve polynomial in $\alpha$ , to find the linearly independent functions $e^{\alpha _{j}x}$ . Particular integral $y_{p}$ : in general the method of variation of parameters, though for very simple $r(x)$ inspection may work. | $y=y_{c}+y_{p}$ Since $\alpha _{j}$ are the solutions of the polynomial of degree n : ${\textstyle \prod _{j=1}^{n}(\alpha -\alpha _{j})=0}$ , then: for $\alpha _{j}$ all different, $y_{c}=\sum _{j=1}^{n}C_{j}e^{\alpha _{j}x}$ for each root $\alpha _{j}$ repeated $k_{j}$ times, $y_{c}=\sum _{j=1}^{n}\left(\sum _{\ell =1}^{k_{j}}C_{j,\ell }x^{\ell -1}\right)e^{\alpha _{j}x}$ for some $\alpha _{j}$ complex, then setting $\alpha _{j}=\chi _{j}+i\gamma _{j}$ , and using Euler's formula, allows some terms in the previous results to be written in the form $C_{j}e^{\alpha _{j}x}=C_{j}e^{\chi _{j}x}\cos(\gamma _{j}x+\varphi _{j})$ where $\varphi _{j}$ is an arbitrary constant (phase shift). |

## Guessing solutions

When all other methods for solving an ODE fail, or in the cases where we have some intuition about what the solution to a DE might look like, it is sometimes possible to solve a DE simply by guessing the solution and validating it is correct. To use this method, we simply guess a solution to the differential equation, and then plug the solution into the differential equation to verify whether it satisfies the equation. If it does then we have a particular solution to the DE, otherwise we start over again and try another guess. For instance we could guess that the solution to a DE has the form: $y=Ae^{i\alpha t}$ since this is a very common solution that physically behaves in a sinusoidal way.

In the case of a first order ODE that is non-homogeneous we need to first find a solution to the homogeneous portion of the DE, otherwise known as the associated homogeneous equation, and then find a solution to the entire non-homogeneous equation by guessing. Finally, we add both of these solutions together to obtain the general solution to the ODE, that is:

${\text{general solution}}={\text{general solution of the associated homogeneous equation}}+{\text{particular solution}}$

## Software for ODE solving

- Maxima, an open-source computer algebra system.
- COPASI, a free (Artistic License 2.0) software package for the integration and analysis of ODEs.
- MATLAB, a technical computing application (MATrix LABoratory)
- GNU Octave, a high-level language, primarily intended for numerical computations.
- Scilab, an open source application for numerical computation.
- Maple, a proprietary application for symbolic calculations.
- Mathematica, a proprietary application primarily intended for symbolic calculations.
- SymPy, a Python package that can solve ODEs symbolically
- Julia (programming language), a high-level language primarily intended for numerical computations.
- SageMath, an open-source application that uses a Python-like syntax with a wide range of capabilities spanning several branches of mathematics.
- SciPy, a Python package that includes an ODE integration module.
- Chebfun, an open-source package, written in MATLAB, for computing with functions to 15-digit accuracy.
- GNU R, an open source computational environment primarily intended for statistics, which includes packages for ODE solving.
