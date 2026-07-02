---
title: "Ext functor"
source: https://en.wikipedia.org/wiki/Ext_functor
domain: homological-algebra
license: CC-BY-SA-4.0
tags: homological algebra, chain complex, exact sequence, derived functor
fetched: 2026-07-02
---

# Ext functor

In mathematics, the **Ext functors** are the derived functors of the Hom functor. Along with the Tor functor, Ext is one of the core concepts of homological algebra, in which ideas from algebraic topology are used to define invariants of algebraic structures. The cohomology of groups, Lie algebras, and associative algebras can all be defined in terms of Ext. The name comes from the fact that the first Ext group Ext1 classifies extensions of one module by another.

In the special case of abelian groups, Ext was introduced by Reinhold Baer in 1934. It was named by Samuel Eilenberg and Saunders MacLane in 1942, and applied to topology (the universal coefficient theorem for cohomology). For modules over any ring, Ext was defined by Henri Cartan and Eilenberg in 1956.

## Definition

Let R be a ring and let $R{\text{-Mod}}$ be the category of modules over R . (One can take this to mean either left R -modules or right R -modules.) For a fixed R -module A , let $T(B)={\text{Hom}}_{R}(A,B)$ for B in $R{\text{-Mod}}$ . (Here ${\text{Hom}}_{R}(A,B)$ is the abelian group of R -linear maps from A to B ; this is an R -module if R is commutative.) This is a left exact functor from $R{\text{-Mod}}$ to the category of abelian groups $\mathbf {Ab}$ , and so it has right derived functors $R^{i}T$ . The Ext groups are the abelian groups defined by

$\operatorname {Ext} _{R}^{i}(A,B)=(R^{i}T)(B),$

for an integer *i*. By definition, this means: take any injective resolution

$0\to B\to I^{0}\to I^{1}\to \cdots ,$

remove the term *B*, and form the cochain complex:

$0\to \operatorname {Hom} _{R}(A,I^{0})\to \operatorname {Hom} _{R}(A,I^{1})\to \cdots .$

For each integer i , ${\text{Ext}}_{R}^{i}(A,B)$ is the cohomology of this complex at position i . It is zero for i negative. For example, ${\text{Ext}}_{R}^{0}(A,B)$ is the kernel of the map ${\text{Hom}}_{R}(A,I^{0})\rightarrow {\text{Hom}}_{R}(A,I^{1})$ , which is isomorphic to ${\text{Hom}}_{R}(A,B)$ .

An alternative definition uses the functor $G(A)=\operatorname {Hom} _{R}(A,B)$ , for a fixed R -module B . This is a contravariant functor, which can be viewed as a left exact functor from the opposite category $(R{\text{-Mod}})^{\text{op}}$ to $\mathbf {Ab}$ . The Ext groups are defined as the right derived functors $R^{i}G$ :

$\operatorname {Ext} _{R}^{i}(A,B)=(R^{i}G)(A).$

That is, choose any projective resolution

$\cdots \to P_{1}\to P_{0}\to A\to 0,$

remove the term A , and form the cochain complex:

$0\to \operatorname {Hom} _{R}(P_{0},B)\to \operatorname {Hom} _{R}(P_{1},B)\to \cdots .$

Then $\operatorname {Ext} _{R}^{i}(A,B)$ is the cohomology of this complex at position i .

One may wonder why the choice of resolution has been left vague so far. In fact, Cartan and Eilenberg showed that these constructions are independent of the choice of projective or injective resolution, and that both constructions yield the same Ext groups. Moreover, for a fixed ring *R*, Ext is a functor in each variable (contravariant in *A*, covariant in *B*).

For a commutative ring *R* and *R*-modules *A* and *B*, Ext*i* *R*(*A*, *B*) is an *R*-module (using that Hom*R*(*A*, *B*) is an *R*-module in this case). For a non-commutative ring *R*, Ext*i* *R*(*A*, *B*) is only an abelian group, in general. If *R* is an algebra over a ring *S* (which means in particular that *S* is commutative), then Ext*i* *R*(*A*, *B*) is at least an *S*-module.

## Properties of Ext

Here are some of the basic properties and computations of $\operatorname {Ext}$ groups.

- $\operatorname {Ext} _{R}^{0}(A,B)\cong \operatorname {Hom} _{R}(A,B)$ for any R -modules A and B .
- $\operatorname {Ext} _{R}^{i}(A,B)=0$ for all $i>0$ if the R -module A is projective (for example, free) or if B is injective.
- The converses also hold:
  - If Ext1 *R*(*A*, *B*) = 0 for all *B*, then *A* is projective (and hence Ext*i* *R*(*A*, *B*) = 0 for all *i* > 0).
  - If Ext1 *R*(*A*, *B*) = 0 for all *A*, then *B* is injective (and hence Ext*i* *R*(*A*, *B*) = 0 for all *i* > 0).
- $\operatorname {Ext} _{\mathbb {Z} }^{i}(A,B)=0$ for all $i\geq 2$ and all abelian groups A and B .
- Generalizing the previous example, $\operatorname {Ext} _{R}^{i}(A,B)=0$ for all $i\geq 2$ if R is a principal ideal domain.
- If R is a commutative ring and u in R is not a zero divisor, then

$\operatorname {Ext} _{R}^{i}(R/(u),B)\cong {\begin{cases}B[u]&i=0\\B/uB&i=1\\0&{\text{otherwise,}}\end{cases}}$

for any

R

-module

B

. Here

$B[u]$

denotes the

u

-

torsion subgroup

of

B

,

$\{x\in B:ux=0\}$

. Taking

R

to be the ring

$\mathbb {Z}$

of integers, this calculation can be used to compute

$\operatorname {Ext} _{\mathbb {Z} }^{1}(A,B)$

for any

finitely generated abelian group

A

.

- Generalizing the previous example, one can compute $\operatorname {Ext}$ groups when the first module is the quotient of a commutative ring by any regular sequence, using the Koszul complex. For example, if R is the polynomial ring $k[x_{1},\ldots ,x_{n}]$ over a field k , then $\operatorname {Ext} _{R}^{*}(k,k)$ is the exterior algebra S over k on n generators in $\operatorname {Ext} ^{1}$ . Moreover, $\operatorname {Ext} _{S}^{*}(k,k)$ is the polynomial ring R ; this is an example of Koszul duality.
- By the general properties of derived functors, there are two basic exact sequences for $\operatorname {Ext}$ . First, a short exact sequence $0\rightarrow K\rightarrow L\rightarrow M\rightarrow 0$ of R -modules induces a long exact sequence of the form

$0\to \mathrm {Hom} _{R}(A,K)\to \mathrm {Hom} _{R}(A,L)\to \mathrm {Hom} _{R}(A,M)\to \mathrm {Ext} _{R}^{1}(A,K)\to \mathrm {Ext} _{R}^{1}(A,L)\to \cdots ,$

for any

R

-module

A

. Also, a short exact sequence

$0\rightarrow K\rightarrow L\rightarrow M\rightarrow 0$

induces a long exact sequence of the form

$0\to \mathrm {Hom} _{R}(M,B)\to \mathrm {Hom} _{R}(L,B)\to \mathrm {Hom} _{R}(K,B)\to \mathrm {Ext} _{R}^{1}(M,B)\to \mathrm {Ext} _{R}^{1}(L,B)\to \cdots ,$

for any

R

-module

B

.

- Ext takes direct sums (possibly infinite) in the first variable and products in the second variable to products. That is:

${\begin{aligned}\operatorname {Ext} _{R}^{i}\left(\bigoplus _{\alpha }M_{\alpha },N\right)&\cong \prod _{\alpha }\operatorname {Ext} _{R}^{i}(M_{\alpha },N)\\\operatorname {Ext} _{R}^{i}\left(M,\prod _{\alpha }N_{\alpha }\right)&\cong \prod _{\alpha }\operatorname {Ext} _{R}^{i}(M,N_{\alpha })\end{aligned}}$

- Let *A* be a finitely generated module over a commutative Noetherian ring *R*. Then Ext commutes with localization, in the sense that for every multiplicatively closed set *S* in *R*, every *R*-module *B*, and every integer *i*,

$S^{-1}\operatorname {Ext} _{R}^{i}(A,B)\cong \operatorname {Ext} _{S^{-1}R}^{i}\left(S^{-1}A,S^{-1}B\right).$

## Ext and extensions

### Equivalence of extensions

The $\operatorname {Ext}$ groups derive their name from their relation to extensions of modules. Given R -modules A and B , an **extension of *A* by *B*** is a short exact sequence of R -modules

$0\to B\to E\to A\to 0.$

Two extensions

$0\to B\to E\to A\to 0$

$0\to B\to E'\to A\to 0$

are said to be **equivalent** (as extensions of A by B ) if there is a commutative diagram:

Note that the Five lemma implies that the middle arrow is an isomorphism. An extension of A by B is called **split** if it is equivalent to the **trivial extension**

$0\to B\to A\oplus B\to A\to 0.$

There is a one-to-one correspondence between equivalence classes of extensions of A by B and elements of $\operatorname {Ext} _{R}^{1}(A,B)$ . This can be made precise as follows.

Proof

Fix a short exact sequence

$0\to M\to P\to A\to 0$

where P is projective. Applying $\operatorname {Hom} (-,B)$ yields the long exact sequence

$\operatorname {Hom} (P,B)\to \operatorname {Hom} (M,B)\xrightarrow {\delta } \operatorname {Ext} (A,B)\to 0.$

Given $x\in \operatorname {Ext} (A,B)$ , choose $\beta \in \operatorname {Hom} (M,B)$ such that $\delta (\beta )=x$ . Consider the pushout of $j:M\to P$ along $\beta$ , given by the cokernel of the map

$M\to P\oplus B,\quad m\mapsto (j(m),-\beta (m)).$

Define X as this pushout object. This yields the commutative diagram:

Here, $X\to A$ is induced by the map $P\to A$ . The bottom row is an extension of A by B , denoted $\xi$ , and the connecting map $\delta$ ensures that $\delta (\xi )=x$ , proving surjectivity.

To show well-definedness on equivalence classes, suppose $\beta '$ is another lift of x . Then there exists $f\in \operatorname {Hom} (P,B)$ such that $\beta '=\beta +f\circ j$ . If $X'$ is the pushout of j and $\beta '$ , then an isomorphism $X\cong X'$ is induced, making the extensions equivalent.

Conversely, given an extension

$0\to B\to X\to A\to 0$

,

the lifting property of P gives a map $\tau :P\to X$ fitting into the diagram

Here X is the pushout of j and $\gamma$ . This shows that the map is injective.

Thus, the set of equivalence classes of extensions of A by B is naturally isomorphic to $\operatorname {Ext} (A,B)$ .

The trivial extension corresponds to the zero element of $\operatorname {Ext} _{R}^{1}(A,B)$ .

### The Baer sum of extensions

The **Baer sum** is an explicit description of the abelian group structure on $\operatorname {Ext} _{R}^{1}(A,B)$ , viewed as the set of equivalence classes of extensions of A by B . Namely, given two extensions

$0\to B\xrightarrow {f} E\xrightarrow {g} A\to 0$

and

$0\to B\xrightarrow {f'} E'\xrightarrow {g'} A\to 0,$

first form the pullback over A ,

$\Gamma =\left\{(e,e')\in E\oplus E'\;|\;g(e)=g'(e')\right\}.$

Then form the quotient module

$Y=\Gamma /\{(f(b),-f'(b))\;|\;b\in B\}.$

The Baer sum of E and $E'$ is the extension

$0\to B\to Y\to A\to 0,$

where the first map is $b\mapsto [(f(b),0)]=[(0,f'(b))]$ and the second is $(e,e')\mapsto g(e)=g'(e')$ .

Up to equivalence of extensions, the Baer sum is commutative and has the trivial extension as identity element. The negative of an extension $0\rightarrow B\rightarrow E\rightarrow A\rightarrow 0$ is the extension involving the same module E , but with the homomorphism $B\rightarrow E$ replaced by its negative.

## Construction of Ext in abelian categories

Nobuo Yoneda defined the abelian groups Ext*n* **C**(*A*, *B*) for objects *A* and *B* in any abelian category **C**; this agrees with the definition in terms of resolutions if **C** has enough projectives or enough injectives. First, Ext0 **C**(*A*,*B*) = Hom**C**(*A*, *B*). Next, Ext1 **C**(*A*, *B*) is the set of equivalence classes of extensions of *A* by *B*, forming an abelian group under the Baer sum. Finally, the higher Ext groups Ext*n* **C**(*A*, *B*) are defined as equivalence classes of *n-extensions*, which are exact sequences

$0\to B\to X_{n}\to \cdots \to X_{1}\to A\to 0,$

under the equivalence relation generated by the relation that identifies two extensions

${\begin{aligned}\xi :0&\to B\to X_{n}\to \cdots \to X_{1}\to A\to 0\\\xi ':0&\to B\to X'_{n}\to \cdots \to X'_{1}\to A\to 0\end{aligned}}$

if there are maps $X_{m}\to X'_{m}$ for all *m* in {1, 2, ..., *n*} so that every resulting square commutes ${\begin{array}{cc cc cc c cc cc cc}0&\longrightarrow &B&\longrightarrow &X_{n}&\longrightarrow &\dots &\longrightarrow &X_{1}&\longrightarrow &A&\longrightarrow &0\\&&{\Bigg \Vert }&&{\Bigg \downarrow }\iota _{n}\!&&&&{\Bigg \downarrow }\iota _{1}&&{\Bigg \Vert }&&\\0&\longrightarrow &B&\longrightarrow &X'_{n}&\longrightarrow &\dots &\longrightarrow &X'_{1}&\longrightarrow &A&\longrightarrow &0\end{array}}$ that is, if there is a chain map $\iota \colon \xi \to \xi '$ which is the identity on *A* and *B*.

The Baer sum of two *n*-extensions as above is formed by letting $X''_{1}$ be the pullback of $X_{1}$ and $X'_{1}$ over *A*, and $X''_{n}$ be the pushout of $X_{n}$ and $X'_{n}$ under *B*. Then the Baer sum of the extensions is

$0\to B\to X''_{n}\to X_{n-1}\oplus X'_{n-1}\to \cdots \to X_{2}\oplus X'_{2}\to X''_{1}\to A\to 0.$

## The derived category and the Yoneda product

An important point is that Ext groups in an abelian category **C** can be viewed as sets of morphisms in a category associated to **C**, the derived category *D*(**C**). The objects of the derived category are complexes of objects in **C**. Specifically, one has

$\operatorname {Ext} _{\mathbf {C} }^{i}(A,B)=\operatorname {Hom} _{D({\mathbf {C} })}(A,B[i]),$

where an object of **C** is viewed as a complex concentrated in degree zero, and [*i*] means shifting a complex *i* steps to the left. From this interpretation, there is a bilinear map, sometimes called the Yoneda product:

$\operatorname {Ext} _{\mathbf {C} }^{i}(A,B)\times \operatorname {Ext} _{\mathbf {C} }^{j}(B,C)\to \operatorname {Ext} _{\mathbf {C} }^{i+j}(A,C),$

which is simply the composition of morphisms in the derived category.

The Yoneda product can also be described in more elementary terms. For *i* = *j* = 0, the product is the composition of maps in the category **C**. In general, the product can be defined by splicing together two Yoneda extensions.

Alternatively, the Yoneda product can be defined in terms of resolutions. (This is close to the definition of the derived category.) For example, let *R* be a ring, with *R*-modules *A*, *B*, *C*, and let *P*, *Q*, and *T* be projective resolutions of *A*, *B*, *C*. Then Ext*i* *R*(*A*,*B*) can be identified with the group of chain homotopy classes of chain maps *P* → *Q*[*i*]. The Yoneda product is given by composing chain maps:

$P\to Q[i]\to T[i+j].$

By any of these interpretations, the Yoneda product is associative. As a result, $\operatorname {Ext} _{R}^{*}(A,A)$ is a graded ring, for any *R*-module *A*. For example, this gives the ring structure on group cohomology $H^{*}(G,\mathbb {Z} ),$ since this can be viewed as $\operatorname {Ext} _{\mathbb {Z} [G]}^{*}(\mathbb {Z} ,\mathbb {Z} )$ . Also by associativity of the Yoneda product: for any *R*-modules *A* and *B*, $\operatorname {Ext} _{R}^{*}(A,B)$ is a module over $\operatorname {Ext} _{R}^{*}(A,A)$ .

## Important special cases

- Group cohomology is defined by $H^{*}(G,M)=\operatorname {Ext} _{\mathbb {Z} [G]}^{*}(\mathbb {Z} ,M)$ ,

where

G

is a group,

M

is a

representation

of

G

over the integers, and

$\mathbb {Z} [G]$

is the

group ring

of

G

.

- For an algebra A over a field k and an A -bimodule M , Hochschild cohomology is defined by $HH^{*}(A,M)=\operatorname {Ext} _{A\otimes _{k}A^{\text{op}}}^{*}(A,M).$

- Lie algebra cohomology is defined by $H^{*}({\mathfrak {g}},M)=\operatorname {Ext} _{U{\mathfrak {g}}}^{*}(k,M)$ , where ${\mathfrak {g}}$ is a Lie algebra over a commutative ring k , M is a ${\mathfrak {g}}$ -module, and $U{\mathfrak {g}}$ is the universal enveloping algebra.

- For a topological space X , sheaf cohomology can be defined as $H^{*}(X,A)=\operatorname {Ext} ^{*}(\mathbb {Z} _{X},A).$ Here Ext is taken in the abelian category of sheaves of abelian groups on X , and $\mathbb {Z} _{X}$ is the sheaf of locally constant $\mathbb {Z}$ -valued functions. Instead of $\mathbb {Z} _{X}$ , one can consider any sheaf of rings ${\mathcal {O}}_{X}$ on X and take Ext in the category of sheaves of ${\mathcal {O}}_{X}$ -modules.

- For a sheaf of modules ${\mathcal {F}}$ on a ringed space $(X,{\mathcal {O}}_{X})$ , taking the right derived functors of the sheaf Hom ${\mathcal {Hom}}_{X}({\mathcal {F}},-)$ , the internal Hom in the category of ${\mathcal {O}}_{X}$ -modules, gives the Ext sheaves ${\mathcal {Ext}}_{X}^{*}({\mathcal {F}},-)$ . They are related to the global Ext groups via the local-to-global Ext spectral sequence.

- For a commutative Noetherian local ring R with residue field k , $\operatorname {Ext} _{R}^{*}(k,k)$ is the universal enveloping algebra of a graded Lie algebra $\pi ^{*}(R)$ over k , known as the **homotopy Lie algebra** of R . (To be precise, when k has characteristic 2, $\pi ^{*}(R)$ has to be viewed as an "adjusted Lie algebra".) There is a natural homomorphism of graded Lie algebras from the André–Quillen cohomology $D^{*}(k/R,k)$ to $\pi ^{*}(R)$ , which is an isomorphism if k has characteristic zero.
