---
title: "Montgomery curve"
source: https://en.wikipedia.org/wiki/Montgomery_curve
domain: elliptic-curve-cryptography
license: CC-BY-SA-4.0
tags: elliptic curve cryptography, elliptic curve, discrete logarithm, digital signature algorithm
fetched: 2026-07-02
---

# Montgomery curve

In mathematics, the **Montgomery curve** is a form of elliptic curve introduced by Peter L. Montgomery in 1987, different from the usual Weierstrass form. It is used for certain computations, and in particular in different cryptography applications.

## Definition

A Montgomery curve over a field *K* is defined by the equation

$M_{A,B}:By^{2}=x^{3}+Ax^{2}+x$

for *A*, *B* ∈ *K* such that *B*(*A*2 − 4) ≠ 0.

Generally this curve is considered over a finite field *K* (for example, over a finite field of *q* elements, *K* = **F***q*) with characteristic different from 2 and with *A* ≠ ±2 and *B* ≠ 0. Over such fields, the group order of the curve is always divisible by 4. Montgomery curves are also considered over the rationals with the same restrictions for *A* and *B*.

Every Montgomery curve has a point at $(0,0)$ .

## Montgomery arithmetic

It is possible to do some "operations" between the points of an elliptic curve: "adding" two points $P,Q$ consists of finding a third one R such that $R=P+Q$ ; "doubling" a point consists of computing $[2]P=P+P$ (For more information about operations see The group law) and below.

A point $P=(x,y)$ on the elliptic curve in the Montgomery form $By^{2}=x^{3}+Ax^{2}+x$ can be represented in Montgomery coordinates $P=(X:Z)$ , where $P=(X:Z)$ are projective coordinates and $x=X/Z$ for $Z\neq 0$ .

Notice that this kind of representation for a point loses information: indeed, in this case, there is no distinction between the affine points $(x,y)$ and $(x,-y)$ because they are both given by the point $(X:Z)$ . However, with this representation it is possible to obtain multiples of points, that is, given $P=(X:Z)$ , to compute $[n]P=(X_{n}:Z_{n})$ .

Now, considering the two points $P_{n}=[n]P=(X_{n}:Z_{n})$ and $P_{m}=[m]P=(X_{m}:Z_{m})$ : their sum is given by the point $P_{m+n}=P_{m}+P_{n}=(X_{m+n}:Z_{m+n})$ whose coordinates are:

$X_{m+n}=Z_{m-n}((X_{m}-Z_{m})(X_{n}+Z_{n})+(X_{m}+Z_{m})(X_{n}-Z_{n}))^{2}$

$Z_{m+n}=X_{m-n}((X_{m}-Z_{m})(X_{n}+Z_{n})-(X_{m}+Z_{m})(X_{n}-Z_{n}))^{2}$

If $m=n$ , then the operation becomes a "doubling"; the coordinates of $[2]P_{n}=P_{n}+P_{n}=P_{2n}=(X_{2n}:Z_{2n})$ are given by the following equations:

$4X_{n}Z_{n}=(X_{n}+Z_{n})^{2}-(X_{n}-Z_{n})^{2}$

$X_{2n}=(X_{n}+Z_{n})^{2}(X_{n}-Z_{n})^{2}$

$Z_{2n}=(4X_{n}Z_{n})((X_{n}-Z_{n})^{2}+((A+2)/4)(4X_{n}Z_{n}))$

The first operation considered above (addition) has a time-cost of 3**M**+2**S**, where **M** denotes the multiplication between two general elements of the field on which the elliptic curve is defined, while **S** denotes squaring of a general element of the field.

The second operation (doubling) has a time-cost of 2**M** + 2**S** + 1**D**, where **D** denotes the multiplication of a general element by a constant; notice that the constant is $(A+2)/4$ , so A can be chosen in order to have a small **D**.

## Algorithm and example

The following algorithm represents a doubling of a point $P_{1}=(X_{1}:Z_{1})$ on an elliptic curve in the Montgomery form.

It is assumed that $Z_{1}=1$ . The cost of this implementation is 1M + 2S + 1*A + 3add + 1*4. Here M denotes the multiplications required, S indicates the squarings, and a refers to the multiplication by A.

$XX_{1}=X_{1}^{2}\,$

$X_{2}=(XX_{1}-1)^{2}\,$

$Z_{2}=4X_{1}(XX_{1}+aX_{1}+1)\,$

### Example

Let $P_{1}=(2,{\sqrt {3}})$ be a point on the curve $2y^{2}=x^{3}-x^{2}+x$ . In coordinates $(X_{1}:Z_{1})$ , with $x_{1}=X_{1}/Z_{1}$ , $P_{1}=(2:1)$ .

Then:

$XX_{1}=X_{1}^{2}=4\,$

$X_{2}=(XX_{1}-1)^{2}=9\,$

$Z_{2}=4X_{1}(XX_{1}+AX_{1}+1)=24\,$

The result is the point $P_{2}=(X_{2}:Z_{2})=(9:24)$ such that $P_{2}=2P_{1}$ .

## Addition

Given two points $P_{1}=(x_{1},y_{1})$ , $P_{2}=(x_{2},y_{2})$ on the Montgomery curve $M_{A,B}$ in affine coordinates, the point $P_{3}=P_{1}+P_{2}$ represents, geometrically the third point of intersection between $M_{A,B}$ and the line passing through $P_{1}$ and $P_{2}$ . It is possible to find the coordinates $(x_{3},y_{3})$ of $P_{3}$ , in the following way:

1) consider a generic line $~y=lx+m$ in the affine plane and let it pass through $P_{1}$ and $P_{2}$ (impose the condition), in this way, one obtains $l={\frac {y_{2}-y_{1}}{x_{2}-x_{1}}}$ and $m=y_{1}-\left({\frac {y_{2}-y_{1}}{x_{2}-x_{1}}}\right)x_{1}$ ;

2) intersect the line with the curve $M_{A,B}$ , substituting the $~y$ variable in the curve equation with $~y=lx+m$ ; the following equation of third degree is obtained:

$x^{3}+(A-Bl^{2})x^{2}+(1-2Blm)x-Bm^{2}=0.$

As it has been observed before, this equation has three solutions that correspond to the $~x$ coordinates of $P_{1}$ , $P_{2}$ and $P_{3}$ . In particular this equation can be re-written as:

$(x-x_{1})(x-x_{2})(x-x_{3})=0$

3) Comparing the coefficients of the two identical equations given above, in particular the coefficients of the terms of second degree, one gets:

$-x_{1}-x_{2}-x_{3}=A-Bl^{2}$

.

So, $x_{3}$ can be written in terms of $x_{1}$ , $y_{1}$ , $x_{2}$ , $y_{2}$ , as:

$x_{3}=B\left({\frac {y_{2}-y_{1}}{x_{2}-x_{1}}}\right)^{2}-A-x_{1}-x_{2}.$

4) To find the $~y$ coordinate of the point $P_{3}$ it is sufficient to substitute the value $x_{3}$ in the line $~y=lx+m$ . Notice that this will not give the point $P_{3}$ directly. Indeed, with this method one find the coordinates of the point $~R$ such that $R+P_{1}+P_{2}=P_{\infty }$ , but if one needs the resulting point of the sum between $P_{1}$ and $P_{2}$ , then it is necessary to observe that: $R+P_{1}+P_{2}=P_{\infty }$ if and only if $-R=P_{1}+P_{2}$ . So, given the point $~R$ , it is necessary to find $~-R$ , but this can be done easily by changing the sign to the $~y$ coordinate of $~R$ . In other words, it will be necessary to change the sign of the $~y$ coordinate obtained by substituting the value $x_{3}$ in the equation of the line.

Resuming, the coordinates of the point $P_{3}=(x_{3},y_{3})$ , $P_{3}=P_{1}+P_{2}$ are:

$x_{3}={\frac {B(y_{2}-y_{1})^{2}}{(x_{2}-x_{1})^{2}}}-A-x_{1}-x_{2}$

$y_{3}={\frac {(2x_{1}+x_{2}+A)(y_{2}-y_{1})}{x_{2}-x_{1}}}-{\frac {B(y_{2}-y_{1})^{3}}{(x_{2}-x_{1})^{3}}}-y_{1}$

## Doubling

Given a point $P_{1}$ on the Montgomery curve $M_{A,B}$ , the point $[2]P_{1}$ represents geometrically the third point of intersection between the curve and the line tangent to $P_{1}$ ; so, to find the coordinates of the point $P_{3}=2P_{1}$ it is sufficient to follow the same method given in the addition formula; however, in this case, the line *y* = *lx* + *m* has to be tangent to the curve at $P_{1}$ , so, if $M_{A,B}:f(x,y)=0$ with

$f(x,y)=x^{3}+Ax^{2}+x-By^{2},$

then the value of *l*, which represents the slope of the line, is given by:

$l=-\left.{\frac {\partial f}{\partial x}}\right/{\frac {\partial f}{\partial y}}$

by the implicit function theorem.

So $l={\frac {3x_{1}^{2}+2Ax_{1}+1}{2By_{1}}}$ and the coordinates of the point $P_{3}$ , $P_{3}=2P_{1}$ are:

${\begin{aligned}x_{3}&=Bl^{2}-A-x_{1}-x_{1}={\frac {B(3x_{1}^{2}+2Ax_{1}+1)^{2}}{(2By_{1})^{2}}}-A-x_{1}-x_{1}\\y_{3}&=(2x_{1}+x_{1}+A)l-Bl^{3}-y_{1}\\&={\frac {(2x_{1}+x_{1}+A)(3{x_{1}}^{2}+2Ax_{1}+1)}{2By_{1}}}-{\frac {B(3{x_{1}}^{2}+2Ax_{1}+1)^{3}}{(2By_{1})^{3}}}-y_{1}.\end{aligned}}$

## Equivalence with twisted Edwards curves

Let K be a field with characteristic different from 2.

Let $M_{A,B}$ be an elliptic curve in the Montgomery form:

$M_{A,B}:Bv^{2}=u^{3}+Au^{2}+u$

with $A\in K\smallsetminus \{-2,2\}$ , $B\in K\smallsetminus \{0\}$

and let $E_{a,d}$ be an elliptic curve in the twisted Edwards form:

$E_{a,d}\ :\ ax^{2}+y^{2}=1+dx^{2}y^{2},\,$

with $a,d\in K\smallsetminus \{0\},\quad a\neq d.$

The following theorem shows the birational equivalence between Montgomery curves and twisted Edwards curve:

**Theorem** (i) Every twisted Edwards curve is birationally equivalent to a Montgomery curve over K . In particular, the twisted Edwards curve $E_{a,d}$ is birationally equivalent to the Montgomery curve $M_{A,B}$ where $A={\frac {2(a+d)}{a-d}}$ , and $B={\frac {4}{a-d}}$ .

The map:

$\psi \,:\,E_{a,d}\rightarrow M_{A,B}$

$(x,y)\mapsto (u,v)=\left({\frac {1+y}{1-y}},{\frac {1+y}{(1-y)x}}\right)$

is a birational equivalence from $E_{a,d}$ to $M_{A,B}$ , with inverse:

$\psi ^{-1}$

:

$M_{A,B}\rightarrow E_{a,d}$

$(u,v)\mapsto (x,y)=\left({\frac {u}{v}},{\frac {u-1}{u+1}}\right),a={\frac {A+2}{B}},d={\frac {A-2}{B}}$

Notice that this equivalence between the two curves is not valid everywhere: indeed the map $\psi$ is not defined at the points $v=0$ or $u+1=0$ of the $M_{A,B}$ .

## Equivalence with Weierstrass curves

Any elliptic curve can be written in Weierstrass form. In particular, the elliptic curve in the Montgomery form

$M_{A,B}$

:

$By^{2}=x^{3}+Ax^{2}+x,$

can be transformed in the following way: divide each term of the equation for $M_{A,B}$ by $B^{3}$ , and substitute the variables *x* and *y*, with $u={\frac {x}{B}}$ and $v={\frac {y}{B}}$ respectively, to get the equation

$v^{2}=u^{3}+{\frac {A}{B}}u^{2}+{\frac {1}{B^{2}}}u.$

To obtain a short Weierstrass form from here, it is sufficient to replace *u* with the variable $t-{\frac {A}{3B}}$ :

$v^{2}=\left(t-{\frac {A}{3B}}\right)^{3}+{\frac {A}{B}}\left(t-{\frac {A}{3B}}\right)^{2}+{\frac {1}{B^{2}}}\left(t-{\frac {A}{3B}}\right);$

finally, this gives the equation:

$v^{2}=t^{3}+\left({\frac {3-A^{2}}{3B^{2}}}\right)t+\left({\frac {2A^{3}-9A}{27B^{3}}}\right).$

Hence the mapping is given as

$\psi$

:

$M_{A,B}\rightarrow E_{a,b}$

$(x,y)\mapsto (t,v)=\left({\frac {x}{B}}+{\frac {A}{3B}},{\frac {y}{B}}\right),a={\frac {3-A^{2}}{3B^{2}}},b={\frac {2A^{3}-9A}{27B^{3}}}$

In contrast, an elliptic curve over base field $\mathbb {F}$ in Weierstrass form

$E_{a,b}$

:

$v^{2}=t^{3}+at+b$

can be converted to Montgomery form if and only if $E_{a,b}$ satisfies the following conditions:

1. $z^{3}+az+b=0$ has at least one root $\alpha \in \mathbb {F}$ ; and
2. $3\alpha ^{2}+a$ is a quadratic residue in $\mathbb {F}$ .

When these conditions are satisfied, then for $s=({\sqrt {3\alpha ^{2}+a}})^{-1}$ we have the mapping

$\psi ^{-1}$

:

$E_{a,b}\rightarrow M_{A,B}$

$(t,v)\mapsto (x,y)=\left(s(t-\alpha ),sv\right),A=3\alpha s,B=s$

.
