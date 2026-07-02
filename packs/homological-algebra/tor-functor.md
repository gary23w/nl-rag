---
title: "Tor functor"
source: https://en.wikipedia.org/wiki/Tor_functor
domain: homological-algebra
license: CC-BY-SA-4.0
tags: homological algebra, chain complex, exact sequence, derived functor
fetched: 2026-07-02
---

# Tor functor

In mathematics, the **Tor functors** are the derived functors of the tensor product of modules over a ring. Along with the Ext functor, Tor is one of the central concepts of homological algebra, in which ideas from algebraic topology are used to construct invariants of algebraic structures. The homology of groups, Lie algebras, and associative algebras can all be defined in terms of Tor. The name comes from a relation between the first Tor group Tor1 and the torsion subgroup of an abelian group.

In the special case of abelian groups, Tor was introduced by Eduard Čech in 1935 and named by Samuel Eilenberg around 1950. It was first applied to the Künneth theorem and universal coefficient theorem in topology. For modules over any ring, Ext was defined by Henri Cartan and Eilenberg in 1956.

## Definition

Let R be a ring. Write $R{\textsf {-Mod}}$ for the category of left R -modules and ${\textsf {Mod-}}R$ for the category of right R -modules. (If R is commutative, the two categories can be identified.) For a fixed left R -module B , let $T(A)=A\otimes _{R}B$ for A in ${\textsf {Mod-}}R$ . This is a right exact functor from ${\textsf {Mod-}}R$ to the category of abelian groups ${\textbf {Ab}}$ , and so it has left derived functors ${\mathcal {L}}_{i}T$ . The Tor groups are the abelian groups defined by $\operatorname {Tor} _{i}^{R}(A,B)=({\mathcal {L}}_{i}T)(A),$ for an integer i . By definition, this means: take any projective resolution $\cdots \to P_{2}\to P_{1}\to P_{0}\to A\to 0,$ and remove A , and form the chain complex: $\cdots \to P_{2}\otimes _{R}B\to P_{1}\otimes _{R}B\to P_{0}\otimes _{R}B\to 0$

For each integer i , the group $\operatorname {Tor} _{i}^{R}(A,B)$ is the homology of this complex at position i . It is zero for i negative. Moreover, $\operatorname {Tor} _{0}^{R}(A,B)$ is the cokernel of the map $P_{1}\otimes _{R}B\to P_{0}\otimes _{R}B$ , which is isomorphic to $A\otimes _{R}B$ .

Alternatively, one can define $\mathrm {Tor}$ by fixing A and taking the left derived functors of the right exact functor $G(B)=A\otimes _{R}B$ . That is, tensor A with a projective resolution of B and take homology. Cartan and Eilenberg showed that these constructions are independent of the choice of projective resolution, and that both constructions yield the same Tor groups. Moreover, for a fixed ring R , $\mathrm {Tor}$ is a functor in each variable (from R -modules to abelian groups).

For a commutative ring R and R -modules A and B , $\operatorname {Tor} _{i}^{R}(A,B)$ is an R -module (using that $A\otimes _{R}B$ is an R -module in this case). For a non-commutative ring R , $\operatorname {Tor} _{i}^{R}(A,B)$ is only an abelian group, in general. If R is an algebra over a ring S (which means in particular that S is commutative), then $\operatorname {Tor} _{i}^{R}(A,B)$ is at least an S -module.

## Properties

Here are some of the basic properties and computations of Tor groups.

- $\mathrm {Tor} _{0}^{R}(A,B)\cong A\otimes _{R}B$ for any right R -module A and left R -module B .
- $\mathrm {Tor} _{i}^{R}(A,B)=0$ for all $i>0$ if either A or B is flat (for example, free) as an R -module. In fact, one can compute Tor using a flat resolution of either A or B ; this is more general than a projective (or free) resolution.
- If $A,B$ are finitely generated abelian groups, then $\operatorname {Tor} _{1}^{\mathbb {Z} }(A,B)\cong A_{\text{tor}}\otimes _{\mathbb {Z} }B_{\text{tor}}$ , where $A_{\text{tor}}$ is the torsion subgroup of A .
- There are converses to the previous statement:
  - If $\mathrm {Tor} _{1}^{R}(A,B)=0$ for all B , then A is flat (and hence $\mathrm {Tor} _{i}^{R}(A,B)=0$ for all $i>0$ ).
  - If $\mathrm {Tor} _{1}^{R}(A,B)=0$ for all A , then B is flat (and hence $\mathrm {Tor} _{i}^{R}(A,B)=0$ for all $i>0$ ).
- By the general properties of derived functors, every short exact sequence $0\to K\to L\to M\to 0$ of right R -modules induces a long exact sequence of the form $\cdots \to \operatorname {Tor} _{2}^{R}(M,B)\to \operatorname {Tor} _{1}^{R}(K,B)\to \operatorname {Tor} _{1}^{R}(L,B)\to \operatorname {Tor} _{1}^{R}(M,B)\to K\otimes _{R}B\to L\otimes _{R}B\to M\otimes _{R}B\to 0,$ for any left R -module B . The analogous exact sequence also holds for Tor with respect to the second variable.
- Symmetry: for a commutative ring R , there is a natural isomorphism $\mathrm {Tor} _{i}^{R}(A,B)\cong \mathrm {Tor} _{i}^{R}(B,A)$ . (For R commutative, there is no need to distinguish between left and right R -modules.)
- If R is a commutative ring and u in R is not a zero divisor, then for any R -module B , $\operatorname {Tor} _{i}^{R}(R/(u),B)\cong {\begin{cases}B/uB&i=0\\B[u]&i=1\\0&{\text{otherwise}}\end{cases}}$ where $B[u]=\{x\in B:ux=0\}$ is the u -torsion subgroup of B . This is the explanation for the name Tor. Taking R to be the ring $\mathbb {Z}$ of integers, this calculation can be used to compute $\operatorname {Tor} _{1}^{\mathbb {Z} }(A,B)$ for any finitely generated abelian group A .
- Generalizing the previous example, one can compute Tor groups that involve the quotient of a commutative ring by any regular sequence, using the Koszul complex. For example, if R is the polynomial ring $k[x_{1},\ldots ,x_{n}]$ over a field k , then $\operatorname {Tor} _{*}^{R}(k,k)$ is the exterior algebra over k on n generators in $\mathrm {Tor} _{1}$ .
- $\operatorname {Tor} _{i}^{\mathbb {Z} }(A,B)=0$ for all $i\geq 2$ . The reason: every abelian group A has a free resolution of length 1, since every subgroup of a free abelian group is free abelian.
- Generalizing the previous example, $\operatorname {Tor} _{i}^{R}(A,B)=0$ for all $i\geq 2$ if R is a principal ideal domain (PID). The reason: every module A over a PID has a free resolution of length 1, since every submodule of a free module over a PID is free.
- For any ring R , Tor preserves direct sums (possibly infinite) and filtered colimits in each variable. For example, in the first variable, this says that ${\begin{aligned}\operatorname {Tor} _{i}^{R}\left(\bigoplus _{\alpha }M_{\alpha },N\right)&\cong \bigoplus _{\alpha }\operatorname {Tor} _{i}^{R}(M_{\alpha },N)\\\operatorname {Tor} _{i}^{R}\left(\varinjlim _{\alpha }M_{\alpha },N\right)&\cong \varinjlim _{\alpha }\operatorname {Tor} _{i}^{R}(M_{\alpha },N)\end{aligned}}$
- Flat base change: for a commutative flat R -algebra T , R -modules A and B , and an integer i , $\mathrm {Tor} _{i}^{R}(A,B)\otimes _{R}T\cong \mathrm {Tor} _{i}^{T}(A\otimes _{R}T,B\otimes _{R}T).$ It follows that Tor commutes with localization. That is, for a multiplicatively closed set S in R , $S^{-1}\operatorname {Tor} _{i}^{R}(A,B)\cong \operatorname {Tor} _{i}^{S^{-1}R}\left(S^{-1}A,S^{-1}B\right).$
- For a commutative ring R and commutative R -algebras A and B , $\mathrm {Tor} _{*}^{R}(A,B)$ has the structure of a graded-commutative algebra over R . Moreover, elements of odd degree in the Tor algebra have square zero, and there are divided power operations on the elements of positive even degree.

## Important special cases

- Group homology is defined by $H_{*}(G,M)=\operatorname {Tor} _{*}^{\mathbb {Z} [G]}(\mathbb {Z} ,M),$ where *G* is a group, *M* is a representation of *G* over the integers, and $\mathbb {Z} [G]$ is the group ring of *G*.
- For an algebra *A* over a field *k* and an *A*-bimodule *M*, Hochschild homology is defined by $HH_{*}(A,M)=\operatorname {Tor} _{*}^{A\otimes _{k}A^{\text{op}}}(A,M).$
- Lie algebra homology is defined by $H_{*}({\mathfrak {g}},M)=\operatorname {Tor} _{*}^{U{\mathfrak {g}}}(R,M)$ , where ${\mathfrak {g}}$ is a Lie algebra over a commutative ring *R*, *M* is a ${\mathfrak {g}}$ -module, and $U{\mathfrak {g}}$ is the universal enveloping algebra.
- For a commutative ring *R* with a homomorphism onto a field *k*, $\operatorname {Tor} _{*}^{R}(k,k)$ is a graded-commutative Hopf algebra over *k*. (If *R* is a Noetherian local ring with residue field *k*, then the dual Hopf algebra to $\operatorname {Tor} _{*}^{R}(k,k)$ is Ext* *R*(*k*,*k*).) As an algebra, $\operatorname {Tor} _{*}^{R}(k,k)$ is the free graded-commutative divided power algebra on a graded vector space π*(*R*). When *k* has characteristic zero, π*(*R*) can be identified with the André-Quillen homology *D**(*k*/*R*,*k*).
