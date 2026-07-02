---
title: "Chain complex"
source: https://en.wikipedia.org/wiki/Chain_complex
domain: homological-algebra
license: CC-BY-SA-4.0
tags: homological algebra, chain complex, exact sequence, derived functor
fetched: 2026-07-02
---

# Chain complex

In mathematics, a **chain complex** is an algebraic structure that consists of a sequence of abelian groups (or modules) and a sequence of homomorphisms between consecutive groups such that the image of each homomorphism is contained in the kernel of the next. Associated to a chain complex is its homology, which is (loosely speaking) a measure of the failure of a chain complex to be exact.

A **cochain complex** is similar to a chain complex, except that its homomorphisms are in the opposite direction. The homology of a cochain complex is called its cohomology.

In algebraic topology, the singular chain complex of a topological space X is constructed using continuous maps from a simplex to X, and the homomorphisms of the chain complex capture how these maps restrict to the boundary of the simplex. The homology of this chain complex is called the singular homology of X, and is a commonly used invariant of a topological space.

Chain complexes are studied in homological algebra, but are used in several areas of mathematics, including abstract algebra, Galois theory, differential geometry and algebraic geometry. They can be defined more generally in abelian categories.

## Definitions

A **chain complex** $(A_{\bullet },d_{\bullet })$ is a sequence of abelian groups or modules $\cdots ,A_{0},A_{1},A_{2},\dots$ connected by homomorphisms (called **boundary operators** or **differentials**) $d_{n}:A_{n}\to A_{n-1}$ , such that the composition of any two consecutive maps is the zero map. Explicitly, the differentials satisfy $d_{n}\circ d_{n+1}=0$ for all n , or, concisely, $d^{2}=0$ . The complex may be written out as follows:

$\cdots \xleftarrow {d_{0}} A_{0}\xleftarrow {d_{1}} A_{1}\xleftarrow {d_{2}} A_{2}\xleftarrow {d_{3}} A_{3}\xleftarrow {d_{4}} A_{4}\xleftarrow {d_{5}} \cdots$

The **cochain complex** $(A^{\bullet },d^{\bullet })$ is the dual notion to a chain complex. It consists of a sequence of abelian groups or modules $\cdots ,A^{0},A^{1},A^{2},\dots$ connected by homomorphisms (**coboundary operators**) $d^{n}:A^{n}\to A^{n+1}$ satisfying $d^{n+1}\circ d^{n}=0$ . The cochain complex may be written out in a similar fashion to the chain complex:

$\cdots \xrightarrow {d^{-1}} A^{0}\xrightarrow {d^{0}} A^{1}\xrightarrow {d^{1}} A^{2}\xrightarrow {d^{2}} A^{3}\xrightarrow {d^{3}} A^{4}\xrightarrow {d^{4}} \cdots$

In both cases, the index n is referred to as the **degree** (or **dimension**). The difference between chain and cochain complexes is that, in chain complexes, the differentials decrease dimension, whereas in cochain complexes they increase dimension. All the concepts and definitions for chain complexes apply to cochain complexes, except that they will follow this different convention for dimension, and often terms will be given the prefix *co-*. In this article, definitions will be given for chain complexes when the distinction is not required.

A **bounded chain complex** is one in which almost all the $A_{n}$ are 0; that is, a finite complex extended to the left and right by 0. An example is the chain complex defining the simplicial homology of a finite simplicial complex. A chain complex is **bounded above** if all modules above some fixed degree N are 0, and is **bounded below** if all modules below some fixed degree are 0. Clearly, a complex is bounded both above and below if and only if the complex is bounded.

The elements of the individual groups of a (co)chain complex are called **(co)chains**. The elements in the kernel of d are called **(co)cycles** (or **closed** elements), and the elements in the image of *d* are called **(co)boundaries** (or **exact** elements). Right from the definition of the differential, all boundaries are cycles. The ***n*-th (co)homology group** *H**n* (*H**n*) is the group of (co)cycles modulo (co)boundaries in degree *n*, that is,

$H_{n}=\ker d_{n}/{\mbox{im }}d_{n+1}\quad \left(H^{n}=\ker d^{n}/{\mbox{im }}d^{n-1}\right)$

### Exact sequences

An **exact sequence** (or **exact** complex) is a chain complex whose homology groups are all zero. This means all closed elements in the complex are exact. A **short exact sequence** is a bounded exact sequence in which only the groups *A**k*, *A**k*+1, *A**k*+2 may be nonzero. For example, the following chain complex is a short exact sequence.

$\cdots {\xrightarrow {}}\;0\;{\xrightarrow {}}\;\mathbf {Z} \;{\xrightarrow {\times p}}\;\mathbf {Z} \twoheadrightarrow \mathbf {Z} /p\mathbf {Z} \;{\xrightarrow {}}\;0\;{\xrightarrow {}}\cdots$

In the middle group, the closed elements are the elements p**Z**; these are clearly the exact elements in this group.

### Chain maps

A **chain map** *f* between two chain complexes $(A_{\bullet },d_{A,\bullet })$ and $(B_{\bullet },d_{B,\bullet })$ is a sequence $f_{\bullet }$ of homomorphisms $f_{n}:A_{n}\rightarrow B_{n}$ for each *n* that commutes with the boundary operators on the two chain complexes, so $d_{B,n}\circ f_{n}=f_{n-1}\circ d_{A,n}$ . This is written out in the following commutative diagram.

A chain map sends cycles to cycles and boundaries to boundaries, and thus induces a map on homology $(f_{\bullet })_{*}:H_{\bullet }(A_{\bullet },d_{A,\bullet })\rightarrow H_{\bullet }(B_{\bullet },d_{B,\bullet })$ .

A continuous map *f* between topological spaces *X* and *Y* induces a chain map between the singular chain complexes of *X* and *Y*, and hence induces a map *f** between the singular homology of *X* and *Y* as well. When *X* and *Y* are both equal to the *n*-sphere, the map induced on homology defines the degree of the map *f*.

The concept of chain map reduces to the one of boundary through the construction of the cone of a chain map.

### Chain homotopy

A chain homotopy offers a way to relate two chain maps that induce the same map on homology groups, even though the maps may be different. Given two chain complexes *A* and *B*, and two chain maps *f*, *g* : *A* → *B*, a **chain homotopy** is a sequence of homomorphisms *h**n* : *A**n* → *B**n*+1 such that *hd**A* + *d**B**h* = *f* − *g*. The maps may be written out in a diagram as follows, but this diagram is not commutative.

The map *hd**A* + *d**B**h* is easily verified to induce the zero map on homology, for any *h*. It immediately follows that *f* and *g* induce the same map on homology. One says *f* and *g* are **chain homotopic** (or simply **homotopic**), and this property defines an equivalence relation between chain maps.

Let *X* and *Y* be topological spaces. In the case of singular homology, a homotopy between continuous maps *f*, *g* : *X* → *Y* induces a chain homotopy between the chain maps corresponding to *f* and *g*. This shows that two homotopic maps induce the same map on singular homology. The name "chain homotopy" is motivated by this example.

## Examples

### Singular homology

Let *X* be a topological space. Define *C**n*(*X*) for natural *n* to be the free abelian group formally generated by singular n-simplices in *X*, and define the boundary map $\partial _{n}:C_{n}(X)\to C_{n-1}(X)$ to be

${\displaystyle \partial _{n}:\,(\sigma$

where the hat denotes the omission of a vertex. That is, the boundary of a singular simplex is the alternating sum of restrictions to its faces. It can be shown that ∂2 = 0, so $(C_{\bullet },\partial _{\bullet })$ is a chain complex; the **singular homology** $H_{\bullet }(X)$ is the homology of this complex.

Singular homology is a useful invariant of topological spaces up to homotopy equivalence. The degree zero homology group is a free abelian group on the path-components of *X*.

### de Rham cohomology

The differential *k*-forms on any smooth manifold *M* form a real vector space called Ω*k*(*M*) under addition. The exterior derivative *d* maps Ω*k*(*M*) to Ω*k*+1(*M*), and *d*2 = 0 follows essentially from symmetry of second derivatives, so the vector spaces of *k*-forms along with the exterior derivative are a cochain complex.

$0{\stackrel {\subset }{\to }}\ {\Re ^{c}}{\stackrel {\subset }{\to }}\ {\Omega ^{0}(M)}{\stackrel {d}{\to }}\ {\Omega ^{1}(M)}{\stackrel {d}{\to }}\ {\Omega ^{2}(M)}{\stackrel {d}{\to }}\ \Omega ^{3}(M)\to \cdots$

The cohomology of this complex is called the **de Rham cohomology** of *M*. Locally constant functions are designated with its isomorphism $\Re ^{c}$ with c the count of mutually disconnected components of *M*. This way the complex was extended to leave the complex exact at zero-form level using the subset operator.

Smooth maps between manifolds induce chain maps, and smooth homotopies between maps induce chain homotopies.

## Category of chain complexes

Chain complexes of K -modules with chain maps as morphisms form a category $\mathbf {Ch} _{K}$ , where K is a commutative ring.

If $V=V_{*}$ and $W=W_{*}$ are chain complexes, their **tensor product** $V\otimes W$ is a chain complex with degree n elements given by

$(V\otimes W)_{n}=\bigoplus _{\{i,j\mid i+j=n\}}V_{i}\otimes W_{j}$

and differential given by

$\partial (a\otimes b)=\partial a\otimes b+(-1)^{\left|a\right|}a\otimes \partial b$

where a and b are any two homogeneous vectors in V and W respectively, and $\left|a\right|$ denotes the degree of a .

This tensor product makes the category $\mathbf {Ch} _{K}$ into a symmetric monoidal category. The identity object with respect to this monoidal product is the base ring K viewed as a chain complex in degree 0 . The braiding is given on simple tensors of homogeneous elements by

$a\otimes b\mapsto (-1)^{\left|a\right|\left|b\right|}b\otimes a$

The sign is necessary for the braiding to be a chain map.

Moreover, the category of chain complexes of K -modules also has internal Hom: given chain complexes V and W , the internal Hom of V and W , denoted $\mathrm {Hom} (V,W)$ , is the chain complex with degree n elements given by $\Pi _{i}{\text{Hom}}_{K}(V_{i},W_{i+n})$ and differential given by

$(\partial f)(v)=\partial (f(v))-(-1)^{\left|f\right|}f(\partial (v))$

.

We have a natural isomorphism

${\text{Hom}}(A\otimes B,C)\cong {\text{Hom}}(A,{\text{Hom}}(B,C))$

## Further examples

- Amitsur complex
- A complex used to define Bloch's higher Chow groups
- Buchsbaum–Rim complex
- Čech complex
- Cousin complex
- Eagon–Northcott complex
- Gersten complex
- Graph complex
- Koszul complex
- Moore complex
- Schur complex
