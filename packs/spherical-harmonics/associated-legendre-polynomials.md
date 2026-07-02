---
title: "Associated Legendre polynomials"
source: https://en.wikipedia.org/wiki/Associated_Legendre_polynomials
domain: spherical-harmonics
license: CC-BY-SA-4.0
tags: spherical harmonics, associated legendre polynomials, multipole expansion, wigner d-matrix
fetched: 2026-07-02
---

# Associated Legendre polynomials

In mathematics, the **associated Legendre polynomials** are the canonical solutions of the **general Legendre differential equation**

$\left(1-x^{2}\right){\frac {d^{2}}{dx^{2}}}P_{\ell }^{m}(x)-2x{\frac {d}{dx}}P_{\ell }^{m}(x)+\left[\ell (\ell +1)-{\frac {m^{2}}{1-x^{2}}}\right]P_{\ell }^{m}(x)=0,$

or equivalently

${\frac {d}{dx}}\left[\left(1-x^{2}\right){\frac {d}{dx}}P_{\ell }^{m}(x)\right]+\left[\ell (\ell +1)-{\frac {m^{2}}{1-x^{2}}}\right]P_{\ell }^{m}(x)=0,$

where the indices *ℓ* and *m* (which are integers) are referred to as the degree and order of the associated Legendre polynomial respectively. This equation has nonzero solutions that are nonsingular on [−1, 1] only if *ℓ* and *m* are integers with 0 ≤ *m* ≤ *ℓ*, or with trivially equivalent negative values. When in addition *m* is even, the function is a polynomial. When *m* is zero and *ℓ* integer, these functions are identical to the Legendre polynomials. In general, when *ℓ* and *m* are integers, the regular solutions are sometimes called "associated Legendre polynomials", even though they are not polynomials when *m* is odd. The fully general class of functions with arbitrary real or complex values of *ℓ* and *m* are Legendre functions. In that case the parameters are usually labelled with Greek letters.

The Legendre ordinary differential equation is frequently encountered in physics and other technical fields. In particular, it occurs when solving Laplace's equation (and related partial differential equations) in spherical coordinates. Associated Legendre polynomials play a vital role in the definition of spherical harmonics.

## Definition for non-negative integer parameters ℓ and m

These functions are denoted $P_{\ell }^{m}(x)$ , where the superscript indicates the order and not a power of *P*. Their most straightforward definition is in terms of derivatives of ordinary Legendre polynomials (*m* ≥ 0)

$P_{\ell }^{m}(x)=(-1)^{m}(1-x^{2})^{m/2}{\frac {d^{m}}{dx^{m}}}\left(P_{\ell }(x)\right),$

The (−1)*m* factor in this formula is known as the Condon–Shortley phase. Some authors omit it. That the functions described by this equation satisfy the general Legendre differential equation with the indicated values of the parameters *ℓ* and *m* follows by differentiating *m* times the Legendre equation for *P**ℓ*: $\left(1-x^{2}\right){\frac {d^{2}}{dx^{2}}}P_{\ell }(x)-2x{\frac {d}{dx}}P_{\ell }(x)+\ell (\ell +1)P_{\ell }(x)=0.$

Moreover, since by Rodrigues' formula, $P_{\ell }(x)={\frac {1}{2^{\ell }\,\ell !}}\ {\frac {d^{\ell }}{dx^{\ell }}}\left[(x^{2}-1)^{\ell }\right],$ the *P**m* *ℓ* can be expressed in the form $P_{\ell }^{m}(x)={\frac {(-1)^{m}}{2^{\ell }\ell !}}(1-x^{2})^{m/2}\ {\frac {d^{\ell +m}}{dx^{\ell +m}}}(x^{2}-1)^{\ell }.$

This equation allows extension of the range of *m* to: −*ℓ* ≤ *m* ≤ *ℓ*. The definitions of *P**ℓ*±*m*, resulting from this expression by substitution of ±*m*, are proportional. Indeed, equate the coefficients of equal powers on the left and right hand side of ${\frac {d^{\ell -m}}{dx^{\ell -m}}}(x^{2}-1)^{\ell }=c_{lm}(1-x^{2})^{m}{\frac {d^{\ell +m}}{dx^{\ell +m}}}(x^{2}-1)^{\ell },$ then it follows that the proportionality constant is $c_{lm}=(-1)^{m}{\frac {(\ell -m)!}{(\ell +m)!}},$ so that $P_{\ell }^{-m}(x)=(-1)^{m}{\frac {(\ell -m)!}{(\ell +m)!}}P_{\ell }^{m}(x).$

### Alternative notations

The following alternative notations are also used in literature: $P_{\ell m}(x)=(-1)^{m}P_{\ell }^{m}(x)$

### Closed Form

Starting from the explicit form provided in the article of Legendre Polynomials

$P_{l}(x)=2^{l}\sum _{k=0}^{l}x^{k}{\binom {l}{k}}{\binom {(l+k-1)/2}{l}}$

one obtains with the standard rules for m -fold derivatives for powers

$P_{l}^{m}(x)=(-1)^{m}\cdot 2^{l}\cdot (1-x^{2})^{m/2}\cdot \sum _{k=m}^{l}{\frac {k!}{(k-m)!}}\cdot x^{k-m}\cdot {\binom {l}{k}}{\binom {\frac {l+k-1}{2}}{l}}$

with simple monomials and the generalized form of the binomial coefficient. The sum effectively extends only over terms where $l-k$ is even, because for odd $l-k$ the binomial factor ${\binom {(l+k-1)/2}{l}}$ is zero.

Summarizing results of Doha the expansion of derivatives into Legendre Polynomials defines coefficients $\tau$

${\frac {d^{m}}{dx^{m}}}P_{l}(x)=\sum _{t=0}^{\lfloor (l-m)/2\rfloor }\tau _{l,m,t}P_{l-m-2t}(x),$

where

$\tau _{l,m,t}=\epsilon _{l-t}{\frac {l-m-2t+1/2}{2l-2t+1}}{\frac {(2m)!}{2^{m}m!}}{\binom {2l-2t+1}{2m}}{\frac {m}{m+t}}{\binom {m+t}{t}}{\frac {1}{\binom {l-t}{m}}},$

and where

$\epsilon _{q}\equiv {\begin{cases}1,&q=0;\\2,&q\geq 1\end{cases}}$

is the Neumann factor.

## Orthogonality

The associated Legendre polynomials are not mutually orthogonal in general. For example, $P_{1}^{1}$ is not orthogonal to $P_{2}^{2}$ . However, some subsets are orthogonal. Assuming 0 ≤ *m* ≤ *ℓ*, they satisfy the orthogonality condition for fixed *m*:

$\int _{-1}^{1}P_{k}^{m}P_{\ell }^{m}dx={\frac {2(\ell +m)!}{(2\ell +1)(\ell -m)!}}\ \delta _{k,\ell }$

Where *δ**k*,*ℓ* is the Kronecker delta.

Also, they satisfy the orthogonality condition for fixed *ℓ*:

$\int _{-1}^{1}{\frac {P_{\ell }^{m}P_{\ell }^{n}}{1-x^{2}}}dx={\begin{cases}0&{\text{if }}m\neq n\\{\frac {(\ell +m)!}{m(\ell -m)!}}&{\text{if }}m=n\neq 0\\\infty &{\text{if }}m=n=0\end{cases}}$

## Negative m and/or negative ℓ

The differential equation is clearly invariant under a change in sign of *m*.

The functions for negative *m* were shown above to be proportional to those of positive *m*: $P_{\ell }^{-m}=(-1)^{m}{\frac {(\ell -m)!}{(\ell +m)!}}P_{\ell }^{m}$

(This followed from the Rodrigues' formula definition. This definition also makes the various recurrence formulas work for positive or negative m.) ${\text{If}}\quad |m|>\ell \,\quad {\text{then}}\quad P_{\ell }^{m}=0.\,$

The differential equation is also invariant under a change from ℓ to −*ℓ* − 1, and the functions for negative ℓ are defined by

$P_{-\ell }^{m}=P_{\ell -1}^{m},\ (\ell =1,\,2,\,\dots ).$

## Parity

From their definition, one can verify that the Associated Legendre functions are either even or odd according to

$P_{\ell }^{m}(-x)=(-1)^{\ell -m}P_{\ell }^{m}(x)$

## The first few associated Legendre functions

The first few associated Legendre functions, including those for negative values of *m*, are:

$P_{0}^{0}(x)=1$

${\begin{aligned}P_{1}^{-1}(x)&=-{\tfrac {1}{2}}P_{1}^{1}(x)\\P_{1}^{0}(x)&=x\\P_{1}^{1}(x)&=-(1-x^{2})^{1/2}\end{aligned}}$

${\begin{aligned}P_{2}^{-2}(x)&={\tfrac {1}{24}}P_{2}^{2}(x)\\P_{2}^{-1}(x)&=-{\tfrac {1}{6}}P_{2}^{1}(x)\\P_{2}^{0}(x)&={\tfrac {1}{2}}(3x^{2}-1)\\P_{2}^{1}(x)&=-3x(1-x^{2})^{1/2}\\P_{2}^{2}(x)&=3(1-x^{2})\end{aligned}}$

${\begin{aligned}P_{3}^{-3}(x)&=-{\tfrac {1}{720}}P_{3}^{3}(x)\\P_{3}^{-2}(x)&={\tfrac {1}{120}}P_{3}^{2}(x)\\P_{3}^{-1}(x)&=-{\tfrac {1}{12}}P_{3}^{1}(x)\\P_{3}^{0}(x)&={\tfrac {1}{2}}(5x^{3}-3x)\\P_{3}^{1}(x)&={\tfrac {3}{2}}(1-5x^{2})(1-x^{2})^{1/2}\\P_{3}^{2}(x)&=15x(1-x^{2})\\P_{3}^{3}(x)&=-15(1-x^{2})^{3/2}\end{aligned}}$

${\begin{aligned}P_{4}^{-4}(x)&={\tfrac {1}{40320}}P_{4}^{4}(x)\\P_{4}^{-3}(x)&=-{\tfrac {1}{5040}}P_{4}^{3}(x)\\P_{4}^{-2}(x)&={\tfrac {1}{360}}P_{4}^{2}(x)\\P_{4}^{-1}(x)&=-{\tfrac {1}{20}}P_{4}^{1}(x)\\P_{4}^{0}(x)&={\tfrac {1}{8}}(35x^{4}-30x^{2}+3)\\P_{4}^{1}(x)&=-{\tfrac {5}{2}}(7x^{3}-3x)(1-x^{2})^{1/2}\\P_{4}^{2}(x)&={\tfrac {15}{2}}(7x^{2}-1)(1-x^{2})\\P_{4}^{3}(x)&=-105x(1-x^{2})^{3/2}\\P_{4}^{4}(x)&=105(1-x^{2})^{2}\end{aligned}}$

## Recurrence formula

These functions have a number of recurrence properties:

$(\ell -m+1)P_{\ell +1}^{m}(x)=(2\ell +1)xP_{\ell }^{m}(x)-(\ell +m)P_{\ell -1}^{m}(x)$

$2mxP_{\ell }^{m}(x)=-{\sqrt {1-x^{2}}}\left[P_{\ell }^{m+1}(x)+(\ell +m)(\ell -m+1)P_{\ell }^{m-1}(x)\right]$

${\frac {1}{\sqrt {1-x^{2}}}}P_{\ell }^{m}(x)={\frac {-1}{2m}}\left[P_{\ell -1}^{m+1}(x)+(\ell +m-1)(\ell +m)P_{\ell -1}^{m-1}(x)\right]$

${\frac {1}{\sqrt {1-x^{2}}}}P_{\ell }^{m}(x)={\frac {-1}{2m}}\left[P_{\ell +1}^{m+1}(x)+(\ell -m+1)(\ell -m+2)P_{\ell +1}^{m-1}(x)\right]$

${\sqrt {1-x^{2}}}P_{\ell }^{m}(x)={\frac {1}{2\ell +1}}\left[(\ell -m+1)(\ell -m+2)P_{\ell +1}^{m-1}(x)-(\ell +m-1)(\ell +m)P_{\ell -1}^{m-1}(x)\right]$

${\sqrt {1-x^{2}}}P_{\ell }^{m}(x)={\frac {-1}{2\ell +1}}\left[P_{\ell +1}^{m+1}(x)-P_{\ell -1}^{m+1}(x)\right]$

${\sqrt {1-x^{2}}}P_{\ell }^{m+1}(x)=(\ell -m)xP_{\ell }^{m}(x)-(\ell +m)P_{\ell -1}^{m}(x)$

${\sqrt {1-x^{2}}}P_{\ell }^{m+1}(x)=(\ell -m+1)P_{\ell +1}^{m}(x)-(\ell +m+1)xP_{\ell }^{m}(x)$

${\sqrt {1-x^{2}}}{\frac {d}{dx}}{P_{\ell }^{m}}(x)={\frac {1}{2}}\left[(\ell +m)(\ell -m+1)P_{\ell }^{m-1}(x)-P_{\ell }^{m+1}(x)\right]$

$(1-x^{2}){\frac {d}{dx}}{P_{\ell }^{m}}(x)={\frac {1}{2\ell +1}}\left[(\ell +1)(\ell +m)P_{\ell -1}^{m}(x)-\ell (\ell -m+1)P_{\ell +1}^{m}(x)\right]$

$(x^{2}-1){\frac {d}{dx}}{P_{\ell }^{m}}(x)={\ell }xP_{\ell }^{m}(x)-(\ell +m)P_{\ell -1}^{m}(x)$

$(x^{2}-1){\frac {d}{dx}}{P_{\ell }^{m}}(x)=-(\ell +1)xP_{\ell }^{m}(x)+(\ell -m+1)P_{\ell +1}^{m}(x)$

$(x^{2}-1){\frac {d}{dx}}{P_{\ell }^{m}}(x)={\sqrt {1-x^{2}}}P_{\ell }^{m+1}(x)+mxP_{\ell }^{m}(x)$

$(x^{2}-1){\frac {d}{dx}}{P_{\ell }^{m}}(x)=-(\ell +m)(\ell -m+1){\sqrt {1-x^{2}}}P_{\ell }^{m-1}(x)-mxP_{\ell }^{m}(x)$

$(\ell -m-1)(\ell -m)P_{\ell }^{m}(x)=-P_{\ell }^{m+2}(x)+P_{\ell -2}^{m+2}(x)+(\ell +m)(\ell +m-1)P_{\ell -2}^{m}(x)$

Helpful identities (initial values for the first recursion):

$P_{\ell +1}^{\ell +1}(x)=-(2\ell +1){\sqrt {1-x^{2}}}P_{\ell }^{\ell }(x)$ $P_{\ell }^{\ell }(x)=(-1)^{\ell }(2\ell -1)!!(1-x^{2})^{(\ell /2)}$ $P_{\ell +1}^{\ell }(x)=x(2\ell +1)P_{\ell }^{\ell }(x)$

with !! the double factorial.

## Gaunt's formula

The integral over the product of three associated Legendre polynomials (with orders matching as shown below) is a necessary ingredient when developing products of Legendre polynomials into a series linear in the Legendre polynomials. For instance, this turns out to be necessary when doing atomic calculations of the Hartree–Fock variety where matrix elements of the Coulomb operator are needed. For this we have Gaunt's formula ${\begin{aligned}{\frac {1}{2}}\int _{-1}^{1}P_{l}^{u}(x)P_{m}^{v}(x)P_{n}^{w}(x)dx={}&{}(-1)^{s-m-w}{\frac {(m+v)!(n+w)!(2s-2n)!s!}{(m-v)!(s-l)!(s-m)!(s-n)!(2s+1)!}}\\&{}\times \ \sum _{t=p}^{q}(-1)^{t}{\frac {(l+u+t)!(m+n-u-t)!}{t!(l-u-t)!(m-n+u+t)!(n-w-t)!}}\end{aligned}}$ This formula is to be used under the following assumptions:

1. the degrees are non-negative integers $l,m,n\geq 0$
2. all three orders are non-negative integers $u,v,w\geq 0$
3. u is the largest of the three orders
4. the orders sum up $u=v+w$
5. the degrees obey $m\geq n$

Other quantities appearing in the formula are defined as $2s=l+m+n$ $p=\max(0,\,n-m-u)$ $q=\min(m+n-u,\,l-u,\,n-w)$

The integral is zero unless

1. the sum of degrees is even so that s is an integer
2. the triangular condition is satisfied $m+n\geq l\geq m-n$

Dong and Lemus (2002) generalized the derivation of this formula to integrals over a product of an arbitrary number of associated Legendre polynomials.

## Generalization via hypergeometric functions

These functions may actually be defined for general complex parameters and argument:

$P_{\lambda }^{\mu }(z)={\frac {1}{\Gamma (1-\mu )}}\left[{\frac {1+z}{1-z}}\right]^{\mu /2}\,_{2}F_{1}(-\lambda ,\lambda +1;1-\mu ;{\frac {1-z}{2}})$

where $\Gamma$ is the gamma function and $_{2}F_{1}$ is the hypergeometric function

$\,_{2}F_{1}(\alpha ,\beta ;\gamma ;z)={\frac {\Gamma (\gamma )}{\Gamma (\alpha )\Gamma (\beta )}}\sum _{n=0}^{\infty }{\frac {\Gamma (n+\alpha )\Gamma (n+\beta )}{\Gamma (n+\gamma )\ n!}}z^{n},$

They are called the **Legendre functions** when defined in this more general way. They satisfy the same differential equation as before:

$(1-z^{2})\,y''-2zy'+\left(\lambda [\lambda +1]-{\frac {\mu ^{2}}{1-z^{2}}}\right)\,y=0.\,$

Since this is a second order differential equation, it has a second solution, $Q_{\lambda }^{\mu }(z)$ , defined as:

$Q_{\lambda }^{\mu }(z)={\frac {{\sqrt {\pi }}\ \Gamma (\lambda +\mu +1)}{2^{\lambda +1}\Gamma (\lambda +3/2)}}{\frac {1}{z^{\lambda +\mu +1}}}(1-z^{2})^{\mu /2}\,_{2}F_{1}\left({\frac {\lambda +\mu +1}{2}},{\frac {\lambda +\mu +2}{2}};\lambda +{\frac {3}{2}};{\frac {1}{z^{2}}}\right)$

$P_{\lambda }^{\mu }(z)$ and $Q_{\lambda }^{\mu }(z)$ both obey the various recurrence formulas given previously.

## Reparameterization in terms of angles

These functions are most useful when the argument is reparameterized in terms of angles, letting $x=\cos \theta$ :

$P_{\ell }^{m}(\cos \theta )=(-1)^{m}(\sin \theta )^{m}\ {\frac {d^{m}}{d(\cos \theta )^{m}}}\left(P_{\ell }(\cos \theta )\right)$

Using the relation $(1-x^{2})^{1/2}=\sin \theta$ , the list given above yields the first few polynomials, parameterized this way, as:

${\begin{aligned}P_{0}^{0}(\cos \theta )&=1\\[8pt]P_{1}^{0}(\cos \theta )&=\cos \theta \\[8pt]P_{1}^{1}(\cos \theta )&=-\sin \theta \\[8pt]P_{2}^{0}(\cos \theta )&={\tfrac {1}{2}}(3\cos ^{2}\theta -1)\\[8pt]P_{2}^{1}(\cos \theta )&=-3\cos \theta \sin \theta \\[8pt]P_{2}^{2}(\cos \theta )&=3\sin ^{2}\theta \\[8pt]P_{3}^{0}(\cos \theta )&={\tfrac {1}{2}}(5\cos ^{3}\theta -3\cos \theta )\\[8pt]P_{3}^{1}(\cos \theta )&=-{\tfrac {3}{2}}(5\cos ^{2}\theta -1)\sin \theta \\[8pt]P_{3}^{2}(\cos \theta )&=15\cos \theta \sin ^{2}\theta \\[8pt]P_{3}^{3}(\cos \theta )&=-15\sin ^{3}\theta \\[8pt]P_{4}^{0}(\cos \theta )&={\tfrac {1}{8}}(35\cos ^{4}\theta -30\cos ^{2}\theta +3)\\[8pt]P_{4}^{1}(\cos \theta )&=-{\tfrac {5}{2}}(7\cos ^{3}\theta -3\cos \theta )\sin \theta \\[8pt]P_{4}^{2}(\cos \theta )&={\tfrac {15}{2}}(7\cos ^{2}\theta -1)\sin ^{2}\theta \\[8pt]P_{4}^{3}(\cos \theta )&=-105\cos \theta \sin ^{3}\theta \\[8pt]P_{4}^{4}(\cos \theta )&=105\sin ^{4}\theta \end{aligned}}$

The orthogonality relations given above become in this formulation: for fixed *m*, $P_{\ell }^{m}(\cos \theta )$ are orthogonal, parameterized by θ over $[0,\pi ]$ , with weight $\sin \theta$ :

$\int _{0}^{\pi }P_{k}^{m}(\cos \theta )P_{\ell }^{m}(\cos \theta )\,\sin \theta \,d\theta ={\frac {2(\ell +m)!}{(2\ell +1)(\ell -m)!}}\ \delta _{k,\ell }$

Also, for fixed *ℓ*:

$\int _{0}^{\pi }P_{\ell }^{m}(\cos \theta )P_{\ell }^{n}(\cos \theta )\csc \theta \,d\theta ={\begin{cases}0&{\text{if }}m\neq n\\{\frac {(\ell +m)!}{m(\ell -m)!}}&{\text{if }}m=n\neq 0\\\infty &{\text{if }}m=n=0\end{cases}}$

In terms of θ, $P_{\ell }^{m}(\cos \theta )$ are solutions of

${\frac {d^{2}y}{d\theta ^{2}}}+\cot \theta {\frac {dy}{d\theta }}+\left[\lambda -{\frac {m^{2}}{\sin ^{2}\theta }}\right]\,y=0\,$

More precisely, given an integer *m* $\geq$ 0, the above equation has nonsingular solutions only when $\lambda =\ell (\ell +1)\,$ for *ℓ* an integer ≥ *m*, and those solutions are proportional to $P_{\ell }^{m}(\cos \theta )$ .

## Applications in physics: spherical harmonics

In many occasions in physics, associated Legendre polynomials in terms of angles occur where spherical symmetry is involved. The colatitude angle in spherical coordinates is the angle $\theta$ used above. The longitude angle, $\phi$ , appears in a multiplying factor. Together, they make a set of functions called spherical harmonics. These functions express the symmetry of the two-sphere under the action of the Lie group SO(3).

What makes these functions useful is that they are central to the solution of the equation $\nabla ^{2}\psi +\lambda \psi =0$ on the surface of a sphere. In spherical coordinates θ (colatitude) and φ (longitude), the Laplacian is

$\nabla ^{2}\psi ={\frac {\partial ^{2}\psi }{\partial \theta ^{2}}}+\cot \theta {\frac {\partial \psi }{\partial \theta }}+\csc ^{2}\theta {\frac {\partial ^{2}\psi }{\partial \phi ^{2}}}.$

When the partial differential equation

${\frac {\partial ^{2}\psi }{\partial \theta ^{2}}}+\cot \theta {\frac {\partial \psi }{\partial \theta }}+\csc ^{2}\theta {\frac {\partial ^{2}\psi }{\partial \phi ^{2}}}+\lambda \psi =0$

is solved by the method of separation of variables, one gets a φ-dependent part $\sin(m\phi )$ or $\cos(m\phi )$ for integer m≥0, and an equation for the θ-dependent part

${\frac {d^{2}y}{d\theta ^{2}}}+\cot \theta {\frac {dy}{d\theta }}+\left[\lambda -{\frac {m^{2}}{\sin ^{2}\theta }}\right]\,y=0\,$

for which the solutions are $P_{\ell }^{m}(\cos \theta )$ with $\ell {\geq }m$ and $\lambda =\ell (\ell +1)$ .

Therefore, the equation

$\nabla ^{2}\psi +\lambda \psi =0$

has nonsingular separated solutions only when $\lambda =\ell (\ell +1)$ , and those solutions are proportional to

$P_{\ell }^{m}(\cos \theta )\ \cos(m\phi )\ \ \ \ 0\leq m\leq \ell$

and

$P_{\ell }^{m}(\cos \theta )\ \sin(m\phi )\ \ \ \ 0<m\leq \ell .$

For each choice of *ℓ*, there are 2ℓ + 1 functions for the various values of *m* and choices of sine and cosine. They are all orthogonal in both *ℓ* and *m* when integrated over the surface of the sphere.

The solutions are usually written in terms of complex exponentials:

$Y_{\ell ,m}(\theta ,\phi )={\sqrt {\frac {(2\ell +1)(\ell -m)!}{4\pi (\ell +m)!}}}\ P_{\ell }^{m}(\cos \theta )\ e^{im\phi }\qquad -\ell \leq m\leq \ell .$ The functions $Y_{\ell ,m}(\theta ,\phi )$ are the spherical harmonics, and the quantity in the square root is a normalizing factor. Recalling the relation between the associated Legendre functions of positive and negative *m*, it is easily shown that the spherical harmonics satisfy the identity

$Y_{\ell ,m}^{*}(\theta ,\phi )=(-1)^{m}Y_{\ell ,-m}(\theta ,\phi ).$

The spherical harmonic functions form a complete orthonormal set of functions in the sense of Fourier series. Workers in the fields of geodesy, geomagnetism and spectral analysis use a different phase and normalization factor than given here (see spherical harmonics).

When a 3-dimensional spherically symmetric partial differential equation is solved by the method of separation of variables in spherical coordinates, the part that remains after removal of the radial part is typically of the form

$\nabla ^{2}\psi (\theta ,\phi )+\lambda \psi (\theta ,\phi )=0,$

and hence the solutions are spherical harmonics.

## Generalizations

The Legendre polynomials are closely related to hypergeometric series. In the form of spherical harmonics, they express the symmetry of the two-sphere under the action of the Lie group SO(3). There are many other Lie groups besides SO(3), and analogous generalizations of the Legendre polynomials exist to express the symmetries of semi-simple Lie groups and Riemannian symmetric spaces. Crudely speaking, one may define a Laplacian on symmetric spaces; the eigenfunctions of the Laplacian can be thought of as generalizations of the spherical harmonics to other settings.

By solving the Laplace equation in higher dimensions (with a potential that does not fall of $\sim 1/r$ ) Legendre Polynomials in higher than 3D can be defined.
