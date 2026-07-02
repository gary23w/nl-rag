---
title: "Homology (mathematics)"
source: https://en.wikipedia.org/wiki/Homology_(mathematics)
domain: algebraic-topology
license: CC-BY-SA-4.0
tags: algebraic topology, homotopy theory, homology group, fundamental group
fetched: 2026-07-02
---

# Homology (mathematics)

In mathematics, the term **homology**, originally introduced in algebraic topology, has three primary, closely related usages. First, there is the *homology of a chain complex*, a sequence of abelian groups, called *homology groups*, which are regarded as fundamental invariants of the chain complex. Secondly, when one can associate a chain complex to a different mathematical object, one can also associate its homology to that object. Distinct procedures of associating chain complexes to a given object are grouped into *homology theories*. Finally, homology is important in the study of topological spaces. Under nice conditions in which distinct homology theories for a single topological space produce the same homology groups, one can define a single *homology of a topological space*. This last notion of homology is closely related to topological ideas frequently discussed in popular mathematics such as the holes of a surface or the cycles of a graph. There is also a related notion of the cohomology of a cochain complex, giving rise to various cohomology theories, in addition to the notion of the cohomology of a topological space.

## Homology of chain complexes

We start with a **chain complex,** which is a sequence $(C_{\bullet },d_{\bullet })$ of abelian groups $C_{n}$ (whose elements are called chains) and group homomorphisms $d_{n}$ (called boundary maps):

$\cdots \longrightarrow C_{n+1}{\stackrel {d_{n+1}}{\longrightarrow }}C_{n}{\stackrel {d_{n}}{\longrightarrow }}C_{n-1}{\stackrel {d_{n-1}}{\longrightarrow }}\cdots$

,

such that the composition of any two consecutive maps is zero:

$d_{n}\circ d_{n+1}=0.$

The n th group of **cycles**, $Z_{n}$ , is given by the kernel subgroup

$Z_{n}=\ker d_{n}=\{c\in C_{n}\,|\;d_{n}(c)=0\}$

,

and the n th group of **boundaries**, $B_{n}$ , is given by the image subgroup

$B_{n}:=\mathrm {im} \,d_{n+1}=\{d_{n+1}(c)\,|\;c\in C_{n+1}\}$

.

The n th **homology group** $H_{n}$ of this chain complex is then the quotient group $H_{n}=Z_{n}/B_{n}$ of cycles modulo boundaries.

One can endow chain complexes with additional structure: for example, taking the groups $C_{n}$ to be modules over a coefficient ring R and taking the boundary maps $d_{n}$ to be R -module homomorphisms results in homology groups $H_{n}$ that are also quotient modules.

Tools from homological algebra can be used to relate homology groups of different chain complexes.

## Homology theories

To associate a *homology theory* to other types of mathematical objects, one first gives a prescription for associating chain complexes to that object, and then takes the homology of such a chain complex. For the homology theory to be valid, all such chain complexes associated to the same mathematical object must have the same homology. The resulting homology theory is often named according to the type of chain complex prescribed. For example, singular homology, Morse homology, Khovanov homology, and Hochschild homology are respectively obtained from singular chain complexes, Morse complexes, Khovanov complexes, and Hochschild complexes. In other cases, such as for group homology, there are multiple common methods to compute the same homology groups.

In the language of category theory, a homology theory is a type of functor from the category of the mathematical object being studied to the category of abelian groups and group homomorphisms, or more generally to the category corresponding to the associated chain complexes. One can also formulate homology theories as derived functors on appropriate abelian categories, measuring the failure of an appropriate functor to be exact. One can describe this latter construction explicitly in terms of resolutions, or more abstractly from the perspective of derived categories or model categories.

Regardless of how they are formulated, homology theories help provide information about the structure of the mathematical objects to which they are associated, and can sometimes help distinguish different objects.

## Homology of a topological space

Perhaps the most familiar usage of the term homology is for the *homology of a topological space*. For sufficiently nice topological spaces and compatible choices of coefficient rings, any homology theory satisfying the Eilenberg–Steenrod axioms yields the same homology groups as the singular homology (see below) of that topological space, with the consequence that one often simply refers to the "homology" of that space, instead of specifying which homology theory was used to compute the homology groups in question.

For 1-dimensional topological spaces, probably the simplest homology theory to use is graph homology, which could be regarded as a 1-dimensional special case of simplicial homology, the latter of which involves a decomposition of the topological space into simplices. (Simplices are a generalization of triangles to arbitrary dimension; for example, an edge in a graph is homeomorphic to a one-dimensional simplex, and a triangle-based pyramid is a 3-simplex.) Simplicial homology can in turn be generalized to singular homology, which allows more general maps of simplices into the topological space. Replacing simplices with disks of various dimensions results in a related construction called cellular homology.

There are also other ways of computing these homology groups, for example via Morse homology, or by taking the output of the universal coefficient theorem when applied to a cohomology theory such as Čech cohomology or (in the case of real coefficients) De Rham cohomology.

### Inspirations for homology (informal discussion)

One of the ideas that led to the development of homology was the observation that certain low-dimensional shapes can be topologically distinguished by examining their "holes." For instance, a figure-eight shape has more holes than a circle $S^{1}$ , and a 2-torus $T^{2}$ (a 2-dimensional surface shaped like an inner tube) has different holes from a 2-sphere $S^{2}$ (a 2-dimensional surface shaped like a basketball).

Studying topological features such as these led to the notion of the *cycles* that represent homology classes (the elements of homology groups). For example, the two embedded circles in a figure-eight shape provide examples of one-dimensional cycles, or 1-cycles, and the 2-torus $T^{2}$ and 2-sphere $S^{2}$ represent 2-cycles. Cycles form a group under the operation of *formal addition,* which refers to adding cycles symbolically rather than combining them geometrically. Any formal sum of cycles is again called a cycle.

### Cycles and boundaries (informal discussion)

Explicit constructions of homology groups are somewhat technical. As mentioned above, an explicit realization of the homology groups $H_{n}(X)$ of a topological space X is defined in terms of the *cycles* and *boundaries* of a *chain complex* $(C_{\bullet },d_{\bullet })$ associated to X , where the type of chain complex depends on the choice of homology theory in use. These cycles and boundaries are elements of abelian groups, and are defined in terms of the boundary homomorphisms $d_{n}:C_{n}\to C_{n-1}$ of the chain complex, where each $C_{n}$ is an abelian group, and the $d_{n}$ are group homomorphisms that satisfy $d_{n-1}\circ d_{n}=0$ for all n .

Since such constructions are somewhat technical, informal discussions of homology sometimes focus instead on topological notions that parallel some of the group-theoretic aspects of cycles and boundaries.

For example, in the context of chain complexes, a **boundary** is any element of the image $B_{n}:=\mathrm {im} \,d_{n+1}:=\{d_{n+1}(c)\,|\;c\in C_{n+1}\}$ of the boundary homomorphism $d_{n}:C_{n}\to C_{n-1}$ , for some n . In topology, the boundary of a space is technically obtained by taking the space's closure minus its interior, but it is also a notion familiar from examples, e.g., the boundary of the unit disk is the unit circle, or more topologically, the boundary of $D^{2}$ is $S^{1}$ .

Topologically, the boundary of the closed interval $[0,1]$ is given by the disjoint union $\{0\}\,\amalg \,\{1\}$ , and with respect to suitable orientation conventions, the oriented boundary of $[0,1]$ is given by the union of a positively oriented $\{1\}$ with a negatively oriented $\{0\}.$ The simplicial chain complex analog of this statement is that $d_{1}([0,1])=\{1\}-\{0\}$ . (Since $d_{1}$ is a homomorphism, this implies $d_{1}(k\cdot [0,1])=k\cdot \{1\}-k\cdot \{0\}$ for any integer k .)

In the context of chain complexes, a **cycle** is any element of the kernel $Z_{n}:=\ker d_{n}:=\{c\in C_{n}\,|\;d_{n}(c)=0\}$ , for some n . In other words, $c\in C_{n}$ is a cycle if and only if $d_{n}(c)=0$ . The closest topological analog of this idea would be a shape that has "no boundary," in the sense that its boundary is the empty set. For example, since $S^{1},S^{2}$ , and $T^{2}$ have no boundary, one can associate cycles to each of these spaces. However, the chain complex notion of cycles (elements whose boundary is a "zero chain") is more general than the topological notion of a shape with no boundary.

It is this topological notion of no boundary that people generally have in mind when they claim that cycles can intuitively be thought of as detecting holes. The idea is that for no-boundary shapes like $S^{1}$ , $S^{2}$ , and $T^{2}$ , it is possible in each case to glue on a larger shape for which the original shape is the boundary. For instance, starting with a circle $S^{1}$ , one could glue a 2-dimensional disk $D^{2}$ to that $S^{1}$ such that the $S^{1}$ is the boundary of that $D^{2}$ . Similarly, given a two-sphere $S^{2}$ , one can glue a ball $B^{3}$ to that $S^{2}$ such that the $S^{2}$ is the boundary of that $B^{3}$ . This phenomenon is sometimes described as saying that $S^{2}$ has a $B^{3}$ -shaped "hole" or that it could be "filled in" with a $B^{3}$ .

More generally, any shape with no boundary can be "filled in" with a cone, since if a given space Y has no boundary, then the boundary of the cone on Y is given by Y , and so if one "filled in" Y by gluing the cone on Y onto Y , then Y would be the boundary of that cone. (For example, a cone on $S^{1}$ is homeomorphic to a disk $D^{2}$ whose boundary is that $S^{1}$ .) However, it is sometimes desirable to restrict to nicer spaces such as manifolds, and not every cone is homeomorphic to a manifold. Embedded representatives of 1-cycles, 3-cycles, and oriented 2-cycles all admit manifold-shaped holes, but for example the real projective plane $\mathbb {RP} ^{2}$ and complex projective plane $\mathbb {CP} ^{2}$ have nontrivial cobordism classes and therefore cannot be "filled in" with manifolds.

On the other hand, the boundaries discussed in the homology of a topological space X are different from the boundaries of "filled in" holes, because the homology of a topological space X has to do with the original space X , and not with new shapes built from gluing extra pieces onto X . For example, any embedded circle C in $S^{2}$ already bounds some embedded disk D in $S^{2}$ , so such C gives rise to a boundary class in the homology of $S^{2}$ . By contrast, no embedding of $S^{1}$ into one of the 2 lobes of the figure-eight shape gives a boundary, despite the fact that it is possible to glue a disk onto a figure-eight lobe.

### Homology groups

Given a sufficiently-nice topological space X , a choice of appropriate homology theory, and a chain complex $(C_{\bullet },d_{\bullet })$ associated to X that is compatible with that homology theory, the n th homology group $H_{n}(X)$ is then given by the quotient group $H_{n}(X)=Z_{n}/B_{n}$ of n -cycles ( n -dimensional cycles) modulo n -dimensional boundaries. In other words, the elements of $H_{n}(X)$ , called *homology classes*, are equivalence classes whose representatives are n -cycles, and any two cycles are regarded as equal in $H_{n}(X)$ if and only if they differ by the addition of a boundary. This also implies that the "zero" element of $H_{n}(X)$ is given by the group of n -dimensional boundaries, which also includes formal sums of such boundaries.

## Informal examples

The homology of a topological space *X* is a set of topological invariants of *X* represented by its *homology groups* $H_{0}(X),H_{1}(X),H_{2}(X),\ldots$ where the $k^{\rm {th}}$ homology group $H_{k}(X)$ describes, informally, the number of holes in *X* with a *k*-dimensional boundary. A 0-dimensional-boundary hole is simply a gap between two components. Consequently, $H_{0}(X)$ describes the path-connected components of *X*.

The circle or 1-sphere

$S^{1}$

The 2-sphere

$S^{2}$

is the outer shell, not the interior, of a ball

A one-dimensional sphere $S^{1}$ is a circle. It has a single connected component and a one-dimensional-boundary hole, but no higher-dimensional holes. The corresponding homology groups are given as $H_{k}\left(S^{1}\right)={\begin{cases}\mathbb {Z} &k=0,1\\\{0\}&{\text{otherwise}}\end{cases}}$ where $\mathbb {Z}$ is the group of integers and $\{0\}$ is the trivial group. The group $H_{1}\left(S^{1}\right)=\mathbb {Z}$ represents a finitely-generated abelian group, with a single generator representing the one-dimensional hole contained in a circle.

A two-dimensional sphere $S^{2}$ has a single connected component, no one-dimensional-boundary holes, a two-dimensional-boundary hole, and no higher-dimensional holes. The corresponding homology groups are $H_{k}\left(S^{2}\right)={\begin{cases}\mathbb {Z} &k=0,2\\\{0\}&{\text{otherwise}}\end{cases}}$

In general for an *n*-dimensional sphere $S^{n},$ the homology groups are $H_{k}\left(S^{n}\right)={\begin{cases}\mathbb {Z} &k=0,n\\\{0\}&{\text{otherwise}}\end{cases}}$

The solid disc or 2-ball

$B^{2}$

The torus

$T=S^{1}\times S^{1}$

A two-dimensional ball $B^{2}$ is a solid disc. It has a single path-connected component, but in contrast to the circle, has no higher-dimensional holes. The corresponding homology groups are all trivial except for $H_{0}\left(B^{2}\right)=\mathbb {Z}$ . In general, for an *n*-dimensional ball $B^{n},$ $H_{k}\left(B^{n}\right)={\begin{cases}\mathbb {Z} &k=0\\\{0\}&{\text{otherwise}}\end{cases}}$

The torus is defined as a product of two circles $T^{2}=S^{1}\times S^{1}$ . The torus has a single path-connected component, two independent one-dimensional holes (indicated by circles in red and blue) and one two-dimensional hole as the interior of the torus. The corresponding homology groups are $H_{k}(T^{2})={\begin{cases}\mathbb {Z} &k=0,2\\\mathbb {Z} \times \mathbb {Z} &k=1\\\{0\}&{\text{otherwise}}\end{cases}}$

If *n* products of a topological space *X* is written as $X^{n}$ , then in general, for an *n*-dimensional torus $T^{n}=(S^{1})^{n}$ , $H_{k}(T^{n})={\begin{cases}\mathbb {Z} ^{\binom {n}{k}}&0\leq k\leq n\\\{0\}&{\text{otherwise}}\end{cases}}$ (see *Torus § n-dimensional torus* and *Betti number § More examples* for more details).

The two independent 1-dimensional holes form independent generators in a finitely generated abelian group, expressed as the product group $\mathbb {Z} \times \mathbb {Z} .$

For the projective plane *P*, a simple computation shows (where $\mathbb {Z} _{2}$ is the cyclic group of order 2): $H_{k}(P)={\begin{cases}\mathbb {Z} &k=0\\\mathbb {Z} _{2}&k=1\\\{0\}&{\text{otherwise}}\end{cases}}$ $H_{0}(P)=\mathbb {Z}$ corresponds, as in the previous examples, to the fact that there is a single connected component. $H_{1}(P)=\mathbb {Z} _{2}$ is a new phenomenon: intuitively, it corresponds to the fact that there is a single non-contractible "loop", but if we do the loop twice, it becomes contractible to zero. This phenomenon is called **torsion**.

## Construction of homology groups

The following text describes a general algorithm for constructing the homology groups. It may be easier for the reader to look at some simple examples first: graph homology and simplicial homology.

The general construction begins with an object such as a topological space *X*, on which one first defines a *chain complex* *C*(*X*) encoding information about *X*. A chain complex is a sequence of abelian groups or modules $C_{0},C_{1},C_{2},\ldots$ . connected by homomorphisms $\partial _{n}:C_{n}\to C_{n-1},$ which are called **boundary operators**. That is,

$\dotsb {\overset {\partial _{n+1}}{\longrightarrow \,}}C_{n}{\overset {\partial _{n}}{\longrightarrow \,}}C_{n-1}{\overset {\partial _{n-1}}{\longrightarrow \,}}\dotsb {\overset {\partial _{2}}{\longrightarrow \,}}C_{1}{\overset {\partial _{1}}{\longrightarrow \,}}C_{0}{\overset {\partial _{0}}{\longrightarrow \,}}0$

where 0 denotes the trivial group and $C_{i}\equiv 0$ for *i* < 0. It is also required that the composition of any two consecutive boundary operators be trivial. That is, for all *n*,

$\partial _{n}\circ \partial _{n+1}=0_{n+1,n-1},$

i.e., the constant map sending every element of $C_{n+1}$ to the group identity in $C_{n-1}.$

The statement that the boundary of a boundary is trivial is equivalent to the statement that $\operatorname {im} (\partial _{n+1})\subseteq \ker(\partial _{n})$ , where $\operatorname {im} (\partial _{n+1})$ denotes the image of the boundary operator and $\ker(\partial _{n})$ its kernel. Elements of $B_{n}(X)=\mathrm {im} (\partial _{n+1})$ are called **boundaries** and elements of $Z_{n}(X)=\ker(\partial _{n})$ are called **cycles**.

Since each chain group *Cn* is abelian all its subgroups are normal. Then because $\ker(\partial _{n})$ is a subgroup of *Cn*, $\ker(\partial _{n})$ is abelian, and since $\operatorname {im} (\partial _{n+1})\subseteq \ker(\partial _{n})$ therefore $\operatorname {im} (\partial _{n+1})$ is a normal subgroup of $\ker(\partial _{n})$ . Then one can create the quotient group

$H_{n}(X):=\ker(\partial _{n})/\operatorname {im} (\partial _{n+1})=Z_{n}(X)/B_{n}(X),$

called the ***n*th homology group of *X***. The elements of *Hn*(*X*) are called **homology classes**. Each homology class is an equivalence class over cycles and two cycles in the same homology class are said to be **homologous**.

A chain complex is said to be exact if the image of the (*n*+1)th map is always equal to the kernel of the *n*th map. The homology groups of *X* therefore measure "how far" the chain complex associated to *X* is from being exact.

The reduced homology groups of a chain complex *C*(*X*) are defined as homologies of the augmented chain complex

$\dotsb {\overset {\partial _{n+1}}{\longrightarrow \,}}C_{n}{\overset {\partial _{n}}{\longrightarrow \,}}C_{n-1}{\overset {\partial _{n-1}}{\longrightarrow \,}}\dotsb {\overset {\partial _{2}}{\longrightarrow \,}}C_{1}{\overset {\partial _{1}}{\longrightarrow \,}}C_{0}{\overset {\varepsilon }{\longrightarrow \,}}\mathbb {Z} {\longrightarrow \,}0$

where the boundary operator $\varepsilon$ is

$\varepsilon \left(\sum _{i}n_{i}\sigma _{i}\right)=\sum _{i}n_{i}$

for a combination $\sum n_{i}\sigma _{i},$ of points $\sigma _{i},$ which are the fixed generators of *C*0. The reduced homology groups ${\tilde {H}}_{i}(X)$ coincide with $H_{i}(X)$ for $i\neq 0.$ The extra $\mathbb {Z}$ in the chain complex represents the unique map $[\emptyset ]\longrightarrow X$ from the empty simplex to *X*.

Computing the cycle $Z_{n}(X)$ and boundary $B_{n}(X)$ groups is usually rather difficult since they have a very large number of generators. On the other hand, there are tools which make the task easier.

The *simplicial homology* groups *Hn*(*X*) of a *simplicial complex* *X* are defined using the simplicial chain complex *C*(*X*), with *Cn*(*X*) the free abelian group generated by the *n*-simplices of *X*. See simplicial homology for details.

The *singular homology* groups *Hn*(*X*) are defined for any topological space *X*, and agree with the simplicial homology groups for a simplicial complex.

Cohomology groups are formally similar to homology groups: one starts with a cochain complex, which is the same as a chain complex but whose arrows, now denoted $d_{n},$ point in the direction of increasing *n* rather than decreasing *n*; then the groups $\ker \left(d^{n}\right)=Z^{n}(X)$ of *cocycles* and $\operatorname {im} \left(d^{n-1}\right)=B^{n}(X)$ of *coboundaries* follow from the same description. The *n*th cohomology group of *X* is then the quotient group

$H^{n}(X)=Z^{n}(X)/B^{n}(X),$

in analogy with the *n*th homology group.

## Homology vs. homotopy

The nth homotopy group $\pi _{n}(X)$ of a topological space X is the group of homotopy classes of basepoint-preserving maps from the n -sphere $S^{n}$ to X , under the group operation of concatenation. The most fundamental homotopy group is the fundamental group $\pi _{1}(X)$ . For connected X , the Hurewicz theorem describes a homomorphism $h_{*}:\pi _{n}(X)\to H_{n}(X)$ called the Hurewicz homomorphism. For $n>1$ , this homomorphism can be complicated, but when $n=1$ , the Hurewicz homomorphism coincides with abelianization. That is, $h_{*}:\pi _{1}(X)\to H_{1}(X)$ is surjective and its kernel is the commutator subgroup of $\pi _{1}(X)$ , with the consequence that $H_{1}(X)$ is isomorphic to the abelianization of $\pi _{1}(X)$ . Higher homotopy groups are sometimes difficult to compute. For instance, the homotopy groups of spheres are poorly understood and are not known in general, in contrast to the straightforward description given above for the homology groups.

For an $n=1$ example, suppose X is the figure eight. As usual, its first homotopy group, or fundamental group, $\pi _{1}(X)$ is the group of homotopy classes of directed loops starting and ending at a predetermined point (e.g. its center). It is isomorphic to the free group of rank 2, $\pi _{1}(X)\cong \mathbb {Z} *\mathbb {Z}$ , which is not commutative: looping around the lefthand cycle and then around the righthand cycle is different from looping around the righthand cycle and then looping around the lefthand cycle. By contrast, the figure eight's first homology group $H_{1}(X)\cong \mathbb {Z} \times \mathbb {Z}$ is abelian. To express this explicitly in terms of homology classes of cycles, one could take the homology class l of the lefthand cycle and the homology class r of the righthand cycle as basis elements of $H_{1}(X)$ , allowing us to write $H_{1}(X)=\{a_{l}l+a_{r}r\,|\;a_{l},a_{r}\in \mathbb {Z} \}$ .

## Types of homology

The different types of homology theory arise from functors mapping from various categories of mathematical objects to the category of chain complexes. In each case the composition of the functor from objects to chain complexes and the functor from chain complexes to homology groups defines the overall homology functor for the theory.

### Simplicial homology

The motivating example comes from algebraic topology: the **simplicial homology** of a simplicial complex *X*. Here the chain group *Cn* is the free abelian group or free module whose generators are the *n*-dimensional oriented simplexes of *X*. The orientation is captured by ordering the complex's vertices and expressing an oriented simplex $\sigma$ as an *n*-tuple $(\sigma [0],\sigma [1],\dots ,\sigma [n])$ of its vertices listed in increasing order (i.e. $\sigma [0]<\sigma [1]<\cdots <\sigma [n]$ in the complex's vertex ordering, where $\sigma [i]$ is the i th vertex appearing in the tuple). The mapping $\partial _{n}$ from *Cn* to *Cn−1* is called the *boundary mapping* and sends the simplex

$\sigma =(\sigma [0],\sigma [1],\dots ,\sigma [n])$

to the formal sum

$\partial _{n}(\sigma )=\sum _{i=0}^{n}(-1)^{i}\left(\sigma [0],\dots ,\sigma [i-1],\sigma [i+1],\dots ,\sigma [n]\right),$

\

which is evaluated as 0 if $n=0.$ This behavior on the generators induces a homomorphism on all of *Cn* as follows. Given an element $c\in C_{n}$ , write it as the sum of generators ${\textstyle c=\sum _{\sigma _{i}\in X_{n}}m_{i}\sigma _{i},}$ where $X_{n}$ is the set of *n*-simplexes in *X* and the *mi* are coefficients from the ring *Cn* is defined over (usually integers, unless otherwise specified). Then define

$\partial _{n}(c)=\sum _{\sigma _{i}\in X_{n}}m_{i}\partial _{n}(\sigma _{i}).$

The dimension of the *n*-th homology of *X* turns out to be the number of "holes" in *X* at dimension *n*. It may be computed by putting matrix representations of these boundary mappings in Smith normal form.

### Singular homology

Using simplicial homology example as a model, one can define a *singular homology* for any topological space *X*. A chain complex for *X* is defined by taking *Cn* to be the free abelian group (or free module) whose generators are all continuous maps from *n*-dimensional simplices into *X*. The homomorphisms ∂*n* arise from the boundary maps of simplices.

### Group homology

In abstract algebra, one uses homology to define derived functors, for example the Tor functors. Here one starts with some covariant additive functor *F* and some module *X*. The chain complex for *X* is defined as follows: first find a free module $F_{1}$ and a surjective homomorphism $p_{1}:F_{1}\to X.$ Then one finds a free module $F_{2}$ and a surjective homomorphism $p_{2}:F_{2}\to \ker \left(p_{1}\right).$ Continuing in this fashion, a sequence of free modules $F_{n}$ and homomorphisms $p_{n}$ can be defined. By applying the functor *F* to this sequence, one obtains a chain complex; the homology $H_{n}$ of this complex depends only on *F* and *X* and is, by definition, the *n*-th derived functor of *F*, applied to *X*.

A common use of group (co)homology $H^{2}(G,M)$ is to classify the possible extension groups *E* which contain a given *G*-module *M* as a normal subgroup and have a given quotient group *G*, so that $G=E/M.$

### Other homology theories

- Borel–Moore homology
- Cellular homology
- Cyclic homology
- Hochschild homology
- Floer homology
- Intersection homology
- K-homology
- Khovanov homology
- Morse homology
- Persistent homology
- Steenrod homology

## Homology functors

Chain complexes form a category: A morphism from the chain complex ( $d_{n}:A_{n}\to A_{n-1}$ ) to the chain complex ( $e_{n}:B_{n}\to B_{n-1}$ ) is a sequence of homomorphisms $f_{n}:A_{n}\to B_{n}$ such that $f_{n-1}\circ d_{n}=e_{n}\circ f_{n}$ for all *n*. The *n*-th homology *Hn* can be viewed as a covariant functor from the category of chain complexes to the category of abelian groups (or modules).

If the chain complex depends on the object *X* in a covariant manner (meaning that any morphism $X\to Y$ induces a morphism from the chain complex of *X* to the chain complex of *Y*), then the *Hn* are covariant functors from the category that *X* belongs to into the category of abelian groups (or modules).

The only difference between homology and cohomology is that in cohomology the chain complexes depend in a *contravariant* manner on *X*, and that therefore the homology groups (which are called *cohomology groups* in this context and denoted by *Hn*) form *contravariant* functors from the category that *X* belongs to into the category of abelian groups or modules.

## Properties

If ( $d_{n}:A_{n}\to A_{n-1}$ ) is a chain complex such that all but finitely many *An* are zero, and the others are finitely generated abelian groups (or finite-dimensional vector spaces), then we can define the *Euler characteristic*

$\chi =\sum (-1)^{n}\,\mathrm {rank} (A_{n})$

(using the rank in the case of abelian groups and the Hamel dimension in the case of vector spaces). It turns out that the Euler characteristic can also be computed on the level of homology:

$\chi =\sum (-1)^{n}\,\mathrm {rank} (H_{n})$

and, especially in algebraic topology, this provides two ways to compute the important invariant $\chi$ for the object *X* which gave rise to the chain complex.

Every short exact sequence

$0\rightarrow A\rightarrow B\rightarrow C\rightarrow 0$

of chain complexes gives rise to a long exact sequence of homology groups

$\cdots \to H_{n}(A)\to H_{n}(B)\to H_{n}(C)\to H_{n-1}(A)\to H_{n-1}(B)\to H_{n-1}(C)\to H_{n-2}(A)\to \cdots$

All maps in this long exact sequence are induced by the maps between the chain complexes, except for the maps $H_{n}(C)\to H_{n-1}(A)$ The latter are called *connecting homomorphisms* and are provided by the zig-zag lemma. This lemma can be applied to homology in numerous ways that aid in calculating homology groups, such as the theories of relative homology and Mayer-Vietoris sequences.

## Applications

### Application in pure mathematics

Notable theorems proved using homology include the following:

- The Brouwer fixed point theorem: If *f* is any continuous map from the ball *Bn* to itself, then there is a fixed point $a\in B^{n}$ with $f(a)=a.$
- Invariance of domain: If *U* is an open subset of $\mathbb {R} ^{n}$ and $f:U\to \mathbb {R} ^{n}$ is an injective continuous map, then $V=f(U)$ is open and *f* is a homeomorphism between *U* and *V*.
- The Hairy ball theorem: any continuous vector field on the 2-sphere (or more generally, the 2*k*-sphere for any $k\geq 1$ ) vanishes at some point.
- The Borsuk–Ulam theorem: any continuous function from an *n*-sphere into Euclidean *n*-space maps some pair of antipodal points to the same point. (Two points on a sphere are called antipodal if they are in exactly opposite directions from the sphere's center.)
- Invariance of dimension: if non-empty open subsets $U\subseteq \mathbb {R} ^{m}$ and $V\subseteq \mathbb {R} ^{n}$ are homeomorphic, then $m=n.$

### Application in science and engineering

In topological data analysis, data sets are regarded as a point cloud sampling of a manifold or algebraic variety embedded in Euclidean space. By linking nearest neighbor points in the cloud into a triangulation, a simplicial approximation of the manifold is created and its simplicial homology may be calculated. Finding techniques to robustly calculate homology using various triangulation strategies over multiple length scales is the topic of persistent homology.

In sensor networks, sensors may communicate information via an ad-hoc network that dynamically changes in time. To understand the global context of this set of local measurements and communication paths, it is useful to compute the homology of the network topology to evaluate, for instance, holes in coverage.

In dynamical systems theory in physics, Poincaré was one of the first to consider the interplay between the invariant manifold of a dynamical system and its topological invariants. Morse theory relates the dynamics of a gradient flow on a manifold to, for example, its homology. Floer homology extended this to infinite-dimensional manifolds. The KAM theorem established that periodic orbits can follow complex trajectories; in particular, they may form braids that can be investigated using Floer homology.

In one class of finite element methods, boundary-value problems for differential equations involving the Hodge-Laplace operator may need to be solved on topologically nontrivial domains, for example, in electromagnetic simulations. In these simulations, solution is aided by fixing the cohomology class of the solution based on the chosen boundary conditions and the homology of the domain. FEM domains can be triangulated, from which the simplicial homology can be calculated.

## Software

Various software packages have been developed for the purposes of computing homology groups of finite cell complexes. Linbox is a C++ library for performing fast matrix operations, including Smith normal form; it interfaces with both Gap and Maple. Chomp, CAPD::Redhom Archived 2013-07-15 at the Wayback Machine and Perseus are also written in C++. All three implement pre-processing algorithms based on simple-homotopy equivalence and discrete Morse theory to perform homology-preserving reductions of the input cell complexes before resorting to matrix algebra. Kenzo is written in Lisp, and in addition to homology it may also be used to generate presentations of homotopy groups of finite simplicial complexes. Gmsh includes a homology solver for finite element meshes, which can generate Cohomology bases directly usable by finite element software.

## Some non-homology-based discussions of surfaces

### Origins

Homology theory can be said to start with the Euler polyhedron formula, or Euler characteristic. This was followed by Riemann's definition of genus and *n*-fold connectedness numerical invariants in 1857 and Betti's proof in 1871 of the independence of "homology numbers" from the choice of basis.

### Surfaces

Cycles on a 2-sphere

$S^{2}$

Cycles on a torus

$T^{2}$

Cycles on a Klein

bottle

$K^{2}$

Cycles on a hemispherical projective plane

$P^{2}$

On the ordinary sphere $S^{2}$ , the curve *b* in the diagram can be shrunk to the pole, and even the equatorial great circle *a* can be shrunk in the same way. The Jordan curve theorem shows that any closed curve such as *c* can be similarly shrunk to a point. This implies that $S^{2}$ has trivial fundamental group, so as a consequence, it also has trivial first homology group.

The torus $T^{2}$ has closed curves which cannot be continuously deformed into each other, for example in the diagram none of the cycles *a*, *b* or *c* can be deformed into one another. In particular, cycles *a* and *b* cannot be shrunk to a point whereas cycle *c* can.

If the torus surface is cut along both *a* and *b*, it can be opened out and flattened into a rectangle or, more conveniently, a square. One opposite pair of sides represents the cut along *a*, and the other opposite pair represents the cut along *b*.

The edges of the square may then be glued back together in different ways. The square can be twisted to allow edges to meet in the opposite direction, as shown by the arrows in the diagram. The various ways of gluing the sides yield just four topologically distinct surfaces:

$K^{2}$ is the Klein bottle, which is a torus with a twist in it (In the square diagram, the twist can be seen as the reversal of the bottom arrow). It is a theorem that the re-glued surface must self-intersect (when immersed in Euclidean 3-space). Like the torus, cycles *a* and *b* cannot be shrunk while *c* can be. But unlike the torus, following *b* forwards right round and back reverses left and right, because *b* happens to cross over the twist given to one join. If an equidistant cut on one side of *b* is made, it returns on the other side and goes round the surface a second time before returning to its starting point, cutting out a twisted Möbius strip. Because local left and right can be arbitrarily re-oriented in this way, the surface as a whole is said to be non-orientable.

The projective plane $P^{2}$ has both joins twisted. The uncut form, generally represented as the Boy surface, is visually complex, so a hemispherical embedding is shown in the diagram, in which antipodal points around the rim such as *A* and *A′* are identified as the same point. Again, *a* is non-shrinkable while *c* is. If *b* were only wound once, it would also be non-shrinkable and reverse left and right. However it is wound a second time, which swaps right and left back again; it can be shrunk to a point and is homologous to *c*.

Cycles can be joined or added together, as *a* and *b* on the torus were when it was cut open and flattened down. In the Klein bottle diagram, *a* goes round one way and −*a* goes round the opposite way. If *a* is thought of as a cut, then −*a* can be thought of as a gluing operation. Making a cut and then re-gluing it does not change the surface, so *a* + (−*a*) = 0.

But now consider two *a*-cycles. Since the Klein bottle is nonorientable, you can transport one of them all the way round the bottle (along the *b*-cycle), and it will come back as −*a*. This is because the Klein bottle is made from a cylinder, whose *a*-cycle ends are glued together with opposite orientations. Hence 2*a* = *a* + *a* = *a* + (−*a*) = 0. This phenomenon is called torsion. Similarly, in the projective plane, following the unshrinkable cycle *b* round twice remarkably creates a trivial cycle which *can* be shrunk to a point; that is, *b* + *b* = 0. Because *b* must be followed around twice to achieve a zero cycle, the surface is said to have a torsion coefficient of 2. However, following a *b*-cycle around twice in the Klein bottle gives simply *b* + *b* = 2*b*, since this cycle lives in a torsion-free homology class. This corresponds to the fact that in the fundamental polygon of the Klein bottle, only one pair of sides is glued with a twist, whereas in the projective plane both sides are twisted.

A square is a contractible topological space, which implies that it has trivial homology. Consequently, additional cuts disconnect it. The square is not the only shape in the plane that can be glued into a surface. Gluing opposite sides of an octagon, for example, produces a surface with two holes. In fact, all closed surfaces can be produced by gluing the sides of some polygon and all even-sided polygons (2*n*-gons) can be glued to make different manifolds. Conversely, a closed surface with *n* non-zero classes can be cut into a 2*n*-gon. Variations are also possible, for example a hexagon may also be glued to form a torus.

The first recognisable theory of homology was published by Henri Poincaré in his seminal paper "Analysis situs", *J. Ecole polytech.* (2) **1**. 1–121 (1895). The paper introduced homology classes and relations. The possible configurations of orientable cycles are classified by the Betti numbers of the manifold (Betti numbers are a refinement of the Euler characteristic). Classifying the non-orientable cycles requires additional information about torsion coefficients.

The complete classification of 1- and 2-manifolds is given in the table.

| Manifold | Euler no., χ | Orientability | Betti numbers | Torsion coefficient (1-dimensional) |   |   |   |
|---|---|---|---|---|---|---|---|
| Symbol | Name | *b*0 | *b*1 | *b*2 |   |   |   |
| $S^{1}$ | Circle (1-manifold) | 0 | Orientable | 1 | 1 | —N/a | —N/a |
| $S^{2}$ | Sphere | 2 | Orientable | 1 | 0 | 1 | None |
| $T^{2}$ | Torus | 0 | Orientable | 1 | 2 | 1 | None |
| $P^{2}$ | Projective plane | 1 | Non-orientable | 1 | 0 | 0 | 2 |
| $K^{2}$ | Klein bottle | 0 | Non-orientable | 1 | 1 | 0 | 2 |
|   | 2-holed torus | −2 | Orientable | 1 | 4 | 1 | None |
|   | *g*-holed torus (*g* is the genus) | 2 − 2*g* | Orientable | 1 | 2*g* | 1 | None |
|   | Sphere with *c* cross-caps | 2 − *c* | Non-orientable | 1 | *c* − 1 | 0 | 2 |
|   | 2-Manifold with *g* holes and *c* cross-caps (*c* > 0) | 2 − (2*g* + *c*) | Non-orientable | 1 | (2*g* + *c*) − 1 | 0 | 2 |

Notes

1. For a non-orientable surface, a hole is equivalent to two cross-caps.
2. Any closed 2-manifold can be realised as the connected sum of *g* tori and *c* projective planes, where the 2-sphere $S^{2}$ is regarded as the empty connected sum. Homology is preserved by the operation of connected sum.

In a search for increased rigour, Poincaré went on to develop the simplicial homology of a triangulated manifold and to create what is now called a simplicial chain complex. Chain complexes (since greatly generalized) form the basis for most modern treatments of homology.

Emmy Noether and, independently, Leopold Vietoris and Walther Mayer further developed the theory of algebraic homology groups in the period 1925–28. The new combinatorial topology formally treated topological classes as abelian groups. Homology groups are finitely generated abelian groups, and homology classes are elements of these groups. The Betti numbers of the manifold are the rank of the free part of the homology group, and in the special case of surfaces, the torsion part of the homology group only occurs for non-orientable cycles.

The subsequent spread of homology groups brought a change of terminology and viewpoint from "combinatorial topology" to "algebraic topology". Algebraic homology remains the primary method of classifying manifolds.
