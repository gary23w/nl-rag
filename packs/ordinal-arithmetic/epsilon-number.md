---
title: "Epsilon number"
source: https://en.wikipedia.org/wiki/Epsilon_number
domain: ordinal-arithmetic
license: CC-BY-SA-4.0
tags: ordinal arithmetic, ordinal number, transfinite induction, cantor normal form
fetched: 2026-07-02
---

# Epsilon number

In mathematics, the **epsilon numbers** are a collection of transfinite numbers whose defining property is that they are fixed points of an **exponential map**. Consequently, they are not reachable from 0 via a finite series of applications of the chosen exponential map and of "weaker" operations like addition and multiplication. The original epsilon numbers were introduced by Georg Cantor in the context of ordinal arithmetic; they are the ordinal numbers *ε* that satisfy the equation $\varepsilon =\omega ^{\varepsilon },$ in which ω is the smallest infinite ordinal.

The least such ordinal is ***ε*0** (pronounced **epsilon nought** (chiefly British), **epsilon naught** (chiefly American), or **epsilon zero**), which can be viewed as the "limit" obtained by transfinite recursion from a sequence of smaller limit ordinals: $\varepsilon _{0}=\omega ^{\omega ^{\omega ^{\cdot ^{\cdot ^{\cdot }}}}}=\sup \left\{\omega ,\omega ^{\omega },\omega ^{\omega ^{\omega }},\omega ^{\omega ^{\omega ^{\omega }}},\dots \right\},$ where sup is the supremum, which is equivalent to set union in the case of the von Neumann representation of ordinals.

Larger ordinal fixed points of the exponential map are indexed by ordinal subscripts, resulting in $\varepsilon _{1},\varepsilon _{2},\ldots ,\varepsilon _{\omega },\varepsilon _{\omega +1},\ldots ,\varepsilon _{\varepsilon _{0}},\ldots ,\varepsilon _{\varepsilon _{1}},\ldots ,\varepsilon _{\varepsilon _{\varepsilon _{\cdot _{\cdot _{\cdot }}}}},\ldots \zeta _{0}=\varphi _{2}(0)$ . The ordinal *ε*0 is still countable, as is any epsilon number whose index is countable. Uncountable ordinals also exist, along with uncountable epsilon numbers whose index is an uncountable ordinal.

The smallest epsilon number *ε*0 appears in many induction proofs, because for many purposes transfinite induction is only required up to *ε*0 (as in Gentzen's consistency proof and the proof of Goodstein's theorem). Its use by Gentzen to prove the consistency of Peano arithmetic, along with Gödel's second incompleteness theorem, show that Peano arithmetic cannot prove the well-foundedness of this ordering (it is in fact the least ordinal with this property, and as such, in proof-theoretic ordinal analysis, is used as a measure of the strength of the theory of Peano arithmetic).

Many larger epsilon numbers can be defined using the Veblen function.

A more general class of epsilon numbers has been identified by John Horton Conway and Donald Knuth in the surreal number system, consisting of all surreals that are fixed points of the base-ω exponential map *x* → *ω**x*.

Hessenberg (1906) defined gamma numbers (see additively indecomposable ordinal) to be numbers *γ* > 0 such that *α* + *γ* = *γ* whenever *α* < *γ*, and delta numbers (see multiplicatively indecomposable ordinal) to be numbers *δ* > 1 such that *αδ* = *δ* whenever 0 < *α* < *δ*, and epsilon numbers to be numbers *ε* > 2 such that *α**ε* = *ε* whenever 1 < *α* < *ε*. His gamma numbers are those of the form *ω**β*, and his delta numbers are those of the form *ω**ω**β*.

## Ordinal ε numbers

The standard definition of ordinal exponentiation with base α is:

- $\alpha ^{0}=1\,,$
- $\alpha ^{\beta }=\alpha ^{\beta -1}\cdot \alpha \,,$ when $\beta$ has an immediate predecessor $\beta -1$ .
- $\alpha ^{\beta }=\sup \lbrace \alpha ^{\delta }\mid 0<\delta <\beta \rbrace$ , whenever $\beta$ is a limit ordinal.

From this definition, it follows that for any fixed ordinal *α* > 1, the mapping $\beta \mapsto \alpha ^{\beta }$ is a normal function, so it has arbitrarily large fixed points by the fixed-point lemma for normal functions. When $\alpha =\omega$ , these fixed points are precisely the ordinal epsilon numbers.

- $\varepsilon _{0}=\sup \left\lbrace 1,\omega ,\omega ^{\omega },\omega ^{\omega ^{\omega }},\omega ^{\omega ^{\omega ^{\omega }}},\ldots \right\rbrace \,,$
- $\varepsilon _{\beta }=\sup \left\lbrace {\varepsilon _{\beta -1}+1},\omega ^{\varepsilon _{\beta -1}+1},\omega ^{\omega ^{\varepsilon _{\beta -1}+1}},\omega ^{\omega ^{\omega ^{\varepsilon _{\beta -1}+1}}},\ldots \right\rbrace \,,$ when $\beta$ has an immediate predecessor $\beta -1$ .
- $\varepsilon _{\beta }=\sup \lbrace \varepsilon _{\delta }\mid \delta <\beta \rbrace$ , whenever $\beta$ is a limit ordinal.

Because

$\omega ^{\varepsilon _{0}+1}=\omega ^{\varepsilon _{0}}\cdot \omega ^{1}=\varepsilon _{0}\cdot \omega \,,$

$\omega ^{\omega ^{\varepsilon _{0}+1}}=\omega ^{(\varepsilon _{0}\cdot \omega )}={(\omega ^{\varepsilon _{0}})}^{\omega }=\varepsilon _{0}^{\omega }\,,$

$\omega ^{\omega ^{\omega ^{\varepsilon _{0}+1}}}=\omega ^{{\varepsilon _{0}}^{\omega }}=\omega ^{{\varepsilon _{0}}^{1+\omega }}=\omega ^{(\varepsilon _{0}\cdot {\varepsilon _{0}}^{\omega })}={(\omega ^{\varepsilon _{0}})}^{{\varepsilon _{0}}^{\omega }}={\varepsilon _{0}}^{{\varepsilon _{0}}^{\omega }}\,,$

a different sequence with the same supremum, $\varepsilon _{1}$ , is obtained by starting from 0 and exponentiating with base *ε*0 instead:

$\varepsilon _{1}=\sup \left\{1,\varepsilon _{0},{\varepsilon _{0}}^{\varepsilon _{0}},{\varepsilon _{0}}^{{\varepsilon _{0}}^{\varepsilon _{0}}},\ldots \right\}.$

Generally, the epsilon number $\varepsilon _{\beta }$ indexed by any ordinal that has an immediate predecessor $\beta -1$ can be constructed similarly.

$\varepsilon _{\beta }=\sup \left\{1,\varepsilon _{\beta -1},\varepsilon _{\beta -1}^{\varepsilon _{\beta -1}},\varepsilon _{\beta -1}^{\varepsilon _{\beta -1}^{\varepsilon _{\beta -1}}},\dots \right\}.$

In particular, whether or not the index β is a limit ordinal, $\varepsilon _{\beta }$ is a fixed point not only of base ω exponentiation but also of base δ exponentiation for all ordinals $1<\delta <\varepsilon _{\beta }$ .

Since the epsilon numbers are an unbounded subclass of the ordinal numbers, they are enumerated using the ordinal numbers themselves. For any ordinal number $\beta$ , $\varepsilon _{\beta }$ is the least epsilon number (fixed point of the exponential map) not already in the set $\{\varepsilon _{\delta }\mid \delta <\beta \}$ . It might appear that this is the non-constructive equivalent of the constructive definition using iterated exponentiation; but the two definitions are equally non-constructive at steps indexed by limit ordinals, which represent transfinite recursion of a higher order than taking the supremum of an exponential series.

The following facts about epsilon numbers are straightforward to prove:

- Although it is quite a large number, $\varepsilon _{0}$ is still countable, being a countable union of countable ordinals; in fact, $\varepsilon _{\beta }$ is countable if and only if $\beta$ is countable.
- The union (or supremum) of any non-empty set of epsilon numbers is an epsilon number; so for instance $\varepsilon _{\omega }=\sup\{\varepsilon _{0},\varepsilon _{1},\varepsilon _{2},\ldots \}$ is an epsilon number. Thus, the mapping $\beta \mapsto \varepsilon _{\beta }$ is a normal function.
- The initial ordinal of any uncountable cardinal is an epsilon number. $\alpha \geq 1\Rightarrow \varepsilon _{\omega _{\alpha }}=\omega _{\alpha }\,.$

## Representation of ε0 by rooted trees

Any epsilon number ε has Cantor normal form $\varepsilon =\omega ^{\varepsilon }$ , which means that the Cantor normal form is not very useful for epsilon numbers. The ordinals less than *ε*0, however, can be usefully described by their Cantor normal forms, which leads to a representation of *ε*0 as the ordered set of all finite rooted trees, as follows. Any ordinal $\alpha <\varepsilon _{0}$ has Cantor normal form $\alpha =\omega ^{\beta _{1}}+\omega ^{\beta _{2}}+\cdots +\omega ^{\beta _{k}}$ where *k* is a natural number and $\beta _{1},\ldots ,\beta _{k}$ are ordinals with $\alpha >\beta _{1}\geq \cdots \geq \beta _{k}$ , uniquely determined by $\alpha$ . Each of the ordinals $\beta _{1},\ldots ,\beta _{k}$ in turn has a similar Cantor normal form. We obtain the finite rooted tree representing α by joining the roots of the trees representing $\beta _{1},\ldots ,\beta _{k}$ to a new root. (This has the consequence that the number 0 is represented by a single root while the number $1=\omega ^{0}$ is represented by a tree containing a root and a single leaf.) An order on the set of finite rooted trees is defined recursively: we first order the subtrees joined to the root in decreasing order, and then use lexicographic order on these ordered sequences of subtrees. In this way the set of all finite rooted trees becomes a well-ordered set which is order isomorphic to *ε*0.

This representation is related to the proof of the hydra theorem, which represents decreasing sequences of ordinals as a graph-theoretic game.

## Veblen hierarchy

The fixed points of the "epsilon mapping" $x\mapsto \varepsilon _{x}$ form a normal function, whose fixed points form a normal function; this is known as the Veblen hierarchy (the Veblen functions with base *φ*0(*α*) = *ω**α*). In the notation of the Veblen hierarchy, the epsilon mapping is *φ*1, and its fixed points are enumerated by *φ*2 (see ordinal collapsing function.)

Continuing in this vein, one can define maps *φ**α* for progressively larger ordinals α (including, by this rarefied form of transfinite recursion, limit ordinals), with progressively larger least fixed points *φ**α*+1(0). The least ordinal not reachable from 0 by this procedure—i. e., the least ordinal α for which *φ**α*(0) = *α*, or equivalently the first fixed point of the map $\alpha \mapsto \varphi _{\alpha }(0)$ —is the Feferman–Schütte ordinal Γ0. In a set theory where such an ordinal can be proved to exist, one has a map Γ that enumerates the fixed points Γ0, Γ1, Γ2, ... of $\alpha \mapsto \varphi _{\alpha }(0)$ ; these are all still epsilon numbers, as they lie in the image of *φ**β* for every *β* ≤ Γ0, including of the map *φ*1 that enumerates epsilon numbers.

## Surreal ε numbers

In *On Numbers and Games*, the classic exposition on surreal numbers, John Horton Conway provided a number of examples of concepts that had natural extensions from the ordinals to the surreals. One such function is the $\omega$ -map $n\mapsto \omega ^{n}$ ; this mapping generalises naturally to include all surreal numbers in its domain, which in turn provides a natural generalisation of the Cantor normal form for surreal numbers.

It is natural to consider any fixed point of this expanded map to be an epsilon number, whether or not it happens to be strictly an ordinal number. Some examples of non-ordinal epsilon numbers are

$\varepsilon _{-1}=\left\{0,1,\omega ,\omega ^{\omega },\ldots \mid \varepsilon _{0}-1,\omega ^{\varepsilon _{0}-1},\ldots \right\}$

and

$\varepsilon _{1/2}=\left\{\varepsilon _{0}+1,\omega ^{\varepsilon _{0}+1},\ldots \mid \varepsilon _{1}-1,\omega ^{\varepsilon _{1}-1},\ldots \right\}.$

There is a natural way to define $\varepsilon _{n}$ for every surreal number *n*, and the map remains order-preserving. Conway goes on to define a broader class of "irreducible" surreal numbers that includes the epsilon numbers as a particularly interesting subclass.
