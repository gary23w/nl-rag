---
title: "Sequent calculus"
source: https://en.wikipedia.org/wiki/Sequent_calculus
domain: proof-theory
license: CC-BY-SA-4.0
tags: proof theory, natural deduction, sequent calculus, formal proof
fetched: 2026-07-02
---

# Sequent calculus

In mathematical logic, **sequent calculus** is a style of formal logical argumentation in which every line of a proof is a conditional tautology (called a sequent by Gerhard Gentzen) instead of an unconditional tautology. Each conditional tautology is inferred from other conditional tautologies on earlier lines in a formal argument according to rules and procedures of inference, giving a better approximation to the natural style of deduction used by mathematicians than David Hilbert's earlier style of formal logic, in which every line was an unconditional tautology. More subtle distinctions may exist; for example, propositions may implicitly depend upon non-logical axioms. In that case, sequents signify conditional theorems of a first-order theory rather than conditional tautologies.

Sequent calculus is one of several extant styles of proof calculus for expressing line-by-line logical arguments.

- Hilbert style. Every line is an unconditional tautology (or theorem).
- Gentzen style. Every line is a conditional tautology (or theorem) with zero or more conditions on the left.
  - Natural deduction. Every (conditional) line has exactly one asserted proposition on the right.
  - Sequent calculus. Every (conditional) line has zero or more asserted propositions on the right.

In other words, natural deduction and sequent calculus systems are particular distinct kinds of Gentzen-style systems. Hilbert-style systems typically have a very small number of inference rules, relying more on sets of axioms. Gentzen-style systems typically have very few axioms, if any, relying more on sets of rules.

Gentzen-style systems have significant practical and theoretical advantages compared to Hilbert-style systems. For example, both natural deduction and sequent calculus systems facilitate the elimination and introduction of universal and existential quantifiers so that unquantified logical expressions can be manipulated according to the much simpler rules of propositional calculus. In a typical argument, quantifiers are eliminated, then propositional calculus is applied to unquantified expressions (which typically contain free variables), and then the quantifiers are reintroduced. This very much parallels the way in which mathematical proofs are carried out in practice by mathematicians. Predicate calculus proofs are generally much easier to discover with this approach, and are often shorter. Natural deduction systems are more suited to practical theorem-proving. Sequent calculus systems are more suited to theoretical analysis.

## Overview

In proof theory and mathematical logic, sequent calculus is a family of formal systems sharing a certain style of inference and certain formal properties. The first sequent calculi systems, **LK** and **LJ**, were introduced in 1934/1935 by Gerhard Gentzen as a tool for studying natural deduction in first-order logic (in classical and intuitionistic versions, respectively). Gentzen's so-called "Main Theorem" (*Hauptsatz*) about LK and LJ was the cut-elimination theorem, a result with far-reaching meta-theoretic consequences, including consistency. Gentzen further demonstrated the power and flexibility of this technique a few years later, applying a cut-elimination argument to give a (transfinite) proof of the consistency of Peano arithmetic, in surprising response to Gödel's incompleteness theorems. Since this early work, sequent calculi, also called **Gentzen systems**, and the general concepts relating to them, have been widely applied in the fields of proof theory, mathematical logic, and automated deduction.

### Hilbert-style deduction systems

One way to classify different styles of deduction systems is to look at the form of *judgments* in the system, *i.e.*, which things may appear as the conclusion of a (sub)proof. The simplest judgment form is used in Hilbert-style deduction systems, where a judgment has the form

B

where B is any formula of first-order logic (or whatever logic the deduction system applies to, *e.g.*, propositional calculus or a higher-order logic or a modal logic). The theorems are those formulas that appear as the concluding judgment in a valid proof. A Hilbert-style system needs no distinction between formulas and judgments; we make one here solely for comparison with the cases that follow.

The price paid for the simple syntax of a Hilbert-style system is that complete formal proofs tend to get extremely long. Concrete arguments about proofs in such a system almost always appeal to the deduction theorem. This leads to the idea of including the deduction theorem as a formal rule in the system, which happens in natural deduction.

### Natural deduction systems

In natural deduction, judgments have the shape

$A_{1},A_{2},\ldots ,A_{n}\vdash B$

where the $A_{i}$ 's and B are again formulas and $n\geq 0$ . In other words, a judgment consists of a *list* (possibly empty) of formulas on the left-hand side of a turnstile symbol " $\vdash$ ", with a single formula on the right-hand side, (though permutations of the $A_{i}$ 's are often immaterial). The theorems are those formulae B such that $\vdash B$ (with an empty left-hand side) is the conclusion of a valid proof. (In some presentations of natural deduction, the $A_{i}$ s and the turnstile are not written down explicitly; instead a two-dimensional notation from which they can be inferred is used.)

The standard semantics of a judgment in natural deduction is that it asserts that whenever $A_{1}$ , $A_{2}$ , etc., are all true, B will also be true. The judgments

$A_{1},\ldots ,A_{n}\vdash B$

and

$\vdash (A_{1}\land \cdots \land A_{n})\rightarrow B$

are equivalent in the strong sense that a proof of either one may be extended to a proof of the other.

### Sequent calculus systems

Finally, sequent calculus generalizes the form of a natural deduction judgment to

$A_{1},\ldots ,A_{n}\vdash B_{1},\ldots ,B_{k},$

a syntactic object called a sequent. The formulas on left-hand side of the turnstile are called the *antecedent*, and the formulas on right-hand side are called the *succedent* or *consequent*; together they are called *cedents* or *sequent formulas*. Again, $A_{i}$ and $B_{i}$ are formulas, and n and k are nonnegative integers, that is, the left-hand-side or the right-hand-side (or neither or both) may be empty. As in natural deduction, theorems are those B where $\vdash B$ is the conclusion of a valid proof.

The standard semantics of a sequent is an assertion that whenever *every* $A_{i}$ is true, *at least one* $B_{i}$ will also be true. Thus the empty sequent, having both cedents empty, is false. One way to express this is that a comma to the left of the turnstile should be thought of as an "and", and a comma to the right of the turnstile should be thought of as an (inclusive) "or". The sequents

$A_{1},\ldots ,A_{n}\vdash B_{1},\ldots ,B_{k}$

and

$\vdash (A_{1}\land \cdots \land A_{n})\rightarrow (B_{1}\lor \cdots \lor B_{k})$

are equivalent in the strong sense that a proof of either sequent may be extended to a proof of the other sequent.

At first sight, this extension of the judgment form may appear to be a strange complication—it is not motivated by an obvious shortcoming of natural deduction, and it is initially confusing that the comma seems to mean entirely different things on the two sides of the turnstile. However, in a classical context the semantics of the sequent can also (by propositional tautology) be expressed either as

$\vdash \neg A_{1}\lor \neg A_{2}\lor \cdots \lor \neg A_{n}\lor B_{1}\lor B_{2}\lor \cdots \lor B_{k}$

(at least one of the As is false, or one of the Bs is true)

or as

$\vdash \neg (A_{1}\land A_{2}\land \cdots \land A_{n}\land \neg B_{1}\land \neg B_{2}\land \cdots \land \neg B_{k})$

(it cannot be the case that all of the As are true and all of the Bs are false).

In these formulations, the only difference between formulas on either side of the turnstile is that one side is negated. Thus, swapping left for right in a sequent corresponds to negating all of the constituent formulas. This means that a symmetry such as De Morgan's laws, which manifests itself as logical negation on the semantic level, translates directly into a left–right symmetry of sequents—and indeed, the inference rules in sequent calculus for dealing with conjunction (∧) are mirror images of those dealing with disjunction (∨).

Many logicians feel that this symmetric presentation offers a deeper insight in the structure of the logic than other styles of proof system, where the classical duality of negation is not as apparent in the rules.

### Distinction between natural deduction and sequent calculus

Gentzen asserted a sharp distinction between his single-output natural deduction systems (NK and NJ) and his multiple-output sequent calculus systems (LK and LJ). He wrote that the intuitionistic natural deduction system NJ was somewhat ugly. He said that the special role of the excluded middle in the classical natural deduction system NK is removed in the classical sequent calculus system LK. He said that the sequent calculus LJ gave more symmetry than natural deduction NJ in the case of intuitionistic logic, as also in the case of classical logic (LK versus NK). Then he said that in addition to these reasons, the sequent calculus with multiple succedent formulas is intended particularly for his principal theorem ("Hauptsatz").

### Historical notes

The word "sequent" is taken from the word "Sequenz" in Gentzen's 1934 paper. Kleene makes the following comment on the translation into English: "Gentzen says 'Sequenz', which we translate as 'sequent', because we have already used 'sequence' for any succession of objects, where the German is 'Folge'."

Gentzen used two-letter capitals to stand for various proof systems. In his 1935 paper, he stated that in **LK**, the **L** stood for "logische" (logical) and the **K** stood for "klassische Pradikatenlogik" ("classical predicative logic"). The **J** in **LJ** stood for "intuitionistische Pradikatenlogik" ("intuitionistic predicative logic"). Similarly, the **N** in **NK** and **NJ** stood for "natürlichen Schließens" ("natural deduction"). It is unclear how he came to use **J** to stand for "intuitionistische", but presumably to typographically distinguish it from the numeral 1 and the Roman numeral I. In other places, Gentzen used **LI** and **NI** instead of **LJ** and **NJ**.

## Proving logical formulas

### Reduction trees

Sequent calculus can be seen as a tool for proving formulas in propositional logic, similar to the method of analytic tableaux. It gives a series of steps that allows one to reduce the problem of proving a logical formula to simpler and simpler formulas until one arrives at trivial ones.

Consider the following formula:

$((p\rightarrow r)\lor (q\rightarrow r))\rightarrow ((p\land q)\rightarrow r)$

This is written in the following form, where the proposition that needs to be proven is to the right of the turnstile symbol $\vdash$ :

$\vdash ((p\rightarrow r)\lor (q\rightarrow r))\rightarrow ((p\land q)\rightarrow r)$

Now, instead of proving this from the axioms, it is enough to assume the premise of the implication and then try to prove its conclusion. Hence one moves to the following sequent:

$(p\rightarrow r)\lor (q\rightarrow r)\vdash (p\land q)\rightarrow r$

Again the right hand side includes an implication, whose premise can further be assumed so that only its conclusion needs to be proven:

$(p\rightarrow r)\lor (q\rightarrow r),(p\land q)\vdash r$

Since the arguments in the left-hand side are assumed to be related by conjunction, this can be replaced by the following:

$(p\rightarrow r)\lor (q\rightarrow r),p,q\vdash r$

This is equivalent to proving the conclusion in both cases of the disjunction on the first argument on the left. Thus we may split the sequent to two, where we now have to prove each separately:

$p\rightarrow r,p,q\vdash r$

$q\rightarrow r,p,q\vdash r$

In the case of the first judgment, we rewrite $p\rightarrow r$ as $\lnot p\lor r$ and split the sequent again to get:

$\lnot p,p,q\vdash r$

$r,p,q\vdash r$

The second sequent is done; the first sequent can be further simplified into:

$p,q\vdash p,r$

This process can always be continued until there are only atomic formulas in each side. The process can be graphically described by a rooted tree, as depicted on the right. The root of the tree is the formula we wish to prove; the leaves consist of atomic formulas only. The tree is known as a **reduction tree**.

The items to the left of the turnstile are understood to be connected by conjunction, and those to the right by disjunction. Therefore, when both consist only of atomic symbols, the sequent is accepted axiomatically (and always true) if and only if at least one of the symbols on the right also appears on the left.

Following are the rules by which one proceeds along the tree. Whenever one sequent is split into two, the tree vertex has two child vertices, and the tree is branched. Additionally, one may freely change the order of the arguments in each side; Γ and Δ stand for possible additional arguments.

The usual term for the horizontal line used in Gentzen-style layouts for natural deduction is **inference line**.

| Left | Right |
|---|---|
| $L\land {\text{rule: }}\quad {\cfrac {\Gamma ,A\land B\vdash \Delta }{\Gamma ,A,B\vdash \Delta }}$ | $R\land {\text{rule: }}{\cfrac {\Gamma \vdash \Delta ,A\land B}{\Gamma \vdash \Delta ,A\qquad \Gamma \vdash \Delta ,B}}$ |
| $L\lor {\text{rule: }}{\cfrac {\Gamma ,A\lor B\vdash \Delta }{\Gamma ,A\vdash \Delta \qquad \Gamma ,B\vdash \Delta }}$ | $R\lor {\text{rule: }}\quad {\cfrac {\Gamma \vdash \Delta ,A\lor B}{\Gamma \vdash \Delta ,A,B}}$ |
| $L\rightarrow {\text{rule: }}{\cfrac {\Gamma ,A\rightarrow B\vdash \Delta }{\Gamma \vdash \Delta ,A\qquad \Gamma ,B\vdash \Delta }}$ | $R\rightarrow {\text{rule: }}\quad {\cfrac {\Gamma \vdash \Delta ,A\rightarrow B}{\Gamma ,A\vdash \Delta ,B}}$ |
| $L\lnot {\text{rule: }}\quad {\cfrac {\Gamma ,\lnot A\vdash \Delta }{\Gamma \vdash \Delta ,A}}$ | $R\lnot {\text{rule: }}\quad {\cfrac {\Gamma \vdash \Delta ,\lnot A}{\Gamma ,A\vdash \Delta }}$ |
| Axiom: $\Gamma ,A\vdash \Delta ,A$ |   |

Starting with any formula in propositional logic, by a series of steps, the right side of the turnstile can be processed until it includes only atomic symbols. Then, the same is done for the left side. Since every logical operator appears in one of the rules above, and is removed by the rule, the process terminates when no logical operators remain: The formula has been *decomposed*.

Thus, the sequents in the leaves of the trees include only atomic symbols, which are either provable by the axiom or not, according to whether one of the symbols on the right also appears on the left.

It is easy to see that the steps in the tree preserve the semantic truth value of the formulas implied by them, with conjunction understood between the tree's different branches whenever there is a split. It is also obvious that an axiom is provable if and only if it is true for every assignment of truth values to the atomic symbols. Thus this system is sound and complete for classical propositional logic.

### Relation to standard axiomatizations

Sequent calculus is related to other axiomatizations of classical propositional calculus, such as Frege's propositional calculus or Jan Łukasiewicz's axiomatization (itself a part of the standard Hilbert system): Every formula that can be proven in these has a reduction tree. This can be shown as follows: Every proof in propositional calculus uses only axioms and the inference rules. Each use of an axiom scheme yields a true logical formula, and can thus be proven in sequent calculus; examples for these are shown below. The only inference rule in the systems mentioned above is modus ponens, which is implemented by the cut rule.

## The system LK

This section introduces the rules of the sequent calculus **LK** (standing for Logistische Kalkül) as introduced by Gentzen in 1934. A (formal) proof in this calculus is a finite sequence of sequents, where each of the sequents is derivable from sequents appearing earlier in the sequence by using one of the rules below.

### Inference rules

The following notation will be used:

- $\vdash$ known as the turnstile, separates the *assumptions* on the left from the *propositions* on the right
- A and B denote formulas of first-order predicate logic (one may also restrict this to propositional logic),
- $\Gamma ,\Delta ,\Sigma$ , and $\Pi$ are finite (possibly empty) sequences of formulas (in fact, the order of formulas does not matter; see § Structural rules), called contexts,
  - when on the *left* of the $\vdash$ , the sequence of formulas is considered *conjunctively* (all assumed to hold at the same time),
  - while on the *right* of the $\vdash$ , the sequence of formulas is considered *disjunctively* (at least one of the formulas must hold for any assignment of variables),
- t denotes an arbitrary term,
- x and y denote variables.
- a variable is said to occur free within a formula if it is not bound by quantifiers $\forall$ or $\exists$ .
- $A[t/x]$ denotes the formula that is obtained by substituting the term t for every free occurrence of the variable x in formula A with the restriction that the term t must be free for the variable x in A (i.e., no occurrence of any variable in t becomes bound in $A[t/x]$ ).
- $WL$ , $WR$ , $CL$ , $CR$ , $PL$ , $PR$ : These six stand for the two versions of each of three structural rules; one for use on the left ('L') of a $\vdash$ , and the other on its right ('R'). The rules are abbreviated 'W' for *Weakening (Left/Right)*, 'C' for *Contraction*, and 'P' for *Permutation*.

Note that, contrary to the rules for proceeding along the reduction tree presented above, the following rules are for moving in the opposite directions, from axioms to theorems. Thus they are exact mirror-images of the rules above, except that here symmetry is not implicitly assumed, and rules regarding quantification are added.

In the table below, $A\setminus B$ denotes the relative complement of B in A .

| Axiom | Cut |
|---|---|
| ${\cfrac {\qquad }{A\vdash A}}\quad (I)$ | ${\cfrac {\Gamma \vdash \Delta ,A\qquad A,\Sigma \vdash \Pi }{\Gamma ,\Sigma \vdash \Delta ,\Pi }}\quad ({\mathit {Cut}})$ |

| Left logical rules | Right logical rules |
|---|---|
| ${\cfrac {\Gamma ,A\vdash \Delta }{\Gamma ,A\land B\vdash \Delta }}\quad ({\land }L_{1})$ | ${\cfrac {\Gamma \vdash A,\Delta }{\Gamma \vdash A\lor B,\Delta }}\quad ({\lor }R_{1})$ |
| ${\cfrac {\Gamma ,B\vdash \Delta }{\Gamma ,A\land B\vdash \Delta }}\quad ({\land }L_{2})$ | ${\cfrac {\Gamma \vdash B,\Delta }{\Gamma \vdash A\lor B,\Delta }}\quad ({\lor }R_{2})$ |
| ${\cfrac {\Gamma ,A\vdash \Delta \qquad \Gamma ,B\vdash \Delta }{\Gamma ,A\lor B\vdash \Delta }}\quad ({\lor }L)$ | ${\cfrac {\Gamma \vdash A,\Delta \qquad \Gamma \vdash B,\Delta }{\Gamma \vdash A\land B,\Delta }}\quad ({\land }R)$ |
| ${\cfrac {\Gamma \vdash A,\Delta \qquad \Sigma ,B\vdash \Pi }{\Gamma ,\Sigma ,A\rightarrow B\vdash \Delta ,\Pi }}\quad ({\rightarrow }L)$ | ${\cfrac {\Gamma ,A\vdash B,\Delta }{\Gamma \vdash A\rightarrow B,\Delta }}\quad ({\rightarrow }R)$ |
| ${\cfrac {\Gamma ,A\vdash B,\Delta }{\Gamma ,A\setminus B\vdash \Delta }}\quad ({\setminus }L)$ | ${\cfrac {\Gamma \vdash A,\Delta \qquad \Sigma ,B\vdash \Pi }{\Gamma ,\Sigma \vdash A\setminus B,\Delta ,\Pi }}\quad ({\setminus }R)$ |
| ${\cfrac {\Gamma \vdash A,\Delta }{\Gamma ,\lnot A\vdash \Delta }}\quad ({\lnot }L)$ | ${\cfrac {\Gamma ,A\vdash \Delta }{\Gamma \vdash \lnot A,\Delta }}\quad ({\lnot }R)$ |
| ${\cfrac {\Gamma ,A[t/x]\vdash \Delta }{\Gamma ,\forall xA\vdash \Delta }}\quad ({\forall }L)$ | ${\cfrac {\Gamma \vdash A[y/x],\Delta }{\Gamma \vdash \forall xA,\Delta }}\quad ({\forall }R)$ (†) |
| ${\cfrac {\Gamma ,A[y/x]\vdash \Delta }{\Gamma ,\exists xA\vdash \Delta }}\quad ({\exists }L)$ (†) | ${\cfrac {\Gamma \vdash A[t/x],\Delta }{\Gamma \vdash \exists xA,\Delta }}\quad ({\exists }R)$ |

| Left structural rules | Right structural rules |
|---|---|
| ${\cfrac {\Gamma \vdash \Delta }{\Gamma ,A\vdash \Delta }}\quad ({\mathit {WL}})$ | ${\cfrac {\Gamma \vdash \Delta }{\Gamma \vdash A,\Delta }}\quad ({\mathit {WR}})$ |
| ${\cfrac {\Gamma ,A,A\vdash \Delta }{\Gamma ,A\vdash \Delta }}\quad ({\mathit {CL}})$ | ${\cfrac {\Gamma \vdash A,A,\Delta }{\Gamma \vdash A,\Delta }}\quad ({\mathit {CR}})$ |
| ${\cfrac {\Gamma _{1},A,B,\Gamma _{2}\vdash \Delta }{\Gamma _{1},B,A,\Gamma _{2}\vdash \Delta }}\quad ({\mathit {PL}})$ | ${\cfrac {\Gamma \vdash \Delta _{1},A,B,\Delta _{2}}{\Gamma \vdash \Delta _{1},B,A,\Delta _{2}}}\quad ({\mathit {PR}})$ |

***Restrictions**: In the rules marked with (†), $({\forall }R)$ and $({\exists }L)$ , the variable y must not occur free anywhere in the respective lower sequents.*

### An intuitive explanation

The above rules can be divided into two major groups: *logical* and *structural* ones. Each of the logical rules introduces a new logical formula either on the left or on the right of the turnstile $\vdash$ . In contrast, the structural rules operate on the structure of the sequents, ignoring the exact shape of the formulas. The two exceptions to this general scheme are the axiom of identity (I) and the rule of (Cut).

Although stated in a formal way, the above rules allow for a very intuitive reading in terms of classical logic. Consider, for example, the rule $({\land }L_{1})$ . It says that, whenever one can prove that $\Delta$ can be concluded from some sequence of formulas that contain A , then one can also conclude $\Delta$ from the (stronger) assumption that $A\land B$ holds. Likewise, the rule $({\neg }R)$ states that, if $\Gamma$ and A suffice to conclude $\Delta$ , then from $\Gamma$ alone one can either still conclude $\Delta$ or that A must be false, i.e. ${\neg }A$ holds. All the rules can be interpreted in this way.

For an intuition about the quantifier rules, consider the rule $({\forall }R)$ . Of course concluding that $\forall {x}A$ holds just from the fact that $A[y/x]$ is true is not in general possible. If, however, the variable *y* is not mentioned elsewhere (i.e. it can still be chosen freely, without influencing the other formulas), then one may assume, that $A[y/x]$ holds for any value of *y*. The other rules should then be pretty straightforward.

Instead of viewing the rules as descriptions for legal derivations in predicate logic, one may also consider them as instructions for the construction of a proof for a given statement. In this case the rules can be read bottom-up; for example, $({\land }R)$ says that, to prove that $A\land B$ follows from the assumptions $\Gamma$ and $\Sigma$ , it suffices to prove that A can be concluded from $\Gamma$ and B can be concluded from $\Sigma$ , respectively. Note that, given some antecedent, it is not clear how this is to be split into $\Gamma$ and $\Sigma$ . However, there are only finitely many possibilities to be checked since the antecedent by assumption is finite. This also illustrates how proof theory can be viewed as operating on proofs in a combinatorial fashion: given proofs for both A and B , one can construct a proof for $A\land B$ .

When looking for some proof, most of the rules offer more or less direct recipes of how to do this. The rule of cut is different: it states that, when a formula A can be concluded and this formula may also serve as a premise for concluding other statements, then the formula A can be "cut out" and the respective derivations are joined. When constructing a proof bottom-up, this creates the problem of guessing A (since it does not appear at all below). The cut-elimination theorem is thus crucial to the applications of sequent calculus in automated deduction: it states that all uses of the cut rule can be eliminated from a proof, implying that any provable sequent can be given a *cut-free* proof.

The second rule that is somewhat special is the axiom of identity (I). The intuitive reading of this is obvious: every formula proves itself. Like the cut rule, the axiom of identity is somewhat redundant: the completeness of atomic initial sequents states that the rule can be restricted to atomic formulas without any loss of provability.

Observe that, if we ignore the non-standard connective \, all rules have mirror companions, except the ones for implication. This reflects the fact that the usual language of first-order logic does not include the "is not implied by" connective $\not \leftarrow$ that would be the De Morgan dual of implication. Adding such a connective with its natural rules makes the calculus completely left–right symmetric.

### Example derivations

Here is the derivation of " $\vdash A\lor \lnot A$ ", known as the *Law of excluded middle* (*tertium non datur* in Latin).

|   |   | $(I)$ |
|---|---|---|
| $A\vdash A$ |   |   |
|   | $(\lnot R)$ |   |
| $\vdash \lnot A,A$ |   |   |
|   | $(\lor R_{2})$ |   |
| $\vdash A\lor \lnot A,A$ |   |   |
|   | $(PR)$ |   |
| $\vdash A,A\lor \lnot A$ |   |   |
|   | $(\lor R_{1})$ |   |
| $\vdash A\lor \lnot A,A\lor \lnot A$ |   |   |
|   | $(CR)$ |   |
| $\vdash A\lor \lnot A$ |   |   |
|   |   |   |

Next is the proof of a simple fact involving quantifiers. Note that the converse is not true, and its falsity can be seen when attempting to derive it bottom-up, because an existing free variable cannot be used in substitution in the rules $(\forall R)$ and $(\exists L)$ .

|   |   | $(I)$ |
|---|---|---|
| $p(x,y)\vdash p(x,y)$ |   |   |
|   | $(\forall L)$ |   |
| $\forall x\left(p(x,y)\right)\vdash p(x,y)$ |   |   |
|   | $(\exists R)$ |   |
| $\forall x\left(p(x,y)\right)\vdash \exists y\left(p(x,y)\right)$ |   |   |
|   | $(\exists L)$ |   |
| $\exists y\left(\forall x\left(p(x,y)\right)\right)\vdash \exists y\left(p(x,y)\right)$ |   |   |
|   | $(\forall R)$ |   |
| $\exists y\left(\forall x\left(p(x,y)\right)\right)\vdash \forall x\left(\exists y\left(p(x,y)\right)\right)$ |   |   |
|   |   |   |

For something more interesting we shall prove ${\left(\left(A\rightarrow \left(B\lor C\right)\right)\rightarrow \left(\left(\left(B\rightarrow \lnot A\right)\land \lnot C\right)\rightarrow \lnot A\right)\right)}$ . It is straightforward to find the derivation, which exemplifies the usefulness of LK in automated proving.

| $(I)$ $A\vdash A$     $(\lnot R)$ $\vdash \lnot A,A$     $(PR)$ $\vdash A,\lnot A$            $(I)$ $B\vdash B$     $(WR)$ $B\vdash B,C$            $(I)$ $C\vdash C$     $(WR)$ $C\vdash B,C$         $(\lor L)$ $B\lor C\vdash B,C$     $(PR)$ $B\lor C\vdash C,B$     $(\lnot L)$ $B\lor C,\lnot C\vdash B$              $(I)$ $\lnot A\vdash \lnot A$         $(\rightarrow L)$ $\left(B\lor C\right),\lnot C,\left(B\rightarrow \lnot A\right)\vdash \lnot A$     $(\land L_{1})$ $\left(B\lor C\right),\lnot C,\left(\left(B\rightarrow \lnot A\right)\land \lnot C\right)\vdash \lnot A$     $(PL)$ $\left(B\lor C\right),\left(\left(B\rightarrow \lnot A\right)\land \lnot C\right),\lnot C\vdash \lnot A$     $(\land L_{2})$ $\left(B\lor C\right),\left(\left(B\rightarrow \lnot A\right)\land \lnot C\right),\left(\left(B\rightarrow \lnot A\right)\land \lnot C\right)\vdash \lnot A$     $(CL)$ $\left(B\lor C\right),\left(\left(B\rightarrow \lnot A\right)\land \lnot C\right)\vdash \lnot A$     $(PL)$ $\left(\left(B\rightarrow \lnot A\right)\land \lnot C\right),\left(B\lor C\right)\vdash \lnot A$ |   | $(\rightarrow L)$ |
|---|---|---|
| $\left(\left(B\rightarrow \lnot A\right)\land \lnot C\right),\left(A\rightarrow \left(B\lor C\right)\right)\vdash \lnot A,\lnot A$ |   |   |
|   | $(CR)$ |   |
| $\left(\left(B\rightarrow \lnot A\right)\land \lnot C\right),\left(A\rightarrow \left(B\lor C\right)\right)\vdash \lnot A$ |   |   |
|   | $(PL)$ |   |
| $\left(A\rightarrow \left(B\lor C\right)\right),\left(\left(B\rightarrow \lnot A\right)\land \lnot C\right)\vdash \lnot A$ |   |   |
|   | $(\rightarrow R)$ |   |
| $\left(A\rightarrow \left(B\lor C\right)\right)\vdash \left(\left(\left(B\rightarrow \lnot A\right)\land \lnot C\right)\rightarrow \lnot A\right)$ |   |   |
|   | $(\rightarrow R)$ |   |
| $\vdash \left(\left(A\rightarrow \left(B\lor C\right)\right)\rightarrow \left(\left(\left(B\rightarrow \lnot A\right)\land \lnot C\right)\rightarrow \lnot A\right)\right)$ |   |   |
|   |   |   |

These derivations also emphasize the strictly formal structure of the sequent calculus. For example, the logical rules as defined above always act on a formula immediately adjacent to the turnstile, such that the permutation rules are necessary. Note, however, that this is in part an artifact of the presentation, in the original style of Gentzen. A common simplification involves the use of multisets of formulas in the interpretation of the sequent, rather than sequences, eliminating the need for an explicit permutation rule. This corresponds to shifting commutativity of assumptions and derivations outside the sequent calculus, whereas LK embeds it within the system itself.

### Relation to analytic tableaux

For certain formulations (i.e. variants) of the sequent calculus, a proof in such a calculus is isomorphic to an upside-down, closed analytic tableau.

### Structural rules

The structural rules deserve some additional discussion.

Weakening (W) allows the addition of arbitrary elements to a sequence. Intuitively, this is allowed in the antecedent because we can always restrict the scope of our proof (if all cars have wheels, then it's safe to say that all black cars have wheels); and in the succedent because we can always allow for alternative conclusions (if all cars have wheels, then it's safe to say that all cars have either wheels or wings).

Contraction (C) and Permutation (P) assure that neither the order (P) nor the multiplicity of occurrences (C) of elements of the sequences matters. Thus, one could instead of sequences also consider sets.

The extra effort of using sequences, however, is justified since part or all of the structural rules may be omitted. Doing so, one obtains the so-called substructural logics.

### Properties of the system LK

This system of rules can be shown to be both sound and complete with respect to first-order logic, i.e. a statement A follows semantically from a set of premises $\Gamma$ $(\Gamma \vDash A)$ if and only if the sequent $\Gamma \vdash A$ can be derived by the above rules.

In the sequent calculus, the rule of cut is admissible. This result is also referred to as Gentzen's *Hauptsatz* ("Main Theorem").

## Variants

The above rules can be modified in various ways:

### Minor structural alternatives

There is some freedom of choice regarding the technical details of how sequents and structural rules are formalized without changing what sequents the system derives.

First of all, as mentioned above, the sequents can be viewed to consist of sets or multisets. In this case, the rules for permuting and (when using sets) contracting formulas are unnecessary.

The rule of weakening becomes admissible if the axiom (I) is changed to derive any sequent of the form $\Gamma ,A\vdash A,\Delta$ . Any weakening that appears in a derivation can then be moved to the beginning of the proof. This may be a convenient change when constructing proofs bottom-up.

One may also change whether rules with more than one premise share the same context for each of those premises or split their contexts between them: For example, $({\lor }L)$ may be instead formulated as

${\cfrac {\Gamma ,A\vdash \Delta \qquad \Sigma ,B\vdash \Pi }{\Gamma ,\Sigma ,A\lor B\vdash \Delta ,\Pi }}.$

Contraction and weakening make this version of the rule interderivable with the version above, although in their absence, as in linear logic, these rules define different connectives.

### Absurdity

One can introduce $\bot$ , the absurdity constant representing *false*, with the axiom:

${\cfrac {}{\bot \vdash \quad }}$

Or if, as described above, weakening is to be an admissible rule, then with the axiom:

${\cfrac {}{\Gamma ,\bot \vdash \Delta }}$

With $\bot$ , negation can be subsumed as a special case of implication, via the definition $(\neg A)\iff (A\to \bot )$ .

### Substructural logics

Alternatively, one may restrict or forbid the use of some of the structural rules. This yields a variety of substructural logic systems. They are generally weaker than LK (*i.e.*, they have fewer theorems), and thus not complete with respect to the standard semantics of first-order logic. However, they have other interesting properties that have led to applications in theoretical computer science and artificial intelligence.

### Intuitionistic sequent calculus: System LJ

Surprisingly, some small changes in the rules of LK suffice to turn it into a proof system for intuitionistic logic. To this end, one has to restrict to sequents with at most one formula on the right-hand side, and modify the rules to maintain this invariant. For example, $({\lor }L)$ is reformulated as follows (where C is an arbitrary formula):

${\cfrac {\Gamma ,A\vdash C\qquad \Gamma ,B\vdash C}{\Gamma ,A\lor B\vdash C}}\quad ({\lor }L)$

The resulting system is called LJ. It is sound and complete with respect to intuitionistic logic and admits a similar cut-elimination proof. This can be used in proving disjunction and existence properties.

In fact, the only rules in LK that need to be restricted to single-formula consequents are $({\to }R)$ , $(\neg R)$ (which can be seen as a special case of ${\to }R$ , as described above) and $({\forall }R)$ . When multi-formula consequents are interpreted as disjunctions, all of the other inference rules of LK are derivable in LJ, while the rules $({\to }R)$ and $({\forall }R)$ become

${\cfrac {\Gamma ,A\vdash B\lor C}{\Gamma \vdash (A\to B)\lor C}}$

and (when y does not occur free in the bottom sequent)

${\cfrac {\Gamma \vdash A[y/x]\lor C}{\Gamma \vdash (\forall xA)\lor C}}.$

These two rules are *not* intuitionistically valid.
