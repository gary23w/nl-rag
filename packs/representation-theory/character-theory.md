---
title: "Character theory"
source: https://en.wikipedia.org/wiki/Character_theory
domain: representation-theory
license: CC-BY-SA-4.0
tags: representation theory, group representation, character theory, irreducible representation
fetched: 2026-07-02
---

# Character theory

In mathematics, more specifically in group theory, the **character** of a group representation is a function on the group that associates to each group element the trace of the corresponding matrix. The character carries the essential information about the representation in a more condensed form. Georg Frobenius initially developed representation theory of finite groups entirely based on the characters, and without any explicit matrix realization of representations themselves. This is possible because a complex representation of a finite group is determined (up to isomorphism) by its character. The situation with representations over a field of positive characteristic, so-called "modular representations", is more delicate, but Richard Brauer developed a powerful theory of characters in this case as well. Many deep theorems on the structure of finite groups use characters of modular representations.

## Applications

Characters of irreducible representations encode many important properties of a group and can thus be used to study its structure. Character theory is an essential tool in the classification of finite simple groups. Close to half of the proof of the Feit–Thompson theorem involves intricate calculations with character values. Easier, but still essential, results that use character theory include Burnside's theorem (a purely group-theoretic proof of Burnside's theorem has since been found, but that proof came over half a century after Burnside's original proof), and a theorem of Richard Brauer and Michio Suzuki stating that a finite simple group cannot have a generalized quaternion group as its Sylow 2-subgroup.

## Definitions

Let V be a finite-dimensional vector space over a field F and let *ρ* : *G* → GL(*V*) be a representation of a group G on V. The **character** of ρ is the function *χρ* : *G* → *F* given by

$\chi _{\rho }(g)=\operatorname {Tr} (\rho (g))$

where Tr is the trace.

A character *χρ* is called **irreducible** or **simple** if ρ is an irreducible representation. The **degree** of the character χ is the dimension of ρ; in characteristic zero this is equal to the value *χ*(1). A character of degree 1 is called **linear**. When G is finite and F has characteristic zero, the **kernel** of the character *χρ* is the normal subgroup:

$\ker \chi _{\rho }:=\left\lbrace g\in G\mid \chi _{\rho }(g)=\chi _{\rho }(1)\right\rbrace ,$

which is precisely the kernel of the representation ρ. However, the character is *not* a group homomorphism in general.

## Properties

- Characters are class functions, that is, they each take a constant value on a given conjugacy class. More precisely, the set of irreducible characters of a given group G into a field F form a basis of the F-vector space of all class functions *G* → *F*.
- Isomorphic representations have the same characters. Over a field of characteristic 0, two representations are isomorphic if and only if they have the same character.
- If a representation is the direct sum of subrepresentations, then the corresponding character is the sum of the characters of those subrepresentations.
- If a character of the finite group G is restricted to a subgroup H, then the result is also a character of H.
- Every character value *χ*(*g*) is a sum of n m-th roots of unity, where n is the degree (that is, the dimension of the associated vector space) of the representation with character χ and m is the order of g. In particular, when *F* = **C**, every such character value is an algebraic integer.
- If *F* = **C** and χ is irreducible, then $[G:C_{G}(x)]{\frac {\chi (x)}{\chi (1)}}$ is an algebraic integer for all x in G.
- If F is algebraically closed and char(*F*) does not divide the order of G, then the number of irreducible characters of G is equal to the number of conjugacy classes of G. Furthermore, in this case, the degrees of the irreducible characters are divisors of the order of G (and they even divide [*G* : *Z*(*G*)] if *F* = **C**).

### Arithmetic properties

Let ρ and σ be representations of G. Then the following identities hold:

- $\chi _{\rho \oplus \sigma }=\chi _{\rho }+\chi _{\sigma }$
- $\chi _{\rho \otimes \sigma }=\chi _{\rho }\cdot \chi _{\sigma }$
- $\chi _{\rho ^{*}}={\overline {\chi _{\rho }}}$
- $\chi _{{\scriptscriptstyle {\rm {{Alt}^{2}}}}\rho }(g)={\tfrac {1}{2}}\!\left[\left(\chi _{\rho }(g)\right)^{2}-\chi _{\rho }(g^{2})\right]$
- $\chi _{{\scriptscriptstyle {\rm {{Sym}^{2}}}}\rho }(g)={\tfrac {1}{2}}\!\left[\left(\chi _{\rho }(g)\right)^{2}+\chi _{\rho }(g^{2})\right]$

where *ρ*⊕*σ* is the direct sum, *ρ*⊗*σ* is the tensor product, *ρ*∗ denotes the conjugate transpose of ρ, and Alt2 is the alternating product Alt2*ρ* = *ρ* ∧ *ρ* and Sym2 is the symmetric square, which is determined by $\rho \otimes \rho =\left(\rho \wedge \rho \right)\oplus {\textrm {Sym}}^{2}\rho .$

## Character tables

The irreducible complex characters of a finite group form a **character table** which encodes much useful information about the group G in a compact form. Each row is labelled by an irreducible representation and the entries in the row are the characters of the representation on the respective conjugacy class of G. The columns are labelled by (representatives of) the conjugacy classes of G. It is customary to label the first row by the character of the **trivial representation**, which is the trivial action of G on a 1-dimensional vector space by $\rho (g)=1$ for all $g\in G$ . Each entry in the first row is therefore 1. Similarly, it is customary to label the first column by the identity. Therefore, the first column contains the degree of each irreducible character.

Here is the character table of

$C_{3}=\langle u\mid u^{3}=1\rangle ,$

the cyclic group with three elements and generator *u*:

|   | (1) | (*u*) | (*u*2) |
|---|---|---|---|
| **1** | 1 | 1 | 1 |
| *χ*1 | 1 | ω | *ω*2 |
| *χ*2 | 1 | *ω*2 | ω |

where ω is a primitive third root of unity.

The character table is always square, because the number of irreducible representations is equal to the number of conjugacy classes.

### Orthogonality relations

The space of complex-valued class functions of a finite group G has a natural inner product:

$\langle \alpha ,\beta \rangle :={\frac {1}{{\mathopen {\vert }}G{\mathclose {\vert }}}}\sum _{g\in G}\alpha (g){\overline {\beta (g)}}$

where *β*(*g*) is the complex conjugate of *β*(*g*). With respect to this inner product, the irreducible characters form an orthonormal basis for the space of class-functions, and this yields the orthogonality relation for the rows of the character table:

$\langle \chi _{i},\chi _{j}\rangle ={\begin{cases}0&{\mbox{ if }}i\neq j,\\1&{\mbox{ if }}i=j.\end{cases}}$

For *g*, *h* in G, applying the same inner product to the columns of the character table yields:

$\sum _{\chi _{i}}\chi _{i}(g){\overline {\chi _{i}(h)}}={\begin{cases}{\mathopen {\vert }}C_{G}(g){\mathclose {\vert }},&{\mbox{ if }}g,h{\mbox{ are conjugate }}\\0&{\mbox{ otherwise.}}\end{cases}}$

where the sum is over all of the irreducible characters *χi* of G and the symbol |*CG*(*g*)| denotes the order of the centralizer of g. Note that since g and h are conjugate iff they are in the same column of the character table, this implies that the columns of the character table are orthogonal.

The orthogonality relations can aid many computations including:

- Decomposing an unknown character as a linear combination of irreducible characters.
- Constructing the complete character table when only some of the irreducible characters are known.
- Finding the orders of the centralizers of representatives of the conjugacy classes of a group.
- Finding the order of the group.

### Character table properties

Certain properties of the group G can be deduced from its character table:

- The order of G is given by the sum of the squares of the entries of the first column (the degrees of the irreducible characters). More generally, the sum of the squares of the absolute values of the entries in any column gives the order of the centralizer of an element of the corresponding conjugacy class.
- All normal subgroups of G (and thus whether or not G is simple) can be recognised from its character table. The kernel of a character χ is the set of elements g in G for which *χ*(*g*) = *χ*(1); this is a normal subgroup of G. Each normal subgroup of G is the intersection of the kernels of some of the irreducible characters of G.
- The commutator subgroup of G is the intersection of the kernels of the linear characters of G.
- If G is finite, then since the character table is square and has as many rows as conjugacy classes, it follows that G is abelian iff each conjugacy class is a singleton iff the character table of G is $|G|\!\times \!|G|$ iff each irreducible character is linear.
- It follows, using some results of Richard Brauer from modular representation theory, that the prime divisors of the orders of the elements of each conjugacy class of a finite group can be deduced from its character table (an observation of Graham Higman).

The character table does not in general determine the group up to isomorphism: for example, the quaternion group Q and the dihedral group of 8 elements, *D*4, have the same character table. Brauer asked whether the character table, together with the knowledge of how the powers of elements of its conjugacy classes are distributed, determines a finite group up to isomorphism. In 1964, this was answered in the negative by E. C. Dade.

The linear representations of G are themselves a group under the tensor product, since the tensor product of 1-dimensional vector spaces is again 1-dimensional. That is, if $\rho _{1}:G\to V_{1}$ and $\rho _{2}:G\to V_{2}$ are linear representations, then $\rho _{1}\otimes \rho _{2}(g)=(\rho _{1}(g)\otimes \rho _{2}(g))$ defines a new linear representation. This gives rise to a group of linear characters, called the character group under the operation $[\chi _{1}*\chi _{2}](g)=\chi _{1}(g)\chi _{2}(g)$ . This group is connected to Dirichlet characters and Fourier analysis.

## Induced characters and Frobenius reciprocity

The characters discussed in this section are assumed to be complex-valued. Let H be a subgroup of the finite group G. Given a character χ of G, let *χH* denote its restriction to H. Let θ be a character of H. Ferdinand Georg Frobenius showed how to construct a character of G from θ, using what is now known as *Frobenius reciprocity*. Since the irreducible characters of G form an orthonormal basis for the space of complex-valued class functions of G, there is a unique class function *θG* of G with the property that

$\langle \theta ^{G},\chi \rangle _{G}=\langle \theta ,\chi _{H}\rangle _{H}$

for each irreducible character χ of G (the leftmost inner product is for class functions of G and the rightmost inner product is for class functions of H). Since the restriction of a character of G to the subgroup H is again a character of H, this definition makes it clear that *θG* is a non-negative integer combination of irreducible characters of G, so is indeed a character of G. It is known as *the character of* G *induced from* θ. The defining formula of Frobenius reciprocity can be extended to general complex-valued class functions.

Given a matrix representation ρ of H, Frobenius later gave an explicit way to construct a matrix representation of G, known as the representation induced from ρ, and written analogously as *ρG*. This led to an alternative description of the induced character *θG*. This induced character vanishes on all elements of G which are not conjugate to any element of H. Since the induced character is a class function of G, it is only now necessary to describe its values on elements of H. If one writes G as a disjoint union of right cosets of H, say

$G=Ht_{1}\cup \ldots \cup Ht_{n},$

then, given an element h of H, we have:

$\theta ^{G}(h)=\sum _{i\ :\ t_{i}ht_{i}^{-1}\in H}\theta \left(t_{i}ht_{i}^{-1}\right).$

Because θ is a class function of H, this value does not depend on the particular choice of coset representatives.

This alternative description of the induced character sometimes allows explicit computation from relatively little information about the embedding of H in G, and is often useful for calculation of particular character tables. When θ is the trivial character of H, the induced character obtained is known as the **permutation character** of G (on the cosets of H).

The general technique of character induction and later refinements found numerous applications in finite group theory and elsewhere in mathematics, in the hands of mathematicians such as Emil Artin, Richard Brauer, Walter Feit and Michio Suzuki, as well as Frobenius himself.

## Mackey decomposition

The Mackey decomposition was defined and explored by George Mackey in the context of Lie groups, but is a powerful tool in the character theory and representation theory of finite groups. Its basic form concerns the way a character (or module) induced from a subgroup H of a finite group G behaves on restriction back to a (possibly different) subgroup K of G, and makes use of the decomposition of G into (*H*, *K*)-double cosets.

If ${\textstyle G=\bigcup _{t\in T}HtK}$ is a disjoint union, and θ is a complex class function of H, then Mackey's formula states that

$\left(\theta ^{G}\right)_{K}=\sum _{t\in T}\left(\left[\theta ^{t}\right]_{t^{-1}Ht\cap K}\right)^{K},$

where *θt* is the class function of *t*−1*Ht* defined by *θt*(*t*−1*ht*) = *θ*(*h*) for all h in H. There is a similar formula for the restriction of an induced module to a subgroup, which holds for representations over any ring, and has applications in a wide variety of algebraic and topological contexts.

Mackey decomposition, in conjunction with Frobenius reciprocity, yields a well-known and useful formula for the inner product of two class functions θ and ψ induced from respective subgroups H and K, whose utility lies in the fact that it only depends on how conjugates of H and K intersect each other. The formula (with its derivation) is:

${\begin{aligned}\left\langle \theta ^{G},\psi ^{G}\right\rangle &=\left\langle \left(\theta ^{G}\right)_{K},\psi \right\rangle \\&=\sum _{t\in T}\left\langle \left(\left[\theta ^{t}\right]_{t^{-1}Ht\cap K}\right)^{K},\psi \right\rangle \\&=\sum _{t\in T}\left\langle \left(\theta ^{t}\right)_{t^{-1}Ht\cap K},\psi _{t^{-1}Ht\cap K}\right\rangle ,\end{aligned}}$

(where T is a full set of (*H*, *K*)-double coset representatives, as before). This formula is often used when θ and ψ are linear characters, in which case all the inner products appearing in the right hand sum are either 1 or 0, depending on whether or not the linear characters *θt* and ψ have the same restriction to *t*−1*Ht* ∩ *K*. If θ and ψ are both trivial characters, then the inner product simplifies to |*T*|.

## "Twisted" dimension

One may interpret the character of a representation as the "twisted" dimension of a vector space. Treating the character as a function of the elements of the group *χ*(*g*), its value at the identity is the dimension of the space, since *χ*(1) = Tr(*ρ*(1)) = Tr(*IV*) = dim(*V*). Accordingly, one can view the other values of the character as "twisted" dimensions.

One can find analogs or generalizations of statements about dimensions to statements about characters or representations. A sophisticated example of this occurs in the theory of monstrous moonshine: the j-invariant is the graded dimension of an infinite-dimensional graded representation of the Monster group, and replacing the dimension with the character gives the McKay–Thompson series for each element of the Monster group.

## Characters of Lie groups and Lie algebras

If G is a Lie group and $\rho$ a finite-dimensional representation of G , the character $\chi _{\rho }$ of $\rho$ is defined precisely as for any group as

$\chi _{\rho }(g)=\operatorname {Tr} (\rho (g))$

.

Meanwhile, if ${\mathfrak {g}}$ is a Lie algebra and $\rho$ a finite-dimensional representation of ${\mathfrak {g}}$ , we can define the character $\chi _{\rho }$ by

$\chi _{\rho }(X)=\operatorname {Tr} (e^{\rho (X)})$

.

The character will satisfy $\chi _{\rho }(\operatorname {Ad} _{g}(X))=\chi _{\rho }(X)$ for all g in the associated Lie group G and all $X\in {\mathfrak {g}}$ . If we have a Lie group representation and an associated Lie algebra representation, the character $\chi _{\rho }$ of the Lie algebra representation is related to the character $\mathrm {X} _{\rho }$ of the group representation by the formula

$\chi _{\rho }(X)=\mathrm {X} _{\rho }(e^{X})$

.

Suppose now that ${\mathfrak {g}}$ is a complex semisimple Lie algebra with Cartan subalgebra ${\mathfrak {h}}$ . The value of the character $\chi _{\rho }$ of an irreducible representation $\rho$ of ${\mathfrak {g}}$ is determined by its values on ${\mathfrak {h}}$ . The restriction of the character to ${\mathfrak {h}}$ can easily be computed in terms of the weight spaces, as follows:

$\chi _{\rho }(H)=\sum _{\lambda }m_{\lambda }e^{\lambda (H)},\quad H\in {\mathfrak {h}}$

,

where the sum is over all weights $\lambda$ of $\rho$ and where $m_{\lambda }$ is the multiplicity of $\lambda$ .

The (restriction to ${\mathfrak {h}}$ of the) character can be computed more explicitly by the Weyl character formula.
