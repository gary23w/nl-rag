---
title: "Equational logic"
source: https://en.wikipedia.org/wiki/Equational_logic
domain: knuth-bendix
license: CC-BY-SA-4.0
tags: Knuth-Bendix completion, completion algorithm, reduction ordering, equational theory
fetched: 2026-07-02
---

# Equational logic

First-order **equational logic** consists of quantifier-free terms of ordinary first-order logic, with equality as the only predicate symbol. The model theory of this logic was developed into universal algebra by Birkhoff, Grätzer, and Cohn. It was later made into a branch of category theory by Lawvere ("algebraic theories").

The terms of equational logic are built up from variables and constants using function symbols (or operations).

## Syllogism

Here are the four inference rules of logic. ${\textstyle P[x:=E]}$ denotes textual substitution of expression ${\textstyle E}$ for variable ${\textstyle x}$ in expression ${\textstyle P}$ . Next, ${\textstyle b=c}$ denotes equality, for ${\textstyle b}$ and ${\textstyle c}$ of the same type, while ${\textstyle b\equiv c}$ , or equivalence, is defined only for ${\textstyle b}$ and ${\textstyle c}$ of type boolean. For ${\textstyle b}$ and ${\textstyle c}$ of type boolean, ${\textstyle b=c}$ and ${\textstyle b\equiv c}$ have the same meaning.

| Substitution | If ${\textstyle P}$ is a theorem, then so is ${\textstyle P[x:=E]}$ . | $\vdash P\qquad \rightarrow \qquad \vdash P[x:=E]$ |
|---|---|---|
| Leibniz | If ${\textstyle P=Q}$ is a theorem, then so is ${\textstyle E[x:=P]=E[x:=Q]}$ . | $\vdash P=Q\qquad \rightarrow \qquad \vdash E[x:=P]=E[x:=Q]$ |
| Transitivity | If ${\textstyle P=Q}$ and ${\textstyle Q=R}$ are theorems, then so is ${\textstyle P=R}$ . | $\vdash P=Q,\;\vdash Q=R\qquad \rightarrow \qquad \vdash P=R$ |
| Equanimity | If ${\textstyle P}$ and ${\textstyle P\equiv Q}$ are theorems, then so is ${\textstyle Q}$ . | $\vdash P,\;\vdash P\equiv Q\qquad \rightarrow \qquad \vdash Q$ |

## Proof

We explain how the four inference rules are used in proofs, using the proof of ${\textstyle \lnot p\equiv p\equiv \bot }$ . The logic symbols ${\textstyle \top }$ and ${\textstyle \bot }$ indicate "true" and "false," respectively, and ${\textstyle \lnot }$ indicates "not." The theorem numbers refer to theorems of *A Logical Approach to Discrete Math*.

${\begin{array}{lcl}(0)&&\lnot p\equiv p\equiv \bot \\(1)&=&\quad \left\langle \;(3.9),\;\lnot (p\equiv q)\equiv \lnot p\equiv q,\;{\text{with}}\ q:=p\;\right\rangle \\(2)&&\lnot (p\equiv p)\equiv \bot \\(3)&=&\quad \left\langle \;{\text{Identity of}}\ \equiv (3.9),\;{\text{with}}\ q:=p\;\right\rangle \\(4)&&\lnot \top \equiv \bot &(3.8)\end{array}}$

First, lines ${\textstyle (0)}$ – ${\textstyle (2)}$ show a use of inference rule Leibniz:

$(0)=(2)$

is the conclusion of Leibniz, and its premise ${\textstyle \lnot (p\equiv p)\equiv \lnot p\equiv p}$ is given on line ${\textstyle (1)}$ . In the same way, the equality on lines ${\textstyle (2)}$ – ${\textstyle (4)}$ are substantiated using Leibniz.

The "hint" on line ${\textstyle (1)}$ is supposed to give a premise of Leibniz, showing what substitution of equals for equals is being used. This premise is theorem ${\textstyle (3.9)}$ with the substitution ${\textstyle p:=q}$ , i.e.

$(\lnot (p\equiv q)\equiv \lnot p\equiv q)[p:=q]$

This shows how inference rule Substitution is used within hints.

From ${\textstyle (0)=(2)}$ and ${\textstyle (2)=(4)}$ , we conclude by inference rule Transitivity that ${\textstyle (0)=(4)}$ . This shows how Transitivity is used.

Finally, note that line ${\textstyle (4)}$ , ${\textstyle \lnot \top \equiv \bot }$ , is a theorem, as indicated by the hint to its right. Hence, by inference rule Equanimity, we conclude that line ${\textstyle (0)}$ is also a theorem. And ${\textstyle (0)}$ is what we wanted to prove.
