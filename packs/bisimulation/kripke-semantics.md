---
title: "Kripke semantics"
source: https://en.wikipedia.org/wiki/Kripke_semantics
domain: bisimulation
license: CC-BY-SA-4.0
tags: bisimulation relation, bisimulation equivalence, coinductive proof, labelled transition system
fetched: 2026-07-02
---

# Kripke semantics

**Kripke semantics** (also known as **relational semantics** or **frame semantics**, and often confused with possible world semantics) is a formal semantics for non-classical logic systems created in the late 1950s and early 1960s by Saul Kripke and André Joyal. It was first conceived for modal logics, and later adapted to intuitionistic logic and other non-classical systems. The development of Kripke semantics was a breakthrough in the theory of non-classical logics, because the model theory of such logics was almost non-existent before Kripke (algebraic semantics existed, but were considered 'syntax in disguise').

## Semantics of modal logic

The language of propositional modal logic consists of a countably infinite set of propositional variables, a set of truth-functional connectives (in this article $\to$ and $\neg$ ), and the modal operator $\Box$ ("necessarily"). The modal operator $\Diamond$ ("possibly") is (classically) the dual of $\Box$ and may be defined in terms of necessity like so: $\Diamond A:=\neg \Box \neg A$ ("possibly A" is defined as equivalent to "not necessarily not A").

### Basic definitions

A **Kripke frame** or **modal frame** is a pair $\langle W,R\rangle$ , where *W* is a (possibly empty) set, and *R* is a binary relation on *W*. Elements of *W* are called *nodes* or *worlds*, and *R* is known as the accessibility relation.

A **Kripke model** is a triplet $\langle W,R,\Vdash \rangle$ , where $\langle W,R\rangle$ is a Kripke frame, and $\Vdash$ is a relation between nodes of *W* and modal formulas, such that for all *w* ∈ *W* and modal formulas *A* and *B*:

- $w\Vdash \neg A$ if and only if $w\nVdash A$ ,
- $w\Vdash A\to B$ if and only if $w\nVdash A$ or $w\Vdash B$ ,
- $w\Vdash \Box A$ if and only if $u\Vdash A$ for all u such that $w\;R\;u$ .

We read $w\Vdash A$ as “*w* satisfies *A*”, “*A* is satisfied in *w*”, or “*w* forces *A*”. The relation $\Vdash$ is called the *satisfaction relation*, *evaluation*, or *forcing relation*. The satisfaction relation is uniquely determined by its value on propositional variables.

A formula *A* is **valid** in:

- a model $\langle W,R,\Vdash \rangle$ , if $w\Vdash A$ for all $w\in W$ ,
- a frame $\langle W,R\rangle$ , if it is valid in $\langle W,R,\Vdash \rangle$ for all possible choices of $\Vdash$ ,
- a class *C* of frames or models, if it is valid in every member of *C*.

We define Thm(*C*) to be the set of all formulas that are valid in *C*. Conversely, if *X* is a set of formulas, let Mod(*X*) be the class of all frames which validate every formula from *X*.

A modal logic (i.e., a set of formulas) *L* is **sound** with respect to a class of frames *C*, if *L* ⊆ Thm(*C*). *L* is **complete** wrt *C* if *L* ⊇ Thm(*C*).

### Correspondence and completeness

Semantics is useful for investigating a logic (i.e. a derivation system) only if the semantic consequence relation reflects its syntactical counterpart, the *syntactic consequence* relation (*derivability*). It is vital to know which modal logics are sound and complete with respect to a class of Kripke frames, and to determine also which class that is.

For any class *C* of Kripke frames, Thm(*C*) is a normal modal logic (in particular, theorems of the minimal normal modal logic, *K*, are valid in every Kripke model). However, the converse does not hold in general: while most of the modal systems studied are complete of classes of frames described by simple conditions, Kripke incomplete normal modal logics do exist. A natural example of such a system is Japaridze's polymodal logic.

A normal modal logic *L* **corresponds** to a class of frames *C*, if *C* = Mod(*L*). In other words, *C* is the largest class of frames such that *L* is sound wrt *C*. It follows that *L* is Kripke complete if and only if it is complete of its corresponding class.

Consider the schema **T** : $\Box A\to A$ . **T** is valid in any reflexive frame $\langle W,R\rangle$ : if $w\Vdash \Box A$ , then $w\Vdash A$ since *w* *R* *w*. On the other hand, a frame which validates **T** has to be reflexive: fix *w* ∈ *W*, and define satisfaction of a propositional variable *p* as follows: $u\Vdash p$ if and only if *w* *R* *u*. Then $w\Vdash \Box p$ , thus $w\Vdash p$ by **T**, which means *w* *R* *w* using the definition of $\Vdash$ . **T** corresponds to the class of reflexive Kripke frames.

It is often much easier to characterize the corresponding class of *L* than to prove its completeness, thus correspondence serves as a guide to completeness proofs. Correspondence is also used to show *incompleteness* of modal logics: suppose *L*1 ⊆ *L*2 are normal modal logics that correspond to the same class of frames, but *L*1 does not prove all theorems of *L*2. Then *L*1 is Kripke incomplete. For example, the schema $\Box (A\leftrightarrow \Box A)\to \Box A$ generates an incomplete logic, as it corresponds to the same class of frames as **GL** (viz. transitive and converse well-founded frames), but does not prove the **GL**-tautology $\Box A\to \Box \Box A$ .

#### Common modal axiom schemata

The following table lists common modal axioms together with their corresponding classes. The naming of the axioms often varies; Here, axiom **K** is named after Saul Kripke; axiom **T** is named after the truth axiom in epistemic logic; axiom **D** is named after deontic logic; axiom **B** is named after L. E. J. Brouwer; and axioms **4** and **5** are named based on C. I. Lewis's numbering of symbolic logic systems.

| Name | Axiom | Frame condition |
|---|---|---|
| K | $\Box (A\to B)\to (\Box A\to \Box B)$ | holds true for any frames |
| T | $\Box A\to A$ | reflexive: $w\,R\,w$ |
| Q | $\Box \Box A\to \Box A$ | dense: $w\,R\,u\Rightarrow \exists v\,(w\,R\,v\land v\,R\,u)$ |
| 4 | $\Box A\to \Box \Box A$ | transitive: $w\,R\,v\wedge v\,R\,u\Rightarrow w\,R\,u$ |
| D | $\Box A\to \Diamond A$ or $\Diamond \top$ or $\neg \Box \bot$ | serial: $\forall w\,\exists v\,(w\,R\,v)$ |
| B | $A\to \Box \Diamond A$ or $\Diamond \Box A\to A$ | symmetric : $w\,R\,v\Rightarrow v\,R\,w$ |
| 5 | $\Diamond A\to \Box \Diamond A$ | Euclidean: $w\,R\,u\land w\,R\,v\Rightarrow u\,R\,v$ |
| GL | $\Box (\Box A\to A)\to \Box A$ | *R* transitive, *R*−1 well-founded |
| Grz | $\Box (\Box (A\to \Box A)\to A)\to A$ | *R* reflexive and transitive, *R*−1−Id well-founded |
| H | $\Box (\Box A\to B)\lor \Box (\Box B\to A)$ | $w\,R\,u\land w\,R\,v\Rightarrow u\,R\,v\lor v\,R\,u$ |
| M | $\Box \Diamond A\to \Diamond \Box A$ | (a complicated second-order property) |
| G | $\Diamond \Box A\to \Box \Diamond A$ | convergent: $w\,R\,u\land w\,R\,v\Rightarrow \exists x\,(u\,R\,x\land v\,R\,x)$ |
| - | $A\to \Box A$ | discrete: $w\,R\,v\Rightarrow w=v$ |
| - | $\Diamond A\to \Box A$ | partial function: $w\,R\,u\land w\,R\,v\Rightarrow u=v$ |
| - | $\Diamond A\leftrightarrow \Box A$ | function: $\forall w\,\exists !u\,w\,R\,u$ ( $\exists !$ is the uniqueness quantification) |
| - | $\Box A$ or $\Box \bot$ | empty: $\forall w\,\forall u\,\neg (w\,R\,u)$ |

Axiom **K** can also be rewritten as $\Box [(A\to B)\land A]\to \Box B$ , which logically establishes modus ponens as a rule of inference in every possible world.

Note that for axiom **D**, $\Diamond A$ implicitly implies $\Diamond \top$ , which means that for every possible world in the model, there is always at least one possible world accessible from it (which could be itself). This implicit implication $\Diamond A\rightarrow \Diamond \top$ is similar to the implicit implication by existential quantifier on the range of quantification.

#### Common modal systems

The following table lists several common normal modal systems. Frame conditions for some of the systems were simplified: the logics are *sound and complete* with respect to the frame classes given in the table, but they may *correspond* to a larger class of frames.

| Name | Axioms | Frame condition |
|---|---|---|
| K | — | all frames |
| T | T | reflexive |
| K4 | 4 | transitive |
| S4 | T, 4 | preorder |
| S5 | T, 5 or D, B, 4 | equivalence relation |
| S4.3 | T, 4, H | total preorder |
| S4.1 | T, 4, M | preorder and $\forall w\,\exists u\,(w\,R\,u\land \forall v\,(u\,R\,v\Rightarrow u=v))$ |
| S4.2 | T, 4, G | directed preorder |
| GL, K4W | GL or 4, GL | finite strict partial order |
| Grz, S4Grz | Grz or T, 4, Grz | finite partial order |
| D | D | serial |
| D45 | D, 4, 5 | transitive, serial, and Euclidean |

### Canonical models

For any normal modal logic, *L*, a Kripke model (called the **canonical model**) can be constructed that refutes precisely the non-theorems of *L*, by an adaptation of the standard technique of using maximal consistent sets as models. Canonical Kripke models play a role similar to the Lindenbaum–Tarski algebra construction in algebraic semantics.

A set of formulas is *L*-*consistent* if no contradiction can be derived from it using the theorems of *L*, and Modus Ponens. A *maximal L-consistent set* (an *L*-*MCS* for short) is an *L*-consistent set that has no proper *L*-consistent superset.

The **canonical model** of *L* is a Kripke model $\langle W,R,\Vdash \rangle$ , where *W* is the set of all *L*-*MCS*, and the relations *R* and $\Vdash$ are as follows:

$X\;R\;Y$

if and only if for every formula

A

, if

$\Box A\in X$

then

$A\in Y$

,

$X\Vdash A$

if and only if

$A\in X$

.

The canonical model is a model of *L*, as every *L*-*MCS* contains all theorems of *L*. By Zorn's lemma, each *L*-consistent set is contained in an *L*-*MCS*, in particular every formula unprovable in *L* has a counterexample in the canonical model.

The main application of canonical models are completeness proofs. Properties of the canonical model of **K** immediately imply completeness of **K** with respect to the class of all Kripke frames. This argument does *not* work for arbitrary *L*, because there is no guarantee that the underlying *frame* of the canonical model satisfies the frame conditions of *L*.

We say that a formula or a set *X* of formulas is **canonical** with respect to a property *P* of Kripke frames, if

- *X* is valid in every frame that satisfies *P*,
- for any normal modal logic *L* that contains *X*, the underlying frame of the canonical model of *L* satisfies *P*.

A union of canonical sets of formulas is itself canonical. It follows from the preceding discussion that any logic axiomatized by a canonical set of formulas is Kripke complete, and compact.

The axioms T, 4, D, B, 5, H, G (and thus any combination of them) are canonical. GL and Grz are not canonical, because they are not compact. The axiom M by itself is not canonical (Goldblatt, 1991), but the combined logic **S4.1** (in fact, even **K4.1**) is canonical.

In general, it is undecidable whether a given axiom is canonical. We know a nice sufficient condition: Henrik Sahlqvist identified a broad class of formulas (now called Sahlqvist formulas) such that

- a Sahlqvist formula is canonical,
- the class of frames corresponding to a Sahlqvist formula is first-order definable,
- there is an algorithm that computes the corresponding frame condition to a given Sahlqvist formula.

This is a powerful criterion: for example, all axioms listed above as canonical are (equivalent to) Sahlqvist formulas.

### Finite model property

A logic has the **finite model property** (FMP) if it is complete with respect to a class of finite frames. An application of this notion is the decidability question: it follows from Post's theorem that a recursively axiomatized modal logic *L* which has FMP is decidable, provided it is decidable whether a given finite frame is a model of *L*. In particular, every finitely axiomatizable logic with FMP is decidable.

There are various methods for establishing FMP for a given logic. Refinements and extensions of the canonical model construction often work, using tools such as filtration or unravelling. As another possibility, completeness proofs based on cut-free sequent calculi usually produce finite models directly.

Most of the modal systems used in practice (including all listed above) have FMP.

In some cases, we can use FMP to prove Kripke completeness of a logic: every normal modal logic is complete with respect to a class of modal algebras, and a *finite* modal algebra can be transformed into a Kripke frame. As an example, Robert Bull proved using this method that every normal extension of **S4.3** has FMP, and is Kripke complete.

### Multimodal logics

Kripke semantics has a straightforward generalization to logics with more than one modality. A Kripke frame for a language with $\{\Box _{i}\mid \,i\in I\}$ as the set of its necessity operators consists of a non-empty set *W* equipped with binary relations *Ri* for each *i* ∈ *I*. The definition of a satisfaction relation is modified as follows:

$w\Vdash \Box _{i}A$

if and only if

$\forall u\,(w\;R_{i}\;u\Rightarrow u\Vdash A).$

A simplified semantics, discovered by Tim Carlson, is often used for polymodal provability logics. A **Carlson model** is a structure $\langle W,R,\{D_{i}\}_{i\in I},\Vdash \rangle$ with a single accessibility relation *R*, and subsets *Di* ⊆ *W* for each modality. Satisfaction is defined as

$w\Vdash \Box _{i}A$

if and only if

$\forall u\in D_{i}\,(w\;R\;u\Rightarrow u\Vdash A).$

Carlson models are easier to visualize and to work with than usual polymodal Kripke models; there are, however, Kripke complete polymodal logics which are Carlson incomplete.

## Semantics of intuitionistic logic

Kripke semantics for intuitionistic logic follows the same principles as the semantics of modal logic, but it uses a different definition of satisfaction.

An **intuitionistic Kripke model** is a triple $\langle W,\leq ,\Vdash \rangle$ , where $\langle W,\leq \rangle$ is a preordered Kripke frame, and $\Vdash$ satisfies the following conditions:

- if *p* is a propositional variable, $w\leq u$ , and $w\Vdash p$ , then $u\Vdash p$ (*persistency* condition (cf. monotonicity)),
- $w\Vdash A\land B$ if and only if $w\Vdash A$ and $w\Vdash B$ ,
- $w\Vdash A\lor B$ if and only if $w\Vdash A$ or $w\Vdash B$ ,
- $w\Vdash A\to B$ if and only if for all $u\geq w$ , $u\Vdash A$ implies $u\Vdash B$ ,
- not $w\Vdash \bot$ .

Intuitively, the additional requirement for $w\Vdash A\to B$ is to ensure the monotinicity even for compound propositions, i.e., for any proposition *A*, if $w\leq u$ and $w\Vdash A$ , then $u\Vdash A$ . The negation of *A*, ¬*A*, could be defined as an abbreviation for *A* → ⊥. If for all *u* such that *w* ≤ *u*, not *u* ⊩ *A*, then *w* ⊩ *A* → ⊥ is vacuously true, so *w* ⊩ ¬*A*.

Intuitionistic logic is sound and complete with respect to its Kripke semantics, and it has the finite model property.

### Intuitionistic first-order logic

Let *L* be a first-order language. A Kripke model of *L* is a triple $\langle W,\leq ,\{M_{w}\}_{w\in W}\rangle$ , where $\langle W,\leq \rangle$ is an intuitionistic Kripke frame, *Mw* is a (classical) *L*-structure for each node *w* ∈ *W*, and the following compatibility conditions hold whenever *u* ≤ *v*:

- the domain of *Mu* is included in the domain of *Mv*,
- realizations of function symbols in *Mu* and *Mv* agree on elements of *Mu*,
- for each *n*-ary predicate *P* and elements *a*1,...,*an* ∈ *Mu*: if *P*(*a*1,...,*an*) holds in *Mu*, then it holds in *Mv*.

Given an evaluation *e* of variables by elements of *Mw*, we define the satisfaction relation $w\Vdash A[e]$ :

- $w\Vdash P(t_{1},\dots ,t_{n})[e]$ if and only if $P(t_{1}[e],\dots ,t_{n}[e])$ holds in *Mw*,
- $w\Vdash (A\land B)[e]$ if and only if $w\Vdash A[e]$ and $w\Vdash B[e]$ ,
- $w\Vdash (A\lor B)[e]$ if and only if $w\Vdash A[e]$ or $w\Vdash B[e]$ ,
- $w\Vdash (A\to B)[e]$ if and only if for all $u\geq w$ , $u\Vdash A[e]$ implies $u\Vdash B[e]$ ,
- not $w\Vdash \bot [e]$ ,
- $w\Vdash (\exists x\,A)[e]$ if and only if there exists an $a\in M_{w}$ such that $w\Vdash A[e(x\to a)]$ ,
- $w\Vdash (\forall x\,A)[e]$ if and only if for every $u\geq w$ and every $a\in M_{u}$ , $u\Vdash A[e(x\to a)]$ .

Here *e*(*x*→*a*) is the evaluation which gives *x* the value *a*, and otherwise agrees with *e*.

### Kripke–Joyal semantics

As part of the independent development of sheaf theory, it was realised around 1965 that Kripke semantics was intimately related to the treatment of existential quantification in topos theory. That is, the 'local' aspect of existence for sections of a sheaf was a kind of logic of the 'possible'. Though this development was the work of a number of people, the name **Kripke–Joyal** or simple **sheaf semantics** is often used in this connection.

Sheaf semantics unifies Kripke and the similar Beth semantics, as well as extend it from the proof-irrelevant (propositional) to the proof relevant cases, in the case the accessibility relation R is reflexive and transitive.

## Model constructions

As in classical model theory, there are methods for constructing a new Kripke model from other models.

The natural homomorphisms in Kripke semantics are called **p-morphisms** (which is short for *pseudo-epimorphism*, but the latter term is rarely used). A p-morphism of Kripke frames $\langle W,R\rangle$ and $\langle W',R'\rangle$ is a mapping $f\colon W\to W'$ such that

- *f* preserves the accessibility relation, i.e., *u R v* implies *f*(*u*) *R’* *f*(*v*),
- whenever *f*(*u*) *R’* *v*’, there is a *v* ∈ *W* such that *u R v* and *f*(*v*) = *v*’.

A p-morphism of Kripke models $\langle W,R,\Vdash \rangle$ and $\langle W',R',\Vdash '\rangle$ is a p-morphism of their underlying frames $f\colon W\to W'$ , which satisfies

$w\Vdash p$

if and only if

$f(w)\Vdash 'p$

, for any propositional variable

p

.

P-morphisms are a special kind of bisimulations. In general, a **bisimulation** between frames $\langle W,R\rangle$ and $\langle W',R'\rangle$ is a relation *B ⊆ W × W’*, which satisfies the following “zig-zag” property:

- if *u B u’* and *u R v*, there exists *v’* ∈ *W’* such that *v B v’* and *u’ R’ v’*,
- if *u B u’* and *u’ R’ v’*, there exists *v* ∈ *W* such that *v B v’* and *u R v*.

A bisimulation of models is additionally required to preserve forcing of atomic formulas:

if

w B w’

, then

$w\Vdash p$

if and only if

$w'\Vdash 'p$

, for any propositional variable

p

.

The key property which follows from this definition is that bisimulations (hence also p-morphisms) of models preserve the satisfaction of *all* formulas, not only propositional variables.

We can transform a Kripke model into a tree using **unravelling**. Given a model $\langle W,R,\Vdash \rangle$ and a fixed node *w*0 ∈ *W*, we define a model $\langle W',R',\Vdash '\rangle$ , where *W’* is the set of all finite sequences $s=\langle w_{0},w_{1},\dots ,w_{n}\rangle$ such that *wi R wi+1* for all *i* < *n*, and $s\Vdash 'p$ if and only if $w_{n}\Vdash p$ for a propositional variable *p*. The definition of the accessibility relation *R’* varies; in the simplest case we put

$\langle w_{0},w_{1},\dots ,w_{n}\rangle \;R'\;\langle w_{0},w_{1},\dots ,w_{n},w_{n+1}\rangle$

,

but many applications need the reflexive and/or transitive closure of this relation, or similar modifications.

**Filtration** is a useful construction which one can use to prove FMP for many logics. Let *X* be a set of formulas closed under taking subformulas. An *X*-filtration of a model $\langle W,R,\Vdash \rangle$ is a mapping *f* from *W* to a model $\langle W',R',\Vdash '\rangle$ such that

- *f* is a surjection,
- *f* preserves the accessibility relation, and (in both directions) satisfaction of variables *p* ∈ *X*,
- if *f*(*u*) *R’* *f*(*v*) and $u\Vdash \Box A$ , where $\Box A\in X$ , then $v\Vdash A$ .

It follows that *f* preserves satisfaction of all formulas from *X*. In typical applications, we take *f* as the projection onto the quotient of *W* over the relation

u ≡

X

v

if and only if for all

A

∈

X

,

$u\Vdash A$

if and only if

$v\Vdash A$

.

As in the case of unravelling, the definition of the accessibility relation on the quotient varies.

## General frame semantics

The main defect of Kripke semantics is the existence of Kripke incomplete logics, and logics which are complete but not compact. It can be remedied by equipping Kripke frames with extra structure which restricts the set of possible valuations, using ideas from algebraic semantics. This gives rise to the general frame semantics.

## Computer science applications

Blackburn et al. (2001) argue that, because a relational structure is simply a set together with a collection of relations on that set, it is unsurprising that relational structures can often be found. As an example from theoretical computer science, they give labeled transition systems, which model program execution. Blackburn et al. thus claim because of this connection that modal languages are ideally suited in providing "internal, local perspective on relational structures." (p. xii)

## History and terminology

Similar work that predated Kripke's revolutionary semantic breakthroughs:

- Rudolf Carnap seems to have been the first to have the idea that one can give a **possible world semantics** for the modalities of necessity and possibility by means of giving the valuation function a parameter that ranges over Leibnizian possible worlds. Bayart develops this idea further, but neither gave recursive definitions of satisfaction in the style introduced by Tarski.
- J.C.C. McKinsey and Alfred Tarski developed an approach to modeling modal logics that is still influential in modern research, namely the algebraic approach, in which Boolean algebras with operators are used as models. Bjarni Jónsson and Tarski established the representability of Boolean algebras with operators in terms of frames. If the two ideas had been put together, the result would have been precisely frame models, which is to say Kripke models, years before Kripke. But no one (not even Tarski) saw the connection at the time.
- Arthur Prior, building on unpublished work of C. A. Meredith, developed a translation of sentential modal logic into classical predicate logic that, if he had combined it with the usual model theory for the latter, would have produced a model theory equivalent to Kripke models for the former. But his approach was resolutely syntactic and anti-model-theoretic.
- Stig Kanger gave a rather more complex approach to the interpretation of modal logic, but one that contains many of the key ideas of Kripke's approach. He first noted the relationship between conditions on accessibility relations and Lewis-style axioms for modal logic. Kanger failed, however, to give a completeness proof for his system.
- Jaakko Hintikka gave a semantics in his papers introducing epistemic logic that is a simple variation of Kripke's semantics, equivalent to the characterisation of valuations by means of maximal consistent sets. He doesn't give inference rules for epistemic logic, and so cannot give a completeness proof.
- Richard Montague had many of the key ideas contained in Kripke's work, but he did not regard them as significant, because he had no completeness proof, and so did not publish until after Kripke's papers had created a sensation in the logic community.
- Evert Willem Beth presented a semantics of intuitionistic logic based on trees, which closely resembles Kripke semantics, except for using a more cumbersome definition of satisfaction.
