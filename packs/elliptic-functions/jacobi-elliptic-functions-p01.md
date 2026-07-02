---
title: "Jacobi elliptic functions (part 1/2)"
source: https://en.wikipedia.org/wiki/Jacobi_elliptic_functions
domain: elliptic-functions
license: CC-BY-SA-4.0
tags: elliptic function, jacobi elliptic functions, weierstrass elliptic function, theta function
fetched: 2026-07-02
part: 1/2
---

# Jacobi elliptic functions

In mathematics, the **Jacobi elliptic functions** are a set of basic elliptic functions. They are found in the description of the motion of a pendulum, as well as in the design of electronic elliptic filters. While trigonometric functions are defined with reference to a circle, the Jacobi elliptic functions are a generalization which refer to other conic sections, the ellipse in particular. The relation to trigonometric functions is contained in the notation, for example, by the matching notation $\operatorname {sn}$ for $\sin$ . The Jacobi elliptic functions are used more often in practical problems than the Weierstrass elliptic functions as they do not require notions of complex analysis to be defined and/or understood. They were introduced by Carl Gustav Jakob Jacobi (1829). Carl Friedrich Gauss had already studied special Jacobi elliptic functions in 1797, the lemniscate elliptic functions in particular, but his work was published much later.


## Overview

There are twelve Jacobi elliptic functions denoted by $\operatorname {pq} (u,m)$ , where $\mathrm {p}$ and $\mathrm {q}$ are any of the letters $\mathrm {c}$ , $\mathrm {s}$ , $\mathrm {n}$ , and $\mathrm {d}$ . (Functions of the form $\operatorname {pp} (u,m)$ are trivially set to unity for notational completeness.) u is the argument, and m is the parameter, both of which may be complex. In fact, the Jacobi elliptic functions are meromorphic in both u and m . The distribution of the zeros and poles in the u -plane is well-known. However, questions of the distribution of the zeros and poles in the m -plane remain to be investigated.

In the complex plane of the argument u , the twelve functions form a repeating lattice of simple poles and zeroes. Depending on the function, one repeating parallelogram, or unit cell, will have sides of length $2K$ or $4K$ on the real axis, and $2K'$ or $4K'$ on the imaginary axis, where $K=K(m)$ and $K'=K(1-m)$ are known as the quarter periods with $K(\cdot )$ being the elliptic integral of the first kind. The nature of the unit cell can be determined by inspecting the "auxiliary rectangle" (generally a parallelogram), which is a rectangle formed by the origin $(0,0)$ at one corner, and $(K,K')$ as the diagonally opposite corner. As in the diagram, the four corners of the auxiliary rectangle are named $\mathrm {s}$ , $\mathrm {c}$ , $\mathrm {d}$ , and $\mathrm {n}$ , going counter-clockwise from the origin. The function $\operatorname {pq} (u,m)$ will have a zero at the $\mathrm {p}$ corner and a pole at the $\mathrm {q}$ corner. The twelve functions correspond to the twelve ways of arranging these poles and zeroes in the corners of the rectangle.

When the argument u and parameter m are real, with $0<m<1$ , K and $K'$ will be real and the auxiliary parallelogram will in fact be a rectangle, and the Jacobi elliptic functions will all be real valued on the real line.

Since the Jacobi elliptic functions are doubly periodic in u , they factor through a torus – in effect, their domain can be taken to be a torus, just as cosine and sine are in effect defined on a circle. Instead of having only one circle, we now have the product of two circles, one real and the other imaginary. The complex plane can be replaced by a complex torus. The circumference of the first circle is $4K$ and the second $4K'$ , where K and $K'$ are the quarter periods. Each function has two zeroes and two poles at opposite positions on the torus. Among the points 0 , K , $K+iK'$ , $iK'$ there is one zero and one pole.

The Jacobi elliptic functions are then doubly periodic, meromorphic functions satisfying the following properties:

- There is a simple zero at the corner $\mathrm {p}$ , and a simple pole at the corner  $\mathrm {q}$ .
- The complex number $\mathrm {p} -\mathrm {q}$ is equal to half the period of the function $\operatorname {pq} u$ ; that is, the function $\operatorname {pq} u$ is periodic in the direction $\operatorname {pq}$ , with the period being $2(\mathrm {p} -\mathrm {q} )$ . The function $\operatorname {pq} u$ is also periodic in the other two directions $\mathrm {pp} '$ and $\mathrm {pq} '$ , with periods such that $\mathrm {p} -\mathrm {p} '$ and $\mathrm {p} -\mathrm {q} '$ are quarter periods.

Jacobi elliptic function

$\operatorname {sn}$

Jacobi elliptic function

$\operatorname {cn}$

Jacobi elliptic function

$\operatorname {dn}$

Jacobi elliptic function

$\operatorname {sc}$

Plots of four Jacobi Elliptic Functions in the complex plane of

u

, illustrating their double periodic behavior. Images generated using a version of the

domain coloring

method.

All have values of

$k={\sqrt {m}}$

equal to

$0.8$

.


## Notation

The elliptic functions can be given in a variety of notations, which can make the subject unnecessarily confusing. Elliptic functions are functions of two variables. The first variable might be given in terms of the **amplitude** $\varphi$ , or more commonly, in terms of u given below. The second variable might be given in terms of the **parameter** m , or as the **elliptic modulus** k , where $k^{2}=m$ , or in terms of the **modular angle** $\alpha$ , where $m=\sin ^{2}\alpha$ . The complements of k and m are defined as $m'=1-m$ and ${\textstyle k'={\sqrt {m'}}}$ . These four terms are used below without comment to simplify various expressions.

The twelve Jacobi elliptic functions are generally written as $\operatorname {pq} (u,m)$ where $\mathrm {p}$ and $\mathrm {q}$ are any of the letters $\mathrm {c}$ , $\mathrm {s}$ , $\mathrm {n}$ , and $\mathrm {d}$ . Functions of the form $\operatorname {pp} (u,m)$ are trivially set to unity for notational completeness. The “major” functions are generally taken to be $\operatorname {cn} (u,m)$ , $\operatorname {sn} (u,m)$ and $\operatorname {dn} (u,m)$ from which all other functions can be derived and expressions are often written solely in terms of these three functions, however, various symmetries and generalizations are often most conveniently expressed using the full set. (This notation is due to Gudermann and Glaisher and is not Jacobi's original notation.)

Throughout this article, $\operatorname {pq} (u,t^{2})=\operatorname {pq} (u;t)$ .

The functions are notationally related to each other by the multiplication rule: (arguments suppressed)

$\operatorname {pq} \cdot \operatorname {p'q'} =\operatorname {pq'} \cdot \operatorname {p'q}$

from which other commonly used relationships can be derived:

${\frac {\operatorname {pr} }{\operatorname {qr} }}=\operatorname {pq}$ $\operatorname {pr} \cdot \operatorname {rq} =\operatorname {pq}$ ${\frac {1}{\operatorname {qp} }}=\operatorname {pq}$

The multiplication rule follows immediately from the identification of the elliptic functions with the Neville theta functions

$\operatorname {pq} (u,m)={\frac {\theta _{\operatorname {p} }(u,m)}{\theta _{\operatorname {q} }(u,m)}}$ Also note that:

$K(m)=K(k^{2})=\int _{0}^{1}{\frac {dt}{\sqrt {(1-t^{2})(1-mt^{2})}}}=\int _{0}^{1}{\frac {dt}{\sqrt {(1-t^{2})(1-k^{2}t^{2})}}}.$


## Definition in terms of inverses of elliptic integrals

There is a definition, relating the elliptic functions to the inverse of the incomplete elliptic integral of the first kind F . These functions take the parameters u and m as inputs. The $\varphi$ that satisfies

$u=F(\varphi |m)=\int _{0}^{\varphi }{\frac {\mathrm {d} \theta }{\sqrt {1-m\sin ^{2}\theta }}}$

is called the **Jacobi amplitude**:

$\operatorname {am} (u|m)=\varphi .$

In this framework, the *elliptic sine* sn *u* (Latin: *sinus amplitudinis*) is given by

$\operatorname {sn} (u|m)=\sin \operatorname {am} (u|m)$

and the *elliptic cosine* cn *u* (Latin: *cosinus amplitudinis*) is given by

$\operatorname {cn} (u|m)=\cos \operatorname {am} (u|m)$

and the *delta amplitude* dn *u* (Latin: *delta amplitudinis*)

$\operatorname {dn} (u|m)={\frac {\mathrm {d} }{\mathrm {d} u}}\operatorname {am} (u|m).$ In the above, the value m is a free parameter, usually taken to be real such that $0\leq m\leq 1$ (but can be complex in general), and so the elliptic functions can be thought of as being given by two variables, u and the parameter  m . The remaining nine elliptic functions are easily built from the above three ( $\operatorname {sn}$ , $\operatorname {cn}$ , $\operatorname {dn}$ ), and are given in a section below. Note that when $\varphi =\pi /2$ , that u then equals the quarter period  K .

In the most general setting, $\operatorname {am} (u|m)$ is a multivalued function (in u ) with infinitely many logarithmic branch points (the branches differ by integer multiples of $2\pi$ ), namely the points $2sK(m)+(4t+1)K(1-m)i$ and $2sK(m)+(4t+3)K(1-m)i$ where $s,t\in \mathbb {Z}$ . This multivalued function can be made single-valued by cutting the complex plane along the line segments joining these branch points (the cutting can be done in non-equivalent ways, giving non-equivalent single-valued functions), thus making $\operatorname {am} (u|m)$ analytic everywhere except on the branch cuts. In contrast, $\sin \operatorname {am} (u|m)$ and other elliptic functions have no branch points, give consistent values for every branch of $\operatorname {am}$ , and are meromorphic in the whole complex plane. Since every elliptic function is meromorphic in the whole complex plane (by definition), $\operatorname {am} (u|m)$ (when considered as a single-valued function) is not an elliptic function.

However, a particular cutting for $\operatorname {am} (u|m)$ can be made in the u -plane by line segments from $2sK(m)+(4t+1)K(1-m)i$ to $2sK(m)+(4t+3)K(1-m)i$ with $s,t\in \mathbb {Z}$ ; then it only remains to define $\operatorname {am} (u|m)$ at the branch cuts by continuity from some direction. Then $\operatorname {am} (u|m)$ becomes single-valued and singly-periodic in u with the minimal period $4iK(1-m)$ and it has singularities at the logarithmic branch points mentioned above. If $m\in \mathbb {R}$ and $m\leq 1$ , $\operatorname {am} (u|m)$ is continuous in u on the real line. When $m>1$ , the branch cuts of $\operatorname {am} (u|m)$ in the u -plane cross the real line at $2(2s+1)K(1/m)/{\sqrt {m}}$ for $s\in \mathbb {Z}$ ; therefore for $m>1$ , $\operatorname {am} (u|m)$ is not continuous in u on the real line and jumps by $2\pi$ on the discontinuities.

But defining $\operatorname {am} (u|m)$ this way gives rise to very complicated branch cuts in the m -plane (*not* the u -plane); they have not been fully described as of yet.

Let $E(\varphi |m)=\int _{0}^{\varphi }{\sqrt {1-m\sin ^{2}\theta }}\,\mathrm {d} \theta$ be the incomplete elliptic integral of the second kind with parameter m .

Then the **Jacobi epsilon** function can be defined as ${\mathcal {E}}(u|m)=E(\operatorname {am} (u|m)|m)$ for $u\in \mathbb {R}$ and $0<m<1$ and by analytic continuation in each of the variables otherwise: the Jacobi epsilon function is meromorphic in the whole complex plane (in both u and m ). Alternatively, throughout both the u -plane and m -plane, ${\mathcal {E}}(u|m)=\int _{0}^{u}\operatorname {dn} ^{2}(t|m)\,\mathrm {d} t;$ ${\mathcal {E}}$ is well-defined in this way because all residues of $t\mapsto \operatorname {dn} (t|m)^{2}$ are zero, so the integral is path-independent. So the Jacobi epsilon relates the incomplete elliptic integral of the first kind to the incomplete elliptic integral of the second kind: $E(\varphi |m)={\mathcal {E}}(F(\varphi |m)|m).$ The Jacobi epsilon function is not an elliptic function, but it appears when differentiating the Jacobi elliptic functions with respect to the parameter.

The **Jacobi zn** function is defined by $\operatorname {zn} (u|m)={\mathcal {E}}(u|m)-{\frac {E(m)}{K(m)}}u.$ It is a singly periodic function which is meromorphic in u , but not in m (due to the branch cuts of E and K ). Its minimal period in u is $2K(m)$ . It is related to the Jacobi zeta function by $Z(\varphi |m)=\operatorname {zn} (F(\varphi |m)|m).$

Historically, the Jacobi elliptic functions were first defined by using the amplitude. In more modern texts on elliptic functions, the Jacobi elliptic functions are defined by other means, for example by ratios of theta functions (see below), and the amplitude is ignored.

In modern terms, the relation to elliptic integrals would be expressed by $\operatorname {sn} (F(\varphi |m)|m)=\sin \varphi$ (or $\operatorname {cn} (F(\varphi |m)|m)=\cos \varphi$ ) instead of $\operatorname {am} (F(\varphi |m)|m)=\varphi$ .


## Definition as trigonometry: the Jacobi ellipse

$\cos \varphi ,\,\sin \varphi$ are defined on the unit circle with radius $r=1$ and angle $\varphi =$ arc length of the unit circle measured from the positive *x*-axis. Similarly, Jacobi elliptic functions are defined on the unit ellipse with $a=1$ and $b\geq 1$ . Let

${\begin{aligned}&x^{2}+{\frac {y^{2}}{b^{2}}}=1,\quad m=1-{\frac {1}{b^{2}}},\\&x=r\cos \varphi ,\quad y=r\sin \varphi .\end{aligned}}$

Then $0\leq m<1$ and

$r(\varphi ,m)={\frac {1}{\sqrt {1-m\sin ^{2}\varphi }}}\,.$

For each angle $\varphi$ the parameter $u=u(\varphi ,m)=\int _{0}^{\varphi }r(\theta ,m)\,d\theta$ (the incomplete elliptic integral of the first kind) is computed. On the unit circle ( $a=b=1$ ), u would be an arc length. However, the relation of u to the arc length of an ellipse is more complicated.

Let $P=(x,y)=(r\cos \varphi ,r\sin \varphi )$ be a point on the ellipse, and let $P'=(x',y')=(\cos \varphi ,\sin \varphi )$ be the point where the unit circle intersects the line between P and the origin O . Then the familiar relations from the unit circle

$x'=\cos \varphi ,\quad y'=\sin \varphi$

read for the ellipse

$x'=\operatorname {cn} (u,m),\quad y'=\operatorname {sn} (u,m).$

So the projections of the intersection point $P'$ of the line $OP$ with the unit circle on the *x*- and *y*-axes are simply $\operatorname {cn} (u,m)$ and $\operatorname {sn} (u,m)$ . These projections may be interpreted as 'definition as trigonometry'. In short,

$\operatorname {cn} (u,m)={\frac {x}{r(\varphi ,m)}},\quad \operatorname {sn} (u,m)={\frac {y}{r(\varphi ,m)}},\quad \operatorname {dn} (u,m)={\frac {1}{r(\varphi ,m)}}.$

For the x and y values of the point P with u and parameter m we get, by inserting the relation

$r(\varphi ,m)={\frac {1}{\operatorname {dn} (u,m)}}$

into $x=r(\varphi ,m)\cos \varphi$ and $y=r(\varphi ,m)\sin \varphi$ , we find

$x={\frac {\operatorname {cn} (u,m)}{\operatorname {dn} (u,m)}},\quad y={\frac {\operatorname {sn} (u,m)}{\operatorname {dn} (u,m)}}.$

The latter relations for the *x*- and *y*-coordinates of points on the unit ellipse may be considered as generalization of the relations $x=\cos \varphi$ and $y=\sin \varphi$ for the coordinates of points on the unit circle.

The following table summarizes the expressions for all Jacobi elliptic functions pq(u,m) in the variables (*x*,*y*,*r*) and (*φ*,dn) with ${\textstyle r={\sqrt {x^{2}+y^{2}}}}$ .

|   | q |   |   |   |
|---|---|---|---|---|
| c | s | n | d |   |
| p |   |   |   |   |
| c | 1 | $x/y=\cot(\varphi )$ | $x/r=\cos(\varphi )$ | $x=\cos(\varphi )/\operatorname {dn}$ |
| s | $y/x=\tan(\varphi )$ | 1 | $y/r=\sin(\varphi )$ | $y=\sin(\varphi )/\operatorname {dn}$ |
| n | $r/x=\sec(\varphi )$ | $r/y=\csc(\varphi )$ | 1 | $r=1/\operatorname {dn}$ |
| d | $1/x=\sec(\varphi )\operatorname {dn}$ | $1/y=\csc(\varphi )\operatorname {dn}$ | $1/r=\operatorname {dn}$ | 1 |


## Definition in terms of the Jacobi theta functions

### Using elliptic integrals

Equivalently, Jacobi's elliptic functions can be defined in terms of the theta functions. With $z,\tau \in \mathbb {C}$ such that $\operatorname {Im} \tau >0$ , let

$\theta _{1}(z|\tau )=\displaystyle \sum _{n=-\infty }^{\infty }(-1)^{n-{\frac {1}{2}}}e^{(2n+1)iz+\pi i\tau \left(n+{\frac {1}{2}}\right)^{2}},$ $\theta _{2}(z|\tau )=\displaystyle \sum _{n=-\infty }^{\infty }e^{(2n+1)iz+\pi i\tau \left(n+{\frac {1}{2}}\right)^{2}},$ $\theta _{3}(z|\tau )=\displaystyle \sum _{n=-\infty }^{\infty }e^{2niz+\pi i\tau n^{2}},$ $\theta _{4}(z|\tau )=\displaystyle \sum _{n=-\infty }^{\infty }(-1)^{n}e^{2niz+\pi i\tau n^{2}}$ and let $\theta _{2}(\tau )=\theta _{2}(0|\tau )$ , $\theta _{3}(\tau )=\theta _{3}(0|\tau )$ , $\theta _{4}(\tau )=\theta _{4}(0|\tau )$ . Then with $K=K(m)$ , $K'=K(1-m)$ , $\zeta =\pi u/(2K)$ and $\tau =iK'/K$ ,

${\begin{aligned}\operatorname {sn} (u,m)&={\frac {\theta _{3}(\tau )\theta _{1}(\zeta |\tau )}{\theta _{2}(\tau )\theta _{4}(\zeta |\tau )}},\\\operatorname {cn} (u,m)&={\frac {\theta _{4}(\tau )\theta _{2}(\zeta |\tau )}{\theta _{2}(\tau )\theta _{4}(\zeta |\tau )}},\\\operatorname {dn} (u,m)&={\frac {\theta _{4}(\tau )\theta _{3}(\zeta |\tau )}{\theta _{3}(\tau )\theta _{4}(\zeta |\tau )}}.\end{aligned}}$

The Jacobi zn function can be expressed by theta functions as well: ${\begin{aligned}\operatorname {zn} (u,m)&={\frac {\pi }{2K}}{\frac {\theta _{4}'(\zeta |\tau )}{\theta _{4}(\zeta |\tau )}}\\&={\frac {\pi }{2K}}{\frac {\theta _{3}'(\zeta |\tau )}{\theta _{3}(\zeta |\tau )}}+m{\frac {\operatorname {sn} (u,m)\operatorname {cn} (u,m)}{\operatorname {dn} (u,m)}}\\&={\frac {\pi }{2K}}{\frac {\theta _{2}'(\zeta |\tau )}{\theta _{2}(\zeta |\tau )}}+{\frac {\operatorname {dn} (u,m)\operatorname {sn} (u,m)}{\operatorname {cn} (u,m)}}\\&={\frac {\pi }{2K}}{\frac {\theta _{1}'(\zeta |\tau )}{\theta _{1}(\zeta |\tau )}}-{\frac {\operatorname {cn} (u,m)\operatorname {dn} (u,m)}{\operatorname {sn} (u,m)}}\end{aligned}}$ where ' denotes the partial derivative with respect to the first variable.

### Using modular inversion

In fact, the definition of the Jacobi elliptic functions in Whittaker & Watson is stated a little bit differently than the one given above (but it's equivalent to it) and relies on modular inversion: The function $\lambda$ , defined by

$\lambda (\tau )={\frac {\theta _{2}(\tau )^{4}}{\theta _{3}(\tau )^{4}}},$ assumes every value in $\mathbb {C} -\{0,1\}$ *once and only once* in $F_{1}-(\partial F_{1}\cap \{\tau \in \mathbb {H} :\operatorname {Re} \tau <0\})$ where $\mathbb {H}$ is the upper half-plane in the complex plane, $\partial F_{1}$ is the boundary of $F_{1}$ and $F_{1}=\{\tau \in \mathbb {H} :\left|\operatorname {Re} \tau \right|\leq 1,\left|\operatorname {Re} (1/\tau )\right|\leq 1\}.$ In this way, each $m\,{\overset {\text{def}}{=}}\,\lambda (\tau )\in \mathbb {C} -\{0,1\}$ can be associated with *one and only one* $\tau$ . Then Whittaker & Watson define the Jacobi elliptic functions by ${\begin{aligned}\operatorname {sn} (u,m)&={\frac {\theta _{3}(\tau )\theta _{1}(\zeta |\tau )}{\theta _{2}(\tau )\theta _{4}(\zeta |\tau )}},\\\operatorname {cn} (u,m)&={\frac {\theta _{4}(\tau )\theta _{2}(\zeta |\tau )}{\theta _{2}(\tau )\theta _{4}(\zeta |\tau )}},\\\operatorname {dn} (u,m)&={\frac {\theta _{4}(\tau )\theta _{3}(\zeta |\tau )}{\theta _{3}(\tau )\theta _{4}(\zeta |\tau )}}\end{aligned}}$ where $\zeta =u/\theta _{3}(\tau )^{2}$ . In the book, they place an additional restriction on m (that $m\notin (-\infty ,0)\cup (1,\infty )$ ), but it is in fact not a necessary restriction (see the Cox reference). Also, if $m=0$ or $m=1$ , the Jacobi elliptic functions degenerate to non-elliptic functions which is described below.


## Definition in terms of Neville theta functions

The Jacobi elliptic functions can be defined very simply using the Neville theta functions:

$\operatorname {pq} (u,m)={\frac {\theta _{\operatorname {p} }(u,m)}{\theta _{\operatorname {q} }(u,m)}}$

Simplifications of complicated products of the Jacobi elliptic functions are often made easier using these identities.


## Jacobi transformations

### The Jacobi imaginary transformations

The Jacobi imaginary transformations relate various functions of the imaginary variable *i u* or, equivalently, relations between various values of the *m* parameter. In terms of the major functions:

$\operatorname {cn} (u,m)=\operatorname {nc} (i\,u,1\!-\!m)$ $\operatorname {sn} (u,m)=-i\operatorname {sc} (i\,u,1\!-\!m)$ $\operatorname {dn} (u,m)=\operatorname {dc} (i\,u,1\!-\!m)$

Using the multiplication rule, all other functions may be expressed in terms of the above three. The transformations may be generally written as $\operatorname {pq} (u,m)=\gamma _{\operatorname {pq} }\operatorname {pq} '(i\,u,1\!-\!m)$ . The following table gives the $\gamma _{\operatorname {pq} }\operatorname {pq} '(i\,u,1\!-\!m)$ for the specified pq(*u,m*). (The arguments $(i\,u,1\!-\!m)$ are suppressed)

|   | q |   |   |   |
|---|---|---|---|---|
| c | s | n | d |   |
| p |   |   |   |   |
| c | 1 | i ns | nc | nd |
| s | −*i* sn | 1 | −*i* sc | −*i* sd |
| n | cn | *i* cs | 1 | cd |
| d | dn | *i* ds | dc | 1 |

Since the hyperbolic trigonometric functions are proportional to the circular trigonometric functions with imaginary arguments, it follows that the Jacobi functions will yield the hyperbolic functions for m=1. In the figure, the Jacobi curve has degenerated to two vertical lines at *x* = 1 and *x* = −1.

### The Jacobi real transformations

The Jacobi real transformations yield expressions for the elliptic functions in terms with alternate values of *m*. The transformations may be generally written as $\operatorname {pq} (u,m)=\gamma _{\operatorname {pq} }\operatorname {pq} '(k\,u,1/m)$ . The following table gives the $\gamma _{\operatorname {pq} }\operatorname {pq} '(k\,u,1/m)$ for the specified pq(*u,m*). (The arguments $(k\,u,1/m)$ are suppressed)

|   | q |   |   |   |
|---|---|---|---|---|
| c | s | n | d |   |
| p |   |   |   |   |
| c | 1 | $k\operatorname {ds}$ | $\operatorname {dn}$ | $\operatorname {dc}$ |
| s | ${\frac {1}{k}}\operatorname {sd}$ | 1 | ${\frac {1}{k}}\operatorname {sn}$ | ${\frac {1}{k}}\operatorname {sc}$ |
| n | $\operatorname {nd}$ | $k\operatorname {ns}$ | 1 | $\operatorname {nc}$ |
| d | $\operatorname {cd}$ | $k\operatorname {cs}$ | $\operatorname {cn}$ | 1 |

### Other Jacobi transformations

Jacobi's real and imaginary transformations can be combined in various ways to yield three more simple transformations. The real and imaginary transformations are two transformations in a group (D3 or anharmonic group) of six transformations. If

$\mu _{R}(m)=1/m$

is the transformation for the *m* parameter in the real transformation, and

$\mu _{I}(m)=1-m=m'$

is the transformation of *m* in the imaginary transformation, then the other transformations can be built up by successive application of these two basic transformations, yielding only three more possibilities:

${\begin{aligned}\mu _{IR}(m)&=&\mu _{I}(\mu _{R}(m))&=&-m'/m\\\mu _{RI}(m)&=&\mu _{R}(\mu _{I}(m))&=&1/m'\\\mu _{RIR}(m)&=&\mu _{R}(\mu _{I}(\mu _{R}(m)))&=&-m/m'\end{aligned}}$

These five transformations, along with the identity transformation (*μ**U*(*m*) = *m*) yield the six-element group. With regard to the Jacobi elliptic functions, the general transformation can be expressed using just three functions:

$\operatorname {cs} (u,m)=\gamma _{i}\operatorname {cs'} (\gamma _{i}u,\mu _{i}(m))$ $\operatorname {ns} (u,m)=\gamma _{i}\operatorname {ns'} (\gamma _{i}u,\mu _{i}(m))$ $\operatorname {ds} (u,m)=\gamma _{i}\operatorname {ds'} (\gamma _{i}u,\mu _{i}(m))$

where *i* = U, I, IR, R, RI, or RIR, identifying the transformation, γi is a multiplication factor common to these three functions, and the prime indicates the transformed function. The other nine transformed functions can be built up from the above three. The reason the cs, ns, ds functions were chosen to represent the transformation is that the other functions will be ratios of these three (except for their inverses) and the multiplication factors will cancel.

The following table lists the multiplication factors for the three ps functions, the transformed *m*'s, and the transformed function names for each of the six transformations. (As usual, *k*2 = *m*, 1 − *k*2 = *k*12 = *m*′ and the arguments ( $\gamma _{i}u,\mu _{i}(m)$ ) are suppressed)

| Transformation i | $\gamma _{i}$ | $\mu _{i}(m)$ | cs' | ns' | ds' |
|---|---|---|---|---|---|
| U | 1 | m | cs | ns | ds |
| I | i | m' | ns | cs | ds |
| IR | i k | −m'/m | ds | cs | ns |
| R | k | 1/m | ds | ns | cs |
| RI | i k1 | 1/m' | ns | ds | cs |
| RIR | k1 | −m/m' | cs | ds | ns |

Thus, for example, we may build the following table for the RIR transformation. The transformation is generally written $\operatorname {pq} (u,m)=\gamma _{\operatorname {pq} }\,\operatorname {pq'} (k'\,u,-m/m')$ (The arguments $(k'\,u,-m/m')$ are suppressed)

|   | q |   |   |   |
|---|---|---|---|---|
| c | s | n | d |   |
| p |   |   |   |   |
| c | 1 | k' cs | cd | cn |
| s | ${\frac {1}{k'}}$ sc | 1 | ${\frac {1}{k'}}$ sd | ${\frac {1}{k'}}$ sn |
| n | dc | $k'$ ds | 1 | dn |
| d | nc | $k'$ ns | nd | 1 |

The value of the Jacobi transformations is that any set of Jacobi elliptic functions with any real-valued parameter *m* can be converted into another set for which $0<m\leq 1/2$ and, for real values of *u*, the function values will be real.

### Amplitude transformations

In the following, the second variable is suppressed and is equal to m :

$\sin(\operatorname {am} (u+v)+\operatorname {am} (u-v))={\frac {2\operatorname {sn} u\operatorname {cn} u\operatorname {dn} v}{1-m\operatorname {sn} ^{2}u\operatorname {sn} ^{2}v}},$ $\cos(\operatorname {am} (u+v)-\operatorname {am} (u-v))={\dfrac {\operatorname {cn} ^{2}v-\operatorname {sn} ^{2}v\operatorname {dn} ^{2}u}{1-m\operatorname {sn} ^{2}u\operatorname {sn} ^{2}v}}$ where both identities are valid for all $u,v,m\in \mathbb {C}$ such that both sides are well-defined.

With

$m_{1}=\left({\frac {1-{\sqrt {m'}}}{1+{\sqrt {m'}}}}\right)^{2},$

we have

$\cos(\operatorname {am} (u,m)+\operatorname {am} (K-u,m))=-\operatorname {sn} ((1-{\sqrt {m'}})u,1/m_{1}),$ $\sin(\operatorname {am} ({\sqrt {m'}}u,-m/m')+\operatorname {am} ((1-{\sqrt {m'}})u,1/m_{1}))=\operatorname {sn} (u,m),$ $\sin(\operatorname {am} ((1+{\sqrt {m'}})u,m_{1})+\operatorname {am} ((1-{\sqrt {m'}})u,1/m_{1}))=\sin(2\operatorname {am} (u,m))$

where all the identities are valid for all $u,m\in \mathbb {C}$ such that both sides are well-defined.


## The Jacobi hyperbola

Introducing complex numbers, our ellipse has an associated hyperbola:

$x^{2}-{\frac {y^{2}}{b^{2}}}=1$ from applying Jacobi's imaginary transformation to the elliptic functions in the above equation for *x* and *y*.

$x={\frac {1}{\operatorname {dn} (u,1-m)}},\quad y={\frac {\operatorname {sn} (u,1-m)}{\operatorname {dn} (u,1-m)}}$

It follows that we can put $x=\operatorname {dn} (u,1-m),y=\operatorname {sn} (u,1-m)$ . So our ellipse has a dual ellipse with m replaced by 1-m. This leads to the complex torus mentioned in the Introduction. Generally, m may be a complex number, but when m is real and m<0, the curve is an ellipse with major axis in the x direction. At m=0 the curve is a circle, and for 0<m<1, the curve is an ellipse with major axis in the y direction. At *m* = 1, the curve degenerates into two vertical lines at *x* = ±1. For *m* > 1, the curve is a hyperbola. When *m* is complex but not real, *x* or *y* or both are complex and the curve cannot be described on a real *x*-*y* diagram.


## Minor functions

Reversing the order of the two letters of the function name results in the reciprocals of the three functions above:

$\operatorname {ns} (u)={\frac {1}{\operatorname {sn} (u)}},\qquad \operatorname {nc} (u)={\frac {1}{\operatorname {cn} (u)}},\qquad \operatorname {nd} (u)={\frac {1}{\operatorname {dn} (u)}}.$

Similarly, the ratios of the three primary functions correspond to the first letter of the numerator followed by the first letter of the denominator:

${\begin{aligned}\operatorname {sc} (u)&={\frac {\operatorname {sn} (u)}{\operatorname {cn} (u)}},&\operatorname {sd} (u)&={\frac {\operatorname {sn} (u)}{\operatorname {dn} (u)}},&\operatorname {dc} (u)&={\frac {\operatorname {dn} (u)}{\operatorname {cn} (u)}},\\[1ex]\operatorname {ds} (u)&={\frac {\operatorname {dn} (u)}{\operatorname {sn} (u)}},&\operatorname {cs} (u)&={\frac {\operatorname {cn} (u)}{\operatorname {sn} (u)}},&\operatorname {cd} (u)&={\frac {\operatorname {cn} (u)}{\operatorname {dn} (u)}}.\end{aligned}}$ More compactly, we have

$\operatorname {pq} (u)={\frac {\operatorname {pn} (u)}{\operatorname {qn} (u)}}$

where p and q are any of the letters s, c, d.


## Periodicity, poles, and residues

In the complex plane of the argument *u*, the Jacobi elliptic functions form a repeating pattern of poles (and zeroes). The residues of the poles all have the same absolute value, differing only in sign. Each function pq(*u*,*m*) has an "inverse function" (in the multiplicative sense) qp(*u*,*m*) in which the positions of the poles and zeroes are exchanged. The periods of repetition are generally different in the real and imaginary directions, hence the use of the term "doubly periodic" to describe them.

For the Jacobi amplitude and the Jacobi epsilon function: $\operatorname {am} (u+2K,m)=\operatorname {am} (u,m)+\pi ,$ $\operatorname {am} (u+4iK',m)=\operatorname {am} (u,m),$ ${\mathcal {E}}(u+2K,m)={\mathcal {E}}(u,m)+2E,$ ${\mathcal {E}}(u+2iK',m)={\mathcal {E}}(u,m)+2iE{\frac {K'}{K}}-{\frac {\pi i}{K}}$ where $E(m)$ is the complete elliptic integral of the second kind with parameter m .

The double periodicity of the Jacobi elliptic functions may be expressed as:

$\operatorname {pq} (u+2\alpha K(m)+2i\beta K(1-m)\,,\,m)=(-1)^{\gamma }\operatorname {pq} (u,m)$

where *α* and *β* are any pair of integers. *K*(⋅) is the complete elliptic integral of the first kind, also known as the quarter period. The power of negative unity (*γ*) is given in the following table:

|   | q |   |   |   |
|---|---|---|---|---|
| c | s | n | d |   |
| p |   |   |   |   |
| c | 0 | β | α + β | α |
| s | β | 0 | α | α + β |
| n | α + β | α | 0 | β |
| d | α | α + β | β | 0 |

When the factor (−1)*γ* is equal to −1, the equation expresses quasi-periodicity. When it is equal to unity, it expresses full periodicity. It can be seen, for example, that for the entries containing only α when α is even, full periodicity is expressed by the above equation, and the function has full periods of 4*K*(*m*) and 2*iK*(1 − *m*). Likewise, functions with entries containing only *β* have full periods of 2K(m) and 4*iK*(1 − *m*), while those with α + β have full periods of 4*K*(*m*) and 4*iK*(1 − *m*).

In the diagram on the right, which plots one repeating unit for each function, indicating phase along with the location of poles and zeroes, a number of regularities can be noted: The inverse of each function is opposite the diagonal, and has the same size unit cell, with poles and zeroes exchanged. The pole and zero arrangement in the auxiliary rectangle formed by (0,0), (*K*,0), (0,*K*′) and (*K*,*K*′) are in accordance with the description of the pole and zero placement described in the introduction above. Also, the size of the white ovals indicating poles are a rough measure of the absolute value of the residue for that pole. The residues of the poles closest to the origin in the figure (i.e. in the auxiliary rectangle) are listed in the following table:

|   | q |   |   |   |
|---|---|---|---|---|
| c | s | n | d |   |
| p |   |   |   |   |
| c |   | 1 | $-{\frac {i}{k}}$ | $-{\frac {1}{k}}$ |
| s | $-{\frac {1}{k'}}$ |   | ${\frac {1}{k}}$ | $-{\frac {i}{k\,k'}}$ |
| n | $-{\frac {1}{k'}}$ | 1 |   | $-{\frac {i}{k'}}$ |
| d | -1 | 1 | $-i$ |   |

When applicable, poles displaced above by 2*K* or displaced to the right by 2*K*′ have the same value but with signs reversed, while those diagonally opposite have the same value. Note that poles and zeroes on the left and lower edges are considered part of the unit cell, while those on the upper and right edges are not.

The information about poles can in fact be used to characterize the Jacobi elliptic functions:

The function $u\mapsto \operatorname {sn} (u,m)$ is the unique elliptic function having simple poles at $2rK+(2s+1)iK'$ (with $r,s\in \mathbb {Z}$ ) with residues $(-1)^{r}/{\sqrt {m}}$ taking the value 0 at 0 .

The function $u\mapsto \operatorname {cn} (u,m)$ is the unique elliptic function having simple poles at $2rK+(2s+1)iK'$ (with $r,s\in \mathbb {Z}$ ) with residues $(-1)^{r+s-1}i/{\sqrt {m}}$ taking the value 1 at 0 .

The function $u\mapsto \operatorname {dn} (u,m)$ is the unique elliptic function having simple poles at $2rK+(2s+1)iK'$ (with $r,s\in \mathbb {Z}$ ) with residues $(-1)^{s-1}i$ taking the value 1 at 0 .


## Special values

Setting $m=-1$ gives the lemniscate elliptic functions $\operatorname {sl}$ and $\operatorname {cl}$ :

$\operatorname {sl} u=\operatorname {sn} (u,-1),\quad \operatorname {cl} u=\operatorname {cd} (u,-1)={\frac {\operatorname {cn} (u,-1)}{\operatorname {dn} (u,-1)}}.$

When $m=0$ or $m=1$ , the Jacobi elliptic functions are reduced to non-elliptic functions:

| Function | *m* = 0 | *m* = 1 |
|---|---|---|
| $\operatorname {sn} (u,m)$ | $\sin u$ | $\tanh u$ |
| $\operatorname {cn} (u,m)$ | $\cos u$ | $\operatorname {sech} u$ |
| $\operatorname {dn} (u,m)$ | 1 | $\operatorname {sech} u$ |
| $\operatorname {ns} (u,m)$ | $\csc u$ | $\coth u$ |
| $\operatorname {nc} (u,m)$ | $\sec u$ | $\cosh u$ |
| $\operatorname {nd} (u,m)$ | 1 | $\cosh u$ |
| $\operatorname {sd} (u,m)$ | $\sin u$ | $\sinh u$ |
| $\operatorname {cd} (u,m)$ | $\cos u$ | 1 |
| $\operatorname {cs} (u,m)$ | $\cot u$ | $\operatorname {csch} u$ |
| $\operatorname {ds} (u,m)$ | $\csc u$ | $\operatorname {csch} u$ |
| $\operatorname {dc} (u,m)$ | $\sec u$ | 1 |
| $\operatorname {sc} (u,m)$ | $\tan u$ | $\sinh u$ |

For the Jacobi amplitude, $\operatorname {am} (u,0)=u$ and $\operatorname {am} (u,1)=\operatorname {gd} u$ where $\operatorname {gd}$ is the Gudermannian function.

In general if neither of p,q is d then $\operatorname {pq} (u,1)=\operatorname {pq} (\operatorname {gd} (u),0)$ .


## Identities

### Half angle formula

$\operatorname {sn} \left({\frac {u}{2}},m\right)=\pm {\sqrt {\frac {1-\operatorname {cn} (u,m)}{1+\operatorname {dn} (u,m)}}}$ $\operatorname {cn} \left({\frac {u}{2}},m\right)=\pm {\sqrt {\frac {\operatorname {cn} (u,m)+\operatorname {dn} (u,m)}{1+\operatorname {dn} (u,m)}}}$ $\operatorname {dn} \left({\frac {u}{2}},m\right)=\pm {\sqrt {\frac {m'+\operatorname {dn} (u,m)+m\operatorname {cn} (u,m)}{1+\operatorname {dn} (u,m)}}}$

### K formulas

**Half K formula**

$\operatorname {sn} \left[{\tfrac {1}{2}}K(k);k\right]={\frac {\sqrt {2}}{{\sqrt {1+k}}+{\sqrt {1-k}}}}$

$\operatorname {cn} \left[{\tfrac {1}{2}}K(k);k\right]={\frac {{\sqrt {2}}\,{\sqrt[{4}]{1-k^{2}}}}{{\sqrt {1+k}}+{\sqrt {1-k}}}}$

$\operatorname {dn} \left[{\tfrac {1}{2}}K(k);k\right]={\sqrt[{4}]{1-k^{2}}}$

**Third K formula**

$\operatorname {sn} \left[{\frac {1}{3}}K\left({\frac {x^{3}}{{\sqrt {x^{6}+1}}+1}}\right);{\frac {x^{3}}{{\sqrt {x^{6}+1}}+1}}\right]={\frac {{\sqrt {2{\sqrt {x^{4}-x^{2}+1}}-x^{2}+2}}+{\sqrt {x^{2}+1}}-1}{{\sqrt {2{\sqrt {x^{4}-x^{2}+1}}-x^{2}+2}}+{\sqrt {x^{2}+1}}+1}}$

To get *x*3, we take the tangent of twice the arctangent of the modulus.

Also this equation leads to the sn-value of the third of *K*:

$k^{2}s^{4}-2k^{2}s^{3}+2s-1=0$

$s=\operatorname {sn} \left[{\tfrac {1}{3}}K(k);k\right]$

These equations lead to the other values of the Jacobi-Functions:

$\operatorname {cn} \left[{\tfrac {2}{3}}K(k);k\right]=1-\operatorname {sn} \left[{\tfrac {1}{3}}K(k);k\right]$

$\operatorname {dn} \left[{\tfrac {2}{3}}K(k);k\right]=1/\operatorname {sn} \left[{\tfrac {1}{3}}K(k);k\right]-1$

**Fifth K formula**

Following equation has following solution:

$4k^{2}x^{6}+8k^{2}x^{5}+2(1-k^{2})^{2}x-(1-k^{2})^{2}=0$

$x={\frac {1}{2}}-{\frac {1}{2}}k^{2}\operatorname {sn} \left[{\tfrac {2}{5}}K(k);k\right]^{2}\operatorname {sn} \left[{\tfrac {4}{5}}K(k);k\right]^{2}={\frac {\operatorname {sn} \left[{\frac {4}{5}}K(k);k\right]^{2}-\operatorname {sn} \left[{\frac {2}{5}}K(k);k\right]^{2}}{2\operatorname {sn} \left[{\frac {2}{5}}K(k);k\right]\operatorname {sn} \left[{\frac {4}{5}}K(k);k\right]}}$

To get the sn-values, we put the solution x into following expressions:

$\operatorname {sn} \left[{\tfrac {2}{5}}K(k);k\right]=(1+k^{2})^{-1/2}{\sqrt {2(1-x-x^{2})(x^{2}+1-x{\sqrt {x^{2}+1}})}}$

$\operatorname {sn} \left[{\tfrac {4}{5}}K(k);k\right]=(1+k^{2})^{-1/2}{\sqrt {2(1-x-x^{2})(x^{2}+1+x{\sqrt {x^{2}+1}})}}$

### Relations between squares of the functions

Relations between squares of the functions can be derived from two basic relationships (Arguments (*u*,*m*) suppressed): $\operatorname {cn} ^{2}+\operatorname {sn} ^{2}=1$ $\operatorname {cn} ^{2}+m'\operatorname {sn} ^{2}=\operatorname {dn} ^{2}$ where *m + m'*= 1. Multiplying by any function of the form *nq* yields more general equations:

$\operatorname {cq} ^{2}+\operatorname {sq} ^{2}=\operatorname {nq} ^{2}$ $\operatorname {cq} ^{2}{}+m'\operatorname {sq} ^{2}=\operatorname {dq} ^{2}$

With *q* = *d*, these correspond trigonometrically to the equations for the unit circle ( $x^{2}+y^{2}=r^{2}$ ) and the unit ellipse ( $x^{2}{}+m'y^{2}=1$ ), with *x* = *cd*, *y* = *sd* and *r* = *nd*. Using the multiplication rule, other relationships may be derived. For example:

$-\operatorname {dn} ^{2}{}+m'=-m\operatorname {cn} ^{2}=m\operatorname {sn} ^{2}-m$

$-m'\operatorname {nd} ^{2}{}+m'=-mm'\operatorname {sd} ^{2}=m\operatorname {cd} ^{2}-m$

$m'\operatorname {sc} ^{2}{}+m'=m'\operatorname {nc} ^{2}=\operatorname {dc} ^{2}-m$

$\operatorname {cs} ^{2}{}+m'=\operatorname {ds} ^{2}=\operatorname {ns} ^{2}-m$

### Addition theorems

The functions satisfy the two square relations (dependence on *m* suppressed) $\operatorname {cn} ^{2}(u)+\operatorname {sn} ^{2}(u)=1,\,$

$\operatorname {dn} ^{2}(u)+m\operatorname {sn} ^{2}(u)=1.\,$

From this we see that (cn, sn, dn) parametrizes an elliptic curve which is the intersection of the two quadrics defined by the above two equations. We now may define a group law for points on this curve by the addition formulas for the Jacobi functions

${\begin{aligned}\operatorname {cn} (x+y)&={\operatorname {cn} (x)\operatorname {cn} (y)-\operatorname {sn} (x)\operatorname {sn} (y)\operatorname {dn} (x)\operatorname {dn} (y) \over {1-m\operatorname {sn} ^{2}(x)\operatorname {sn} ^{2}(y)}},\\[8pt]\operatorname {sn} (x+y)&={\operatorname {sn} (x)\operatorname {cn} (y)\operatorname {dn} (y)+\operatorname {sn} (y)\operatorname {cn} (x)\operatorname {dn} (x) \over {1-m\operatorname {sn} ^{2}(x)\operatorname {sn} ^{2}(y)}},\\[8pt]\operatorname {dn} (x+y)&={\operatorname {dn} (x)\operatorname {dn} (y)-m\operatorname {sn} (x)\operatorname {sn} (y)\operatorname {cn} (x)\operatorname {cn} (y) \over {1-m\operatorname {sn} ^{2}(x)\operatorname {sn} ^{2}(y)}}.\end{aligned}}$

The Jacobi epsilon and zn functions satisfy a quasi-addition theorem: ${\begin{aligned}{\mathcal {E}}(x+y,m)&={\mathcal {E}}(x,m)+{\mathcal {E}}(y,m)-m\operatorname {sn} (x,m)\operatorname {sn} (y,m)\operatorname {sn} (x+y,m),\\\operatorname {zn} (x+y,m)&=\operatorname {zn} (x,m)+\operatorname {zn} (y,m)-m\operatorname {sn} (x,m)\operatorname {sn} (y,m)\operatorname {sn} (x+y,m).\end{aligned}}$

Double angle formulae can be easily derived from the above equations by setting *x* = *y*. Half angle formulae are all of the form:

$\operatorname {pq} ({\tfrac {1}{2}}u,m)^{2}=f_{\mathrm {p} }/f_{\mathrm {q} }$

where: $f_{\mathrm {c} }=\operatorname {cn} (u,m)+\operatorname {dn} (u,m)$ $f_{\mathrm {s} }=1-\operatorname {cn} (u,m)$ $f_{\mathrm {n} }=1+\operatorname {dn} (u,m)$ $f_{\mathrm {d} }=(1+\operatorname {dn} (u,m))-m(1-\operatorname {cn} (u,m))$


## Jacobi elliptic functions as solutions of nonlinear ordinary differential equations

### Derivatives with respect to the first variable

The derivatives of the three basic Jacobi elliptic functions (with respect to the first variable, with m fixed) are: ${\frac {\mathrm {d} }{\mathrm {d} z}}\operatorname {sn} (z)=\operatorname {cn} (z)\operatorname {dn} (z),$ ${\frac {\mathrm {d} }{\mathrm {d} z}}\operatorname {cn} (z)=-\operatorname {sn} (z)\operatorname {dn} (z),$ ${\frac {\mathrm {d} }{\mathrm {d} z}}\operatorname {dn} (z)=-m\operatorname {sn} (z)\operatorname {cn} (z).$

These can be used to derive the derivatives of all other functions as shown in the table below (arguments (u,m) suppressed):

|   | q |   |   |   |
|---|---|---|---|---|
| c | s | n | d |   |
| p |   |   |   |   |
| c | 0 | −ds ns | −dn sn | −m' nd sd |
| s | dc nc | 0 | cn dn | cd nd |
| n | dc sc | −cs ds | 0 | *m* cd sd |
| d | m' nc sc | −cs ns | −*m* cn sn | 0 |

Also ${\frac {\mathrm {d} }{\mathrm {d} z}}{\mathcal {E}}(z)=\operatorname {dn} (z)^{2}.$

With the addition theorems above and for a given *m* with 0 < *m* < 1 the major functions are therefore solutions to the following nonlinear ordinary differential equations:

- $\operatorname {am} (x)$ solves the differential equations ${\frac {\mathrm {d} ^{2}y}{\mathrm {d} x^{2}}}+m\sin(y)\cos(y)=0$ and

$\left({\frac {\mathrm {d} y}{\mathrm {d} x}}\right)^{2}=1-m\sin(y)^{2}$ (for x not on a branch cut)

- $\operatorname {sn} (x)$ solves the differential equations ${\frac {\mathrm {d} ^{2}y}{\mathrm {d} x^{2}}}+(1+m)y-2my^{3}=0$ and $\left({\frac {\mathrm {d} y}{\mathrm {d} x}}\right)^{2}=(1-y^{2})(1-my^{2})$
- $\operatorname {cn} (x)$ solves the differential equations ${\frac {\mathrm {d} ^{2}y}{\mathrm {d} x^{2}}}+(1-2m)y+2my^{3}=0$ and $\left({\frac {\mathrm {d} y}{\mathrm {d} x}}\right)^{2}=(1-y^{2})(1-m+my^{2})$
- $\operatorname {dn} (x)$ solves the differential equations ${\frac {\mathrm {d} ^{2}y}{\mathrm {d} x^{2}}}-(2-m)y+2y^{3}=0$ and $\left({\frac {\mathrm {d} y}{\mathrm {d} x}}\right)^{2}=(y^{2}-1)(1-m-y^{2})$

The function which exactly solves the pendulum differential equation, ${\frac {\mathrm {d} ^{2}\theta }{\mathrm {d} t^{2}}}+c\sin \theta =0,$ with initial angle $\theta _{0}$ and zero initial angular velocity is

${\begin{aligned}\theta &=2\arcsin({\sqrt {m}}\operatorname {cd} ({\sqrt {c}}t,m))\\&=2\operatorname {am} \left({\frac {1+{\sqrt {m}}}{2}}({\sqrt {c}}t+K),{\frac {4{\sqrt {m}}}{(1+{\sqrt {m}})^{2}}}\right)-2\operatorname {am} \left({\frac {1+{\sqrt {m}}}{2}}({\sqrt {c}}t-K),{\frac {4{\sqrt {m}}}{(1+{\sqrt {m}})^{2}}}\right)-\pi \end{aligned}}$ where $m=\sin(\theta _{0}/2)^{2}$ , $c>0$ and $t\in \mathbb {R}$ .

### Derivatives with respect to the second variable

With the first argument z fixed, the derivatives with respect to the second variable m are as follows:

${\begin{aligned}{\frac {\mathrm {d} }{\mathrm {d} m}}\operatorname {sn} (z)&={\frac {\operatorname {dn} (z)\operatorname {cn} (z)((1-m)z-{\mathcal {E}}(z)+m\operatorname {cd} (z)\operatorname {sn} (z))}{2m(1-m)}},\\{\frac {\mathrm {d} }{\mathrm {d} m}}\operatorname {cn} (z)&={\frac {\operatorname {sn} (z)\operatorname {dn} (z)((m-1)z+{\mathcal {E}}(z)-m\operatorname {sn} (z)\operatorname {cd} (z))}{2m(1-m)}},\\{\frac {\mathrm {d} }{\mathrm {d} m}}\operatorname {dn} (z)&={\frac {\operatorname {sn} (z)\operatorname {cn} (z)((m-1)z+{\mathcal {E}}(z)-\operatorname {dn} (z)\operatorname {sc} (z))}{2(1-m)}},\\{\frac {\mathrm {d} }{\mathrm {d} m}}{\mathcal {E}}(z)&={\frac {\operatorname {cn} (z)(\operatorname {sn} (z)\operatorname {dn} (z)-\operatorname {cn} (z){\mathcal {E}}(z))}{2(1-m)}}-{\frac {z}{2}}\operatorname {sn} (z)^{2}.\end{aligned}}$


## Expansion in terms of the nome

Let the nome be $q=\exp(-\pi K'(m)/K(m))=e^{i\pi \tau }$ , $\operatorname {Im} (\tau )>0$ , $m=k^{2}$ and let $v=\pi u/(2K(m))$ . Then the functions have expansions as Lambert series

$\operatorname {am} (u,m)={\frac {\pi u}{2K(m)}}+2\sum _{n=1}^{\infty }{\frac {q^{n}}{n(1+q^{2n})}}\sin(2nv),$

$\operatorname {sn} (u,m)={\frac {2\pi }{kK(m)}}\sum _{n=0}^{\infty }{\frac {q^{n+1/2}}{1-q^{2n+1}}}\sin((2n+1)v),$

$\operatorname {cn} (u,m)={\frac {2\pi }{kK(m)}}\sum _{n=0}^{\infty }{\frac {q^{n+1/2}}{1+q^{2n+1}}}\cos((2n+1)v),$

$\operatorname {dn} (u,m)={\frac {\pi }{2K(m)}}+{\frac {2\pi }{K(m)}}\sum _{n=1}^{\infty }{\frac {q^{n}}{1+q^{2n}}}\cos(2nv),$

$\operatorname {zn} (u,m)={\frac {2\pi }{K(m)}}\sum _{n=1}^{\infty }{\frac {q^{n}}{1-q^{2n}}}\sin(2nv)$

when $\left|\operatorname {Im} (u/K)\right|<\operatorname {Im} (iK'/K).$

Bivariate power series expansions have been published by Schett.


## Fast computation

The theta function ratios provide an efficient way of computing the Jacobi elliptic functions. There is an alternative method, based on the arithmetic-geometric mean and Landen's transformations:

Initialize $a_{0}=1,\,b_{0}={\sqrt {1-m}}$ where $0<m<1$ . Define $a_{n}={\frac {a_{n-1}+b_{n-1}}{2}},\,b_{n}={\sqrt {a_{n-1}b_{n-1}}},\,c_{n}={\frac {a_{n-1}-b_{n-1}}{2}}$ where $n\geq 1$ . Then define $\varphi _{N}=2^{N}a_{N}u$ for $u\in \mathbb {R}$ and a fixed $N\in \mathbb {N}$ . If $\varphi _{n-1}={\frac {1}{2}}\left(\varphi _{n}+\arcsin \left({\frac {c_{n}}{a_{n}}}\sin \varphi _{n}\right)\right)$ for $n\geq 1$ , then $\operatorname {am} (u,m)=\varphi _{0},\quad \operatorname {zn} (u,m)=\sum _{n=1}^{N}c_{n}\sin \varphi _{n}$ as $N\to \infty$ . This is notable for its rapid convergence. It is then trivial to compute all Jacobi elliptic functions from the Jacobi amplitude $\operatorname {am}$ on the real line.

In conjunction with the addition theorems for elliptic functions (which hold for complex numbers in general) and the Jacobi transformations, the method of computation described above can be used to compute all Jacobi elliptic functions in the whole complex plane.

Another method of fast computation of the Jacobi elliptic functions via the arithmetic–geometric mean, avoiding the computation of the Jacobi amplitude, is due to Herbert E. Salzer:

Let $0\leq m\leq 1,\,0\leq u\leq K(m),\,a_{0}=1,\,b_{0}={\sqrt {1-m}},$ $a_{n+1}={\frac {a_{n}+b_{n}}{2}},\,b_{n+1}={\sqrt {a_{n}b_{n}}},\,c_{n+1}={\frac {a_{n}-b_{n}}{2}}.$ Set ${\begin{aligned}y_{N}&={\frac {a_{N}}{\sin(a_{N}u)}}\\y_{N-1}&=y_{N}+{\frac {a_{N}c_{N}}{y_{N}}}\\y_{N-2}&=y_{N-1}+{\frac {a_{N-1}c_{N-1}}{y_{N-1}}}\\\vdots &=\vdots \\y_{0}&=y_{1}+{\frac {m}{4y_{1}}}.\end{aligned}}$ Then ${\begin{aligned}\operatorname {sn} (u,m)&={\frac {1}{y_{0}}}\\\operatorname {cn} (u,m)&={\sqrt {1-{\frac {1}{y_{0}^{2}}}}}\\\operatorname {dn} (u,m)&={\sqrt {1-{\frac {m}{y_{0}^{2}}}}}\end{aligned}}$ as $N\to \infty$ .

Yet, another method for a rapidly converging fast computation of the Jacobi elliptic sine function found in the literature is shown below.

Let:

${\begin{aligned}&a_{0}=u&b_{0}={\frac {1-{\sqrt {1-m}}}{1+{\sqrt {1-m}}}}\\&a_{1}={\frac {a_{0}}{1+b_{0}}}&b_{1}={\frac {1-{\sqrt {1-b_{0}^{2}}}}{1+{\sqrt {1-b_{0}^{2}}}}}\\&\vdots =\vdots &\vdots =\vdots \\&a_{n}={\frac {a_{n-1}}{1+b_{n-1}}}&b_{n}={\frac {1-{\sqrt {1-b_{n-1}^{2}}}}{1+{\sqrt {1-b_{n-1}^{2}}}}}\\\end{aligned}}$

Then set:

${\begin{aligned}y_{n+1}&=\sin(a_{n})\\y_{n}&={\frac {y_{n+1}(1+b_{n})}{1+y_{n+1}^{2}b_{n}}}\\\vdots &=\vdots \\y_{0}&={\frac {y_{1}(1+b_{0})}{1+y_{1}^{2}b_{0}}}\\\end{aligned}}$

Then:

$\operatorname {sn} (u,m)=y_{0}{\text{ as }}n\rightarrow \infty$ .


## Approximation in terms of hyperbolic functions

The Jacobi elliptic functions can be expanded in terms of the hyperbolic functions. When m is close to unity, such that $m'^{2}$ and higher powers of $m'$ can be neglected, we have:

- sn(*u*): $\operatorname {sn} (u,m)\approx \tanh(u)+{\frac {1}{4}}m'(\sinh(u)\cosh(u)-u)\operatorname {sech} ^{2}(u).$
- cn(*u*): $\operatorname {cn} (u,m)\approx \operatorname {sech} (u)-{\frac {1}{4}}m'(\sinh(u)\cosh(u)-u)\tanh(u)\operatorname {sech} (u).$
- dn(*u*): $\operatorname {dn} (u,m)\approx \operatorname {sech} (u)+{\frac {1}{4}}m'(\sinh(u)\cosh(u)+u)\tanh(u)\operatorname {sech} (u).$

For the Jacobi amplitude, $\operatorname {am} (u,m)\approx \operatorname {gd} (u)+{\frac {1}{4}}m'(\sinh(u)\cosh(u)-u)\operatorname {sech} (u).$
