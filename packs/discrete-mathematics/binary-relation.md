---
title: "Binary relation"
source: https://en.wikipedia.org/wiki/Binary_relation
domain: discrete-mathematics
license: CC-BY-SA-4.0
tags: discrete math, discrete mathematics, combinatorics, graph theory, set theory, permutation
fetched: 2026-07-02
---

# Binary relation

| Transitive binary relations |
|---|
| Symmetric Antisymmetric Connected Well-founded Has joins Has meets Reflexive Irreflexive Asymmetric Total, Semiconnex Anti- reflexive Equivalence relation (Green tick)Y ✗ ✗ ✗ ✗ ✗ (Green tick)Y ✗ ✗ Preorder (Quasiorder) ✗ ✗ ✗ ✗ ✗ ✗ (Green tick)Y ✗ ✗ Partial order ✗ (Green tick)Y ✗ ✗ ✗ ✗ (Green tick)Y ✗ ✗ Total preorder ✗ ✗ (Green tick)Y ✗ ✗ ✗ (Green tick)Y ✗ ✗ Total order ✗ (Green tick)Y (Green tick)Y ✗ ✗ ✗ (Green tick)Y ✗ ✗ Prewellordering ✗ ✗ (Green tick)Y (Green tick)Y ✗ ✗ (Green tick)Y ✗ ✗ Well-quasi-ordering ✗ ✗ ✗ (Green tick)Y ✗ ✗ (Green tick)Y ✗ ✗ Well-ordering ✗ (Green tick)Y (Green tick)Y (Green tick)Y ✗ ✗ (Green tick)Y ✗ ✗ Lattice ✗ (Green tick)Y ✗ ✗ (Green tick)Y (Green tick)Y (Green tick)Y ✗ ✗ Join-semilattice ✗ (Green tick)Y ✗ ✗ (Green tick)Y ✗ (Green tick)Y ✗ ✗ Meet-semilattice ✗ (Green tick)Y ✗ ✗ ✗ (Green tick)Y (Green tick)Y ✗ ✗ Strict partial order ✗ (Green tick)Y ✗ ✗ ✗ ✗ ✗ (Green tick)Y (Green tick)Y Strict weak order ✗ (Green tick)Y ✗ ✗ ✗ ✗ ✗ (Green tick)Y (Green tick)Y Strict total order ✗ (Green tick)Y (Green tick)Y ✗ ✗ ✗ ✗ (Green tick)Y (Green tick)Y Symmetric Antisymmetric Connected Well-founded Has joins Has meets Reflexive Irreflexive Asymmetric Definitions, for all $a,b$ and $S\neq \varnothing :$ ${\begin{aligned}&aRb\\\Rightarrow {}&bRa\end{aligned}}$ ${\begin{aligned}aRb{\text{ and }}&bRa\\\Rightarrow a={}&b\end{aligned}}$ ${\begin{aligned}a\neq {}&b\Rightarrow \\aRb{\text{ or }}&bRa\end{aligned}}$ ${\begin{aligned}\min S\\{\text{exists}}\end{aligned}}$ ${\begin{aligned}a\vee b\\{\text{exists}}\end{aligned}}$ ${\begin{aligned}a\wedge b\\{\text{exists}}\end{aligned}}$ $aRa$ ${\text{not }}aRa$ ${\begin{aligned}aRb\Rightarrow \\{\text{not }}bRa\end{aligned}}$ |
| (Green tick)Y indicates that the column's property is always true for the row's term (at the very left), while ✗ indicates that the property is not guaranteed in general (it might, or might not, hold). For example, that every equivalence relation is symmetric, but not necessarily antisymmetric, is indicated by (Green tick)Y in the "Symmetric" column and ✗ in the "Antisymmetric" column, respectively. All definitions tacitly require the homogeneous relation R be transitive: for all $a,b,c,$ if $aRb$ and $bRc$ then $aRc.$ A term's definition may require additional properties that are not listed in this table. |

In mathematics, a **binary relation** associates some elements of one set called the *domain* with some elements of another set (possibly the same) called the *codomain*. Precisely, a binary relation over sets X and Y is a set of ordered pairs $(x,y)$ , where x is an element of X and y is an element of Y . It encodes the common concept of relation: an element x is *related* to an element y if and only if the pair $(x,y)$ belongs to the set of ordered pairs that defines the binary relation.

An example of a binary relation is the "divides" relation over the set of prime numbers $\mathbb {P}$ and the set of integers $\mathbb {Z}$ , in which each prime p is related to each integer z that is a multiple of p , but not to an integer that is not a multiple of p . In this relation, for instance, the prime number 2 is related to numbers such as $-4$ , 0 , 6 , $10$ , but not to 1 or 9 , just as the prime number 3 is related to 0 , 6 , and 9 , but not to 4 or $13$ .

A binary relation is called a homogeneous relation when $X=Y$ . A binary relation is also called a *heterogeneous relation* when it is not necessary that $X=Y$ .

Binary relations, and especially homogeneous relations, are used in many branches of mathematics to model a wide variety of concepts. These include, among others:

- the "is greater than", "is equal to", and "divides" relations in arithmetic;
- the "is congruent to" relation in geometry;
- the "is adjacent to" relation in graph theory;
- the "is orthogonal to" relation in linear algebra.

A function may be defined as a binary relation that meets additional constraints. Binary relations are also heavily used in computer science.

A binary relation over sets X and Y can be identified with an element of the power set of the Cartesian product $X\times Y.$ Since a powerset is a lattice for set inclusion ( $\subseteq$ ), relations can be manipulated using set operations (union, intersection, and complementation) and algebra of sets.

In some systems of axiomatic set theory, relations are extended to classes, which are generalizations of sets. This extension is needed for, among other things, modeling the concepts of "is an element of" or "is a subset of" in set theory, without running into logical inconsistencies such as Russell's paradox.

A binary relation is the most studied special case $n=2$ of an n -ary relation over sets $X_{1},\dots ,X_{n}$ , which is a subset of the Cartesian product $X_{1}\times \cdots \times X_{n}.$

## Definition

Given sets X and Y , the Cartesian product $X\times Y$ is defined as $\{(x,y)\mid x\in X{\text{ and }}y\in Y\},$ and its elements are called *ordered pairs*.

A *binary relation* R over sets X and Y is a subset of $X\times Y.$ The set X is called the *domain* or *set of departure* of R , and the set Y the *codomain* or *set of destination* of R . In order to specify the choices of the sets X and Y , some authors define a *binary relation* or *correspondence* as an ordered triple $(X,Y,G)$ , where G is a subset of $X\times Y$ called the *graph* of the binary relation. The statement $(x,y)\in R$ reads " x is R -related to y " and is denoted by $xRy$ . The *domain of definition* or *active domain* of R is the set of all x such that $xRy$ for at least one y . The *codomain of definition*, *active codomain*, *image* or *range* of R is the set of all y such that $xRy$ for at least one x . The *field* of R is the union of its domain of definition and its codomain of definition.

When $X=Y,$ a binary relation is called a *homogeneous relation* (or *endorelation*). To emphasize the fact that X and Y are allowed to be different, a binary relation is also called a **heterogeneous relation**. The prefix *hetero* is from the Greek ἕτερος (*heteros*, "other, another, different").

A heterogeneous relation has been called a **rectangular relation**, suggesting that it does not have the square-like symmetry of a homogeneous relation on a set where $A=B.$ Commenting on the development of binary relations beyond homogeneous relations, researchers wrote, "... a variant of the theory has evolved that treats relations from the very beginning as *heterogeneous* or *rectangular*, i.e. as relations where the normal case is that they are relations between different sets."

The terms *correspondence*, **dyadic relation** and **two-place relation** are synonyms for binary relation, though some authors use the term "binary relation" for any subset of a Cartesian product $X\times Y$ without reference to X and Y , and reserve the term "correspondence" for a binary relation with reference to X and Y .

In a binary relation, the order of the elements is important; if $x\neq y$ then $yRx$ can be true or false independently of $xRy$ . For example, 3 divides 9 , but 9 does not divide 3 .

## Operations

### Union

If R and S are binary relations over sets X and Y then $R\cup S=\{(x,y)\mid xRy{\text{ or }}xSy\}$ is the *union relation* of R and S over X and Y .

The identity element is the empty relation, in which no x is related to any y .

For example, $\leq$ is the union of < and = , and $\geq$ is the union of > and = .

### Intersection

If R and S are binary relations over sets X and Y then $R\cap S=\{(x,y)\mid xRy{\text{ and }}xSy\}$ is the *intersection relation* of R and S over X and Y .

The identity element is the universal relation, in which every x is related to every y .

For example, the relation "is divisible by 6" is the intersection of the relations "is divisible by 3" and "is divisible by 2".

### Composition

If R is a binary relation over sets X and Y , and S is a binary relation over sets Y and Z then $S\circ R=\{(x,z)\mid {\text{ there exists }}y\in Y{\text{ such that }}xRy{\text{ and }}ySz\}$ (also denoted by $R;S$ ) is the *composition relation* of R and S over X and Z .

If $X=Y=Z$ , the identity element w.r.t. composition is the identity relation on X , in which $x\in X$ is related only to itself.

The order of R and S in the notation $S\circ R$ used here agrees with the standard notational order for composition of functions. For example, the composition (is parent of) $\circ$ (is mother of) yields (is grandmother of), while the composition (is mother of) $\circ$ (is parent of) yields (is maternal grandparent of). For the latter case, if x is the parent of y and y is the mother of z , then x is the maternal grandparent of z .

### Converse

If R is a binary relation over sets X and Y then $R^{\textsf {T}}=\{(y,x)\mid xRy\}$ is the *converse relation*, also called *inverse relation*, of R over Y and X .

For example, = is the converse of itself, as is $\neq$ , and < and > are each other's converse, as are $\leq$ and $\geq .$ A binary relation is equal to its converse if and only if it is symmetric.

### Complement

If R is a binary relation over sets X and Y then ${\bar {R}}=\{(x,y)\mid \neg xRy\}$ (also denoted by $\neg R$ ) is the *complementary relation* of R over X and Y .

For example, = and $\neq$ are each other's complement, as are $\subseteq$ and $\not \subseteq$ , $\supseteq$ and $\not \supseteq$ , $\in$ and $\not \in$ , and for total orders also < and $\geq$ , and > and $\leq$ .

The complement of the converse relation $R^{\textsf {T}}$ is the converse of the complement: ${\overline {R^{\mathsf {T}}}}={\bar {R}}^{\mathsf {T}}.$

If $X=Y,$ the complement has the following properties:

- If a relation is symmetric, then so is the complement.
- The complement of a reflexive relation is irreflexive—and vice versa.
- The complement of a strict weak order is a total preorder—and vice versa.

### Restriction

If R is a binary homogeneous relation over a set X and S is a subset of X then $R_{\vert S}=\{(x,y)\mid xRy{\text{ and }}x\in S{\text{ and }}y\in S\}$ is the *restriction relation* of R to S over X .

If R is a binary relation over sets X and Y and if S is a subset of X then $R_{\vert S}=\{(x,y)\mid xRy{\text{ and }}x\in S\}$ is the *left-restriction relation* of R to S over X and Y .

If a relation is reflexive, irreflexive, symmetric, antisymmetric, asymmetric, transitive, total, trichotomous, a partial order, total order, strict weak order, total preorder (weak order), or an equivalence relation, then so too are its restrictions.

However, the transitive closure of a restriction is a subset of the restriction of the transitive closure, i.e., in general not equal. For example, restricting the relation " x is parent of y " to females yields the relation " x is mother of the woman y "; its transitive closure does not relate a woman with her paternal grandmother. On the other hand, the transitive closure of "is parent of" is "is ancestor of"; its restriction to females does relate a woman with her paternal grandmother.

Also, the various concepts of completeness (not to be confused with being "total") do not carry over to restrictions. For example, over the real numbers a property of the relation $\leq$ is that every non-empty subset $S\subseteq \mathbb {R}$ with an upper bound in $\mathbb {R}$ has a least upper bound (also called supremum) in $\mathbb {R} .$ However, for the rational numbers this supremum is not necessarily rational, so the same property does not hold on the restriction of the relation $\leq$ to the rational numbers.

A binary relation R over sets X and Y is said to be *contained in* a relation S over X and Y , written $R\subseteq S,$ if R is a subset of S , that is, for all $x\in X$ and $y\in Y,$ if $xRy$ , then $xSy$ . If R is contained in S and S is contained in R , then R and S are called *equal* written $R=S$ . If R is contained in S but S is not contained in R , then R is said to be *smaller* than S , written $R\subsetneq S.$ For example, on the rational numbers, the relation > is smaller than $\geq$ , and equal to the composition $>\circ >$ .

### Matrix representation

Binary relations over sets X and Y can be represented algebraically by logical matrices indexed by X and Y with entries in the Boolean semiring (addition corresponds to OR and multiplication to AND) where matrix addition corresponds to union of relations, matrix multiplication corresponds to composition of relations (of a relation over X and Y and a relation over Y and Z ), the Hadamard product corresponds to intersection of relations, the zero matrix corresponds to the empty relation, and the matrix of ones corresponds to the universal relation. Homogeneous relations (when $X=Y$ ) form a matrix semiring (indeed, a matrix semialgebra over the Boolean semiring) where the identity matrix corresponds to the identity relation.

## Examples

| A B | ball | car | doll | cup |
|---|---|---|---|---|
| John | **+** | − | − | − |
| Mary | − | − | **+** | − |
| Venus | − | **+** | − | − |

| A B | ball | car | doll | cup |
|---|---|---|---|---|
| John | **+** | − | − | − |
| Mary | − | − | **+** | − |
| Ian | − | − | − | − |
| Venus | − | **+** | − | − |

1. The following example shows that the choice of codomain is important. Suppose there are four objects $A=\{{\text{ball, car, doll, cup}}\}$ and four people $B=\{{\text{John, Mary, Ian, Venus}}\}.$ A possible relation on A and B is the relation "is owned by", given by $R=\{({\text{ball, John}}),({\text{doll, Mary}}),({\text{car, Venus}})\}.$ That is, John owns the ball, Mary owns the doll, and Venus owns the car. Nobody owns the cup and Ian owns nothing; see the 1st example. As a set, R does not involve Ian, and therefore R could have been viewed as a subset of $A\times \{{\text{John, Mary, Venus}}\},$ i.e. a relation over A and $\{{\text{John, Mary, Venus}}\};$ see the 2nd example. But in that second example, R contains no information about the ownership by Ian. While the 2nd example relation is surjective (see below), the 1st is not. Ocean borders continent NA SA AF EU AS AU AA Indian 0 0 1 0 1 1 1 Arctic 1 0 0 1 1 0 0 Atlantic 1 1 1 1 0 0 1 Pacific 1 1 0 0 1 1 1
2. Let $A=\{{\text{Indian}},{\text{Arctic}},{\text{Atlantic}},{\text{Pacific}}\}$ , the oceans of the globe, and $B=\{{\text{NA}},{\text{SA}},{\text{AF}},{\text{EU}},{\text{AS}},{\text{AU}},{\text{AA}}\}$ , the continents. Let $aRb$ represent that ocean a borders continent b . Then the logical matrix for this relation is: $R={\begin{pmatrix}0&0&1&0&1&1&1\\1&0&0&1&1&0&0\\1&1&1&1&0&0&1\\1&1&0&0&1&1&1\end{pmatrix}}.$ The connectivity of the planet Earth can be viewed through $RR^{\mathsf {T}}$ and $R^{\mathsf {T}}R$ , the former being a $4\times 4$ relation on A , which is the universal relation ( $A\times A$ or a logical matrix of all ones). This universal relation reflects the fact that every ocean is separated from the others by at most one continent. On the other hand, $R^{\mathsf {T}}R$ is a relation on $B\times B$ which *fails* to be universal because at least two oceans must be traversed to voyage from Europe to Australia.
3. Visualization of relations leans on graph theory: For relations on a set (homogeneous relations), a directed graph illustrates a relation and a graph a symmetric relation. For heterogeneous relations a hypergraph has edges possibly with more than two nodes, and can be illustrated by a bipartite graph. Just as the clique is integral to relations on a set, so bicliques are used to describe heterogeneous relations; indeed, they are the "concepts" that generate a lattice associated with a relation.
4. Hyperbolic orthogonality: Time and space are different categories, and temporal properties are separate from spatial properties. The idea of *simultaneous events* is simple in absolute space and time since each time t determines a simultaneous hyperplane in that cosmology. Hermann Minkowski changed that when he articulated the notion of *relative simultaneity*, which exists when spatial events are "normal" to a time characterized by a velocity. He used an indefinite inner product, and specified that a time vector is normal to a space vector when that product is zero. The indefinite inner product in a composition algebra is given by $\langle x,z\rangle =x{\bar {z}}+{\bar {x}}z\;$ where the overbar denotes conjugation. As a relation between some temporal events and some spatial events, hyperbolic orthogonality (as found in split-complex numbers) is a heterogeneous relation.
5. A geometric configuration can be considered a relation between its points and its lines. The relation is expressed as incidence. Finite and infinite projective and affine planes are included. Jakob Steiner pioneered the cataloguing of configurations with the Steiner systems $\operatorname {S} (t,k,n)$ which have an n-element set $\operatorname {S}$ and a set of k-element subsets called **blocks**, such that a subset with t elements lies in just one block. These incidence structures have been generalized with block designs. The incidence matrix used in these geometrical contexts corresponds to the logical matrix used generally with binary relations. An incidence structure is a triple $\mathbf {D} =(V,\mathbf {B} ,I)$ where V and $\mathbf {B}$ are any two disjoint sets and I is a binary relation between V and $\mathbf {B}$ , i.e. $I\subseteq V\times \mathbf {B} .$ The elements of V will be called *points*, those of $\mathbf {B}$ *blocks*, and those of I *flags*.

## Types of binary relations

Some important types of binary relations R over sets X and Y are listed below.

Uniqueness properties:

- **Injective** (also called **left-unique**): for all $x,y\in X$ and all $z\in Y,$ if $xRz$ and $yRz$ then $x=y$ . In other words, every element of the codomain has *at most* one preimage element. For such a relation, Y is called *a primary key* of R . For example, the green and blue binary relations in the diagram are injective, but the red one is not (as it relates both $-1$ and 1 to 1 ), nor the black one (as it relates both $-1$ and 1 to 0 ).
- **Functional** (also called **right-unique** or **univalent**): for all $x\in X$ and all $y,z\in Y,$ if $xRy$ and $xRz$ then $y=z$ . In other words, every element of the domain has *at most* one image element. Such a binary relation is called a *partial function* or *partial mapping*. For such a relation, $\{X\}$ is called *a primary key* of R . For example, the red and green binary relations in the diagram are functional, but the blue one is not (as it relates 1 to both 1 and $-1$ ), nor the black one (as it relates 0 to both $-1$ and 1 ).
- **One-to-one**: injective and functional. For example, the green binary relation in the diagram is one-to-one, but the red, blue and black ones are not.
- **One-to-many**: injective and not functional. For example, the blue binary relation in the diagram is one-to-many, but the red, green and black ones are not.
- **Many-to-one**: functional and not injective. For example, the red binary relation in the diagram is many-to-one, but the green, blue and black ones are not.
- **Many-to-many**: not injective nor functional. For example, the black binary relation in the diagram is many-to-many, but the red, green and blue ones are not.

Totality properties (only definable if the domain X and codomain Y are specified):

- **Total** (also called **left-total**): for all $x\in X$ there exists a $y\in Y$ such that $xRy$ . In other words, every element of the domain has *at least* one image element. In other words, the domain of definition of R is equal to X . This property, is different from the definition of *connected* (also called *total* by some authors) in Properties. Such a binary relation is called a *multivalued function*. For example, the red and green binary relations in the diagram are total, but the blue one is not (as it does not relate $-1$ to any real number), nor the black one (as it does not relate 2 to any real number). As another example, > is a total relation over the integers. But it is not a total relation over the positive integers, because there is no y in the positive integers such that $1>y$ . However, < is a total relation over the positive integers, the rational numbers and the real numbers. Every reflexive relation is total: for a given x , choose $y=x$ .
- **Surjective** (also called **right-total**): for all $y\in Y$ , there exists an $x\in X$ such that $xRy$ . In other words, every element of the codomain has *at least* one preimage element. In other words, the codomain of definition of R is equal to Y . For example, the green and blue binary relations in the diagram are surjective, but the red one is not (as it does not relate any real number to $-1$ ), nor the black one (as it does not relate any real number to 2 ).

Uniqueness and totality properties (only definable if the domain X and codomain Y are specified):

- A **function** (also called **mapping**): a binary relation that is functional and total. In other words, every element of the domain has *exactly* one image element. For example, the red and green binary relations in the diagram are functions, but the blue and black ones are not.
  - An **injection**: a function that is injective. For example, the green relation in the diagram is an injection, but the red one is not; the black and the blue relation is not even a function.
  - A **surjection**: a function that is surjective. For example, the green relation in the diagram is a surjection, but the red one is not.
  - A **bijection**: a function that is injective and surjective. In other words, every element of the domain has *exactly* one image element and every element of the codomain has *exactly* one preimage element. For example, the green binary relation in the diagram is a bijection, but the red one is not.

If relations over proper classes are allowed:

- **Set-like** (also called **local**): for all $x\in X$ , the class of all $y\in Y$ such that $yRx$ , i.e. $\{y\in Y,yRx\}$ , is a set. For example, the relation $\in$ is set-like, and every relation on two sets is set-like. The usual ordering < over the class of ordinal numbers is a set-like relation, while its inverse > is not.

## Sets versus classes

Certain mathematical "relations", such as "equal to", "subset of", and "member of", cannot be understood to be binary relations as defined above, because their domains and codomains cannot be taken to be sets in the usual systems of axiomatic set theory. For example, to model the general concept of "equality" as a binary relation = , take the domain and codomain to be the "class of all sets", which is not a set in the usual set theory.

In most mathematical contexts, references to the relations of equality, membership and subset are harmless because they can be understood implicitly to be restricted to some set in the context. The usual work-around to this problem is to select a "large enough" set A , that contains all the objects of interest, and work with the restriction $=_{A}$ instead of = . Similarly, the "subset of" relation $\subseteq$ needs to be restricted to have domain and codomain $P(A)$ (the power set of a specific set A ): the resulting set relation can be denoted by $\subseteq _{A}.$ Also, the "member of" relation needs to be restricted to have domain A and codomain $P(A)$ to obtain a binary relation $\in _{A}$ that is a set. Bertrand Russell has shown that assuming $\in$ to be defined over all sets leads to a contradiction in naive set theory, see *Russell's paradox*.

Another solution to this problem is to use a set theory with proper classes, such as NBG or Morse–Kelley set theory, and allow the domain and codomain (and so the graph) to be proper classes: in such a theory, equality, membership, and subset are binary relations without special comment. (A minor modification needs to be made to the concept of the ordered triple $(X,Y,G)$ , as normally a proper class cannot be a member of an ordered tuple; or of course one can identify the binary relation with its graph in this context.) With this definition one can for instance define a binary relation over every set and its power set.

## Homogeneous relation

A **homogeneous relation** over a set X is a binary relation over X and itself, i.e. it is a subset of the Cartesian product $X\times X.$ It is also simply called a (binary) relation over X .

A homogeneous relation R over a set X may be identified with a directed simple graph permitting loops, where X is the vertex set and R is the edge set (there is an edge from a vertex x to a vertex y if and only if $xRy$ ). The set of all homogeneous relations ${\mathcal {B}}(X)$ over a set X is the power set $2^{X\times X}$ which is a Boolean algebra augmented with the involution of mapping of a relation to its converse relation. Considering composition of relations as a binary operation on ${\mathcal {B}}(X)$ , it forms a semigroup with involution.

Some important properties that a homogeneous relation R over a set X may have are:

- *Reflexive*: for all $x\in X,$ $xRx$ . For example, $\geq$ is a reflexive relation but > is not.
- *Irreflexive*: for all $x\in X,$ not $xRx$ . For example, > is an irreflexive relation, but $\geq$ is not.
- *Symmetric*: for all $x,y\in X,$ if $xRy$ then $yRx$ . For example, "is a blood relative of" is a symmetric relation.
- *Antisymmetric*: for all $x,y\in X,$ if $xRy$ and $yRx$ then $x=y.$ For example, $\geq$ is an antisymmetric relation.
- *Asymmetric*: for all $x,y\in X,$ if $xRy$ then not $yRx$ . A relation is asymmetric if and only if it is both antisymmetric and irreflexive. For example, > is an asymmetric relation, but $\geq$ is not.
- *Transitive*: for all $x,y,z\in X,$ if $xRy$ and $yRz$ then $xRz$ . A transitive relation is irreflexive if and only if it is asymmetric. For example, "is ancestor of" is a transitive relation, while "is parent of" is not.
- *Connected*: for all $x,y\in X,$ if $x\neq y$ then $xRy$ or $yRx$ .
- *Strongly connected*: for all $x,y\in X,$ $xRy$ or $yRx$ .
- *Dense*: for all $x,y\in X,$ if $xRy,$ then some $z\in X$ exists such that $xRz$ and $zRy$ .

A *partial order* is a relation that is reflexive, antisymmetric, and transitive. A *strict partial order* is a relation that is irreflexive, asymmetric, and transitive. A *total order* is a relation that is reflexive, antisymmetric, transitive and connected. A *strict total order* is a relation that is irreflexive, asymmetric, transitive and connected. An *equivalence relation* is a relation that is reflexive, symmetric, and transitive. For example, " x divides y " is a partial, but not a total order on natural numbers $\mathbb {N} ,$ " $x<y$ " is a strict total order on $\mathbb {N} ,$ and " x is parallel to y " is an equivalence relation on the set of all lines in the Euclidean plane.

All operations defined in section § Operations also apply to homogeneous relations. Beyond that, a homogeneous relation over a set X may be subjected to closure operations like:

***Reflexive closure***

the smallest reflexive relation over

X

containing

R

,

***Transitive closure***

the smallest transitive relation over

X

containing

R

,

***Equivalence closure***

the smallest

equivalence relation

over

X

containing

R

.

## Calculus of relations

Developments in algebraic logic have facilitated usage of binary relations. The calculus of relations includes the algebra of sets, extended by composition of relations and the use of converse relations. The inclusion $R\subseteq S,$ meaning that $aRb$ implies $aSb$ , sets the scene in a lattice of relations. But since $P\subseteq Q\equiv (P\cap {\bar {Q}}=\varnothing )\equiv (P\cap Q=P),$ the inclusion symbol is superfluous. Nevertheless, composition of relations and manipulation of the operators according to Schröder rules, provides a calculus to work in the power set of $A\times B.$

In contrast to homogeneous relations, the composition of relations operation is only a partial function. The necessity of matching target to source of composed relations has led to the suggestion that the study of heterogeneous relations is a chapter of category theory as in the category of sets, except that the morphisms of this category are relations. The *objects* of the category Rel are sets, and the relation-morphisms compose as required in a category.

## Induced concept lattice

Binary relations have been described through their induced concept lattices: A **concept** $C\subset R$ satisfies two properties:

- The logical matrix of C is the outer product of logical vectors $C_{ij}=u_{i}v_{j},\quad u,v$ logical vectors.
- C is maximal, not contained in any other outer product. Thus C is described as a *non-enlargeable rectangle*.

For a given relation $R\subseteq X\times Y,$ the set of concepts, enlarged by their joins and meets, forms an "induced lattice of concepts", with inclusion $\sqsubseteq$ forming a preorder.

The MacNeille completion theorem (1937) (that any partial order may be embedded in a complete lattice) is cited in a 2013 survey article "Decomposition of relations on concept lattices". The decomposition is

$R=fEg^{\textsf {T}}$

, where

f

and

g

are

functions

, called

mappings

or left-total, functional relations in this context. The "induced concept lattice is isomorphic to the cut completion of the partial order

E

that belongs to the minimal decomposition

$(f,g,E)$

of the relation

R

."

Particular cases are considered below: E total order corresponds to Ferrers type, and E identity corresponds to difunctional, a generalization of equivalence relation on a set.

Relations may be ranked by the **Schein rank** which counts the number of concepts necessary to cover a relation. Structural analysis of relations with concepts provides an approach for data mining.

## Particular relations

- *Proposition*: If R is a surjective relation and $R^{\mathsf {T}}$ is its transpose, then $I\subseteq R^{\textsf {T}}R$ where I is the $m\times m$ identity relation.
- *Proposition*: If R is a serial relation, then $I\subseteq RR^{\textsf {T}}$ where I is the $n\times n$ identity relation.

### Difunctional

The idea of a difunctional relation is to partition objects by distinguishing attributes, as a generalization of the concept of an equivalence relation. One way this can be done is with an intervening set $Z=\{x,y,z,\ldots \}$ of indicators. The partitioning relation $R=FG^{\textsf {T}}$ is a composition of relations using *functional* relations $F\subseteq A\times Z{\text{ and }}G\subseteq B\times Z.$ Jacques Riguet named these relations **difunctional** since the composition $FG^{\mathsf {T}}$ involves functional relations, commonly called *partial functions*.

In 1950 Riguet showed that such relations satisfy the inclusion:

$RR^{\textsf {T}}R\subseteq R$

In automata theory, the term **rectangular relation** has also been used to denote a difunctional relation. This terminology recalls the fact that, when represented as a logical matrix, the columns and rows of a difunctional relation can be arranged as a block matrix with rectangular blocks of ones on the (asymmetric) main diagonal. More formally, a relation R on $X\times Y$ is difunctional if and only if it can be written as the union of Cartesian products $A_{i}\times B_{i}$ , where the $A_{i}$ are a partition of a subset of X and the $B_{i}$ likewise a partition of a subset of Y .

Using the notation $\{y\mid xRy\}=xR$ , a difunctional relation can also be characterized as a relation R such that wherever $x_{1}R$ and $x_{2}R$ have a non-empty intersection, then these two sets coincide; formally $x_{1}\cap x_{2}\neq \varnothing$ implies $x_{1}R=x_{2}R.$

In 1997 researchers found "utility of binary decomposition based on difunctional dependencies in database management." Furthermore, difunctional relations are fundamental in the study of bisimulations.

In the context of homogeneous relations, a partial equivalence relation is difunctional.

### Ferrers type

A strict order on a set is a homogeneous relation arising in order theory. In 1951 Jacques Riguet adopted the ordering of an integer partition, called a Ferrers diagram, to extend ordering to binary relations in general.

The corresponding logical matrix of a general binary relation has rows which finish with a sequence of ones. Thus the dots of a Ferrer's diagram are changed to ones and aligned on the right in the matrix.

An algebraic statement required for a Ferrers type relation R is $R{\bar {R}}^{\textsf {T}}R\subseteq R.$

If any one of the relations $R,{\bar {R}},R^{\textsf {T}}$ is of Ferrers type, then all of them are.

### Contact

Suppose B is the power set of A , the set of all subsets of A . Then a relation g is a **contact relation** if it satisfies three properties:

1. ${\text{for all }}x\in A,Y=\{x\}{\text{ implies }}xgY.$
2. $Y\subseteq Z{\text{ and }}xgY{\text{ implies }}xgZ.$
3. ${\text{for all }}y\in Y,ygZ{\text{ and }}xgY{\text{ implies }}xgZ.$

The set membership relation, $\epsilon =$ "is an element of", satisfies these properties so $\epsilon$ is a contact relation. The notion of a general contact relation was introduced by Georg Aumann in 1970.

In terms of the calculus of relations, sufficient conditions for a contact relation include $C^{\textsf {T}}{\bar {C}}\subseteq \ni {\bar {C}}\equiv C{\overline {\ni {\bar {C}}}}\subseteq C,$ where $\ni$ is the converse of set membership ( $\in$ ).

## Preorder R\R

Every relation R generates a preorder $R\backslash R$ which is the left residual. In terms of converse and complements, $R\backslash R\equiv {\overline {R^{\textsf {T}}{\bar {R}}}}.$ Forming the diagonal of $R^{\textsf {T}}{\bar {R}}$ , the corresponding row of $R^{\textsf {T}}$ and column of ${\bar {R}}$ will be of opposite logical values, so the diagonal is all zeros. Then

$R^{\textsf {T}}{\bar {R}}\subseteq {\bar {I}}\implies I\subseteq {\overline {R^{\textsf {T}}{\bar {R}}}}=R\backslash R$

, so that

$R\backslash R$

is a

reflexive relation

.

To show transitivity, one requires that $(R\backslash R)(R\backslash R)\subseteq R\backslash R.$ Recall that $X=R\backslash R$ is the largest relation such that $RX\subseteq R.$ Then

$R(R\backslash R)\subseteq R$

$R(R\backslash R)(R\backslash R)\subseteq R$

(repeat)

$\equiv R^{\textsf {T}}{\bar {R}}\subseteq {\overline {(R\backslash R)(R\backslash R)}}$

(Schröder's rule)

$\equiv (R\backslash R)(R\backslash R)\subseteq {\overline {R^{\textsf {T}}{\bar {R}}}}$

(complementation)

$\equiv (R\backslash R)(R\backslash R)\subseteq R\backslash R.$

(definition)

The inclusion relation Ω on the power set of U can be obtained in this way from the membership relation $\in$ on subsets of U :

$\Omega ={\overline {\ni {\bar {\in }}}}=\in \backslash \in .$

## Fringe of a relation

Given a relation R , its **fringe** is the sub-relation defined as $\operatorname {fringe} (R)=R\cap {\overline {R{\bar {R}}^{\textsf {T}}R}}.$

When R is a partial identity relation, difunctional, or a block diagonal relation, then $\operatorname {fringe} (R)=R$ . Otherwise the $\operatorname {fringe}$ operator selects a boundary sub-relation described in terms of its logical matrix: $\operatorname {fringe} (R)$ is the side diagonal if R is an upper right triangular linear order or strict order. $\operatorname {fringe} (R)$ is the block fringe if R is irreflexive ( $R\subseteq {\bar {I}}$ ) or upper right block triangular. $\operatorname {fringe} (R)$ is a sequence of boundary rectangles when R is of Ferrers type.

On the other hand, $\operatorname {fringe} (R)=\emptyset$ when R is a dense, linear, strict order.

## Mathematical heaps

Given two sets A and B , the set of binary relations between them ${\mathcal {B}}(A,B)$ can be equipped with a ternary operation $[a,b,c]=ab^{\textsf {T}}c$ where $b^{\mathsf {T}}$ denotes the converse relation of b . In 1953 Viktor Wagner used properties of this ternary operation to define semiheaps, heaps, and generalized heaps. The contrast of heterogeneous and homogeneous relations is highlighted by these definitions:

> There is a pleasant symmetry in Wagner's work between heaps, semiheaps, and generalised heaps on the one hand, and groups, semigroups, and generalised groups on the other. Essentially, the various types of semiheaps appear whenever we consider binary relations (and partial one-one mappings) between *different* sets A and B , while the various types of semigroups appear in the case where $A=B$ .

— Christopher Hollings, "Mathematics across the Iron Curtain: a history of the algebraic theory of semigroups"
