---
title: "De Rham cohomology"
source: https://en.wikipedia.org/wiki/De_Rham_cohomology
domain: differential-topology
license: CC-BY-SA-4.0
tags: differential topology, smooth manifold, morse theory, de rham cohomology
fetched: 2026-07-02
---

# De Rham cohomology

In mathematics, **de Rham cohomology** (named after Georges de Rham) is a tool belonging both to algebraic topology and to differential topology, capable of expressing basic topological information about smooth manifolds in a form particularly adapted to computation and the concrete representation of cohomology classes. It is a cohomology theory based on the existence of differential forms with prescribed properties.

On any smooth manifold, every exact form is closed, but the converse may fail to hold. Roughly speaking, this failure is related to the possible existence of "holes" in the manifold, and the **de Rham cohomology groups** comprise a set of topological invariants of smooth manifolds that precisely quantify this relationship.

> The integration on forms concept is of fundamental importance in differential topology, geometry, and physics, and also yields one of the most important examples of
> 
> cohomology
> 
> , namely
> 
> de Rham cohomology
> 
> , which (roughly speaking) measures precisely the extent to which the
> 
> fundamental theorem of calculus
> 
> fails in higher dimensions and on general manifolds.
> 
> —
> 
> Terence Tao
> 
> ,
> 
> Differential Forms and Integration

## Definition

The **de Rham complex** is the cochain complex of differential forms on some smooth manifold M , with the exterior derivative as the differential:

$0\to \Omega ^{0}(M)\xrightarrow {d} \Omega ^{1}(M)\xrightarrow {d} \Omega ^{2}(M)\xrightarrow {d} \Omega ^{3}(M)\to \cdots ,$

where $\Omega ^{0}(M)$ is the space of smooth functions on M , $\Omega ^{1}(M)$ is the space of 1-forms, and so forth. Forms that are the image of other forms under the exterior derivative, plus the constant 0 function in $\Omega ^{0}(M)$ , are called **exact** and forms whose exterior derivative is 0 are called **closed** (see *Closed and exact differential forms*); the relationship $d^{2}=0$ then says that exact forms are closed.

In contrast, closed forms are not necessarily exact. An illustrative case is a circle as a manifold, and the 1 -form corresponding to the derivative of angle from a reference point at its centre, typically written as ${\text{d}}\theta$ (described at *Closed and exact differential forms*). There is no function $\theta$ defined on the whole circle such that ${\text{d}}\theta$ is its derivative; the increase of $2\pi$ in going once around the circle in the positive direction implies a multivalued function $\theta$ . Removing one point of the circle obviates this, at the same time changing the topology of the manifold.

One prominent example when all closed forms are exact is when the underlying space is contractible to a point or, more generally, if it is simply connected (no-holes condition). In this case the exterior derivative d restricted to closed forms has a local inverse called a homotopy operator. Since it is also nilpotent, it forms a dual chain complex with the arrows reversed compared to the de Rham complex. This is the situation described in the Poincaré lemma.

The idea behind de Rham cohomology is to define equivalence classes of closed forms on a manifold. One classifies two closed forms $\alpha ,\beta \in \Omega ^{k}(M)$ as **cohomologous** if they differ by an exact form, that is, if $\alpha -\beta$ is exact. This classification induces an equivalence relation on the space of closed forms in $\Omega ^{k}(M)$ . One then defines the k -th **de Rham cohomology group** $H_{\mathrm {dR} }^{k}(M)$ to be the set of equivalence classes, that is, the set of closed forms in $\Omega ^{k}(M)$ modulo the exact forms.

Note that, for any manifold M composed of m disconnected components, each of which is connected, we have that

$H_{\mathrm {dR} }^{0}(M)\cong \mathbb {R} ^{m}.$

This follows from the fact that any smooth function on M with zero derivative everywhere is separately constant on each of the connected components of M .

## De Rham cohomology computed

One may often find the general de Rham cohomologies of a manifold using the above fact about the zero cohomology and a Mayer–Vietoris sequence. Another useful fact is that the de Rham cohomology is a homotopy invariant. While the computation is not given, the following are the computed de Rham cohomologies for some common topological objects:

### The *n*-sphere

For the n-sphere, $S^{n}$ , and also when taken together with a product of open intervals, we have the following. Let $n>0$ , $m\geq 0$ , and I be an open real interval. Then

$H_{\mathrm {dR} }^{k}(S^{n}\times I^{m})\simeq {\begin{cases}\mathbb {R} &k=0{\text{ or }}k=n,\\0&k\neq 0{\text{ and }}k\neq n.\end{cases}}$

### The *n*-torus

The n -torus is the Cartesian product: $T^{n}=\underbrace {S^{1}\times \cdots \times S^{1}} _{n}$ . Similarly, allowing $n\geq 1$ here, we obtain

$H_{\mathrm {dR} }^{k}(T^{n})\simeq \mathbb {R} ^{n \choose k}.$

We can also find explicit generators for the de Rham cohomology of the torus directly using differential forms. Given a quotient manifold $\pi :X\to X/G$ and a differential form $\omega \in \Omega ^{k}(X)$ we can say that $\omega$ is G **-invariant** if given any diffeomorphism induced by G , $\cdot g:X\to X$ we have $(\cdot g)^{*}(\omega )=\omega$ . In particular, the pullback of any form on $X/G$ is G -invariant. Also, the pullback is an injective morphism. In our case of $\mathbb {R} ^{n}/\mathbb {Z} ^{n}$ the differential forms $dx_{i}$ are $\mathbb {Z} ^{n}$ -invariant since $d(x_{i}+k)=dx_{i}$ . But, notice that $x_{i}+\alpha$ for $\alpha \in \mathbb {R}$ is not an invariant 0 -form. This with injectivity implies that

$[dx_{i}]\in H_{dR}^{1}(T^{n})$

Since the cohomology ring of a torus is generated by $H^{1}$ , taking the exterior products of these forms gives all of the explicit representatives for the de Rham cohomology of a torus.

### Punctured Euclidean space

Punctured Euclidean space is simply $\mathbb {R} ^{n}$ with the origin removed.

$H_{\text{dR}}^{k}(\mathbb {R} ^{n}\setminus \{0\})\cong {\begin{cases}\mathbb {R} ^{2}&n=1,k=0\\\mathbb {R} &n>1,k=0,n-1\\0&{\text{otherwise}}\end{cases}}.$

### The Möbius strip

We may deduce from the fact that the Möbius strip, M , can be deformation retracted to the 1 -sphere (i.e. the real unit circle), that:

$H_{\mathrm {dR} }^{k}(M)\simeq H_{\mathrm {dR} }^{k}(S^{1}).$

## De Rham theorem

Stokes' theorem is an expression of duality between de Rham cohomology and the homology of chains. It says that the pairing of differential forms and chains, via integration, gives a homomorphism from de Rham cohomology $H_{\mathrm {dR} }^{k}(M)$ to singular cohomology groups $H^{k}(M;\mathbb {R} ).$ de Rham's theorem, proved by Georges de Rham in 1931, states that for a smooth manifold M , this map is in fact an isomorphism.

More precisely, consider the map

$I:H_{\mathrm {dR} }^{p}(M)\to H^{p}(M;\mathbb {R} ),$

defined as follows: for any $[\omega ]\in H_{\mathrm {dR} }^{p}(M)$ , let $I(\omega )$ be the element of ${\text{Hom}}(H_{p}(M),\mathbb {R} )\simeq H^{p}(M;\mathbb {R} )$ that acts as follows:

$H_{p}(M)\ni [c]\longmapsto \int _{c}\omega .$

The theorem of de Rham asserts that this is an isomorphism between de Rham cohomology and singular cohomology.

The exterior product endows the direct sum of these groups with a ring structure. A further result of the theorem is that the two cohomology rings are isomorphic (as graded rings), where the analogous product on singular cohomology is the cup product.

## Sheaf-theoretic de Rham isomorphism

For any smooth manifold M , let ${\textstyle {\underline {\mathbb {R} }}}$ be the constant sheaf on M associated to the abelian group ${\textstyle \mathbb {R} }$ ; in other words, ${\textstyle {\underline {\mathbb {R} }}}$ is the sheaf of locally constant real-valued functions on M . Then we have a natural isomorphism

$H_{\mathrm {dR} }^{*}(M)\cong H^{*}(M,{\underline {\mathbb {R} }})$

between the de Rham cohomology and the sheaf cohomology of ${\textstyle {\underline {\mathbb {R} }}}$ . (Note that this shows that de Rham cohomology may also be computed in terms of Čech cohomology; indeed, since every smooth manifold is paracompact Hausdorff we have that sheaf cohomology is isomorphic to the Čech cohomology ${\textstyle {\check {H}}^{*}({\mathcal {U}},{\underline {\mathbb {R} }})}$ for any good cover ${\textstyle {\mathcal {U}}}$ of M .)

### Proof

The standard proof proceeds by showing that the de Rham complex, when viewed as a complex of sheaves, is an acyclic resolution of ${\textstyle {\underline {\mathbb {R} }}}$ . In more detail, let m be the dimension of M and let ${\textstyle \Omega ^{k}}$ denote the sheaf of germs of k -forms on M (with ${\textstyle \Omega ^{0}}$ the sheaf of ${\textstyle C^{\infty }}$ functions on M ). By the Poincaré lemma, the following sequence of sheaves is exact (in the abelian category of sheaves):

$0\to {\underline {\mathbb {R} }}\to \Omega ^{0}\xrightarrow {d_{0}} \Omega ^{1}\xrightarrow {d_{1}} \Omega ^{2}\xrightarrow {d_{2}} \cdots \xrightarrow {d_{m-1}} \Omega ^{m}\to 0.$

This long exact sequence now breaks up into short exact sequences of sheaves

$0\to \operatorname {im} d_{k-1}\xrightarrow {\subset } \Omega ^{k}\xrightarrow {d_{k}} \operatorname {im} d_{k}\to 0,$

where by exactness we have isomorphisms ${\textstyle \operatorname {im} d_{k-1}\cong \ker d_{k}}$ for all k . Each of these induces a long exact sequence in cohomology. Since the sheaf ${\textstyle \Omega ^{0}}$ of ${\textstyle C^{\infty }}$ functions on M admits partitions of unity, any ${\textstyle \Omega ^{0}}$ -module is a fine sheaf; in particular, the sheaves ${\textstyle \Omega ^{k}}$ are all fine. Therefore, the sheaf cohomology groups ${\textstyle H^{i}(M,\Omega ^{k})}$ vanish for ${\textstyle i>0}$ since all fine sheaves on paracompact spaces are acyclic. So the long exact cohomology sequences themselves ultimately separate into a chain of isomorphisms. At one end of the chain is the sheaf cohomology of ${\textstyle {\underline {\mathbb {R} }}}$ and at the other lies the de Rham cohomology.

The de Rham cohomology has inspired many mathematical ideas, including Dolbeault cohomology, Hodge theory, and the Atiyah–Singer index theorem. However, even in more classical contexts, the theorem has inspired a number of developments. Firstly, the Hodge theory proves that there is an isomorphism between the cohomology consisting of harmonic forms and the de Rham cohomology consisting of closed forms modulo exact forms. This relies on an appropriate definition of harmonic forms and of the Hodge theorem. For further details see Hodge theory.

### Harmonic forms

If M is a compact Riemannian manifold, then each equivalence class in $H_{\mathrm {dR} }^{k}(M)$ contains exactly one harmonic form. That is, every member $\omega$ of a given equivalence class of closed forms can be written as

$\omega =\alpha +\gamma$

where $\alpha$ is exact and $\gamma$ is harmonic: $\Delta \gamma =0$ .

Any harmonic function on a compact connected Riemannian manifold is a constant. Thus, this particular representative element can be understood to be an extremum (a minimum) of all cohomologously equivalent forms on the manifold. For example, on a 2 -torus, one may envision a constant 1 -form as one where all of the "hair" is combed neatly in the same direction (and all of the "hair" having the same length). In this case, there are two cohomologically distinct combings; all of the others are linear combinations. In particular, this implies that the 1st Betti number of a 2 -torus is two. More generally, on an n -dimensional torus $T^{n}$ , one can consider the various combings of k -forms on the torus. There are n choose k such combings that can be used to form the basis vectors for $H_{\text{dR}}^{k}(T^{n})$ ; the k -th Betti number for the de Rham cohomology group for the n -torus is thus n choose k .

More precisely, for a differential manifold M , one may equip it with some auxiliary Riemannian metric. Then the Laplacian $\Delta$ is defined by

$\Delta =d\delta +\delta d$

with d the exterior derivative and $\delta$ the codifferential. The Laplacian is a homogeneous (in grading) linear differential operator acting upon the exterior algebra of differential forms: we can look at its action on each component of degree k separately.

If M is compact and oriented, the dimension of the kernel of the Laplacian acting upon the space of k-forms is then equal (by Hodge theory) to that of the de Rham cohomology group in degree k : the Laplacian picks out a unique **harmonic form** in each cohomology class of closed forms. In particular, the space of all harmonic k -forms on M is isomorphic to $H^{k}(M;\mathbb {R} )$ . The dimension of each such space is finite, and is given by the k -th Betti number.

### Hodge decomposition

Let M be a compact oriented Riemannian manifold. The *Hodge decomposition* states that any k -form on M uniquely splits into the sum of three *L*2 components:

$\omega =\alpha +\beta +\gamma ,$

where $\alpha$ is exact, $\beta$ is co-exact, and $\gamma$ is harmonic.

One says that a form $\beta$ is co-closed if $\delta \beta =0$ and co-exact if $\beta =\delta \eta$ for some form $\eta$ , and that $\gamma$ is harmonic if the Laplacian is zero, $\Delta \gamma =0$ . This follows by noting that exact and co-exact forms are orthogonal; the orthogonal complement then consists of forms that are both closed and co-closed: that is, of harmonic forms. Here, orthogonality is defined with respect to the *L*2 inner product on $\Omega ^{k}(M)$ :

$(\alpha ,\beta )=\int _{M}\alpha \wedge {\star \beta }.$

By use of Sobolev spaces or distributions, the decomposition can be extended for example to a complete (oriented or not) Riemannian manifold.
