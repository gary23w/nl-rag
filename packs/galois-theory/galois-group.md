---
title: "Galois group"
source: https://en.wikipedia.org/wiki/Galois_group
domain: galois-theory
license: CC-BY-SA-4.0
tags: galois theory, galois group, field extension, solvable group
fetched: 2026-07-02
---

# Galois group

In Galois theory, a branch of abstract algebra, the **Galois group** of a certain type of field extension is a symmetry group characterizing how it extends the base field. Each element of the Galois group is a transformation of the field extension which leaves each element of the base field fixed.

This connection between fields and groups, given by the fundamental theorem of Galois theory, allows for group-theoretic tools to be used on problems in field theory, such as describing the solutions to quintic polynomials. The study of field extensions and their relationship to the polynomials that give rise to them via Galois groups is called Galois theory, so named in honor of Évariste Galois who first discovered them.

## Informal description

A field is a set, like the rational numbers $\mathbb {Q}$ or the real numbers $\mathbb {R}$ , on which the four operations of addition, subtraction, multiplication, and division are defined and have certain standardized properties. Fields can be extended into larger fields with the same operations, such as how $\mathbb {Q}$ can be extended to $\mathbb {R}$ and $\mathbb {R}$ can be extended to the complex numbers $\mathbb {C}$ . These extensions may arise when there is no solution to a given equation within the smaller field (the base field) but there is in the extension: for instance, $\mathbb {x^{2}=2}$ has no solution in $\mathbb {Q}$ but has two solutions in its extension $\mathbb {R}$ .

The problem of identifying and classifying the extensions of a field can be made easier by using group theory. Each extension of a field adds additional structure that is "invisible" to the base field, and the Galois group describes that structure. It does this by considering transformations which change the extension but leave the base field unchanged. For instance, the transformation of complex conjugation, which maps $a+bi\mapsto a-bi$ , leaves every real number fixed but generally does not leave complex numbers fixed. The "Galois group of $\mathbb {C}$ over $\mathbb {R}$ ", written ${\text{Gal}}(\mathbb {C} /\mathbb {R} )$ , is the cyclic group of order 2 (equivalently, the integers modulo 2), with its one non-identity element representing this transformation of complex conjugation.

## Definition

Suppose that E is an extension of the field F (written as $E/F$ and read "*E* over *F*"). An automorphism of $E/F$ is defined to be an automorphism of E that fixes F pointwise. In other words, an automorphism of $E/F$ is an isomorphism $\alpha :E\to E$ such that $\alpha (x)=x$ for each $x\in F$ . The set of all automorphisms of $E/F$ forms a group with the operation of function composition. This group is sometimes denoted by $\operatorname {Aut} (E/F).$

If $E/F$ is a Galois extension, then $\operatorname {Aut} (E/F)$ is called the **Galois group** of $E/F$ , and is usually denoted by $\operatorname {Gal} (E/F)$ .

If $E/F$ is not a Galois extension, then the Galois group of $E/F$ is sometimes defined as $\operatorname {Aut} (K/F)$ , where K is the Galois closure of E .

### Galois group of a polynomial

Another definition of the Galois group comes from the Galois group of an irreducible polynomial $f\in F[x]$ . If there is a field $K/F$ such that f factors as a product of distinct linear polynomials

$f(x)=(x-\alpha _{1})\cdots (x-\alpha _{k})\in K[x]$

over the field K , then the **Galois group of the polynomial** f is defined as the Galois group of $K/F$ where K is minimal among all such fields.

## Structure of Galois groups

### Fundamental theorem of Galois theory

One of the important structure theorems from Galois theory comes from the fundamental theorem of Galois theory. This states that given a finite Galois extension $K/k$ , there is a bijection between the set of subfields $k\subset E\subset K$ and the subgroups $H\subset G.$ Then, E is given by the set of invariants of K under the action of H , so

$E=K^{H}=\{a\in K:\forall g\in H,\ ga=a\}$

Moreover, if H is a normal subgroup then $G/H\cong \operatorname {Gal} (E/k)$ . And conversely, if $E/k$ is a normal field extension, then the associated subgroup in $\operatorname {Gal} (K/k)$ is a normal group.

### Lattice structure

Suppose $K_{1},K_{2}$ are Galois extensions of k with Galois groups $G_{1},G_{2}.$ The field $K_{1}K_{2}$ with Galois group $G=\operatorname {Gal} (K_{1}K_{2}/k)$ has an injection $G\to G_{1}\times G_{2}$ which is an isomorphism whenever $K_{1}\cap K_{2}=k$ .

#### Inducting

As a corollary, this can be inducted finitely many times. Given Galois extensions $K_{1},\ldots ,K_{n}/k$ where $K_{i+1}\cap (K_{1}\cdots K_{i})=k,$ then there is an isomorphism of the corresponding Galois groups:

$\operatorname {Gal} (K_{1}\cdots K_{n}/k)\cong \operatorname {Gal} (K_{1}/k)\times \cdots \times \operatorname {Gal} (K_{n}/k).$

## Examples

In the following examples F is a field, and $\mathbb {C} ,\mathbb {R} ,\mathbb {Q}$ are the fields of complex, real, and rational numbers, respectively. The notation *F*(*a*) indicates the field extension obtained by adjoining an element *a* to the field *F*.

### Computational tools

#### Cardinality of the Galois group and the degree of the field extension

One of the basic propositions required for completely determining the Galois group of a finite field extension is the following: Given a polynomial $f(x)\in F[x]$ , let $E/F$ be its splitting field extension. Then the order of the Galois group is equal to the degree of the field extension; that is,

$\left|\operatorname {Gal} (E/F)\right|=[E:F]$

#### Eisenstein's criterion

A useful tool for determining the Galois group of a polynomial comes from Eisenstein's criterion. If a polynomial $f\in F[x]$ factors into irreducible polynomials $f=f_{1}\cdots f_{k}$ the Galois group of f can be determined using the Galois groups of each $f_{i}$ since the Galois group of f contains each of the Galois groups of the $f_{i}.$

### Trivial group

$\operatorname {Gal} (F/F)$ is the trivial group that has a single element, namely the identity automorphism.

Another example of a Galois group which is trivial is $\operatorname {Aut} (\mathbb {R} /\mathbb {Q} ).$ Indeed, it can be shown that any automorphism of $\mathbb {R}$ must preserve the ordering of the real numbers and hence must be the identity.

Consider the field $K=\mathbb {Q} ({\sqrt[{3}]{2}}).$ The group $\operatorname {Aut} (K/\mathbb {Q} )$ contains only the identity automorphism. This is because K is not a normal extension, since the other two cube roots of 2 ,

${\exp }{\bigl (}{\tfrac {2}{3}}\pi i{\bigr )}{\sqrt[{3}]{2}},\quad {\exp }{\bigl (}{\tfrac {4}{3}}\pi i{\bigr )}{\sqrt[{3}]{2}},$

are missing from the extension—in other words *K* is not a splitting field.

### Finite abelian groups

The Galois group $\operatorname {Gal} (\mathbb {C} /\mathbb {R} )$ has two elements, the identity automorphism and the complex conjugation automorphism.

#### Quadratic extensions

The degree two field extension $\mathbb {Q} ({\sqrt {2}})/\mathbb {Q}$ has the Galois group $\operatorname {Gal} (\mathbb {Q} ({\sqrt {2}})/\mathbb {Q} )$ with two elements, the identity automorphism and the automorphism $\sigma$ which exchanges ${\sqrt {2}}$ and $-{\sqrt {2}}$ . This example generalizes for a prime number $p\in \mathbb {N} .$

#### Product of quadratic extensions

Using the lattice structure of Galois groups, for distinct prime numbers $p_{1},\ldots ,p_{k}$ the Galois group of $\mathbb {Q} \left({\sqrt {p_{1}}},\ldots ,{\sqrt {p_{k}}}\right)/\mathbb {Q}$ is

$\operatorname {Gal} \left(\mathbb {Q} ({\sqrt {p_{1}}},\ldots ,{\sqrt {p_{k}}})/\mathbb {Q} \right)\cong \operatorname {Gal} \left(\mathbb {Q} ({\sqrt {p_{1}}})/\mathbb {Q} \right)\times \cdots \times \operatorname {Gal} \left(\mathbb {Q} ({\sqrt {p_{k}}})/\mathbb {Q} \right)\cong (\mathbb {Z} /2\mathbb {Z} )^{k}$

#### Cyclotomic extensions

Another useful class of examples comes from the splitting fields of cyclotomic polynomials. These are polynomials $\Phi _{n}$ defined as

$\Phi _{n}(x)=\prod _{\begin{matrix}1\leq k\leq n\\\gcd(k,n)=1\end{matrix}}\left(x-e^{2ik\pi /n}\right)$

whose degree is $\phi (n)$ , Euler's totient function at n . Then, the splitting field over $\mathbb {Q}$ is $\mathbb {Q} (\zeta _{n})$ and has automorphisms $\sigma _{a}$ sending $\zeta _{n}\mapsto \zeta _{n}^{a}$ for $1\leq a<n$ relatively prime to n . Since the degree of the field is equal to the degree of the polynomial, these automorphisms generate the Galois group. If $n=p_{1}^{a_{1}}\cdots p_{k}^{a_{k}},$ then

$\operatorname {Gal} (\mathbb {Q} (\zeta _{n})/\mathbb {Q} )\cong \prod _{a_{i}}\operatorname {Gal} \left(\mathbb {Q} (\zeta _{p_{i}^{a_{i}}})/\mathbb {Q} \right)$

If n is a prime p , then a corollary of this is

$\operatorname {Gal} (\mathbb {Q} (\zeta _{p})/\mathbb {Q} )\cong \mathbb {Z} /(p-1)\mathbb {Z}$

In fact, any finite abelian group can be found as the Galois group of some subfield of a cyclotomic field extension by the Kronecker–Weber theorem.

#### Finite fields

Another useful class of examples of Galois groups with finite abelian groups comes from finite fields. If *q* is a prime power, and if $F=\mathbb {F} _{q}$ and $E=\mathbb {F} _{q^{n}}$ denote the Galois fields of order q and $q^{n}$ respectively, then $\operatorname {Gal} (E/F)$ is cyclic of order *n* and generated by the Frobenius homomorphism.

#### Degree 4 examples

The field extension $\mathbb {Q} {\bigl (}{\sqrt {2}},{\sqrt {3}}~\!{\bigr )}{\big /}\mathbb {Q}$ is an example of a degree 4 field extension. This has two automorphisms $\sigma ,\tau$ where $\sigma {\bigl (}{\sqrt {2}}~\!{\bigr )}=-{\sqrt {2}}$ and $\tau {\bigl (}{\sqrt {3}}~\!{\bigr )}=-{\sqrt {3}}.$ Since these two generators define a group of order 4 , the Klein four-group, they determine the entire Galois group.

Another example is given from the splitting field $E/\mathbb {Q}$ of the polynomial

$f(x)=x^{4}+x^{3}+x^{2}+x+1$

Note because $(x-1)f(x)=x^{5}-1,$ the roots of $f(x)$ are $\exp {\bigl (}{\tfrac {2}{5}}k\pi i{\bigr )}.$ There are automorphisms

${\begin{cases}\sigma _{\ell }:E\to E\\\sigma _{2}:\exp {\bigl (}{\tfrac {2}{5}}\pi i{\bigr )}\mapsto \exp {\bigl (}{\tfrac {2}{5}}\pi i{\bigr )}^{\ell }\end{cases}}$

generating a group of order 4 . Since $\sigma _{2}$ generates this group, the Galois group is isomorphic to $\mathbb {Z} /4\mathbb {Z}$ .

### Finite non-abelian groups

Consider now $L=\mathbb {Q} ({\sqrt[{3}]{2}},\omega ),$ where $\omega$ is a primitive cube root of unity. The group $\operatorname {Gal} (L/\mathbb {Q} )$ is isomorphic to *S*3, the dihedral group of order 6, and *L* is in fact the splitting field of $x^{3}-2$ over $\mathbb {Q} .$

#### Quaternion group

The Quaternion group can be found as the Galois group of a field extension of $\mathbb {Q}$ . For example, the field extension

$\mathbb {Q} \left({\sqrt {2}},{\sqrt {3}},{\sqrt {(2+{\sqrt {2}})(3+{\sqrt {3}})}}\right)$

has the prescribed Galois group.

#### Symmetric group of prime order

If f is an irreducible polynomial of prime degree p with rational coefficients and exactly two non-real roots, then the Galois group of f is the full symmetric group $S_{p}.$

For example, $f(x)=x^{5}-4x+2\in \mathbb {Q} [x]$ is irreducible from Eisenstein's criterion. Plotting the graph of f with graphing software or paper shows it has three real roots, hence two complex roots, showing its Galois group is $S_{5}$ .

### Comparing Galois groups of field extensions of global fields

Given a global field extension $K/k$ (such as $\mathbb {Q} ({\sqrt[{5}]{3}},\zeta _{5})/\mathbb {Q}$ ) and equivalence classes of valuations w on K (such as the p -adic valuation) and v on k such that their completions give a Galois field extension

$K_{w}/k_{v}$

of local fields, there is an induced action of the Galois group $G=\operatorname {Gal} (K/k)$ on the set of equivalence classes of valuations such that the completions of the fields are compatible. This means if $s\in G$ then there is an induced isomorphism of local fields

$s_{w}:K_{w}\to K_{sw}$

Since we have taken the hypothesis that w lies over v (i.e. there is a Galois field extension $K_{w}/k_{v}$ ), the field morphism $s_{w}$ is in fact an isomorphism of $k_{v}$ -algebras. If we take the isotropy subgroup of G for the valuation class w

$G_{w}=\{s\in G:sw=w\}$

then there is a surjection of the global Galois group to the local Galois group such that there is an isomorphism between the local Galois group and the isotropy subgroup. Diagrammatically, this means

${\begin{matrix}\operatorname {Gal} (K/v)&\twoheadrightarrow &\operatorname {Gal} (K_{w}/k_{v})\\\downarrow &&\downarrow \\G&\twoheadrightarrow &G_{w}\end{matrix}}$

where the vertical arrows are isomorphisms. This gives a technique for constructing Galois groups of local fields using global Galois groups.

### Infinite groups

A basic example of a field extension with an infinite group of automorphisms is $\operatorname {Aut} (\mathbb {C} /\mathbb {Q} )$ , since it contains every algebraic field extension $E/\mathbb {Q}$ . For example, the field extensions $\mathbb {Q} ({\sqrt {a}})/\mathbb {Q}$ for a square-free element $a\in \mathbb {Q}$ each have a unique degree 2 automorphism, inducing an automorphism in $\operatorname {Aut} (\mathbb {C} /\mathbb {Q} ).$

One of the most studied classes of infinite Galois group is the absolute Galois group, which is an infinite, profinite group defined as the inverse limit of all finite Galois extensions $E/F$ for a fixed field. The inverse limit is denoted

$\operatorname {Gal} ({\overline {F}}/F):=\varprojlim _{E/F{\text{ finite separable}}}{\operatorname {Gal} (E/F)}$

,

where ${\overline {F}}$ is the separable closure of the field F . Note this group is a topological group. Some basic examples include $\operatorname {Gal} ({\overline {\mathbb {Q} }}/\mathbb {Q} )$ and

$\operatorname {Gal} ({\overline {\mathbb {F} }}_{q}/\mathbb {F} _{q})\cong {\hat {\mathbb {Z} }}\cong \prod _{p}\mathbb {Z} _{p}$

.

Another readily computable example comes from the field extension $\mathbb {Q} ({\sqrt {2}},{\sqrt {3}},{\sqrt {5}},\ldots )/\mathbb {Q}$ containing the square root of every positive prime. It has Galois group

$\operatorname {Gal} (\mathbb {Q} ({\sqrt {2}},{\sqrt {3}},{\sqrt {5}},\ldots )/\mathbb {Q} )\cong \prod _{p}\mathbb {Z} /2$

,

which can be deduced from the profinite limit

$\cdots \to \operatorname {Gal} (\mathbb {Q} ({\sqrt {2}},{\sqrt {3}},{\sqrt {5}})/\mathbb {Q} )\to \operatorname {Gal} (\mathbb {Q} ({\sqrt {2}},{\sqrt {3}})/\mathbb {Q} )\to \operatorname {Gal} (\mathbb {Q} ({\sqrt {2}})/\mathbb {Q} )$

and using the computation of the Galois groups.

## Properties

The significance of an extension being Galois is that it obeys the fundamental theorem of Galois theory: the closed (with respect to the Krull topology) subgroups of the Galois group correspond to the intermediate fields of the field extension.

If $E/F$ is a Galois extension, then $\operatorname {Gal} (E/F)$ can be given a topology, called the Krull topology, that makes it into a profinite group.
