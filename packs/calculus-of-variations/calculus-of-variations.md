---
title: "Calculus of variations"
source: https://en.wikipedia.org/wiki/Calculus_of_variations
domain: calculus-of-variations
license: CC-BY-SA-4.0
tags: calculus of variations, euler-lagrange equation, principle of least action, isoperimetric inequality
fetched: 2026-07-02
---

# Calculus of variations

The **calculus of variations** (or **variational calculus**) is a field of mathematical analysis that uses variations, which are small changes in functions and functionals, to find maxima and minima of functionals: mappings from a set of functions to the real numbers. Functionals are often expressed as definite integrals involving functions and their derivatives. Functions that maximize or minimize functionals may be found using the Euler–Lagrange equation of the calculus of variations.

A simple example of such a problem is to find the curve of shortest length connecting two points. If there are no constraints, the solution is a straight line between the points. However, if the curve is constrained to lie on a surface in space, then the solution is less obvious, and possibly many solutions may exist. Such solutions are known as *geodesics*. A related problem is posed by Fermat's principle: light follows the path of shortest optical length connecting two points, which depends upon the material of the medium. One corresponding concept in mechanics is the principle of least/stationary action.

Many important problems involve functions of several variables. Solutions of boundary value problems for the Laplace equation satisfy the Dirichlet's principle. Plateau's problem requires finding a surface of minimal area that spans a given contour in space: a solution can often be found by dipping a frame in soapy water. Although such experiments are relatively easy to perform, their mathematical formulation is far from simple: there may be more than one locally minimizing surface, and they may have non-trivial topology.

## History

The calculus of variations began with the work of Isaac Newton, such as with Newton's minimal resistance problem, which he formulated and solved in 1685, and later published in his *Principia* in 1687, which was the first problem in the field to be formulated and correctly solved, and was also one of the most difficult problems tackled by variational methods prior to the twentieth century. This problem was followed by the brachistochrone curve problem raised by Johann Bernoulli (1696), which was similar to one raised by Galileo Galilei in 1638, but he did not solve the problem explicitly nor did he use the methods based on calculus. Bernoulli solved the problem using the principle of least time in the process, but not calculus of variations. In 1697 Newton solved the problem using variational techniques, and as a result, he pioneered the field with his work on the two problems. The problem would immediately occupy the attention of Jacob Bernoulli and the Marquis de l'Hôpital, but Leonhard Euler first elaborated the subject, beginning in 1733. Joseph-Louis Lagrange was influenced by Euler's work to contribute greatly to the theory. After Euler saw the 1755 work of the 19-year-old Lagrange, Euler dropped his own partly geometric approach in favor of Lagrange's purely analytic approach and renamed the subject the *calculus of variations* in his 1756 lecture *Elementa Calculi Variationum*.

Adrien-Marie Legendre (1786) laid down a method, not entirely satisfactory, for the discrimination of maxima and minima. Isaac Newton and Gottfried Leibniz also gave some early attention to the subject. To this discrimination Vincenzo Brunacci (1810), Carl Friedrich Gauss (1829), Siméon Poisson (1831), Mikhail Ostrogradsky (1834), and Carl Jacobi (1837) have been among the contributors. An important general work is that of Pierre Frédéric Sarrus (1842) which was condensed and improved by Augustin-Louis Cauchy (1844). Other valuable treatises and memoirs have been written by Strauch (1849), John Hewitt Jellett (1850), Otto Hesse (1857), Alfred Clebsch (1858), and Lewis Buffett Carll (1885), but perhaps the most important work of the century is that of Karl Weierstrass. His celebrated course on the theory is epoch-making, and it may be asserted that he was the first to place it on a firm and unquestionable foundation. The 20th and the 23rd Hilbert problem published in 1900 encouraged further development.

In the 20th century David Hilbert, Oskar Bolza, Gilbert Ames Bliss, Emmy Noether, Leonida Tonelli, Henri Lebesgue and Jacques Hadamard among others made significant contributions. Marston Morse applied calculus of variations in what is now called Morse theory. Lev Pontryagin, Ralph Rockafellar and F. H. Clarke developed new mathematical tools for the calculus of variations in optimal control theory. The dynamic programming of Richard Bellman is an alternative to the calculus of variations.

## Extrema

The calculus of variations is concerned with the maxima or minima (collectively called **extrema**) of functionals. A functional maps functions to scalars, so functionals have been described as "functions of functions." Functionals have extrema with respect to the elements y of a given function space defined over a given domain. A functional $J[y]$ is said to have an extremum at the function f if $\Delta J=J[y]-J[f]$ has the same sign for all y in an arbitrarily small neighborhood of $f.$ The function f is called an **extremal** function or extremal. The extremum $J[f]$ is called a local maximum if $\Delta J\leq 0$ everywhere in an arbitrarily small neighborhood of $f,$ and a local minimum if $\Delta J\geq 0$ there. For a function space of continuous functions, extrema of corresponding functionals are called **strong extrema** or **weak extrema**, depending on whether the first derivatives of the continuous functions are respectively all continuous or not.

Both strong and weak extrema of functionals are for a space of continuous functions but strong extrema have the additional requirement that the first derivatives of the functions in the space be continuous. Thus a strong extremum is also a weak extremum, but the converse may not hold. Finding strong extrema is more difficult than finding weak extrema. An example of a necessary condition that is used for finding weak extrema is the Euler–Lagrange equation.

## Euler–Lagrange equation

Finding the extrema of functionals is similar to finding the maxima and minima of functions. The maxima and minima of a function may be located by finding the points where its derivative vanishes (i.e., is equal to zero). The extrema of functionals may be obtained by finding functions for which the functional derivative is equal to zero. This leads to solving the associated Euler–Lagrange equation.

Consider the functional

$J[y]=\int _{x_{1}}^{x_{2}}L\left(x,y(x),y'(x)\right)\,dx,$

where

- $x_{1},x_{2}$ are constants,
- $y(x)$ is twice continuously differentiable,
- $y'(x)={\frac {dy}{dx}},$
- $L\left(x,y(x),y'(x)\right)$ is twice continuously differentiable with respect to its arguments $x,y,$ and $y'.$

If the functional $J[y]$ attains a local minimum at $f,$ and $\eta (x)$ is an arbitrary function that has at least one derivative and vanishes at the endpoints $x_{1}$ and $x_{2},$ then for any number $\varepsilon$ close to 0,

$J[f]\leq J[f+\varepsilon \eta ]\,.$

The term $\varepsilon \eta$ is called the **variation** of the function f and is denoted by $\delta f.$

Substituting $f+\varepsilon \eta$ for y in the functional $J[y],$ the result is a function of $\varepsilon ,$

$\Phi (\varepsilon )=J[f+\varepsilon \eta ]\,.$

Since the functional $J[y]$ has a minimum for $y=f$ the function $\Phi (\varepsilon )$ has a minimum at $\varepsilon =0$ and thus,

$\Phi '(0)\equiv \left.{\frac {d\Phi }{d\varepsilon }}\right|_{\varepsilon =0}=\int _{x_{1}}^{x_{2}}\left.{\frac {dL}{d\varepsilon }}\right|_{\varepsilon =0}dx=0\,.$

Taking the total derivative of $L\left[x,y,y'\right],$ where $y=f+\varepsilon \eta$ and $y'=f'+\varepsilon \eta '$ are considered as functions of $\varepsilon$ rather than $x,$ yields

${\frac {dL}{d\varepsilon }}={\frac {\partial L}{\partial y}}{\frac {dy}{d\varepsilon }}+{\frac {\partial L}{\partial y'}}{\frac {dy'}{d\varepsilon }}$

and because ${\frac {dy}{d\varepsilon }}=\eta$ and ${\frac {dy'}{d\varepsilon }}=\eta ',$

${\frac {dL}{d\varepsilon }}={\frac {\partial L}{\partial y}}\eta +{\frac {\partial L}{\partial y'}}\eta '.$

Therefore,

${\begin{aligned}\int _{x_{1}}^{x_{2}}\left.{\frac {dL}{d\varepsilon }}\right|_{\varepsilon =0}dx&=\int _{x_{1}}^{x_{2}}\left({\frac {\partial L}{\partial f}}\eta +{\frac {\partial L}{\partial f'}}\eta '\right)\,dx\\&=\int _{x_{1}}^{x_{2}}{\frac {\partial L}{\partial f}}\eta \,dx+\left.{\frac {\partial L}{\partial f'}}\eta \right|_{x_{1}}^{x_{2}}-\int _{x_{1}}^{x_{2}}\eta {\frac {d}{dx}}{\frac {\partial L}{\partial f'}}\,dx\\&=\int _{x_{1}}^{x_{2}}\left({\frac {\partial L}{\partial f}}\eta -\eta {\frac {d}{dx}}{\frac {\partial L}{\partial f'}}\right)\,dx\\\end{aligned}}$

where $L\left[x,y,y'\right]\to L\left[x,f,f'\right]$ when $\varepsilon =0$ and we have used integration by parts on the second term. The second term on the second line vanishes because $\eta =0$ at $x_{1}$ and $x_{2}$ by definition. Also, as previously mentioned the left side of the equation is zero so that

$\int _{x_{1}}^{x_{2}}\eta (x)\left({\frac {\partial L}{\partial f}}-{\frac {d}{dx}}{\frac {\partial L}{\partial f'}}\right)\,dx=0\,.$

According to the fundamental lemma of calculus of variations, the fact that this equation holds for any choice of $\eta$ implies that the part of the integrand in parentheses is zero, i.e.

${\frac {\partial L}{\partial f}}-{\frac {d}{dx}}{\frac {\partial L}{\partial f'}}=0$

which is called the **Euler–Lagrange equation**. The left hand side of this equation is called the functional derivative of $J[f]$ and is denoted $\delta J$ or $\delta f(x).$

In general this gives a second-order ordinary differential equation which can be solved to obtain the extremal function $f(x).$ The Euler–Lagrange equation is a necessary, but not sufficient, condition for an extremum $J[f].$ A sufficient condition for a minimum is given in the section Variations and sufficient condition for a minimum.

### Example

In order to illustrate this process, consider the problem of finding the extremal function $y=f(x),$ which is the shortest curve that connects two points $\left(x_{1},y_{1}\right)$ and $\left(x_{2},y_{2}\right).$ The arc length of the curve is given by

$A[y]=\int _{x_{1}}^{x_{2}}{\sqrt {1+[y'(x)]^{2}}}\,dx\,,$

with

$y'(x)={\frac {dy}{dx}}\,,\ \ y_{1}=f(x_{1})\,,\ \ y_{2}=f(x_{2})\,.$

Note that assuming y is a function of x loses generality; ideally both should be a function of some other parameter. This approach is good solely for instructive purposes.

The Euler–Lagrange equation will now be used to find the extremal function $f(x)$ that minimizes the functional $A[y].$

${\frac {\partial L}{\partial f}}-{\frac {d}{dx}}{\frac {\partial L}{\partial f'}}=0$

with

$L={\sqrt {1+[f'(x)]^{2}}}\,.$

Since f does not appear explicitly in $L,$ the first term in the Euler–Lagrange equation vanishes for all $f(x)$ and thus,

${\frac {d}{dx}}{\frac {\partial L}{\partial f'}}=0\,.$

Substituting for L and taking the derivative,

${\frac {d}{dx}}\ {\frac {f'(x)}{\sqrt {1+[f'(x)]^{2}}}}\ =0\,.$

Thus

${\frac {f'(x)}{\sqrt {1+[f'(x)]^{2}}}}=c\,,$

for some constant c . Then

${\frac {[f'(x)]^{2}}{1+[f'(x)]^{2}}}=c^{2}\,,$

where

$0\leq c^{2}<1.$

Solving, we get

$[f'(x)]^{2}={\frac {c^{2}}{1-c^{2}}}$

which implies that

$f'(x)=m$

is a constant and therefore that the shortest curve that connects two points $\left(x_{1},y_{1}\right)$ and $\left(x_{2},y_{2}\right)$ is

$f(x)=mx+b\qquad {\text{with}}\ \ m={\frac {y_{2}-y_{1}}{x_{2}-x_{1}}}\quad {\text{and}}\quad b={\frac {x_{2}y_{1}-x_{1}y_{2}}{x_{2}-x_{1}}}$

and we have thus found the extremal function $f(x)$ that minimizes the functional $A[y]$ so that $A[f]$ is a minimum. The equation for a straight line is $y=mx+b.$ In other words, the shortest distance between two points is a straight line.

## Beltrami's identity

In physics problems it may be the case that ${\frac {\partial L}{\partial x}}=0,$ meaning the integrand is a function of $f(x)$ and $f'(x)$ but x does not appear separately. In that case, the Euler–Lagrange equation can be simplified to the Beltrami identity

$L-f'{\frac {\partial L}{\partial f'}}=C\,,$

where C is a constant. The left hand side is the Legendre transformation of L with respect to $f'(x).$

The intuition behind this result is that, if the variable x is actually time, then the statement ${\frac {\partial L}{\partial x}}=0$ implies that the Lagrangian is time-independent. By Noether's theorem, there is an associated conserved quantity. In this case, this quantity is the Hamiltonian, the Legendre transform of the Lagrangian, which (often) coincides with the energy of the system. This is (minus) the constant in Beltrami's identity.

Recently, methods have been developed to incorporate symmetry information directly into the inverse problem of the calculus of variations. By combining the Helmholtz conditions involved in the inverse problem with relations derived from Noether's identity, it is possible to reconstruct Lagrangians that reproduce given equations of motion while ensuring the presence of prescribed symmetries.

## Euler–Poisson equation

If S depends on higher-derivatives of $y(x)$ , that is, if

$S=\int _{a}^{b}f(x,y(x),y'(x),\dots ,y^{(n)}(x))dx,$

then y must satisfy the Euler–Poisson equation,

${\frac {\partial f}{\partial y}}-{\frac {d}{dx}}\left({\frac {\partial f}{\partial y'}}\right)+\dots +(-1)^{n}{\frac {d^{n}}{dx^{n}}}\left[{\frac {\partial f}{\partial y^{(n)}}}\right]=0.$

## Du Bois-Reymond's theorem

The discussion thus far has assumed that extremal functions possess two continuous derivatives, although the existence of the integral J requires only first derivatives of trial functions. The condition that the first variation vanishes at an extremal may be regarded as a **weak form** of the Euler–Lagrange equation. The theorem of Du Bois-Reymond asserts that this weak form implies the strong form. If L has continuous first and second derivatives with respect to all of its arguments, and if

${\frac {\partial ^{2}L}{\partial f'^{2}}}\neq 0,$

then f has two continuous derivatives, and it satisfies the Euler–Lagrange equation.

## Lavrentiev phenomenon

Hilbert was the first to give good conditions for the Euler–Lagrange equations to give a stationary solution. Within a convex area and a positive thrice differentiable Lagrangian the solutions are composed of a countable collection of sections that either go along the boundary or satisfy the Euler–Lagrange equations in the interior.

However Lavrentiev in 1926 showed that there are circumstances where there is no optimum solution but one can be approached arbitrarily closely by increasing numbers of sections. The Lavrentiev Phenomenon identifies a difference in the infimum of a minimization problem across different classes of admissible functions. For instance the following problem, presented by Manià in 1934:

$L[x]=\int _{0}^{1}(x^{3}-t)^{2}x'^{6},$

${A}=\{x\in W^{1,1}(0,1):x(0)=0,\ x(1)=1\}.$

Clearly, $x(t)=t^{\frac {1}{3}}$ minimizes the functional, but we find any function $x\in W^{1,\infty }$ gives a value bounded away from the infimum.

Examples (in one-dimension) are traditionally manifested across $W^{1,1}$ and $W^{1,\infty },$ but Ball and Mizel procured the first functional that displayed Lavrentiev's Phenomenon across $W^{1,p}$ and $W^{1,q}$ for $1\leq p<q<\infty .$ There are several results that gives criteria under which the phenomenon does not occur - for instance 'standard growth', a Lagrangian with no dependence on the second variable, or an approximating sequence satisfying Cesari's Condition (D) - but results are often particular, and applicable to a small class of functionals.

Connected with the Lavrentiev Phenomenon is the repulsion property: any functional displaying Lavrentiev's Phenomenon will display the weak repulsion property.

## Functions of several variables

For example, if $\varphi (x,y)$ denotes the displacement of a membrane above the domain D in the $x,y$ plane, then its potential energy is proportional to its surface area:

$U[\varphi ]=\iint _{D}{\sqrt {1+\nabla \varphi \cdot \nabla \varphi }}\,dx\,dy.$

Plateau's problem consists of finding a function that minimizes the surface area while assuming prescribed values on the boundary of D ; the solutions are called **minimal surfaces**. The Euler–Lagrange equation for this problem is nonlinear:

$\varphi _{xx}(1+\varphi _{y}^{2})+\varphi _{yy}(1+\varphi _{x}^{2})-2\varphi _{x}\varphi _{y}\varphi _{xy}=0.$

See Courant (1950) for details.

### Dirichlet's principle

It is often sufficient to consider only small displacements of the membrane, whose energy difference from no displacement is approximated by

$V[\varphi ]={\frac {1}{2}}\iint _{D}\nabla \varphi \cdot \nabla \varphi \,dx\,dy.$

The functional V is to be minimized among all trial functions $\varphi$ that assume prescribed values on the boundary of D . If u is the minimizing function and v is an arbitrary smooth function that vanishes on the boundary of D , then the first variation of $V[u+\varepsilon v]$ must vanish:

$\left.{\frac {d}{d\varepsilon }}V[u+\varepsilon v]\right|_{\varepsilon =0}=\iint _{D}\nabla u\cdot \nabla v\,dx\,dy=0.$

Provided that u has two derivatives, we may apply the divergence theorem to obtain

$\iint _{D}\nabla \cdot (v\nabla u)\,dx\,dy=\iint _{D}\nabla u\cdot \nabla v+v\nabla \cdot \nabla u\,dx\,dy=\int _{C}v{\frac {\partial u}{\partial n}}\,ds,$

where C is the boundary of $D,$ s is arclength along C and $\partial u/\partial n$ is the normal derivative of u on $C.$ Since v vanishes on C and the first variation vanishes, the result is

$\iint _{D}v\nabla \cdot \nabla u\,dx\,dy=0$

for all smooth functions v that vanish on the boundary of D . The proof for the case of one dimensional integrals may be adapted to this case to show that

$\nabla \cdot \nabla u=0$ in $D.$

The difficulty with this reasoning is the assumption that the minimizing function u must have two derivatives. Riemann argued that the existence of a smooth minimizing function was assured by the connection with the physical problem: membranes do indeed assume configurations with minimal potential energy. Riemann named this idea the Dirichlet principle in honor of his teacher Peter Gustav Lejeune Dirichlet. However Weierstrass gave an example of a variational problem with no solution: minimize

$W[\varphi ]=\int _{-1}^{1}(x\varphi ')^{2}\,dx$

among all functions $\varphi$ that satisfy $\varphi (-1)=-1$ and $\varphi (1)=1.$ W can be made arbitrarily small by choosing piecewise linear functions that make a transition between −1 and 1 in a small neighborhood of the origin. However, there is no function that makes $W=0.$ Eventually it was shown that Dirichlet's principle is valid, but it requires a sophisticated application of the regularity theory for elliptic partial differential equations; see Jost and Li–Jost (1998).

### Generalization to other boundary value problems

A more general expression for the potential energy of a membrane is

$V[\varphi ]=\iint _{D}\left[{\frac {1}{2}}\nabla \varphi \cdot \nabla \varphi +f(x,y)\varphi \right]\,dx\,dy\,+\int _{C}\left[{\frac {1}{2}}\sigma (s)\varphi ^{2}+g(s)\varphi \right]\,ds.$

This corresponds to an external force density $f(x,y)$ in $D,$ an external force $g(s)$ on the boundary $C,$ and elastic forces with modulus $\sigma (s)$ acting on C . The function that minimizes the potential energy **with no restriction on its boundary values** will be denoted by u . Provided that f and g are continuous, regularity theory implies that the minimizing function u will have two derivatives. In taking the first variation, no boundary condition need be imposed on the increment v . The first variation of $V[u+\varepsilon v]$ is given by

$\iint _{D}\left[\nabla u\cdot \nabla v+fv\right]\,dx\,dy+\int _{C}\left[\sigma uv+gv\right]\,ds=0.$

If we apply the divergence theorem, the result is

$\iint _{D}\left[-v\nabla \cdot \nabla u+vf\right]\,dx\,dy+\int _{C}v\left[{\frac {\partial u}{\partial n}}+\sigma u+g\right]\,ds=0.$

If we first set $v=0$ on $C,$ the boundary integral vanishes, and we conclude as before that

$-\nabla \cdot \nabla u+f=0$

in D . Then if we allow v to assume arbitrary boundary values, this implies that u must satisfy the boundary condition

${\frac {\partial u}{\partial n}}+\sigma u+g=0,$

on C . This boundary condition is a consequence of the minimizing property of u : it is not imposed beforehand. Such conditions are called **natural boundary conditions**.

The preceding reasoning is not valid if $\sigma$ vanishes identically on $C.$ In such a case, we could allow a trial function $\varphi \equiv c$ , where c is a constant. For such a trial function,

$V[c]=c\left[\iint _{D}f\,dx\,dy+\int _{C}g\,ds\right].$

By appropriate choice of c , V can assume any value unless the quantity inside the brackets vanishes. Therefore, the variational problem is meaningless unless

$\iint _{D}f\,dx\,dy+\int _{C}g\,ds=0.$

This condition implies that net external forces on the system are in equilibrium. If these forces are in equilibrium, then the variational problem has a solution, but it is not unique, since an arbitrary constant may be added. Further details and examples are in Courant and Hilbert (1953).

## Eigenvalue problems

Both one-dimensional and multi-dimensional **eigenvalue problems** can be formulated as variational problems.

### Sturm–Liouville problems

The Sturm–Liouville eigenvalue problem involves a general quadratic form

$Q[y]=\int _{x_{1}}^{x_{2}}\left[p(x)y'(x)^{2}+q(x)y(x)^{2}\right]\,dx,$

where y is restricted to functions that satisfy the boundary conditions

$y(x_{1})=0,\quad y(x_{2})=0.$

Let R be a normalization integral

$R[y]=\int _{x_{1}}^{x_{2}}r(x)y(x)^{2}\,dx.$

The functions $p(x)$ and $r(x)$ are required to be everywhere positive and bounded away from zero. The primary variational problem is to minimize the ratio $Q/R$ among all y satisfying the endpoint conditions, which is equivalent to minimizing $Q[y]$ under the constraint that $R[y]$ is constant. It is shown below that the Euler–Lagrange equation for the minimizing u is

$-(pu')'+qu-\lambda ru=0,$

where $\lambda$ is the quotient

$\lambda ={\frac {Q[u]}{R[u]}}.$

It can be shown (see Gelfand and Fomin 1963) that the minimizing u has two derivatives and satisfies the Euler–Lagrange equation. The associated $\lambda$ will be denoted by $\lambda _{1}$ ; it is the lowest eigenvalue for this equation and boundary conditions. The associated minimizing function will be denoted by $u_{1}(x)$ . This variational characterization of eigenvalues leads to the Rayleigh–Ritz method: choose an approximating u as a linear combination of basis functions (for example trigonometric functions) and carry out a finite-dimensional minimization among such linear combinations. This method is often surprisingly accurate.

The next smallest eigenvalue and eigenfunction can be obtained by minimizing Q under the additional constraint

$\int _{x_{1}}^{x_{2}}r(x)u_{1}(x)y(x)\,dx=0.$

This procedure can be extended to obtain the complete sequence of eigenvalues and eigenfunctions for the problem.

The variational problem also applies to more general boundary conditions. Instead of requiring that y vanish at the endpoints, we may not impose any condition at the endpoints, and set

$Q[y]=\int _{x_{1}}^{x_{2}}\left[p(x)y'(x)^{2}+q(x)y(x)^{2}\right]\,dx+a_{1}y(x_{1})^{2}+a_{2}y(x_{2})^{2},$

where $a_{1}$ and $a_{2}$ are arbitrary. If we set $y=u+\varepsilon v$ , the first variation for the ratio $Q/R$ is

$V_{1}={\frac {2}{R[u]}}\left(\int _{x_{1}}^{x_{2}}\left[p(x)u'(x)v'(x)+q(x)u(x)v(x)-\lambda r(x)u(x)v(x)\right]\,dx+a_{1}u(x_{1})v(x_{1})+a_{2}u(x_{2})v(x_{2})\right),$

where $\lambda$ is given by the ratio $Q[u]/R[u]$ as previously. After integration by parts,

${\frac {R[u]}{2}}V_{1}=\int _{x_{1}}^{x_{2}}v(x)\left[-(pu')'+qu-\lambda ru\right]\,dx+v(x_{1})[-p(x_{1})u'(x_{1})+a_{1}u(x_{1})]+v(x_{2})[p(x_{2})u'(x_{2})+a_{2}u(x_{2})].$

If we first require that v vanish at the endpoints, the first variation will vanish for all such v only if

$-(pu')'+qu-\lambda ru=0\quad {\hbox{for}}\quad x_{1}<x<x_{2}.$

If u satisfies this condition, then the first variation will vanish for arbitrary v only if

$-p(x_{1})u'(x_{1})+a_{1}u(x_{1})=0,\quad {\hbox{and}}\quad p(x_{2})u'(x_{2})+a_{2}u(x_{2})=0.$

These latter conditions are the **natural boundary conditions** for this problem, since they are not imposed on trial functions for the minimization, but are instead a consequence of the minimization.

### Eigenvalue problems in several dimensions

Eigenvalue problems in higher dimensions are defined in analogy with the one-dimensional case. For example, given a domain D with boundary B in three dimensions we may define

$Q[\varphi ]=\iiint _{D}p(X)\nabla \varphi \cdot \nabla \varphi +q(X)\varphi ^{2}\,dx\,dy\,dz+\iint _{B}\sigma (S)\varphi ^{2}\,dS,$

and

$R[\varphi ]=\iiint _{D}r(X)\varphi (X)^{2}\,dx\,dy\,dz.$

Let u be the function that minimizes the quotient $Q[\varphi ]/R[\varphi ]$ , with no condition prescribed on the boundary $B.$ The Euler–Lagrange equation satisfied by u is

$-\nabla \cdot (p(X)\nabla u)+q(x)u-\lambda r(x)u=0,$

where

$\lambda ={\frac {Q[u]}{R[u]}}.$

The minimizing u must also satisfy the natural boundary condition

$p(S){\frac {\partial u}{\partial n}}+\sigma (S)u=0,$

on the boundary $B.$ This result depends upon the regularity theory for elliptic partial differential equations; see Jost and Li–Jost (1998) for details. Many extensions, including completeness results, asymptotic properties of the eigenvalues and results concerning the nodes of the eigenfunctions are in Courant and Hilbert (1953).

## Applications

### Optics

Fermat's principle states that light takes a path that (locally) minimizes the optical length between its endpoints. If the x -coordinate is chosen as the parameter along the path, and $y=f(x)$ along the path, then the optical length is given by

$A[f]=\int _{x_{0}}^{x_{1}}n(x,f(x)){\sqrt {1+f'(x)^{2}}}dx,$

where the refractive index $n(x,y)$ depends upon the material. If we try $f(x)=f_{0}(x)+\varepsilon f_{1}(x)$ then the first variation of A (the derivative of A with respect to $\varepsilon$ ) is

$\delta A[f_{0},f_{1}]=\int _{x_{0}}^{x_{1}}\left[{\frac {n(x,f_{0})f_{0}'(x)f_{1}'(x)}{\sqrt {1+f_{0}'(x)^{2}}}}+n_{y}(x,f_{0})f_{1}{\sqrt {1+f_{0}'(x)^{2}}}\right]dx.$

After integration by parts of the first term within brackets, we obtain the Euler–Lagrange equation

$-{\frac {d}{dx}}\left[{\frac {n(x,f_{0})f_{0}'}{\sqrt {1+f_{0}'^{2}}}}\right]+n_{y}(x,f_{0}){\sqrt {1+f_{0}'(x)^{2}}}=0.$

The light rays may be determined by integrating this equation. This formalism is used in the context of Lagrangian optics and Hamiltonian optics.

#### Snell's law

There is a discontinuity of the refractive index when light enters or leaves a lens. Let

$n(x,y)={\begin{cases}n_{(-)}&{\text{if}}\quad x<0,\\n_{(+)}&{\text{if}}\quad x>0,\end{cases}}$

where $n_{(-)}$ and $n_{(+)}$ are constants. Then the Euler–Lagrange equation holds as before in the region where $x<0$ or $x>0$ , and in fact the path is a straight line there, since the refractive index is constant. At the $x=0$ , f must be continuous, but $f'$ may be discontinuous. After integration by parts in the separate regions and using the Euler–Lagrange equations, the first variation takes the form

$\delta A[f_{0},f_{1}]=f_{1}(0)\left[n_{(-)}{\frac {f_{0}'(0^{-})}{\sqrt {1+f_{0}'(0^{-})^{2}}}}-n_{(+)}{\frac {f_{0}'(0^{+})}{\sqrt {1+f_{0}'(0^{+})^{2}}}}\right].$

The factor multiplying $n_{(-)}$ is the sine of angle of the incident ray with the x axis, and the factor multiplying $n_{(+)}$ is the sine of angle of the refracted ray with the x axis. Snell's law for refraction requires that these terms be equal. As this calculation demonstrates, Snell's law is equivalent to vanishing of the first variation of the optical path length.

#### Fermat's principle in three dimensions

It is expedient to use vector notation: let $X=(x_{1},x_{2},x_{3}),$ let t be a parameter, let $X(t)$ be the parametric representation of a curve $C,$ and let ${\dot {X}}(t)$ be its tangent vector. The optical length of the curve is given by

$A[C]=\int _{t_{0}}^{t_{1}}n(X){\sqrt {{\dot {X}}\cdot {\dot {X}}}}\,dt.$

Note that this integral is invariant with respect to changes in the parametric representation of $C.$ The Euler–Lagrange equations for a minimizing curve have the symmetric form

${\frac {d}{dt}}P={\sqrt {{\dot {X}}\cdot {\dot {X}}}}\,\nabla n,$

where

$P={\frac {n(X){\dot {X}}}{\sqrt {{\dot {X}}\cdot {\dot {X}}}}}.$

It follows from the definition that P satisfies

$P\cdot P=n(X)^{2}.$

Therefore, the integral may also be written as

$A[C]=\int _{t_{0}}^{t_{1}}P\cdot {\dot {X}}\,dt.$

This form suggests that if we can find a function $\psi$ whose gradient is given by $P,$ then the integral A is given by the difference of $\psi$ at the endpoints of the interval of integration. Thus the problem of studying the curves that make the integral stationary can be related to the study of the level surfaces of $\psi$ . In order to find such a function, we turn to the wave equation, which governs the propagation of light. This formalism is used in the context of Lagrangian optics and Hamiltonian optics.

##### Connection with the wave equation

The wave equation for an inhomogeneous medium is

$u_{tt}=c^{2}\nabla \cdot \nabla u,$

where c is the velocity, which generally depends upon X . Wave fronts for light are characteristic surfaces for this partial differential equation: they satisfy

$\varphi _{t}^{2}=c(X)^{2}\,\nabla \varphi \cdot \nabla \varphi .$

We may look for solutions in the form

$\varphi (t,X)=t-\psi (X).$

In that case, $\psi$ satisfies

$\nabla \psi \cdot \nabla \psi =n^{2},$

where $n=1/c$ . According to the theory of first-order partial differential equations, if $P=\nabla \psi ,$ then P satisfies

${\frac {dP}{ds}}=n\,\nabla n,$

along a system of curves (**the light rays**) that are given by

${\frac {dX}{ds}}=P.$

These equations for solution of a first-order partial differential equation are identical to the Euler–Lagrange equations if we make the identification

${\frac {ds}{dt}}={\frac {\sqrt {{\dot {X}}\cdot {\dot {X}}}}{n}}.$

We conclude that the function $\psi$ is the value of the minimizing integral A as a function of the upper end point. That is, when a family of minimizing curves is constructed, the values of the optical length satisfy the characteristic equation corresponding the wave equation. Hence, solving the associated partial differential equation of first order is equivalent to finding families of solutions of the variational problem. This is the essential content of the Hamilton–Jacobi theory, which applies to more general variational problems.

### Mechanics

In classical mechanics, the action, $S,$ is defined as the time integral of the Lagrangian, L . The Lagrangian is the difference of energies,

$L=T-U,$

where T is the kinetic energy of a mechanical system and U its potential energy. Hamilton's principle (or the action principle) states that the motion of a conservative holonomic (integrable constraints) mechanical system is such that the action integral

$S=\int _{t_{0}}^{t_{1}}L(x,{\dot {x}},t)\,dt$

is stationary with respect to variations in the path $x(t)$ . The Euler–Lagrange equations for this system are known as Lagrange's equations:

${\frac {d}{dt}}{\frac {\partial L}{\partial {\dot {x}}}}={\frac {\partial L}{\partial x}},$

and they are equivalent to Newton's equations of motion (for such systems).

The conjugate momenta P are defined by

$p={\frac {\partial L}{\partial {\dot {x}}}}.$

For example, if

$T={\frac {1}{2}}m{\dot {x}}^{2},$

then $p=m{\dot {x}}.$

Hamiltonian mechanics results if the conjugate momenta are introduced in place of ${\dot {x}}$ by a Legendre transformation of the Lagrangian L into the Hamiltonian H defined by

$H(x,p,t)=p\,{\dot {x}}-L(x,{\dot {x}},t).$

The Hamiltonian is the total energy of the system: $H=T+U$ . Analogy with Fermat's principle suggests that solutions of Lagrange's equations (the particle trajectories) may be described in terms of level surfaces of some function of X . This function is a solution of the Hamilton–Jacobi equation:

${\frac {\partial \psi }{\partial t}}+H\left(x,{\frac {\partial \psi }{\partial x}},t\right)=0.$

### Further applications

Further applications of the calculus of variations include the following:

- The derivation of the catenary shape
- Solution to Newton's minimal resistance problem
- Solution to the brachistochrone problem
- Solution to the tautochrone problem
- Solution to isoperimetric problems
- Calculating geodesics
- Finding minimal surfaces and solving Plateau's problem
- Optimal control
- Analytical mechanics, or reformulations of Newton's laws of motion, most notably Lagrangian and Hamiltonian mechanics;
- Geometric optics, especially Lagrangian and Hamiltonian optics;
- Variational method (quantum mechanics), one way of finding approximations to the lowest energy eigenstate or ground state, and some excited states;
- Variational Bayesian methods, a family of techniques for approximating intractable integrals arising in Bayesian inference and machine learning;
- Variational methods in general relativity, a family of techniques using calculus of variations to solve problems in Einstein's general theory of relativity;
- Finite element method is a variational method for finding numerical solutions to boundary-value problems in differential equations;
- Total variation denoising, an image processing method for filtering high variance or noisy signals.

## Variations and sufficient condition for a minimum

Calculus of variations is concerned with variations of functionals, which are small changes in the functional's value due to small changes in the function that is its argument. The **first variation** is defined as the linear part of the change in the functional, and the **second variation** is defined as the quadratic part.

For example, if $J[y]$ is a functional with the function $y=y(x)$ as its argument, and there is a small change in its argument from y to $y+h,$ where $h=h(x)$ is a function in the same function space as y , then the corresponding change in the functional is

$\Delta J[h]=J[y+h]-J[y].$

The functional $J[y]$ is said to be **differentiable** if

$\Delta J[h]=\varphi [h]+\varepsilon \|h\|,$

where $\varphi [h]$ is a linear functional, $\|h\|$ is the norm of $h,$ and $\varepsilon \to 0$ as $\|h\|\to 0.$ The linear functional $\varphi [h]$ is the first variation of $J[y]$ and is denoted by,

$\delta J[h]=\varphi [h].$

The functional $J[y]$ is said to be **twice differentiable** if

$\Delta J[h]=\varphi _{1}[h]+\varphi _{2}[h]+\varepsilon \|h\|^{2},$

where $\varphi _{1}[h]$ is a linear functional (the first variation), $\varphi _{2}[h]$ is a quadratic functional, and $\varepsilon \to 0$ as $\|h\|\to 0.$ The quadratic functional $\varphi _{2}[h]$ is the second variation of $J[y]$ and is denoted by,

$\delta ^{2}J[h]=\varphi _{2}[h].$

The second variation $\delta ^{2}J[h]$ is said to be **strongly positive** if

$\delta ^{2}J[h]\geq k\|h\|^{2},$

for all h and for some constant $k>0$ .

Using the above definitions, especially the definitions of first variation, second variation, and strongly positive, the following sufficient condition for a minimum of a functional can be stated.

> **Sufficient condition for a minimum:**
> 
> The functional
> 
> $J[y]$
> 
> has a minimum at
> 
> $y={\hat {y}}$
> 
> if its first variation
> 
> $\delta J[h]=0$
> 
> at
> 
> $y={\hat {y}}$
> 
> and its second variation
> 
> $\delta ^{2}J[h]$
> 
> is strongly positive at
> 
> $y={\hat {y}}.$
