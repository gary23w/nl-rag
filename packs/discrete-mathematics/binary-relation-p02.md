---
title: "Binary relation (part 2/2)"
source: https://en.wikipedia.org/wiki/Binary_relation
domain: discrete-mathematics
license: CC-BY-SA-4.0
tags: discrete math, discrete mathematics, combinatorics, graph theory, set theory, permutation
fetched: 2026-07-02
part: 2/2
---

## Calculus of relations

Developments in algebraic logic have facilitated usage of binary relations. The calculus of relations includes the algebra of sets, extended by composition of relations and the use of converse relations. The inclusion R ⊆ S , {\displaystyle R\subseteq S,} ({\displaystyle R\subseteq S,}) meaning that a R b {\displaystyle aRb} ({\displaystyle aRb}) implies a S b {\displaystyle aSb} ({\displaystyle aSb}), sets the scene in a lattice of relations. But since P ⊆ Q ≡ ( P ∩ Q ¯ = ∅ ) ≡ ( P ∩ Q = P ) , {\displaystyle P\subseteq Q\equiv (P\cap {\bar {Q}}=\varnothing )\equiv (P\cap Q=P),} ({\displaystyle P\subseteq Q\equiv (P\cap {\bar {Q}}=\varnothing )\equiv (P\cap Q=P),}) the inclusion symbol is superfluous. Nevertheless, composition of relations and manipulation of the operators according to Schröder rules, provides a calculus to work in the power set of A × B . {\displaystyle A\times B.} ({\displaystyle A\times B.})

In contrast to homogeneous relations, the composition of relations operation is only a partial function. The necessity of matching target to source of composed relations has led to the suggestion that the study of heterogeneous relations is a chapter of category theory as in the category of sets, except that the morphisms of this category are relations. The *objects* of the category Rel are sets, and the relation-morphisms compose as required in a category.


## Induced concept lattice

Binary relations have been described through their induced concept lattices: A **concept** C ⊂ R {\displaystyle C\subset R} ({\displaystyle C\subset R}) satisfies two properties:

- The logical matrix of C {\displaystyle C} ({\displaystyle C}) is the outer product of logical vectors C i j = u i v j , u , v {\displaystyle C_{ij}=u_{i}v_{j},\quad u,v} ({\displaystyle C_{ij}=u_{i}v_{j},\quad u,v}) logical vectors.
- C {\displaystyle C} ({\displaystyle C}) is maximal, not contained in any other outer product. Thus C {\displaystyle C} ({\displaystyle C}) is described as a *non-enlargeable rectangle*.

For a given relation R ⊆ X × Y , {\displaystyle R\subseteq X\times Y,} ({\displaystyle R\subseteq X\times Y,}) the set of concepts, enlarged by their joins and meets, forms an "induced lattice of concepts", with inclusion ⊑ {\displaystyle \sqsubseteq } ({\displaystyle \sqsubseteq }) forming a preorder.

The MacNeille completion theorem (1937) (that any partial order may be embedded in a complete lattice) is cited in a 2013 survey article "Decomposition of relations on concept lattices". The decomposition is

R

=

f

E

g

T

{\displaystyle R=fEg^{\textsf {T}}}

, where

f

{\displaystyle f}

and

g

{\displaystyle g}

are

functions

, called

mappings

or left-total, functional relations in this context. The "induced concept lattice is isomorphic to the cut completion of the partial order

E

{\displaystyle E}

that belongs to the minimal decomposition

(

f

,

g

,

E

)

{\displaystyle (f,g,E)}

of the relation

R

{\displaystyle R}

."

Particular cases are considered below: E {\displaystyle E} ({\displaystyle E}) total order corresponds to Ferrers type, and E {\displaystyle E} ({\displaystyle E}) identity corresponds to difunctional, a generalization of equivalence relation on a set.

Relations may be ranked by the **Schein rank** which counts the number of concepts necessary to cover a relation. Structural analysis of relations with concepts provides an approach for data mining.


## Particular relations

- *Proposition*: If R {\displaystyle R} ({\displaystyle R}) is a surjective relation and R T {\displaystyle R^{\mathsf {T}}} ({\displaystyle R^{\mathsf {T}}}) is its transpose, then I ⊆ R T R {\displaystyle I\subseteq R^{\textsf {T}}R} ({\displaystyle I\subseteq R^{\textsf {T}}R}) where I {\displaystyle I} ({\displaystyle I}) is the m × m {\displaystyle m\times m} ({\displaystyle m\times m}) identity relation.
- *Proposition*: If R {\displaystyle R} ({\displaystyle R}) is a serial relation, then I ⊆ R R T {\displaystyle I\subseteq RR^{\textsf {T}}} ({\displaystyle I\subseteq RR^{\textsf {T}}}) where I {\displaystyle I} ({\displaystyle I}) is the n × n {\displaystyle n\times n} ({\displaystyle n\times n}) identity relation.

### Difunctional

The idea of a difunctional relation is to partition objects by distinguishing attributes, as a generalization of the concept of an equivalence relation. One way this can be done is with an intervening set Z = { x , y , z , … } {\displaystyle Z=\{x,y,z,\ldots \}} ({\displaystyle Z=\{x,y,z,\ldots \}}) of indicators. The partitioning relation R = F G T {\displaystyle R=FG^{\textsf {T}}} ({\displaystyle R=FG^{\textsf {T}}}) is a composition of relations using *functional* relations F ⊆ A × Z  and  G ⊆ B × Z . {\displaystyle F\subseteq A\times Z{\text{ and }}G\subseteq B\times Z.} ({\displaystyle F\subseteq A\times Z{\text{ and }}G\subseteq B\times Z.}) Jacques Riguet named these relations **difunctional** since the composition F G T {\displaystyle FG^{\mathsf {T}}} ({\displaystyle FG^{\mathsf {T}}}) involves functional relations, commonly called *partial functions*.

In 1950 Riguet showed that such relations satisfy the inclusion:

R

R

T

R

⊆

R

{\displaystyle RR^{\textsf {T}}R\subseteq R}

In automata theory, the term **rectangular relation** has also been used to denote a difunctional relation. This terminology recalls the fact that, when represented as a logical matrix, the columns and rows of a difunctional relation can be arranged as a block matrix with rectangular blocks of ones on the (asymmetric) main diagonal. More formally, a relation R {\displaystyle R} ({\displaystyle R}) on X × Y {\displaystyle X\times Y} ({\displaystyle X\times Y}) is difunctional if and only if it can be written as the union of Cartesian products A i × B i {\displaystyle A_{i}\times B_{i}} ({\displaystyle A_{i}\times B_{i}}), where the A i {\displaystyle A_{i}} ({\displaystyle A_{i}}) are a partition of a subset of X {\displaystyle X} ({\displaystyle X}) and the B i {\displaystyle B_{i}} ({\displaystyle B_{i}}) likewise a partition of a subset of Y {\displaystyle Y} ({\displaystyle Y}).

Using the notation { y ∣ x R y } = x R {\displaystyle \{y\mid xRy\}=xR} ({\displaystyle \{y\mid xRy\}=xR}), a difunctional relation can also be characterized as a relation R {\displaystyle R} ({\displaystyle R}) such that wherever x 1 R {\displaystyle x_{1}R} ({\displaystyle x_{1}R}) and x 2 R {\displaystyle x_{2}R} ({\displaystyle x_{2}R}) have a non-empty intersection, then these two sets coincide; formally x 1 ∩ x 2 ≠ ∅ {\displaystyle x_{1}\cap x_{2}\neq \varnothing } ({\displaystyle x_{1}\cap x_{2}\neq \varnothing }) implies x 1 R = x 2 R . {\displaystyle x_{1}R=x_{2}R.} ({\displaystyle x_{1}R=x_{2}R.})

In 1997 researchers found "utility of binary decomposition based on difunctional dependencies in database management." Furthermore, difunctional relations are fundamental in the study of bisimulations.

In the context of homogeneous relations, a partial equivalence relation is difunctional.

### Ferrers type

A strict order on a set is a homogeneous relation arising in order theory. In 1951 Jacques Riguet adopted the ordering of an integer partition, called a Ferrers diagram, to extend ordering to binary relations in general.

The corresponding logical matrix of a general binary relation has rows which finish with a sequence of ones. Thus the dots of a Ferrer's diagram are changed to ones and aligned on the right in the matrix.

An algebraic statement required for a Ferrers type relation R is R R ¯ T R ⊆ R . {\displaystyle R{\bar {R}}^{\textsf {T}}R\subseteq R.} ({\displaystyle R{\bar {R}}^{\textsf {T}}R\subseteq R.})

If any one of the relations R , R ¯ , R T {\displaystyle R,{\bar {R}},R^{\textsf {T}}} ({\displaystyle R,{\bar {R}},R^{\textsf {T}}}) is of Ferrers type, then all of them are.

### Contact

Suppose B {\displaystyle B} ({\displaystyle B}) is the power set of A {\displaystyle A} ({\displaystyle A}), the set of all subsets of A {\displaystyle A} ({\displaystyle A}). Then a relation g {\displaystyle g} ({\displaystyle g}) is a **contact relation** if it satisfies three properties:

1. for all  x ∈ A , Y = { x }  implies  x g Y . {\displaystyle {\text{for all }}x\in A,Y=\{x\}{\text{ implies }}xgY.} ({\displaystyle {\text{for all }}x\in A,Y=\{x\}{\text{ implies }}xgY.})
2. Y ⊆ Z  and  x g Y  implies  x g Z . {\displaystyle Y\subseteq Z{\text{ and }}xgY{\text{ implies }}xgZ.} ({\displaystyle Y\subseteq Z{\text{ and }}xgY{\text{ implies }}xgZ.})
3. for all  y ∈ Y , y g Z  and  x g Y  implies  x g Z . {\displaystyle {\text{for all }}y\in Y,ygZ{\text{ and }}xgY{\text{ implies }}xgZ.} ({\displaystyle {\text{for all }}y\in Y,ygZ{\text{ and }}xgY{\text{ implies }}xgZ.})

The set membership relation, ϵ = {\displaystyle \epsilon =} ({\displaystyle \epsilon =}) "is an element of", satisfies these properties so ϵ {\displaystyle \epsilon } ({\displaystyle \epsilon }) is a contact relation. The notion of a general contact relation was introduced by Georg Aumann in 1970.

In terms of the calculus of relations, sufficient conditions for a contact relation include C T C ¯ ⊆∋ C ¯ ≡ C ∋ C ¯ ¯ ⊆ C , {\displaystyle C^{\textsf {T}}{\bar {C}}\subseteq \ni {\bar {C}}\equiv C{\overline {\ni {\bar {C}}}}\subseteq C,} ({\displaystyle C^{\textsf {T}}{\bar {C}}\subseteq \ni {\bar {C}}\equiv C{\overline {\ni {\bar {C}}}}\subseteq C,}) where ∋ {\displaystyle \ni } ({\displaystyle \ni }) is the converse of set membership ( ∈ {\displaystyle \in } ({\displaystyle \in })).


## Preorder R\R

Every relation R {\displaystyle R} ({\displaystyle R}) generates a preorder R ∖ R {\displaystyle R\backslash R} ({\displaystyle R\backslash R}) which is the left residual. In terms of converse and complements, R ∖ R ≡ R T R ¯ ¯ . {\displaystyle R\backslash R\equiv {\overline {R^{\textsf {T}}{\bar {R}}}}.} ({\displaystyle R\backslash R\equiv {\overline {R^{\textsf {T}}{\bar {R}}}}.}) Forming the diagonal of R T R ¯ {\displaystyle R^{\textsf {T}}{\bar {R}}} ({\displaystyle R^{\textsf {T}}{\bar {R}}}), the corresponding row of R T {\displaystyle R^{\textsf {T}}} ({\displaystyle R^{\textsf {T}}}) and column of R ¯ {\displaystyle {\bar {R}}} ({\displaystyle {\bar {R}}}) will be of opposite logical values, so the diagonal is all zeros. Then

R

T

R

¯

⊆

I

¯

⟹

I

⊆

R

T

R

¯

¯

=

R

∖

R

{\displaystyle R^{\textsf {T}}{\bar {R}}\subseteq {\bar {I}}\implies I\subseteq {\overline {R^{\textsf {T}}{\bar {R}}}}=R\backslash R}

, so that

R

∖

R

{\displaystyle R\backslash R}

is a

reflexive relation

.

To show transitivity, one requires that ( R ∖ R ) ( R ∖ R ) ⊆ R ∖ R . {\displaystyle (R\backslash R)(R\backslash R)\subseteq R\backslash R.} ({\displaystyle (R\backslash R)(R\backslash R)\subseteq R\backslash R.}) Recall that X = R ∖ R {\displaystyle X=R\backslash R} ({\displaystyle X=R\backslash R}) is the largest relation such that R X ⊆ R . {\displaystyle RX\subseteq R.} ({\displaystyle RX\subseteq R.}) Then

R

(

R

∖

R

)

⊆

R

{\displaystyle R(R\backslash R)\subseteq R}

R

(

R

∖

R

)

(

R

∖

R

)

⊆

R

{\displaystyle R(R\backslash R)(R\backslash R)\subseteq R}

(repeat)

≡

R

T

R

¯

⊆

(

R

∖

R

)

(

R

∖

R

)

¯

{\displaystyle \equiv R^{\textsf {T}}{\bar {R}}\subseteq {\overline {(R\backslash R)(R\backslash R)}}}

(Schröder's rule)

≡

(

R

∖

R

)

(

R

∖

R

)

⊆

R

T

R

¯

¯

{\displaystyle \equiv (R\backslash R)(R\backslash R)\subseteq {\overline {R^{\textsf {T}}{\bar {R}}}}}

(complementation)

≡

(

R

∖

R

)

(

R

∖

R

)

⊆

R

∖

R

.

{\displaystyle \equiv (R\backslash R)(R\backslash R)\subseteq R\backslash R.}

(definition)

The inclusion relation Ω on the power set of U {\displaystyle U} ({\displaystyle U}) can be obtained in this way from the membership relation ∈ {\displaystyle \in } ({\displaystyle \in }) on subsets of U {\displaystyle U} ({\displaystyle U}):

Ω

=

∋

∈

¯

¯

=∈

∖

∈

.

{\displaystyle \Omega ={\overline {\ni {\bar {\in }}}}=\in \backslash \in .}


## Fringe of a relation

Given a relation R {\displaystyle R} ({\displaystyle R}), its **fringe** is the sub-relation defined as fringe ⁡ ( R ) = R ∩ R R ¯ T R ¯ . {\displaystyle \operatorname {fringe} (R)=R\cap {\overline {R{\bar {R}}^{\textsf {T}}R}}.} ({\displaystyle \operatorname {fringe} (R)=R\cap {\overline {R{\bar {R}}^{\textsf {T}}R}}.})

When R {\displaystyle R} ({\displaystyle R}) is a partial identity relation, difunctional, or a block diagonal relation, then fringe ⁡ ( R ) = R {\displaystyle \operatorname {fringe} (R)=R} ({\displaystyle \operatorname {fringe} (R)=R}). Otherwise the fringe {\displaystyle \operatorname {fringe} } ({\displaystyle \operatorname {fringe} }) operator selects a boundary sub-relation described in terms of its logical matrix: fringe ⁡ ( R ) {\displaystyle \operatorname {fringe} (R)} ({\displaystyle \operatorname {fringe} (R)}) is the side diagonal if R {\displaystyle R} ({\displaystyle R}) is an upper right triangular linear order or strict order. fringe ⁡ ( R ) {\displaystyle \operatorname {fringe} (R)} ({\displaystyle \operatorname {fringe} (R)}) is the block fringe if R {\displaystyle R} ({\displaystyle R}) is irreflexive ( R ⊆ I ¯ {\displaystyle R\subseteq {\bar {I}}} ({\displaystyle R\subseteq {\bar {I}}})) or upper right block triangular. fringe ⁡ ( R ) {\displaystyle \operatorname {fringe} (R)} ({\displaystyle \operatorname {fringe} (R)}) is a sequence of boundary rectangles when R {\displaystyle R} ({\displaystyle R}) is of Ferrers type.

On the other hand, fringe ⁡ ( R ) = ∅ {\displaystyle \operatorname {fringe} (R)=\emptyset } ({\displaystyle \operatorname {fringe} (R)=\emptyset }) when R {\displaystyle R} ({\displaystyle R}) is a dense, linear, strict order.


## Mathematical heaps

Given two sets A {\displaystyle A} ({\displaystyle A}) and B {\displaystyle B} ({\displaystyle B}), the set of binary relations between them B ( A , B ) {\displaystyle {\mathcal {B}}(A,B)} ({\displaystyle {\mathcal {B}}(A,B)}) can be equipped with a ternary operation [ a , b , c ] = a b T c {\displaystyle [a,b,c]=ab^{\textsf {T}}c} ({\displaystyle [a,b,c]=ab^{\textsf {T}}c}) where b T {\displaystyle b^{\mathsf {T}}} ({\displaystyle b^{\mathsf {T}}}) denotes the converse relation of b {\displaystyle b} ({\displaystyle b}). In 1953 Viktor Wagner used properties of this ternary operation to define semiheaps, heaps, and generalized heaps. The contrast of heterogeneous and homogeneous relations is highlighted by these definitions:

> There is a pleasant symmetry in Wagner's work between heaps, semiheaps, and generalised heaps on the one hand, and groups, semigroups, and generalised groups on the other. Essentially, the various types of semiheaps appear whenever we consider binary relations (and partial one-one mappings) between *different* sets A {\displaystyle A} ({\displaystyle A}) and B {\displaystyle B} ({\displaystyle B}), while the various types of semigroups appear in the case where A = B {\displaystyle A=B} ({\displaystyle A=B}).

— Christopher Hollings, "Mathematics across the Iron Curtain: a history of the algebraic theory of semigroups"
