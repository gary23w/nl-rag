---
title: "Proof calculus"
source: https://en.wikipedia.org/wiki/Proof_calculus
domain: proof-theory
license: CC-BY-SA-4.0
tags: proof theory, natural deduction, sequent calculus, formal proof
fetched: 2026-07-02
---

# Proof calculus

In mathematical logic, a **proof calculus** or a **proof system** is built to prove statements.

## Overview

A proof system includes the components:

- Formal language: The set *L* of formulas admitted by the system, for example, propositional logic or first-order logic.
- Rules of inference: List of rules that can be employed to prove theorems from axioms and theorems.
- Axioms: Formulas in *L* assumed to be valid. All theorems are derived from axioms.

A formal proof of a well-formed formula in a proof system is a set of axioms and rules of inference of the proof system that infers that the well-formed formula is a theorem of the proof system.

Usually a given proof calculus encompasses more than a single particular formal system, since many proof calculi are under-determined and can be used for radically different logics. For example, a paradigmatic case is the sequent calculus, which can be used to express the consequence relations of both intuitionistic logic and relevance logic. Thus, loosely speaking, a proof calculus is a template or design pattern, characterized by a certain style of formal inference, that may be specialized to produce specific formal systems, namely by specifying the actual inference rules for such a system. There is no consensus among logicians on how best to define the term.

## Examples of proof calculi

The most widely known proof calculi are those classical calculi that are still in widespread use:

- The class of Hilbert systems, of which the most famous example is the 1928 Hilbert–Ackermann system of first-order logic;
- Gerhard Gentzen's calculus of natural deduction, which is the first formalism of structural proof theory, and which is the cornerstone of the formulae-as-types correspondence relating logic to functional programming;
- Gentzen's sequent calculus, which is the most studied formalism of structural proof theory.

Many other proof calculi were, or might have been, seminal, but are not widely used today.

- Aristotle's syllogistic calculus, presented in the *Organon*, readily admits formalisation. There is still some modern interest in syllogisms, carried out under the aegis of term logic.
- Gottlob Frege's two-dimensional notation of the *Begriffsschrift* (1879) is usually regarded as introducing the modern concept of quantifier to logic.
- C.S. Peirce's existential graph easily might have been seminal, had history worked out differently.

Modern research in logic teems with rival proof calculi:

- Several systems have been proposed that replace the usual textual syntax with some graphical syntax. proof nets and cirquent calculus are among such systems.
- Recently, many logicians interested in structural proof theory have proposed calculi with deep inference, for instance display logic, hypersequents, the calculus of structures, and bunched implication.
