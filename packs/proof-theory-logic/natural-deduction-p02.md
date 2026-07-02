---
title: "Natural deduction (part 2/2)"
source: https://en.wikipedia.org/wiki/Natural_deduction
domain: proof-theory-logic
license: CC-BY-SA-4.0
tags: proof theory, sequent calculus, natural deduction, cut-elimination theorem
fetched: 2026-07-02
part: 2/2
---

## Comparison with sequent calculus

The sequent calculus is the chief alternative to natural deduction as a foundation of mathematical logic. In natural deduction the flow of information is bi-directional: elimination rules flow information downwards by deconstruction, and introduction rules flow information upwards by assembly. Thus, a natural deduction proof does not have a purely bottom-up or top-down reading, making it unsuitable for automation in proof search. To address this fact, Gentzen in 1935 proposed his sequent calculus, though he initially intended it as a technical device for clarifying the consistency of predicate logic. Kleene, in his seminal 1952 book *Introduction to Metamathematics*, gave the first formulation of the sequent calculus in the modern style.

In the sequent calculus all inference rules have a purely bottom-up reading. Inference rules can apply to elements on both sides of the turnstile. (To differentiate from natural deduction, this article uses a double arrow ⇒ instead of the right tack ⊢ for sequents.) The introduction rules of natural deduction are viewed as *right rules* in the sequent calculus, and are structurally very similar. The elimination rules on the other hand turn into *left rules* in the sequent calculus. To give an example, consider disjunction; the right rules are familiar:

| Γ ⇒ A ───────── ∨R1 Γ ⇒ A ∨ B |   | Γ ⇒ B ───────── ∨R2 Γ ⇒ A ∨ B |
|---|---|---|

On the left:

| Γ, u:A ⇒ C Γ, v:B ⇒ C ─────────────────────────── ∨L Γ, w: (A ∨ B) ⇒ C |
|---|

Recall the ∨E rule of natural deduction in localised form:

| Γ ⊢ A ∨ B Γ, u:A ⊢ C Γ, v:B ⊢ C ─────────────────────────────────────── ∨E Γ ⊢ C |
|---|

The proposition *A ∨ B*, which is the succedent of a premise in ∨E, turns into a hypothesis of the conclusion in the left rule ∨L. Thus, left rules can be seen as a sort of inverted elimination rule. This observation can be illustrated as follows:

| natural deduction |   | sequent calculus |
|---|---|---|
| ────── hyp \| \| elim. rules \| ↓ ────────────────────── ↑↓ meet ↑ \| \| intro. rules \| conclusion | ⇒ | ─────────────────────────── init ↑ ↑ \| \| \| left rules \| right rules \| \| conclusion |

In the sequent calculus, the left and right rules are performed in lock-step until one reaches the *initial sequent*, which corresponds to the meeting point of elimination and introduction rules in natural deduction. These initial rules are superficially similar to the hypothesis rule of natural deduction, but in the sequent calculus they describe a *transposition* or a *handshake* of a left and a right proposition:

| ────────── init Γ, u:A ⇒ A |
|---|

The correspondence between the sequent calculus and natural deduction is a pair of soundness and completeness theorems, which are both provable by means of an inductive argument.

**Soundness of ⇒ wrt. ⊢**

If

Γ ⇒

A

,

then

Γ ⊢

A

.

**Completeness of ⇒ wrt. ⊢**

If

Γ ⊢

A

,

then

Γ ⇒

A

.

It is clear by these theorems that the sequent calculus does not change the notion of truth, because the same collection of propositions remain true. Thus, one can use the same proof objects as before in sequent calculus derivations. As an example, consider the conjunctions. The right rule is virtually identical to the introduction rule

| sequent calculus |   | natural deduction |
|---|---|---|
| Γ ⇒ π1 : A Γ ⇒ π2 : B ─────────────────────────── ∧R Γ ⇒ (π1, π2) : A ∧ B |   | Γ ⊢ π1 : A Γ ⊢ π2 : B ───────────────────────── ∧I Γ ⊢ (π1, π2) : A ∧ B |

The left rule, however, performs some additional substitutions that are not performed in the corresponding elimination rules.

| sequent calculus |   | natural deduction |
|---|---|---|
| Γ, u:A ⇒ π : C ──────────────────────────────── ∧L1 Γ, v: (A ∧ B) ⇒ [**fst** v/u] π : C |   | Γ ⊢ π : A ∧ B ───────────── ∧E1 Γ ⊢ **fst** π : A |
| Γ, u:B ⇒ π : C ──────────────────────────────── ∧L2 Γ, v: (A ∧ B) ⇒ [**snd** v/u] π : C |   | Γ ⊢ π : A ∧ B ───────────── ∧E2 Γ ⊢ **snd** π : B |

The kinds of proofs generated in the sequent calculus are therefore rather different from those of natural deduction. The sequent calculus produces proofs in what is known as the *β-normal η-long* form, which corresponds to a canonical representation of the normal form of the natural deduction proof. If one attempts to describe these proofs using natural deduction itself, one obtains what is called the *intercalation calculus* (first described by John Byrnes), which can be used to formally define the notion of a *normal form* for natural deduction.

The substitution theorem of natural deduction takes the form of a structural rule or structural theorem known as *cut* in the sequent calculus.

### Cut (substitution)

If

Γ ⇒ π

1

:

A

and

Γ,

u

:

A

⇒ π

2

:

C

,

then

Γ ⇒ [π

1

/u] π

2

:

C

.

In most well behaved logics, cut is unnecessary as an inference rule, though it remains provable as a meta-theorem; the superfluousness of the cut rule is usually presented as a computational process, known as *cut elimination*. This has an interesting application for natural deduction; usually it is extremely tedious to prove certain properties directly in natural deduction because of an unbounded number of cases. For example, consider showing that a given proposition is *not* provable in natural deduction. A simple inductive argument fails because of rules like ∨E or E which can introduce arbitrary propositions. However, we know that the sequent calculus is complete with respect to natural deduction, so it is enough to show this unprovability in the sequent calculus. Now, if cut is not available as an inference rule, then all sequent rules either introduce a connective on the right or the left, so the depth of a sequent derivation is fully bounded by the connectives in the final conclusion. Thus, showing unprovability is much easier, because there are only a finite number of cases to consider, and each case is composed entirely of sub-propositions of the conclusion. A simple instance of this is the *global consistency* theorem: "⋅ ⊢ ⊥" is not provable. In the sequent calculus version, this is manifestly true because there is no rule that can have "⋅ ⇒ ⊥" as a conclusion! Proof theorists often prefer to work on cut-free sequent calculus formulations because of such properties.
