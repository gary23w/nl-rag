---
title: "Homotopy"
source: https://en.wikipedia.org/wiki/Homotopy
domain: topology
license: CC-BY-SA-4.0
tags: point-set topology, topological space, continuous function, compact space
fetched: 2026-07-02
---

# Homotopy

In topology, two continuous functions from one topological space to another are called **homotopic** (from Ancient Greek: ὁμός *homós* 'same, similar' and τόπος *tópos* 'place') if one can be "continuously deformed" into the other, such a deformation being called a **homotopy** (/həˈmɒtəpiː/ *hə-MOT-ə-pee*; /ˈhoʊmoʊˌtoʊpiː/ *HOH-moh-toh-pee*) between the two functions. A notable use of homotopy is the definition of homotopy groups and cohomotopy groups, important invariants in algebraic topology.

In practice, there are technical difficulties in using homotopies with certain spaces. Algebraic topologists work with compactly generated spaces, CW complexes, or spectra.

## Formal definition

Formally, a homotopy between two continuous functions *f* and *g* from a topological space *X* to a topological space *Y* is defined to be a continuous function $H:X\times [0,1]\to Y$ from the product of the space *X* with the unit interval [0, 1] to *Y* such that $H(x,0)=f(x)$ and $H(x,1)=g(x)$ for all $x\in X$ .

If we think of the second parameter of *H* as time, then *H* describes a *continuous deformation* of *f* into *g*: at time 0, we have the function *f*, and at time 1, we have the function *g*. We can also think of the second parameter as a "slider control" that allows us to smoothly transition from *f* to *g* as the slider moves from 0 to 1, and vice versa.

An alternative notation is to say that a homotopy between two continuous functions $f,g:X\to Y$ is a family of continuous functions $h_{t}:X\to Y$ for $t\in [0,1]$ such that $h_{0}=f$ and $h_{1}=g$ , and the map $(x,t)\mapsto h_{t}(x)$ is continuous from $X\times [0,1]$ to Y . The two versions coincide by setting $h_{t}(x)=H(x,t)$ . It is not sufficient to require each map $h_{t}(x)$ to be continuous.

The animation that is looped above right provides an example of a homotopy between two embeddings, *f* and *g*, of the torus into *R*3. *X* is the torus, *Y* is *R*3, *f* is some continuous function from the torus to *R*3 that takes the torus to the embedded surface-of-a-doughnut shape with which the animation starts; *g* is some continuous function that takes the torus to the embedded surface-of-a-coffee-mug shape. The animation shows the image of *h**t*(X) as a function of the parameter *t*, where *t* varies with time from 0 to 1 over each cycle of the animation loop. It pauses, then shows the image as *t* varies back from 1 to 0, pauses, and repeats this cycle.

### Properties

Continuous functions *f* and *g* are said to be homotopic if and only if there is a homotopy *H* taking *f* to *g* as described above. Being homotopic is an equivalence relation on the set of all continuous functions from *X* to *Y*. This homotopy relation is compatible with function composition in the following sense: if *f*1, *g*1 : *X* → *Y* are homotopic, and *f*2, *g*2 : *Y* → *Z* are homotopic, then their compositions *f*2 ∘ *f*1 and *g*2 ∘ *g*1 : *X* → *Z* are also homotopic.

## Examples

- If $f,g:\mathbb {R} \to \mathbb {R} ^{2}$ are given by $f(x):=\left(x,x^{3}\right)$ and $g(x)=\left(x,e^{x}\right)$ , then the map $H:\mathbb {R} \times [0,1]\to \mathbb {R} ^{2}$ given by $H(x,t)=\left(x,(1-t)x^{3}+te^{x}\right)$ is a homotopy between them.
- More generally, if $C\subseteq \mathbb {R} ^{n}$ is a convex subset of Euclidean space and $f,g:[0,1]\to C$ are paths with the same endpoints, then there is a **linear homotopy** (or **straight-line homotopy**) given by ${\begin{aligned}H:[0,1]\times [0,1]&\longrightarrow C\\(s,t)&\longmapsto (1-t)f(s)+tg(s).\end{aligned}}$
- Let $\operatorname {id} _{B^{n}}:B^{n}\to B^{n}$ be the identity function on the unit *n*-disk; i.e. the set $B^{n}:=\left\{x\in \mathbb {R} ^{n}:\|x\|\leq 1\right\}$ . Let $c_{\vec {0}}:B^{n}\to B^{n}$ be the constant function $c_{\vec {0}}(x):={\vec {0}}$ which sends every point to the origin. Then the following is a homotopy between them: ${\begin{aligned}H:B^{n}\times [0,1]&\longrightarrow B^{n}\\(x,t)&\longmapsto (1-t)x.\end{aligned}}$

## Homotopy equivalence

Given two topological spaces *X* and *Y*, a **homotopy equivalence** between *X* and *Y* is a pair of continuous maps *f* : *X* → *Y* and *g* : *Y* → *X*, such that *g* ∘ *f* is homotopic to the identity map id*X* and *f* ∘ *g* is homotopic to id*Y*. If such a pair exists, then *X* and *Y* are said to be **homotopy equivalent**, or of the same **homotopy type**. This relation of homotopy equivalence is often denoted $\simeq$ . Intuitively, two spaces *X* and *Y* are homotopy equivalent if they can be transformed into one another by bending, shrinking and expanding operations. Spaces that are homotopy equivalent to a point are called contractible.

### Homotopy equivalence vs. homeomorphism

A homeomorphism is a special case of a homotopy equivalence, in which *g* ∘ *f* is equal to the identity map id*X* (not only homotopic to it), and *f* ∘ *g* is equal to id*Y*. Therefore, if X and Y are homeomorphic, then they are homotopy equivalent, but the opposite is not true. Some examples:

- A solid disk is homotopy equivalent to a single point, since you can deform the disk along radial lines continuously to a single point; however, they are not homeomorphic, since there is no bijection between them (since one is an infinite set, while the other is finite).
- The Möbius strip and an untwisted (closed) strip are homotopy equivalent, since you can deform both strips continuously to a circle. But they are not homeomorphic.

### Examples

- The first example of a homotopy equivalence is $\mathbb {R} ^{n}$ with a point, denoted $\mathbb {R} ^{n}\simeq \{0\}$ . The part that needs to be checked is the existence of a homotopy $H:I\times \mathbb {R} ^{n}\to \mathbb {R} ^{n}$ between $\operatorname {id} _{\mathbb {R} ^{n}}$ and $p_{0}$ , the projection of $\mathbb {R} ^{n}$ onto the origin. This can be described as $H(t,\cdot )=t\cdot p_{0}+(1-t)\cdot \operatorname {id} _{\mathbb {R} ^{n}}$ .
- There is a homotopy equivalence between $S^{1}$ (the 1-sphere) and $\mathbb {R} ^{2}-\{0\}$ .
  - More generally, $\mathbb {R} ^{n}-\{0\}\simeq S^{n-1}$ .
- Any fiber bundle $\pi :E\to B$ with fibers $F_{b}$ homotopy equivalent to a point has homotopy-equivalent total and base spaces. This generalizes the previous two examples since $\pi :\mathbb {R} ^{n}-\{0\}\to S^{n-1}$ is a fiber bundle with fiber $\mathbb {R} _{>0}$ .
- Every vector bundle is a fiber bundle with a fiber homotopy equivalent to a point.
- $\mathbb {R} ^{n}-\mathbb {R} ^{k}\simeq S^{n-k-1}$ for any $0\leq k<n$ , by writing $\mathbb {R} ^{n}-\mathbb {R} ^{k}$ as the total space of the fiber bundle $\mathbb {R} ^{k}\times (\mathbb {R} ^{n-k}-\{0\})\to (\mathbb {R} ^{n-k}-\{0\})$ , then applying the homotopy equivalences above.
- If a subcomplex A of a CW complex X is contractible, then the quotient space $X/A$ is homotopy equivalent to X .
- A deformation retraction is a homotopy equivalence.

### Null-homotopy

A function f is said to be **null-homotopic** if it is homotopic to a constant function. (The homotopy from f to a constant function is then sometimes called a **null-homotopy**.) For example, a map f from the unit circle $S^{1}$ to any space X is null-homotopic precisely when it can be continuously extended to a map from the unit disk $D^{2}$ to X that agrees with f on the boundary.

It follows from these definitions that a space X is contractible if and only if the identity map from X to itself—which is always a homotopy equivalence—is null-homotopic.

## Invariance

Homotopy equivalence is important because in algebraic topology many concepts are **homotopy invariant**, that is, they respect the relation of homotopy equivalence. For example, if *X* and *Y* are homotopy equivalent spaces, then:

- *X* is path-connected if and only if *Y* is.
- *X* is simply connected if and only if *Y* is.
- The (singular) homology and cohomology groups of *X* and *Y* are isomorphic.
- If *X* and *Y* are path-connected, then the fundamental groups of *X* and *Y* are isomorphic, and so are the higher homotopy groups. (Without the path-connectedness assumption, one has π1(*X*, *x*0) isomorphic to π1(*Y*, *f*(*x*0)) where *f* : *X* → *Y* is a homotopy equivalence and *x*0 ∈ *X*.)

An example of an algebraic invariant of topological spaces which is not homotopy invariant is compactly supported homology (which is, roughly speaking, the homology of the compactification, and compactification is not homotopy invariant).

## Variants

### Relative homotopy

In order to define the fundamental group, one needs the notion of **homotopy relative to a subspace**. These are homotopies which keep the elements of the subspace fixed. Formally: if *f* and *g* are continuous maps from *X* to *Y* and *K* is a subset of *X*, then we say that *f* and *g* are homotopic relative to *K* if there exists a homotopy *H* : *X* × [0, 1] → *Y* between *f* and *g* such that *H*(*k*, *t*) = *f*(*k*) = *g*(*k*) for all *k* ∈ *K* and *t* ∈ [0, 1]. Also, if *g* is a retraction from *X* to *K* and *f* is the identity map, this is known as a strong deformation retract of *X* to *K*. When *K* is a point, the term **pointed homotopy** is used.

### Isotopy

The

unknot

is not equivalent to the

trefoil knot

since one cannot be deformed into the other through a continuous path of homeomorphisms of the ambient space. Thus, they are not ambient-isotopic.

When two given continuous functions *f* and *g* from the topological space *X* to the topological space *Y* are embeddings, one can ask whether they can be connected 'through embeddings'. This gives rise to the concept of **isotopy**, which is a homotopy, *H*, in the notation used before, such that for each fixed *t*, *H*(*x*, *t*) gives an embedding.

A related, but separate, concept is that of ambient isotopy.

Requiring that two embeddings be isotopic is a stronger requirement than that they be homotopic. For example, the map from the interval [−1, 1] into the real numbers defined by *f*(*x*) = −*x* is *not* isotopic to the identity *g*(*x*) = *x*. Any homotopy from *f* to the identity would have to exchange the endpoints, which would mean that they would have to 'pass through' each other. Moreover, *f* has changed the orientation of the interval and *g* has not, which is impossible under an isotopy. However, the maps are homotopic; one homotopy from *f* to the identity is *H*: [−1, 1] × [0, 1] → [−1, 1] given by *H*(*x*, *y*) = 2*yx* − *x*.

Two homeomorphisms (which are special cases of embeddings) of the unit ball which agree on the boundary can be shown to be isotopic using Alexander's trick. For this reason, the map of the unit disc in $\mathbb {R} ^{2}$ defined by *f*(*x*, *y*) = (−*x*, −*y*) is isotopic to a 180-degree rotation around the origin, and so the identity map and *f* are isotopic because they can be connected by rotations.

In geometric topology—for example, in knot theory—the idea of isotopy is used to construct equivalence relations. For example, when should two knots be considered the same? We take two knots, *K*1 and *K*2, in three-dimensional space. A knot is an embedding of a one-dimensional space, the "loop of string" (or the circle), into this space, and this embedding gives a homeomorphism between the circle and its image in the embedding space. One may try to define knot equivalence based on isotopy instead of the more restricted property of ambient isotopy. That is, two knots are isotopic when there exists a continuous function starting at *t* = 0 giving the *K*1 embedding, ending at *t* = 1 giving the *K*2 embedding, with all intermediate values corresponding to embeddings. However, this definition would make every knot equivalent to the unknot, as the knotted portions can be "contracted" down to a straight line. The problem is that, while continuous, this is not an injective function of the Euclidean space that the knot is embedded in. An ambient isotopy, studied in this context, is an isotopy of the larger space, considered in light of its action on the embedded submanifold. Knots *K*1 and *K*2 are considered equivalent when there is a continuous [0, 1]-indexed family of maps which moves *K*1 to *K*2 via homeomorphisms of the Euclidean space.

Similar language is used for the equivalent concept in contexts where one has a stronger notion of equivalence. For example, a path between two smooth embeddings is a **smooth isotopy**.

### Timelike homotopy

On a Lorentzian manifold, certain curves are distinguished as timelike (representing something that only goes forwards, not backwards, in time, in every local frame). A timelike homotopy between two timelike curves is a homotopy such that the curve remains timelike during the continuous transformation from one curve to another. No closed timelike curve (CTC) on a Lorentzian manifold is timelike homotopic to a point (that is, null timelike homotopic); such a manifold is therefore said to be multiply connected by timelike curves. A manifold such as the 3-sphere can be simply connected (by any type of curve), and yet be timelike multiply connected.

## Properties

### Lifting and extension properties

If we have a homotopy $H:X\times [0,1]\rightarrow Y$ and a cover $p:{\overline {Y}}\rightarrow Y$ and we are given a map ${\overline {h}}_{0}:X\rightarrow {\overline {Y}}$ such that $H_{0}=P\circ {\overline {h}}_{0}$ ( ${\overline {h}}_{0}$ is called a lift of $h_{0}$ ), then we can lift all H to a map ${\overline {H}}:X\times [0,1]\rightarrow {\overline {Y}}$ such that $p\circ {\overline {H}}=H$ . The homotopy lifting property is used to characterize fibrations.

Another useful property involving homotopy is the homotopy extension property, which characterizes the extension of a homotopy between two functions from a subset of some set to the set itself. It is useful when dealing with cofibrations.

### Groups

Since the relation of two functions $f,g\colon X\to Y$ being homotopic relative to a subspace is an equivalence relation, we can look at the equivalence classes of maps between a fixed *X* and *Y*. If we fix $X=[0,1]^{n}$ , the unit interval [0, 1] crossed with itself *n* times, and we take its boundary $\partial ([0,1]^{n})$ as a subspace, then the equivalence classes form a group, denoted $\pi _{n}(Y,y_{0})$ , where $y_{0}$ is in the image of the subspace $\partial ([0,1]^{n})$ .

We can define the action of one equivalence class on another, and so we get a group. These groups are called the homotopy groups. In the case $n=1$ , it is also called the fundamental group.

### Homotopy category

The idea of homotopy can be turned into a formal category of category theory. The **homotopy category** is the category whose objects are topological spaces, and whose morphisms are homotopy equivalence classes of continuous maps. Two topological spaces *X* and *Y* are isomorphic in this category if and only if they are homotopy equivalent. Then a functor on the category of topological spaces is homotopy invariant if it can be expressed as a functor on the homotopy category.

For example, homology groups are a *functorial* homotopy invariant: this means that if *f* and *g* from *X* to *Y* are homotopic, then the group homomorphisms induced by *f* and *g* on the level of homology groups are the same: H*n*(*f*) = H*n*(*g*) : H*n*(*X*) → H*n*(*Y*) for all *n*. Likewise, if *X* and *Y* are in addition path-connected, and the homotopy between *f* and *g* is pointed, then the group homomorphisms induced by *f* and *g* on the level of homotopy groups are also the same: π*n*(*f*) = π*n*(*g*) : π*n*(*X*) → π*n*(*Y*).

## Applications

Based on the concept of the homotopy, computation methods for algebraic and differential equations have been developed. The methods for algebraic equations include the homotopy continuation method and the continuation method (see numerical continuation). The methods for differential equations include the homotopy analysis method.

Homotopy theory can be used as a foundation for homology theory: one can represent a cohomology functor on a space *X* by mappings of *X* into an appropriate fixed space, up to homotopy equivalence. For example, for any abelian group *G*, and any based CW-complex *X*, the set $[X,K(G,n)]$ of based homotopy classes of based maps from *X* to the Eilenberg–MacLane space $K(G,n)$ is in natural bijection with the *n*-th singular cohomology group $H^{n}(X,G)$  of the space *X*. One says that the omega-spectrum of Eilenberg-MacLane spaces are representing spaces for singular cohomology with coefficients in *G*. Using this fact, homotopy classes between a CW complex and a multiply connected space can be calculated using cohomology as described by the Hopf–Whitney theorem.

Recently, homotopy theory is used to develop deep learning-based generative models like diffusion models and flow-based generative models. Perturbing the complex non-Gaussian states is a tough task. Using deep learning and homotopy, such complex states can be transformed to Gaussian state and mildly perturbed to get transformed back to perturbed complex states.
