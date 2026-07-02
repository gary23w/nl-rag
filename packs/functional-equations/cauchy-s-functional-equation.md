---
title: "Cauchy's functional equation"
source: https://en.wikipedia.org/wiki/Cauchy's_functional_equation
domain: functional-equations
license: CC-BY-SA-4.0
tags: functional equation, cauchy functional equation, recurrence relation, generating function
fetched: 2026-07-02
---

# Cauchy's functional equation

**Cauchy's functional equation** is the functional equation: $f(x+y)=f(x)+f(y).$

A function f that solves this equation is called an additive function. Over the rational numbers, it can be shown using elementary algebra that there is a single family of solutions, namely $f\colon x\mapsto cx$ for any rational constant $c.$ Over the real numbers, the family of linear maps $f\colon x\mapsto cx,$ now with c an arbitrary real constant, is likewise a family of solutions; however there can exist other solutions not of this form that are extremely complicated. However, any of a number of regularity conditions, some of them quite weak, will preclude the existence of these pathological solutions. For example, an additive function $f\colon \mathbb {R} \to \mathbb {R}$ is linear if:

- f is continuous (Cauchy, 1821). In fact, it suffices for f to be continuous at one point (Darboux, 1875).
- $f(x)\geq 0$ or $f(x)\leq 0$ for all ⁠ $x\geq 0$ ⁠.
- f is monotonic on any interval.
- f is bounded above or below on any interval.
- f is Lebesgue measurable.
- $f\left(x^{n+1}\right)=x^{n}f(x)$ for all real x and some positive integer ⁠ n ⁠.
- The graph of f is not dense in ⁠ $\mathbb {R} ^{2}$ ⁠.

On the other hand, if no further conditions are imposed on ⁠ f ⁠, then (assuming the axiom of choice) there are infinitely many other functions that satisfy the equation. This was proved in 1905 by Georg Hamel using Hamel bases. Such functions are sometimes called *Hamel functions*.

The fifth problem on Hilbert's list is a generalisation of this equation. Functions where there exists a real number c such that $f(cx)\neq cf(x)$ are known as Cauchy–Hamel functions and are used in Dehn–Hadwiger invariants which are used in the extension of Hilbert's third problem from 3D to higher dimensions.

This equation is sometimes referred to as **Cauchy's additive functional equation** to distinguish it from the other functional equations introduced by Cauchy in 1821, the exponential functional equation ⁠ $f(x+y)=f(x)f(y)$ ⁠, the logarithmic functional equation ⁠ $f(xy)=f(x)+f(y)$ ⁠, and the multiplicative functional equation ⁠ $f(xy)=f(x)f(y)$ ⁠.

## Solutions over the rational numbers

A simple argument, involving only elementary algebra, demonstrates that the set of additive maps $f\colon V\to W$ , where $V,W$ are vector spaces over an extension field of $\mathbb {Q}$ , is a subset of the set of $\mathbb {Q}$ -linear maps from V to W .

**Theorem:** *Let $f\colon V\to W$ be an additive function. Then f is $\mathbb {Q}$ -linear.*

**Proof:** We want to prove that any solution $f\colon V\to W$ to Cauchy’s functional equation, $f(x+y)=f(x)+f(y)$ , satisfies $f(qv)=qf(v)$ for any $q\in \mathbb {Q}$ and $v\in V$ . Let $v\in V$ .

First note $f(0)=f(0+0)=f(0)+f(0)$ , hence $f(0)=0$ , and therewith $0=f(0)=f(v+(-v))=f(v)+f(-v)$ from which follows $f(-v)=-f(v)$ .

Via induction, $f(mv)=mf(v)$ is proved for any $m\in \mathbb {N} \cup \{0\}$ .

For any negative integer $m\in \mathbb {Z}$ we know ⁠ $-m\in \mathbb {N}$ ⁠, therefore ⁠ $f(mv)=f((-m)(-v))=(-m)f(-v)=(-m)(-f(v))=mf(v)$ ⁠. Thus far we have proved

$f(mv)=mf(v)$

for any

$m\in \mathbb {Z}$

.

Let $n\in \mathbb {N}$ , then $f(v)=f(nn^{-1}v)=nf(n^{-1}v)$ and hence ⁠ $f(n^{-1}v)=n^{-1}f(v)$ ⁠.

Finally, any $q\in \mathbb {Q}$ has a representation $q={\frac {m}{n}}$ with $m\in \mathbb {Z}$ and ⁠ $n\in \mathbb {N}$ ⁠, so, putting things together,

$f(qv)=f\left({\frac {m}{n}}\,v\right)=f\left({\frac {1}{n}}\,(mv)\right)={\frac {1}{n}}\,f(mv)={\frac {1}{n}}\,m\,f(v)=qf(v)$

, q.e.d.

## Properties of nonlinear solutions over the real numbers

We prove below that any other solutions must be highly pathological functions. In particular, it is shown that any other solution must have the property that its graph $\{(x,f(x))\vert x\in \mathbb {R} \}$ is dense in ⁠ $\mathbb {R} ^{2}$ ⁠, that is, that any disk in the plane (however small) contains a point from the graph. From this it is easy to prove the various conditions given in the introductory paragraph.

**Lemma**—Let $t>0$ . If f satisfies the Cauchy functional equation on the interval $[0,t]$ , but is not linear, then its graph is dense on the strip $[0,t]\times \mathbb {R}$ .

Proof

WLOG, scale f on the x-axis and y-axis, so that f satisfies the Cauchy functional equation on ⁠ $[0,1]$ ⁠, and ⁠ $f(1)=1$ ⁠. It suffices to show that the graph of f is dense in ⁠ $(0,1)\times \mathbb {R}$ ⁠, which is dense in ⁠ $[0,1]\times \mathbb {R}$ ⁠.

Since f is not linear, we have $f(a)\neq a$ for some ⁠ $a\in (0,1)$ ⁠.

Claim: The lattice defined by $L:=\{(r_{1}+r_{2}a,r_{1}+r_{2}f(a)):r_{1},r_{2}\in \mathbb {Q} \}$ is dense in ⁠ $\mathbb {R} ^{2}$ ⁠.

Consider the linear transformation $A:\mathbb {R} ^{2}\to \mathbb {R} ^{2}$ defined by $A(x,y)={\begin{bmatrix}1&a\\1&f(a)\end{bmatrix}}{\begin{bmatrix}x\\y\end{bmatrix}}$

With this transformation, we have ⁠ $L=A(\mathbb {Q} ^{2})$ ⁠.

Since ⁠ $\det A=f(a)-a\neq 0$ ⁠, the transformation is invertible, thus it is bicontinuous. Since $\mathbb {Q} ^{2}$ is dense in ⁠ $\mathbb {R} ^{2}$ ⁠, so is ⁠ L ⁠. $\square$

Claim: if ⁠ $r_{1},r_{2}\in \mathbb {Q}$ ⁠, and ⁠ $r_{1}+r_{2}a\in (0,1)$ ⁠, then ⁠ $f(r_{1}+r_{2}a)=r_{1}+r_{2}f(a)$ ⁠.

If ⁠ $r_{1},r_{2}\geq 0$ ⁠, then it is true by additivity. If ⁠ $r_{1},r_{2}<0$ ⁠, then ⁠ $r_{1}+r_{2}a<0$ ⁠, contradiction.

If ⁠ $r_{1}\geq 0,r_{2}<0$ ⁠, then since ⁠ $r_{1}+r_{2}a>0$ ⁠, we have ⁠ $r_{1}>0$ ⁠. Let k be a positive integer large enough such that ⁠ ${\frac {r_{1}}{k}},{\frac {-r_{2}a}{k}}\in (0,1)$ ⁠. Then we have by additivity: $f\left({\frac {r_{1}}{k}}+{\frac {r_{2}a}{k}}\right)+f\left({\frac {-r_{2}a}{k}}\right)=f\left({\frac {r_{1}}{k}}\right)$

That is, ${\frac {1}{k}}f\left(r_{1}+r_{2}a\right)+{\frac {-r_{2}}{k}}f\left(a\right)=f\left({\frac {r_{1}}{k}}\right)={\frac {r_{1}}{k}}f(1)={\frac {r_{1}}{k}}$ $\square$

Thus, the graph of f contains ⁠ $L\cap ((0,1)\times \mathbb {R} )$ ⁠, which is dense in ⁠ $(0,1)\times \mathbb {R}$ ⁠.

Expressed differently, nonlinearity in an additive function $f:\mathbb {R} \to \mathbb {R}$ implies there is some $a\in \mathbb {R}$ such that $f(a)-af(1)\neq 0$ . Let $r_{n}:\mathbb {R} \to \mathbb {Q} ,n\in \mathbb {N}$ denote a series of rational approximation functions such that for all $z\in \mathbb {R}$ , $\lim _{n\to \infty }r_{n}(z)=z$ (such as writing z by its first n decimals). Then, as f is $\mathbb {Q}$ -linear, $\lim f(r_{n}(a))=af(1)\neq f(a)$ , even though $\lim r_{n}(a)=a$ . From this, one can construct an orthonormal basis: defining $x_{n}={\frac {r_{n}(f(a))-ar_{n}(f(1))}{r_{n}(f(a)-af(1))}}$ and $y_{n}={\frac {a-r_{n}(a)}{r_{n}(f(a)-af(1))}}$ , $\lim x_{n}=\lim f(y_{n})=1,\lim y_{n}=\lim f(x_{n})=0$ . Thus, for any $r_{x},r_{y}\in \mathbb {Q}$ , $\lim r_{x}x_{n}+r_{y}y_{n}=r_{x}$ and $\lim f(r_{x}x_{n}+r_{y}y_{n})=r_{y}$ , meaning any point $(r_{x},r_{y})\in \mathbb {Q} ^{2}$ can be approximated.

## Existence of nonlinear solutions over the real numbers

The linearity proof given above also applies to ⁠ $f\colon \alpha \mathbb {Q} \to \mathbb {R}$ ⁠, where $\alpha \mathbb {Q}$ is a scaled copy of the rationals. This shows that only linear solutions are permitted when the domain of f is restricted to such sets. Thus, in general, we have $f(\alpha q)=f(\alpha )q$ for all $\alpha \in \mathbb {R}$ and ⁠ $q\in \mathbb {Q}$ ⁠. However, as we will demonstrate below, highly pathological solutions can be found for functions $f\colon \mathbb {R} \to \mathbb {R}$ based on these linear solutions, by viewing the reals as a vector space over the field of rational numbers. Note, however, that this method is nonconstructive, relying as it does on the existence of a (Hamel) basis for any vector space, a statement proved using Zorn's lemma. (In fact, the existence of a basis for every vector space is logically equivalent to the axiom of choice.) There exist models such as the Solovay model where all sets of reals are measurable which are consistent with ZF + DC, and therein all solutions are linear.

To show that solutions other than the ones defined by $f(x)=f(1)x$ exist, we first note that because every vector space has a basis, there is a basis for $\mathbb {R}$ over the field ⁠ $\mathbb {Q}$ ⁠, i.e. a set ${\mathcal {B}}\subset \mathbb {R}$ with the property that any $x\in \mathbb {R}$ can be expressed uniquely as ⁠ $\textstyle x=\sum _{i\in I}{\lambda _{i}x_{i}}$ ⁠, where $\{x_{i}\}_{i\in I}$ is a finite subset of ⁠ ${\mathcal {B}}$ ⁠, and each $\lambda _{i}$ is in ⁠ $\mathbb {Q}$ ⁠. We note that because no explicit basis for $\mathbb {R}$ over $\mathbb {Q}$ can be written down, the pathological solutions defined below likewise cannot be expressed explicitly.

As argued above, the restriction of f to $x_{i}\mathbb {Q}$ must be a linear map for each ⁠ $x_{i}\in {\mathcal {B}}$ ⁠. Moreover, because $x_{i}q\mapsto f(x_{i})q$ for ⁠ $q\in \mathbb {Q}$ ⁠, it is clear that $f(x_{i})/x_{i}$ is the constant of proportionality. In other words, $f\colon x_{i}\mathbb {Q} \to \mathbb {R}$ is the map ⁠ $\xi \mapsto [f(x_{i})/x_{i}]\xi$ ⁠. Since any $x\in \mathbb {R}$ can be expressed as a unique (finite) linear combination of the ⁠ $x_{i}$ ⁠, and $f\colon \mathbb {R} \to \mathbb {R}$ is additive, $f(x)$ is well-defined for all $x\in \mathbb {R}$ and is given by: $f(x)=f{\Big (}\sum _{i\in I}\lambda _{i}x_{i}{\Big )}=\sum _{i\in I}f(x_{i}\lambda _{i})=\sum _{i\in I}f(x_{i})\lambda _{i}.$

It is easy to check that f is a solution to Cauchy's functional equation given a definition of f on the basis elements, ⁠ $f\colon {\mathcal {B}}\to \mathbb {R}$ ⁠. Moreover, it is clear that every solution is of this form. In particular, the solutions of the functional equation are linear if and only if $f(x_{i})/x_{i}$ is constant over all ⁠ $x_{i}\in {\mathcal {B}}$ ⁠. Thus, in a sense, despite the inability to exhibit a nonlinear solution, "most" (in the sense of cardinality) solutions to the Cauchy functional equation are actually nonlinear and pathological.
