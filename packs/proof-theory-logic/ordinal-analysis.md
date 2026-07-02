---
title: "Ordinal analysis"
source: https://en.wikipedia.org/wiki/Ordinal_analysis
domain: proof-theory-logic
license: CC-BY-SA-4.0
tags: proof theory, sequent calculus, natural deduction, cut-elimination theorem
fetched: 2026-07-02
---

# Ordinal analysis

In proof theory, **ordinal analysis** assigns ordinals (often large countable ordinals) to mathematical theories as a measure of their strength. If theories have the same proof-theoretic ordinal they are often equiconsistent, and if one theory has a larger proof-theoretic ordinal than another it can often prove the consistency of the second theory.

In addition to obtaining the proof-theoretic ordinal of a theory, in practice ordinal analysis usually also yields various other pieces of information about the theory being analyzed, for example characterizations of the classes of provably recursive, hyperarithmetical, or $\Delta _{2}^{1}$ functions of the theory.

## History

The field of ordinal analysis was formed when Gerhard Gentzen in 1934 used cut elimination to prove, in modern terms, that the **proof-theoretic ordinal** of Peano arithmetic is ε0. See Gentzen's consistency proof.

## Definition

Ordinal analysis concerns true, effective (recursive) theories that can interpret a sufficient portion of arithmetic to make statements about ordinal notations.

The **proof-theoretic ordinal** of such a theory T is the supremum of the order types of all ordinal notations (necessarily recursive, see next section) that the theory can prove are well founded—the supremum of all ordinals $\alpha$ for which there exists a notation o in Kleene's sense such that T proves that o is an ordinal notation. Equivalently, it is the supremum of all ordinals $\alpha$ such that there exists a recursive relation R on $\omega$ (the set of natural numbers) that well-orders it with ordinal $\alpha$ and such that T proves transfinite induction of arithmetical statements for R .

### Ordinal notations

Some theories, such as subsystems of second-order arithmetic (Z2), have no conceptualization or way to make arguments about transfinite ordinals. For example, to formalize what it means for a subsystem T of Z2 to "prove $\alpha$ well-ordered", we instead construct an ordinal notation $(A,{\tilde {<}})$ with order type $\alpha$ . T can now work with various transfinite induction principles along $(A,{\tilde {<}})$ , which substitute for reasoning about set-theoretic ordinals.

However, some pathological notation systems exist that are unexpectedly difficult to work with. For example, Rathjen gives a primitive recursive notation system $(\mathbb {N} ,<_{T})$ that is well-founded if and only if PA is consistent,p. 3 despite having order type $\omega$ . Including such a notation in the ordinal analysis of PA would result in the false equality ${\mathsf {PTO(PA)}}=\omega$ .

## Upper bound

Since an ordinal notation must be recursive, the proof-theoretic ordinal of any theory is less than or equal to the Church–Kleene ordinal $\omega _{1}^{\mathrm {CK} }$ . In particular, the proof-theoretic ordinal of an inconsistent theory is equal to $\omega _{1}^{\mathrm {CK} }$ , because an inconsistent theory trivially proves that all ordinal notations are well-founded.

For any theory that's both $\Sigma _{1}^{1}$ -axiomatizable and $\Pi _{1}^{1}$ -sound, the existence of a recursive ordering that the theory fails to prove is well-ordered follows from the $\Sigma _{1}^{1}$ bounding theorem, and said provably well-founded ordinal notations are in fact well-founded by $\Pi _{1}^{1}$ -soundness. Thus the proof-theoretic ordinal of a $\Pi _{1}^{1}$ -sound theory that has a $\Sigma _{1}^{1}$ axiomatization will always be a (countable) recursive ordinal, that is, strictly less than $\omega _{1}^{\mathrm {CK} }$ .Theorem 2.21

## Examples

### Theories with proof-theoretic ordinal ω

- Q, Robinson arithmetic (although the definition of the proof-theoretic ordinal for such weak theories has to be tweaked).
- PA–, the first-order theory of the nonnegative part of a discretely ordered ring.

### Theories with proof-theoretic ordinal ω2

- RFA, rudimentary function arithmetic.
- IΔ0, arithmetic with induction on Δ0-predicates without any axiom asserting that exponentiation is total.

### Theories with proof-theoretic ordinal ω3

- EFA, elementary function arithmetic.
- IΔ0 + exp, arithmetic with induction on Δ0-predicates augmented by an axiom asserting that exponentiation is total.
- RCA* 0, a second-order form of EFA sometimes used in reverse mathematics.
- WKL* 0, a second-order form of EFA sometimes used in reverse mathematics.

Friedman's grand conjecture suggests that much "ordinary" mathematics can be proved in weak systems having this as their proof-theoretic ordinal.

### Theories with proof-theoretic ordinal ω*n* (for *n* = 2, 3, ... ω)

- IΔ0 or EFA augmented by an axiom ensuring that each element of the *n*-th level ${\mathcal {E}}^{n}$ of the Grzegorczyk hierarchy is total.

### Theories with proof-theoretic ordinal ωω

- RCA0, recursive comprehension.
- WKL0, weak Kőnig's lemma.
- PRA, primitive recursive arithmetic.
- IΣ1, arithmetic with induction on Σ1-predicates.

### Theories with proof-theoretic ordinal ε0

- PA, Peano arithmetic (shown by Gentzen using cut elimination).
- ACA0, arithmetical comprehension.

### Theories with proof-theoretic ordinal the Feferman–Schütte ordinal Γ0

- ATR0, arithmetical transfinite recursion.
- Martin-Löf type theory with arbitrarily many finite level universes.

This ordinal is sometimes considered to be the upper limit for "predicative" theories.

### Theories with proof-theoretic ordinal the Bachmann–Howard ordinal

- ID1, the first theory of inductive definitions.
- KP, Kripke–Platek set theory with the axiom of infinity.
- CZF, Aczel's constructive Zermelo–Fraenkel set theory.
- EON, a weak variant of the Feferman's explicit mathematics system T0.

The Kripke–Platek or CZF set theories are weak set theories without axioms for the full powerset given as set of all subsets. Instead, they tend to either have axioms of restricted separation and formation of new sets, or they grant existence of certain function spaces (exponentiation) instead of carving them out from bigger relations.

### Theories with larger proof-theoretic ordinals

Unsolved problem in mathematics

What is the proof-theoretic ordinal of full second-order arithmetic?

More unsolved problems in mathematics

- $\Pi _{1}^{1}{\mbox{-}}{\mathsf {CA}}_{0}$ , Π11 comprehension has a rather large proof-theoretic ordinal, which was described by Takeuti in terms of "ordinal diagrams",p. 13 and which is bounded by ψ0(Ωω) in Buchholz's notation. It is also the ordinal of IDω, the theory of finitely iterated inductive definitions. And also the ordinal of MLW, Martin-Löf type theory with indexed W-Types Setzer (2004).
- IDω, the theory of ω-iterated inductive definitions. Its proof-theoretic ordinal is equal to the Takeuti–Feferman–Buchholz ordinal.
- T0, Feferman's constructive system of explicit mathematics has a larger proof-theoretic ordinal, which is also the proof-theoretic ordinal of the KPi, Kripke–Platek set theory with iterated admissibles and $\Sigma _{2}^{1}{\mbox{-}}{\mathsf {AC}}+{\mathsf {BI}}$ .
- KPi, an extension of Kripke–Platek set theory based on a recursively inaccessible ordinal, has a very large proof-theoretic ordinal $\psi (\varepsilon _{I+1})$ described in a 1983 paper of Jäger and Pohlers, where I is the smallest inaccessible. This ordinal is also the proof-theoretic ordinal of $\Delta _{2}^{1}{\mbox{-}}{\mathsf {CA}}+{\mathsf {BI}}$ .
- KPM, an extension of Kripke–Platek set theory based on a recursively Mahlo ordinal, has a very large proof-theoretic ordinal θ, which was described by Rathjen (1990).
- TTM, an extension of Martin-Löf type theory by one Mahlo-universe, has an even larger proof-theoretic ordinal $\psi _{\Omega _{1}}(\Omega _{M+\omega })$ .
- ${\mathsf {KP}}+\Pi _{3}-Ref$ has a proof-theoretic ordinal equal to $\Psi (\varepsilon _{K+1})$ , where K refers to the first weakly compact, due to (Rathjen 1993)
- ${\mathsf {KP}}+\Pi _{\omega }-Ref$ has a proof-theoretic ordinal equal to $\Psi _{X}^{\varepsilon _{\Xi +1}}$ , where $\Xi$ refers to the first $\Pi _{0}^{2}$ -indescribable and $\mathbb {X} =(\omega ^{+};P_{0};\epsilon ,\epsilon ,0)$ , due to (Stegert 2010).
- ${\mathsf {Stability}}$ has a proof-theoretic ordinal equal to $\Psi _{\mathbb {X} }^{\varepsilon _{\Upsilon +1}}$ where $\Upsilon$ is a cardinal analogue of the least ordinal $\alpha$ which is $(\alpha +\beta )$ -stable for all $\beta <\alpha$ and $\mathbb {X} =(\omega ^{+};P_{0};\epsilon ,\epsilon ,0)$ , due to (Stegert 2010).

Most theories capable of describing the power set of the natural numbers have proof-theoretic ordinals that are so large that no explicit combinatorial description has yet been given. This includes $\Pi _{2}^{1}-CA_{0}$ , full second-order arithmetic ( $\Pi _{\infty }^{1}-CA_{0}$ ) and set theories with powersets including ZF and ZFC. The strength of intuitionistic ZF (IZF) equals that of ZF.

## Table of ordinal analyses

| Ordinal | First-order arithmetic | Second-order arithmetic | Kripke–Platek set theory | Type theory | Constructive set theory | Explicit mathematics |   |
|---|---|---|---|---|---|---|---|
| $\omega$ | ${\mathsf {Q}}$ , ${\mathsf {PA}}^{-}$ |   |   |   |   |   |   |
| $\omega ^{2}$ | ${\mathsf {RFA}}$ , ${\mathsf {I\Delta }}_{0}$ |   |   |   |   |   |   |
| $\omega ^{3}$ | ${\mathsf {EFA}}$ , ${\mathsf {I\Delta }}_{0}^{\mathsf {+}}$ , ${\mathsf {B}}\Sigma _{1}$ Theorem 4.1 | ${\mathsf {RCA}}_{0}^{*}$ , ${\mathsf {WKL}}_{0}^{*}$ |   |   |   |   |   |
| $\omega ^{n}$ [1] | ${\mathsf {EFA}}^{\mathsf {n}}$ , ${\mathsf {I\Delta }}_{0}^{\mathsf {n+}}$ |   |   |   |   |   |   |
| $\omega ^{\omega }$ | ${\mathsf {PRA}}$ , ${\mathsf {I\Sigma }}_{1}$ p. 13 | ${\mathsf {RCA}}_{0}$ p. 13, ${\mathsf {WKL}}_{0}$ p. 13 |   | ${\mathsf {CPRC}}$ |   |   |   |
| $\omega ^{\omega ^{\omega }}$ | ${\mathsf {I}}\Sigma _{2}$ p. 13 |   |   |   |   |   |   |
| $\omega ^{\omega ^{\omega ^{\omega }}}$ | ${\mathsf {I}}\Sigma _{3}$ p. 13 | ${\mathsf {RCA}}_{0}+(\Pi _{2}^{0})^{-}{\mathsf {-IND}}$ |   |   |   |   |   |
| $\omega \uparrow \uparrow (n+1)$ [2] | ${\mathsf {I}}\Sigma _{n}$ p. 13 |   |   |   |   |   |   |
| $\varepsilon _{0}$ | ${\mathsf {PA}}$ p. 13 | ${\mathsf {ACA}}_{0}$ p. 13, ${\mathsf {\Sigma }}_{1}^{1}{\mathsf {-AC}}_{0}$ p. 13, ${\text{R-}}{\widehat {\mathbf {E} {\boldsymbol {\Omega }}}}$ p. 8, ${\mathsf {RCA}}$ p. 148, ${\mathsf {WKL}}$ p. 148, ${\mathsf {\Delta }}_{1}^{1}{\mathsf {-CA}}_{0}$ | $\mathrm {KPu} ^{r}$ p. 869 |   |   | ${\mathsf {EM}}_{0}$ |   |
| $\varepsilon _{\omega }$ |   | ${\mathsf {ACA}}_{0}+{\mathsf {iRT}}$ , ${\mathsf {RCA}}_{0}+\forall Y\forall n\exists X({\textrm {TJ}}(n,X,Y))$ |   |   |   |   |   |
| $\varepsilon _{\varepsilon _{0}}$ |   | ${\mathsf {ACA}}$ p. 959 |   |   |   |   |   |
| $\zeta _{0}$ |   | ${\mathsf {ACA}}_{0}+\forall X\exists Y({\textrm {TJ}}(\omega ,X,Y))$ , ${\mathsf {p}}_{1}({\mathsf {ACA}}_{0})$ , ${\mathsf {RFN}}_{0}$ p. 17, ${\mathsf {ACA}}_{0}+({\mathsf {BR}})$ p. 5 |   |   |   |   |   |
| $\varphi (2,\varepsilon _{0})$ |   | ${\mathsf {RFN}}$ , ${\mathsf {ACA}}+\forall X\exists Y({\textrm {TJ}}(\omega ,X,Y))$ p. 52 |   |   |   |   |   |
| $\varphi (\omega ,0)$ | ${\mathsf {ID}}_{1}\#$ , ${\mathsf {TID}}_{0}$ p. 137 | ${\mathsf {\Delta }}_{1}^{1}{\mathsf {-CR}}$ , $\Sigma _{1}^{1}{\mathsf {-DC}}_{0}$ |   |   |   | ${\mathsf {EM}}_{0}{\mathsf {+JR}}$ |   |
| $\varphi (\varepsilon _{0},0)$ | ${\widehat {\mathsf {ID}}}_{1}$ , ${\mathsf {KFL}}$ p. 17, ${\mathsf {KF}}$ p. 17 | ${\mathsf {\Delta }}_{1}^{1}{\mathsf {-CA}}$ p. 140, ${\mathsf {\Sigma }}_{1}^{1}{\mathsf {-AC}}$ p. 140, ${\mathsf {\Sigma }}_{1}^{1}{\mathsf {-DC}}$ p. 140, ${\text{W-}}{\widehat {\mathbf {E} {\boldsymbol {\Omega }}}}$ p. 8 | $\mathrm {KPu} ^{r}+(\mathrm {IND} _{N})$ p. 870 | ${\mathsf {ML}}_{1}$ |   | ${\mathsf {EM}}_{0}{\mathsf {+J}}$ |   |
| $\varphi (\varepsilon _{\varepsilon _{0}},0)$ |   | ${\widehat {\mathbf {E} {\boldsymbol {\Omega }}}}$ p. 27, ${\widehat {\mathbf {EID} }}_{\boldsymbol {1}}$ p. 27 |   |   |   |   |   |
| $\varphi (\varphi (\omega ,0),0)$ | $\mathrm {PRS} \omega$ p. 9 |   |   |   |   |   |   |
| $\varphi ({\mathsf {<}}\Omega ,0)$ [3] | ${\mathsf {Aut(ID\#)}}$ |   |   |   |   |   |   |
| $\Gamma _{0}$ | ${\widehat {\mathsf {ID}}}_{<\omega }$ , ${\mathsf {U(PA)}}$ , $\mathbf {KFL} ^{*}$ p. 22, $\mathbf {KF} ^{*}$ p. 22, ${\mathcal {U}}(\mathrm {NFA} )$ , ${\mathsf {TID}}_{0}^{+}$ p. 137 | ${\mathsf {ATR}}_{0}$ , ${\mathsf {\Delta }}_{1}^{1}{\mathsf {-CA+BR}}$ , $\Delta _{1}^{1}\mathrm {-CA} _{0}+\mathrm {(SUB)}$ , $\mathrm {FP} _{0}$ p. 26 | ${\mathsf {KPi}}^{0}$ p. 878, ${\mathsf {KPu}}^{0}+(\mathrm {BR} )$ p. 878 | ${\mathsf {ML}}_{<\omega }$ , ${\mathsf {MLU}}$ |   |   |   |
| $\Gamma _{\omega ^{\omega }}$ |   |   | ${\mathsf {KPI}}^{0}+({\mathsf {\Sigma _{1}-I}}_{\omega })$ p. 13 |   |   |   |   |
| $\Gamma _{\varepsilon _{0}}$ | ${\widehat {\mathsf {ID}}}_{\omega }$ | ${\mathsf {ATR}}$ | ${\mathsf {KPI}}^{0}{\mathsf {+F-I}}_{\omega }$ |   |   |   |   |
| $\varphi (1,\omega ,0)$ | ${\widehat {\mathsf {ID}}}_{<\omega ^{\omega }}$ | ${\mathsf {ATR}}_{0}+({\mathsf {\Sigma }}_{1}^{1}{\mathsf {-DC}})$ | ${\mathsf {KPi}}^{0}{\mathsf {+\Sigma _{1}-I}}_{\omega }$ |   |   |   |   |
| $\varphi (1,\varepsilon _{0},0)$ | ${\widehat {\mathsf {ID}}}_{<\varepsilon _{0}}$ | ${\mathsf {ATR}}+({\mathsf {\Sigma }}_{1}^{1}{\mathsf {-DC}})$ | ${\mathsf {KPi}}^{0}{\mathsf {+F-I}}_{\omega }$ |   |   |   |   |
| $\varphi (1,\Gamma _{0},0)$ | ${\widehat {\mathsf {ID}}}_{<\Gamma _{0}}$ |   |   | ${\mathsf {MLS}}$ |   |   |   |
| $\varphi (2,0,0)$ | ${\mathsf {Aut({\widehat {ID}})}}$ , ${\mathsf {FTR}}_{0}$ | $Ax_{\Sigma _{1}^{1}{\mathsf {-AC}}}{\mathsf {TR}}_{0}$ p. 1167, $Ax_{{\mathsf {ATR}}+\Sigma _{1}^{1}{\mathsf {-DC}}}{\mathsf {RFN}}_{0}$ p. 1167 | ${\mathsf {KPh}}^{0}$ | ${\mathsf {Aut(ML)}}$ |   |   |   |
| $\varphi (2,0,\varepsilon _{0})$ | ${\mathsf {FTR}}$ | $Ax_{\Sigma _{1}^{1}{\mathsf {-AC}}}{\mathsf {TR}}$ p. 1167, $Ax_{{\mathsf {ATR}}+\Sigma _{1}^{1}{\mathsf {-DC}}}{\mathsf {RFN}}$ p. 1167 |   |   |   |   |   |
| $\varphi (2,\varepsilon _{0},0)$ |   |   | ${\mathsf {KPh}}_{0}+({\mathsf {F-I}}_{\omega })$ |   |   |   |   |
| $\varphi (\omega ,0,0)$ |   | $(\Pi _{2}^{1}{\mathsf {-RFN}})_{0}^{\Sigma _{1}^{1}{\mathsf {-DC}}}$ p. 233, $\Sigma _{1}^{1}{\mathsf {-TDC}}_{0}$ p. 233 | ${\mathsf {KPm}}^{0}$ p. 276 | ${\mathsf {EMA}}$ p. 276 |   |   |   |
| $\varphi (\varepsilon _{0},0,0)$ |   | $(\Pi _{2}^{1}{\mathsf {-RFN}})^{\Sigma _{1}^{1}{\mathsf {-DC}}}$ p. 233, $\Sigma _{1}^{1}{\mathsf {-TDC}}$ | ${\mathsf {KPm}}^{0}+({\mathcal {L}}^{*}{\mathsf {-I}}_{\mathsf {N}})$ p. 277 | ${\mathsf {EMA}}+(\mathbb {L} {\mathsf {-I}}_{\mathsf {N}})$ p. 277 |   |   |   |
| $\varphi (1,0,0,0)$ |   | ${\mathsf {p}}_{1}(\Sigma _{1}^{1}{\mathsf {-TDC}}_{0})$ |   |   |   |   |   |
| $\psi _{\Omega _{1}}(\Omega ^{\Omega ^{\omega }})$ |   | ${\mathsf {RCA}}_{0}^{*}+\Pi _{1}^{1}{\mathsf {-CA}}^{-}$ , ${\mathsf {p}}_{3}({\mathsf {ACA}}_{0})$ |   |   |   |   |   |
| $\vartheta (\Omega ^{\Omega })$ | ${\mathsf {TID}}$ , ${\mathsf {TID}}_{1}$ p. 171 | ${\mathsf {p}}_{1}({\mathsf {p}}_{3}({\mathsf {ACA}}_{0}))$ |   | ${\mathsf {FIT}}$ p. 171 |   |   |   |
| $\psi _{0}(\varepsilon _{\Omega +1})$ [4] | ${\mathsf {ID}}_{1}$ | ${\text{W-}}{\widetilde {\mathbf {E} {\boldsymbol {\Omega }}}}$ p. 8 | ${\mathsf {KP}}$ , ${\mathsf {KP\omega }}$ , $\mathrm {KPu}$ p. 869 | ${\mathsf {ML}}_{1}{\mathsf {V}}$ | ${\mathsf {CZF}}$ | ${\mathsf {EON}}$ |   |
| $\psi (\varepsilon _{\Omega +\varepsilon _{0}})$ |   | ${\widetilde {\mathbf {E} {\boldsymbol {\Omega }}}}$ p. 31, ${\widetilde {\mathbf {EID} }}_{\boldsymbol {1}}$ p. 31, $\mathbf {ACA} +(\Pi _{1}^{1}{\text{-CA}})^{-}$ p. 31 |   |   |   |   |   |
| $\psi (\varepsilon _{\Omega +\Omega })$ |   | $({\mathsf {ID}}_{1}^{2})_{0}+{\mathsf {BR}}$ |   |   |   |   |   |
| $\psi (\varepsilon _{\varepsilon _{\Omega +1}})$ |   | $\mathbf {E} {\boldsymbol {\Omega }}$ p. 33, $\mathbf {EID} _{\boldsymbol {1}}$ p. 33, $\mathbf {ACA} +(\Pi _{1}^{1}{\text{-CA}})^{-}+(\mathrm {BI} _{\mathrm {PR} })^{-}$ p. 33 |   |   |   |   |   |
| $\psi _{0}(\Gamma _{\Omega +1})$ [5] | ${\mathsf {U(ID}}_{1}{\mathsf {)}}$ , ${\widehat {\mathsf {ID}}}_{<\omega }^{\bullet }$ p. 26, $\Sigma _{1}^{1}{\mathsf {-DC}}_{0}^{\bullet }+({\mathsf {SUB}}^{\bullet })$ p. 26, ${\mathsf {ATR}}_{0}^{\bullet }$ p. 26, $\Sigma _{1}^{1}{\mathsf {-AC}}_{0}^{\bullet }+({\mathsf {SUB}}^{\bullet })$ p. 26, ${\mathcal {U}}({\mathsf {ID}}_{1})$ p. 26 | ${\mathsf {FP}}_{0}^{\bullet }$ p. 26, ${\mathsf {ATR}}_{0}^{\bullet }$ p. 26 |   |   |   |   |   |
| $\psi _{0}(\varphi ({\mathsf {<}}\Omega ,0,\Omega +1))$ | ${\mathsf {Aut(U(ID))}}$ |   |   |   |   |   |   |
| $\psi _{0}(\Omega _{\omega })$ | ${\mathsf {ID}}_{<\omega }$ p. 28 | ${\mathsf {\Pi }}_{1}^{1}{\mathsf {-CA}}_{0}$ p. 28, ${\mathsf {\Delta }}_{2}^{1}{\mathsf {-CA}}_{0}$ |   | ${\mathsf {MLW}}$ |   | ${\mathsf {SUS}}+({\mathsf {S}}-{\mathsf {I}}_{\mathsf {N}})$ p. 27 |   |
| $\psi _{0}(\Omega _{\omega }\omega ^{\omega })$ |   | $\Pi _{1}^{1}{\mathsf {-CA}}_{0}+\Pi _{2}^{1}{\mathsf {-IND}}$ |   |   |   |   |   |
| $\psi _{0}(\Omega _{\omega }\varepsilon _{0})$ | ${\mathsf {W-ID}}_{\omega }$ | ${\mathsf {\Pi }}_{1}^{1}{\mathsf {-CA}}$ p. 14 | ${\mathsf {W-KPI}}$ |   |   |   |   |
| $\psi _{0}(\Omega _{\omega }\Omega )$ |   | $\Pi _{1}^{1}{\mathsf {-CA+BR}}$ |   |   |   |   |   |
| $\psi _{0}(\Omega _{\omega }^{\omega })$ |   | $\Pi _{1}^{1}{\mathsf {-CA}}_{0}+\Pi _{2}^{1}{\mathsf {-BI}}$ |   |   |   |   |   |
| $\psi _{0}(\Omega _{\omega }^{\omega ^{\omega }})$ |   | $\Pi _{1}^{1}{\mathsf {-CA}}_{0}+\Pi _{2}^{1}{\mathsf {-BI}}+\Pi _{3}^{1}{\mathsf {-IND}}$ |   |   |   |   |   |
| $\psi _{0}(\varepsilon _{\Omega _{\omega }+1})$ [6] | ${\mathsf {ID}}_{\omega }$ | ${\mathsf {\Pi }}_{1}^{1}{\mathsf {-CA+BI}}$ | ${\mathsf {KPI}}$ |   |   |   |   |
| $\psi _{0}(\Omega _{\omega ^{\omega }})$ | ${\mathsf {ID}}_{<\omega ^{\omega }}$ | ${\mathsf {\Delta }}_{2}^{1}{\mathsf {-CR}}$ p. 28 |   |   |   | ${\mathsf {SUS}}+({\mathsf {N}}-{\mathsf {I}}_{\mathsf {N}})$ p. 27 |   |
| $\psi _{0}(\Omega _{\varepsilon _{0}})$ | ${\mathsf {ID}}_{<\varepsilon _{0}}$ | ${\mathsf {\Delta }}_{2}^{1}{\mathsf {-CA}}$ p. 28, ${\mathsf {\Sigma }}_{2}^{1}{\mathsf {-AC}}$ | ${\mathsf {W-KPi}}$ |   |   | ${\mathsf {SUS}}+(\mathrm {L} -{\mathsf {I}}_{\mathsf {N}})$ p. 27 |   |
| $\psi _{0}(\Omega _{\Omega })$ | ${\mathsf {Aut(ID)}}$ [7] |   |   |   |   |   |   |
| $\psi _{\Omega _{1}}(\varepsilon _{\Omega _{\Omega }+1})$ | ${\mathsf {ID}}_{\prec ^{*}}$ , ${\mathsf {BID}}^{2*}$ , ${\mathsf {ID}}^{2*}+{\mathsf {BI}}$ |   | ${\mathsf {KPl}}^{*}$ , ${\mathsf {KPl}}_{\Omega }^{r}$ |   |   |   |   |
| $\psi _{0}(\Phi _{1}(0))$ |   | $\Pi _{1}^{1}{\mathsf {-TR}}_{0}$ , $\Pi _{1}^{1}{\mathsf {-TR}}_{0}+\Delta _{2}^{1}{\mathsf {-CA}}_{0}$ , $\Delta _{2}^{1}{\mathsf {-CA+BI(impl-}}\Sigma _{2}^{1})$ , $\Delta _{2}^{1}{\mathsf {-CA+BR(impl-}}\Sigma _{2}^{1})$ , $\mathbf {AUT-ID} _{0}^{pos}$ , $\mathbf {AUT-ID} _{0}^{mon}$ | ${\mathsf {KPi}}^{w}+{\mathsf {FOUNDR}}({\mathsf {impl-}})\Sigma )$ , ${\mathsf {KPi}}^{w}+{\mathsf {FOUND}}({\mathsf {impl-}})\Sigma )$ , $\mathbf {AUT-KPl} ^{r}$ , $\mathbf {AUT-KPl} ^{r}+\mathbf {KPi} ^{r}$ |   |   |   |   |
| $\psi _{0}(\Phi _{1}(0)\varepsilon _{0})$ |   | $\Pi _{1}^{1}{\mathsf {-TR}}$ , $\mathbf {AUT-ID} ^{pos}$ , $\mathbf {AUT-ID} ^{mon}$ | $\mathbf {AUT-KPl} ^{w}$ |   |   |   |   |
| $\psi _{0}(\varepsilon _{\Phi _{1}(0)+1})$ |   | $\Pi _{1}^{1}{\mathsf {-TR}}+({\mathsf {BI}})$ , $\mathbf {AUT-ID} _{2}^{pos}$ , $\mathbf {AUT-ID} _{2}^{mon}$ | $\mathbf {AUT-KPl}$ |   |   |   |   |
| $\psi _{0}(\Phi _{1}(\varepsilon _{0}))$ |   | $\Pi _{1}^{1}{\mathsf {-TR}}+\Delta _{2}^{1}{\mathsf {-CA}}$ , $\Pi _{1}^{1}{\mathsf {-TR}}+\Sigma _{2}^{1}{\mathsf {-AC}}$ | $\mathbf {AUT-KPl} ^{w}+\mathbf {KPi} ^{w}$ |   |   |   |   |
| $\psi _{0}(\Phi _{\omega }(0))$ |   | $\Delta _{2}^{1}{\mathsf {-TR}}_{0}$ , $\Sigma _{2}^{1}{\mathsf {-TRDC}}_{0}$ , $\Delta _{2}^{1}{\mathsf {-CA}}_{0}+(\Sigma _{2}^{1}{\mathsf {-BI}})$ | $\mathbf {KPi} ^{r}+(\Sigma {\mathsf {-FOUND}})$ , $\mathbf {KPi} ^{r}+(\Sigma {\mathsf {-REC}})$ |   |   |   |   |
| $\psi _{0}(\Phi _{\varepsilon _{0}}(0))$ |   | $\Delta _{2}^{1}{\mathsf {-TR}}$ , $\Sigma _{2}^{1}{\mathsf {-TRDC}}$ , $\Delta _{2}^{1}{\mathsf {-CA}}+(\Sigma _{2}^{1}{\mathsf {-BI}})$ | $\mathbf {KPi} ^{w}+(\Sigma {\mathsf {-FOUND}})$ , $\mathbf {KPi} ^{w}+(\Sigma {\mathsf {-REC}})$ |   |   |   |   |
| $\psi (\varepsilon _{I+1})$ [8] |   | ${\mathsf {\Delta }}_{2}^{1}{\mathsf {-CA+BI}}$ p. 28, ${\mathsf {\Sigma }}_{2}^{1}{\mathsf {-AC+BI}}$ | ${\mathsf {KPi}}$ |   | ${\mathsf {CZF+REA}}$ | ${\mathsf {T}}_{0}$ |   |
| $\psi (\Omega _{I+\omega })$ |   |   |   | ${\mathsf {ML}}_{1}{\mathsf {W}}$ |   |   |   |
| $\psi (\Omega _{L})$ [9] |   |   | ${\mathsf {KPh}}$ | ${\mathsf {ML}}_{<\omega }{\mathsf {W}}$ |   |   |   |
| $\psi (\Omega _{L^{*}})$ [10] |   |   |   | ${\mathsf {Aut(MLW)}}$ |   |   |   |
| $\psi _{\Omega }(\chi _{\varepsilon _{M+1}}(0))$ [11] |   | ${\mathsf {\Delta }}_{2}^{1}{\mathsf {-CA+BI+(M)}}$ | ${\mathsf {KPM}}$ |   | ${\mathsf {CZFM}}$ |   |   |
| $\psi (\Omega _{M+\omega })$ [12] |   |   | ${\mathsf {KPM}}^{+}$ | ${\mathsf {TTM}}$ |   |   |   |
| $\Psi _{\Omega }^{0}(\varepsilon _{K+1})$ [13] |   |   | ${\mathsf {KP+\Pi }}_{3}-{\mathsf {Ref}}$ |   |   |   |   |
| $\Psi _{(\omega ^{+};P_{0},\epsilon ,\epsilon ,0)}^{\varepsilon _{\Xi +1}}$ [14] |   |   | ${\mathsf {KP+\Pi }}_{\omega }-{\mathsf {Ref}}$ |   |   |   |   |
| $\Psi _{(\omega ^{+};P_{0},\epsilon ,\epsilon ,0)}^{\varepsilon _{\Upsilon +1}}$ [15] |   |   | ${\mathsf {Stability}}$ |   |   |   |   |
| $\psi _{\omega _{1}^{CK}}(\varepsilon _{\mathbb {S} ^{+}+1})$ |   |   | ${\mathsf {KP}}\omega +\Pi _{1}^{1}-{\mathsf {Ref}}$ , ${\mathsf {KP}}\omega +(M\prec _{\Sigma _{1}}V)$ |   |   |   |   |
| $\psi _{\omega _{1}^{CK}}(\varepsilon _{\mathbb {I} +1})$ |   | $\Sigma _{3}^{1}{\mathsf {-DC+BI}}$ , $\Sigma _{3}^{1}{\mathsf {-AC+BI}}$ | ${\mathsf {KP}}\omega +\Pi _{1}-{\mathsf {Collection}}+(V=L)$ |   |   |   |   |
| $\psi _{\omega _{1}^{CK}}(\varepsilon _{\mathbb {I} _{N}+1})$ |   | $\Sigma _{N+2}^{1}{\mathsf {-DC+BI}}$ , $\Sigma _{N+2}^{1}{\mathsf {-AC+BI}}$ | ${\mathsf {KP}}\omega +\Pi _{N}-{\mathsf {Collection}}+(V=L)$ |   |   |   |   |
| $\psi _{\omega _{1}^{CK}}(\mathbb {I} _{\omega })$ | ${\mathsf {PA}}+\bigcup \limits _{N<\omega }{\mathsf {TI}}[\Pi _{0}^{1-},\psi _{\omega _{1}^{CK}}(\varepsilon _{\mathbb {I} _{N}+1})]$ | $\mathbf {Z} _{2}$ , $\Pi _{\infty }^{1}-{\mathsf {CA}}$ , Bar | ${\mathsf {KP}}+\Pi _{\omega }^{\text{set}}-{\mathsf {Separation}}$ | $\lambda 2$ | ${\mathsf {CZF+Sep}}$ |   |   |

### Key

This is a list of symbols used in this table:

- ψ represents various ordinal collapsing functions as defined in their respective citations.
- Ψ represents either Rathjen's or Stegert's Psi.
- φ represents Veblen's function.
- ω represents the first transfinite ordinal.
- εα represents the epsilon numbers.
- Γα represents the gamma numbers (Γ0 is the Feferman–Schütte ordinal)
- Ωα represent the uncountable ordinals (Ω1, abbreviated Ω, is ω1). Countability is considered necessary for an ordinal to be regarded as proof theoretic.
- $\mathbb {S}$ is an ordinal term denoting a stable ordinal, and $\mathbb {S} ^{+}$ the least admissible ordinal above $\mathbb {S}$ .
- $\mathbb {I} _{N}$ is an ordinal term denoting an ordinal such that $L_{\mathbb {I} _{N}}\models {\mathsf {KP}}\omega +\Pi _{N}-{\mathsf {Collection}}+(V=L)$ ; N is a variable that defines a series of ordinal analyses of the results of $\Pi _{N}-{\mathsf {Collection}}$ forall $1\leq N<\omega$ . when N=1, $\psi _{\omega _{1}^{CK}}(\varepsilon _{\mathbb {I} _{1}+1})=\psi _{\omega _{1}^{CK}}(\varepsilon _{\mathbb {I} +1})$
- Additional symbols can be found in the notes.

This is a list of the abbreviations used in this table:

- First-order arithmetic
  - ${\mathsf {Q}}$ is Robinson arithmetic
  - ${\mathsf {PA}}^{-}$ is the first-order theory of the nonnegative part of a discretely ordered ring.
  - ${\mathsf {RFA}}$ is rudimentary function arithmetic.
  - ${\mathsf {I\Delta }}_{0}$ is arithmetic with induction restricted to Δ0-predicates without any axiom asserting that exponentiation is total.
  - ${\mathsf {EFA}}$ is elementary function arithmetic.
  - ${\mathsf {I\Delta }}_{0}^{\mathsf {+}}$ is arithmetic with induction restricted to Δ0-predicates augmented by an axiom asserting that exponentiation is total.
  - ${\mathsf {EFA}}^{\mathsf {n}}$ is elementary function arithmetic augmented by an axiom ensuring that each element of the *n*-th level ${\mathcal {E}}^{n}$ of the Grzegorczyk hierarchy is total.
  - ${\mathsf {I\Delta }}_{0}^{\mathsf {n+}}$ is ${\mathsf {I\Delta }}_{0}^{\mathsf {+}}$ augmented by an axiom ensuring that each element of the *n*-th level ${\mathcal {E}}^{n}$ of the Grzegorczyk hierarchy is total.
  - ${\mathsf {PRA}}$ is primitive recursive arithmetic.
  - ${\mathsf {I\Sigma }}_{1}$ is arithmetic with induction restricted to Σ1-predicates.
  - ${\mathsf {PA}}$ is Peano arithmetic.
  - ${\mathsf {ID}}_{\nu }\#$ is ${\widehat {\mathsf {ID}}}_{\nu }$ but with induction only for positive formulas.
  - ${\widehat {\mathsf {ID}}}_{\nu }$ extends PA by ν iterated fixed points of monotone operators.
  - ${\mathsf {U(PA)}}$ is not exactly a first-order arithmetic system, but captures what one can get by predicative reasoning based on the natural numbers.
  - ${\mathsf {Aut({\widehat {ID}})}}$ is autonomously iterated ${\widehat {\mathsf {ID}}}_{\nu }$ (in other words, once an ordinal is defined, it can be used to index a new series of definitions.)
  - ${\mathsf {ID}}_{\nu }$ extends PA by ν iterated **least** fixed points of monotone operators.
  - ${\mathsf {U(ID}}_{\nu }{\mathsf {)}}$ is not exactly a first-order arithmetic system, but captures what one can get by predicative reasoning based on ν-times iterated generalized inductive definitions.
  - ${\mathsf {Aut(U(ID))}}$ is autonomously iterated ${\mathsf {U(ID}}_{\nu }{\mathsf {)}}$ .
  - ${\mathsf {W-ID}}_{\nu }$ is a weakened version of ${\mathsf {ID}}_{\nu }$ based on W-types.
  - ${\mathsf {TI}}[\Pi _{0}^{1-},\alpha ]$ is a transfinite induction of length α no more than $\Pi _{0}^{1}$ -formulas. It happens to be the representation of the ordinal notation when used in first-order arithmetic.
- Second-order arithmetic

In general, a subscript 0 means that the induction scheme is restricted to a single set induction axiom.

  - ${\mathsf {RCA}}_{0}^{*}$ is a second order form of ${\mathsf {EFA}}$ sometimes used in reverse mathematics.
  - ${\mathsf {WKL}}_{0}^{*}$ is a second order form of ${\mathsf {EFA}}$ sometimes used in reverse mathematics.
  - ${\mathsf {RCA}}_{0}$ is recursive comprehension.
  - ${\mathsf {WKL}}_{0}$ is weak Kőnig's lemma.
  - ${\mathsf {ACA}}_{0}$ is arithmetical comprehension.
  - ${\mathsf {ACA}}$ is ${\mathsf {ACA}}_{0}$ plus the full second-order induction scheme.
  - ${\mathsf {TJ}}(n,X,Y)$ is the predicate "the *n*th Turing jump of *X* is *Y*".
  - ${\mathsf {ATR}}_{0}$ is arithmetical transfinite recursion.
  - ${\mathsf {ATR}}$ is ${\mathsf {ATR}}_{0}$ plus the full second-order induction scheme.
  - ${\mathsf {BI}}$ is the bar induction axiom.
  - ${\mathsf {\Delta }}_{2}^{1}{\mathsf {-CA+BI+(M)}}$ is ${\mathsf {\Delta }}_{2}^{1}{\mathsf {-CA+BI}}$ plus the assertion *"every true ${\mathsf {\Pi }}_{3}^{1}$ -sentence with parameters holds in a (countable coded) $\beta$ -model of ${\mathsf {\Delta }}_{2}^{1}{\mathsf {-CA}}$ ".*
- Kripke–Platek set theory
  - ${\mathsf {KP}}$ is Kripke–Platek set theory with the axiom of infinity.
  - ${\mathsf {KP\omega }}$ is Kripke–Platek set theory, whose universe is an admissible set containing $\omega$ .
  - ${\mathsf {W-KPI}}$ is a weakened version of ${\mathsf {KPI}}$ based on W-types.
  - ${\mathsf {KPI}}$ asserts that the universe is a limit of admissible sets.
  - ${\mathsf {W-KPi}}$ is a weakened version of ${\mathsf {KPi}}$ based on W-types.
  - ${\mathsf {KPi}}$ asserts that the universe is inaccessible sets.
  - ${\mathsf {KPh}}$ asserts that the universe is hyperinaccessible: an inaccessible set and a limit of inaccessible sets.
  - ${\mathsf {KPM}}$ asserts that the universe is a Mahlo set.
  - ${\mathsf {KP+\Pi }}_{\mathsf {n}}-{\mathsf {Ref}}$ is ${\mathsf {KP}}$ augmented by a certain first-order reflection scheme.
  - ${\mathsf {Stability}}$ is KPi augmented by the axiom $\forall \alpha \exists \kappa \geq \alpha (L_{\kappa }\preceq _{1}L_{\kappa +\alpha })$ .
  - ${\mathsf {KPM}}^{+}$ is KPI augmented by the assertion *"at least one recursively Mahlo ordinal exists".*
  - ${\mathsf {KP}}\omega +(M\prec _{\Sigma _{1}}V)$ is ${\mathsf {KP}}\omega$ with an axiom stating that 'there exists a non-empty and transitive set M such that $M\prec _{\Sigma _{1}}V$ '.

A superscript zero indicates that $\in$ -induction is removed (making the theory significantly weaker).

- Type theory
  - ${\mathsf {CPRC}}$ is the Herbelin-Patey Calculus of Primitive Recursive Constructions.
  - ${\mathsf {ML}}_{\mathsf {n}}$ is type theory without W-types and with n universes.
  - ${\mathsf {ML}}_{<\omega }$ is type theory without W-types and with finitely many universes.
  - ${\mathsf {MLU}}$ is type theory with a next universe operator.
  - ${\mathsf {MLS}}$ is type theory without W-types and with a superuniverse.
  - ${\mathsf {Aut(ML)}}$ is type theory without W-types and with autonomously iterated universes.
  - ${\mathsf {ML}}_{1}{\mathsf {V}}$ is type theory with one universe and Aczel's type of iterative sets.
  - ${\mathsf {MLW}}$ is type theory with indexed W-Types.
  - ${\mathsf {ML}}_{1}{\mathsf {W}}$ is type theory with W-types and one universe.
  - ${\mathsf {ML}}_{<\omega }{\mathsf {W}}$ is type theory with W-types and finitely many universes.
  - ${\mathsf {Aut(MLW)}}$ is type theory with W-types and with autonomously iterated universes.
  - ${\mathsf {TTM}}$ is type theory with a Mahlo universe.
  - $\lambda 2$ is System F, also polymorphic lambda calculus or second-order lambda calculus.
- Constructive set theory
  - ${\mathsf {CZF}}$ is Aczel's constructive set theory.
  - ${\mathsf {CZF+REA}}$ is ${\mathsf {CZF}}$ plus the regular extension axiom.
  - ${\mathsf {CZF+REA+FZ}}_{2}$ is ${\mathsf {CZF+REA}}$ plus the full-second order induction scheme.
  - ${\mathsf {CZFM}}$ is ${\mathsf {CZF}}$ with a Mahlo universe.
- Explicit mathematics
  - ${\mathsf {EM}}_{0}$ is basic explicit mathematics plus elementary comprehension
  - ${\mathsf {EM}}_{0}{\mathsf {+JR}}$ is ${\mathsf {EM}}_{0}$ plus join rule
  - ${\mathsf {EM}}_{0}{\mathsf {+J}}$ is ${\mathsf {EM}}_{0}$ plus join axioms
  - ${\mathsf {EON}}$ is a weak variant of the Feferman's ${\mathsf {T}}_{0}$ .
  - ${\mathsf {T}}_{0}$ is ${\mathsf {EM}}_{0}{\mathsf {+J+IG}}$ , where ${\mathsf {IG}}$ is inductive generation.
  - ${\mathsf {T}}$ is ${\mathsf {EM}}_{0}{\mathsf {+J+IG+FZ}}_{2}$ , where ${\mathsf {FZ}}_{2}$ is the full second-order induction scheme.
