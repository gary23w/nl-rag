---
title: "Lagrange inversion theorem"
source: https://en.wikipedia.org/wiki/Lagrange_inversion_theorem
domain: generating-functions-deep
license: CC-BY-SA-4.0
tags: generating function, formal power series, umbral calculus, lagrange inversion theorem
fetched: 2026-07-02
---

# Lagrange inversion theorem

In mathematical analysis, the **Lagrange inversion theorem**, also known as the **Lagrange–Bürmann formula**, gives the Taylor series expansion of the inverse function of an analytic function. Lagrange inversion is a special case of the inverse function theorem.

## Statement

Suppose z is defined as a function of w by an equation of the form

$z=f(w)$

where f is analytic at a point a and $f'(a)\neq 0.$ Then it is possible to *invert* or *solve* the equation for w, expressing it in the form $w=g(z)$ given by a power series

$g(z)=a+\sum _{n=1}^{\infty }g_{n}{\frac {(z-f(a))^{n}}{n!}},$

where

$g_{n}=\lim _{w\to a}{\frac {d^{n-1}}{dw^{n-1}}}\left[\left({\frac {w-a}{f(w)-f(a)}}\right)^{n}\right].$

The theorem further states that this series has a non-zero radius of convergence, i.e., $g(z)$ represents an analytic function of z in a neighbourhood of $z=f(a).$ This is also called **reversion of series**.

If the assertions about analyticity are omitted, the formula is also valid for formal power series and can be generalized in various ways: It can be formulated for functions of several variables; it can be extended to provide a ready formula for *F*(*g*(*z*)) for any analytic function F; and it can be generalized to the case $f'(a)=0,$ where the inverse g is a multivalued function.

The theorem was proved by Lagrange and generalized by Hans Heinrich Bürmann, both in the late 18th century. There is a straightforward derivation using complex analysis and contour integration; the complex formal power series version is a consequence of knowing the formula for polynomials, so the theory of analytic functions may be applied. Actually, the machinery from analytic function theory enters only in a formal way in this proof, in that what is really needed is some property of the formal residue, and a more direct formal proof is available. In fact, the Lagrange inversion theorem has a number of additional rather different proofs, including ones using tree-counting arguments or induction.

If f is a formal power series, then the above formula does not give the coefficients of the compositional inverse series g directly in terms for the coefficients of the series f. If one can express the functions f and g in formal power series as

$f(w)=\sum _{k=0}^{\infty }f_{k}{\frac {w^{k}}{k!}}\qquad {\text{and}}\qquad g(z)=\sum _{k=0}^{\infty }g_{k}{\frac {z^{k}}{k!}}$

with *f*0 = 0 and *f*1 ≠ 0, then an explicit form of inverse coefficients can be given in term of Bell polynomials:

$g_{n}={\frac {1}{f_{1}^{n}}}\sum _{k=1}^{n-1}(-1)^{k}n^{\overline {k}}B_{n-1,k}({\hat {f}}_{1},{\hat {f}}_{2},\ldots ,{\hat {f}}_{n-k}),\quad n\geq 2,$

where

${\begin{aligned}{\hat {f}}_{k}&={\frac {f_{k+1}}{(k+1)f_{1}}},\\g_{1}&={\frac {1}{f_{1}}},{\text{ and}}\\n^{\overline {k}}&=n(n+1)\cdots (n+k-1)\end{aligned}}$

is the rising factorial.

When *f*1 = 1, the last formula can be interpreted in terms of the faces of associahedra

$g_{n}=\sum _{F{\text{ face of }}K_{n}}(-1)^{n-\dim F}f_{F},\quad n\geq 2,$

where $f_{F}=f_{i_{1}}\cdots f_{i_{m}}$ for each face $F=K_{i_{1}}\times \cdots \times K_{i_{m}}$ of the associahedron $K_{n}.$

## Example

For instance, the algebraic equation of degree p

$x^{p}-x+z=0$

can be solved for x by means of the Lagrange inversion formula for the function *f*(*x*) = *x* − *x**p*, resulting in a formal series solution

$x=\sum _{k=0}^{\infty }{\binom {pk}{k}}{\frac {z^{(p-1)k+1}}{(p-1)k+1}}.$

By convergence tests, this series is in fact convergent for $|z|\leq (p-1)p^{-p/(p-1)},$ which is also the largest disk in which a local inverse to f can be defined.

## Applications

### Lagrange–Bürmann formula

There is a special case of Lagrange inversion theorem that is used in combinatorics and applies when $f(w)=w/\phi (w)$ for some analytic $\phi (w)$ with $\phi (0)\neq 0.$ Take $a=0$ to obtain $f(a)=f(0)=0.$ Then for the inverse $g(z)$ (satisfying $f(g(z))\equiv z$ ), we have

${\begin{aligned}g(z)&=\sum _{n=1}^{\infty }\left[\lim _{w\to 0}{\frac {d^{n-1}}{dw^{n-1}}}\left(\left({\frac {w}{w/\phi (w)}}\right)^{n}\right)\right]{\frac {z^{n}}{n!}}\\{}&=\sum _{n=1}^{\infty }{\frac {1}{n}}\left[{\frac {1}{(n-1)!}}\lim _{w\to 0}{\frac {d^{n-1}}{dw^{n-1}}}(\phi (w)^{n})\right]z^{n},\end{aligned}}$

which can be written alternatively as

$[z^{n}]g(z)={\frac {1}{n}}[w^{n-1}]\phi (w)^{n},$

where $[w^{r}]$ is an operator which extracts the coefficient of $w^{r}$ in the Taylor series of a function of w.

A generalization of the formula is known as the **Lagrange–Bürmann formula**:

$[z^{n}]H(g(z))={\frac {1}{n}}[w^{n-1}](H'(w)\phi (w)^{n})$

where *H* is an arbitrary analytic function.

Sometimes, the derivative *H′*(*w*) can be quite complicated. A simpler version of the formula replaces *H′*(*w*) with *H*(*w*)(1 − *φ′*(*w*)/*φ*(*w*)) to get

$[z^{n}]H(g(z))=[w^{n}]H(w)\phi (w)^{n-1}(\phi (w)-w\phi '(w)),$

which involves *φ′*(*w*) instead of *H′*(*w*).

### Lambert *W* function

The Lambert W function is the function $W(z)$ that is implicitly defined by the equation

$W(z)e^{W(z)}=z.$

We may use the theorem to compute the Taylor series of $W(z)$ at $z=0.$ We take $f(w)=we^{w}$ and $a=0.$ Recognizing that

${\frac {d^{n}}{dx^{n}}}e^{\alpha x}=\alpha ^{n}e^{\alpha x},$

this gives

${\begin{aligned}W(z)&=\sum _{n=1}^{\infty }\left[\lim _{w\to 0}{\frac {d^{n-1}}{dw^{n-1}}}e^{-nw}\right]{\frac {z^{n}}{n!}}\\{}&=\sum _{n=1}^{\infty }(-n)^{n-1}{\frac {z^{n}}{n!}}\\{}&=z-z^{2}+{\frac {3}{2}}z^{3}-{\frac {8}{3}}z^{4}+O(z^{5}).\end{aligned}}$

The radius of convergence of this series is $e^{-1}$ (giving the principal branch of the Lambert function).

A series that converges for $|\ln(z)-1|<{\sqrt {4+\pi ^{2}}}$ (approximately $0.0655<z<112.63$ ) can also be derived by series inversion. The function $f(z)=W(e^{z})-1$ satisfies the equation

$1+f(z)+\ln(1+f(z))=z.$

Then $z+\ln(1+z)$ can be expanded into a power series and inverted. This gives a series for $f(z+1)=W(e^{z+1})-1{\text{:}}$

$W(e^{1+z})=1+{\frac {z}{2}}+{\frac {z^{2}}{16}}-{\frac {z^{3}}{192}}-{\frac {z^{4}}{3072}}+{\frac {13z^{5}}{61440}}-O(z^{6}).$

$W(x)$ can be computed by substituting $\ln x-1$ for z in the above series. For example, substituting −1 for z gives the value of $W(1)\approx 0.567143.$

### Binary trees

Consider the set ${\mathcal {B}}$ of unlabelled binary trees. An element of ${\mathcal {B}}$ is either a leaf of size zero, or a root node with two subtrees. Denote by $B_{n}$ the number of binary trees on n nodes.

Removing the root splits a binary tree into two trees of smaller size. This yields the functional equation on the generating function $\textstyle B(z)=\sum _{n=0}^{\infty }B_{n}z^{n}{\text{:}}$

$B(z)=1+zB(z)^{2}.$

Letting $C(z)=B(z)-1$ , one has thus $C(z)=z(C(z)+1)^{2}.$ Applying the theorem with $\phi (w)=(w+1)^{2}$ yields

$B_{n}=[z^{n}]C(z)={\frac {1}{n}}[w^{n-1}](w+1)^{2n}={\frac {1}{n}}{\binom {2n}{n-1}}={\frac {1}{n+1}}{\binom {2n}{n}}.$

This shows that $B_{n}$ is the nth Catalan number.

### Asymptotic approximation of integrals

In the Laplace–Erdelyi theorem that gives the asymptotic approximation for Laplace-type integrals, the function inversion is taken as a crucial step.
