---
title: "Natural deduction (part 1/2)"
source: https://en.wikipedia.org/wiki/Natural_deduction
domain: proof-theory
license: CC-BY-SA-4.0
tags: proof theory, natural deduction, sequent calculus, formal proof
fetched: 2026-07-02
part: 1/2
---

# Natural deduction

In logic and proof theory, **natural deduction** is a kind of proof calculus in which logical reasoning is expressed by inference rules closely related to the "natural" way of reasoning. This contrasts with Hilbert-style systems, which instead use axioms as much as possible to express the logical laws of deductive reasoning.


## History

Natural deduction grew out of a context of dissatisfaction with the axiomatizations of deductive reasoning common to the systems of Hilbert, Frege, and Russell (see, e.g., Hilbert system). Such axiomatizations were most famously used by Russell and Whitehead in their mathematical treatise *Principia Mathematica*. Spurred on by a series of seminars in Poland in 1926 by Łukasiewicz that advocated a more natural treatment of logic, Jaśkowski made the earliest attempts at defining a more natural deduction, first in 1929 using a diagrammatic notation, and later updating his proposal in a sequence of papers in 1934 and 1935. His proposals led to different notations such as Fitch notation or Suppes' method, for which Lemmon gave a variant now known as Suppes–Lemmon notation.

Natural deduction in its modern form was independently proposed by the German mathematician Gerhard Gentzen in 1933, in a dissertation delivered to the faculty of mathematical sciences of the University of Göttingen. The term *natural deduction* (or rather, its German equivalent *natürliches Schließen*) was coined in that paper:

> Ich wollte nun zunächst einmal einen Formalismus aufstellen, der dem wirklichen Schließen möglichst nahe kommt. So ergab sich ein "Kalkül des natürlichen Schließens".

Translation:

> First I wished to construct a formalism that comes as close as possible to actual reasoning. Thus arose a "calculus of natural deduction".

Gentzen was motivated by a desire to establish the consistency of number theory. He was unable to prove the main result required for the consistency result, the cut elimination theorem—the Hauptsatz—directly for natural deduction. For this reason he introduced his alternative system, the sequent calculus, for which he proved the Hauptsatz both for classical and intuitionistic logic. In a series of seminars in 1961 and 1962 Prawitz gave a comprehensive summary of natural deduction calculi, and transported much of Gentzen's work with sequent calculi into the natural deduction framework. His 1965 monograph *Natural deduction: a proof-theoretical study* was to become a reference work on natural deduction, and included applications for modal and second-order logic.

In natural deduction, a proposition is deduced from a collection of premises by applying inference rules repeatedly. The system presented in this article is a minor variation of Gentzen's or Prawitz's formulation, but with a closer adherence to Martin-Löf's description of logical judgments and connectives.

### History of notation styles

Natural deduction has had a large variety of notation styles, which can make it difficult to recognize a proof for a reader not familiar with one of them. To help with this situation, this article has a § Notation section explaining how to read all the notation that it will actually use. This section just explains the historical evolution of notation styles, most of which cannot be shown because there are no illustrations available under a public copyright license – the reader is pointed to the SEP and IEP for pictures.

- Gentzen invented natural deduction using tree-shaped proofs – see § Gentzen's tree notation for details.
- Jaśkowski changed this to a notation that used various nested boxes.
- Fitch changed Jaśkowski method of drawing the boxes, creating Fitch notation.
- 1940: In a textbook, Quine indicated antecedent dependencies by line numbers in square brackets, anticipating Suppes' 1957 line-number notation.
- 1950: In a textbook, Quine (1982, pp. 241–255) demonstrated a method of using one or more asterisks to the left of each line of proof to indicate dependencies. This is equivalent to Kleene's vertical bars. (It is not totally clear if Quine's asterisk notation appeared in the original 1950 edition or was added in a later edition.)
- 1957: An introduction to practical logic theorem proving in a textbook by Suppes (1999, pp. 25–150). This indicated dependencies (i.e. antecedent propositions) by line numbers at the left of each line.
- 1963: Stoll (1979, pp. 183–190, 215–219) uses sets of line numbers to indicate antecedent dependencies of the lines of sequential logical arguments based on natural deduction inference rules.
- 1965: The entire textbook by Lemmon (1978) is an introduction to logic proofs using a method based on that of Suppes, what is now known as Suppes–Lemmon notation.
- 1967: In a textbook, Kleene (2002, pp. 50–58, 128–130) briefly demonstrated two kinds of practical logic proofs, one system using explicit quotations of antecedent propositions on the left of each line, the other system using vertical bar-lines on the left to indicate dependencies.


## Notation

Here is a table with the most common notational variants for logical connectives.

| Connective | Symbol |
|---|---|
| AND | $A\land B$ , $A\cdot B$ , $AB$ , $A\mathbin {\&} B$ , $A\mathbin {\&\&} B$ |
| equivalent | $A\equiv B$ , $A\Leftrightarrow B$ , $A\leftrightarrow B$ , $A\leftrightharpoons B$ |
| implies | $A\Rightarrow B$ , $A\supset B$ , $A\rightarrow B$ |
| NAND | $A\mathbin {\overline {\land }} B$ , $A\mid B$ , ${\overline {A\cdot B}}$ |
| nonequivalent | $A\not \equiv B$ , $A\not \Leftrightarrow B$ , $A\nleftrightarrow B$ |
| NOR | $A\mathbin {\overline {\lor }} B$ , $A\mathbin {\downarrow } B$ , ${\overline {A+B}}$ |
| NOT | $\neg A$ , $-A$ , ${\overline {A}}$ , ${\mathord {\sim }}A$ |
| OR | $A\lor B$ , $A+B$ , $A\mid B$ , $A\parallel B$ |
| XNOR | $A\mathbin {\textsf {XNOR}} B$ |
| XOR | $A\mathbin {\underline {\lor }} B$ , $A\oplus B$ |

### Gentzen's tree notation

Gentzen, who invented natural deduction, had his own notation style for arguments. This will be exemplified by a simple argument below. Let's say we have a simple example argument in propositional logic, such as, "if it's raining then it's cloudly; it is raining; therefore it's cloudy". (This is in modus ponens.) Representing this as a list of propositions, as is common, we would have:

$1)~P\to Q$

$2)~P$

$\therefore ~Q$

In Gentzen's notation, this would be written like this:

${\frac {P\to Q,P}{Q}}$

The premises are shown above a line, called the **inference line**, separated by a **comma**, which indicates *combination* of premises. The conclusion is written below the inference line. The inference line represents *syntactic consequence*, sometimes called *deductive consequence*, which is also symbolized with ⊢. So the above can also be written in one line as $P\to Q,P\vdash Q$ . (The turnstile, for syntactic consequence, is of lower precedence than the comma, which represents premise combination, which in turn is of lower precedence than the arrow, used for material implication; so no parentheses are needed to interpret this formula.)

Syntactic consequence is contrasted with *semantic consequence*, which is symbolized with ⊧. In this case, the conclusion follows *syntactically* because natural deduction is a syntactic proof system, which assumes inference rules as primitives.

Gentzen's style will be used in much of this article. Gentzen's discharging annotations used to internalise hypothetical judgments can be avoided by representing proofs as a tree of sequents *Γ* ⊢ *A* instead of a tree of judgments that *A* (is true).

### Suppes–Lemmon notation

Many textbooks use Suppes–Lemmon notation, so this article will also give that – although as of now, this is only included for propositional logic, and the rest of the coverage is given only in Gentzen style. A **proof**, laid out in accordance with the Suppes–Lemmon notation style, is a sequence of lines containing sentences, where each sentence is either an assumption, or the result of applying a rule of proof to earlier sentences in the sequence. Each **line of proof** is made up of a **sentence of proof**, together with its **annotation**, its **assumption set**, and the current **line number**. The assumption set lists the assumptions on which the given sentence of proof depends, which are referenced by the line numbers. The annotation specifies which rule of proof was applied, and to which earlier lines, to yield the current sentence. Here's an example proof:

| $P\to Q,\neg Q\vdash \neg P$ |   |   |   |
|---|---|---|---|
| Assumption set | Line number | Formula (*wff*) | Annotation |
| 1 | 1 | $P\to Q$ | A |
| 2 | 2 | $\neg Q$ | A |
| 3 | 3 | P | A |
| 1, 3 | 4 | Q | 1, 3 →E |
| 1, 2 | 5 | $\neg P$ | 2, 4 RAA |
| Q.E.D |   |   |   |

This proof will become clearer when the inference rules and their appropriate annotations are specified – see § Propositional inference rules (Suppes–Lemmon style).


## Propositional language syntax

This section defines the formal syntax for a propositional logic language, contrasting the common ways of doing so with a Gentzen-style way of doing so.

### Common definition styles

In classical propositional calculus the formal language ${\mathcal {L}}$ is usually defined (here: by recursion) as follows:

1. Each propositional variable is a formula.
2. " $\bot$ " is a formula.
3. If $\varphi$ and $\psi$ are formulae, so are $(\varphi \land \psi )$ , $(\varphi \lor \psi )$ , $(\varphi \to \psi )$ , $(\varphi \leftrightarrow \psi )$ .
4. Nothing else is a formula.

Negation ( $\neg$ ) is defined as implication to falsity

$\neg \phi \;{\overset {\text{def}}{=}}\;\phi \to \bot$

,

where $\bot$ (falsum) represents a contradiction or absolute falsehood.

Older publications, and publications that do not focus on logical systems like minimal, intuitionistic or Hilbert systems, take negation as a primitive logical connective, meaning it is assumed as a basic operation and not defined in terms of other connectives. Some authors, such as Bostock, use $\bot$ and $\top$ , and also define $\neg$ as primitives.

### Gentzen-style definition

A syntax definition can also be given using § Gentzen's tree notation, by writing well-formed formulas below the inference line and any schematic variables used by those formulas above it. For instance, the equivalent of rules 3 and 4, from Bostock's definition above, is written as follows:

${\frac {\varphi }{(\neg \varphi )}}\quad {\frac {\varphi \quad \psi }{(\varphi \lor \psi )}}\quad {\frac {\varphi \quad \psi }{(\varphi \land \psi )}}\quad {\frac {\varphi \quad \psi }{(\varphi \rightarrow \psi )}}\quad {\frac {\varphi \quad \psi }{(\varphi \leftrightarrow \psi )}}$

.

A different notational convention sees the language's syntax as a categorial grammar with the single category "formula", denoted by the symbol ${\mathcal {F}}$ . So any elements of the syntax are introduced by categorizations, for which the notation is $\varphi :{\mathcal {F}}$ , meaning " $\varphi$ is an expression for an object in the category ${\mathcal {F}}$ ." The sentence-letters, then, are introduced by categorizations such as $P:{\mathcal {F}}$ ,  $Q:{\mathcal {F}}$ ,  $R:{\mathcal {F}}$ , and so on; the connectives, in turn, are defined by statements similar to the above, but using categorization notation, as seen below:

| **Conjunction (&)** | **Disjunction (∨)** | **Implication (→)** | **Negation (¬)** |
|---|---|---|---|
| ${\frac {A:{\mathcal {F}}\quad B:{\mathcal {F}}}{\&(A)(B):{\mathcal {F}}}}$ | ${\frac {A:{\mathcal {F}}\quad B:{\mathcal {F}}}{\vee (A)(B):{\mathcal {F}}}}$ | ${\frac {A:{\mathcal {F}}\quad B:{\mathcal {F}}}{{\mathord {\supset }}(A)(B):{\mathcal {F}}}}$ | ${\frac {A:{\mathcal {F}}}{\neg (A):{\mathcal {F}}}}$ |

In the rest of this article, the $\varphi :{\mathcal {F}}$ categorization notation will be used for any Gentzen-notation statements defining the language's grammar; any other statements in Gentzen notation will be inferences, asserting that a sequent follows rather than that an expression is a well-formed formula.


## Gentzen-style propositional logic

### Gentzen-style inference rules

Let the propositional language ${\mathcal {L}}$ be inductively defined as $\Phi ::=p_{1},p_{2},\dots \mid \bot \mid (\Phi \to \Phi )\mid (\Phi \land \Phi )\mid (\Phi \lor \Phi )$ .

Define negation as $\neg \Phi \,{\overset {\text{def}}{=}}\,(\Phi \to \bot )$ .

The following is a list of primitive inference rules for natural deduction in propositional logic:

| Introduction rules | Elimination rules |
|---|---|
| ${\begin{array}{c}\varphi \qquad \psi \\\hline \varphi \land \psi \end{array}}(\land _{I})$ | ${\begin{array}{c}\varphi \land \psi \\\hline \varphi \end{array}}(\land _{E})$ |
| ${\begin{array}{c}\varphi \\\hline \varphi \lor \psi \end{array}}(\lor _{I})$ | ${\cfrac {\varphi \lor \psi \quad {\begin{matrix}[\varphi ]^{u}\\\vdots \\\chi \end{matrix}}\quad {\begin{matrix}[\psi ]^{v}\\\vdots \\\chi \end{matrix}}}{\chi }}\ \lor _{E^{u,v}}$ |
| ${\begin{array}{c}[\varphi ]^{u}\\\vdots \\\psi \\\hline \varphi \to \psi \end{array}}(\to _{I})\ u$ | ${\begin{array}{c}\varphi \qquad \varphi \to \psi \\\hline \psi \end{array}}(\to _{E})$ |
|   | ${\begin{array}{c}\bot \\\hline \varphi \end{array}}(\bot _{E})$ |
|   | ${\begin{array}{c}(\varphi \to \bot )\to \bot \\\hline \varphi \end{array}}(\neg \neg _{E})$ |

In this table the Greek letters $\varphi ,\psi ,\chi$ are *schemata*, which range over formulas rather than only over atomic propositions. The name of a rule is given to the right of its formula tree. For instance, the first introduction rule is named $\land _{I}$ , which is short for "conjunction introduction".

- **Minimal logic**: the natural deduction rules are $ND_{MPC}=\{\land _{I},\land _{E},\lor _{I},\lor _{E},\to _{I},\to _{E}\}$ .

Without the rules

$\bot _{E}$

and

$\neg \neg _{E}$

the system defines minimal logic (as discussed by

Johansson

).

- **Intuitionistic logic**: the natural deduction rules are $ND_{IPC}=ND_{MPC}\cup \{\bot _{E}\}$ .

When the rule

$\bot _{E}$

(

principle of explosion

) is added to the rules for minimal logic, the system defines intuitionistic logic.

The statement

$P\to \neg \neg P$

is valid (already in minimal logic, see example 1 below), unlike the reverse implication which would entail the

law of excluded middle

.

- **Classical logic**: the natural deduction rules are $ND_{CPC}=ND_{IPC}\cup \{\neg \neg _{E}\}$ .

When all listed natural deduction rules are admitted, the system defines classical logic.

### Gentzen-style example proofs

**Example 1**: Proof, within minimal logic, of $P\to \neg \neg P$ .

Goal: $P\to ((P\to \bot )\to \bot )$ Proof:

${\cfrac {{\cfrac {[P]^{v}\qquad [P\to \bot ]^{u}}{\bot }}\to _{E}}{{\cfrac {((P\to \bot )\to \bot )}{P\to ((P\to \bot )\to \bot )}}\to _{I^{v}}}}\to _{I^{u}}$

**Example 2**: Proof, within minimal logic, of $A\to \left(B\to \left(A\land B\right)\right)$ :

${\cfrac {{\cfrac {[A]^{u}\quad [B]^{w}}{A\land B}}\ \land _{I}}{{\cfrac {B\to \left(A\land B\right)}{A\to \left(B\to \left(A\land B\right)\right)}}\ \to _{I^{u}}}}\ \to _{I^{w}}$


## Fitch-style propositional logic

Fitch developed a system of natural deduction which is characterized by

- linear presentation of the proof, instead of presentation as a tree;
- **subordinate proofs**, where assumptions could be opened within a subderivation and discharged later.

Later logicians and educators such as Patrick Suppes and E. J. Lemmon rebranded Fitch's system. While they introduced graphical changes—such as replacing indentation with vertical bars—the underlying structure of Fitch-style natural deduction remained intact. These variations are often referred to as the Suppes–Lemmon format, though they are fundamentally based on Fitch's original notation.


## Suppes–Lemmon-style propositional logic

### Suppes–Lemmon-style inference rules

The linear presentation used in Fitch- and Suppes–Lemmon-style proofs — with line numbers and vertical alignment/assumption sets — makes subproofs clearly visible. Fitch (sparingly and cautiously) used **derived rules**. Suppes–Lemmon went further and added derived rules to the toolbox of natural deduction rules.

Suppes introduced natural deduction using Gentzen-style rules.

- He defined negation in terms of contradiction: $\neg P\equiv (P\to \bot )$ .
- He discussed derived rules explicitly, though not always distinguishing them clearly from primitive ones in layout.
- His system is close to minimal, but allows derived steps for brevity.

Lemmon formalized more derived rules. He as well defined negation as implication to falsity: $\neg P\equiv P\to \bot$ . This is not stated as a formal definition in *Beginning Logic*, but it is implicitly assumed throughout the system, as evidenced by the following:

- Use of RAA (Reductio ad Absurdum): Lemmon regularly used RAA in the form: Assume P , derive $\bot$ , then conclude $\neg P$ .
  - This only works if $\neg P$ is understood as $P\to \bot$ .
- Proofs involving contradiction: Lemmon used the fact that from $\neg P\land P$ one can derive $\bot$ .
  - This requires treating $\neg P$ as $P\to \bot$ , so that modus ponens yields contradiction.
- Absence of a primitive “¬” rule: Lemmon did not include a standalone rule for introducing or eliminating ¬. Instead, he derived negation using implication and contradiction.

In the table below, based on Lemmon (1978) and Allen & Hand (2022), Lemmon's derived rules are highlighted. They can be derived from the (non-highlighted) Gentzen rules.

There are nine primitive rules of proof, which are the rule *assumption*, plus four pairs of introduction and elimination rules for the binary connectives, and the rules of *double negation* and *reductio ad absurdum*, of which only one is needed. *Disjunctive Syllogism* can be used as an easier alternative to the proper ∨-elimination, and MTT is a commonly given rule, although it is not primitive.

| Rule Name | Alternative names | Annotation | Assumption set | Statement |
|---|---|---|---|---|
| Rule of Assumptions | Assumption | **A** | The current line number. | At any stage of the argument, introduce a proposition as an assumption of the argument. |
| Conjunction introduction | Ampersand introduction, conjunction (CONJ) | **m, n &I** | The union of the assumption sets at lines **m** and **n**. | From $\varphi$ and $\psi$ at lines **m** and **n**, infer $\varphi \land \psi$ . |
| Conjunction elimination | Simplification (S), ampersand elimination | **m &E** | The same as at line **m**. | From $\varphi \land \psi$ at line **m**, infer $\varphi$ and $\psi$ . |
| Disjunction introduction | Addition (ADD) | **m ∨I** | The same as at line **m**. | From $\varphi$ at line **m**, infer $\varphi \lor \psi$ , whatever $\psi$ may be. |
| Disjunction elimination | Wedge elimination, dilemma (DL) | **j,k,l,m,n ∨E** | The lines **j,k,l,m,n**. | From $\varphi \lor \psi$ at line **j**, and an assumption of $\varphi$ at line **k**, and a derivation of $\chi$ from $\varphi$ at line **l**, and an assumption of $\psi$ at line **m**, and a derivation of $\chi$ from $\psi$ at line **n**, infer $\chi$ . |
| Arrow introduction | Conditional proof (CP), conditional introduction | **n, →I (m)** | Everything in the assumption set at line **n**, excepting **m**, the line where the antecedent was assumed. | From $\psi$ at line **n**, following from the assumption of $\varphi$ at line **m**, infer $\varphi \to \psi$ . |
| Arrow elimination | Modus ponendo ponens (MPP), modus ponens (MP), conditional elimination | **m, n →E** | The union of the assumption sets at lines **m** and **n**. | From $\varphi \to \psi$ at line **m**, and $\varphi$ at line **n**, infer $\psi$ . |
| Double negation | Double negation elimination | **m DN** | The same as at line **m**. | From $\neg \neg \varphi$ at line **m**, infer $\varphi$ . |
| Reductio ad absurdum | Indirect Proof (IP), negation introduction (¬I), negation elimination (¬E) | **m,** **n** **RAA** **(k)** | The union of the assumption sets at lines **m** and **n**, excluding **k** (the denied assumption). | To simplify the statement of the rule, the word "denial" here is used in this way: the *denial* of a formula $\varphi$ that is not a *negation* is $\neg \varphi$ , whereas a *negation*, $\neg \varphi$ , has two *denials*, viz., $\varphi$ and $\neg \neg \varphi$ . at lines **m** and **n**, infer the denial of any assumption appearing in the proof (at line **k**). |
| Disjunctive Syllogism | Wedge elimination (∨E), modus tollendo ponens (MTP) | **m,n DS** | The union of the assumption sets at lines **m** and **n**. | From $\varphi \lor \psi$ at line **m** and $\neg \varphi$ at line **n**, infer $\psi$ From $\varphi \lor \psi$ at line **m** and $\neg \psi$ at line **n**, infer $\varphi$ . |
| Double arrow introduction | Biconditional definition (*Df* $\leftrightarrow$ ), biconditional introduction | **m, n $\leftrightarrow$ I** | The union of the assumption sets at lines **m** and **n**. | From $\varphi \to \psi$ and $\psi \to \varphi$ at lines **m** and **n**, infer $\varphi \leftrightarrow \psi$ . |
| Double arrow elimination | Biconditional definition (*Df* $\leftrightarrow$ ), biconditional elimination | **m $\leftrightarrow$ E** | The same as at line **m**. | From $\varphi \leftrightarrow \psi$ at line **m**, infer either $\varphi \to \psi$ or $\psi \to \varphi$ . |
| Modus tollendo tollens | Modus tollens (MT) | **m, n MTT** | The union of the assumption sets at lines **m** and **n**. | From $\varphi \to \psi$ at line **m**, and $\neg \psi$ at line **n**, infer $\neg \varphi$ . |

### Suppes–Lemmon-style examples proof

Recall that an example proof was already given when introducing § Suppes–Lemmon notation. This is a second example.

#### Example 2

| $P\lor Q,\neg P,\neg P\to \neg Q\vdash \bot$ contradiction |   |   |   |
|---|---|---|---|
| Assumption set | Line number | Formula | Annotation |
| 1 | 1 | $P\lor Q$ | A |
| 2 | 2 | $\neg P$ | A |
| 3 | 3 | $\neg P\to \neg Q$ | A |
| 2,3 | 4 | $\neg Q$ | 2, 3 →E |
| 1,2,3 | 5 | P | A (subproof) |
| 1,2,3,5 | 6 | $\bot$ | 2, 5 RAA |
| 1,2,3 | 7 | Q | A (subproof) |
| 1,2,3,7 | 8 | $\bot$ | 4, 7 RAA |
| 1,2,3 | 9 | $\bot$ | 1, 5–6, 7–8 vE |
| Q.E.D. |   |   |   |

#### Example 3

The next derivation proves two theorems:

- lines 1 - 8 prove **within minimal logic**:

$\vdash _{MPC}\neg \neg (P\lor \neg P)$

.

- lines 1 - 9 prove **within classical logic**:

$\vdash _{CPC}P\lor \neg P$

.

Goals:

- lines 1 - 8: $\vdash _{MPC}((P\lor (P\to \bot ))\to \bot )\to \bot$ .
- lines 1 - 9: $\vdash _{CPC}P\lor (P\to \bot )$ .

| $\vdash P\lor \neg P$ |   |   |   |
|---|---|---|---|
| Assumption set | Line number | Formula | Annotation |
| 1 | 1 | $(P\lor (P\to \bot ))\to \bot$ | A |
| 1, 2 | 2 | P | A |
| 1, 2 | 3 | $P\lor (P\to \bot )$ | 2, ∨I |
| 1, 2 | 4 | $\bot$ | 1, 3, →E |
| 1 | 5 | $P\to \bot$ | 2, 4, →I (discharging 2) |
| 1 | 6 | $P\lor (P\to \bot )$ | 5, ∨I |
| 1 | 7 | $\bot$ | 1, 6, →E |
| ∅ | 8 | $((P\lor (P\to \bot ))\to \bot )\to \bot$ | 1, 7, →I (discharging 1) |
| ∅ | 9 | $P\lor (P\to \bot )$ | 8, DN |
| Q.E.D |   |   |   |

**Remark**: Valery Glivenko proved the following theorem:

If

$\varphi$

is a

propositional formula

, then

$\varphi$

is a classical

tautology

if and only if

$\neg \neg \varphi$

is an intuitionistic tautology.

This implies that all classical propositional theorems $\varphi$ can be proved like in this example:

1. Prove $\neg \neg \varphi$ within intuitionistic logic (i.e. without $\neg \neg _{E}$ ).
2. Apply $\neg \neg _{E}$ to get $\varphi$ from $\neg \neg \varphi$ .


## Consistency, completeness, and normal forms

A theory is said to be consistent if falsehood is not provable (from no assumptions) and is complete if every theorem or its negation is provable using the inference rules of the logic. These are statements about the entire logic, and are usually tied to some notion of a model. However, there are local notions of consistency and completeness that are purely syntactic checks on the inference rules, and require no appeals to models. The first of these is local consistency, also known as local reducibility, which says that any derivation containing an introduction of a connective followed immediately by its elimination can be turned into an equivalent derivation without this detour. It is a check on the *strength* of elimination rules: they must not be so strong that they include knowledge not already contained in their premises. As an example, consider conjunctions.

${\begin{aligned}{\cfrac {{\cfrac {{\cfrac {}{A\ }}u\qquad {\cfrac {}{B\ }}w}{A\wedge B\ }}\wedge _{I}}{A\ }}\wedge _{E1}\end{aligned}}\quad \Rightarrow \quad {\cfrac {}{A\ }}u$

Dually, local completeness says that the elimination rules are strong enough to decompose a connective into the forms suitable for its introduction rule. Again for conjunctions:

${\cfrac {}{A\wedge B\ }}u\quad \Rightarrow \quad {\begin{aligned}{\cfrac {{\cfrac {{\cfrac {}{A\wedge B\ }}u}{A\ }}\wedge _{E1}\qquad {\cfrac {{\cfrac {}{A\wedge B\ }}u}{B\ }}\wedge _{E2}}{A\wedge B\ }}\wedge _{I}\end{aligned}}$

These notions correspond exactly to β-reduction (beta reduction) and η-conversion (eta conversion) in the lambda calculus, using the Curry–Howard isomorphism. By local completeness, we see that every derivation can be converted to an equivalent derivation where the principal connective is introduced. In fact, if the entire derivation obeys this ordering of eliminations followed by introductions, then it is said to be *normal*. In a normal derivation all eliminations happen above introductions. In most logics, every derivation has an equivalent normal derivation, called a *normal form*. The existence of normal forms is generally hard to prove using natural deduction alone, though such accounts do exist in the literature, most notably by Dag Prawitz in 1961. It is much easier to show this indirectly by means of a cut-free sequent calculus presentation.


## First and higher-order extensions

The logic of the earlier section is an example of a *single-sorted* logic, *i.e.*, a logic with a single kind of object: propositions. Many extensions of this simple framework have been proposed; in this section we will extend it with a second sort of *individuals* or *terms*. More precisely, we will add a new category, "term", denoted ${\mathcal {T}}$ . We shall fix a countable set *V* of *variables*, another countable set F of *function symbols*, and construct terms with the following formation rules:

${\frac {v\in V}{v:{\mathcal {T}}}}{\hbox{ var}}_{F}$

and

${\frac {f\in F\qquad t_{1}:{\mathcal {T}}\qquad t_{2}:{\mathcal {T}}\qquad \cdots \qquad t_{n}:{\mathcal {T}}}{f(t_{1},t_{2},\cdots ,t_{n}):{\mathcal {T}}}}{\hbox{ app}}_{F}$

For propositions, we consider a third countable set *P* of *predicates*, and define *atomic predicates over terms* with the following formation rule:

${\frac {\phi \in P\qquad t_{1}:{\mathcal {T}}\qquad t_{2}:{\mathcal {T}}\qquad \cdots \qquad t_{n}:{\mathcal {T}}}{\phi (t_{1},t_{2},\cdots ,t_{n}):{\mathcal {F}}}}{\hbox{ pred}}_{F}$

The first two rules of formation provide a definition of a term that is effectively the same as that defined in term algebra and model theory, although the focus of those fields of study is quite different from natural deduction. The third rule of formation effectively defines an atomic formula, as in first-order logic, and again in model theory.

To these are added a pair of formation rules, defining the notation for *quantified* propositions; one for universal (∀) and existential (∃) quantification:

${\frac {x\in V\qquad A:{\mathcal {F}}}{\forall x.A:{\mathcal {F}}}}\;\forall _{F}\qquad \qquad {\frac {x\in V\qquad A:{\mathcal {F}}}{\exists x.A:{\mathcal {F}}}}\;\exists _{F}$

The universal quantifier has the introduction and elimination rules:

${\cfrac {\begin{array}{c}{\cfrac {}{a:{\mathcal {T}}}}{\text{ u}}\\\vdots \\{}[a/x]A\end{array}}{\forall x.A}}\;\forall _{I^{u,a}}\qquad \qquad {\frac {\forall x.A\qquad t:{\mathcal {T}}}{[t/x]A}}\;\forall _{E}$

The existential quantifier has the introduction and elimination rules:

${\frac {[t/x]A}{\exists x.A}}\;\exists _{I}\qquad \qquad {\cfrac {\begin{array}{cc}&\underbrace {\,{\cfrac {}{a:{\mathcal {T}}}}{\hbox{ u}}\quad {\cfrac {}{[a/x]A}}{\hbox{ v}}\,} \\&\vdots \\\exists x.A\quad &C\\\end{array}}{C}}\exists _{E^{a,u,v}}$

In these rules, the notation [*t*/*x*] *A* stands for the substitution of *t* for every (visible) instance of *x* in *A*, avoiding capture. As before the superscripts on the name stand for the components that are discharged: the term *a* cannot occur in the conclusion of ∀I (such terms are known as *eigenvariables* or *parameters*), and the hypotheses named *u* and *v* in ∃E are localised to the second premise in a hypothetical derivation. Although the propositional logic of earlier sections was decidable, adding the quantifiers makes the logic undecidable.

So far, the quantified extensions are *first-order*: they distinguish propositions from the kinds of objects quantified over. Higher-order logic takes a different approach and has only a single sort of propositions. The quantifiers have as the domain of quantification the very same sort of propositions, as reflected in the formation rules:

${\cfrac {\begin{matrix}{\cfrac {}{p:{\mathcal {F}}}}{\hbox{ u}}\\\vdots \\A:{\mathcal {F}}\\\end{matrix}}{\forall p.A:{\mathcal {F}}}}\;\forall _{F^{u}}\qquad \qquad {\cfrac {\begin{matrix}{\cfrac {}{p:{\mathcal {F}}}}{\hbox{ u}}\\\vdots \\A:{\mathcal {F}}\\\end{matrix}}{\exists p.A:{\mathcal {F}}}}\;\exists _{F^{u}}$

A discussion of the introduction and elimination forms for higher-order logic is beyond the scope of this article. It is possible to be in-between first-order and higher-order logics. For example, second-order logic has two kinds of propositions, one kind quantifying over terms, and the second kind quantifying over propositions of the first kind.


## Proofs and type theory

The presentation of natural deduction so far has concentrated on the nature of propositions without giving a formal definition of a *proof*. To formalise the notion of proof, we alter the presentation of hypothetical derivations slightly. We label the antecedents with *proof variables* (from some countable set *V* of variables), and decorate the succedent with the actual proof. The antecedents or *hypotheses* are separated from the succedent by means of a *turnstile* (⊢). This modification sometimes goes under the name of *localised hypotheses*. The following diagram summarises the change.

| ──── u1 ──── u2 ... ──── un J1 J2 Jn ⋮ J | ⇒ | u1:J1, u2:J2, ..., un:Jn ⊢ J |
|---|---|---|

The collection of hypotheses will be written as Γ when their exact composition is not relevant. To make proofs explicit, we move from the proof-less judgment "*A*" to a judgment: "π *is a proof of (A)*", which is written symbolically as "π : *A*". Following the standard approach, proofs are specified with their own formation rules for the judgment "π *proof*". The simplest possible proof is the use of a labelled hypothesis; in this case the evidence is the label itself.

| u ∈ V ─────── proof-F u proof |   | ───────────────────── hyp u:A ⊢ u : A |
|---|---|---|

Let us re-examine some of the connectives with explicit proofs. For conjunction, we look at the introduction rule ∧I to discover the form of proofs of conjunction: they must be a pair of proofs of the two conjuncts. Thus:

| π1 proof π2 proof ──────────────────── pair-F (π1, π2) proof |   | Γ ⊢ π1 : A Γ ⊢ π2 : B ───────────────────────── ∧I Γ ⊢ (π1, π2) : A ∧ B |
|---|---|---|

The elimination rules ∧E1 and ∧E2 select either the left or the right conjunct; thus the proofs are a pair of projections—first (**fst**) and second (**snd**).

| π proof ─────────── **fst**-F **fst** π proof |   | Γ ⊢ π : A ∧ B ───────────── ∧E1 Γ ⊢ **fst** π : A |
|---|---|---|
| π proof ─────────── **snd**-F **snd** π proof |   | Γ ⊢ π : A ∧ B ───────────── ∧E2 Γ ⊢ **snd** π : B |

For implication, the introduction form localises or *binds* the hypothesis, written using a λ; this corresponds to the discharged label. In the rule, "Γ, *u*:*A*" stands for the collection of hypotheses Γ, together with the additional hypothesis *u*.

| π proof ──────────── λ-F λu. π proof |   | Γ, u:A ⊢ π : B ───────────────── ⊃I Γ ⊢ λu. π : A ⊃ B |
|---|---|---|
| π1 proof π2 proof ─────────────────── app-F π1 π2 proof |   | Γ ⊢ π1 : A ⊃ B Γ ⊢ π2 : A ──────────────────────────── ⊃E Γ ⊢ π1 π2 : B |

With proofs available explicitly, one can manipulate and reason about proofs. The key operation on proofs is the substitution of one proof for an assumption used in another proof. This is commonly known as a *substitution theorem*, and can be proved by induction on the depth (or structure) of the second judgment.

### Substitution theorem

If

Γ ⊢ π

1

:

A

and

Γ,

u

:

A

⊢ π

2

:

B

,

then

Γ ⊢ [π

1

/

u

] π

2

: B.

So far the judgment "Γ ⊢ π : *A*" has had a purely logical interpretation. In type theory, the logical view is exchanged for a more computational view of objects. Propositions in the logical interpretation are now viewed as *types*, and proofs as programs in the lambda calculus. Thus the interpretation of "π : *A*" is "*the program* π has type *A*". The logical connectives are also given a different reading: conjunction is viewed as product (×), implication as the function arrow (→), etc. The differences are only cosmetic, however. Type theory has a natural deduction presentation in terms of formation, introduction and elimination rules; in fact, the reader can easily reconstruct what is known as *simple type theory* from the previous sections.

The difference between logic and type theory is primarily a shift of focus from the types (propositions) to the programs (proofs). Type theory is chiefly interested in the convertibility or reducibility of programs. For every type, there are canonical programs of that type which are irreducible; these are known as *canonical forms* or *values*. If every program can be reduced to a canonical form, then the type theory is said to be *normalising* (or *weakly normalising*). If the canonical form is unique, then the theory is said to be *strongly normalising*. Normalisability is a rare feature of most non-trivial type theories, which is a big departure from the logical world. (Recall that almost every logical derivation has an equivalent normal derivation.) To sketch the reason: in type theories that admit recursive definitions, it is possible to write programs that never reduce to a value; such looping programs can generally be given any type. In particular, the looping program has type ⊥, although there is no logical proof of "⊥". For this reason, the *propositions as types; proofs as programs* paradigm only works in one direction, if at all: interpreting a type theory as a logic generally gives an inconsistent logic.

### Example: Dependent Type Theory

Like logic, type theory has many extensions and variants, including first-order and higher-order versions. One branch, known as dependent type theory, is used in a number of computer-assisted proof systems. Dependent type theory allows quantifiers to range over programs themselves. These quantified types are written as Π and Σ instead of ∀ and ∃, and have the following formation rules:

| Γ ⊢ A type Γ, x:A ⊢ B type ───────────────────────────── Π-F Γ ⊢ Πx:A. B type |   | Γ ⊢ A type Γ, x:A ⊢ B type ──────────────────────────── Σ-F Γ ⊢ Σx:A. B type |
|---|---|---|

These types are generalisations of the arrow and product types, respectively, as witnessed by their introduction and elimination rules.

| Γ, x:A ⊢ π : B ──────────────────── ΠI Γ ⊢ λx. π : Πx:A. B |   | Γ ⊢ π1 : Πx:A. B Γ ⊢ π2 : A ───────────────────────────── ΠE Γ ⊢ π1 π2 : [π2/x] B |
|---|---|---|

| Γ ⊢ π1 : A Γ, x:A ⊢ π2 : B ───────────────────────────── ΣI Γ ⊢ (π1, π2) : Σx:A. B |   | Γ ⊢ π : Σx:A. B ──────────────── ΣE1 Γ ⊢ **fst** π : A |
|---|---|---|

| Γ ⊢ π : Σx:A. B ──────────────────────── ΣE2 Γ ⊢ **snd** π : [**fst** π/x] B |
|---|

Dependent type theory in full generality is very powerful: it is able to express almost any conceivable property of programs directly in the types of the program. This generality comes at a steep price — either typechecking is undecidable (extensional type theory), or extensional reasoning is more difficult (intensional type theory). For this reason, some dependent type theories do not allow quantification over arbitrary programs, but rather restrict to programs of a given decidable *index domain*, for example integers, strings, or linear programs.

Since dependent type theories allow types to depend on programs, a natural question to ask is whether it is possible for programs to depend on types, or any other combination. There are many kinds of answers to such questions. A popular approach in type theory is to allow programs to be quantified over types, also known as *parametric polymorphism*; of this there are two main kinds: if types and programs are kept separate, then one obtains a somewhat more well-behaved system called *predicative polymorphism*; if the distinction between program and type is blurred, one obtains the type-theoretic analogue of higher-order logic, also known as *impredicative polymorphism*. Various combinations of dependency and polymorphism have been considered in the literature, the most famous being the lambda cube of Henk Barendregt.

The intersection of logic and type theory is a vast and active research area. New logics are usually formalised in a general type theoretic setting, known as a logical framework. Popular modern logical frameworks such as the calculus of constructions and LF are based on higher-order dependent type theory, with various trade-offs in terms of decidability and expressive power. These logical frameworks are themselves always specified as natural deduction systems, which is a testament to the versatility of the natural deduction approach.


## Classical and modal logics

For simplicity, the logics presented so far have been intuitionistic. Classical logic extends intuitionistic logic with an additional axiom or principle of excluded middle:

For any proposition p, the proposition p ∨ ¬p is true.

This statement is not obviously either an introduction or an elimination; indeed, it involves two distinct connectives. Gentzen's original treatment of excluded middle prescribed one of the following three (equivalent) formulations, which were already present in analogous forms in the systems of Hilbert and Heyting:

| ────────────── XM1 A ∨ ¬A |   | ¬¬A ────────── XM2 A |   | ──────── *u* ¬A ⋮ *p* ────── XM3*u, p* A |
|---|---|---|---|---|

(XM3 is merely XM2 expressed in terms of E.) This treatment of excluded middle, in addition to being objectionable from a purist's standpoint, introduces additional complications in the definition of normal forms.

A comparatively more satisfactory treatment of classical natural deduction in terms of introduction and elimination rules alone was first proposed by Parigot in 1992 in the form of a classical lambda calculus called λμ. The key insight of his approach was to replace a truth-centric judgment *A* with a more classical notion, reminiscent of the sequent calculus: in localised form, instead of Γ ⊢ *A*, he used Γ ⊢ Δ, with Δ a collection of propositions similar to Γ. Γ was treated as a conjunction, and Δ as a disjunction. This structure is essentially lifted directly from classical sequent calculi, but the innovation in λμ was to give a computational meaning to classical natural deduction proofs in terms of a callcc or a throw/catch mechanism seen in LISP and its descendants. (See also: first class control.)

Another important extension was for modal and other logics that need more than just the basic judgment of truth. These were first described, for the alethic modal logics S4 and S5, in a natural deduction style by Prawitz in 1965, and have since accumulated a large body of related work. To give a simple example, the modal logic S4 requires one new judgment, "*A valid*", that is categorical with respect to truth:

If "A" (is true) under no assumption that "B" (is true), then "A valid".

This categorical judgment is internalised as a unary connective ◻*A* (read "*necessarily A*") with the following introduction and elimination rules:

| A valid ──────── ◻I ◻ A |   | ◻ A ──────── ◻E A |
|---|---|---|

Note that the premise "*A valid*" has no defining rules; instead, the categorical definition of validity is used in its place. This mode becomes clearer in the localised form when the hypotheses are explicit. We write "Ω;Γ ⊢ *A*" where Γ contains the true hypotheses as before, and Ω contains valid hypotheses. On the right there is just a single judgment "*A*"; validity is not needed here since "Ω ⊢ *A valid*" is by definition the same as "Ω;⋅ ⊢ *A*". The introduction and elimination forms are then:

| Ω;⋅ ⊢ π : A ──────────────────── ◻I Ω;⋅ ⊢ **box** π : ◻ A |   | Ω;Γ ⊢ π : ◻ A ────────────────────── ◻E Ω;Γ ⊢ **unbox** π : A |
|---|---|---|

The modal hypotheses have their own version of the hypothesis rule and substitution theorem.

| ─────────────────────────────── valid-hyp Ω, u: (A valid) ; Γ ⊢ u : A |
|---|

### Modal substitution theorem

If

Ω;⋅ ⊢ π

1

:

A

and

Ω,

u

: (

A valid

) ; Γ ⊢ π

2

:

C

,

then

Ω;Γ ⊢ [π

1

/

u

] π

2

:

C

.

This framework of separating judgments into distinct collections of hypotheses, also known as *multi-zoned* or *polyadic* contexts, is very powerful and extensible; it has been applied for many different modal logics, and also for linear and other substructural logics, to give a few examples. However, relatively few systems of modal logic can be formalised directly in natural deduction. To give proof-theoretic characterisations of these systems, extensions such as labelling or systems of deep inference.

The addition of labels to formulae permits much finer control of the conditions under which rules apply, allowing the more flexible techniques of analytic tableaux to be applied, as has been done in the case of labelled deduction. Labels also allow the naming of worlds in Kripke semantics; Simpson (1994) presents an influential technique for converting frame conditions of modal logics in Kripke semantics into inference rules in a natural deduction formalisation of hybrid logic. Stouppa (2004) surveys the application of many proof theories, such as Avron and Pottinger's hypersequents and Belnap's display logic to such modal logics as S5 and B.
