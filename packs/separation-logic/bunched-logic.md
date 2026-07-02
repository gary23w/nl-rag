---
title: "Bunched logic"
source: https://en.wikipedia.org/wiki/Bunched_logic
domain: separation-logic
license: CC-BY-SA-4.0
tags: separation logic, separating conjunction, heap assertion, frame rule
fetched: 2026-07-02
---

# Bunched logic

**Bunched logic** is a variety of substructural logic proposed by Peter O'Hearn and David Pym. Bunched logic provides primitives for reasoning about *resource composition*, which aid in the compositional analysis of computer and other systems. It has category-theoretic and truth-functional semantics, which can be understood in terms of an abstract concept of resource, and a proof theory in which the contexts Γ in an entailment judgement Γ ⊢ A are tree-like structures (bunches) rather than lists or (multi)sets as in most proof calculi. Bunched logic has an associated type theory, and its first application was in providing a way to control the aliasing and other forms of interference in imperative programs. The logic has seen further applications in program verification, where it is the basis of the assertion language of separation logic, and in systems modelling, where it provides a way to decompose the resources used by components of a system.

## Foundations

The deduction theorem of classical logic relates conjunction and implication:

$A\wedge B\vdash C\quad {\mbox{iff}}\quad A\vdash B\Rightarrow C$

Bunched logic has two versions of the deduction theorem:

$A*B\vdash C\quad {\mbox{iff}}\quad A\vdash B{-\!\!*}C\qquad {\mbox{and also}}\qquad A\wedge B\vdash C\quad {\mbox{iff}}\quad A\vdash B\Rightarrow C$

$A*B$ and $B{-\!\!*}C$ are forms of conjunction and implication that take resources into account (explained below). In addition to these connectives bunched logic has a formula, sometimes written I or emp, which is the unit of *. In the original version of bunched logic $\wedge$ and $\Rightarrow$ were the connectives from intuitionistic logic, while a boolean variant takes $\wedge$ and $\Rightarrow$ (and $\neg$ ) as from traditional boolean logic. Thus, bunched logic is compatible with constructive principles, but is in no way dependent on them.

### Truth-functional semantics (resource semantics)

The easiest way to understand these formulae is in terms of its truth-functional semantics. In this semantics a formula is true or false with respect to given resources. $A*B$ asserts that the resource at hand can be decomposed into resources that satisfy A and B . $B{-\!\!*}C$ says that if we compose the resource at hand with additional resource that satisfies B , then the combined resource satisfies C . $\wedge$ and $\Rightarrow$ have their familiar meanings.

The foundation for this reading of formulae was provided by a forcing semantics $r\models A$ advanced by Pym, where the forcing relation means '*A* holds of resource *r*'. The semantics is analogous to Kripke's semantics of intuitionistic or modal logic, but where the elements of the model are regarded as resources that can be composed and decomposed, rather than as possible worlds that are accessible from one another. For example, the forcing semantics for the conjunction is of the form

$r\models A*B\quad {\mbox{iff}}\quad \exists r_{A}r_{B}.\,r_{A}\models A,\,r_{B}\models B,\,{\mbox{and}}\,r_{A}\bullet r_{B}\leq r$

where $r_{A}\bullet r_{B}$ is a way of combining resources and $\leq$ is a relation of approximation.

This semantics of bunched logic draws on prior work in relevance logic (especially the operational semantics of Routley–Meyer), but differs from it by not requiring $r\bullet r\leq r$ and by accepting the semantics of standard intuitionistic or classical versions of $\wedge$ and $\Rightarrow$ . The property $r\bullet r\leq r$ is justified when thinking about relevance but denied by considerations of resource; having two copies of a resource is not the same as having one, and in some models (e.g. heap models) $r\bullet r$ might not even be defined. The standard semantics of $\Rightarrow$ (or of negation) is often rejected by relevantists in their bid to escape the `paradoxes of material implication', which are not a problem from the perspective of modelling resources and so not rejected by bunched logic. The semantics is also related to the 'phase semantics' of linear logic, but again is differentiated by accepting the standard (even boolean) semantics of $\wedge$ and $\Rightarrow$ , which in linear logic is rejected in a bid to be constructive. These considerations are discussed in detail in an article on resource semantics by Pym, O'Hearn and Yang.

### Categorical semantics (doubly closed categories)

The double version of the deduction theorem of bunched logic has a corresponding category-theoretic structure. Proofs in intuitionistic logic can be interpreted in cartesian closed categories, that is, categories with finite products satisfying the (natural in *A* and *C*) adjunction correspondence relating hom sets:

$Hom(A\wedge B,C)\quad {\mbox{is isomorphic to}}\quad Hom(A,B\Rightarrow C)$

Bunched logic can be interpreted in categories possessing two such structures

a categorical model of bunched logic is a single category possessing two closed structures, one symmetric monoidal closed the other cartesian closed.

A host of categorial models can be given using Day's tensor product construction. Additionally, the implicational fragment of bunched logic has been given a game semantics.

### Algebraic semantics

The algebraic semantics of bunched logic is a special case of its categorical semantics, but is simple to state and can be more approachable.

An algebraic model of bunched logic is a poset that is a

Heyting algebra

and that carries an additional commutative

residuated lattice

structure (for the same lattice as the Heyting algebra): that is, an ordered commutative

monoid

with an associated implication satisfying

$A*B\leq C\quad {\mbox{iff}}\quad A\leq B{-\!\!*}C$

.

The boolean version of bunched logic has models as follows.

An algebraic model of boolean bunched logic is a poset that is a

Boolean algebra

and that carries an additional residuated commutative monoid structure.

### Proof theory and type theory (bunches)

The proof calculus of bunched logic differs from usual sequent calculi in having a tree-like context of hypotheses instead of a flat list-like structure. In its sequent-based proof theories, the context $\Delta$ in an entailment judgement $\Delta \vdash A$ is a finite rooted tree whose leaves are propositions and whose internal nodes are labelled with modes of composition corresponding to the two conjunctions. The two combining operators, comma and semicolon, are used (for instance) in the introduction rules for the two implications.

${\frac {\Gamma ,A\vdash B}{\Gamma \vdash A{-\!\!*}B}}\qquad \qquad {\frac {\Gamma ;A\vdash B}{\Gamma \vdash A{\Rightarrow }B}}$

The difference between the two composition rules comes from additional rules that apply to them.

- Multiplicative composition $\Delta ,\Gamma$ denies the structural rules of weakening and contraction.
- Additive composition ${\displaystyle \Delta$ admits weakening and contraction of entire bunches.

The structural rules and other operations on bunches are often applied deep within a tree-context, and not only at the top level: it is thus in a sense a calculus of deep inference.

Corresponding to bunched logic is a type theory having two kinds of function type. Following the Curry–Howard correspondence, introduction rules for implications correspond to introduction rules for function types.

${\frac {\Gamma ,x:A\vdash M:B}{\Gamma \vdash \lambda x.M:A{-\!\!*}B}}\qquad \qquad {\frac {\Gamma ;x:A\vdash M:B}{\Gamma \vdash \alpha x.M:A{\Rightarrow }B}}$

Here, there are two distinct binders, $\lambda$ and $\alpha$ , one for each kind of function type.

The proof theory of bunched logic has an historical debt to the use of bunches in relevance logic. But the bunched structure can in a sense be derived from the categorical and algebraic semantics: to formulate an introduction rule for ${-\!\!*}$ we should mimick * on the left in sequents, and to introduce $\Rightarrow$ we should mimick $\wedge$ . This consideration leads to the use of two combining operators.

James Brotherston has done further significant work on a unified proof theory for bunched logic and variants, employing Belnap's notion of display logic.

Galmiche, Méry, and Pym have provided a comprehensive treatment of bunched logic, including completeness and other meta-theory, based on labelled tableaux.

## Applications

### Interference control

In perhaps the first use of substructural type theory to control resources, John C. Reynolds showed how to use an affine type theory to control aliasing and other forms of interference in ALGOL-like programming languages. O'Hearn used bunched type theory to extend Reynolds' system by allowing interference and non-interference to be more flexibly mixed. This resolved open problems concerning recursion and jumps in Reynolds' system.

### Separation logic

Separation logic is an extension of Hoare logic that facilitates reasoning about mutable data structures that use pointers. Following Hoare logic the formulae of separation logic are of the form $\{Pre\}program\{Post\}$ , but the preconditions and postconditions are formulae interpreted in a model of bunched logic. The original version of the logic was based on models as follows:

- $Heaps=L\rightharpoonup _{f}V\qquad$ (finite partial functions from locations to values)
- $h_{0}\bullet h_{1}=$ union of heaps with disjoint domains, undefined when domains overlap.

It is the undefinedness of the composition on overlapping heaps that models the separation idea. This is a model of the boolean variant of bunched logic.

Separation logic was used originally to prove properties of sequential programs, but then was extended to concurrency using a proof rule

${\frac {\{P_{1}\}C_{1}\{Q_{1}\}\quad \{P_{2}\}C_{2}\{Q_{2}\}}{\{P_{1}*P_{2}\}C_{1}\parallel C_{2}\{Q_{1}*Q_{2}\}}}$

that divides the storage accessed by parallel threads.

Later, the greater generality of the resource semantics was utilized: an abstract version of separation logic works for Hoare triples where the preconditions and postconditions are formulae interpreted over an arbitrary partial commutative monoid instead of a particular heap model. By suitable choice of commutative monoid, it was surprisingly found that the proofs rules of abstract versions of concurrent separation logic could be used to reason about interfering concurrent processes, for example by encoding rely-guarantee and trace-based reasoning.

Separation logic is the basis of a number of tools for automatic and semi-automatic reasoning about programs, and is used in the Infer program analyzer currently deployed at Facebook.

### Resources and processes

Bunched logic has been used in connection with the (synchronous) resource-process calculus SCRP in order to give a (modal) logic that characterizes, in the sense of Hennessy–Milner, the compositional structure of concurrent systems.

SCRP is notable for interpreting $A*B$ in terms of *both* parallel composition of systems and composition of their associated resources. The semantic clause of SCRP's process logic that corresponds to separation logic's rule for concurrency asserts that a formula $A*B$ is true in resource-process state R , E just in case there are decompositions of the resource $R=S\bullet T$ and process E ~ $F\times G$ , where ~ denotes bisimulation, such that A is true in the resource-process state S , F and B is true in the resource-process state T , G ; that is $R,E\models A$ iff $S,F\models A$ and $T,G\models B$ .

The system SCRP is based directly on bunched logic's resource semantics; that is, on ordered monoids of resource elements. While direct and intuitively appealing, this choice leads to a specific technical problem: the Hennessy–Milner completeness theorem holds only for fragments of the modal logic that exclude the multiplicative implication and multiplicative modalities. This problem is solved by basing resource-process calculus on a resource semantics in which resource elements are combined using two combinators, one corresponding to concurrent composition and one corresponding to choice.

### Spatial logics

Cardelli, Caires, Gordon and others have investigated a series of logics of process calculi, where a conjunction is interpreted in terms of parallel composition. Unlike the work of Pym et al. in SCRP, they do not distinguish between parallel composition of systems and composition of resources accessed by the systems.

Their logics are based on instances of the resource semantics that give rise to models of the boolean variant of bunched logic. Although these logics give rise to instances of boolean bunched logic, they appear to have been arrived at independently, and in any case have significant additional structure in the way of modalities and binders. Related logics have been proposed as well for modelling XML data.
