---
title: "Local field"
source: https://en.wikipedia.org/wiki/Local_field
domain: p-adic-analysis
license: CC-BY-SA-4.0
tags: p-adic analysis, p-adic number, hensel's lemma, local field
fetched: 2026-07-02
---

# Local field

In mathematics, a **local field** is a locally compact Hausdorff non-discrete topological field. Local fields find many applications in algebraic number theory, where they arise naturally as completions of global fields. Moreover, tools like integration and Fourier analysis are available for functions defined on local fields.

Given a local field, an absolute value can be defined on it which gives rise to a complete metric that generates its topology. There are two basic types of local field: those called **Archimedean local fields** in which the absolute value is Archimedean, and those called **non-Archimedean local fields** in which it is not. Non-Archimedean local fields can also be defined as those fields which are complete with respect to a metric induced by a discrete valuation whose residue field is finite.

Every local field is isomorphic (as a topological field) to one of the following:

- Archimedean local fields (characteristic zero): the real numbers $\mathbb {R}$ , and the complex numbers $\mathbb {C}$ .
- Non-Archimedean local fields of characteristic zero: finite extensions of the *p*-adic numbers $\mathbb {Q} _{p}$ (where p is any prime number).
- Non-Archimedean local fields of characteristic p : the field $\mathbb {F} _{q}((t))$ of formal Laurent series in the variable t over a finite field $\mathbb {F} _{q}$ , where q is a power of p .

## Module, absolute value, metric

Given a local field F , a "module function" on F can be defined as follows. First, consider the additive group of the field. As a locally compact topological group, it has a unique (up to positive scalar multiple) Haar measure $\mu$ . The module of an element a of F is defined so as to measure the change in size of a set after multiplying it by a . Specifically, define $\operatorname {mod} _{K}:F\to \mathbb {R}$ by

$\operatorname {mod} _{K}(a)={\frac {\mu (aX)}{\mu (X)}}$

for any measurable subset X of F (with $0<\mu (X)<\infty$ ). This module does not depend on X nor on the choice of Haar measure $\mu$ (since the same scalar multiple ambiguity will occur in both the numerator and the denominator). The function $\operatorname {mod} _{K}$ is continuous and satisfies

$\operatorname {mod} _{K}(ab)=\operatorname {mod} _{K}(a)\operatorname {mod} _{K}(b),$

$\operatorname {mod} _{K}(a+b)\leq A\sup \left(\operatorname {mod} _{K}(a),\operatorname {mod} _{K}(b)\right)$

for some constant A that only depends on F .

Using $\operatorname {mod} _{K}$ , one may then define an absolute value $|\cdot |$ on F that induces a metric d on F (by setting $d(x,y)=|x-y|$ ), such that F is complete with respect to this metric, and the metric induces the given topology on F .

## Basic features of non-Archimedean local fields

For a non-Archimedean local field F with absolute value $|\cdot |$ , the following objects are important:

- its **ring of integers** ${\mathcal {O}}=\{a\in F:|a|\leq 1\}$ which is a discrete valuation ring, is the closed unit ball of F , and is compact;

- the **units** in its ring of integers ${\mathcal {O}}^{\times }=\{a\in F:|a|=1\}$ which form a group and is the unit sphere of F ;

- the unique non-zero prime ideal ${\mathfrak {m}}=\{a\in F:|a|<1\}$ in its ring of integers, which is the open unit ball of F ;

- a generator $\varpi$ of ${\mathfrak {m}}$ called a **uniformizer** of F ; and

- its residue field $k={\mathcal {O}}/{\mathfrak {m}}$ which is finite (since it is compact and discrete).

Every non-zero element a of F can be written as $a=\varpi ^{n}u$ with u a unit in ${\mathcal {O}}^{\times }$ , and n a unique integer. The **normalized valuation** of F is the surjective function $v:F\to \mathbb {Z} \cup \{\infty \}$ defined by sending a non-zero a to the unique integer n such that $a=\varpi ^{n}u$ with u a unit, and by sending 0 to $\infty$ . If q is the cardinality of the residue field, the absolute value on F induced by its structure as a local field is given by:

$|a|=q^{-v(a)}.$

An equivalent and very important definition of a non-Archimedean local field is that it is a field that is complete with respect to a discrete valuation and whose residue field is finite.

### Examples

- ***p*-adic numbers**: the ring of integers of $\mathbb {Q} _{p}$ is the ring of p -adic integers $\mathbb {Z} _{p}$ . Its prime ideal is $p\mathbb {Z} _{p}$ and its residue field is $\mathbb {Z} /p\mathbb {Z}$ . Every non-zero element of $\mathbb {Q} _{p}$ can be written as $up^{n}$ where u is a unit in $\mathbb {Z} _{p}$ and n is an integer, with $v(up^{n})=n$ for the normalized valuation.

- **Formal Laurent series over a finite field**: the ring of integers of $\mathbb {F} _{q}((t))$ is the ring of formal power series $\mathbb {F} _{q}[[t]]$ . Its maximal ideal is $(t)$ (i.e. the set of power series whose constant terms are zero) and its residue field is $\mathbb {F} _{q}$ . Its normalized valuation is related to the (lower) degree of a formal Laurent series as follows:

$v{\biggl (}\sum _{i=-m}^{\infty }a_{i}T^{i}{\biggr )}=-m$

where

$a_{-m}$

is non-zero.

- The field $\mathbb {C} ((t))$ of formal Laurent series over the complex numbers is *not* a local field: its residue field is $\mathbb {C} ((t))/(t)=\mathbb {C}$ , which is not finite.

### Higher unit groups

The ***n*-th higher unit group** of a non-Archimedean local field F is

$U^{(n)}=1+{\mathfrak {m}}^{n}=\left\{u\in {\mathcal {O}}^{\times }:u\equiv 1\,(\mathrm {mod} \,{\mathfrak {m}}^{n})\right\}$

for $n\geq 1$ . The group $U^{(1)}$ is called the **group of principal units**. The full unit group ${\mathcal {O}}^{\times }$ is denoted $U^{(1)}$ .

The higher unit groups form a decreasing filtration of the unit group

${\mathcal {O}}^{\times }\supseteq U^{(1)}\supseteq U^{(2)}\supseteq \cdots$

whose quotients are given by

${\mathcal {O}}^{\times }/U^{(n)}\cong \left({\mathcal {O}}/{\mathfrak {m}}^{n}\right)^{\times }{\text{ and }}\,U^{(n)}/U^{(n+1)}\approx {\mathcal {O}}/{\mathfrak {m}}$

for $n\geq 1$ . (Here " $\approx$ " means a non-canonical isomorphism.)

### Structure of the unit group

The multiplicative group of non-zero elements of a non-Archimedean local field F is isomorphic to

$F^{\times }\cong (\varpi )\times \mu _{q-1}\times U^{(1)}$

where q is the order of the residue field, and $\mu _{q-1}$ is the group of ( $q-1$ )-st roots of unity in F . Its structure as an abelian group depends on its characteristic:

- If F has characteristic p , then

$F^{\times }\cong \mathbb {Z} \oplus \mathbb {Z} /{(q-1)}\oplus \mathbb {Z} _{p}^{\mathbb {N} }$

where

$\mathbb {N}$

denotes the

natural numbers

;

- If F has characteristic zero, i.e. it is a finite extension of $\mathbb {Q} _{p}$ of degree d , then

$F^{\times }\cong \mathbb {Z} \oplus \mathbb {Z} /(q-1)\oplus \mathbb {Z} /p^{a}\oplus \mathbb {Z} _{p}^{d}$

where

$a\geq 0$

is defined so that the group of

p

-power roots of unity in

F

is

$\mu _{p^{a}}$

.

## Theory of local fields

This theory includes the study of types of local fields, extensions of local fields using Hensel's lemma, Galois extensions of local fields, ramification groups, filtrations of Galois groups of local fields, the behavior of the norm map on local fields, the local reciprocity homomorphism and existence theorem in local class field theory, local Langlands correspondence, Hodge-Tate theory (also called *p*-adic Hodge theory), explicit formulas for the Hilbert symbol in local class field theory.

## Variant definitions

The definition for "local field" adopted in this article, as a locally compact Hausdorff non-discrete topological field, is common today. Some authors however reserve the term "local field" for what we have called "non-Archimedean local field".

Research papers in modern number theory often consider a more general notion of non-Archimedean local field, requiring only that they be complete with respect to a discrete valuation and that the residue field be perfect of positive characteristic, not necessarily finite.

In his book *Local Fields*, Serre defines "local fields" as fields that are complete with respect to a discrete valuation, without any restriction on the residue field, leading to a notion that is more general still.

## Higher-dimensional local fields

A local field is sometimes called a *one-dimensional local field*.

A non-Archimedean local field can be viewed as the field of fractions of the completion of the local ring of a one-dimensional arithmetic scheme of rank 1 at its non-singular point.

For a non-negative integer n , an n -dimensional local field is a complete discrete valuation field whose residue field is an $(n-1)$ -dimensional local field. Depending on the definition of local field, a *zero-dimensional local field* is then either a finite field (with the definition used in this article), or a perfect field of positive characteristic.

From the geometric point of view, n -dimensional local fields with last finite residue field are naturally associated to a complete flag of subschemes of an n -dimensional arithmetic scheme.
