---
title: "Cut-elimination theorem"
source: https://en.wikipedia.org/wiki/Cut-elimination_theorem
domain: proof-theory
license: CC-BY-SA-4.0
tags: proof theory, natural deduction, sequent calculus, formal proof
fetched: 2026-07-02
---

# Cut-elimination theorem

The **cut-elimination theorem** (or **Gentzen's *Hauptsatz***) is the central result establishing the significance of the sequent calculus. It was originally proved by Gerhard Gentzen in part I of his landmark 1935 paper "Investigations in Logical Deduction" for the systems LJ and LK formalising intuitionistic and classical logic respectively. The cut-elimination theorem states that any sequent that possesses a proof in the sequent calculus making use of the **cut rule** also possesses a **cut-free proof**, that is, a proof that does not make use of the cut rule. The natural deduction version of cut-elimination, known as the *normalization theorem*, was first proved for a variety of logics by Dag Prawitz in 1965 (a similar but less general proof was given the same year by Andrès Raggio).

There are many different possible sequent calculuses for many logics, and consequently there are many different cut-elimination theorems. Indeed, cut-elimination is such an important genre of theorems in logic, that logicians speak of "this logic has cut-elimination" as a way to say that this logic has a desirable property. Conversely, if a formalism or a logic does not have cut-elimination, that is usually considered a point against it, and would motivate research into finding a new formalism, or a modification of the logic, such that cut-elimination is true, or an analog of cut-elimination is true.

## The cut rule

A sequent is a logical expression relating multiple formulas, in the form " $A_{1},A_{2},A_{3},\ldots \vdash B_{1},B_{2},B_{3},\ldots$ ", which is to be read as "If all of $A_{1},A_{2},A_{3},\ldots$ hold, then at least one of $B_{1},B_{2},B_{3},\ldots$ must hold", or (as Gentzen glossed): "If ( $A_{1}$ and $A_{2}$ and $A_{3}$ …) then ( $B_{1}$ or $B_{2}$ or $B_{3}$ …)." Note that the left-hand side (LHS) is a conjunction (and) and the right-hand side (RHS) is a disjunction (or).

The LHS may have arbitrarily many or few formulae; when the LHS is empty, the RHS is a tautology. In LK, the RHS may also have any number of formulae—if it has none, the LHS is a contradiction, whereas in LJ the RHS may only have one formula or none: here we see that allowing more than one formula in the RHS is equivalent, in the presence of the right contraction rule, to the admissibility of the law of the excluded middle. However, the sequent calculus is a fairly expressive framework, and there have been sequent calculi for intuitionistic logic proposed that allow many formulae in the RHS. From Jean-Yves Girard's logic LC it is easy to obtain a rather natural formalisation of classical logic where the RHS contains at most one formula; it is the interplay of the logical and structural rules that is the key here.

"Cut" is a rule of inference in the normal statement of the sequent calculus, and equivalent to a variety of rules in other proof theories, which, given

1. $\Gamma \vdash A,\Delta$

and

1. $\Pi ,A\vdash \Lambda$

allows one to infer

1. $\Gamma ,\Pi \vdash \Delta ,\Lambda$

That is, it "cuts" the occurrences of the formula A out of the inferential relation.

## Cut elimination

The cut-elimination theorem states that (for a given system) any sequent provable using the rule Cut can be proved without use of this rule.

For sequent calculi that have only one formula in the RHS, the "Cut" rule reads, given

1. $\Gamma \vdash A$

and

1. $\Pi ,A\vdash B$

allows one to infer

1. $\Gamma ,\Pi \vdash B$

If we think of B as a theorem, then cut-elimination in this case simply says that a lemma A used to prove this theorem can be inlined. Whenever the theorem's proof mentions lemma A , we can substitute the occurrences for the proof of A . Consequently, the cut rule is admissible.

## Proof sketch

### Note

To avoid confusion, note that there are two meanings of "proof" here. There is the "proof" as a sequent calculus proof-tree. This proof is a mathematical object, and it is an object studied by proof theory. There is also the "proof" as a mathematical argument that is written normally in natural language by mathematicians. Call the first a proof-tree, and the second a proof-argument

The cut-elimination theorem is a theorem about proof-trees. To "prove the cut-elimination theorem" means to write down a proof-argument for the cut-elimination theorem.

### Idea

A proof of a cut-elimination theorem generally goes as follows.

Lists out all the inference rules of a sequent calculus. A proof tree is a tree where each node is an application of an inference rule.

We regard the proof trees as expressions in an abstract language, and then describe rewriting rules. We will define the rewriting rules such that:

- As long as a proof tree contains a cut rule, then we can still apply one of the rewriting rules to it. To ensure this, we design at least one rewriting rule for every possible context in which a cut rule might appear in.
- The rewriting rules always preserve the root of the tree. That is, we obtain another proof tree of the same endsequent.

Now one simply need to prove that the system of rewriting rules is terminating. That is, any sequence of rewriting can only last finitely many steps. In other words, one need to show that the rewriting system is well-founded.

To prove that the system is terminating, one usually designs an ordinal numbering system. For each proof tree T , define a corresponding ordinal number $o(T)$ , then shows that each rewriting step $T\implies T'$ has $o(T)>o(T')$ . Then, since the ordinals are well-founded, the rewriting system is too.

This line of thought also leads to ordinal analysis. That is, in order to prove the system is terminating, one need to assume that $\sup _{T{\text{ is a proof tree}}}o(T)$ is well-ordered. For example, in the case of Gentzen's original proof, he showed that $\sup _{T{\text{ is a proof tree}}}o(T)=\epsilon _{0}$ the 0th epsilon number. Conversely, Peano arithmetic can prove any ordinal lower than $\epsilon _{0}$ is well-founded, but not $\epsilon _{0}$ itself. Thus the common saying "the consistency of Peano arithmetic is equivalent to the well-foundedness of $\epsilon _{0}$ ".

There are in general two types of rewriting rules:

- Commutation rules: The cut rule moves up one step without interaction. This happens when the cut formula is not the principal formula.
- Principal reduction: The cut formula is the principal formula, so an interaction occurs. The tree might grow a new branch, spawn two cut rules, grow a new segment, etc.

### Examples for LK

Consider the typical sequent calculus for propositional LK. We require sequents to be finite multisets, so that we can ignore the bureaucratic annoyance of the exchange rule.

The cut rule is ${\frac {\Gamma \vdash \Delta ,A\qquad A,\Pi \vdash \Lambda }{\Gamma ,\Pi \vdash \Delta ,\Lambda }}\operatorname {Cut} .$ We give 5 illustrative examples. Note that we use "multiplicative" versions of the inference rules of conjunction and disjunction, since they are more convenient for eliminating cuts.

Conjunction, left-sequent, commutation ${\frac {\Gamma \vdash \Delta ,A\qquad {\frac {A,B,C,\Pi \vdash \Lambda }{A,B\land C,\Pi \vdash \Lambda }}\land _{L}}{\Gamma ,B\land C,\Pi \vdash \Delta ,\Lambda }}\operatorname {Cut} \quad \implies \quad {\frac {{\frac {\Gamma \vdash \Delta ,A\qquad A,B,C,\Pi \vdash \Lambda }{\Gamma ,B,C,\Pi \vdash \Delta ,\Lambda }}\operatorname {Cut} }{\Gamma ,B\land C,\Pi \vdash \Delta ,\Lambda }}\land _{L}.$ The cut simply moves one step past $\land _{L}$ without interaction. It would bubble upwards until it meets "resistance" in the form of principal cuts.

Disjunction, left-sequent, commutation ${\frac {\Gamma \vdash \Delta ,A\qquad {\frac {A,B,\Pi \vdash \Lambda \qquad C,\Sigma \vdash \Theta }{A,B\lor C,\Pi ,\Sigma \vdash \Lambda ,\Theta }}\lor _{L}}{\Gamma ,B\lor C,\Pi ,\Sigma \vdash \Delta ,\Lambda ,\Theta }}\operatorname {Cut} \quad \implies \quad {\frac {{\frac {\Gamma \vdash \Delta ,A\qquad A,B,\Pi \vdash \Lambda }{\Gamma ,B,\Pi \vdash \Delta ,\Lambda }}\operatorname {Cut} \qquad C,\Sigma \vdash \Theta }{\Gamma ,B\lor C,\Pi ,\Sigma \vdash \Delta ,\Lambda ,\Theta }}\lor _{L}.$ The cut has moved one step upward, past $\lor _{L}$ .

Identity axiom, principal rule ${\frac {{\overline {A\vdash A}}^{\operatorname {Id} }\qquad A,\Pi \vdash \Lambda }{A,\Pi \vdash \Lambda }}\operatorname {Cut} \quad \implies \quad A,\Pi \vdash \Lambda .$ This is how some cuts may eventually disappear, by canceling out a leaf of the proof tree.

Weakening, left-sequent, principal rule ${\frac {\Gamma \vdash \Delta ,A\qquad {\frac {\Pi \vdash \Lambda }{A,\Pi \vdash \Lambda }}\operatorname {Weak} _{L}}{\Gamma ,\Pi \vdash \Delta ,\Lambda }}\operatorname {Cut} \quad \implies \quad {\frac {\Pi \vdash \Lambda }{\Gamma ,\Pi \vdash \Delta ,\Lambda }}\operatorname {Weak} ^{*}.$ Here $\operatorname {Weak} ^{*}$ denotes finitely many applications of left and right weakening. The cut formula A is introduced by weakening in the right premiss, so that occurrence of A is unused. The left premiss is discarded, and the original endsequent is recovered from $\Pi \vdash \Lambda$ by weakening.

Contraction, principal rule ${\frac {\Gamma \vdash \Delta ,A\qquad {\frac {A,A,\Pi \vdash \Lambda }{A,\Pi \vdash \Lambda }}\operatorname {Contr} _{L}}{\Gamma ,\Pi \vdash \Delta ,\Lambda }}\operatorname {Cut} \quad \implies \quad {\frac {{\frac {\Gamma \vdash \Delta ,A\qquad {\frac {\Gamma \vdash \Delta ,A\qquad A,A,\Pi \vdash \Lambda }{\Gamma ,A,\Pi \vdash \Delta ,\Lambda }}\operatorname {Cut} }{\Gamma ,\Gamma ,\Pi \vdash \Delta ,\Delta ,\Lambda }}\operatorname {Cut} }{\Gamma ,\Pi \vdash \Delta ,\Lambda }}\operatorname {Contr} ^{*}.$ Here $\operatorname {Contr} ^{*}$ denotes finitely many applications of left and right contraction. The contraction in the right premiss has identified two occurrences of the cut formula A . The rewrite first cuts against one occurrence of A , then cuts against the other occurrence of A . The final contractions identify the duplicated copies of $\Gamma$ and $\Delta$ .

Most of the rewriting rules straightforwardly make progress on eliminating the cuts, either by pushing a cut closer to the leafs, or by destroying a cut at the price of possibly making the tree longer. The only exception is the case of contraction, principal rule. In this case, two cuts appeared in the place of one, and the tree increased massively in size. This is still a terminating rewriting rule, but proving this requires care.

Essentially due to the contraction principle rule, cut-elimination increases the size of proof superexponentially. By the Curry–Howard correspondence, cut-elimination corresponds to beta-reduction of simply typed lambda terms. Rewriting corresponds to beta-reduction. Rewriting across a contraction rule corresponds to beta-reduction of form $(\lambda fx.f(fx))t$ , and beta-reduction of $\underbrace {(\lambda fx.f(fx))\cdots (\lambda fx.f(fx))} _{n{\text{ times}}}$ may take $^{n}2$ time, where the notation is tetration.

Quantifier rules have analogous principal reductions, with the usual proviso that eigenvariables are always renamed before rewriting, to avoid accidentally capture. For example, a principal cut between $\forall _{R}$ and $\forall _{L}$ is reduced by substituting the term used in the left rule into the eigenvariable proof from the right rule, then cutting on the resulting instance. Thus the rewriting step preserves the endsequent while replacing a cut on $\forall x\,A(x)$ by a cut on an instance $A(t)$ .

## Consequences of the theorem

For systems formulated in the sequent calculus, analytic proofs are those proofs that do not use Cut. Typically such a proof will be longer, of course, and not necessarily trivially so. In his essay "Don't Eliminate Cut!" George Boolos demonstrated that there was a derivation that could be completed in a page using cut, but whose analytic proof could not be completed in the lifespan of the universe.

The theorem has many, rich consequences:

- A system is inconsistent if it admits a proof of the absurd. If the system has a cut elimination theorem, then if it has a proof of the absurd, or of the empty sequent, it should also have a proof of the absurd (or the empty sequent), without cuts. It is typically very easy to check that there are no such proofs. Thus, once a system is shown to have a cut elimination theorem, it is normally immediate that the system is consistent.
- Normally also the system has, at least in first-order logic, the subformula property, an important property in several approaches to proof-theoretic semantics.

Cut elimination is one of the most powerful tools for proving interpolation theorems. The possibility of carrying out proof search based on resolution, the essential insight leading to the Prolog programming language, depends upon the admissibility of Cut in the appropriate system.

For proof systems based on higher-order typed lambda calculus through a Curry–Howard isomorphism, cut elimination algorithms correspond to the strong normalization property (every proof term reduces in a finite number of steps into a normal form). An analogous result of strong normalisation for various calculi of Natural Deduction was first proved by Dag Prawitz.
