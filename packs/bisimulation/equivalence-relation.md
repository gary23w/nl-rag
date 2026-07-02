---
title: "Equivalence relation"
source: https://en.wikipedia.org/wiki/Equivalence_relation
domain: bisimulation
license: CC-BY-SA-4.0
tags: bisimulation relation, bisimulation equivalence, coinductive proof, labelled transition system
fetched: 2026-07-02
---

# Equivalence relation

| Transitive binary relations |
|---|
| Symmetric Antisymmetric Connected Well-founded Has joins Has meets Reflexive Irreflexive Asymmetric Total, Semiconnex Anti- reflexive Equivalence relation (Green tick)Y ✗ ✗ ✗ ✗ ✗ (Green tick)Y ✗ ✗ Preorder (Quasiorder) ✗ ✗ ✗ ✗ ✗ ✗ (Green tick)Y ✗ ✗ Partial order ✗ (Green tick)Y ✗ ✗ ✗ ✗ (Green tick)Y ✗ ✗ Total preorder ✗ ✗ (Green tick)Y ✗ ✗ ✗ (Green tick)Y ✗ ✗ Total order ✗ (Green tick)Y (Green tick)Y ✗ ✗ ✗ (Green tick)Y ✗ ✗ Prewellordering ✗ ✗ (Green tick)Y (Green tick)Y ✗ ✗ (Green tick)Y ✗ ✗ Well-quasi-ordering ✗ ✗ ✗ (Green tick)Y ✗ ✗ (Green tick)Y ✗ ✗ Well-ordering ✗ (Green tick)Y (Green tick)Y (Green tick)Y ✗ ✗ (Green tick)Y ✗ ✗ Lattice ✗ (Green tick)Y ✗ ✗ (Green tick)Y (Green tick)Y (Green tick)Y ✗ ✗ Join-semilattice ✗ (Green tick)Y ✗ ✗ (Green tick)Y ✗ (Green tick)Y ✗ ✗ Meet-semilattice ✗ (Green tick)Y ✗ ✗ ✗ (Green tick)Y (Green tick)Y ✗ ✗ Strict partial order ✗ (Green tick)Y ✗ ✗ ✗ ✗ ✗ (Green tick)Y (Green tick)Y Strict weak order ✗ (Green tick)Y ✗ ✗ ✗ ✗ ✗ (Green tick)Y (Green tick)Y Strict total order ✗ (Green tick)Y (Green tick)Y ✗ ✗ ✗ ✗ (Green tick)Y (Green tick)Y Symmetric Antisymmetric Connected Well-founded Has joins Has meets Reflexive Irreflexive Asymmetric Definitions, for all $a,b$ and $S\neq \varnothing :$ ${\begin{aligned}&aRb\\\Rightarrow {}&bRa\end{aligned}}$ ${\begin{aligned}aRb{\text{ and }}&bRa\\\Rightarrow a={}&b\end{aligned}}$ ${\begin{aligned}a\neq {}&b\Rightarrow \\aRb{\text{ or }}&bRa\end{aligned}}$ ${\begin{aligned}\min S\\{\text{exists}}\end{aligned}}$ ${\begin{aligned}a\vee b\\{\text{exists}}\end{aligned}}$ ${\begin{aligned}a\wedge b\\{\text{exists}}\end{aligned}}$ $aRa$ ${\text{not }}aRa$ ${\begin{aligned}aRb\Rightarrow \\{\text{not }}bRa\end{aligned}}$ |
| (Green tick)Y indicates that the column's property is always true for the row's term (at the very left), while ✗ indicates that the property is not guaranteed in general (it might, or might not, hold). For example, that every equivalence relation is symmetric, but not necessarily antisymmetric, is indicated by (Green tick)Y in the "Symmetric" column and ✗ in the "Antisymmetric" column, respectively. All definitions tacitly require the homogeneous relation R be transitive: for all $a,b,c,$ if $aRb$ and $bRc$ then $aRc.$ A term's definition may require additional properties that are not listed in this table. |

In mathematics, an **equivalence relation** is a binary relation that is reflexive, symmetric, and transitive. The equipollence relation between line segments in geometry is a common example of an equivalence relation. A simpler example is numerical equality. Any number a is equal to itself (reflexive). If $a=b$ , then $b=a$ (symmetric). If $a=b$ and $b=c$ , then $a=c$ (transitive).

Each equivalence relation provides a partition of the underlying set into disjoint equivalence classes. Two elements of the given set are equivalent to each other if and only if they belong to the same equivalence class.

## Notation

Various notations are used in the literature to denote that two elements a and b of a set are equivalent with respect to an equivalence relation $R;$ the most common are " $a\sim b$ " and " $a\equiv b$ ", which are used when R is implicit, and variations of " $a\sim _{R}b$ ", " $a\equiv _{R}b$ ", or " ${a\mathop {R} b}$ " to specify R explicitly. Non-equivalence may be written " $a\not \sim b$ " or " $a\not \equiv b$ ".

## Definitions

A binary relation $\,\sim \,$ on a set X is said to be an equivalence relation if it is reflexive, symmetric and transitive. That is, for all $a,b,$ and c in $X:$

- $a\sim a$ (reflexivity).
- $a\sim b$ if and only if $b\sim a$ (symmetry).
- If $a\sim b$ and $b\sim c$ then $a\sim c$ (transitivity).

X together with the relation $\,\sim \,$ is called a setoid. The equivalence class of a under $\,\sim ,$ denoted $[a],$ is defined as $[a]=\{x\in X:x\sim a\}.$

### Alternative definition using relational algebra

In relational algebra, if $R\subseteq X\times Y$ and $S\subseteq Y\times Z$ are relations, then the composite relation $SR\subseteq X\times Z$ is defined so that $x\,SR\,z$ if and only if there is a $y\in Y$ such that $x\,R\,y$ and $y\,S\,z$ . This definition is a generalisation of the definition of functional composition. The defining properties of an equivalence relation R on a set X can then be reformulated as follows:

- $\operatorname {id} \subseteq R$ . (reflexivity). (Here, $\operatorname {id}$ denotes the identity function on X .)
- $R=R^{-1}$ (symmetry).
- $RR\subseteq R$ (transitivity).

## Examples

### Simple example

On the set $X=\{a,b,c\}$ , the relation $R=\{(a,a),(b,b),(c,c),(b,c),(c,b)\}$ is an equivalence relation. The following sets are equivalence classes of this relation: $[a]=\{a\},~~~~[b]=[c]=\{b,c\}.$

The set of all equivalence classes for R is $\{\{a\},\{b,c\}\}.$ This set is a partition of the set X . It is also called the quotient set of X by R .

### Equivalence relations

The following relations are all equivalence relations:

- "Is equal to" on the set of numbers. For example, ${\tfrac {1}{2}}$ is equal to ${\tfrac {4}{8}}.$
- "Is similar to" on the set of all triangles.
- "Is congruent to" on the set of all triangles.
- Given a function $f:X\to Y$ , "has the same image under f as" on the elements of f 's domain X . For example, 0 and $\pi$ have the same image under $\sin$ , viz. 0 . In particular:
  - "Has the same absolute value as" on the set of real numbers
  - "Has the same cosine as" on the set of all angles.
  - Given a natural number n , "is congruent to, modulo n " on the integers.
  - "Have the same length and direction" (equipollence) on the set of directed line segments.
  - "Has the same birthday as" on the set of all people.

### Relations that are not equivalences

- The relation "≥" between real numbers is reflexive and transitive, but not symmetric. For example, 7 ≥ 5 but not 5 ≥ 7.
- The relation "has a common factor greater than 1 with" between natural numbers greater than 1, is reflexive and symmetric, but not transitive. For example, the natural numbers 2 and 6 have a common factor greater than 1, and 6 and 3 have a common factor greater than 1, but 2 and 3 do not have a common factor greater than 1.
- The empty relation *R* (defined so that *aRb* is never true) on a set *X* is vacuously symmetric and transitive; however, it is not reflexive (unless *X* itself is empty).
- The relation "is approximately equal to" between real numbers, even if more precisely defined, is not an equivalence relation, because although reflexive and symmetric, it is not transitive, since multiple small changes can accumulate to become a big change. However, if the approximation is defined asymptotically, for example by saying that two functions *f* and *g* are approximately equal near some point if the limit of *f − g* is 0 at that point, then this defines an equivalence relation.

## Connections to other relations

- A partial order is a relation that is reflexive, *antisymmetric*, and transitive.
- Equality is both an equivalence relation and a partial order. Equality is also the only relation on a set that is reflexive, symmetric and antisymmetric. In algebraic expressions, equal variables may be substituted for one another, a facility that is not available for equivalence related variables. The equivalence classes of an equivalence relation can substitute for one another, but not individuals within a class.
- A strict partial order is irreflexive, transitive, and asymmetric.
- A partial equivalence relation is transitive and symmetric. Such a relation is reflexive if and only if it is total, that is, if for all $a,$ there exists some $b{\text{ such that }}a\sim b.$ Therefore, an equivalence relation may be alternatively defined as a symmetric, transitive, and total relation.
- A ternary equivalence relation is a ternary analogue to the usual (binary) equivalence relation.
- A reflexive and symmetric relation is a dependency relation (if finite), and a tolerance relation if infinite.
- A preorder is reflexive and transitive.
- A congruence relation is an equivalence relation whose domain X is also the underlying set for an algebraic structure, and which respects the additional structure. In general, congruence relations play the role of kernels of homomorphisms, and the quotient of a structure by a congruence relation can be formed. In many important cases, congruence relations have an alternative representation as substructures of the structure on which they are defined (e.g., the congruence relations on groups correspond to the normal subgroups).
- Any equivalence relation is the negation of an apartness relation, though the converse statement only holds in classical mathematics (as opposed to constructive mathematics), since it is equivalent to the law of excluded middle.
- Each relation that is both reflexive and left (or right) Euclidean is also an equivalence relation.

## Well-definedness under an equivalence relation

If $\,\sim \,$ is an equivalence relation on $X,$ and $P(x)$ is a property of elements of $X,$ such that whenever $x\sim y,$ $P(x)$ is true if $P(y)$ is true, then the property P is said to be well-defined or a *class invariant* under the relation $\,\sim .$

A frequent particular case occurs when f is a function from X to another set $Y;$ if $x_{1}\sim x_{2}$ implies $f\left(x_{1}\right)=f\left(x_{2}\right)$ then f is said to be a *morphism* for $\,\sim ,$ a *class invariant under* $\,\sim ,$ or simply *invariant under* $\,\sim .$ This occurs, e.g. in the character theory of finite groups. The latter case with the function f can be expressed by a commutative triangle. See also invariant. Some authors use "compatible with $\,\sim$ " or just "respects $\,\sim$ " instead of "invariant under $\,\sim$ ".

More generally, a function may map equivalent arguments (under an equivalence relation $\,\sim _{A}$ ) to equivalent values (under an equivalence relation $\,\sim _{B}$ ). Such a function is known as a morphism from $\,\sim _{A}$ to $\,\sim _{B}.$

Let $a,b\in X$ , and $\sim$ be an equivalence relation. Some key definitions and terminology follow:

### Equivalence class

A subset Y of X such that $a\sim b$ holds for all a and b in Y , and never for a in Y and b outside Y , is called an *equivalence class* of X by $\sim$ . Let $[a]:=\{x\in X:a\sim x\}$ denote the equivalence class to which a belongs. All elements of X equivalent to each other are also elements of the same equivalence class.

### Quotient set

The set of all equivalence classes of X by $\sim ,$ denoted $X/{\mathord {\sim }}:=\{[x]:x\in X\},$ is the *quotient set* of X by $\sim .$ If X is a topological space, there is a natural way of transforming $X/\sim$ into a topological space; see *Quotient space* for the details.

### Projection

The *projection* of $\,\sim \,$ is the function $\pi :X\to X/{\mathord {\sim }}$ defined by $\pi (x)=[x]$ which maps elements of X into their respective equivalence classes by $\,\sim .$

Theorem

on

projections

:

Let the function

$f:X\to B$

be such that if

$a\sim b$

then

$f(a)=f(b).$

Then there is a unique function

$g:X/\sim \to B$

such that

$f=g\pi .$

If

f

is a

surjection

and

$a\sim b{\text{ if and only if }}f(a)=f(b),$

then

g

is a

bijection

.

### Equivalence kernel

The **equivalence kernel** of a function f is the equivalence relation ~ defined by $x\sim y{\text{ if and only if }}f(x)=f(y).$ The equivalence kernel of an injection is the identity relation.

### Partition

A *partition* of *X* is a set *P* of nonempty subsets of *X*, such that every element of *X* is an element of a single element of *P*. Each element of *P* is a *cell* of the partition. Moreover, the elements of *P* are pairwise disjoint and their union is *X*.

#### Counting partitions

Let *X* be a finite set with *n* elements. Since every equivalence relation over *X* corresponds to a partition of *X*, and vice versa, the number of equivalence relations on *X* equals the number of distinct partitions of *X*, which is the *n*th Bell number *Bn*:

$B_{n}={\frac {1}{e}}\sum _{k=0}^{\infty }{\frac {k^{n}}{k!}}\quad$

(

Dobinski's formula

).

## Fundamental theorem of equivalence relations

A key result links equivalence relations and partitions:

- An equivalence relation ~ on a set *X* partitions *X*.
- Conversely, corresponding to any partition of *X*, there exists an equivalence relation ~ on *X*.

In both cases, the cells of the partition of *X* are the equivalence classes of *X* by ~. Since each element of *X* belongs to a unique cell of any partition of *X*, and since each cell of the partition is identical to an equivalence class of *X* by ~, each element of *X* belongs to a unique equivalence class of *X* by ~. Thus there is a natural bijection between the set of all equivalence relations on *X* and the set of all partitions of *X*.

## Comparing equivalence relations

If $\sim$ and $\approx$ are two equivalence relations on the same set S , and $a\sim b$ implies $a\approx b$ for all $a,b\in S,$ then $\approx$ is said to be a **coarser** relation than $\sim$ , and $\sim$ is a **finer** relation than $\approx$ . Equivalently,

- $\sim$ is finer than $\approx$ if every equivalence class of $\sim$ is a subset of an equivalence class of $\approx$ , and thus every equivalence class of $\approx$ is a union of equivalence classes of $\sim$ .
- $\sim$ is finer than $\approx$ if the partition created by $\sim$ is a refinement of the partition created by $\approx$ .

The equality equivalence relation is the finest equivalence relation on any set, while the universal relation, which relates all pairs of elements, is the coarsest.

The relation " $\sim$ is finer than $\approx$ " on the collection of all equivalence relations on a fixed set is itself a partial order relation, which makes the collection a geometric lattice.

## Generating equivalence relations

- Given any set $X,$ an equivalence relation over the set $[X\to X]$ of all functions $X\to X$ can be obtained as follows. Two functions are deemed equivalent when their respective sets of fixed points have the same cardinality, corresponding to cycles of length one in a permutation.
- An equivalence relation $\,\sim \,$ on X is the equivalence kernel of its surjective projection $\pi :X\to X/\sim .$ Conversely, any surjection between sets determines a partition on its domain, the set of preimages of singletons in the codomain. Thus an equivalence relation over $X,$ a partition of $X,$ and a projection whose domain is $X,$ are three equivalent ways of specifying the same thing.
- The intersection of any collection of equivalence relations over *X* (binary relations viewed as a subset of $X\times X$ ) is also an equivalence relation. This yields a convenient way of generating an equivalence relation: given any binary relation *R* on *X*, the equivalence relation *generated by R* is the intersection of all equivalence relations containing *R* (also known as the smallest equivalence relation containing *R*). Concretely, *R* generates the equivalence relation

$a\sim b$

if there exists a

natural number

n

and elements

$x_{0},\ldots ,x_{n}\in X$

such that

$a=x_{0}$

,

$b=x_{n}$

, and

$x_{i-1}\mathrel {R} x_{i}$

or

$x_{i}\mathrel {R} x_{i-1}$

, for

$i=1,\ldots ,n.$

The equivalence relation generated in this manner can be trivial. For instance, the equivalence relation generated by any

total order

on

X

has exactly one equivalence class,

X

itself.

- Equivalence relations can construct new spaces by "gluing things together." Let *X* be the unit Cartesian square $[0,1]\times [0,1],$ and let ~ be the equivalence relation on *X* defined by $(a,0)\sim (a,1)$ for all $a\in [0,1]$ and $(0,b)\sim (1,b)$ for all $b\in [0,1],$ Then the quotient space $X/\sim$ can be naturally identified (homeomorphism) with a torus: take a square piece of paper, bend and glue together the upper and lower edge to form a cylinder, then bend the resulting cylinder so as to glue together its two open ends, resulting in a torus.

## Algebraic structure

Much of mathematics is grounded in the study of equivalences, and order relations. Lattice theory captures the mathematical structure of order relations. Even though equivalence relations are as ubiquitous in mathematics as order relations, the algebraic structure of equivalences is not as well known as that of orders. The former structure draws primarily on group theory and, to a lesser extent, on the theory of lattices, categories, and groupoids.

### Group theory

Just as order relations are grounded in ordered sets, sets closed under pairwise supremum and infimum, equivalence relations are grounded in partitioned sets, which are sets closed under bijections that preserve partition structure. Since all such bijections map an equivalence class onto itself, such bijections are also known as permutations. Hence permutation groups (also known as transformation groups) and the related notion of orbit shed light on the mathematical structure of equivalence relations.

Let '~' denote an equivalence relation over some nonempty set *A*, called the universe or underlying set. Let *G* denote the set of bijective functions over *A* that preserve the partition structure of *A*, meaning that for all $x\in A$ and $g\in G,g(x)\in [x].$ Then the following three connected theorems hold:

- ~ partitions *A* into equivalence classes. (This is the *Fundamental Theorem of Equivalence Relations*, mentioned above);
- Given a partition of *A*, *G* is a transformation group under composition, whose orbits are the cells of the partition;
- Given a transformation group *G* over *A*, there exists an equivalence relation ~ over *A*, whose equivalence classes are the orbits of *G*.

In sum, given an equivalence relation ~ over *A*, there exists a transformation group *G* over *A* whose orbits are the equivalence classes of *A* under ~.

This transformation group characterisation of equivalence relations differs fundamentally from the way lattices characterize order relations. The arguments of the lattice theory operations meet and join are elements of some universe *A*. Meanwhile, the arguments of the transformation group operations composition and inverse are elements of a set of bijections, *A* → *A*.

Moving to groups in general, let *H* be a subgroup of some group *G*. Let ~ be an equivalence relation on *G*, such that $a\sim b{\text{ if and only if }}ab^{-1}\in H.$ The equivalence classes of ~—also called the orbits of the action of *H* on *G*—are the right **cosets** of *H* in *G*. Interchanging *a* and *b* yields the left cosets.

Related thinking can be found in Rosen (2008: chpt. 10).

### Categories and groupoids

Let *G* be a set and let "~" denote an equivalence relation over *G*. Then we can form a groupoid representing this equivalence relation as follows. The objects are the elements of *G*, and for any two elements *x* and *y* of *G*, there exists a unique morphism from *x* to *y* if and only if $x\sim y.$

The advantages of regarding an equivalence relation as a special case of a groupoid include:

- Whereas the notion of "free equivalence relation" does not exist, that of a free groupoid on a directed graph does. Thus it is meaningful to speak of a "presentation of an equivalence relation," i.e., a presentation of the corresponding groupoid;
- Bundles of groups, group actions, sets, and equivalence relations can be regarded as special cases of the notion of groupoid, a point of view that suggests a number of analogies;
- In many contexts "quotienting," and hence the appropriate equivalence relations often called congruences, are important. This leads to the notion of an internal groupoid in a category.

### Lattices

The equivalence relations on any set *X*, when ordered by set inclusion, form a complete lattice, called **Con** *X* by convention. The canonical map **ker** : *X*^*X* → **Con** *X*, relates the monoid *X*^*X* of all functions on *X* and **Con** *X*. **ker** is surjective but not injective. Less formally, the equivalence relation **ker** on *X*, takes each function *f* : *X* → *X* to its kernel **ker** *f*. Likewise, **ker(ker)** is an equivalence relation on *X*^*X*.

## Equivalence relations and mathematical logic

Equivalence relations are a ready source of examples or counterexamples. For example, an equivalence relation with exactly two infinite equivalence classes is an easy example of a theory which is ω-categorical, but not categorical for any larger cardinal number.

An implication of model theory is that the properties defining a relation can be proved independent of each other (and hence necessary parts of the definition) if and only if, for each property, examples can be found of relations not satisfying the given property while satisfying all the other properties. Hence the three defining properties of equivalence relations can be proved mutually independent by the following three examples:

- *Reflexive and transitive*: The relation ≤ on **N**. Or any preorder;
- *Symmetric and transitive*: The relation *R* on **N**, defined as *aRb* ↔ *ab* ≠ 0. Or any partial equivalence relation;
- *Reflexive and symmetric*: The relation *R* on **Z**, defined as *aRb* ↔ "*a* − *b* is divisible by at least one of 2 or 3." Or any dependency relation.

Properties definable in first-order logic that an equivalence relation may or may not possess include:

- The number of equivalence classes is finite or infinite;
- The number of equivalence classes equals the (finite) natural number *n*;
- All equivalence classes have infinite cardinality;
- The number of elements in each equivalence class is the natural number *n*.
