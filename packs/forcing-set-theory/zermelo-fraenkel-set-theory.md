---
title: "Zermelo–Fraenkel set theory"
source: https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory
domain: forcing-set-theory
license: CC-BY-SA-4.0
tags: forcing method, continuum hypothesis, constructible universe, large cardinal
fetched: 2026-07-02
---

# Zermelo–Fraenkel set theory

In set theory, **Zermelo–Fraenkel set theory**, named after mathematicians Ernst Zermelo and Abraham Fraenkel, is an axiomatic system that was proposed in the early twentieth century in order to formulate a theory of sets free of paradoxes such as Russell's paradox. Today, Zermelo–Fraenkel set theory, with the historically controversial axiom of choice (AC) included, is the standard form of axiomatic set theory and as such is the most common foundation of mathematics. Zermelo–Fraenkel set theory with the axiom of choice included is abbreviated **ZFC**, where C stands for "choice", and **ZF** refers to the axioms of Zermelo–Fraenkel set theory with the axiom of choice excluded.

Informally, Zermelo–Fraenkel set theory is intended to formalize a single primitive notion, that of a hereditary well-founded set, so that all entities in the universe of discourse are such sets. Thus the axioms of Zermelo–Fraenkel set theory refer only to pure sets and prevent its models from containing urelements (elements that are not themselves sets). Furthermore, proper classes (collections of mathematical objects defined by a property shared by their members where the collections are too big to be sets) can only be treated indirectly. Specifically, Zermelo–Fraenkel set theory does not allow for the existence of a universal set (a set containing all sets) nor for unrestricted comprehension, thereby avoiding Russell's paradox. Von Neumann–Bernays–Gödel set theory (NBG) is a commonly used conservative extension of Zermelo–Fraenkel set theory that does allow explicit treatment of proper classes.

There are many equivalent formulations of the axioms of Zermelo–Fraenkel set theory. Most of the axioms state the existence of particular sets defined from other sets. For example, the axiom of pairing implies that given any two sets a and b there is a new set $\{a,b\}$ containing exactly a and b . Other axioms describe properties of set membership. A goal of the axioms is that each axiom should be true if interpreted as a statement about the collection of all sets in the von Neumann universe (also known as the cumulative hierarchy).

The metamathematics of Zermelo–Fraenkel set theory has been extensively studied. Landmark results in this area established the logical independence of the axiom of choice from the remaining Zermelo-Fraenkel axioms and of the continuum hypothesis from ZFC. The consistency of a theory such as ZFC cannot be proved within the theory itself, as shown by Gödel's second incompleteness theorem.

## History

The modern study of set theory was initiated by Georg Cantor and Richard Dedekind in the 1870s. However, the discovery of paradoxes in naive set theory, such as Russell's paradox, led to the desire for a more rigorous form of set theory that was free of these paradoxes.

In 1908, Ernst Zermelo proposed the first axiomatic set theory, Zermelo set theory. However, as first pointed out by Abraham Fraenkel in a 1921 letter to Zermelo, this theory was incapable of proving the existence of certain sets and cardinal numbers whose existence was taken for granted by most set theorists of the time, notably the cardinal number aleph-omega ( $\aleph _{\omega }$ ) and the set $\{Z_{0},{\mathcal {P}}(Z_{0}),{\mathcal {P}}({\mathcal {P}}(Z_{0})),{\mathcal {P}}({\mathcal {P}}({\mathcal {P}}(Z_{0}))),...\},$ where $Z_{0}$ is any infinite set and ${\mathcal {P}}$ is the power set operation. Moreover, one of Zermelo's axioms invoked a concept, that of a "definite" property, whose operational meaning was not clear. In 1922, Fraenkel and Thoralf Skolem independently proposed operationalizing a "definite" property as one that could be formulated as a well-formed formula in a first-order logic whose atomic formulas were limited to set membership and identity. They also independently proposed replacing the axiom schema of specification with the axiom schema of replacement. Appending this schema, as well as the axiom of regularity (first proposed by John von Neumann), to Zermelo set theory yields the theory ZFC.

## Formal language

Formally, ZFC is a one-sorted theory in first-order logic. The equality symbol can be treated as either a primitive logical symbol or a high-level abbreviation for having exactly the same elements. The former approach is the most common. The signature has a single predicate symbol, usually denoted $\in$ , which is a predicate symbol of arity 2 (a binary relation symbol). This symbol symbolizes a set membership relation. For example, the formula $a\in b$ means that *a is an element of the set b* (also read as *a is a member of b*).

There are different ways to formulate the formal language. Some authors may choose a different set of connectives or quantifiers. For example, the logical connective NAND alone can encode the other connectives, a property known as functional completeness. This section attempts to strike a balance between simplicity and intuitiveness.

The language's alphabet consists of:

- A countably infinite number of variables used for representing sets
- The logical connectives $\lnot$ , $\land$ , $\lor$
- The quantifier symbols $\forall$ , $\exists$
- The equality symbol =
- The set membership symbol $\in$
- Brackets ( )

With this alphabet, the recursive rules for forming well-formed formulae (wff) are as follows:

- Let x and y be metavariables for any variables. These are the two ways to build atomic formulae (the simplest wffs):

$x=y$

$x\in y$

- Let $\phi$ and $\psi$ be metavariables for any wff, and x be a metavariable for any variable. These are valid wff constructions:

$\lnot \phi$

$(\phi \land \psi )$

$(\phi \lor \psi )$

$\forall x\phi$

$\exists x\phi$

A well-formed formula can be thought as a syntax tree. The leaf nodes are always atomic formulae. Nodes $\land$ and $\lor$ have exactly two child nodes, while nodes $\lnot$ , $\forall x$ and $\exists x$ have exactly one. There are countably infinitely many wffs; however, each wff has a finite number of nodes.

## Axioms

There are many equivalent formulations of the ZFC axioms. The following particular axiom set is from Kunen (1980). The axioms in order below are expressed in a mixture of first-order logic and high-level abbreviations.

Axioms 1–8 form ZF, while the axiom 9 turns ZF into ZFC. Following Kunen (1980), we use the equivalent well-ordering theorem in place of the axiom of choice for axiom 9.

All formulations of ZFC imply that at least one set exists. Kunen includes an axiom that directly asserts the existence of a set, although he notes that he does so only "for emphasis". Its omission here can be justified in two ways. First, in the standard semantics of first-order logic in which ZFC is typically formalized, the domain of discourse must be nonempty. Hence, it is a logical theorem of first-order logic that something exists – usually expressed as the assertion that something is identical to itself, $\exists x(x=x)$ . Consequently, it is a theorem of every first-order theory that something exists. However, as noted above, because in the intended semantics of ZFC, there are only sets, the interpretation of this logical theorem in the context of ZFC is that some *set* exists. Hence, there is no need for a separate axiom asserting that a set exists. Second, however, even if ZFC is formulated in so-called free logic, in which it is not provable from logic alone that something exists, the axiom of infinity asserts that an *infinite* set exists. This implies that *a* set exists, and so, once again, it is superfluous to include an axiom asserting as much.

### Axiom of extensionality - 1

Two sets are equal (are the same set) if they have the same elements.

$\forall x\forall y[\forall z(z\in x\Leftrightarrow z\in y)\Rightarrow x=y].$

The converse of this axiom follows from the substitution property of equality. ZFC is constructed in first-order logic. Some formulations of first-order logic include identity; others do not. If the variety of first-order logic in which one is constructing set theory does not include equality " = ", $x=y$ may be defined as an abbreviation for the following formula: $\forall z[z\in x\Leftrightarrow z\in y]\land \forall w[x\in w\Leftrightarrow y\in w].$

In this case, the axiom of extensionality can be reformulated as

$\forall x\forall y[\forall z(z\in x\Leftrightarrow z\in y)\Rightarrow \forall w(x\in w\Leftrightarrow y\in w)],$

which says that if x and y have the same elements, then they belong to the same sets.

### Axiom of regularity (also called the axiom of foundation) - 2

Every non-empty set x contains a member y such that x and y are disjoint sets.

$\forall x[(\exists a(a\in x))\Rightarrow \exists y(y\in x\land \lnot \exists z(z\in y\land z\in x))].$

or in modern notation: $\forall x\,(x\neq \varnothing \Rightarrow \exists y(y\in x\land y\cap x=\varnothing )).$

With the axioms of pairing and union, this implies that no set is an element of itself. With the axioms of infinity, replacement, and union, this implies that every set has an ordinal rank.

### Axiom schema of specification (or of separation, or of restricted comprehension) - 3

Subsets are commonly constructed using set builder notation. For example, the even integers can be constructed as the subset of the integers $\mathbb {Z}$ satisfying the congruence modulo predicate $x\equiv 0{\pmod {2}}$ :

$\{x\in \mathbb {Z} :x\equiv 0{\pmod {2}}\}.$

In general, the subset of a set z obeying a formula $\varphi (x)$ with one free variable x may be written as:

$\{x\in z:\varphi (x)\}.$

The axiom schema of specification states that this subset always exists (it is an axiom *schema* because there is one axiom for each $\varphi$ ). Formally, let $\varphi$ be any formula in the language of ZFC with all free variables among $x,z,w_{1},\ldots ,w_{n}$ ( y is not free in $\varphi$ ). Then:

$\forall z\forall w_{1}\forall w_{2}\ldots \forall w_{n}\exists y\forall x[x\in y\Leftrightarrow ((x\in z)\land \varphi (x,w_{1},w_{2},...,w_{n},z))].$

Note that the axiom schema of specification can only construct subsets and does not allow the construction of entities of the more general form:

$\{x:\varphi (x)\}.$

This restriction is necessary to avoid Russell's paradox (let $y=\{x:x\notin x\}$ then $y\in y\Leftrightarrow y\notin y$ ) and its variants that accompany naive set theory with unrestricted comprehension (since under this restriction y only refers to sets ***within* z** that don't belong to themselves, and $y\in z$ has ***not*** been established, even though $y\subseteq z$ is the case, so y stands in a separate position from which it can't refer to or comprehend itself; therefore, in a certain sense, this axiom schema is saying that in order to build a y on the basis of a formula $\varphi (x)$ , we need to previously restrict the sets y will regard within a set z that leaves y outside so y can't refer to itself; or, in other words, sets shouldn't refer to themselves).

In some other axiomatizations of ZF, this axiom is redundant in that it follows from the axiom schema of replacement and the axiom of the empty set.

On the other hand, the axiom schema of specification can be used to prove the existence of the empty set, denoted $\varnothing$ , once at least one set is known to exist. One way to do this is to use a property $\varphi$ which no set has. For example, if w is any existing set, the empty set can be constructed as

$\varnothing =\{u\in w\mid (u\notin w)\}.$

Thus, the axiom of the empty set is implied by the nine axioms presented here. The axiom of extensionality implies the empty set is unique (does not depend on w ). It is common to make a definitional extension that adds the symbol " $\varnothing$ " to the language of ZFC.

### Axiom of pairing - 4

If x and y are sets, then there exists a set which contains x and y as elements; for example, if $x=\{1,2\}$ and $y=\{2,3\}$ , then z might be $\{\{1,2\},\{2,3\}\}$ .

$\forall x\forall y\exists z((x\in z)\land (y\in z)).$

The axiom schema of specification must be used to reduce this to a set with exactly these two elements.

### Axiom of union - 5

The union over the elements of a set exists. For example, the union over the elements of the set $\{\{1,2\},\{2,3\}\}$ is $\{1,2,3\}.$

The axiom of union states that for any set of sets ${\mathcal {F}}$ , there is a set A containing every element that is a member of some member of ${\mathcal {F}}$ :

$\forall {\mathcal {F}}\,\exists A\,\forall Y\,\forall x[(x\in Y\land Y\in {\mathcal {F}})\Rightarrow x\in A].$

Although this formula doesn't directly assert the existence of $\cup {\mathcal {F}}$ , the set $\cup {\mathcal {F}}$ can be constructed from A in the above using the axiom schema of specification:

$\cup {\mathcal {F}}=\{x\in A:\exists Y(x\in Y\land Y\in {\mathcal {F}})\}.$

### Axiom schema of replacement - 6

The axiom schema of replacement asserts that the image of a set under any definable function will also fall inside a set.

Formally, let $\varphi$ be any formula in the language of ZFC whose free variables are among $x,y,A,w_{1},\dotsc ,w_{n},$ so that in particular B is not free in $\varphi$ . Then:

$\forall A\forall w_{1}\forall w_{2}\ldots \forall w_{n}{\bigl [}\forall x(x\in A\Rightarrow \exists !y\,\varphi )\Rightarrow \exists B\ \forall x{\bigl (}x\in A\Rightarrow \exists y(y\in B\land \varphi ){\bigr )}{\bigr ]}.$

(The unique existential quantifier $\exists !$ denotes the existence of exactly one element such that it follows a given statement.)

In other words, if the relation $\varphi$ represents a definable function f , A represents its domain, and $f(x)$ is a set for every $x\in A,$ then the range of f is a subset of some set B . The form stated here, in which B may be larger than strictly necessary, is sometimes called the axiom schema of collection.

### Axiom of infinity - 7

| 0 | = | {} | = | ∅ |
|---|---|---|---|---|
| 1 | = | {0} | = | {∅} |
| 2 | = | {0,1} | = | {∅,{∅}} |
| 3 | = | {0,1,2} | = | {∅,{∅},{∅,{∅}}} |
| 4 | = | {0,1,2,3} | = | {∅,{∅},{∅,{∅}},{∅,{∅},{∅,{∅}}}} |

Let $S(w)$ abbreviate $w\cup \{w\},$ where w is some set. (We can see that $\{w\}$ is a valid set by applying the axiom of pairing with $x=y=w$ so that the set z is $\{w\}$ ). Then there exists a set X such that the empty set $\varnothing$ , defined axiomatically, is a member of X and, whenever a set y is a member of X then $S(y)$ is also a member of X.

$\exists X\left[\exists e(\forall z\,\neg (z\in e)\land e\in X)\land \forall y(y\in X\Rightarrow S(y)\in X)\right].$

or in modern notation: $\exists X\left[\varnothing \in X\land \forall y(y\in X\Rightarrow S(y)\in X)\right].$

More colloquially, there exists a set X having infinitely many members. These members are built by repeatedly applying the operation S starting from the empty set. Each result of this construction is distinct from the previous ones, so the process does not loop or repeat. The minimal set X satisfying the axiom of infinity is the von Neumann ordinal ω, which can also be thought of as the set of natural numbers $\mathbb {N}$ . (Note that the well-foundedness of $\mathbb {N}$ does not require the axiom of regularity; it follows naturally from the structure of the construction.)

### Axiom of power set - 8

By definition, a set z is a subset of a set x if and only if every element of z is also an element of x :

$(z\subseteq x)\Leftrightarrow (\forall q(q\in z\Rightarrow q\in x)).$

The Axiom of power set states that for any set x , there is a set y that contains every subset of x :

$\forall x\exists y\forall z(z\subseteq x\Rightarrow z\in y).$

The axiom schema of specification is then used to define the power set ${\mathcal {P}}(x)$ as the subset of such a y containing the subsets of x exactly:

${\mathcal {P}}(x)=\{z\in y:z\subseteq x\}.$

Axioms *1–8* define ZF. Alternative forms of these axioms are often encountered, some of which are listed in Jech (2003). Some ZF axiomatizations include an axiom asserting that the empty set exists. The axioms of pairing, union, replacement, and power set are often stated so that the members of the set x whose existence is being asserted are just those sets which the axiom asserts x must contain.

The following axiom is added to turn ZF into ZFC:

### Axiom of well-ordering (choice) - 9

The last axiom, commonly known as the axiom of choice, is presented here as a property about well-orders, as in Kunen (1980). For any set X , there exists a binary relation R which well-orders X . This means R is a linear order on X such that every nonempty subset of X has a least element under the order R .

$\forall X\exists R(R\;{\mbox{well-orders}}\;X).$

Given axioms 1–8, many statements are provably equivalent to axiom 9. The most common of these goes as follows. Let X be a set whose members are all nonempty. Then there exists a function f from X to the union of the members of X , called a "choice function", such that for all $Y\in X$ one has $f(Y)\in Y$ . A third version of the axiom, also equivalent, is Zorn's lemma.

Since the existence of a choice function when X is a finite set is easily proved from axioms *1–8*, AC only matters for certain infinite sets. AC is characterized as nonconstructive because it asserts the existence of a choice function but says nothing about how this choice function is to be "constructed".

## Motivation via the cumulative hierarchy

One motivation for the ZFC axioms is the cumulative hierarchy of sets introduced by John von Neumann. In this viewpoint, the universe of set theory is built up in stages, with one stage for each ordinal number. At stage 0, there are no sets yet. At each following stage, a set is added to the universe if all of its elements have been added at previous stages. Thus the empty set is added at stage 1, and the set containing the empty set is added at stage 2. The collection of all sets that are obtained in this way, over all the stages, is known as *V*. The sets in *V* can be arranged into a hierarchy by assigning to each set the first stage at which that set was added to *V*.

It is provable that a set is in *V* if and only if the set is pure and well-founded. And *V* satisfies all the axioms of ZFC if the class of ordinals has appropriate reflection properties. For example, suppose that a set *x* is added at stage α, which means that every element of *x* was added at a stage earlier than α. Then, every subset of *x* is also added at (or before) stage α, because all elements of any subset of *x* were also added before stage α. This means that any subset of *x* which the axiom of separation can construct is added at (or before) stage α, and that the powerset of *x* will be added at the next stage after α.

The picture of the universe of sets stratified into the cumulative hierarchy is characteristic of ZFC and related axiomatic set theories such as Von Neumann–Bernays–Gödel set theory (often called NBG) and Morse–Kelley set theory. The cumulative hierarchy is not compatible with other set theories such as New Foundations.

It is possible to change the definition of *V* so that at each stage, instead of adding all the subsets of the union of the previous stages, subsets are only added if they are definable in a certain sense. This results in a more "narrow" hierarchy, which gives the constructible universe *L*, which also satisfies all the axioms of ZFC, including the axiom of choice. It is independent from the ZFC axioms whether *V* = *L*. Although the structure of *L* is more regular and well behaved than that of *V*, few mathematicians argue that *V* = *L* should be added to ZFC as an additional "axiom of constructibility".

## Metamathematics

### Virtual classes

Proper classes (collections of mathematical objects defined by a property shared by their members which are too big to be sets) can only be treated indirectly in ZF (and thus ZFC). An alternative to proper classes while staying within ZF and ZFC is the *virtual class* notational construct introduced by Quine (1969), where the entire construct *y* ∈ { *x* | F*x* } is simply defined as F*y*. This provides a simple notation for classes that can contain sets but need not themselves be sets, while not committing to the ontology of classes (because the notation can be syntactically converted to one that only uses sets). Quine's approach built on the earlier approach of Bernays & Fraenkel (1958). Virtual classes are also used in Levy (2002), Takeuti & Zaring (1982), and in the Metamath implementation of ZFC.

### Finite axiomatization

The axiom schemata of replacement and separation each contain infinitely many instances. Montague (1961) included a result first proved in his 1957 Ph.D. thesis: if ZFC is consistent, it is impossible to axiomatize ZFC using only finitely many axioms. On the other hand, von Neumann–Bernays–Gödel set theory (NBG) can be finitely axiomatized. The ontology of NBG includes proper classes as well as sets; a set is any class that can be a member of another class. NBG and ZFC are equivalent set theories in the sense that any theorem not mentioning classes and provable in one theory can be proved in the other.

### Consistency

Gödel's second incompleteness theorem says that a recursively axiomatizable system that can interpret Robinson arithmetic can prove its own consistency only if it is inconsistent. Moreover, Robinson arithmetic can be interpreted in general set theory, a small fragment of ZFC. Hence the consistency of ZFC cannot be proved within ZFC itself (unless it is actually inconsistent). Thus, to the extent that ZFC is identified with ordinary mathematics, the consistency of ZFC cannot be demonstrated in ordinary mathematics. The consistency of ZFC does follow from the existence of a weakly inaccessible cardinal, which is unprovable in ZFC if ZFC is consistent. Nevertheless, it is deemed unlikely that ZFC harbors an unsuspected contradiction; it is widely believed that if ZFC were inconsistent, that fact would have been uncovered by now. ZFC does not contain the classic paradoxes of naive set theory: Russell's paradox, the Burali-Forti paradox, and Cantor's paradox.

Abian & LaMacchia (1978) studied a subtheory of ZFC consisting of the axioms of extensionality, union, powerset, replacement, and choice. Using models, they proved this subtheory consistent, and proved that each of the axioms of extensionality, replacement, and power set is independent of the four remaining axioms of this subtheory. If this subtheory is augmented with the axiom of infinity, each of the axioms of union, choice, and infinity is independent of the five remaining axioms. Because there are non-well-founded models that satisfy each axiom of ZFC except the axiom of regularity, that axiom is independent of the other ZFC axioms.

If consistent, ZFC cannot prove the existence of the inaccessible cardinals that category theory requires. Huge sets of this nature are possible if ZF is augmented with Tarski's axiom. Assuming that axiom turns the axioms of infinity, power set, and choice (7–9 above) into theorems.

### Independence

Many important statements are independent of ZFC. The independence is usually proved by forcing, whereby it is shown that every countable transitive model of ZFC (sometimes augmented with large cardinal axioms) can be expanded to satisfy the statement in question. A different expansion is then shown to satisfy the negation of the statement. An independence proof by forcing automatically proves independence from arithmetical statements, other concrete statements, and large cardinal axioms. Some statements independent of ZFC can be proven to hold in particular inner models, such as in the constructible universe. However, some statements that are true about constructible sets are not consistent with hypothesized large cardinal axioms.

Forcing proves that the following statements are independent of ZFC:

- Axiom of constructibility (V=L) (which is also not a ZFC axiom)
- Continuum hypothesis
- Diamond principle
- Martin's axiom (which is not a ZFC axiom)
- Suslin hypothesis

Remarks:

- The consistency of V=L is provable by inner models but not forcing: every model of ZF can be trimmed to become a model of ZFC + V=L.
- The diamond principle implies the continuum hypothesis and the negation of the Suslin hypothesis.
- Martin's axiom plus the negation of the continuum hypothesis implies the Suslin hypothesis.
- The constructible universe satisfies the generalized continuum hypothesis, the diamond principle, Martin's axiom and the Kurepa hypothesis.
- The failure of the Kurepa hypothesis is equiconsistent with the existence of a strongly inaccessible cardinal.

A variation on the method of forcing can also be used to demonstrate the consistency and unprovability of the axiom of choice, i.e., that the axiom of choice is independent of ZF. The consistency of choice can be (relatively) easily verified by proving that the inner model L satisfies choice. (Thus every model of ZF contains a submodel of ZFC, so that Con(ZF) implies Con(ZFC).) Since forcing preserves choice, we cannot directly produce a model contradicting choice from a model satisfying choice. However, we can use forcing to create a model which contains a suitable submodel, namely one satisfying ZF but not C.

Another method of proving independence results, one owing nothing to forcing, is based on Gödel's second incompleteness theorem. This approach employs the statement whose independence is being examined, to prove the existence of a set model of ZFC, in which case Con(ZFC) is true. Since ZFC satisfies the conditions of Gödel's second theorem, the consistency of ZFC is unprovable in ZFC (provided that ZFC is, in fact, consistent). Hence no statement allowing such a proof can be proved in ZFC. This method can prove that the existence of large cardinals is not provable in ZFC, but cannot prove that assuming such cardinals, given ZFC, is free of contradiction.

### Proposed additions

The project to unify set theorists behind additional axioms to resolve the continuum hypothesis or other meta-mathematical ambiguities is sometimes known as "Gödel's program". Mathematicians currently debate which axioms are the most plausible or "self-evident", which axioms are the most useful in various domains, and about to what degree usefulness should be traded off with plausibility; some "multiverse" set theorists argue that usefulness should be the sole ultimate criterion in which axioms to customarily adopt. One school of thought leans on expanding the "iterative" concept of a set to produce a set-theoretic universe with an interesting and complex but reasonably tractable structure by adopting forcing axioms; another school advocates for a tidier, less cluttered universe, perhaps focused on a "core" inner model.

## Criticisms

ZFC has been criticized both for being excessively strong and for being excessively weak, as well as for its failure to capture objects such as proper classes.

Many mathematical theorems can be proven in much weaker systems than ZFC, such as Peano arithmetic and second-order arithmetic (as explored by the program of reverse mathematics). Saunders Mac Lane and Solomon Feferman have both made this point. Some of "mainstream mathematics" (mathematics not directly connected with axiomatic set theory) is beyond Peano arithmetic and second-order arithmetic, but still, all such mathematics can be carried out in ZC (Zermelo set theory with choice), another theory weaker than ZFC. Much of the power of ZFC, including the axiom of regularity and the axiom schema of replacement, is included primarily to facilitate the study of the set theory itself.

On the other hand, among axiomatic set theories, ZFC is comparatively weak. Unlike New Foundations, ZFC does not admit the existence of a universal set. Hence the universe of sets under ZFC is not closed under the elementary operations of the algebra of sets. Unlike von Neumann–Bernays–Gödel set theory (NBG) and Morse–Kelley set theory (MK), ZFC does not admit the existence of proper classes. A further comparative weakness of ZFC is that the axiom of choice included in ZFC is weaker than the axiom of global choice included in NBG and MK.

There are numerous mathematical statements independent of ZFC. These include the continuum hypothesis, the Whitehead problem, and the normal Moore space conjecture. Some of these conjectures are provable with the addition of axioms such as Martin's axiom or large cardinal axioms to ZFC. Some others are decided in ZF+AD where AD is the axiom of determinacy, a strong supposition incompatible with choice. One attraction of large cardinal axioms is that they enable many results from ZF+AD to be established in ZFC adjoined by some large cardinal axiom. The Mizar system and metamath have adopted Tarski–Grothendieck set theory, an extension of ZFC, so that proofs involving Grothendieck universes (encountered in category theory and algebraic geometry) can be formalized.
