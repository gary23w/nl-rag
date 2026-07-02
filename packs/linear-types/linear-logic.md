---
title: "Linear logic"
source: https://en.wikipedia.org/wiki/Linear_logic
domain: linear-types
license: CC-BY-SA-4.0
tags: linear type system, linear logic, substructural type system, resource management
fetched: 2026-07-02
---

# Linear logic

**Linear logic** is a substructural logic proposed by French logician Jean-Yves Girard as a refinement of classical and intuitionistic logic, joining the dualities of the former with many of the constructive properties of the latter. Although the logic has also been studied for its own sake, more broadly, ideas from linear logic have been influential in fields such as programming languages, game semantics, and quantum physics (because linear logic can be seen as the logic of quantum information theory), as well as linguistics, particularly because of its emphasis on resource-boundedness, duality, and interaction.

Linear logic lends itself to many different presentations, explanations, and intuitions. Proof-theoretically, it derives from an analysis of classical sequent calculus in which uses of (the structural rules) contraction and weakening are carefully controlled. Operationally, this means that logical deduction is no longer merely about an ever-expanding collection of persistent "truths", but also a way of manipulating *resources* that cannot always be duplicated or thrown away at will. In terms of simple denotational models, linear logic may be seen as refining the interpretation of intuitionistic logic by replacing cartesian (closed) categories by symmetric monoidal (closed) categories, or the interpretation of classical logic by replacing Boolean algebras by C*-algebras.

## Notation comparison

This article follows Girard's notation. For readers who are familiar with different notations, the following table, compiled by Paoli 2002, compares the notations for linear-logic connectives and constants across several sources.

| Girard 1987 | Troelstra 1992 | Restall 2000 | Paoli 2002 |
|---|---|---|---|
| $\bot$ | $\sim$ | $\sim$ | $\neg$ |
| $\otimes$ | $\star$ | $\circ$ | $\otimes$ |
| ⅋ | + | + | $\oplus$ |
| $\&$ | $\sqcap$ | $\wedge$ | $\wedge$ |
| $\oplus$ | $\sqcup$ | $\vee$ | $\vee$ |
| $\multimap$ | $\multimap$ | $\rightarrow$ | $\rightarrow$ |
| ${\displaystyle$ | ${\displaystyle$ | ${\displaystyle$ | ${\displaystyle$ |
| ${\displaystyle$ | ${\displaystyle$ | ${\displaystyle$ | ${\displaystyle$ |
| $\mathbf {1}$ | $\mathbf {1}$ | $\mathbf {1}$ | $\mathbf {1}$ |
| $\bot$ | $\mathbf {0}$ | $\mathbf {0}$ | $\mathbf {0}$ |
| $\top$ | $\top$ | $\top$ | $\top$ |
| $\mathbf {0}$ | $\bot$ | $\bot$ | $\bot$ |

## Connectives, duality, and polarity

### Syntax

The language ${\mathcal {L}}$ of classical propositional linear logic can be defined recursively as follows.

1. If $\varphi$ is an atomic formula, then $\varphi$ is a formula of ${\mathcal {L}}$ .
2. If $\varphi$ is an atomic formula, then $\varphi ^{\bot }$ is a formula of ${\mathcal {L}}$ .
3. If $\varphi$ and $\psi$ are formulas of ${\mathcal {L}}$ , then $\varphi \otimes \psi$ is too.
4. If $\varphi$ and $\psi$ are formulas of ${\mathcal {L}}$ , then $\varphi$ ⅋ $\psi$ is too.
5. If $\varphi$ and $\psi$ are formulas of ${\mathcal {L}}$ , then $\varphi \ \&\ \psi$ is too.
6. If $\varphi$ and $\psi$ are formulas of ${\mathcal {L}}$ , then $\varphi \oplus \psi$ is too.
7. If $\varphi$ is a formula of ${\mathcal {L}}$ , then ${\displaystyle$ is too.
8. If $\varphi$ is a formula of ${\mathcal {L}}$ , then ${\displaystyle$ is too.
9. ${\bf {1}}$ is a formula of ${\mathcal {L}}$ .
10. $\bot$ is a formula of ${\mathcal {L}}$ .
11. $\top$ is a formula of ${\mathcal {L}}$ .
12. ${\bf {0}}$ is a formula of ${\mathcal {L}}$ .

Here *p* and *p*⊥ range over logical atoms. For reasons to be explained below, the connectives ⊗, ⅋, 1, and ⊥ are called *multiplicatives*, the connectives &, ⊕, ⊤, and 0 are called *additives*, and the connectives ! and ? are called *exponentials*. We can further employ the following terminology:

| Symbol | Name |   |   |
|---|---|---|---|
| ⊗ | multiplicative conjunction | times | tensor |
| ⊕ | additive disjunction | plus |   |
| & | additive conjunction | with |   |
| ⅋ | multiplicative disjunction | par |   |
| ! | of course | bang |   |
| ? | why not | quest |   |

Binary connectives ⊗, ⊕, & and ⅋ are associative and commutative; 1 is the unit for ⊗, 0 is the unit for ⊕, ⊥ is the unit for ⅋ and ⊤ is the unit for &.

Every proposition *A* in CLL has a **dual** *A*⊥, defined as follows:

| (*p*)⊥ = *p*⊥ | (*p*⊥)⊥ = *p* |
|---|---|
| (*A* ⊗ *B*)⊥ = *A*⊥ ⅋ *B*⊥ | (*A* ⅋ *B*)⊥ = *A*⊥ ⊗ *B*⊥ |
| (*A* ⊕ *B*)⊥ = *A*⊥ & *B*⊥ | (*A* & *B*)⊥ = *A*⊥ ⊕ *B*⊥ |
| (1)⊥ = ⊥ | (⊥)⊥ = 1 |
| (0)⊥ = ⊤ | (⊤)⊥ = 0 |
| (!*A*)⊥ = ?(*A*⊥) | (?*A*)⊥ = !(*A*⊥) |

|   | add | mul | exp |
|---|---|---|---|
| pos | ⊕ 0 | ⊗ 1 | ! |
| neg | & ⊤ | ⅋ ⊥ | ? |

Observe that (-)⊥ is an involution, i.e., *A*⊥⊥ = *A* for all propositions. *A*⊥ is also called the *linear negation* of *A*.

The columns of the table suggest another way of classifying the connectives of linear logic, termed ***polarity***: the connectives negated in the left column (⊗, ⊕, 1, 0, !) are called *positive*, while their duals on the right (⅋, &, ⊥, ⊤, ?) are called *negative*; cf. table on the right.

*Linear implication* is not included in the grammar of connectives, but is definable in CLL using linear negation and multiplicative disjunction, by *A* ⊸ *B*:= *A*⊥ ⅋ *B*. The connective ⊸ is sometimes pronounced "lollipop", owing to its shape.

## Sequent calculus presentation

One way of defining linear logic is as a sequent calculus. We use the letters Γ and Δ to range over finite lists of propositions *A*1, ..., *A**n*, also called *contexts*. A *sequent* places a context to the left and the right of the turnstile, written Γ $\vdash$ Δ. Intuitively, the sequent asserts that the conjunction of Γ entails the disjunction of Δ (though we mean the "multiplicative" conjunction and disjunction, as explained below). Girard describes classical linear logic using only *one-sided* sequents (where the left-hand context is empty), and we follow here that more economical presentation. This is possible because any premises to the left of a turnstile can always be moved to the other side and dualised.

We now give inference rules describing how to build proofs of sequents.

First, to formalize the fact that we do not care about the order of propositions inside a context, we add the structural rule of exchange:

| $\vdash$ Γ, A1, A2, Δ |
|---|
|   |
| $\vdash$ Γ, A2, A1, Δ |

Note that we do **not** add the structural rules of weakening and contraction, because we do care about the absence of propositions in a sequent, and the number of copies present.

Next we add *initial sequents* and *cuts*:

| $\vdash$ *A*, *A*⊥ |   | $\vdash$ Γ, *A* $\vdash$ *A*⊥, Δ $\vdash$ Γ, Δ |
|---|---|---|

The cut rule can be seen as a way of composing proofs, and initial sequents serve as the units for composition. In a certain sense these rules are redundant: as we introduce additional rules for building proofs below, we will obtain the property that arbitrary initial sequents can be derived from atomic initial sequents, and that whenever a sequent is provable it can be given a cut-free proof. Ultimately, this canonical form property (which can be divided into the completeness of atomic initial sequents and the cut-elimination theorem, inducing a notion of analytic proof) lies behind the applications of linear logic in computer science, since it allows the logic to be used in proof search and as a resource-aware lambda-calculus.

Now, we explain the connectives by giving *logical rules*. Typically in sequent calculus one gives both "right-rules" and "left-rules" for each connective, essentially describing two modes of reasoning about propositions involving that connective (e.g., verification and falsification). In a one-sided presentation, one instead makes use of negation: the right-rules for a connective (say ⅋) effectively play the role of left-rules for its dual (⊗). So, we should expect a certain "harmony" between the rule(s) for a connective and the rule(s) for its dual.

### Multiplicatives

The rules for multiplicative conjunction (⊗) and disjunction (⅋):

| $\vdash$ Γ, *A* $\vdash$ Δ, *B* $\vdash$ Γ, Δ, *A* ⊗ *B* |   | $\vdash$ Γ, *A*, *B* $\vdash$ Γ, *A* ⅋ *B* |
|---|---|---|

and for their units:

| $\vdash$ 1 |   | $\vdash$ Γ $\vdash$ Γ, ⊥ |
|---|---|---|

Observe that the rules for multiplicative conjunction and disjunction are admissible for plain *conjunction* and *disjunction* under a classical interpretation (i.e., they are admissible rules in LK).

### Additives

The rules for additive conjunction (&) and disjunction (⊕):

| $\vdash$ Γ, *A* $\vdash$ Γ, *B* $\vdash$ Γ, *A* & *B* |   | $\vdash$ Γ, *A* $\vdash$ Γ, *A* ⊕ *B* |   | $\vdash$ Γ, *B* $\vdash$ Γ, *A* ⊕ *B* |
|---|---|---|---|---|

and for their units:

| $\vdash$ Γ, ⊤ |   | (no rule for 0) |
|---|---|---|

Observe that the rules for additive conjunction and disjunction are again admissible under a classical interpretation. But now we can explain the basis for the multiplicative/additive distinction in the rules for the two different versions of conjunction: for the multiplicative connective (⊗), the context of the conclusion (Γ, Δ) is split up between the premises, whereas for the additive case connective (&) the context of the conclusion (Γ) is carried whole into both premises.

### Exponentials

The exponentials are used to give controlled access to weakening and contraction. Specifically, we add structural rules of weakening and contraction for ?'d propositions:

| $\vdash$ Γ $\vdash$ Γ, ?*A* |   | $\vdash$ Γ, ?*A*, ?*A* $\vdash$ Γ, ?*A* |
|---|---|---|

and use the following logical rules, in which ?Γ stands for a list of propositions each prefixed with ?:

| $\vdash$ ?Γ, *A* $\vdash$ ?Γ, !*A* |   | $\vdash$ Γ, *A* $\vdash$ Γ, ?*A* |
|---|---|---|

One might observe that the rules for the exponentials follow a different pattern from the rules for the other connectives, resembling the inference rules governing modalities in sequent calculus formalisations of the normal modal logic S4, and that there is no longer such a clear symmetry between the duals ! and ?. This situation is remedied in alternative presentations of CLL (e.g., the LU presentation).

## Remarkable formulas

In addition to the De Morgan dualities described above, some important equivalences in linear logic include:

**Distributivity**

| *A* ⊗ (*B* ⊕ *C*) ≣ (*A* ⊗ *B*) ⊕ (*A* ⊗ *C*) |
|---|
| (*A* ⊕ *B*) ⊗ *C* ≣ (*A* ⊗ *C*) ⊕ (*B* ⊗ *C*) |
| *A* ⅋ (*B* & *C*) ≣ (*A* ⅋ *B*) & (*A* ⅋ *C*) |
| (*A* & *B*) ⅋ *C* ≣ (*A* ⅋ *C*) & (*B* ⅋ *C*) |

By definition of *A* ⊸ *B* as *A*⊥ ⅋ *B*, the last two distributivity laws also give:

| *A* ⊸ (*B* & *C*) ≣ (*A* ⊸ *B*) & (*A* ⊸ *C*) |
|---|
| (*A* ⊕ *B*) ⊸ *C* ≣ (*A* ⊸ *C*) & (*B* ⊸ *C*) |

(Here *A* ≣ *B* is (*A* ⊸ *B*) & (*B* ⊸ *A*).)

**Exponential isomorphism**

| !(*A* & *B*) ≣ !*A* ⊗ !*B* |
|---|
| ?(*A* ⊕ *B*) ≣ ?*A* ⅋ ?*B* |

**Linear distributions**

A map that is not an isomorphism yet plays a crucial role in linear logic is:

| (*A* ⊗ (*B* ⅋ *C*)) ⊸ ((*A* ⊗ *B*) ⅋ *C*) |
|---|

Linear distributions are fundamental in the proof theory of linear logic. The consequences of this map were first investigated in Cockett & Seely (1997) and called a "weak distribution". In subsequent work it was renamed to "linear distribution" to reflect the fundamental connection to linear logic.

**Other implications**

The following distributivity formulas are not in general an equivalence, only an implication:

| !*A* ⊗ !*B* ⊸ !(*A* ⊗ *B*) |
|---|
| !*A* ⊕ !*B* ⊸ !(*A* ⊕ *B*) |

| ?(*A* ⅋ *B*) ⊸ ?*A* ⅋ ?*B* |
|---|
| ?(*A* & *B*) ⊸ ?*A* & ?*B* |

| (*A* & *B*) ⊗ *C* ⊸ (*A* ⊗ *C*) & (*B* ⊗ *C*) |
|---|
| (*A* & *B*) ⊕ *C* ⊸ (*A* ⊕ *C*) & (*B* ⊕ *C*) |

| (*A* ⅋ *C*) ⊕ (*B* ⅋ *C*) ⊸ (*A* ⊕ *B*) ⅋ *C* |
|---|
| (*A* & *C*) ⊕ (*B* & *C*) ⊸ (*A* ⊕ *B*) & *C* |

## Extending classical/intuitionistic logic

Both intuitionistic and classical implication can be recovered from linear implication by inserting exponentials: intuitionistic implication is encoded as !*A* ⊸ *B*, while classical implication can be encoded as !?*A* ⊸ ?*B* or !*A* ⊸ ?!*B* (or a variety of alternative possible translations). The idea is that exponentials allow us to use a formula as many times as we need, which is always possible in classical and intuitionistic logic.

Formally, there exists a translation of formulas of intuitionistic logic to formulas of linear logic in a way that guarantees that the original formula is provable in intuitionistic logic if and only if the translated formula is provable in linear logic. Using the Gödel–Gentzen negative translation, we can thus embed classical first-order logic into linear first-order logic.

## Proof systems

### Proof nets

Introduced by Jean-Yves Girard, proof nets have been created to avoid the *bureaucracy*, that is all the things that make two derivations different in the logical point of view, but not in a "moral" point of view.

For instance, these two proofs are "morally" identical:

| $\vdash$ *A*, *B*, *C*, *D* $\vdash$ *A* ⅋ *B*, *C*, *D* $\vdash$ *A* ⅋ *B*, *C* ⅋ *D* | $\vdash$ *A*, *B*, *C*, *D* $\vdash$ *A*, *B*, *C* ⅋ *D* $\vdash$ *A* ⅋ *B*, *C* ⅋ *D* |
|---|---|

The goal of proof nets is to make them identical by creating a graphical representation of them.

## Semantics

Multiple distinct semantics have been developed for linear logic, reflecting its complex nature as a resource-sensitive logical system. Unlike classical or intuitionistic logic, linear logic distinguishes between different ways of combining formulas and treats assumptions as finite resources that are consumed during proof rather than being endlessly reproducible.

The main semantic approaches include:

**Phase semantics**

An early model focusing on provability.

**Categorical semantics**

An algebraic framework that models proofs as

morphisms

. The appropriate category is a subcategory of complete, separated,

bornological vector space

with

continuous linear maps

.

**Game semantics**

An interactive model that interprets formulas as games and proofs as strategies.

**Denotational semantics**

A model that interprets proofs as mathematical objects.

The algebraic semantics of linear logic is that of quantales.

In linguistics, linear logic models grammatical parsing as deduction. In that circumstance, a valid parse tree corresponds to proving the existence of a sentence using implication rules encoding the grammar.

### The resource interpretation

Lafont (1993) first showed how intuitionistic linear logic can be explained as a logic of resources, so providing the logical language with access to formalisms that can be used for reasoning about resources within the logic itself, rather than, as in classical logic, by means of non-logical predicates and relations. Tony Hoare (1985) used purchases at a vending machine to illustrate the logic, and culinary transactions have become the traditional example to describe use of the connectives.

In particular, a *prix fixe* menu corresponds to a linear implication from the price to the meal; either

(Cash) ⊸ (Meal)

or equivalently

(Cash)

⊥

⅋ (Meal)

depending on if implication or par is taken to be the primitive connective. Different courses are then conjoined using tensor, as a purchased meal is guaranteed to consist of both. For example, one might define (Meal) as

(Meal)

:= (Appetizer) ⊗ (Main) ⊗ (Dessert) ⊗ (Drink)

The customer's choice is conjoined using &:

(Appetizer)

:= (Soup)

&

(Salad)

indicating that the customer must choose either a soup or a salad. Contrariwise, the restaurant's choice is disjoined using ⊕: if the dessert is seasonal fruits, then it might be well-modeled as

(Dessert)

:= (Summer berries) ⊕ (Apple slices) ⊕ (Winter pineapple) ⊕ (Cherries)

Finally, an all-you-can-eat/drink item is modeled with !:

(Drink)

:= (Coffee)

&

(Tea)

&

!(Tap water)

In the resource interpretation, the constant 1 denotes the absence of any resource, and so functions as the unit of ⊗ (any formula A is equivalent to *A* ⊗ 1). ⊤ is the unit for & and consumes any unneeded resources; 0 represents a product that cannot be made, and thus serves as the unit of ⊕ (a machine that might produce A or 0 is as good as a machine that always produces A, because it will never succeed in producing a 0); and ⊥ denotes unconsumable resources.

## Decidability/complexity of entailment

The entailment relation in full CLL is undecidable. When considering fragments of CLL, the decision problem has varying complexity:

- Multiplicative linear logic (MLL): only the multiplicative connectives. MLL entailment is NP-complete, even restricting to Horn clauses in the purely implicative fragment, or to atom-free formulas.
- Multiplicative-additive linear logic (MALL): only multiplicatives and additives (i.e., exponential-free). MALL entailment is PSPACE-complete.
- Multiplicative-exponential linear logic (MELL): only multiplicatives and exponentials. By reduction from the reachability problem for Petri nets, MELL entailment must be at least EXPSPACE-hard, although decidability itself has had the status of a longstanding open problem. In 2015, a proof of decidability was published in the journal *Theoretical Computer Science*, but was later shown erroneous.
- Affine linear logic (that is linear logic with weakening, an extension rather than a fragment) was shown to be decidable, in 1995.

## Variants

Many variations of linear logic arise by further tinkering with the structural rules:

- Affine logic, which forbids contraction but allows global weakening (a decidable extension).
- Strict logic or relevance logic, which forbids weakening but allows global contraction.
- Non-commutative logic or ordered logic, which removes the rule of exchange, in addition to barring weakening and contraction. In ordered logic, linear implication divides further into left-implication and right-implication.

Different intuitionistic variants of linear logic have been considered. When based on a single-conclusion sequent calculus presentation, like in ILL (Intuitionistic Linear Logic), the connectives ⅋, ⊥, and ? are absent, and linear implication is treated as a primitive connective. In FILL (Full Intuitionistic Linear Logic) the connectives ⅋, ⊥, and ? are present, linear implication is a primitive connective and, similarly to what happens in intuitionistic logic, all connectives (except linear negation) are independent. There are also first- and higher-order extensions of linear logic, whose formal development is somewhat standard (see first-order logic and higher-order logic).
