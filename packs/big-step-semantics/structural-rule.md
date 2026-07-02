---
title: "Structural rule"
source: https://en.wikipedia.org/wiki/Structural_rule
domain: big-step-semantics
license: CC-BY-SA-4.0
tags: big-step semantics, natural semantics, evaluation relation, inference rule
fetched: 2026-07-02
---

# Structural rule

In the logical discipline of proof theory, a **structural rule** is an inference rule of a sequent calculus that does not refer to any logical connective but instead operates on the sequents directly. Structural rules often mimic the intended meta-theoretic properties of the logic. Logics that deny one or more of the structural rules are classified as substructural logics.

## Common structural rules

Three common structural rules are:

- **Weakening**, where the hypotheses or conclusion of a sequence may be extended with additional members. In symbolic form weakening rules can be written as ${\frac {\Gamma \vdash \Sigma }{\Gamma ,A\vdash \Sigma }}$ on the left of the turnstile, and ${\frac {\Gamma \vdash \Sigma }{\Gamma \vdash \Sigma ,A}}$ on the right. Known as monotonicity of entailment in classical logic.
- **Contraction**, where two equal (or unifiable) members on the same side of a sequent may be replaced by a single member (or common instance). Symbolically: ${\frac {\Gamma ,A,A\vdash \Sigma }{\Gamma ,A\vdash \Sigma }}$ and ${\frac {\Gamma \vdash A,A,\Sigma }{\Gamma \vdash A,\Sigma }}$ . Also known as **factoring** in automated theorem proving systems using resolution. Known as **idempotency of entailment** in classical logic.
- **Exchange**, where two members on the same side of a sequent may be swapped. Symbolically: ${\frac {\Gamma _{1},A,\Gamma _{2},B,\Gamma _{3}\vdash \Sigma }{\Gamma _{1},B,\Gamma _{2},A,\Gamma _{3}\vdash \Sigma }}$ and ${\frac {\Gamma \vdash \Sigma _{1},A,\Sigma _{2},B,\Sigma _{3}}{\Gamma \vdash \Sigma _{1},B,\Sigma _{2},A,\Sigma _{3}}}$ . (This is also known as the *permutation rule*.)

A logic without any of the above structural rules would interpret the sides of a sequent as pure sequences; with exchange, they can be considered to be multisets; and with both contraction and exchange they can be considered to be sets.

These are not the only possible structural rules. A famous structural rule is known as **cut**. Considerable effort is spent by proof theorists in showing that cut rules are superfluous in various logics. More precisely, what is shown is that cut is only (in a sense) a tool for abbreviating proofs, and does not add to the theorems that can be proved. The successful 'removal' of cut rules, known as *cut elimination*, is directly related to the philosophy of *computation as normalization* (see Curry–Howard correspondence); it often gives a good indication of the complexity of deciding a given logic.
