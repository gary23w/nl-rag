---
title: "Isomorphism"
source: https://en.wikipedia.org/wiki/Isomorphism
domain: abstract-algebra
license: CC-BY-SA-4.0
tags: abstract algebra, algebraic structure, group homomorphism, quotient structure
fetched: 2026-07-02
---

# Isomorphism

The

group

of fifth

roots of unity

under multiplication is isomorphic to the group of rotations of the regular pentagon under composition.

In mathematics, an **isomorphism** is a structure-preserving mapping or morphism between two structures of the same type that can be reversed by an inverse mapping. Two mathematical structures are **isomorphic** if an isomorphism exists between them, and this is often denoted as ⁠ $A\cong B$ ⁠. The word is derived from Ancient Greek ἴσος*(*isos*)* 'equal' and μορφή*(*morphe*)* 'form, shape'.

The interest in isomorphisms lies in the fact that two isomorphic objects have the same properties (excluding further information such as additional structure or names of objects). Thus isomorphic structures cannot be distinguished from the point of view of structure only, and may often be identified. In mathematical jargon, one says that two objects are the same up to an isomorphism. A common example where isomorphic structures cannot be identified is when the structures are substructures of a larger one. For example, all subspaces of dimension one of a vector space are isomorphic and cannot be identified.

An automorphism is an isomorphism from a structure to itself. An isomorphism between two structures is a **canonical isomorphism** (a canonical map that is an isomorphism) if there is only one isomorphism between the two structures (as is the case for solutions of a universal property), or if the isomorphism is much more natural (in some sense) than other isomorphisms. For example, for every prime number p, all fields with p elements are canonically isomorphic, with a unique isomorphism. The isomorphism theorems provide canonical isomorphisms that are not unique.

The term *isomorphism* is mainly used for algebraic structures and categories. In the case of algebraic structures, mappings are called homomorphisms, and a homomorphism is an isomorphism if and only if it is bijective.

In various areas of mathematics, isomorphisms have received specialized names, depending on the type of structure under consideration. For example:

- An isometry is an isomorphism of metric spaces.
- A homeomorphism is an isomorphism of topological spaces.
- A diffeomorphism is an isomorphism of spaces equipped with a differential structure, typically differentiable manifolds.
- A symplectomorphism is an isomorphism of symplectic manifolds.
- A permutation is an automorphism of a set.
- In geometry, isomorphisms and automorphisms are often called transformations, for example rigid transformations, affine transformations, projective transformations.

Category theory, which can be viewed as a formalization of the concept of mapping between structures, provides a language that may be used to unify the approach to these different aspects of the basic idea.

## Examples

### Logarithm and exponential

Let $\mathbb {R} ^{+}$ be the multiplicative group of positive real numbers, and let $\mathbb {R}$ be the additive group of real numbers.

The logarithm function $\log :\mathbb {R} ^{+}\to \mathbb {R}$ satisfies $\log(xy)=\log x+\log y$ for all $x,y\in \mathbb {R} ^{+},$ so it is a group homomorphism. The exponential function $\exp :\mathbb {R} \to \mathbb {R} ^{+}$ satisfies $\exp(x+y)=(\exp x)(\exp y)$ for all $x,y\in \mathbb {R} ,$ so it too is a homomorphism.

The identities $\log \exp x=x$ and $\exp \log y=y$ show that $\log$ and $\exp$ are inverses of each other. So, $\exp :\mathbb {R} \to \mathbb {R} ^{+}\quad {\text{and}}\quad \log :\mathbb {R} ^{+}\to \mathbb {R}$ are group isomorphisms that are inverse of each other.

The $\log$ function is an isomorphism which translates multiplication of positive real numbers into addition of real numbers. This facility makes it possible to multiply real numbers using a ruler and a table of logarithms, or using a slide rule with a logarithmic scale.

### Integers modulo 6

Consider the ring $\mathbb {Z} _{6}$ of the integers from 0 to 5 with addition and multiplication modulo 6. Also consider the ring $\mathbb {Z} _{2}\times \mathbb {Z} _{3}$ of the ordered pairs where the first element is an integer modulo 2 and the second element is an integer modulo 3, with component-wise addition and multiplication modulo 2 and 3.

These rings are isomorphic under the following map: ${\begin{alignedat}{4}(0,0)&\mapsto 0\\(1,1)&\mapsto 1\\(0,2)&\mapsto 2\\(1,0)&\mapsto 3\\(0,1)&\mapsto 4\\(1,2)&\mapsto 5\\\end{alignedat}}$ or in general $(a,b)\mapsto (3a+4b)\mod 6.$

For example, $(1,1)+(1,0)=(0,1),$ which translates in the other system as $1+3=4.$

This is a special case of the Chinese remainder theorem which asserts that, if ⁠ m ⁠ and ⁠ n ⁠ are coprime integers, the ring of the integers modulo ⁠ $mn$ ⁠ is isomorphic to the direct product of the integers modulo ⁠ m ⁠ and the integers modulo ⁠ n ⁠.

### Relation-preserving isomorphism

If one object consists of a set *X* with a binary relation R and the other object consists of a set *Y* with a binary relation S then an isomorphism from *X* to *Y* is a bijective function $f:X\to Y$ such that: $\operatorname {S} (f(u),f(v))\quad {\text{ if and only if }}\quad \operatorname {R} (u,v)$

S is reflexive, irreflexive, symmetric, antisymmetric, asymmetric, transitive, total, trichotomous, a partial order, total order, well-order, strict weak order, total preorder (weak order), an equivalence relation, or a relation with any other special properties, if and only if R is.

For example, R is an ordering ≤ and S an ordering $\scriptstyle \sqsubseteq ,$ then an isomorphism from *X* to *Y* is a bijective function $f:X\to Y$ such that $f(u)\sqsubseteq f(v)\quad {\text{ if and only if }}\quad u\leq v.$ Such an isomorphism is called an *order isomorphism* or (less commonly) an *isotone isomorphism*.

If $X=Y,$ then this is a relation-preserving automorphism.

## Applications

In algebra, isomorphisms are defined for all algebraic structures. Some are more specifically studied; for example:

- Linear isomorphisms between vector spaces; they are specified by invertible matrices.
- Group isomorphisms between groups; the classification of isomorphism classes of finite groups is an open problem.
- Ring isomorphisms between rings.
- Field isomorphisms are the same as ring isomorphism between fields; their study, and more specifically the study of field automorphisms is an important part of Galois theory.

Just as the automorphisms of an algebraic structure form a group, the isomorphisms between two algebras sharing a common structure form a heap. Letting a particular isomorphism identify the two structures turns this heap into a group.

In mathematical analysis, the Laplace transform is an isomorphism mapping hard differential equations into easier algebraic equations.

In graph theory, an isomorphism between two graphs *G* and *H* is a bijective map *f* from the vertices of *G* to the vertices of *H* that preserves the "edge structure" in the sense that there is an edge from vertex *u* to vertex *v* in *G* if and only if there is an edge from $f(u)$ to $f(v)$ in *H*. See graph isomorphism.

In order theory, an isomorphism between two partially ordered sets *P* and *Q* is a bijective map f from *P* to *Q* that preserves the order structure in the sense that for any elements x and y of *P* we have x less than y in *P* if and only if $f(x)$ is less than $f(y)$ in *Q*. As an example, the set {1,2,3,6} of whole numbers ordered by the *is-a-factor-of* relation is isomorphic to the set {*O*, *A*, *B*, *AB*} of blood types ordered by the *can-donate-to* relation. See order isomorphism.

In mathematical analysis, an isomorphism between two Hilbert spaces is a bijection preserving addition, scalar multiplication, and inner product.

In early theories of logical atomism, the formal relationship between facts and true propositions was theorized by Bertrand Russell and Ludwig Wittgenstein to be isomorphic. An example of this line of thinking can be found in Russell's *Introduction to Mathematical Philosophy*.

In cybernetics, the good regulator theorem or Conant–Ashby theorem is stated as "Every good regulator of a system must be a model of that system". Whether regulated or self-regulating, an isomorphism is required between the regulator and processing parts of the system.

## Category theoretic view

In category theory, given a category *C*, an isomorphism is a morphism $f:a\to b$ that has an inverse morphism $g:b\to a,$ that is, $fg=1_{b}$ and $gf=1_{a}.$

Two categories C and D are isomorphic if there exist functors $F:C\to D$ and $G:D\to C$ which are mutually inverse to each other, that is, $FG=1_{D}$ (the identity functor on D) and $GF=1_{C}$ (the identity functor on C).

### Isomorphism vs. bijective morphism

In a concrete category (roughly, a category whose objects are sets (perhaps with extra structure) and whose morphisms are structure-preserving functions), such as the category of topological spaces or categories of algebraic objects (like the category of groups, the category of rings, and the category of modules), an isomorphism must be bijective on the underlying sets. In algebraic categories (specifically, categories of varieties in the sense of universal algebra), an isomorphism is the same as a homomorphism which is bijective on underlying sets. However, there are concrete categories in which bijective morphisms are not necessarily isomorphisms (such as the category of topological spaces).

## Isomorphism classes

Since a composition of isomorphisms is an isomorphism, the identity is an isomorphism, and the inverse of an isomorphism is an isomorphism, the relation that two mathematical objects are isomorphic is an equivalence relation. An equivalence class given by isomorphisms is commonly called an **isomorphism class**.

### Examples

Examples of isomorphism classes are plentiful in mathematics.

- Two sets are isomorphic if there is a bijection between them. The isomorphism class of a finite set can be identified with the non-negative integer representing the number of elements it contains.
- The isomorphism class of a finite-dimensional vector space can be identified with the non-negative integer representing its dimension.
- The classification of finite simple groups enumerates the isomorphism classes of all finite simple groups.
- The classification of closed surfaces enumerates the isomorphism classes of all connected closed surfaces.
- Ordinals intuitively correspond to isomorphism classes of well-ordered sets (though there are technical set-theoretic issues involved).
- There are three isomorphism classes of the planar subalgebras of M(2,**R**), the 2 x 2 real matrices.

However, there are circumstances in which the isomorphism class of an object conceals vital information about it.

- Given a mathematical structure, it is common that two substructures belong to the same isomorphism class. However, the way they are included in the whole structure can not be studied if they are identified. For example, in a finite-dimensional vector space, all subspaces of the same dimension are isomorphic, but must be distinguished to consider their intersection, sum, etc.
- In homotopy theory, the fundamental group of a space X at a point p , though technically denoted $\pi _{1}(X,p)$ to emphasize the dependence on the base point, is often written lazily as simply $\pi _{1}(X)$ if X is path connected. The reason for this is that the existence of a path between two points allows one to identify loops at one with loops at the other; however, unless $\pi _{1}(X,p)$ is abelian this isomorphism is non-unique. Furthermore, the classification of covering spaces makes strict reference to particular subgroups of $\pi _{1}(X,p)$ , specifically distinguishing between isomorphic but conjugate subgroups, and therefore amalgamating the elements of an isomorphism class into a single featureless object seriously decreases the level of detail provided by the theory.

## Relation to equality

Although there are cases where isomorphic objects can be considered equal, one must distinguish *equality* and *isomorphism*. Equality is when two objects are the same, and therefore everything that is true about one object is true about the other. On the other hand, isomorphisms are related to some structure, and two isomorphic objects share only the properties that are related to this structure.

For example, the sets $A=\left\{x\in \mathbb {Z} \mid x^{2}<2\right\}\quad {\text{ and }}\quad B=\{-1,0,1\}$ are *equal*; they are merely different representations—the first an intensional one (in set builder notation), and the second extensional (by explicit enumeration)—of the same subset of the integers. By contrast, the sets $\{4,5,6\}$ and $\{1,2,3\}$ are not *equal* since they do not have the same elements. They are isomorphic as sets, but there are many choices (in fact 6) of an isomorphism between them: one isomorphism is

${\text{4}}\mapsto 1,{\text{5}}\mapsto 2,{\text{6}}\mapsto 3,$

while another is

${\text{4}}\mapsto 3,{\text{5}}\mapsto 2,{\text{6}}\mapsto 1,$

and no one isomorphism is intrinsically better than any other.

Also, integers and even numbers are isomorphic as ordered sets and abelian groups (for addition), but cannot be considered equal sets, since one is a proper subset of the other.

On the other hand, when sets (or other mathematical objects) are specified only by their properties, one often considers two different concrete realizations to be equal and will use the equal sign = to identify them, even if the sets arising from these constructions contain elements that are not set-theoretically equal (or, in some cases, even comparable). This is generally the case for objects defined by universal properties. For example, the polynomial rings ⁠ $\mathbb {Z} [X,Y]$ ⁠, ⁠ $(\mathbb {Z} [X])[Y]$ ⁠, and ⁠ $(\mathbb {Z} [Y])[X]$ ⁠ are considered as equal, since they all satisfy the same universal property. As another example, the ring localizations $R_{f}$ , $R_{f^{2}}$ , and $R[X]/(1-fX)$ are considered equal for the same reason. In these examples, the "equal" objects contain elements that are not set-theoretically identical, so they are not equal in this strict sense. However, because they are unique up to unique isomorphism, they can be canonically identified and treated as the same mathematical object.

When objects defined by their properties are equated in this way, we can speak of them as unique entities (e.g., *the* Klein four-group or *the* complex numbers), even though two people may have different constructions or realizations in mind. The rational numbers, for instance, are formally defined as equivalence classes of pairs of integers. The universal property of the rational numbers is essentially that they form a field that contains the integers and does not contain any proper subfield. Given two fields with these properties, there is a unique field isomorphism between them. This allows identifying these two fields, since every property of one of them can be transferred to the other through the isomorphism. The real numbers that can be expressed as a quotient of integers form the smallest subfield of the reals. There is thus a unique isomorphism from this subfield of the reals to the rational numbers defined by equivalence classes. So, the rational numbers may be identified to the elements of a subset of the real numbers. However, in some contexts this identification is not allowed. For example, in computer languages and type theory, real numbers and rational numbers have different representations, and the identification must be replaced with a type conversion.

## Notation

The most common notation to denote that two objects *A* and *B* are isomorphic is $A\cong B$ , and if $f:A\to B$ maps *A* isomorphically to *B*, then one can also write $f:A\;{\overset {\sim }{\longrightarrow }}\;B$ . However, depending on context, some authors may also use symbols including $\simeq$ , or $\approx$ to denote an isomorphism.
