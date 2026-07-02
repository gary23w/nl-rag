---
title: "Hilbert system"
source: https://en.wikipedia.org/wiki/Hilbert_system
domain: proof-theory
license: CC-BY-SA-4.0
tags: proof theory, natural deduction, sequent calculus, formal proof
fetched: 2026-07-02
---

# Hilbert system

In logic, more specifically proof theory, a **Hilbert system**, sometimes called **Hilbert calculus**, **Hilbert-style system**, **Hilbert-style proof system**, **Hilbert-style deductive system** or **Hilbert–Ackermann system**, is a type of formal proof system attributed to Gottlob Frege and David Hilbert. These deductive systems are most often studied for first-order logic, but are of interest for other logics as well.

It is defined as a deductive system that generates theorems from axioms and inference rules, especially if the only postulated inference rule is modus ponens. Every Hilbert system is an axiomatic system, which is used by many authors as a sole less specific term to declare their Hilbert systems, without mentioning any more specific terms. In this context, "Hilbert systems" are contrasted with natural deduction systems, in which no axioms are used, only inference rules.

While all sources that refer to an "axiomatic" logical proof system characterize it simply as a logical proof system with axioms, sources that use variants of the term "Hilbert system" sometimes define it in different ways, which will not be used in this article. For instance, Troelstra defines a "Hilbert system" as a system with axioms *and* with ${\rightarrow }E$ and ${\forall }I$ as the only inference rules. A specific set of axioms is also sometimes called "the Hilbert system", or "the Hilbert-style calculus". Sometimes, "Hilbert-style" is used to convey the type of axiomatic system that has its axioms given in *schematic* form, as in the § Schematic form of P2 below—but other sources use the term "Hilbert-style" as encompassing both systems with schematic axioms and systems with a rule of substitution, as this article does. The use of "Hilbert-style" and similar terms to describe axiomatic proof systems in logic is due to the influence of Hilbert and Ackermann's *Principles of Mathematical Logic* (1928).

Most variants of Hilbert systems take a characteristic tack in the way they balance a trade-off between logical axioms and rules of inference. Hilbert systems can be characterised by the choice of a large number of schemas of logical axioms and a small set of rules of inference. Systems of natural deduction take the opposite tack, including many deduction rules but very few or no axiom schemas. The most commonly studied Hilbert systems have either just one rule of inference – modus ponens, for propositional logics – or two – with generalisation, to handle predicate logics, as well – and several infinite axiom schemas. Hilbert systems for alethic modal logics, sometimes called Hilbert-Lewis systems, additionally require the necessitation rule. Some systems use a finite list of concrete formulas as axioms instead of an infinite set of formulas via axiom schemas, in which case the uniform substitution rule is required.

A characteristic feature of the many variants of Hilbert systems is that the *context* is not changed in any of their rules of inference, while both natural deduction and sequent calculus contain some context-changing rules. Thus, if one is interested only in the derivability of tautologies, no hypothetical judgments, then one can formalize the Hilbert system in such a way that its rules of inference contain only judgments of a rather simple form. The same cannot be done with the other two deductions systems: as context is changed in some of their rules of inferences, they cannot be formalized so that hypothetical judgments could be avoided – not even if we want to use them just for proving derivability of tautologies.

## Formal deductions

In a Hilbert system, a **formal deduction** (or **proof**) is a finite sequence of formulas in which each formula is either an axiom or is obtained from previous formulas by a rule of inference. These formal deductions are meant to mirror natural-language proofs, although they are far more detailed.

Suppose $\Gamma$ is a set of formulas, considered as **hypotheses**. For example, $\Gamma$ could be a set of axioms for group theory or set theory. The notation $\Gamma \vdash \phi$ means that there is a deduction that ends with $\phi$ using as axioms only **logical axioms** and elements of $\Gamma$ . Thus, informally, $\Gamma \vdash \phi$ means that $\phi$ is provable assuming all the formulas in $\Gamma$ .

Hilbert systems are characterized by the use of numerous schemas of **logical axioms**. An axiom schema is an infinite set of axioms obtained by substituting all formulas of some form into a specific pattern. The set of logical axioms includes not only those axioms generated from this pattern, but also any generalization of one of those axioms. A generalization of a formula is obtained by prefixing zero or more universal quantifiers on the formula; for example $\forall y(\forall xPxy\to Pty)$ is a generalization of $\forall xPxy\to Pty$ .

## Propositional logic

The following are some Hilbert systems that have been used in propositional logic. One of them, the § Schematic form of P2, is also considered a Frege system.

### Frege's *Begriffsschrift*

Axiomatic proofs have been used in mathematics since the famous Ancient Greek textbook, Euclid's *Elements of Geometry*, c. 300 BC. But the first known fully formalized proof system that thereby qualifies as a Hilbert system dates back to Gottlob Frege's 1879 *Begriffsschrift*. Frege's system used only implication and negation as connectives, and it had six axioms, which were these ones:

- Proposition 1: $a\supset (b\supset a)$
- Proposition 2: $(c\supset (b\supset a))\supset ((c\supset b)\supset (c\supset a))$
- Proposition 8: $(d\supset (b\supset a))\supset (b\supset (d\supset a))$
- Proposition 28: $(b\supset a)\supset (\neg a\supset \neg b)$
- Proposition 31: $\neg \neg a\supset a$
- Proposition 41: $a\supset \neg \neg a$

These were used by Frege together with modus ponens and a rule of substitution (which was used but never precisely stated) to yield a complete and consistent axiomatization of classical truth-functional propositional logic.

### Łukasiewicz's P2

Jan Łukasiewicz showed that, in Frege's system, "the third axiom is superfluous since it can be derived from the preceding two axioms, and that the last three axioms can be replaced by the single sentence $CCNpNqCqp$ ". Which, taken out of Łukasiewicz's Polish notation into modern notation, means $(\neg p\rightarrow \neg q)\rightarrow (q\rightarrow p)$ . Hence, Łukasiewicz is credited with this system of three axioms:

- $p\to (q\to p)$
- $(p\to (q\to r))\to ((p\to q)\to (p\to r))$
- $(\neg p\to \neg q)\to (q\to p)$

Just like Frege's system, this system uses a substitution rule and uses modus ponens as an inference rule. The exact same system was given (with an explicit substitution rule) by Alonzo Church, who referred to it as the system P2, and helped popularize it.

### Schematic form of P2

One may avoid using the rule of substitution by giving the axioms in schematic form, using them to generate an infinite set of axioms. Hence, using Greek letters to represent schemas (metalogical variables that may stand for any well-formed formulas), the axioms are given as:

- $\varphi \to (\psi \to \varphi )$
- $(\varphi \to (\psi \to \chi ))\to ((\varphi \to \psi )\to (\varphi \to \chi ))$
- $(\neg \varphi \to \neg \psi )\to (\psi \to \varphi )$

The schematic version of P2 is attributed to John von Neumann, and is used in the Metamath "set.mm" formal proof database. In fact, the very idea of using axiom schemas to replace the rule of substitution is attributed to von Neumann. The schematic version of P2 has also been attributed to Hilbert, and named ${\mathcal {H}}$ in this context.

Systems for propositional logic whose inference rules are schematic are also called Frege systems; as the authors that originally defined the term "Frege system" note, this actually excludes Frege's own system, given above, since it had axioms instead of axiom schemas.

#### Proof example in P2

As an example, a proof of $A\to A$ in P2 is given below. First, the axioms are given names:

(A1)

$(p\to (q\to p))$

(A2)

$((p\to (q\to r))\to ((p\to q)\to (p\to r)))$

(A3)

$((\neg p\to \neg q)\to (q\to p))$

And the proof is as follows:

1. $A\to ((B\to A)\to A)$       (instance of (A1))
2. $(A\to ((B\to A)\to A))\to ((A\to (B\to A))\to (A\to A))$       (instance of (A2))
3. $(A\to (B\to A))\to (A\to A)$       (from (1) and (2) by modus ponens)
4. $A\to (B\to A)$       (instance of (A1))
5. $A\to A$       (from (4) and (3) by modus ponens)

## Predicate logic (example system)

There is an unlimited amount of axiomatisations of predicate logic, since for any logic there is freedom in choosing axioms and rules that characterise that logic. We describe here a Hilbert system with nine axioms and just the rule modus ponens, which we call the one-rule axiomatisation and which describes classical equational logic. We deal with a minimal language for this logic, where formulas use only the connectives $\lnot$ and $\to$ and only the quantifier $\forall$ . Later we show how the system can be extended to include additional logical connectives, such as $\land$ and $\lor$ , without enlarging the class of deducible formulas.

The first four logical axiom schemas allow (together with modus ponens) for the manipulation of logical connectives.

P1.

$\phi \to \phi$

P2.

$\phi \to \left(\psi \to \phi \right)$

P3.

$\left(\phi \to \left(\psi \rightarrow \xi \right)\right)\to \left(\left(\phi \to \psi \right)\to \left(\phi \to \xi \right)\right)$

P4.

$\left(\lnot \phi \to \lnot \psi \right)\to \left(\psi \to \phi \right)$

The axiom P1 is redundant, as it follows from P3, P2 and modus ponens (see proof). These axioms describe classical propositional logic; without axiom P4 we get positive implicational logic. Minimal logic is achieved either by adding instead the axiom P4m, or by defining $\lnot \phi$ as $\phi \to \bot$ .

P4m.

$\left(\phi \to \psi \right)\to \left(\left(\phi \to \lnot \psi \right)\to \lnot \phi \right)$

Intuitionistic logic is achieved by adding axioms P4i and P5i to positive implicational logic, or by adding axiom P5i to minimal logic. Both P4i and P5i are theorems of classical propositional logic.

P4i.

$\left(\phi \to \lnot \phi \right)\to \lnot \phi$

P5i.

$\lnot \phi \to \left(\phi \to \psi \right)$

Note that these are axiom schemas, which represent infinitely many specific instances of axioms. For example, P1 might represent the particular axiom instance $p\to p$ , or it might represent $\left(p\to q\right)\to \left(p\to q\right)$ : the $\phi$ is a place where any formula can be placed. A variable such as this that ranges over formulae is called a 'schematic variable'.

With a second rule of uniform substitution (US), we can change each of these axiom schemas into a single axiom, replacing each schematic variable by some propositional variable that isn't mentioned in any axiom to get what we call the substitutional axiomatisation. Both formalisations have variables, but where the one-rule axiomatisation has schematic variables that are outside the logic's language, the substitutional axiomatisation uses propositional variables that do the same work by expressing the idea of a variable ranging over formulae with a rule that uses substitution.

US. Let

$\phi (p)$

be a formula with one or more instances of the propositional variable

p

, and let

$\psi$

be another formula. Then from

$\phi (p)$

, infer

$\phi (\psi )$

.

The next three logical axiom schemas provide ways to add, manipulate, and remove universal quantifiers.

Q5.

$\forall x\left(\phi \right)\to \phi [x:=t]$

where

t

may be substituted for

x

in

$\,\!\phi$

Q6.

$\forall x\left(\phi \to \psi \right)\to \left(\forall x\left(\phi \right)\to \forall x\left(\psi \right)\right)$

Q7.

$\phi \to \forall x\left(\phi \right)$

where

x

is not free in

$\phi$

.

These three additional rules extend the propositional system to axiomatise classical predicate logic. Likewise, these three rules extend system for intuitionistic propositional logic (with P1-3 and P4i and P5i) to intuitionistic predicate logic.

Universal quantification is often given an alternative axiomatisation using an extra rule of generalisation, in which case the rules Q6 and Q7 are redundant.

- Generalization: If $\Gamma \vdash \phi$ and *x* does not occur free in any formula of $\Gamma$ then $\Gamma \vdash \forall x\phi$ .

The final axiom schemas are required to work with formulas involving the equality symbol.

I8.

$x=x$

for every variable

x

.

I9.

$\left(x=y\right)\to \left(\phi [z:=x]\to \phi [z:=y]\right)$

## Conservative extensions

It is common to include in a Hilbert system only axioms for the logical operators implication and negation towards functional completeness. Given these axioms, it is possible to form conservative extensions of the deduction theorem that permit the use of additional connectives. These extensions are called conservative because if a formula φ involving new connectives is rewritten as a logically equivalent formula θ involving only negation, implication, and universal quantification, then φ is derivable in the extended system if and only if θ is derivable in the original system. When fully extended, a Hilbert system will resemble more closely a system of natural deduction.

### Existential quantification

- Introduction

$\forall x(\phi \to \exists y(\phi [x:=y]))$

- Elimination

$\forall x(\phi \to \psi )\to (\exists x(\phi )\to \psi )$

where

x

is not a

free variable

of

$\psi$

.

### Conjunction and disjunction

- Conjunction introduction and elimination

introduction:

$\alpha \to (\beta \to \alpha \land \beta )$

elimination left:

$\alpha \wedge \beta \to \alpha$

elimination right:

$\alpha \wedge \beta \to \beta$

- Disjunction introduction and elimination

introduction left:

$\alpha \to \alpha \vee \beta$

introduction right:

$\beta \to \alpha \vee \beta$

elimination:

$(\alpha \to \gamma )\to ((\beta \to \gamma )\to \alpha \vee \beta \to \gamma )$
