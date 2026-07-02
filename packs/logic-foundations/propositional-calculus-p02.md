---
title: "Propositional logic (part 2/2)"
source: https://en.wikipedia.org/wiki/Propositional_calculus
domain: logic-foundations
license: CC-BY-SA-4.0
tags: propositional logic, first-order logic, boolean algebra, truth table, mathematical proof
fetched: 2026-07-02
part: 2/2
---

## Syntactic proof via natural deduction

Natural deduction, since it is a method of syntactical proof, is specified by providing *inference rules* (also called *rules of proof*) for a language with the typical set of connectives $\{-,\&,\lor ,\to ,\leftrightarrow \}$ ; no axioms are used other than these rules. The rules are covered below, and a proof example is given afterwards.

### Notation styles

Different authors vary to some extent regarding which inference rules they give, which will be noted. More striking to the look and feel of a proof, however, is the variation in notation styles. The § Gentzen notation, which was covered earlier for a short argument, can actually be stacked to produce large tree-shaped natural deduction proofs—not to be confused with "truth trees", which is another name for analytic tableaux. There is also a style due to Stanisław Jaśkowski, where the formulas in the proof are written inside various nested boxes, and there is a simplification of Jaśkowski's style due to Fredric Fitch (Fitch notation), where the boxes are simplified to simple horizontal lines beneath the introductions of suppositions, and vertical lines to the left of the lines that are under the supposition. Lastly, there is the only notation style which will actually be used in this article, which is due to Patrick Suppes, but was much popularized by E.J. Lemmon and Benson Mates. This method has the advantage that, graphically, it is the least intensive to produce and display, which made it a natural choice for the editor who wrote this part of the article, who did not understand the complex LaTeX commands that would be required to produce proofs in the other methods.

A **proof**, then, laid out in accordance with the Suppes–Lemmon notation style, is a sequence of lines containing sentences, where each sentence is either an assumption, or the result of applying a rule of proof to earlier sentences in the sequence. Each **line of proof** is made up of a **sentence of proof**, together with its **annotation**, its **assumption set**, and the current **line number**. The assumption set lists the assumptions on which the given sentence of proof depends, which are referenced by the line numbers. The annotation specifies which rule of proof was applied, and to which earlier lines, to yield the current sentence. See the § Natural deduction proof example.

### Inference rules

Natural deduction inference rules, due ultimately to Gentzen, are given below. There are ten primitive rules of proof, which are the rule *assumption*, plus four pairs of introduction and elimination rules for the binary connectives, and the rule *reductio ad adbsurdum*. Disjunctive Syllogism can be used as an easier alternative to the proper ∨-elimination, and MTT and DN are commonly given rules, although they are not primitive.

| Rule Name | Alternative names | Annotation | Assumption set | Statement |
|---|---|---|---|---|
| Rule of Assumptions | Assumption | **A** | The current line number. | At any stage of the argument, introduce a proposition as an assumption of the argument. |
| Conjunction introduction | Ampersand introduction, conjunction (CONJ) | **m, n &I** | The union of the assumption sets at lines **m** and **n**. | From $\varphi$ and $\psi$ at lines **m** and **n**, infer $\varphi ~\&~\psi$ . |
| Conjunction elimination | Simplification (S), ampersand elimination | **m &E** | The same as at line **m**. | From $\varphi ~\&~\psi$ at line **m**, infer $\varphi$ and $\psi$ . |
| Disjunction introduction | Addition (ADD) | **m ∨I** | The same as at line **m**. | From $\varphi$ at line **m**, infer $\varphi \lor \psi$ , whatever $\psi$ may be. |
| Disjunction elimination | Wedge elimination, dilemma (DL) | **j,k,l,m,n ∨E** | The lines **j,k,l,m,n**. | From $\varphi \lor \psi$ at line **j**, and an assumption of $\varphi$ at line **k**, and a derivation of $\chi$ from $\varphi$ at line **l**, and an assumption of $\psi$ at line **m**, and a derivation of $\chi$ from $\psi$ at line **n**, infer $\chi$ . |
| Disjunctive Syllogism | Wedge elimination (∨E), modus tollendo ponens (MTP) | **m,n DS** | The union of the assumption sets at lines **m** and **n**. | From $\varphi \lor \psi$ at line **m** and $-\varphi$ at line **n**, infer $\psi$ ; from $\varphi \lor \psi$ at line **m** and $-\psi$ at line **n**, infer $\varphi$ . |
| Arrow elimination | Modus ponendo ponens (MPP), modus ponens (MP), conditional elimination | **m, n →E** | The union of the assumption sets at lines **m** and **n**. | From $\varphi \to \psi$ at line **m**, and $\varphi$ at line **n**, infer $\psi$ . |
| Arrow introduction | Conditional proof (CP), conditional introduction | **n, →I (m)** | Everything in the assumption set at line **n**, excepting **m**, the line where the antecedent was assumed. | From $\psi$ at line **n**, following from the assumption of $\varphi$ at line **m**, infer $\varphi \to \psi$ . |
| Reductio ad absurdum | Indirect Proof (IP), negation introduction (−I), negation elimination (−E) | **m,** **n** **RAA** **(k)** | The union of the assumption sets at lines **m** and **n**, excluding **k** (the denied assumption). | From a sentence and its denial at lines **m** and **n**, infer the denial of any assumption appearing in the proof (at line **k**). |
| Double arrow introduction | Biconditional definition (*Df* ↔), biconditional introduction | **m, n ↔ I** | The union of the assumption sets at lines **m** and **n**. | From $\varphi \to \psi$ and $\psi \to \varphi$ at lines **m** and **n**, infer $\varphi \leftrightarrow \psi$ . |
| Double arrow elimination | Biconditional definition (*Df* ↔), biconditional elimination | **m ↔ E** | The same as at line **m**. | From $\varphi \leftrightarrow \psi$ at line **m**, infer either $\varphi \to \psi$ or $\psi \to \varphi$ . |
| Double negation | Double negation elimination | **m DN** | The same as at line **m**. | From $--\varphi$ at line **m**, infer $\varphi$ . |
| Modus tollendo tollens | Modus tollens (MT) | **m, n MTT** | The union of the assumption sets at lines **m** and **n**. | From $\varphi \to \psi$ at line **m**, and $-\psi$ at line **n**, infer $-\varphi$ . |

### Natural deduction proof example

The proof below derives $-P$ from $P\to Q$ and $-Q$ using only **MPP** and **RAA**, which shows that **MTT** is not a primitive rule, since it can be derived from those two other rules.

| Assumption set | Line number | Sentence of proof | Annotation |
|---|---|---|---|
| 1 | 1 | $P\to Q$ | A |
| 2 | 2 | $-Q$ | A |
| 3 | 3 | P | A |
| 1, 3 | 4 | Q | 1, 3 →E |
| 1, 2 | 5 | $-P$ | 2, 4 RAA |


## Syntactic proof via axioms

It is possible to perform proofs axiomatically, which means that certain tautologies are taken as self-evident and various others are deduced from them using modus ponens as an inference rule, as well as a *rule of substitution*, which permits replacing any well-formed formula with any *substitution-instance* of it. Alternatively, one uses axiom schemas instead of axioms, and no rule of substitution is used.

This section gives the axioms of some historically notable axiomatic systems for propositional logic. For more examples, as well as metalogical theorems that are specific to such axiomatic systems (such as their completeness and consistency), see the article Axiomatic system (logic).

### Frege's *Begriffsschrift*

Although axiomatic proof has been used since the famous Ancient Greek textbook, Euclid's *Elements of Geometry*, in propositional logic it dates back to Gottlob Frege's 1879 *Begriffsschrift*. Frege's system used only implication and negation as connectives. It had six axioms:

- Proposition 1: $a\to (b\to a)$
- Proposition 2: $(c\to (b\to a))\to ((c\to b)\to (c\to a))$
- Proposition 8: $(d\to (b\to a))\to (b\to (d\to a))$
- Proposition 28: $(b\to a)\to (\neg a\to \neg b)$
- Proposition 31: $\neg \neg a\to a$
- Proposition 41: $a\to \neg \neg a$

These were used by Frege together with modus ponens and a rule of substitution (which was used but never precisely stated) to yield a complete and consistent axiomatization of classical truth-functional propositional logic.

### Łukasiewicz's P2

Jan Łukasiewicz showed that, in Frege's system, "the third axiom is superfluous since it can be derived from the preceding two axioms, and that the last three axioms can be replaced by the single sentence $CCNpNqCqp$ ". Which, taken out of Łukasiewicz's Polish notation into modern notation, means $(\neg p\rightarrow \neg q)\rightarrow (q\rightarrow p)$ . Hence, Łukasiewicz is credited with this system of three axioms:

- $p\to (q\to p)$
- $(p\to (q\to r))\to ((p\to q)\to (p\to r))$
- $(\neg p\to \neg q)\to (q\to p)$

Just like Frege's system, this system uses a substitution rule and uses modus ponens as an inference rule. The exact same system was given (with an explicit substitution rule) by Alonzo Church, who referred to it as the system P2 and helped popularize it.

#### Schematic form of P2

One may avoid using the rule of substitution by giving the axioms in schematic form, using them to generate an infinite set of axioms. Hence, using Greek letters to represent schemata (metalogical variables that may stand for any well-formed formulas), the axioms are given as:

- $\varphi \to (\psi \to \varphi )$
- $(\varphi \to (\psi \to \chi ))\to ((\varphi \to \psi )\to (\varphi \to \chi ))$
- $(\neg \varphi \to \neg \psi )\to (\psi \to \varphi )$

The schematic version of P2 is attributed to John von Neumann, and is used in the Metamath "set.mm" formal proof database. It has also been attributed to Hilbert, and named ${\mathcal {H}}$ in this context.

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


## Metalogic

Classical propositional logic has a number of especially well-behaved metalogical properties. Relative to any of the standard types of proof systems mentioned above, it is *sound*: whenever $\Gamma \vdash \varphi$ , one also has $\Gamma \models \varphi$ . It is also *complete*, indeed *strongly complete* for arbitrary sets of premises: whenever $\Gamma \models \varphi$ , then $\Gamma \vdash \varphi$ . In particular, a formula is a theorem if and only if it is logically valid.

A further central result is *compactness*: a set $\Gamma$ of propositional formulas is satisfiable if and only if every finite subset of $\Gamma$ is satisfiable. Equivalently, if $\Gamma \models \varphi$ , then there is some finite $\Delta \subseteq \Gamma$ such that $\Delta \models \varphi$ . Because standard derivations use only finitely many premises, compactness can also be obtained from completeness.

By the same token, syntactic consistency coincides with satisfiability: a set of formulas is consistent if and only if it has a Boolean valuation (that is, a model). Thus the semantic and proof-theoretic notions used in classical propositional logic line up exactly.

Classical propositional logic is also *decidable*. Since each formula contains only finitely many propositional variables, one can determine in finitely many steps whether it is satisfiable, unsatisfiable, or valid, for example by means of truth tables.


## Solvers

One notable difference between propositional calculus and predicate calculus is that satisfiability of a propositional formula is decidable. Deciding satisfiability of propositional logic formulas is an NP-complete problem. However, practical methods exist (e.g., DPLL algorithm, 1962; Chaff algorithm, 2001) that are very fast for many useful cases. Recent work has extended the SAT solver algorithms to work with propositions containing arithmetic expressions; these are the SMT solvers.
