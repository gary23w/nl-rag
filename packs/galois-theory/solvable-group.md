---
title: "Solvable group"
source: https://en.wikipedia.org/wiki/Solvable_group
domain: galois-theory
license: CC-BY-SA-4.0
tags: galois theory, galois group, field extension, solvable group
fetched: 2026-07-02
---

# Solvable group

In mathematics, more specifically in the field of group theory, a **solvable group** or **soluble group** is a group that can be constructed from abelian groups using extensions. Equivalently, a solvable group is a group whose derived series terminates in the trivial subgroup.

## Motivation

Historically, the word "solvable" arose from Galois theory and the proof of the general unsolvability of quintic equations. Specifically, a polynomial equation is solvable in radicals if and only if the corresponding Galois group is solvable (note this theorem holds only in characteristic 0). This means associated to a polynomial $f\in F[x]$ there is a tower of field extensions

> $F=F_{0}\subseteq F_{1}\subseteq F_{2}\subseteq \cdots \subseteq F_{m}=K$

such that

1. $F_{i}=F_{i-1}[\alpha _{i}]$ where $\alpha _{i}^{m_{i}}\in F_{i-1}$ , so $\alpha _{i}$ is a solution to the equation $x^{m_{i}}-a$ where $a\in F_{i-1}$
2. $F_{m}$ contains a splitting field for $f(x)$

### Example

The smallest Galois field extension of $\mathbb {Q}$ containing the element

> $a={\sqrt[{5}]{{\sqrt {2}}+{\sqrt {3}}}}$

gives a solvable group. The associated field extensions

> $\mathbb {Q} \subseteq \mathbb {Q} ({\sqrt {2}})\subseteq \mathbb {Q} ({\sqrt {2}},{\sqrt {3}})\subseteq \mathbb {Q} ({\sqrt {2}},{\sqrt {3}})\left(e^{2i\pi /5}\right)\subseteq \mathbb {Q} ({\sqrt {2}},{\sqrt {3}})\left(e^{2i\pi /5},a\right)$

give a solvable group of Galois extensions containing the following composition factors (where 1 is the identity permutation).

- $\mathrm {Aut} \left(\mathbb {Q({\sqrt {2}})} \right/\mathbb {Q} )\cong \mathbb {Z} /2$ with group action $f\left(\pm {\sqrt {2}}\right)=\mp {\sqrt {2}},\ f^{2}=1$ , and minimal polynomial $x^{2}-2$
- $\mathrm {Aut} \left(\mathbb {Q({\sqrt {2}},{\sqrt {3}})} \right/\mathbb {Q({\sqrt {2}})} )\cong \mathbb {Z} /2$ with group action $g\left(\pm {\sqrt {3}}\right)=\mp {\sqrt {3}},\ g^{2}=1$ , and minimal polynomial $x^{2}-3$
- $\mathrm {Aut} \left(\mathbb {Q} ({\sqrt {2}},{\sqrt {3}})\left(e^{2i\pi /5}\right)/\mathbb {Q} ({\sqrt {2}},{\sqrt {3}})\right)\cong \mathbb {Z} /4$ with group action $h^{n}\left(e^{2im\pi /5}\right)=e^{2^{n}im\pi /5},\ 0\leq n\leq 3,\ h^{4}=1$ , and minimal polynomial $x^{4}+x^{3}+x^{2}+x+1=(x^{5}-1)/(x-1)$ containing the 5th roots of unity excluding 1
- $\mathrm {Aut} \left(\mathbb {Q} ({\sqrt {2}},{\sqrt {3}})\left(e^{2i\pi /5},a\right)/\mathbb {Q} ({\sqrt {2}},{\sqrt {3}})\left(e^{2i\pi /5}\right)\right)\cong \mathbb {Z} /5$ with group action $j^{l}(a)=e^{2li\pi /5}a,\ j^{5}=1$ , and minimal polynomial $x^{5}-\left({\sqrt {2}}+{\sqrt {3}}\right)$

Each of the defining group actions (for example, $fgh^{3}j^{4}$ ) changes a single extension while keeping all of the other extensions fixed. The 80 group actions are the set $\{f^{a}g^{b}h^{n}j^{l},\ 0\leq a,b\leq 1,\ 0\leq n\leq 3,\ 0\leq l\leq 4\}$ .

This group is not abelian. For example, $hj(a)=h(e^{2i\pi /5}a)=e^{4i\pi /5}a$ , whilst $jh(a)=j(a)=e^{2i\pi /5}a$ , and in fact, $jh=hj^{3}$ .

It is isomorphic to $(\mathbb {Z} _{5}\rtimes _{\varphi }\mathbb {Z} _{4})\times (\mathbb {Z} _{2}\times \mathbb {Z} _{2})$ , where $\varphi _{h}(j)=hjh^{-1}=j^{2}$ , defined using the semidirect product and direct product of the cyclic groups. $\mathbb {Z} _{4}$ is not a normal subgroup.

## Definition

A group *G* is called **solvable** if it has a subnormal series whose factor groups (quotient groups) are all abelian, that is, if there are subgroups

$1=G_{0}\triangleleft G_{1}\triangleleft \cdots \triangleleft G_{k}=G$

meaning that *G**j*−1 is normal in *Gj*, such that *Gj*/*G**j*−1 is an abelian group, for *j* = 1, 2, ..., *k*.

Or equivalently, if its derived series, the descending normal series

$G\triangleright G^{(1)}\triangleright G^{(2)}\triangleright \cdots ,$

where every subgroup is the commutator subgroup of the previous one, eventually reaches the trivial subgroup of *G*. These two definitions are equivalent, since for every group *H* and every normal subgroup *N* of *H*, the quotient *H*/*N* is abelian if and only if *N* includes the commutator subgroup of *H*. The least *n* such that *G*(*n*) = 1 is called the **derived length** of the solvable group *G*.

For finite groups, an equivalent definition is that a solvable group is a group with a composition series all of whose factors are cyclic groups of prime order. This is equivalent because a finite group has finite composition length, and every simple abelian group is cyclic of prime order. The Jordan–Hölder theorem guarantees that if one composition series has this property, then all composition series will have this property as well. For the Galois group of a polynomial, these cyclic groups correspond to *n*th roots (radicals) over some field. The equivalence does not necessarily hold for infinite groups: for example, since every nontrivial subgroup of the group **Z** of integers under addition is isomorphic to **Z** itself, it has no composition series, but the normal series {0, **Z**}, with its only factor group isomorphic to **Z**, proves that it is in fact solvable.

## Examples

### Abelian groups

The basic example of solvable groups are abelian groups. They are trivially solvable since a subnormal series is formed by just the group itself and the trivial group. But non-abelian groups may or may not be solvable.

### Nilpotent groups

More generally, all nilpotent groups are solvable. In particular, finite *p*-groups are solvable, as all finite *p*-groups are nilpotent.

#### Quaternion groups

In particular, the quaternion group is a solvable group given by the group extension

> $1\to \mathbb {Z} /2\to Q\to \mathbb {Z} /2\times \mathbb {Z} /2\to 1$

where the kernel $\mathbb {Z} /2$ is the subgroup generated by $-1$ .

### Group extensions

Group extensions form the prototypical examples of solvable groups. That is, if G and $G'$ are solvable groups, then any extension

> $1\to G\to G''\to G'\to 1$

defines a solvable group $G''$ . In fact, all solvable groups can be formed from such group extensions.

### Non-abelian group which is non-nilpotent

A small example of a solvable, non-nilpotent group is the symmetric group *S*3. In fact, as the smallest simple non-abelian group is *A*5, (the alternating group of degree 5) it follows that *every* group with order less than 60 is solvable.

### Finite groups of odd order

The Feit–Thompson theorem states that every finite group of odd order is solvable. In particular this implies that if a finite group is simple, it is either a prime cyclic or of even order.

### Non-example

The group *S*5 is not solvable—it has a composition series {E, *A*5, *S*5} (and the Jordan–Hölder theorem states that every other composition series is equivalent to that one), giving factor groups isomorphic to *A*5 and *C*2; and *A*5 is not abelian. Generalizing this argument, coupled with the fact that *A**n* is a normal, maximal, non-abelian simple subgroup of *S**n* for *n* > 4, we see that *S**n* is not solvable for *n* > 4. This is a key step in the proof that for every *n* > 4 there are polynomials of degree *n* which are not solvable by radicals (Abel–Ruffini theorem). This property is also used in complexity theory in the proof of Barrington's theorem.

### Subgroups of GL2

Consider the subgroups

> $B=\left\{{\begin{bmatrix}*&*\\0&*\end{bmatrix}}\right\}{\text{, }}U=\left\{{\begin{bmatrix}1&*\\0&1\end{bmatrix}}\right\}$ of $GL_{2}(\mathbb {F} )$

for some field $\mathbb {F}$ . Then, the group quotient $B/U$ can be found by taking arbitrary elements in $B,U$ , multiplying them together, and figuring out what structure this gives. So

> ${\begin{bmatrix}a&b\\0&c\end{bmatrix}}\cdot {\begin{bmatrix}1&d\\0&1\end{bmatrix}}={\begin{bmatrix}a&ad+b\\0&c\end{bmatrix}}$

Note the determinant condition on $GL_{2}$ implies $ac\neq 0$ , hence $\mathbb {F} ^{\times }\times \mathbb {F} ^{\times }\subset B$ is a subgroup (which are the matrices where $b=0$ ). For fixed $a,b$ , the linear equation $ad+b=0$ implies $d=-b/a$ , which is an arbitrary element in $\mathbb {F}$ since $b\in \mathbb {F}$ . Since we can take any matrix in B and multiply it by the matrix

> ${\begin{bmatrix}1&d\\0&1\end{bmatrix}}$

with $d=-b/a$ , we can get a diagonal matrix in B . This shows the quotient group $B/U\cong \mathbb {F} ^{\times }\times \mathbb {F} ^{\times }$ .

#### Remark

Notice that this description gives the decomposition of B as $\mathbb {F} \rtimes (\mathbb {F} ^{\times }\times \mathbb {F} ^{\times })$ where $(a,c)$ acts on b by $(a,c)(b)=ab$ . This implies $(a,c)(b+b')=(a,c)(b)+(a,c)(b')=ab+ab'$ . Also, a matrix of the form

> ${\begin{bmatrix}a&b\\0&c\end{bmatrix}}$

corresponds to the element $(b)\times (a,c)$ in the group.

### Borel subgroups

For a linear algebraic group G , a Borel subgroup is defined as a subgroup which is closed, connected, and solvable in G , and is a maximal possible subgroup with these properties (note the first two are topological properties). For example, in $GL_{n}$ and $SL_{n}$ the groups of upper-triangular, or lower-triangular matrices are two of the Borel subgroups. The example given above, the subgroup B in $GL_{2}$ , is a Borel subgroup.

#### Borel subgroup in GL3

In $GL_{3}$ there are the subgroups

> $B=\left\{{\begin{bmatrix}*&*&*\\0&*&*\\0&0&*\end{bmatrix}}\right\},{\text{ }}U_{1}=\left\{{\begin{bmatrix}1&*&*\\0&1&*\\0&0&1\end{bmatrix}}\right\}$

Notice $B/U_{1}\cong \mathbb {F} ^{\times }\times \mathbb {F} ^{\times }\times \mathbb {F} ^{\times }$ , hence the Borel group has the form

> $U\rtimes (\mathbb {F} ^{\times }\times \mathbb {F} ^{\times }\times \mathbb {F} ^{\times })$

#### Borel subgroup in product of simple linear algebraic groups

In the product group $GL_{n}\times GL_{m}$ the Borel subgroup can be represented by matrices of the form

> ${\begin{bmatrix}T&0\\0&S\end{bmatrix}}$

where T is an $n\times n$ upper triangular matrix and S is a $m\times m$ upper triangular matrix.

### Z-groups

Any finite group whose *p*-Sylow subgroups are cyclic is a semidirect product of two cyclic groups, in particular solvable. Such groups are called Z-groups.

## OEIS values

Numbers of solvable groups with order *n* are (start with *n* = 0)

0, 1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51, 1, 2, 1, 14, 1, 2, 2, 14, 1, 6, 1, 4, 2, 2, 1, 52, 2, 5, 1, 5, 1, 15, 2, 13, 2, 2, 1, 12, 1, 2, 4, 267, 1, 4, 1, 5, 1, 4, 1, 50, ... (sequence

A201733

in the

OEIS

)

Orders of non-solvable groups are

60, 120, 168, 180, 240, 300, 336, 360, 420, 480, 504, 540, 600, 660, 672, 720, 780, 840, 900, 960, 1008, 1020, 1080, 1092, 1140, 1176, 1200, 1260, 1320, 1344, 1380, 1440, 1500, ... (sequence

A056866

in the

OEIS

)

## Properties

Solvability is closed under a number of operations.

- If *G* is solvable, and *H* is a subgroup of *G*, then *H* is solvable.
- If *G* is solvable, and there is a homomorphism from *G* onto *H*, then *H* is solvable; equivalently (by the first isomorphism theorem), if *G* is solvable, and *N* is a normal subgroup of *G*, then *G*/*N* is solvable.
- The previous properties can be expanded into the following "three for the price of two" property: *G* is solvable if and only if both *N* and *G*/*N* are solvable.
- In particular, if *G* and *H* are solvable, the direct product *G* × *H* is solvable.

Solvability is closed under group extension:

- If *H* and *G*/*H* are solvable, then so is *G*; in particular, if *N* and *H* are solvable, their semidirect product is also solvable.

It is also closed under wreath product:

- If *G* and *H* are solvable, and *X* is a *G*-set, then the wreath product of *G* and *H* with respect to *X* is also solvable.

For any positive integer *N*, the solvable groups of derived length at most *N* form a subvariety of the variety of groups, as they are closed under the taking of homomorphic images, subalgebras, and (direct) products. The direct product of a sequence of solvable groups with unbounded derived length is not solvable, so the class of all solvable groups is not a variety.

## Burnside's theorem

Burnside's theorem states that if *G* is a finite group of order *paqb* where *p* and *q* are prime numbers, and *a* and *b* are non-negative integers, then *G* is solvable.

### Supersolvable groups

As a strengthening of solvability, a group *G* is called **supersolvable** (or **supersoluble**) if it has an *invariant* normal series whose factors are all cyclic. Since a normal series has finite length by definition, uncountable groups are not supersolvable. In fact, all supersolvable groups are finitely generated, and an abelian group is supersolvable if and only if it is finitely generated. The alternating group *A*4 is an example of a finite solvable group that is not supersolvable.

If we restrict ourselves to finitely generated groups, we can consider the following arrangement of classes of groups:

cyclic

<

abelian

<

nilpotent

<

supersolvable

<

polycyclic

<

solvable

<

finitely generated group

.

### Virtually solvable groups

A group *G* is called **virtually solvable** if it has a solvable subgroup of finite index. This is similar to virtually abelian. Clearly all solvable groups are virtually solvable, since one can just choose the group itself, which has index 1. Virtually solvable groups are one of the two alternatives in the Tits alternative on finitely generated linear groups.

### Hypoabelian

A solvable group is one whose derived series reaches the trivial subgroup at a *finite* stage. For an infinite group, the finite derived series may not stabilize, but the transfinite derived series always stabilizes. A group whose transfinite derived series reaches the trivial group is called a **hypoabelian group**, and every solvable group is a hypoabelian group. The first ordinal *α* such that *G*(*α*) = *G*(*α*+1) is called the (transfinite) derived length of the group *G*, and it has been shown that every ordinal is the derived length of some group (Malcev 1949).

### p-solvable

A finite group is p-solvable for some prime p if every factor in the composition series is a p-group or has order prime to p. A finite group is solvable iff it is p-solvable for every p.
