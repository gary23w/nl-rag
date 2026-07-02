---
title: "Intuitionistic type theory"
source: https://en.wikipedia.org/wiki/Intuitionistic_type_theory
domain: homotopy-type-theory
license: CC-BY-SA-4.0
tags: homotopy type theory, intuitionistic type theory, univalent foundations, identity type
fetched: 2026-07-02
---

# Intuitionistic type theory

**Intuitionistic type theory** (also known as **constructive type theory**, or **Martin-Löf type theory** (**MLTT**)) is a type theory and an alternative foundation of mathematics. Intuitionistic type theory was created by Per Martin-Löf, a Swedish mathematician and philosopher, who first published it in 1972. There are multiple versions of the type theory: Martin-Löf proposed both intensional and extensional variants of the theory and early impredicative versions, shown to be inconsistent by Girard's paradox, gave way to predicative versions. However, all versions keep the core design of constructive logic using dependent types.

## Design

Martin-Löf designed the type theory on the principles of mathematical constructivism. Constructivism requires any existence proof to contain a "witness". So, any proof of "there exists a prime greater than 1000" must identify a specific number that is both prime and greater than 1000. Intuitionistic type theory accomplished this design goal by internalizing the BHK interpretation. A useful consequence is that proofs become mathematical objects that can be examined, compared, and manipulated.

Intuitionistic type theory's type constructors were built to follow a one-to-one correspondence with logical connectives. For example, the logical connective called implication ( $A\implies B$ ) corresponds to the type of a function ( $A\to B$ ). This correspondence is called the Curry–Howard isomorphism. Prior type theories had also followed this isomorphism, but Martin-Löf's was the first to extend it to predicate logic by introducing dependent types.

## Type theory

A type theory is a kind of mathematical ontology, or foundation, describing the fundamental objects that exist. In the standard foundation, set theory combined with mathematical logic, the fundamental object is the set, which is a container that contains elements. In type theory, the fundamental object is the term, each of which belongs to one and only one type.

Intuitionistic type theory has three finite types, which are then composed using five different type constructors. Unlike set theories, type theories are not built on top of a logic like Frege's. So, each feature of the type theory does double duty as a feature of both math and logic.

### 0 type, 1 type and 2 type

There are three finite types: The **0** type contains no terms. The **1** type contains one canonical term. The **2** type contains two canonical terms.

Because the **0** type contains no terms, it is also called the empty type. It is used to represent anything that cannot exist. It is also written $\bot$ and represents anything unprovable (that is, a proof of it cannot exist). As a result, negation is defined as a function to it: $\neg A:=A\to \bot$ .

Likewise, the **1** type contains one canonical term and represents existence. It also is called the unit type.

Finally, the **2** type contains two canonical terms. It represents a definite choice between two values. It is used for Boolean values but *not* propositions.

Propositions are instead represented by particular types. For instance, a true proposition can be represented by the **1** type, while a false proposition can be represented by the **0** type. But we cannot assert that these are the only propositions, i.e. the law of excluded middle does not hold for propositions in intuitionistic type theory.

### Σ type constructor

Σ-types contain ordered pairs. As with typical ordered pair (or 2-tuple) types, a Σ-type can describe the Cartesian product, $A\times B$ , of two other types, A and B . Logically, such an ordered pair would hold a proof of A and a proof of B , so one may see such a type written as $A\wedge B$ .

Σ-types are more powerful than typical ordered pair types because of dependent typing. In the ordered pair, the type of the second term can depend on the value of the first term. For example, the first term of the pair might be a natural number and the second term's type might be a sequence of reals of length equal to the first term. Such a type would be written:

$\sum _{n{\mathbin {:}}{\mathbb {N} }}\operatorname {Vec} ({\mathbb {R} },n)$

Using set-theory terminology, this is similar to an indexed disjoint union of sets. In the case of the usual cartesian product, the type of the second term does not depend on the value of the first term. Thus the type describing the cartesian product ${\mathbb {N} }\times {\mathbb {R} }$ is written:

$\sum _{n{\mathbin {:}}{\mathbb {N} }}{\mathbb {R} }$

The value of the first term, n , is not dependent on the type of the second term, ${\mathbb {R} }$ .

Σ-types can be used to build up longer dependently-typed tuples used in mathematics and the records or structs used in most programming languages. An example of a dependently-typed 3-tuple is two integers and a proof that the first integer is smaller than the second integer, described by the type:

$\sum _{m{\mathbin {:}}{\mathbb {Z} }}{\sum _{n{\mathbin {:}}{\mathbb {Z} }}((m<n)={\text{True}})}$

Dependent typing allows Σ-types to serve the role of existential quantifier. The statement "there exists an n of type ${\mathbb {N} }$ , such that $P(n)$ is proven" becomes the type of ordered pairs where the first item is the value n of type ${\mathbb {N} }$ and the second item is a proof of $P(n)$ . Notice that the type of the second item (proofs of $P(n)$ ) depends on the value in the first part of the ordered pair ( n ). Its type would be:

$\sum _{n{\mathbin {:}}{\mathbb {N} }}P(n)$

### Π type constructor

Π-types contain functions. As with typical function types, they consist of an input type and an output type. They are more powerful than typical function types however, in that the return type can depend on the input value. Functions in type theory are different from set theory. In set theory, you look up the argument's value in a set of ordered pairs. In type theory, the argument is substituted into a term and then computation ("reduction") is applied to the term.

As an example, the type of a function that, given a natural number n , returns a vector containing n real numbers is written:

$\prod _{n{\mathbin {:}}{\mathbb {N} }}\operatorname {Vec} ({\mathbb {R} },n)$

When the output type does not depend on the input value, the function type is often simply written with a $\to$ . Thus, ${\mathbb {N} }\to {\mathbb {R} }$ is the type of functions from natural numbers to real numbers. Such Π-types correspond to logical implication. The logical proposition $A\implies B$ corresponds to the type $A\to B$ , containing functions that take proofs-of-A and return proofs-of-B. This type could be written more consistently as:

$\prod _{a{\mathbin {:}}A}B$

Π-types are also used in logic for universal quantification. The statement "for every n of type ${\mathbb {N} }$ , $P(n)$ is proven" becomes a function from n of type ${\mathbb {N} }$ to proofs of $P(n)$ . Thus, given the value for n the function generates a proof that $P(\,\cdot \,)$ holds for that value. The type would be

$\prod _{n{\mathbin {:}}{\mathbb {N} }}P(n)$

### = type constructor

=-types are created from two terms. Given two terms like $2+2$ and $2\cdot 2$ , you can create a new type $2+2=2\cdot 2$ . The terms of that new type represent proofs that the pair reduce to the same canonical term. Thus, since both $2+2$ and $2\cdot 2$ compute to the canonical term 4 , there will be a term of the type $2+2=2\cdot 2$ . In intuitionistic type theory, there is a single way to introduce =-types and that is by reflexivity:

$\operatorname {refl} {\mathbin {:}}\prod _{a{\mathbin {:}}A}(a=a).$

It is possible to create =-types such as $1=2$ where the terms do not reduce to the same canonical term, but you will be unable to create terms of that new type. In fact, if you were able to create a term of $1=2$ , you could create a term of $\bot$ . Putting that into a function would generate a function of type $1=2\to \bot$ . Since $\ldots \to \bot$ is how intuitionistic type theory defines negation, you would have $\neg (1=2)$ or, finally, $1\neq 2$ .

Equality of proofs is an area of active research in proof theory and has led to the development of homotopy type theory and other type theories.

### Inductive types

Inductive types allow the creation of complex, self-referential types. For example, a linked list of natural numbers is either an empty list or a pair of a natural number and another linked list. Inductive types can be used to define unbounded mathematical structures like trees, graphs, etc.. In fact, the natural numbers type may be defined as an inductive type, either being 0 or the successor of another natural number.

Inductive types define new constants, such as zero $0{\mathbin {:}}{\mathbb {N} }$ and the successor function $S{\mathbin {:}}{\mathbb {N} }\to {\mathbb {N} }$ . Since S does not have a definition and cannot be evaluated using substitution, terms like $S0$ and $SSS0$ become the canonical terms of the natural numbers.

Proofs on inductive types are made possible by induction. Each new inductive type comes with its own inductive rule. To prove a predicate $P(\,\cdot \,)$ for every natural number, you use the following rule:

${\operatorname {{\mathbb {N} }-elim} }\,{\mathbin {:}}P(0)\,\to \left(\prod _{n{\mathbin {:}}{\mathbb {N} }}P(n)\to P(S(n))\right)\to \prod _{n{\mathbin {:}}{\mathbb {N} }}P(n)$

Inductive types in intuitionistic type theory are defined in terms of W-types, the type of well-founded trees. Later work in type theory generated coinductive types, induction-recursion, and induction-induction for working on types with more obscure kinds of self-referentiality. Higher inductive types allow equality to be defined between terms.

### Universe types

The universe types allow proofs to be written about all the types created with the other type constructors. Every term in the universe type ${\mathcal {U}}_{0}$ can be mapped to a type created with any combination of $0,1,2,\Sigma ,\Pi ,=,$ and the inductive type constructor. However, to avoid paradoxes, there is no term in ${\mathcal {U}}_{n}$ that maps to ${\mathcal {U}}_{n}$ for any ${\mathcal {n}}\in \mathbb {N}$ .

To write proofs about all "the small types" and ${\mathcal {U}}_{0}$ , you must use ${\mathcal {U}}_{1}$ , which does contain a term for ${\mathcal {U}}_{0}$ , but not for itself ${\mathcal {U}}_{1}$ . Similarly, for ${\mathcal {U}}_{2}$ . There is a predicative hierarchy of universes, so to quantify a proof over any fixed constant k universes, you can use ${\mathcal {U}}_{k+1}$ .

Universe types are a tricky feature of type theories. Martin-Löf's original type theory had to be changed to account for Girard's paradox. Later research covered topics such as "super universes", "Mahlo universes", and impredicative universes.

## Judgements

The formal definition of intuitionistic type theory is written using judgements. For example, in the statement "if A is a type and B is a type then $\textstyle \sum _{a:A}B$ is a type" there are judgements of "is a type", "and", and "if ... then ...". The expression $\textstyle \sum _{a:A}B$ is not a judgement; it is the type being defined.

This second level of the type theory can be confusing, particularly where it comes to equality. There is a judgement of term equality, which might say $4=2+2$ . It is a statement that two terms reduce to the same canonical term. There is also a judgement of type equality, say that $A=B$ , which means every element of A is an element of the type B and vice versa. At the type level, there is a type $4=2+2$ and it contains terms if there is a proof that 4 and $2+2$ reduce to the same value. (Terms of this type are generated using the term-equality judgement.) Lastly, there is an English-language level of equality, because we use the word "four" and symbol " 4 " to refer to the canonical term $SSSS0$ . Synonyms like these are called "definitionally equal" by Martin-Löf.

The description of judgements below is based on the discussion in Nordström, Petersson, and Smith.

The formal theory works with *types* and *objects*.

A type is declared by:

- $A\ {\mathsf {Type}}$

An object exists and is in a type if:

- $a{\mathbin {:}}A$

Objects can be equal

- $a=b$

and types can be equal

- $A=B$

A type that depends on an object from another type is declared

- $(x{\mathbin {:}}A)B$

and removed by substitution

- $B[x/a]$ , replacing the variable x with the object a in B .

An object that depends on an object from another type can be done two ways. If the object is "abstracted", then it is written

- $[x]b$

and removed by substitution

- $b[x/a]$ , replacing the variable x with the object a in b .

The object-depending-on-object can also be declared as a constant as part of a recursive type. An example of a recursive type is:

- $0{\mathbin {:}}\mathbb {N}$
- $S{\mathbin {:}}\mathbb {N} \to \mathbb {N}$

Here, S is a constant object-depending-on-object. It is not associated with an abstraction. Constants like S can be removed by defining equality. Here the relationship with addition is defined using equality and using pattern matching to handle the recursive aspect of S :

${\begin{aligned}\operatorname {add} &{\mathbin {:}}\ (\mathbb {N} \times \mathbb {N} )\to \mathbb {N} \\\operatorname {add} (0,b)&=b\\\operatorname {add} (S(a),b)&=S(\operatorname {add} (a,b)))\end{aligned}}$

S is manipulated as an opaque constant - it has no internal structure for substitution.

So, objects and types and these relations are used to express formulae in the theory. The following styles of judgements are used to create new objects, types and relations from existing ones:

| $\Gamma \vdash \sigma \ {\mathsf {Type}}$ | *σ* is a well-formed type in the context Γ. |
|---|---|
| $\Gamma \vdash t{\mathbin {:}}\sigma$ | *t* is a well-formed term of type *σ* in context Γ. |
| $\Gamma \vdash \sigma \equiv \tau$ | *σ* and *τ* are equal types in context Γ. |
| $\Gamma \vdash t\equiv u{\mathbin {:}}\sigma$ | *t* and *u* are judgmentally equal terms of type *σ* in context Γ. |
| $\vdash \Gamma \ {\mathsf {Context}}$ | Γ is a well-formed context of typing assumptions. |

By convention, there is a type that represents all other types. It is called ${\mathcal {U}}$ (or $\operatorname {Set}$ ). Since ${\mathcal {U}}$ is a type, the members of it are objects. There is a dependent type $\operatorname {El}$ that maps each object to its corresponding type. *In most texts $\operatorname {El}$ is never written.* From the context of the statement, a reader can almost always tell whether A refers to a type, or whether it refers to the object in ${\mathcal {U}}$ that corresponds to the type.

This is the complete foundation of the theory. Everything else is derived.

To implement logic, each proposition is given its own type. The objects in those types represent the different possible ways to prove the proposition. If there is no proof for the proposition, then the type has no objects in it. Operators like "and" and "or" that work on propositions introduce new types and new objects. So $A\times B$ is a type that depends on the type A and the type B . The objects in that dependent type are defined to exist for every pair of objects in A and B . If either A or B have no proof and is an empty type, then the new type representing $A\times B$ is also empty.

This can be done for other types (booleans, natural numbers, etc.) and their operators.

## Categorical models of type theory

Using the language of category theory, R. A. G. Seely introduced the notion of a locally cartesian closed category (LCCC) as the basic model of type theory. This has been refined by Hofmann and Dybjer to Categories with Families or *Categories with Attributes* based on earlier work by Cartmell.

## Extensional versus intensional

A fundamental distinction is extensional vs intensional type theory. In extensional type theory, definitional (i.e., computational) equality is not distinguished from propositional equality, which requires proof. As a consequence type checking becomes undecidable in extensional type theory because programs in the theory might not terminate. For example, such a theory allows one to give a type to the Y-combinator; a detailed example of this can be found in Nordstöm and Petersson *Programming in Martin-Löf's Type Theory*. However, this does not prevent extensional type theory from being a basis for a practical tool; for example, Nuprl is based on extensional type theory.

In contrast, in intensional type theory type checking is decidable, but the representation of standard mathematical concepts is somewhat more cumbersome, since intensional reasoning requires using setoids or similar constructions. There are many common mathematical objects that are hard to work with or cannot be represented without this, for example, integer numbers, rational numbers, and real numbers. Integers and rational numbers can be represented without setoids, but this representation is difficult to work with. Cauchy real numbers cannot be represented without this.

Homotopy type theory works on resolving this problem. It allows one to define higher inductive types, which not only define first-order constructors (values or points), but higher-order constructors, i.e. equalities between elements (paths), equalities between equalities (homotopies), *ad infinitum*.

## Implementations of type theory

Different forms of type theory have been implemented as the formal systems underlying a number of proof assistants. While many are based on Per Martin-Löf's ideas, many have added features, more axioms, or a different philosophical background. For instance, the Nuprl system is based on computational type theory and Rocq is based on the calculus of (co)inductive constructions. Dependent types also feature in the design of programming languages such as ATS, Cayenne, Epigram, Agda, and Idris.

## Martin-Löf type theories

Per Martin-Löf constructed several type theories that were published at various times, some of them much later than when the preprints with their description became accessible to specialists (among others Jean-Yves Girard and Giovanni Sambin). The list below attempts to list all the theories that have been described in a printed form and to sketch the key features that distinguished them from each other. All of these theories had dependent products, dependent sums, disjoint unions, finite types and natural numbers. All the theories had the same reduction rules that did not include η-reduction either for dependent products or for dependent sums, except for MLTT79 where the η-reduction for dependent products is added.

**MLTT71** was the first type theory created by Per Martin-Löf. It appeared in a preprint in 1971. It had one universe, but this universe had a name in itself, i.e., it was a type theory with, as it is called today, "Type in Type". Jean-Yves Girard has shown that this system was inconsistent, and the preprint was never published.

**MLTT72** was presented in a 1972 preprint that has now been published. That theory had one universe V and no identity types (=-types). The universe was "predicative" in the sense that the dependent product of a family of objects from V over an object that was not in V such as, for example, V itself, was not assumed to be in V. The universe was à la Russell's *Principia Mathematica*, i.e., one would write directly "T∈V" and "t∈T" (Martin-Löf uses the sign "∈" instead of modern ":") without an added constructor such as "El".

**MLTT73** was the first definition of a type theory that Per Martin-Löf published (it was presented at the Logic Colloquium '73 and published in 1975). There are identity types, which he describes as "propositions", but since no real distinction between propositions and the rest of the types is introduced the meaning of this is unclear. There is what later acquires the name of J-eliminator but yet without a name (see pp. 94–95). There is in this theory an infinite sequence of universes V0, ..., V*n*, ... . The universes are predicative, à la Russell and *non-cumulative*. In fact, Corollary 3.10 on p. 115 says that if A∈V*m* and B∈V*n* are such that A and B are convertible then *m* = *n*.

**MLTT79** was presented in 1979 and published in 1982. In this paper, Martin-Löf introduced the four basic types of judgement for the dependent type theory that has since become fundamental in the study of the meta-theory of such systems. He also introduced contexts as a separate concept in it (see p. 161). There are identity types with the J-eliminator (which already appeared in MLTT73 but did not have this name there) but also with the rule that makes the theory "extensional" (p. 169). There are W-types. There is an infinite sequence of predicative universes that *are cumulative*.

**Bibliopolis**: there is a discussion of a type theory in the *Bibliopolis* book from 1984, but it is somewhat open-ended and does not seem to represent a particular set of choices and so there is no specific type theory associated with it.
