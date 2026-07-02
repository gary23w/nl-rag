---
title: "Rank of an elliptic curve"
source: https://en.wikipedia.org/wiki/Rank_of_an_elliptic_curve
domain: elliptic-curves-math
license: CC-BY-SA-4.0
tags: elliptic curve, mordell-weil theorem, weierstrass elliptic function, elliptic integral
fetched: 2026-07-02
---

# Rank of an elliptic curve

In mathematics, the **rank of an elliptic curve** is the rational Mordell–Weil rank of an elliptic curve E defined over the field of rational numbers or more generally a number field *K*. Mordell's theorem (generalized to arbitrary number fields by André Weil) says the group of rational points on an elliptic curve has a finite basis. This means that for any elliptic curve there is a finite subset of the rational points on the curve, from which all further rational points may be generated. If the number of rational points on a curve is infinite then some point in a finite basis must have infinite order. The number of *independent* basis points with infinite order is the rank of the curve.

In mathematical terms the set of *K*-rational points is denoted *E(K)* and Mordell's theorem can be stated as the existence of an isomorphism of abelian groups

$E(K)\cong \mathbb {Z} ^{r}\oplus E(K)_{\text{tors}},$

where $E(K)_{\text{tors}}$ is the torsion group of *E*, for which comparatively much is known, and $r\in \mathbb {Z} _{\geq 0}$ is a nonnegative integer called the **rank of E (over *K*)**.

The rank is related to several outstanding problems in number theory, most notably the Birch–Swinnerton-Dyer conjecture. There is currently no consensus among the experts on whether one should expect the ranks of elliptic curves over $\mathbb {Q}$ to be bounded or not. It has been shown that there exist curves with rank at least 29, but it is widely believed that such curves are rare. Indeed, Goldfeld and later Katz–Sarnak conjectured that in a suitable asymptotic sense (see below), the rank of elliptic curves should be 1/2 on average. An even stronger conjecture is that half of all elliptic curves should have rank 0 (meaning that the infinite part of its Mordell–Weil group is trivial) and the other half should have rank 1; all remaining ranks consist of a total of 0% of all elliptic curves over $\mathbb {Q}$ .

## Heights

In order to obtain a reasonable notion of 'average', one must be able to count elliptic curves $E/\mathbb {Q}$ somehow. This requires the introduction of a height function on the set of rational elliptic curves. To define such a function, recall that a rational elliptic curve $E/\mathbb {Q}$ can be given in terms of a Weierstrass form, that is, we can write

$E:y^{2}=x^{3}+Ax+B$

for some integers $A,B$ . Moreover, this model is unique if for any prime number p such that $p^{4}$ divides A , we have $p^{6}\nmid B$ . We can then assume that $A,B$ are integers that satisfy this property and define a height function on the set of elliptic curves $E/\mathbb {Q}$ by

$H(E)=H(E(A,B))=\max\{4|A|^{3},27B^{2}\}.$

It can then be shown that the number of elliptic curves $E/\mathbb {Q}$ with bounded height $H(E)$ is finite.

## Average rank

We denote by $r(E)$ the Mordell–Weil rank of the elliptic curve $E/\mathbb {Q}$ . With the height function $H(E)$ in hand, one can then define the "average rank" as a limit, provided that it exists:

$\lim _{X\rightarrow \infty }{\frac {\sum _{H(E(A,B))\leq X}r(E)}{\sum _{H(E(A,B))\leq X}1}}.$

It is not known whether or not this limit exists. However, by replacing the limit with the limit superior, one can obtain a well-defined quantity. Obtaining estimates for this quantity is therefore obtaining upper bounds for the size of the average rank of elliptic curves (provided that an average exists).

## Upper bounds for the average rank

In the past two decades there has been some progress made towards the task of finding upper bounds for the average rank. A. Brumer showed that, conditioned on the Birch–Swinnerton-Dyer conjecture and the Generalized Riemann hypothesis that one can obtain an upper bound of $2.3$ for the average rank. Heath-Brown showed that one can obtain an upper bound of 2 , still assuming the same two conjectures. Finally, Young showed that one can obtain a bound of $25/14$ , still assuming both conjectures.

Bhargava and Shankar showed that the average rank of elliptic curves is bounded above by $1.5$ and ${\frac {7}{6}}$ without assuming either the Birch–Swinnerton-Dyer conjecture or the Generalized Riemann Hypothesis. This is achieved by computing the average size of the 2 -Selmer and 3 -Selmer groups of elliptic curves $E/\mathbb {Q}$ respectively.

### Bhargava and Shankar's approach

Bhargava and Shankar's unconditional proof of the boundedness of the average rank of elliptic curves is obtained by using a certain exact sequence involving the Mordell-Weil group of an elliptic curve $E/\mathbb {Q}$ . Denote by $E(\mathbb {Q} )$ the Mordell-Weil group of rational points on the elliptic curve E , $\operatorname {Sel} _{p}(E)$ the p -Selmer group of E , and let Ш ${}_{E}[p]$ denote the p -part of the Tate–Shafarevich group of E . Then we have the following exact sequence

$0\rightarrow E(\mathbb {Q} )/pE(\mathbb {Q} )\rightarrow \operatorname {Sel} _{p}(E)\rightarrow$ Ш ${}_{E}[p]\rightarrow 0.$

This shows that the *rank* of $\operatorname {Sel} _{p}(E)$ , also called the p -Selmer rank of E , defined as the non-negative integer s such that $\#\operatorname {Sel} _{p}(E)=p^{s}$ , is an upper bound for the Mordell-Weil rank r of $E(\mathbb {Q} )$ . Therefore, if one can compute or obtain an upper bound on p -Selmer rank of E , then one would be able to bound the Mordell-Weil rank on average as well.

In *Binary quartic forms having bounded invariants, and the boundedness of the average rank of elliptic curves*, Bhargava and Shankar computed the 2-Selmer rank of elliptic curves on average. They did so by counting *binary quartic forms*, using a method used by Birch and Swinnerton-Dyer in their original computation of the analytic rank of elliptic curves which led to their famous conjecture.

## Conjectures on the boundedness of ranks

It is in general an open problem whether the rank of all elliptic curves over a fixed field *K* is bounded by a number ${\tilde {B}}_{K}$ or not. This problem has a long history of opinions of experts in the field about it. Park et al. give an account. A popular article can be found in Quanta magazine. For technical reasons instead of ${\tilde {B}}_{K}$ one considers $B_{K}$ the (potentially infinite) bound on ${\text{rk}}(E(K))$ of elliptic curves *E* defined over *K* that occurs for infinitely many different such *E*. We have $B_{K}\leq {\tilde {B}}_{K}$ and $(B_{K}<\infty )\Leftrightarrow ({\tilde {B}}_{K}<\infty )$ .

### Elliptic curves over number fields *K*

According to Park et al. Néron in 1950 held the existence of an absolute bound $B_{\mathbb {Q} }$ for the rank $r_{E}$ probable. Honda in 1960 conjectured for a general abelian variety *A* defined over $K=\mathbb {Q}$ , which in particular includes elliptic curves, the existence of a constant $c_{A}$ such that ${\text{rk}}(A(K))\leq c_{A}[K:\mathbb {Q} ]$ - such a bound does not translate directly to some ${\tilde {B}}_{K}$ or $B_{K}$ , but confers a favorable attitude towards such bounds.

In 1966 Cassels, 1974 Tate and 1982 Mestre expressed their disbelief in such a bound $B_{K}$ in various generality regarding *K*. This was the consensus among the leading experts up to the 2010s. However Mestre in 1982 proved unconditionally that for elliptic curves *E* over $\mathbb {Q}$ there is a bound ${\text{rk}}(E(\mathbb {Q} ))\leq O(\log(N(E)))$ in terms of the conductor of an elliptic curve $N(E)$ which itself is unbounded for varying *E*.

In 2016 Park et al. introduced a new random model drawing on analogies to the Cohen-Lenstra heuristics for class groups of number fields and the Keating-Snaith heuristics based on random matrix theory for L-functions. Their model was geared along the known results on distribution of elliptic curves in low ranks and their Tate-Shafarevich groups. It predicts a conjectural bound $B_{\mathbb {Q} }\in \{20,21\}$ . The model makes further predictions on upper bounds which are consistent with all currently known lower bounds from example families of elliptic curves in special cases (such as restrictions on the type of torsion groups).

For *K* a general number field the same model would predict the same bound, which however cannot hold. Park et al. show the existence of number fields $K_{n}$ of increasing degree $[K_{n}:\mathbb {Q} ]=2^{n}$ for every $n\in \mathbb {Z} _{\geq 0}$ such that there are infinitely many elliptic curves *E* defined over $K_{n}$ (in fact those elliptic curves have positive density) with ${\text{rk}}(E(K_{n}))\geq 2^{n}=[K_{n}:\mathbb {Q} ]$ , therefore a uniform bound for all number fields is impossible. They attribute the failure of their model in this case to the existence of elliptic curves *E* over general number fields *K* which come from base change of a proper subfield $K_{0}\subsetneq K$ , which their model does not take into account. Instead of the family ${\mathcal {E}}_{K}$ of all elliptic curves defined over *K* they suggest to consider only the family ${\mathcal {E}}_{K}^{\circ }\subset {\mathcal {E}}_{K}$ of all such elliptic curves that do not come from base change of a proper subfield. The model then predicts that the analog bound $B_{K}^{\circ }\in \{20,21\}$ should hold, however Park et al. also show the existence of a number field *K* such that $B_{K}^{\circ }\geq 68.$ While as of 2024 it cannot be ruled out that $B_{K}^{\circ }$ and even $B_{K}$ are finite for every number field *K* (Park et al. even state it is *plausible*) it is not clear which modified heuristics would predict correct values, let alone which approach would prove such bounds.

As of 2024 there is no consensus among the experts if the rank of an elliptic curve should be expected to be bounded uniformly only in terms of its base number field or not.

### Elliptic curves over other fields

Park et al. argue that their model (suitably modified) should not only apply to number fields, but to general global fields, in particular including when *K* is a function field over a finite field. They also point out that function fields *K* are known to exist with $B_{K}=\infty$ , but that $B_{K}^{\circ }<\infty$ for all such *K* cannot be ruled out.

For the question of boundedness of ranks of elliptic curves over some field *K* to make sense, one needs a Mordell-Weil-type theorem over that field that guarantees finite generation for the group *K*-rational points. This holds much more generally than only for global fields, by a result of Néron this is true for all *K* finitely generated over their prime field.

This fails for local fields such as $K\in \{\mathbb {R} ,\mathbb {C} ,\mathbb {Q} _{p},\mathbb {F} _{q}((x))\}$ , as the group of rational points is no longer finitely generated. In this case the rank will always be infinite. For local fields, the *K*-rational points have other useful structures, for $K\in \{\mathbb {R} ,\mathbb {C} \}$ one can talk about dimensions as manifolds or algebraic varieties, for $K\in \{\mathbb {Q} _{p},\mathbb {F} _{q}((x))\}$ one has an infinite filtration where the successive quotients are finite groups of a well classified structure. But for general *K* there is no universal analog in place of the rank that is an interesting object of study.

## Largest known ranks

A common conjecture is that there is no bound on the largest possible rank for an elliptic curve over $\mathbb {Q}$ . In 2006, Noam Elkies discovered an elliptic curve with a rank of at least 28. It was shown that under GRH it has exactly rank 28:

y

2

+

xy

+

y

=

x

3

−

x

2

−

20

067

762

415

575

526

585

033

208

209

338

542

750

930

230

312

178

956

502

x

+

34

481

611

795

030

556

467

032

985

690

390

720

374

855

944

359

319

180

361

266

008

296

291

939

448

732

243

429

Many other examples of (families of) elliptic curves over $\mathbb {Q}$ are known. In particular Elkies gave an infinite family of elliptic curves over $\mathbb {Q}$ each of rank at least 19.

In 2024, Elkies and Zev Klagsbrun discovered a curve with a rank of at least 29 (under the GRH, the rank is exactly 29):

y

2

+

xy

=

x

3

−

27

006

183

241

630

922

218

434

652

145

297

453

784

768

054

621

836

357

954

737

385

x

+

55

258

058

551

342

376

475

736

699

591

118

191

821

521

067

032

535

079

608

372

404

779

149

413

277

716

173

425

636

721

497

.
