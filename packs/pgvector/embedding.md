---
title: "Embedding"
source: https://en.wikipedia.org/wiki/Embedding
domain: pgvector
license: CC-BY-SA-4.0
tags: pgvector, postgres vector extension, vector similarity search, word embedding
fetched: 2026-07-02
---

# Embedding

In mathematics, an **embedding** (or **imbedding**) is one instance of some mathematical structure contained within another instance, such as a group that is a subgroup.

When some object X is said to be embedded in another object Y , the embedding is given by some injective and structure-preserving map $f:X\rightarrow Y$ . The precise meaning of "structure-preserving" depends on the kind of mathematical structure of which X and Y are instances. In the terminology of category theory, a structure-preserving map is called a morphism.

The fact that a map $f:X\rightarrow Y$ is an embedding is often indicated by the use of a "hooked arrow" (U+21AA ↪ RIGHTWARDS ARROW WITH HOOK); thus: $f:X\hookrightarrow Y.$ (On the other hand, this notation is sometimes reserved for inclusion maps.)

Given X and Y , several different embeddings of X in Y may be possible. In many cases of interest there is a standard (or "canonical") embedding, like those of the natural numbers in the integers, the integers in the rational numbers, the rational numbers in the real numbers, and the real numbers in the complex numbers. In such cases it is common to identify the domain X with its image $f(X)$ contained in Y , so that $X\subseteq Y$ .

## Topology and geometry

### General topology

In general topology, an embedding is a homeomorphism onto its image. More explicitly, an injective continuous map $f:X\to Y$ between topological spaces X and Y is a **topological embedding** if f yields a homeomorphism between X and $f(X)$ (where $f(X)$ carries the subspace topology inherited from Y ). Intuitively then, the embedding $f:X\to Y$ lets us treat X as a subspace of Y . Every embedding is injective and continuous. Every map that is injective, continuous and either open or closed is an embedding; however there are also embeddings that are neither open nor closed. The latter happens if the image $f(X)$ is neither an open set nor a closed set in Y .

For a given space Y , the existence of an embedding $X\to Y$ is a topological invariant of X . This allows two spaces to be distinguished if one is able to be embedded in a space while the other is not.

If the domain of a function $f:X\to Y$ is a topological space then the function is said to be *locally injective at a point* if there exists some neighborhood U of this point such that the restriction $f{\big \vert }_{U}:U\to Y$ is injective. It is called *locally injective* if it is locally injective around every point of its domain. Similarly, a *local (topological, resp. smooth) embedding* is a function for which every point in its domain has some neighborhood to which its restriction is a (topological, resp. smooth) embedding.

Every injective function is locally injective but not conversely. Local diffeomorphisms, local homeomorphisms, and smooth immersions are all locally injective functions that are not necessarily injective. The inverse function theorem gives a sufficient condition for a continuously differentiable function to be (among other things) locally injective. Every fiber of a locally injective function $f:X\to Y$ is necessarily a discrete subspace of its domain $X.$

### Differential topology

In differential topology: Let M and N be smooth manifolds and $f:M\to N$ be a smooth map. Then f is called an immersion if its derivative is everywhere injective. An **embedding**, or a **smooth embedding**, is defined to be an immersion that is an embedding in the topological sense mentioned above (i.e. homeomorphism onto its image).

In other words, the domain of an embedding is diffeomorphic to its image, and in particular the image of an embedding must be a submanifold. An immersion is precisely a **local embedding**, i.e. for any point $x\in M$ there is a neighborhood $x\in U\subset M$ such that $f:U\to N$ is an embedding.

When the domain manifold is compact, the notion of a smooth embedding is equivalent to that of an injective immersion.

An important case is $N=\mathbb {R} ^{n}$ . The interest here is in how large n must be for an embedding, in terms of the dimension m of M . The Whitney embedding theorem states that $n=2m$ is enough, and is the best possible linear bound. For example, the real projective space $\mathbb {R} \mathrm {P} ^{m}$ of dimension m , where m is a power of two, requires $n=2m$ for an embedding. However, this does not apply to immersions; for instance, $\mathbb {R} \mathrm {P} ^{2}$ can be immersed in $\mathbb {R} ^{3}$ as is explicitly shown by Boy's surface—which has self-intersections. The Roman surface fails to be an immersion as it contains cross-caps.

An embedding is **proper** if it behaves well with respect to boundaries: one requires the map $f:X\rightarrow Y$ to be such that

- $f(\partial X)=f(X)\cap \partial Y$ , and
- $f(X)$ is transverse to $\partial Y$ in any point of $f(\partial X)$ .

The first condition is equivalent to having $f(\partial X)\subseteq \partial Y$ and $f(X\setminus \partial X)\subseteq Y\setminus \partial Y$ . The second condition, roughly speaking, says that $f(X)$ is not tangent to the boundary of Y .

### Riemannian and pseudo-Riemannian geometry

In Riemannian geometry and pseudo-Riemannian geometry: Let $(M,g)$ and $(N,h)$ be Riemannian manifolds or more generally pseudo-Riemannian manifolds. An **isometric embedding** is a smooth embedding $f:M\rightarrow N$ that preserves the (pseudo-)metric in the sense that g is equal to the pullback of h by f , i.e. $g=f^{*}h$ . Explicitly, for any two tangent vectors $v,w\in T_{x}(M)$ we have

$g(v,w)=h(df(v),df(w)).$

Analogously, **isometric immersion** is an immersion between (pseudo)-Riemannian manifolds that preserves the (pseudo)-Riemannian metrics.

Equivalently, in Riemannian geometry, an isometric embedding (immersion) is a smooth embedding (immersion) that preserves length of curves (cf. Nash embedding theorem).

## Algebra

In general, for an algebraic category C , an embedding between two C -algebraic structures X and Y is a C -morphism $e:X\rightarrow Y$ that is injective.

### Field theory

In field theory, an **embedding** of a field E in a field F is a ring homomorphism $\sigma :E\rightarrow F$ .

The kernel of $\sigma$ is an ideal of E , which cannot be the whole field E , because of the condition $1=\sigma (1)=1$ . Furthermore, any field has as ideals only the zero ideal and the whole field itself (because if there is any non-zero field element in an ideal, it is invertible, showing the ideal is the whole field). Therefore, the kernel is 0 , so any embedding of fields is a monomorphism. Hence, E is isomorphic to the subfield $\sigma (E)$ of F . This justifies the name *embedding* for an arbitrary homomorphism of fields.

### Universal algebra and model theory

If $\sigma$ is a signature and $A,B$ are $\sigma$ -structures (also called $\sigma$ -algebras in universal algebra or models in model theory), then a map $h:A\to B$ is a $\sigma$ -embedding exactly if all of the following hold:

- h is injective,
- for every n -ary function symbol $f\in \sigma$ and $a_{1},\ldots ,a_{n}\in A^{n},$ we have $h(f^{A}(a_{1},\ldots ,a_{n}))=f^{B}(h(a_{1}),\ldots ,h(a_{n}))$ ,
- for every n -ary relation symbol $R\in \sigma$ and $a_{1},\ldots ,a_{n}\in A^{n},$ we have $A\models R(a_{1},\ldots ,a_{n})$ iff $B\models R(h(a_{1}),\ldots ,h(a_{n})).$

Here $A\models R(a_{1},\ldots ,a_{n})$ is a model theoretical notation equivalent to $(a_{1},\ldots ,a_{n})\in R^{A}$ . In model theory there is also a stronger notion of elementary embedding.

## Order theory and domain theory

In order theory, an embedding of partially ordered sets is a function F between partially ordered sets X and Y such that

$\forall x_{1},x_{2}\in X:x_{1}\leq x_{2}\iff F(x_{1})\leq F(x_{2}).$

Injectivity of F follows quickly from this definition. In domain theory, an additional requirement is that

$\forall y\in Y:\{x\mid F(x)\leq y\}$

is

directed

.

## Metric spaces

A mapping $\phi :X\to Y$ of metric spaces is called an *embedding* (with distortion $C>0$ ) if

$Ld_{X}(x,y)\leq d_{Y}(\phi (x),\phi (y))\leq CLd_{X}(x,y)$

for every $x,y\in X$ and some constant $L>0$ .

### Normed spaces

An important special case is that of normed spaces; in this case it is natural to consider linear embeddings.

One of the basic questions that can be asked about a finite-dimensional normed space $(X,\|\cdot \|)$ is, *what is the maximal dimension k such that the Hilbert space $\ell _{2}^{k}$ can be linearly embedded into X with constant distortion?*

The answer is given by Dvoretzky's theorem.

## Category theory

In category theory, there is no satisfactory and generally accepted definition of embeddings that is applicable in all categories. One would expect that all isomorphisms and all compositions of embeddings are embeddings, and that all embeddings are monomorphisms. Other typical requirements are: any extremal monomorphism is an embedding and embeddings are stable under pullbacks.

Ideally the class of all embedded subobjects of a given object, up to isomorphism, should also be small, and thus an ordered set. In this case, the category is said to be well powered with respect to the class of embeddings. This allows defining new local structures in the category (such as a closure operator).

In a concrete category, an **embedding** is a morphism $f:A\rightarrow B$ that is an injective function from the underlying set of A to the underlying set of B and is also an **initial morphism** in the following sense: If g is a function from the underlying set of an object C to the underlying set of A , and if its composition with f is a morphism $fg:C\rightarrow B$ , then g itself is a morphism.

A factorization system for a category also gives rise to a notion of embedding. If $(E,M)$ is a factorization system, then the morphisms in M may be regarded as the embeddings, especially when the category is well powered with respect to M . Concrete theories often have a factorization system in which M consists of the embeddings in the previous sense. This is the case of the majority of the examples given in this article.

As usual in category theory, there is a dual concept, known as quotient. All the preceding properties can be dualized.

An embedding can also refer to an embedding functor.
