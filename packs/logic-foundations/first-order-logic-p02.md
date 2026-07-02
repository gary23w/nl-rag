---
title: "First-order logic (part 2/2)"
source: https://en.wikipedia.org/wiki/First-order_logic
domain: logic-foundations
license: CC-BY-SA-4.0
tags: propositional logic, first-order logic, boolean algebra, truth table, mathematical proof
fetched: 2026-07-02
part: 2/2
---

## Metalogical properties

One motivation for the use of first-order logic, rather than higher-order logic, is that first-order logic has many metalogical properties that stronger logics do not have. These results concern general properties of first-order logic itself, rather than properties of individual theories. They provide fundamental tools for the construction of models of first-order theories.

### Completeness and undecidability

Gödel's completeness theorem, proved by Kurt Gödel in 1929, establishes that there are sound, complete, effective deductive systems for first-order logic, and thus the first-order logical consequence relation is captured by finite provability. Naively, the statement that a formula φ logically implies a formula ψ depends on every model of φ; these models will in general be of arbitrarily large cardinality, and so logical consequence cannot be effectively verified by checking every model. However, it is possible to enumerate all finite derivations and search for a derivation of ψ from φ. If ψ is logically implied by φ, such a derivation will eventually be found. Thus first-order logical consequence is semidecidable: it is possible to make an effective enumeration of all pairs of sentences (φ,ψ) such that ψ is a logical consequence of φ.

Unlike propositional logic, first-order logic is undecidable (although semidecidable), provided that the language has at least one predicate of arity at least 2 (other than equality). This means that there is no decision procedure that determines whether arbitrary formulas are logically valid. This result was established independently by Alonzo Church and Alan Turing in 1936 and 1937, respectively, giving a negative answer to the Entscheidungsproblem posed by David Hilbert and Wilhelm Ackermann in 1928. Their proofs demonstrate a connection between the unsolvability of the decision problem for first-order logic and the unsolvability of the halting problem.

### Decidable fragments

There are systems weaker than full first-order logic for which the logical consequence relation is decidable. These include propositional logic and monadic predicate logic, which is first-order logic restricted to unary predicate symbols and no function symbols. Other logics with no function symbols which are decidable are the guarded fragment of first-order logic, as well as two-variable logic. The Bernays–Schönfinkel class of first-order formulas is also decidable. Decidable subsets of first-order logic are also studied in the framework of description logics. See (Pratt-Hartmann, 2023) for a monograph.

Examples of decidable fragments:

- C2, FOL with two variables and the counting quantifiers $\exists ^{\geq n}$ and $\exists ^{\leq n}$ .
- monadic first-order fragment (MFO, or Löwenheim fragment): FOL without equality, without function symbols, and with only unary predicate symbols.
- Löb–Gurevich fragment: FOL without equality, with only unary function symbols, and with only unary predicate symbols.
- Rabin fragment: FOL with equality, with exactly one unary function symbol, and with only unary predicate symbols.
- Bernays–Schönfinkel–Ramsey fragment: all relational first-order sentences in prenex normal form with $\exists ^{*}\forall ^{*}$ prefix and with equality.

### Löwenheim–Skolem theorem

The Löwenheim–Skolem theorem shows that if a first-order theory of cardinality λ has an infinite model, then it has models of every infinite cardinality greater than or equal to λ. One of the earliest results in model theory, it implies that it is not possible to characterize countability or uncountability in a first-order language with a countable signature. That is, there is no first-order formula φ(*x*) such that an arbitrary structure M satisfies φ if and only if the domain of discourse of M is countable (or, in the second case, uncountable).

The Löwenheim–Skolem theorem implies that infinite structures cannot be categorically axiomatized in first-order logic. For example, there is no first-order theory whose only model is the real line: any first-order theory with an infinite model also has a model of cardinality larger than the continuum. Since the real line is infinite, any theory satisfied by the real line is also satisfied by some nonstandard models. When the Löwenheim–Skolem theorem is applied to first-order set theories, the nonintuitive consequences are known as Skolem's paradox.

### Compactness theorem

The compactness theorem states that a set of first-order sentences has a model if and only if every finite subset of it has a model. This implies that if a formula is a logical consequence of an infinite set of first-order axioms, then it is a logical consequence of some finite number of those axioms. This theorem was proved first by Kurt Gödel as a consequence of the completeness theorem, but many additional proofs have been obtained over time. It is a central tool in model theory, providing a fundamental method for constructing models.

The compactness theorem has a limiting effect on which collections of first-order structures are elementary classes. For example, the compactness theorem implies that any theory that has arbitrarily large finite models has an infinite model. Thus, the class of all finite graphs is not an elementary class (the same holds for many other algebraic structures).

There are also more subtle limitations of first-order logic that are implied by the compactness theorem. For example, in computer science, many situations can be modeled as a directed graph of states (nodes) and connections (directed edges). Validating such a system may require showing that no "bad" state can be reached from any "good" state. Thus, one seeks to determine if the good and bad states are in different connected components of the graph. However, the compactness theorem can be used to show that connected graphs are not an elementary class in first-order logic, and there is no formula φ(*x*,*y*) of first-order logic, in the logic of graphs, that expresses the idea that there is a path from *x* to *y*. Connectedness can be expressed in second-order logic, however, but not with only existential set quantifiers, as $\Sigma _{1}^{1}$ also enjoys compactness.

### Lindström's theorem

Per Lindström showed that the metalogical properties just discussed actually characterize first-order logic in the sense that no stronger logic can also have those properties (Ebbinghaus and Flum 1994, Chapter XIII). Lindström defined a class of abstract logical systems, and a rigorous definition of the relative strength of a member of this class. He established two theorems for systems of this type:

- A logical system satisfying Lindström's definition that contains first-order logic and satisfies both the Löwenheim–Skolem theorem and the compactness theorem must be equivalent to first-order logic.
- A logical system satisfying Lindström's definition that has a semidecidable logical consequence relation and satisfies the Löwenheim–Skolem theorem must be equivalent to first-order logic.


## Limitations

Although first-order logic is sufficient for formalizing much of mathematics and is commonly used in computer science and other fields, it has certain limitations. These include limitations on its expressiveness and limitations of the fragments of natural languages that it can describe.

### Expressiveness

The Löwenheim–Skolem theorem shows that if a first-order theory has any infinite model, then it has infinite models of every cardinality. In particular, no first-order theory with an infinite model can be categorical. Thus, there is no first-order theory whose only model has the set of natural numbers as its domain, or whose only model has the set of real numbers as its domain. Many extensions of first-order logic, including infinitary logics and higher-order logics, are more expressive in the sense that they do permit categorical axiomatizations of the natural numbers or real numbers. This expressiveness comes at a metalogical cost, however: by Lindström's theorem, the compactness theorem and the downward Löwenheim–Skolem theorem cannot hold in any logic stronger than first-order.

### Formalizing natural languages

First-order logic is able to formalize many simple quantifier constructions in natural language, such as "every person who lives in Perth lives in Australia". Hence, first-order logic is used as a basis for knowledge representation languages, such as FO(.).

Still, there are complicated features of natural language that cannot be expressed in first-order logic. "Any logical system which is appropriate as an instrument for the analysis of natural language needs a much richer structure than first-order predicate logic".

| Type | Example | Comment |
|---|---|---|
| Quantification over properties | If John is self-satisfied, then there is at least one thing he has in common with Peter. | Example requires a quantifier over predicates, which cannot be implemented in single-sorted first-order logic: Zj → ∃X(Xj∧Xp). |
| Quantification over properties | Santa Claus has all the attributes of a sadist. | Example requires quantifiers over predicates, which cannot be implemented in single-sorted first-order logic: ∀X(∀x(Sx → Xx) → Xs). |
| Predicate adverbial | John is walking quickly. | Example cannot be analysed as Wj ∧ Qj; predicate adverbials are not the same kind of thing as second-order predicates such as colour. |
| Relative adjective | Jumbo is a small elephant. | Example cannot be analysed as Sj ∧ Ej; predicate adjectives are not the same kind of thing as second-order predicates such as colour. |
| Predicate adverbial modifier | John is walking very quickly. | — |
| Relative adjective modifier | Jumbo is terribly small. | An expression such as "terribly", when applied to a relative adjective such as "small", results in a new composite relative adjective "terribly small". |
| Prepositions | Mary is sitting next to John. | The preposition "next to" when applied to "John" results in the predicate adverbial "next to John". |


## Restrictions, extensions, and variations

There are many variations of first-order logic. Some of these are inessential in the sense that they merely change notation without affecting the semantics. Others change the expressive power more significantly, by extending the semantics through additional quantifiers or other new logical symbols. For example, infinitary logics permit formulas of infinite size, and modal logics add symbols for possibility and necessity.

### Restricted languages

First-order logic can be studied in languages with fewer logical symbols than were described above:

- Because $\exists x\varphi (x)$ can be expressed as $\neg \forall x\neg \varphi (x)$ , and $\forall x\varphi (x)$ can be expressed as $\neg \exists x\neg \varphi (x)$ , either of the two quantifiers $\exists$ and $\forall$ can be dropped.
- Since $\varphi \lor \psi$ can be expressed as $\lnot (\lnot \varphi \land \lnot \psi )$ and $\varphi \land \psi$ can be expressed as $\lnot (\lnot \varphi \lor \lnot \psi )$ , either $\vee$ or $\wedge$ can be dropped. In other words, it is sufficient to have $\neg$ and $\vee$ , or $\neg$ and $\wedge$ , as the only logical connectives.
- Similarly, it is sufficient to have only $\neg$ and $\rightarrow$ as logical connectives, or to have only the Sheffer stroke (NAND) or the Peirce arrow (NOR) operator.
- It is possible to entirely avoid function symbols and constant symbols, rewriting them via predicate symbols in an appropriate way. For example, instead of using a constant symbol $\;0$ one may use a predicate $\;0(x)$ (interpreted as $\;x=0$ ) and replace every predicate such as $\;P(0,y)$ with $\forall x\;(0(x)\rightarrow P(x,y))$ . A function such as $f(x_{1},x_{2},...,x_{n})$ will similarly be replaced by a predicate $F(x_{1},x_{2},...,x_{n},y)$ interpreted as $y=f(x_{1},x_{2},...,x_{n})$ . This change requires adding additional axioms to the theory at hand, so that interpretations of the predicate symbols used have the correct semantics.

Restrictions such as these are useful as a technique to reduce the number of inference rules or axiom schemas in deductive systems, which leads to shorter proofs of metalogical results. The cost of the restrictions is that it becomes more difficult to express natural-language statements in the formal system at hand, because the logical connectives used in the natural language statements must be replaced by their (longer) definitions in terms of the restricted collection of logical connectives. Similarly, derivations in the limited systems may be longer than derivations in systems that include additional connectives. There is thus a trade-off between the ease of working within the formal system and the ease of proving results about the formal system.

It is also possible to restrict the arities of function symbols and predicate symbols, in sufficiently expressive theories. One can in principle dispense entirely with functions of arity greater than 2 and predicates of arity greater than 1 in theories that include a pairing function. This is a function of arity 2 that takes pairs of elements of the domain and returns an ordered pair containing them. It is also sufficient to have two predicate symbols of arity 2 that define projection functions from an ordered pair to its components. In either case it is necessary that the natural axioms for a pairing function and its projections are satisfied.

### Many-sorted logic

Ordinary first-order interpretations have a single domain of discourse over which all quantifiers range. *Many-sorted first-order logic* allows variables to have different *sorts*, which have different domains. This is also called *typed first-order logic*, and the sorts called *types* (as in data type), but it is not the same as first-order type theory. Many-sorted first-order logic is often used in the study of second-order arithmetic.

When there are only finitely many sorts in a theory, many-sorted first-order logic can be reduced to single-sorted first-order logic. One introduces into the single-sorted theory a unary predicate symbol for each sort in the many-sorted theory and adds an axiom saying that these unary predicates partition the domain of discourse. For example, if there are two sorts, one adds predicate symbols $P_{1}(x)$ and $P_{2}(x)$ and the axiom:

$\forall x(P_{1}(x)\lor P_{2}(x))\land \lnot \exists x(P_{1}(x)\land P_{2}(x))$

.

Then the elements satisfying $P_{1}$ are thought of as elements of the first sort, and elements satisfying $P_{2}$ as elements of the second sort. One can quantify over each sort by using the corresponding predicate symbol to limit the range of quantification. For example, to say there is an element of the first sort satisfying formula $\varphi (x)$ , one writes:

$\exists x(P_{1}(x)\land \varphi (x))$

.

### Additional quantifiers

Additional quantifiers can be added to first-order logic.

- Sometimes it is useful to say that "*P*(*x*) holds for exactly one *x*", which can be expressed as ∃!*x* *P*(*x*). This notation, called uniqueness quantification, may be taken to abbreviate a formula such as ∃*x* (*P*(*x*) $\wedge$ ∀*y* (*P*(*y*) → (*x* = *y*))).
- *First-order logic with extra quantifiers* has new quantifiers *Qx*,..., with meanings such as "there are many *x* such that ...". Also see branching quantifiers and the plural quantifiers of George Boolos and others.
- *Bounded quantifiers* are often used in the study of set theory or arithmetic.

### Infinitary logics

Infinitary logic allows infinitely long sentences. For example, one may allow a conjunction or disjunction of infinitely many formulas, or quantification over infinitely many variables. Infinitely long sentences arise in areas of mathematics including topology and model theory.

Infinitary logic generalizes first-order logic to allow formulas of infinite length. The most common way in which formulas can become infinite is through infinite conjunctions and disjunctions. However, it is also possible to admit generalized signatures in which function and relation symbols are allowed to have infinite arities, or in which quantifiers can bind infinitely many variables. Because an infinite formula cannot be represented by a finite string, it is necessary to choose some other representation of formulas; the usual representation in this context is a tree. Thus, formulas are, essentially, identified with their parse trees, rather than with the strings being parsed.

The most commonly studied infinitary logics are denoted *L*αβ, where α and β are each either cardinal numbers or the symbol ∞. In this notation, ordinary first-order logic is *L*ωω. In the logic *L*∞ω, arbitrary conjunctions or disjunctions are allowed when building formulas, and there is an unlimited supply of variables. More generally, the logic that permits conjunctions or disjunctions with less than κ constituents is known as *L*κω. For example, *L*ω1ω permits countable conjunctions and disjunctions.

The set of free variables in a formula of *L*κω can have any cardinality strictly less than κ, yet only finitely many of them can be in the scope of any quantifier when a formula appears as a subformula of another. In other infinitary logics, a subformula may be in the scope of infinitely many quantifiers. For example, in *L*κ∞, a single universal or existential quantifier may bind arbitrarily many variables simultaneously. Similarly, the logic *L*κλ permits simultaneous quantification over fewer than λ variables, as well as conjunctions and disjunctions of size less than κ.

### Non-classical and modal logics

- *Intuitionistic first-order logic* uses intuitionistic rather than classical reasoning; for example, ¬¬φ need not be equivalent to φ and ¬ ∀x.φ is in general not equivalent to ∃ x.¬φ .
- First-order *modal logic* allows one to describe other possible worlds as well as this contingently true world which we inhabit. In some versions, the set of possible worlds varies depending on which possible world one inhabits. Modal logic has extra *modal operators* with meanings which can be characterized informally as, for example "it is necessary that φ" (true in all possible worlds) and "it is possible that φ" (true in some possible world). With standard first-order logic we have a single domain, and each predicate is assigned one extension. With first-order modal logic we have a *domain function* that assigns each possible world its own domain, so that each predicate gets an extension only relative to these possible worlds. This allows us to model cases where, for example, Alex is a philosopher, but might have been a mathematician, and might not have existed at all. In the first possible world *P*(*a*) is true, in the second *P*(*a*) is false, and in the third possible world there is no *a* in the domain at all.
- *First-order fuzzy logics* are first-order extensions of propositional fuzzy logics rather than classical propositional calculus.

### Fixpoint logic

Fixpoint logic extends first-order logic by adding the closure under the least fixed points of positive operators.

### Higher-order logics

The characteristic feature of first-order logic is that individuals can be quantified, but not predicates. Thus

$\exists a({\text{Phil}}(a))$

is a legal first-order formula, but

$\exists {\text{Phil}}({\text{Phil}}(a))$

is not, in most formalizations of first-order logic. Second-order logic extends first-order logic by adding the latter type of quantification. Other higher-order logics allow quantification over even higher types than second-order logic permits. These higher types include relations between relations, functions from relations to relations between relations, and other higher-type objects. Thus the "first" in first-order logic describes the type of objects that can be quantified.

Unlike first-order logic, for which only one semantics is studied, there are several possible semantics for second-order logic. The most commonly employed semantics for second-order and higher-order logic is known as *full semantics*. The combination of additional quantifiers and the full semantics for these quantifiers makes higher-order logic stronger than first-order logic. In particular, the (semantic) logical consequence relation for second-order and higher-order logic is not semidecidable; there is no effective deduction system for second-order logic that is sound and complete under full semantics.

Second-order logic with full semantics is more expressive than first-order logic. For example, it is possible to create axiom systems in second-order logic that uniquely characterize the natural numbers and the real line. The cost of this expressiveness is that second-order and higher-order logics have fewer attractive metalogical properties than first-order logic. For example, the Löwenheim–Skolem theorem and compactness theorem of first-order logic become false when generalized to higher-order logics with full semantics.


## Automated theorem proving and formal methods

Automated theorem proving refers to the development of computer programs that search and find derivations (formal proofs) of mathematical theorems. Finding derivations is a difficult task because the search space can be very large; an exhaustive search of every possible derivation is theoretically possible but computationally infeasible for many systems of interest in mathematics. Thus complicated heuristic functions are developed to attempt to find a derivation in less time than a blind search.

The related area of automated proof verification uses computer programs to check that human-created proofs are correct. Unlike complicated automated theorem provers, verification systems may be small enough that their correctness can be checked both by hand and through automated software verification. This validation of the proof verifier is needed to give confidence that any derivation labeled as "correct" is actually correct.

Some proof verifiers, such as Metamath, insist on having a complete derivation as input. Others, such as Mizar and Isabelle, take a well-formatted proof sketch (which may still be very long and detailed) and fill in the missing pieces by doing simple proof searches or applying known decision procedures: the resulting derivation is then verified by a small core "kernel". Many such systems are primarily intended for interactive use by human mathematicians: these are known as proof assistants. They may also use formal logics that are stronger than first-order logic, such as type theory. Because a full derivation of any nontrivial result in a first-order deductive system will be extremely long for a human to write, results are often formalized as a series of lemmas, for which derivations can be constructed separately.

Automated theorem provers are also used to implement formal verification in computer science. In this setting, theorem provers are used to verify the correctness of programs and of hardware such as processors with respect to a formal specification. Because such analysis is time-consuming and thus expensive, it is usually reserved for projects in which a malfunction would have grave human or financial consequences.

For the problem of model checking, efficient algorithms are known to decide whether an input finite structure satisfies a first-order formula, in addition to computational complexity bounds: see Model checking § First-order logic.
