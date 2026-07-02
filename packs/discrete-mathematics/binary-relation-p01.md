---
title: "Binary relation (part 1/2)"
source: https://en.wikipedia.org/wiki/Binary_relation
domain: discrete-mathematics
license: CC-BY-SA-4.0
tags: discrete math, discrete mathematics, combinatorics, graph theory, set theory, permutation
fetched: 2026-07-02
part: 1/2
---

# Binary relation

| Transitive binary relations |
|---|
| Symmetric Antisymmetric Connected Well-founded Has joins Has meets Reflexive Irreflexive Asymmetric Total, Semiconnex Anti- reflexive Equivalence relation (Green tick)Y ✗ ✗ ✗ ✗ ✗ (Green tick)Y ✗ ✗ Preorder (Quasiorder) ✗ ✗ ✗ ✗ ✗ ✗ (Green tick)Y ✗ ✗ Partial order ✗ (Green tick)Y ✗ ✗ ✗ ✗ (Green tick)Y ✗ ✗ Total preorder ✗ ✗ (Green tick)Y ✗ ✗ ✗ (Green tick)Y ✗ ✗ Total order ✗ (Green tick)Y (Green tick)Y ✗ ✗ ✗ (Green tick)Y ✗ ✗ Prewellordering ✗ ✗ (Green tick)Y (Green tick)Y ✗ ✗ (Green tick)Y ✗ ✗ Well-quasi-ordering ✗ ✗ ✗ (Green tick)Y ✗ ✗ (Green tick)Y ✗ ✗ Well-ordering ✗ (Green tick)Y (Green tick)Y (Green tick)Y ✗ ✗ (Green tick)Y ✗ ✗ Lattice ✗ (Green tick)Y ✗ ✗ (Green tick)Y (Green tick)Y (Green tick)Y ✗ ✗ Join-semilattice ✗ (Green tick)Y ✗ ✗ (Green tick)Y ✗ (Green tick)Y ✗ ✗ Meet-semilattice ✗ (Green tick)Y ✗ ✗ ✗ (Green tick)Y (Green tick)Y ✗ ✗ Strict partial order ✗ (Green tick)Y ✗ ✗ ✗ ✗ ✗ (Green tick)Y (Green tick)Y Strict weak order ✗ (Green tick)Y ✗ ✗ ✗ ✗ ✗ (Green tick)Y (Green tick)Y Strict total order ✗ (Green tick)Y (Green tick)Y ✗ ✗ ✗ ✗ (Green tick)Y (Green tick)Y Symmetric Antisymmetric Connected Well-founded Has joins Has meets Reflexive Irreflexive Asymmetric Definitions, for all a , b {\displaystyle a,b} ({\displaystyle a,b}) and S ≠ ∅ : {\displaystyle S\neq \varnothing :} ({\displaystyle S\neq \varnothing :}) a R b ⇒ b R a {\displaystyle {\begin{aligned}&aRb\\\Rightarrow {}&bRa\end{aligned}}} ({\displaystyle {\begin{aligned}&aRb\\\Rightarrow {}&bRa\end{aligned}}}) a R b  and  b R a ⇒ a = b {\displaystyle {\begin{aligned}aRb{\text{ and }}&bRa\\\Rightarrow a={}&b\end{aligned}}} ({\displaystyle {\begin{aligned}aRb{\text{ and }}&bRa\\\Rightarrow a={}&b\end{aligned}}}) a ≠ b ⇒ a R b  or  b R a {\displaystyle {\begin{aligned}a\neq {}&b\Rightarrow \\aRb{\text{ or }}&bRa\end{aligned}}} ({\displaystyle {\begin{aligned}a\neq {}&b\Rightarrow \\aRb{\text{ or }}&bRa\end{aligned}}}) min S exists {\displaystyle {\begin{aligned}\min S\\{\text{exists}}\end{aligned}}} ({\displaystyle {\begin{aligned}\min S\\{\text{exists}}\end{aligned}}}) a ∨ b exists {\displaystyle {\begin{aligned}a\vee b\\{\text{exists}}\end{aligned}}} ({\displaystyle {\begin{aligned}a\vee b\\{\text{exists}}\end{aligned}}}) a ∧ b exists {\displaystyle {\begin{aligned}a\wedge b\\{\text{exists}}\end{aligned}}} ({\displaystyle {\begin{aligned}a\wedge b\\{\text{exists}}\end{aligned}}}) a R a {\displaystyle aRa} ({\displaystyle aRa}) not  a R a {\displaystyle {\text{not }}aRa} ({\displaystyle {\text{not }}aRa}) a R b ⇒ not  b R a {\displaystyle {\begin{aligned}aRb\Rightarrow \\{\text{not }}bRa\end{aligned}}} ({\displaystyle {\begin{aligned}aRb\Rightarrow \\{\text{not }}bRa\end{aligned}}}) |
| (Green tick)Y indicates that the column's property is always true for the row's term (at the very left), while ✗ indicates that the property is not guaranteed in general (it might, or might not, hold). For example, that every equivalence relation is symmetric, but not necessarily antisymmetric, is indicated by (Green tick)Y in the "Symmetric" column and ✗ in the "Antisymmetric" column, respectively. All definitions tacitly require the homogeneous relation R {\displaystyle R} ({\displaystyle R}) be transitive: for all a , b , c , {\displaystyle a,b,c,} ({\displaystyle a,b,c,}) if a R b {\displaystyle aRb} ({\displaystyle aRb}) and b R c {\displaystyle bRc} ({\displaystyle bRc}) then a R c . {\displaystyle aRc.} ({\displaystyle aRc.}) A term's definition may require additional properties that are not listed in this table. |

In mathematics, a **binary relation** associates some elements of one set called the *domain* with some elements of another set (possibly the same) called the *codomain*. Precisely, a binary relation over sets X {\displaystyle X} ({\displaystyle X}) and Y {\displaystyle Y} ({\displaystyle Y}) is a set of ordered pairs ( x , y ) {\displaystyle (x,y)} ({\displaystyle (x,y)}), where x {\displaystyle x} ({\displaystyle x}) is an element of X {\displaystyle X} ({\displaystyle X}) and y {\displaystyle y} ({\displaystyle y}) is an element of Y {\displaystyle Y} ({\displaystyle Y}). It encodes the common concept of relation: an element x {\displaystyle x} ({\displaystyle x}) is *related* to an element y {\displaystyle y} ({\displaystyle y}) if and only if the pair ( x , y ) {\displaystyle (x,y)} ({\displaystyle (x,y)}) belongs to the set of ordered pairs that defines the binary relation.

An example of a binary relation is the "divides" relation over the set of prime numbers P {\displaystyle \mathbb {P} } ({\displaystyle \mathbb {P} }) and the set of integers Z {\displaystyle \mathbb {Z} } ({\displaystyle \mathbb {Z} }), in which each prime p {\displaystyle p} ({\displaystyle p}) is related to each integer z {\displaystyle z} ({\displaystyle z}) that is a multiple of p {\displaystyle p} ({\displaystyle p}), but not to an integer that is not a multiple of p {\displaystyle p} ({\displaystyle p}). In this relation, for instance, the prime number 2 {\displaystyle 2} ({\displaystyle 2}) is related to numbers such as − 4 {\displaystyle -4} ({\displaystyle -4}), 0 {\displaystyle 0} ({\displaystyle 0}), 6 {\displaystyle 6} ({\displaystyle 6}), 10 {\displaystyle 10} ({\displaystyle 10}), but not to 1 {\displaystyle 1} ({\displaystyle 1}) or 9 {\displaystyle 9} ({\displaystyle 9}), just as the prime number 3 {\displaystyle 3} ({\displaystyle 3}) is related to 0 {\displaystyle 0} ({\displaystyle 0}), 6 {\displaystyle 6} ({\displaystyle 6}), and 9 {\displaystyle 9} ({\displaystyle 9}), but not to 4 {\displaystyle 4} ({\displaystyle 4}) or 13 {\displaystyle 13} ({\displaystyle 13}).

A binary relation is called a homogeneous relation when X = Y {\displaystyle X=Y} ({\displaystyle X=Y}). A binary relation is also called a *heterogeneous relation* when it is not necessary that X = Y {\displaystyle X=Y} ({\displaystyle X=Y}).

Binary relations, and especially homogeneous relations, are used in many branches of mathematics to model a wide variety of concepts. These include, among others:

- the "is greater than", "is equal to", and "divides" relations in arithmetic;
- the "is congruent to" relation in geometry;
- the "is adjacent to" relation in graph theory;
- the "is orthogonal to" relation in linear algebra.

A function may be defined as a binary relation that meets additional constraints. Binary relations are also heavily used in computer science.

A binary relation over sets X {\displaystyle X} ({\displaystyle X}) and Y {\displaystyle Y} ({\displaystyle Y}) can be identified with an element of the power set of the Cartesian product X × Y . {\displaystyle X\times Y.} ({\displaystyle X\times Y.}) Since a powerset is a lattice for set inclusion ( ⊆ {\displaystyle \subseteq } ({\displaystyle \subseteq })), relations can be manipulated using set operations (union, intersection, and complementation) and algebra of sets.

In some systems of axiomatic set theory, relations are extended to classes, which are generalizations of sets. This extension is needed for, among other things, modeling the concepts of "is an element of" or "is a subset of" in set theory, without running into logical inconsistencies such as Russell's paradox.

A binary relation is the most studied special case n = 2 {\displaystyle n=2} ({\displaystyle n=2}) of an n {\displaystyle n} ({\displaystyle n})-ary relation over sets X 1 , … , X n {\displaystyle X_{1},\dots ,X_{n}} ({\displaystyle X_{1},\dots ,X_{n}}), which is a subset of the Cartesian product X 1 × ⋯ × X n . {\displaystyle X_{1}\times \cdots \times X_{n}.} ({\displaystyle X_{1}\times \cdots \times X_{n}.})


## Definition

Given sets X {\displaystyle X} ({\displaystyle X}) and Y {\displaystyle Y} ({\displaystyle Y}), the Cartesian product X × Y {\displaystyle X\times Y} ({\displaystyle X\times Y}) is defined as { ( x , y ) ∣ x ∈ X  and  y ∈ Y } , {\displaystyle \{(x,y)\mid x\in X{\text{ and }}y\in Y\},} ({\displaystyle \{(x,y)\mid x\in X{\text{ and }}y\in Y\},}) and its elements are called *ordered pairs*.

A *binary relation* R {\displaystyle R} ({\displaystyle R}) over sets X {\displaystyle X} ({\displaystyle X}) and Y {\displaystyle Y} ({\displaystyle Y}) is a subset of X × Y . {\displaystyle X\times Y.} ({\displaystyle X\times Y.}) The set X {\displaystyle X} ({\displaystyle X}) is called the *domain* or *set of departure* of R {\displaystyle R} ({\displaystyle R}), and the set Y {\displaystyle Y} ({\displaystyle Y}) the *codomain* or *set of destination* of R {\displaystyle R} ({\displaystyle R}). In order to specify the choices of the sets X {\displaystyle X} ({\displaystyle X}) and Y {\displaystyle Y} ({\displaystyle Y}), some authors define a *binary relation* or *correspondence* as an ordered triple ( X , Y , G ) {\displaystyle (X,Y,G)} ({\displaystyle (X,Y,G)}), where G {\displaystyle G} ({\displaystyle G}) is a subset of X × Y {\displaystyle X\times Y} ({\displaystyle X\times Y}) called the *graph* of the binary relation. The statement ( x , y ) ∈ R {\displaystyle (x,y)\in R} ({\displaystyle (x,y)\in R}) reads " x {\displaystyle x} ({\displaystyle x}) is R {\displaystyle R} ({\displaystyle R})-related to y {\displaystyle y} ({\displaystyle y})" and is denoted by x R y {\displaystyle xRy} ({\displaystyle xRy}). The *domain of definition* or *active domain* of R {\displaystyle R} ({\displaystyle R}) is the set of all x {\displaystyle x} ({\displaystyle x}) such that x R y {\displaystyle xRy} ({\displaystyle xRy}) for at least one y {\displaystyle y} ({\displaystyle y}). The *codomain of definition*, *active codomain*, *image* or *range* of R {\displaystyle R} ({\displaystyle R}) is the set of all y {\displaystyle y} ({\displaystyle y}) such that x R y {\displaystyle xRy} ({\displaystyle xRy}) for at least one x {\displaystyle x} ({\displaystyle x}). The *field* of R {\displaystyle R} ({\displaystyle R}) is the union of its domain of definition and its codomain of definition.

When X = Y , {\displaystyle X=Y,} ({\displaystyle X=Y,}) a binary relation is called a *homogeneous relation* (or *endorelation*). To emphasize the fact that X {\displaystyle X} ({\displaystyle X}) and Y {\displaystyle Y} ({\displaystyle Y}) are allowed to be different, a binary relation is also called a **heterogeneous relation**. The prefix *hetero* is from the Greek ἕτερος (*heteros*, "other, another, different").

A heterogeneous relation has been called a **rectangular relation**, suggesting that it does not have the square-like symmetry of a homogeneous relation on a set where A = B . {\displaystyle A=B.} ({\displaystyle A=B.}) Commenting on the development of binary relations beyond homogeneous relations, researchers wrote, "... a variant of the theory has evolved that treats relations from the very beginning as *heterogeneous* or *rectangular*, i.e. as relations where the normal case is that they are relations between different sets."

The terms *correspondence*, **dyadic relation** and **two-place relation** are synonyms for binary relation, though some authors use the term "binary relation" for any subset of a Cartesian product X × Y {\displaystyle X\times Y} ({\displaystyle X\times Y}) without reference to X {\displaystyle X} ({\displaystyle X}) and Y {\displaystyle Y} ({\displaystyle Y}), and reserve the term "correspondence" for a binary relation with reference to X {\displaystyle X} ({\displaystyle X}) and Y {\displaystyle Y} ({\displaystyle Y}).

In a binary relation, the order of the elements is important; if x ≠ y {\displaystyle x\neq y} ({\displaystyle x\neq y}) then y R x {\displaystyle yRx} ({\displaystyle yRx}) can be true or false independently of x R y {\displaystyle xRy} ({\displaystyle xRy}). For example, 3 {\displaystyle 3} ({\displaystyle 3}) divides 9 {\displaystyle 9} ({\displaystyle 9}), but 9 {\displaystyle 9} ({\displaystyle 9}) does not divide 3 {\displaystyle 3} ({\displaystyle 3}).


## Operations

### Union

If R {\displaystyle R} ({\displaystyle R}) and S {\displaystyle S} ({\displaystyle S}) are binary relations over sets X {\displaystyle X} ({\displaystyle X}) and Y {\displaystyle Y} ({\displaystyle Y}) then R ∪ S = { ( x , y ) ∣ x R y  or  x S y } {\displaystyle R\cup S=\{(x,y)\mid xRy{\text{ or }}xSy\}} ({\displaystyle R\cup S=\{(x,y)\mid xRy{\text{ or }}xSy\}}) is the *union relation* of R {\displaystyle R} ({\displaystyle R}) and S {\displaystyle S} ({\displaystyle S}) over X {\displaystyle X} ({\displaystyle X}) and Y {\displaystyle Y} ({\displaystyle Y}).

The identity element is the empty relation, in which no x {\displaystyle x} ({\displaystyle x}) is related to any y {\displaystyle y} ({\displaystyle y}).

For example, ≤ {\displaystyle \leq } ({\displaystyle \leq }) is the union of < {\displaystyle <} ({\displaystyle <}) and = {\displaystyle =} ({\displaystyle =}), and ≥ {\displaystyle \geq } ({\displaystyle \geq }) is the union of > {\displaystyle >} ({\displaystyle >}) and = {\displaystyle =} ({\displaystyle =}).

### Intersection

If R {\displaystyle R} ({\displaystyle R}) and S {\displaystyle S} ({\displaystyle S}) are binary relations over sets X {\displaystyle X} ({\displaystyle X}) and Y {\displaystyle Y} ({\displaystyle Y}) then R ∩ S = { ( x , y ) ∣ x R y  and  x S y } {\displaystyle R\cap S=\{(x,y)\mid xRy{\text{ and }}xSy\}} ({\displaystyle R\cap S=\{(x,y)\mid xRy{\text{ and }}xSy\}}) is the *intersection relation* of R {\displaystyle R} ({\displaystyle R}) and S {\displaystyle S} ({\displaystyle S}) over X {\displaystyle X} ({\displaystyle X}) and Y {\displaystyle Y} ({\displaystyle Y}).

The identity element is the universal relation, in which every x {\displaystyle x} ({\displaystyle x}) is related to every y {\displaystyle y} ({\displaystyle y}).

For example, the relation "is divisible by 6" is the intersection of the relations "is divisible by 3" and "is divisible by 2".

### Composition

If R {\displaystyle R} ({\displaystyle R}) is a binary relation over sets X {\displaystyle X} ({\displaystyle X}) and Y {\displaystyle Y} ({\displaystyle Y}), and S {\displaystyle S} ({\displaystyle S}) is a binary relation over sets Y {\displaystyle Y} ({\displaystyle Y}) and Z {\displaystyle Z} ({\displaystyle Z}) then S ∘ R = { ( x , z ) ∣  there exists  y ∈ Y  such that  x R y  and  y S z } {\displaystyle S\circ R=\{(x,z)\mid {\text{ there exists }}y\in Y{\text{ such that }}xRy{\text{ and }}ySz\}} ({\displaystyle S\circ R=\{(x,z)\mid {\text{ there exists }}y\in Y{\text{ such that }}xRy{\text{ and }}ySz\}}) (also denoted by R ; S {\displaystyle R;S} ({\displaystyle R;S})) is the *composition relation* of R {\displaystyle R} ({\displaystyle R}) and S {\displaystyle S} ({\displaystyle S}) over X {\displaystyle X} ({\displaystyle X}) and Z {\displaystyle Z} ({\displaystyle Z}).

If X = Y = Z {\displaystyle X=Y=Z} ({\displaystyle X=Y=Z}), the identity element w.r.t. composition is the identity relation on X {\displaystyle X} ({\displaystyle X}), in which x ∈ X {\displaystyle x\in X} ({\displaystyle x\in X}) is related only to itself.

The order of R {\displaystyle R} ({\displaystyle R}) and S {\displaystyle S} ({\displaystyle S}) in the notation S ∘ R {\displaystyle S\circ R} ({\displaystyle S\circ R}) used here agrees with the standard notational order for composition of functions. For example, the composition (is parent of) ∘ {\displaystyle \circ } ({\displaystyle \circ })(is mother of) yields (is grandmother of), while the composition (is mother of) ∘ {\displaystyle \circ } ({\displaystyle \circ })(is parent of) yields (is maternal grandparent of). For the latter case, if x {\displaystyle x} ({\displaystyle x}) is the parent of y {\displaystyle y} ({\displaystyle y}) and y {\displaystyle y} ({\displaystyle y}) is the mother of z {\displaystyle z} ({\displaystyle z}), then x {\displaystyle x} ({\displaystyle x}) is the maternal grandparent of z {\displaystyle z} ({\displaystyle z}).

### Converse

If R {\displaystyle R} ({\displaystyle R}) is a binary relation over sets X {\displaystyle X} ({\displaystyle X}) and Y {\displaystyle Y} ({\displaystyle Y}) then R T = { ( y , x ) ∣ x R y } {\displaystyle R^{\textsf {T}}=\{(y,x)\mid xRy\}} ({\displaystyle R^{\textsf {T}}=\{(y,x)\mid xRy\}}) is the *converse relation*, also called *inverse relation*, of R {\displaystyle R} ({\displaystyle R}) over Y {\displaystyle Y} ({\displaystyle Y}) and X {\displaystyle X} ({\displaystyle X}).

For example, = {\displaystyle =} ({\displaystyle =}) is the converse of itself, as is ≠ {\displaystyle \neq } ({\displaystyle \neq }), and < {\displaystyle <} ({\displaystyle <}) and > {\displaystyle >} ({\displaystyle >}) are each other's converse, as are ≤ {\displaystyle \leq } ({\displaystyle \leq }) and ≥ . {\displaystyle \geq .} ({\displaystyle \geq .}) A binary relation is equal to its converse if and only if it is symmetric.

### Complement

If R {\displaystyle R} ({\displaystyle R}) is a binary relation over sets X {\displaystyle X} ({\displaystyle X}) and Y {\displaystyle Y} ({\displaystyle Y}) then R ¯ = { ( x , y ) ∣ ¬ x R y } {\displaystyle {\bar {R}}=\{(x,y)\mid \neg xRy\}} ({\displaystyle {\bar {R}}=\{(x,y)\mid \neg xRy\}}) (also denoted by ¬ R {\displaystyle \neg R} ({\displaystyle \neg R})) is the *complementary relation* of R {\displaystyle R} ({\displaystyle R}) over X {\displaystyle X} ({\displaystyle X}) and Y {\displaystyle Y} ({\displaystyle Y}).

For example, = {\displaystyle =} ({\displaystyle =}) and ≠ {\displaystyle \neq } ({\displaystyle \neq }) are each other's complement, as are ⊆ {\displaystyle \subseteq } ({\displaystyle \subseteq }) and ⊈ {\displaystyle \not \subseteq } ({\displaystyle \not \subseteq }), ⊇ {\displaystyle \supseteq } ({\displaystyle \supseteq }) and ⊉ {\displaystyle \not \supseteq } ({\displaystyle \not \supseteq }), ∈ {\displaystyle \in } ({\displaystyle \in }) and ∉ {\displaystyle \not \in } ({\displaystyle \not \in }), and for total orders also < {\displaystyle <} ({\displaystyle <}) and ≥ {\displaystyle \geq } ({\displaystyle \geq }), and > {\displaystyle >} ({\displaystyle >}) and ≤ {\displaystyle \leq } ({\displaystyle \leq }).

The complement of the converse relation R T {\displaystyle R^{\textsf {T}}} ({\displaystyle R^{\textsf {T}}}) is the converse of the complement: R T ¯ = R ¯ T . {\displaystyle {\overline {R^{\mathsf {T}}}}={\bar {R}}^{\mathsf {T}}.} ({\displaystyle {\overline {R^{\mathsf {T}}}}={\bar {R}}^{\mathsf {T}}.})

If X = Y , {\displaystyle X=Y,} ({\displaystyle X=Y,}) the complement has the following properties:

- If a relation is symmetric, then so is the complement.
- The complement of a reflexive relation is irreflexive—and vice versa.
- The complement of a strict weak order is a total preorder—and vice versa.

### Restriction

If R {\displaystyle R} ({\displaystyle R}) is a binary homogeneous relation over a set X {\displaystyle X} ({\displaystyle X}) and S {\displaystyle S} ({\displaystyle S}) is a subset of X {\displaystyle X} ({\displaystyle X}) then R | S = { ( x , y ) ∣ x R y  and  x ∈ S  and  y ∈ S } {\displaystyle R_{\vert S}=\{(x,y)\mid xRy{\text{ and }}x\in S{\text{ and }}y\in S\}} ({\displaystyle R_{\vert S}=\{(x,y)\mid xRy{\text{ and }}x\in S{\text{ and }}y\in S\}}) is the *restriction relation* of R {\displaystyle R} ({\displaystyle R}) to S {\displaystyle S} ({\displaystyle S}) over X {\displaystyle X} ({\displaystyle X}).

If R {\displaystyle R} ({\displaystyle R}) is a binary relation over sets X {\displaystyle X} ({\displaystyle X}) and Y {\displaystyle Y} ({\displaystyle Y}) and if S {\displaystyle S} ({\displaystyle S}) is a subset of X {\displaystyle X} ({\displaystyle X}) then R | S = { ( x , y ) ∣ x R y  and  x ∈ S } {\displaystyle R_{\vert S}=\{(x,y)\mid xRy{\text{ and }}x\in S\}} ({\displaystyle R_{\vert S}=\{(x,y)\mid xRy{\text{ and }}x\in S\}}) is the *left-restriction relation* of R {\displaystyle R} ({\displaystyle R}) to S {\displaystyle S} ({\displaystyle S}) over X {\displaystyle X} ({\displaystyle X}) and Y {\displaystyle Y} ({\displaystyle Y}).

If a relation is reflexive, irreflexive, symmetric, antisymmetric, asymmetric, transitive, total, trichotomous, a partial order, total order, strict weak order, total preorder (weak order), or an equivalence relation, then so too are its restrictions.

However, the transitive closure of a restriction is a subset of the restriction of the transitive closure, i.e., in general not equal. For example, restricting the relation " x {\displaystyle x} ({\displaystyle x}) is parent of y {\displaystyle y} ({\displaystyle y})" to females yields the relation " x {\displaystyle x} ({\displaystyle x}) is mother of the woman y {\displaystyle y} ({\displaystyle y})"; its transitive closure does not relate a woman with her paternal grandmother. On the other hand, the transitive closure of "is parent of" is "is ancestor of"; its restriction to females does relate a woman with her paternal grandmother.

Also, the various concepts of completeness (not to be confused with being "total") do not carry over to restrictions. For example, over the real numbers a property of the relation ≤ {\displaystyle \leq } ({\displaystyle \leq }) is that every non-empty subset S ⊆ R {\displaystyle S\subseteq \mathbb {R} } ({\displaystyle S\subseteq \mathbb {R} }) with an upper bound in R {\displaystyle \mathbb {R} } ({\displaystyle \mathbb {R} }) has a least upper bound (also called supremum) in R . {\displaystyle \mathbb {R} .} ({\displaystyle \mathbb {R} .}) However, for the rational numbers this supremum is not necessarily rational, so the same property does not hold on the restriction of the relation ≤ {\displaystyle \leq } ({\displaystyle \leq }) to the rational numbers.

A binary relation R {\displaystyle R} ({\displaystyle R}) over sets X {\displaystyle X} ({\displaystyle X}) and Y {\displaystyle Y} ({\displaystyle Y}) is said to be *contained in* a relation S {\displaystyle S} ({\displaystyle S}) over X {\displaystyle X} ({\displaystyle X}) and Y {\displaystyle Y} ({\displaystyle Y}), written R ⊆ S , {\displaystyle R\subseteq S,} ({\displaystyle R\subseteq S,}) if R {\displaystyle R} ({\displaystyle R}) is a subset of S {\displaystyle S} ({\displaystyle S}), that is, for all x ∈ X {\displaystyle x\in X} ({\displaystyle x\in X}) and y ∈ Y , {\displaystyle y\in Y,} ({\displaystyle y\in Y,}) if x R y {\displaystyle xRy} ({\displaystyle xRy}), then x S y {\displaystyle xSy} ({\displaystyle xSy}). If R {\displaystyle R} ({\displaystyle R}) is contained in S {\displaystyle S} ({\displaystyle S}) and S {\displaystyle S} ({\displaystyle S}) is contained in R {\displaystyle R} ({\displaystyle R}), then R {\displaystyle R} ({\displaystyle R}) and S {\displaystyle S} ({\displaystyle S}) are called *equal* written R = S {\displaystyle R=S} ({\displaystyle R=S}). If R {\displaystyle R} ({\displaystyle R}) is contained in S {\displaystyle S} ({\displaystyle S}) but S {\displaystyle S} ({\displaystyle S}) is not contained in R {\displaystyle R} ({\displaystyle R}), then R {\displaystyle R} ({\displaystyle R}) is said to be *smaller* than S {\displaystyle S} ({\displaystyle S}), written R ⊊ S . {\displaystyle R\subsetneq S.} ({\displaystyle R\subsetneq S.}) For example, on the rational numbers, the relation > {\displaystyle >} ({\displaystyle >}) is smaller than ≥ {\displaystyle \geq } ({\displaystyle \geq }), and equal to the composition > ∘ > {\displaystyle >\circ >} ({\displaystyle >\circ >}).

### Matrix representation

Binary relations over sets X {\displaystyle X} ({\displaystyle X}) and Y {\displaystyle Y} ({\displaystyle Y}) can be represented algebraically by logical matrices indexed by X {\displaystyle X} ({\displaystyle X}) and Y {\displaystyle Y} ({\displaystyle Y}) with entries in the Boolean semiring (addition corresponds to OR and multiplication to AND) where matrix addition corresponds to union of relations, matrix multiplication corresponds to composition of relations (of a relation over X {\displaystyle X} ({\displaystyle X}) and Y {\displaystyle Y} ({\displaystyle Y}) and a relation over Y {\displaystyle Y} ({\displaystyle Y}) and Z {\displaystyle Z} ({\displaystyle Z})), the Hadamard product corresponds to intersection of relations, the zero matrix corresponds to the empty relation, and the matrix of ones corresponds to the universal relation. Homogeneous relations (when X = Y {\displaystyle X=Y} ({\displaystyle X=Y})) form a matrix semiring (indeed, a matrix semialgebra over the Boolean semiring) where the identity matrix corresponds to the identity relation.


## Examples

| A {\displaystyle A} ({\displaystyle A}) B {\displaystyle B} ({\displaystyle B}) | ball | car | doll | cup |
|---|---|---|---|---|
| John | **+** | − | − | − |
| Mary | − | − | **+** | − |
| Venus | − | **+** | − | − |

| A {\displaystyle A} ({\displaystyle A}) B {\displaystyle B} ({\displaystyle B}) | ball | car | doll | cup |
|---|---|---|---|---|
| John | **+** | − | − | − |
| Mary | − | − | **+** | − |
| Ian | − | − | − | − |
| Venus | − | **+** | − | − |

1. The following example shows that the choice of codomain is important. Suppose there are four objects A = { ball, car, doll, cup } {\displaystyle A=\{{\text{ball, car, doll, cup}}\}} ({\displaystyle A=\{{\text{ball, car, doll, cup}}\}}) and four people B = { John, Mary, Ian, Venus } . {\displaystyle B=\{{\text{John, Mary, Ian, Venus}}\}.} ({\displaystyle B=\{{\text{John, Mary, Ian, Venus}}\}.}) A possible relation on A {\displaystyle A} ({\displaystyle A}) and B {\displaystyle B} ({\displaystyle B}) is the relation "is owned by", given by R = { ( ball, John ) , ( doll, Mary ) , ( car, Venus ) } . {\displaystyle R=\{({\text{ball, John}}),({\text{doll, Mary}}),({\text{car, Venus}})\}.} ({\displaystyle R=\{({\text{ball, John}}),({\text{doll, Mary}}),({\text{car, Venus}})\}.}) That is, John owns the ball, Mary owns the doll, and Venus owns the car. Nobody owns the cup and Ian owns nothing; see the 1st example. As a set, R {\displaystyle R} ({\displaystyle R}) does not involve Ian, and therefore R {\displaystyle R} ({\displaystyle R}) could have been viewed as a subset of A × { John, Mary, Venus } , {\displaystyle A\times \{{\text{John, Mary, Venus}}\},} ({\displaystyle A\times \{{\text{John, Mary, Venus}}\},}) i.e. a relation over A {\displaystyle A} ({\displaystyle A}) and { John, Mary, Venus } ; {\displaystyle \{{\text{John, Mary, Venus}}\};} ({\displaystyle \{{\text{John, Mary, Venus}}\};}) see the 2nd example. But in that second example, R {\displaystyle R} ({\displaystyle R}) contains no information about the ownership by Ian. While the 2nd example relation is surjective (see below), the 1st is not. Ocean borders continent NA SA AF EU AS AU AA Indian 0 0 1 0 1 1 1 Arctic 1 0 0 1 1 0 0 Atlantic 1 1 1 1 0 0 1 Pacific 1 1 0 0 1 1 1
2. Let A = { Indian , Arctic , Atlantic , Pacific } {\displaystyle A=\{{\text{Indian}},{\text{Arctic}},{\text{Atlantic}},{\text{Pacific}}\}} ({\displaystyle A=\{{\text{Indian}},{\text{Arctic}},{\text{Atlantic}},{\text{Pacific}}\}}), the oceans of the globe, and B = { NA , SA , AF , EU , AS , AU , AA } {\displaystyle B=\{{\text{NA}},{\text{SA}},{\text{AF}},{\text{EU}},{\text{AS}},{\text{AU}},{\text{AA}}\}} ({\displaystyle B=\{{\text{NA}},{\text{SA}},{\text{AF}},{\text{EU}},{\text{AS}},{\text{AU}},{\text{AA}}\}}), the continents. Let a R b {\displaystyle aRb} ({\displaystyle aRb}) represent that ocean a {\displaystyle a} ({\displaystyle a}) borders continent b {\displaystyle b} ({\displaystyle b}). Then the logical matrix for this relation is: R = ( 0 0 1 0 1 1 1 1 0 0 1 1 0 0 1 1 1 1 0 0 1 1 1 0 0 1 1 1 ) . {\displaystyle R={\begin{pmatrix}0&0&1&0&1&1&1\\1&0&0&1&1&0&0\\1&1&1&1&0&0&1\\1&1&0&0&1&1&1\end{pmatrix}}.} ({\displaystyle R={\begin{pmatrix}0&0&1&0&1&1&1\\1&0&0&1&1&0&0\\1&1&1&1&0&0&1\\1&1&0&0&1&1&1\end{pmatrix}}.}) The connectivity of the planet Earth can be viewed through R R T {\displaystyle RR^{\mathsf {T}}} ({\displaystyle RR^{\mathsf {T}}}) and R T R {\displaystyle R^{\mathsf {T}}R} ({\displaystyle R^{\mathsf {T}}R}), the former being a 4 × 4 {\displaystyle 4\times 4} ({\displaystyle 4\times 4}) relation on A {\displaystyle A} ({\displaystyle A}), which is the universal relation ( A × A {\displaystyle A\times A} ({\displaystyle A\times A}) or a logical matrix of all ones). This universal relation reflects the fact that every ocean is separated from the others by at most one continent. On the other hand, R T R {\displaystyle R^{\mathsf {T}}R} ({\displaystyle R^{\mathsf {T}}R}) is a relation on B × B {\displaystyle B\times B} ({\displaystyle B\times B}) which *fails* to be universal because at least two oceans must be traversed to voyage from Europe to Australia.
3. Visualization of relations leans on graph theory: For relations on a set (homogeneous relations), a directed graph illustrates a relation and a graph a symmetric relation. For heterogeneous relations a hypergraph has edges possibly with more than two nodes, and can be illustrated by a bipartite graph. Just as the clique is integral to relations on a set, so bicliques are used to describe heterogeneous relations; indeed, they are the "concepts" that generate a lattice associated with a relation.
4. Hyperbolic orthogonality: Time and space are different categories, and temporal properties are separate from spatial properties. The idea of *simultaneous events* is simple in absolute space and time since each time t {\displaystyle t} ({\displaystyle t}) determines a simultaneous hyperplane in that cosmology. Hermann Minkowski changed that when he articulated the notion of *relative simultaneity*, which exists when spatial events are "normal" to a time characterized by a velocity. He used an indefinite inner product, and specified that a time vector is normal to a space vector when that product is zero. The indefinite inner product in a composition algebra is given by ⟨ x , z ⟩ = x z ¯ + x ¯ z {\displaystyle \langle x,z\rangle =x{\bar {z}}+{\bar {x}}z\;} ({\displaystyle \langle x,z\rangle =x{\bar {z}}+{\bar {x}}z\;}) where the overbar denotes conjugation. As a relation between some temporal events and some spatial events, hyperbolic orthogonality (as found in split-complex numbers) is a heterogeneous relation.
5. A geometric configuration can be considered a relation between its points and its lines. The relation is expressed as incidence. Finite and infinite projective and affine planes are included. Jakob Steiner pioneered the cataloguing of configurations with the Steiner systems S ⁡ ( t , k , n ) {\displaystyle \operatorname {S} (t,k,n)} ({\displaystyle \operatorname {S} (t,k,n)}) which have an n-element set S {\displaystyle \operatorname {S} } ({\displaystyle \operatorname {S} }) and a set of k-element subsets called **blocks**, such that a subset with t {\displaystyle t} ({\displaystyle t}) elements lies in just one block. These incidence structures have been generalized with block designs. The incidence matrix used in these geometrical contexts corresponds to the logical matrix used generally with binary relations. An incidence structure is a triple D = ( V , B , I ) {\displaystyle \mathbf {D} =(V,\mathbf {B} ,I)} ({\displaystyle \mathbf {D} =(V,\mathbf {B} ,I)}) where V {\displaystyle V} ({\displaystyle V}) and B {\displaystyle \mathbf {B} } ({\displaystyle \mathbf {B} }) are any two disjoint sets and I {\displaystyle I} ({\displaystyle I}) is a binary relation between V {\displaystyle V} ({\displaystyle V}) and B {\displaystyle \mathbf {B} } ({\displaystyle \mathbf {B} }), i.e. I ⊆ V × B . {\displaystyle I\subseteq V\times \mathbf {B} .} ({\displaystyle I\subseteq V\times \mathbf {B} .}) The elements of V {\displaystyle V} ({\displaystyle V}) will be called *points*, those of B {\displaystyle \mathbf {B} } ({\displaystyle \mathbf {B} }) *blocks*, and those of I {\displaystyle I} ({\displaystyle I}) *flags*.


## Types of binary relations

Some important types of binary relations R {\displaystyle R} ({\displaystyle R}) over sets X {\displaystyle X} ({\displaystyle X}) and Y {\displaystyle Y} ({\displaystyle Y}) are listed below.

Uniqueness properties:

- **Injective** (also called **left-unique**): for all x , y ∈ X {\displaystyle x,y\in X} ({\displaystyle x,y\in X}) and all z ∈ Y , {\displaystyle z\in Y,} ({\displaystyle z\in Y,}) if x R z {\displaystyle xRz} ({\displaystyle xRz}) and y R z {\displaystyle yRz} ({\displaystyle yRz}) then x = y {\displaystyle x=y} ({\displaystyle x=y}). In other words, every element of the codomain has *at most* one preimage element. For such a relation, Y {\displaystyle Y} ({\displaystyle Y}) is called *a primary key* of R {\displaystyle R} ({\displaystyle R}). For example, the green and blue binary relations in the diagram are injective, but the red one is not (as it relates both − 1 {\displaystyle -1} ({\displaystyle -1}) and 1 {\displaystyle 1} ({\displaystyle 1}) to 1 {\displaystyle 1} ({\displaystyle 1})), nor the black one (as it relates both − 1 {\displaystyle -1} ({\displaystyle -1}) and 1 {\displaystyle 1} ({\displaystyle 1}) to 0 {\displaystyle 0} ({\displaystyle 0})).
- **Functional** (also called **right-unique** or **univalent**): for all x ∈ X {\displaystyle x\in X} ({\displaystyle x\in X}) and all y , z ∈ Y , {\displaystyle y,z\in Y,} ({\displaystyle y,z\in Y,}) if x R y {\displaystyle xRy} ({\displaystyle xRy}) and x R z {\displaystyle xRz} ({\displaystyle xRz}) then y = z {\displaystyle y=z} ({\displaystyle y=z}). In other words, every element of the domain has *at most* one image element. Such a binary relation is called a *partial function* or *partial mapping*. For such a relation, { X } {\displaystyle \{X\}} ({\displaystyle \{X\}}) is called *a primary key* of R {\displaystyle R} ({\displaystyle R}). For example, the red and green binary relations in the diagram are functional, but the blue one is not (as it relates 1 {\displaystyle 1} ({\displaystyle 1}) to both 1 {\displaystyle 1} ({\displaystyle 1}) and − 1 {\displaystyle -1} ({\displaystyle -1})), nor the black one (as it relates 0 {\displaystyle 0} ({\displaystyle 0}) to both − 1 {\displaystyle -1} ({\displaystyle -1}) and 1 {\displaystyle 1} ({\displaystyle 1})).
- **One-to-one**: injective and functional. For example, the green binary relation in the diagram is one-to-one, but the red, blue and black ones are not.
- **One-to-many**: injective and not functional. For example, the blue binary relation in the diagram is one-to-many, but the red, green and black ones are not.
- **Many-to-one**: functional and not injective. For example, the red binary relation in the diagram is many-to-one, but the green, blue and black ones are not.
- **Many-to-many**: not injective nor functional. For example, the black binary relation in the diagram is many-to-many, but the red, green and blue ones are not.

Totality properties (only definable if the domain X {\displaystyle X} ({\displaystyle X}) and codomain Y {\displaystyle Y} ({\displaystyle Y}) are specified):

- **Total** (also called **left-total**): for all x ∈ X {\displaystyle x\in X} ({\displaystyle x\in X}) there exists a y ∈ Y {\displaystyle y\in Y} ({\displaystyle y\in Y}) such that x R y {\displaystyle xRy} ({\displaystyle xRy}). In other words, every element of the domain has *at least* one image element. In other words, the domain of definition of R {\displaystyle R} ({\displaystyle R}) is equal to X {\displaystyle X} ({\displaystyle X}). This property, is different from the definition of *connected* (also called *total* by some authors) in Properties. Such a binary relation is called a *multivalued function*. For example, the red and green binary relations in the diagram are total, but the blue one is not (as it does not relate − 1 {\displaystyle -1} ({\displaystyle -1}) to any real number), nor the black one (as it does not relate 2 {\displaystyle 2} ({\displaystyle 2}) to any real number). As another example, > {\displaystyle >} ({\displaystyle >}) is a total relation over the integers. But it is not a total relation over the positive integers, because there is no y {\displaystyle y} ({\displaystyle y}) in the positive integers such that 1 > y {\displaystyle 1>y} ({\displaystyle 1>y}). However, < {\displaystyle <} ({\displaystyle <}) is a total relation over the positive integers, the rational numbers and the real numbers. Every reflexive relation is total: for a given x {\displaystyle x} ({\displaystyle x}), choose y = x {\displaystyle y=x} ({\displaystyle y=x}).
- **Surjective** (also called **right-total**): for all y ∈ Y {\displaystyle y\in Y} ({\displaystyle y\in Y}), there exists an x ∈ X {\displaystyle x\in X} ({\displaystyle x\in X}) such that x R y {\displaystyle xRy} ({\displaystyle xRy}). In other words, every element of the codomain has *at least* one preimage element. In other words, the codomain of definition of R {\displaystyle R} ({\displaystyle R}) is equal to Y {\displaystyle Y} ({\displaystyle Y}). For example, the green and blue binary relations in the diagram are surjective, but the red one is not (as it does not relate any real number to − 1 {\displaystyle -1} ({\displaystyle -1})), nor the black one (as it does not relate any real number to 2 {\displaystyle 2} ({\displaystyle 2})).

Uniqueness and totality properties (only definable if the domain X {\displaystyle X} ({\displaystyle X}) and codomain Y {\displaystyle Y} ({\displaystyle Y}) are specified):

- A **function** (also called **mapping**): a binary relation that is functional and total. In other words, every element of the domain has *exactly* one image element. For example, the red and green binary relations in the diagram are functions, but the blue and black ones are not.
  - An **injection**: a function that is injective. For example, the green relation in the diagram is an injection, but the red one is not; the black and the blue relation is not even a function.
  - A **surjection**: a function that is surjective. For example, the green relation in the diagram is a surjection, but the red one is not.
  - A **bijection**: a function that is injective and surjective. In other words, every element of the domain has *exactly* one image element and every element of the codomain has *exactly* one preimage element. For example, the green binary relation in the diagram is a bijection, but the red one is not.

If relations over proper classes are allowed:

- **Set-like** (also called **local**): for all x ∈ X {\displaystyle x\in X} ({\displaystyle x\in X}), the class of all y ∈ Y {\displaystyle y\in Y} ({\displaystyle y\in Y}) such that y R x {\displaystyle yRx} ({\displaystyle yRx}), i.e. { y ∈ Y , y R x } {\displaystyle \{y\in Y,yRx\}} ({\displaystyle \{y\in Y,yRx\}}), is a set. For example, the relation ∈ {\displaystyle \in } ({\displaystyle \in }) is set-like, and every relation on two sets is set-like. The usual ordering < over the class of ordinal numbers is a set-like relation, while its inverse > is not.


## Sets versus classes

Certain mathematical "relations", such as "equal to", "subset of", and "member of", cannot be understood to be binary relations as defined above, because their domains and codomains cannot be taken to be sets in the usual systems of axiomatic set theory. For example, to model the general concept of "equality" as a binary relation = {\displaystyle =} ({\displaystyle =}), take the domain and codomain to be the "class of all sets", which is not a set in the usual set theory.

In most mathematical contexts, references to the relations of equality, membership and subset are harmless because they can be understood implicitly to be restricted to some set in the context. The usual work-around to this problem is to select a "large enough" set A {\displaystyle A} ({\displaystyle A}), that contains all the objects of interest, and work with the restriction = A {\displaystyle =_{A}} ({\displaystyle =_{A}}) instead of = {\displaystyle =} ({\displaystyle =}). Similarly, the "subset of" relation ⊆ {\displaystyle \subseteq } ({\displaystyle \subseteq }) needs to be restricted to have domain and codomain P ( A ) {\displaystyle P(A)} ({\displaystyle P(A)}) (the power set of a specific set A {\displaystyle A} ({\displaystyle A})): the resulting set relation can be denoted by ⊆ A . {\displaystyle \subseteq _{A}.} ({\displaystyle \subseteq _{A}.}) Also, the "member of" relation needs to be restricted to have domain A {\displaystyle A} ({\displaystyle A}) and codomain P ( A ) {\displaystyle P(A)} ({\displaystyle P(A)}) to obtain a binary relation ∈ A {\displaystyle \in _{A}} ({\displaystyle \in _{A}}) that is a set. Bertrand Russell has shown that assuming ∈ {\displaystyle \in } ({\displaystyle \in }) to be defined over all sets leads to a contradiction in naive set theory, see *Russell's paradox*.

Another solution to this problem is to use a set theory with proper classes, such as NBG or Morse–Kelley set theory, and allow the domain and codomain (and so the graph) to be proper classes: in such a theory, equality, membership, and subset are binary relations without special comment. (A minor modification needs to be made to the concept of the ordered triple ( X , Y , G ) {\displaystyle (X,Y,G)} ({\displaystyle (X,Y,G)}), as normally a proper class cannot be a member of an ordered tuple; or of course one can identify the binary relation with its graph in this context.) With this definition one can for instance define a binary relation over every set and its power set.


## Homogeneous relation

A **homogeneous relation** over a set X {\displaystyle X} ({\displaystyle X}) is a binary relation over X {\displaystyle X} ({\displaystyle X}) and itself, i.e. it is a subset of the Cartesian product X × X . {\displaystyle X\times X.} ({\displaystyle X\times X.}) It is also simply called a (binary) relation over X {\displaystyle X} ({\displaystyle X}).

A homogeneous relation R {\displaystyle R} ({\displaystyle R}) over a set X {\displaystyle X} ({\displaystyle X}) may be identified with a directed simple graph permitting loops, where X {\displaystyle X} ({\displaystyle X}) is the vertex set and R {\displaystyle R} ({\displaystyle R}) is the edge set (there is an edge from a vertex x {\displaystyle x} ({\displaystyle x}) to a vertex y {\displaystyle y} ({\displaystyle y}) if and only if x R y {\displaystyle xRy} ({\displaystyle xRy})). The set of all homogeneous relations B ( X ) {\displaystyle {\mathcal {B}}(X)} ({\displaystyle {\mathcal {B}}(X)}) over a set X {\displaystyle X} ({\displaystyle X}) is the power set 2 X × X {\displaystyle 2^{X\times X}} ({\displaystyle 2^{X\times X}}) which is a Boolean algebra augmented with the involution of mapping of a relation to its converse relation. Considering composition of relations as a binary operation on B ( X ) {\displaystyle {\mathcal {B}}(X)} ({\displaystyle {\mathcal {B}}(X)}), it forms a semigroup with involution.

Some important properties that a homogeneous relation R {\displaystyle R} ({\displaystyle R}) over a set X {\displaystyle X} ({\displaystyle X}) may have are:

- *Reflexive*: for all x ∈ X , {\displaystyle x\in X,} ({\displaystyle x\in X,}) x R x {\displaystyle xRx} ({\displaystyle xRx}). For example, ≥ {\displaystyle \geq } ({\displaystyle \geq }) is a reflexive relation but > is not.
- *Irreflexive*: for all x ∈ X , {\displaystyle x\in X,} ({\displaystyle x\in X,}) not x R x {\displaystyle xRx} ({\displaystyle xRx}). For example, > {\displaystyle >} ({\displaystyle >}) is an irreflexive relation, but ≥ {\displaystyle \geq } ({\displaystyle \geq }) is not.
- *Symmetric*: for all x , y ∈ X , {\displaystyle x,y\in X,} ({\displaystyle x,y\in X,}) if x R y {\displaystyle xRy} ({\displaystyle xRy}) then y R x {\displaystyle yRx} ({\displaystyle yRx}). For example, "is a blood relative of" is a symmetric relation.
- *Antisymmetric*: for all x , y ∈ X , {\displaystyle x,y\in X,} ({\displaystyle x,y\in X,}) if x R y {\displaystyle xRy} ({\displaystyle xRy}) and y R x {\displaystyle yRx} ({\displaystyle yRx}) then x = y . {\displaystyle x=y.} ({\displaystyle x=y.}) For example, ≥ {\displaystyle \geq } ({\displaystyle \geq }) is an antisymmetric relation.
- *Asymmetric*: for all x , y ∈ X , {\displaystyle x,y\in X,} ({\displaystyle x,y\in X,}) if x R y {\displaystyle xRy} ({\displaystyle xRy}) then not y R x {\displaystyle yRx} ({\displaystyle yRx}). A relation is asymmetric if and only if it is both antisymmetric and irreflexive. For example, > is an asymmetric relation, but ≥ {\displaystyle \geq } ({\displaystyle \geq }) is not.
- *Transitive*: for all x , y , z ∈ X , {\displaystyle x,y,z\in X,} ({\displaystyle x,y,z\in X,}) if x R y {\displaystyle xRy} ({\displaystyle xRy}) and y R z {\displaystyle yRz} ({\displaystyle yRz}) then x R z {\displaystyle xRz} ({\displaystyle xRz}). A transitive relation is irreflexive if and only if it is asymmetric. For example, "is ancestor of" is a transitive relation, while "is parent of" is not.
- *Connected*: for all x , y ∈ X , {\displaystyle x,y\in X,} ({\displaystyle x,y\in X,}) if x ≠ y {\displaystyle x\neq y} ({\displaystyle x\neq y}) then x R y {\displaystyle xRy} ({\displaystyle xRy}) or y R x {\displaystyle yRx} ({\displaystyle yRx}).
- *Strongly connected*: for all x , y ∈ X , {\displaystyle x,y\in X,} ({\displaystyle x,y\in X,}) x R y {\displaystyle xRy} ({\displaystyle xRy}) or y R x {\displaystyle yRx} ({\displaystyle yRx}).
- *Dense*: for all x , y ∈ X , {\displaystyle x,y\in X,} ({\displaystyle x,y\in X,}) if x R y , {\displaystyle xRy,} ({\displaystyle xRy,}) then some z ∈ X {\displaystyle z\in X} ({\displaystyle z\in X}) exists such that x R z {\displaystyle xRz} ({\displaystyle xRz}) and z R y {\displaystyle zRy} ({\displaystyle zRy}).

A *partial order* is a relation that is reflexive, antisymmetric, and transitive. A *strict partial order* is a relation that is irreflexive, asymmetric, and transitive. A *total order* is a relation that is reflexive, antisymmetric, transitive and connected. A *strict total order* is a relation that is irreflexive, asymmetric, transitive and connected. An *equivalence relation* is a relation that is reflexive, symmetric, and transitive. For example, " x {\displaystyle x} ({\displaystyle x}) divides y {\displaystyle y} ({\displaystyle y})" is a partial, but not a total order on natural numbers N , {\displaystyle \mathbb {N} ,} ({\displaystyle \mathbb {N} ,}) " x < y {\displaystyle x<y} ({\displaystyle x<y})" is a strict total order on N , {\displaystyle \mathbb {N} ,} ({\displaystyle \mathbb {N} ,}) and " x {\displaystyle x} ({\displaystyle x}) is parallel to y {\displaystyle y} ({\displaystyle y})" is an equivalence relation on the set of all lines in the Euclidean plane.

All operations defined in section § Operations also apply to homogeneous relations. Beyond that, a homogeneous relation over a set X {\displaystyle X} ({\displaystyle X}) may be subjected to closure operations like:

***Reflexive closure***

the smallest reflexive relation over

X

{\displaystyle X}

containing

R

{\displaystyle R}

,

***Transitive closure***

the smallest transitive relation over

X

{\displaystyle X}

containing

R

{\displaystyle R}

,

***Equivalence closure***

the smallest

equivalence relation

over

X

{\displaystyle X}

containing

R

{\displaystyle R}

.
