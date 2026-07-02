---
title: "Theory (mathematical logic)"
source: https://en.wikipedia.org/wiki/First-order_theory
domain: model-theory
license: CC-BY-SA-4.0
tags: model theory, compactness theorem, elementary equivalence, quantifier elimination
fetched: 2026-07-02
---

# Theory (mathematical logic)

(Redirected from

First-order theory

)

In mathematical logic, a **theory** (also called a **formal theory**) is a set of sentences in a formal language. In most scenarios a deductive system is first understood from context, giving rise to a formal system that combines the language with deduction rules. An element $\phi \in T$ of a deductively closed theory T is then called a theorem of the theory. In many deductive systems there is usually a subset $\Sigma \subseteq T$ that is called "the set of axioms" of the theory T , in which case the deductive system is also called an "axiomatic system". By definition, every axiom is automatically a theorem. A **first-order theory** is a set of first-order sentences (theorems) recursively obtained by the inference rules of the system applied to the set of axioms.

## General theories (as expressed in formal language)

When defining theories for foundational purposes, additional care must be taken, as normal set-theoretic language may not be appropriate.

The construction of a theory begins by specifying a definite non-empty *conceptual class* ${\mathcal {E}}$ , the elements of which are called *statements*. These initial statements are often called the *primitive elements* or *elementary* statements of the theory—to distinguish them from other statements that may be derived from them.

A theory ${\mathcal {T}}$ is a conceptual class consisting of certain of these elementary statements. The elementary statements that belong to ${\mathcal {T}}$ are called the *elementary theorems* of ${\mathcal {T}}$ and are said to be *true*. In this way, a theory can be seen as a way of designating a subset of ${\mathcal {E}}$ that only contain statements that are true.

This general way of designating a theory stipulates that the truth of any of its elementary statements is not known without reference to ${\mathcal {T}}$ . Thus the same elementary statement may be true with respect to one theory but false with respect to another. This is reminiscent of the case in ordinary language where statements such as "He is an honest person" cannot be judged true or false without interpreting who "he" is, and, for that matter, what an "honest person" is under this theory.

### Subtheories and extensions

A theory *${\mathcal {S}}$* is a **subtheory** of a theory *${\mathcal {T}}$* if *${\mathcal {S}}$* is a subset of *${\mathcal {T}}$*. If *${\mathcal {T}}$* is a subset of *${\mathcal {S}}$* then *${\mathcal {S}}$* is called an **extension** or a **supertheory** of *${\mathcal {T}}$*.

### Deductive theories

A theory is said to be a *deductive theory* if ${\mathcal {T}}$ is an inductive class, which is to say that its content is based on some formal deductive system and that some of its elementary statements are taken as axioms. In a deductive theory, any sentence that is a logical consequence of one or more of the axioms is also a sentence of that theory. More formally, if $\vdash$ is a Tarski-style consequence relation, then ${\mathcal {T}}$ is closed under $\vdash$ (and so each of its theorems is a logical consequence of its axioms) if and only if, for all sentences $\phi$ in the language of the theory ${\mathcal {T}}$ , if ${\mathcal {T}}\vdash \phi$ , then $\phi \in {\mathcal {T}}$ ; or, equivalently, if ${\mathcal {T}}'$ is a finite subset of ${\mathcal {T}}$ (possibly the set of axioms of ${\mathcal {T}}$ in the case of finitely axiomatizable theories) and ${\mathcal {T}}'\vdash \phi$ , then $\phi \in {\mathcal {T}}'$ , and therefore $\phi \in {\mathcal {T}}$ .

### Consistency and completeness

A **syntactically consistent theory** is a theory from which not every sentence in the underlying language can be proven (with respect to some deductive system, which is usually clear from context). In a deductive system (such as first-order logic) that satisfies the principle of explosion, this is equivalent to requiring that there is no sentence φ such that both φ and its negation can be proven from the theory.

A **satisfiable theory** is a theory that has a model. This means there is a structure *M* that satisfies every sentence in the theory. Any satisfiable theory is syntactically consistent, because the structure satisfying the theory will satisfy exactly one of φ and the negation of φ, for each sentence φ.

A **consistent theory** is sometimes defined to be a syntactically consistent theory, and sometimes defined to be a satisfiable theory. For first-order logic, the most important case, it follows from the completeness theorem that the two meanings coincide. In other logics, such as second-order logic, there are syntactically consistent theories that are not satisfiable, such as ω-inconsistent theories.

A complete consistent theory (or just a **complete theory**) is a consistent theory *${\mathcal {T}}$* such that for every sentence φ in its language, either φ is provable from *${\mathcal {T}}$* or *${\mathcal {T}}$* $\cup$ {φ} is inconsistent. For theories closed under logical consequence, this means that for every sentence φ, either φ or its negation is contained in the theory. An **incomplete theory** is a consistent theory that is not complete.

(See also **ω-consistent theory** for a stronger notion of consistency.)

### Interpretation of a theory

An *interpretation of a theory* is the relationship between a theory and some subject matter when there is a many-to-one correspondence between certain elementary statements of the theory, and certain statements related to the subject matter. If every elementary statement in the theory has a correspondent it is called a *full interpretation*, otherwise it is called a *partial interpretation*.

### Theories associated with a structure

Each structure has several associated theories. The **complete theory** of a structure *A* is the set of all first-order sentences over the signature of *A* that are satisfied by *A*. It is denoted by Th(*A*). More generally, the **theory** of *K*, a class of σ-structures, is the set of all first-order σ-sentences that are satisfied by all structures in *K*, and is denoted by Th(*K*). Clearly Th(*A*) = Th({*A*}). These notions can also be defined with respect to other logics.

For each σ-structure *A*, there are several associated theories in a larger signature σ' that extends σ by adding one new constant symbol for each element of the domain of *A*. (If the new constant symbols are identified with the elements of *A* that they represent, σ' can be taken to be σ $\cup$ A.) The cardinality of σ' is thus the larger of the cardinality of σ and the cardinality of *A*.

The **diagram** of *A* consists of all atomic or negated atomic σ'-sentences that are satisfied by *A* and is denoted by diag*A*. The **positive diagram** of *A* is the set of all atomic σ'-sentences that *A* satisfies. It is denoted by diag+*A*. The **elementary diagram** of *A* is the set eldiag*A* of *all* first-order σ'-sentences that are satisfied by *A* or, equivalently, the complete (first-order) theory of the natural expansion of *A* to the signature σ'.

## First-order theories

A first-order theory ${\mathcal {QS}}$ is a set of sentences in a first-order formal language ${\mathcal {Q}}$ .

### Derivation in a first-order theory

There are many formal derivation ("proof") systems for first-order logic. These include Hilbert-style deductive systems, natural deduction, the sequent calculus, the tableaux method and resolution.

### Syntactic consequence in a first-order theory

A formula *A* is a **syntactic consequence** of a first-order theory ${\mathcal {QS}}$ if there is a derivation of *A* using only formulas in ${\mathcal {QS}}$ as non-logical axioms. Such a formula *A* is also called a theorem of ${\mathcal {QS}}$ . The notation " ${\mathcal {QS}}\vdash A$ " indicates *A* is a theorem of ${\mathcal {QS}}$ .

### Interpretation of a first-order theory

An **interpretation** of a first-order theory provides a semantics for the formulas of the theory. An interpretation is said to satisfy a formula if the formula is true according to the interpretation. A **model** of a first-order theory ${\mathcal {QS}}$ is an interpretation in which every formula of ${\mathcal {QS}}$ is satisfied.

### First-order theories with identity

A first-order theory ${\mathcal {QS}}$ is a first-order theory with identity if ${\mathcal {QS}}$ includes the identity relation symbol "=" and the reflexivity and substitution axiom schemes for this symbol.

- Compactness theorem
- Consistent set
- Deduction theorem
- Lindenbaum's lemma
- Löwenheim–Skolem theorem

## Theory specification

A direct way to specify a theory is to define a set of axioms in a formal language. The theory then includes those axioms, and their provable consequences. Theories obtained this way include ZFC and Peano arithmetic.

A second way to specify a theory is to begin with a structure, and let the theory be the set of sentences that are satisfied by the structure. This is a method for producing complete theories through the semantic route, with examples including the set of true sentences under the structure (**N**, +, ×, 0, 1, =), where **N** is the set of natural numbers, and the set of true sentences under the structure (**R**, +, ×, 0, 1, =), where **R** is the set of real numbers. The first of these, called the theory of true arithmetic, cannot be written as the set of logical consequences of any enumerable set of axioms. The theory of (**R**, +, ×, 0, 1, =) was shown by Tarski to be decidable; it is the theory of real closed fields (see Decidability of first-order theories of the real numbers for more).
