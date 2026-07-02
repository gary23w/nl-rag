---
title: "Sperner's theorem"
source: https://en.wikipedia.org/wiki/Sperner's_theorem
domain: extremal-combinatorics
license: CC-BY-SA-4.0
tags: extremal combinatorics, probabilistic method, dilworth's theorem, turan theorem
fetched: 2026-07-02
---

# Sperner's theorem

**Sperner's theorem**, in discrete mathematics, describes the largest possible families of finite sets none of which contain any other sets in the family. It is one of the central results in extremal set theory. It is named after Emanuel Sperner, who published it in 1928.

This result is sometimes called Sperner's lemma, but the name "Sperner's lemma" also refers to an unrelated result on coloring triangulations. To differentiate the two results, the result on the size of a Sperner family is now more commonly known as Sperner's theorem.

## Statement

A family of sets in which none of the sets is a strict subset of another is called a Sperner family, or an antichain of sets, or a clutter. For example, the family of *k*-element subsets of an *n*-element set is a Sperner family. No set in this family can contain any of the others, because a containing set has to be strictly bigger than the set it contains, and in this family all sets have equal size. The value of *k* that makes this example have as many sets as possible is *n*/2 if *n* is even, or either of the nearest integers to *n*/2 if *n* is odd. For this choice, the number of sets in the family is ${\tbinom {n}{\lfloor n/2\rfloor }}$ .

Sperner's theorem states that these examples are the largest possible Sperner families over an *n*-element set. Formally, the theorem states that,

1. for every Sperner family *S* whose union has a total of *n* elements, $|S|\leq {\binom {n}{\lfloor n/2\rfloor }},$ and
2. equality holds if and only if *S* consists of all subsets of an *n*-element set that have size $\lfloor n/2\rfloor$ or all that have size $\lceil n/2\rceil$ .

## Partial orders

Sperner's theorem can also be stated in terms of partial order width. The family of all subsets of an *n*-element set (its power set) can be partially ordered by set inclusion; in this partial order, two distinct elements are said to be incomparable when neither of them contains the other. The width of a partial order is the largest number of elements in an antichain, a set of pairwise incomparable elements. Translating this terminology into the language of sets, an antichain is just a Sperner family, and the width of the partial order is the maximum number of sets in a Sperner family. Thus, another way of stating Sperner's theorem is that the width of the inclusion order on a power set is ${\binom {n}{\lfloor n/2\rfloor }}$ .

A graded partially ordered set is said to have the Sperner property when one of its largest antichains is formed by a set of elements that all have the same rank. In this terminology, Sperner's theorem states that the partially ordered set of all subsets of a finite set, partially ordered by set inclusion, has the Sperner property.

## Proof

There are many proofs of Sperner's theorem, each leading to different generalizations (see Anderson (1987)).

The following proof is due to Lubell (1966). Let *sk* denote the number of *k*-sets in *S*. For all 0 ≤ *k* ≤ *n*,

${n \choose \lfloor {n/2}\rfloor }\geq {n \choose k}$

and, thus,

${s_{k} \over {n \choose \lfloor {n/2}\rfloor }}\leq {s_{k} \over {n \choose k}}.$

Since *S* is an antichain, we can sum over the above inequality from *k* = 0 to *n* and then apply the LYM inequality to obtain

$\sum _{k=0}^{n}{s_{k} \over {n \choose \lfloor {n/2}\rfloor }}\leq \sum _{k=0}^{n}{s_{k} \over {n \choose k}}\leq 1,$

which means

$|S|=\sum _{k=0}^{n}s_{k}\leq {n \choose \lfloor {n/2}\rfloor }.$

This completes the proof of part 1.

To have equality, all the inequalities in the preceding proof must be equalities. Since

${n \choose \lfloor {n/2}\rfloor }={n \choose k}$

if and only if $k=\lfloor {n/2}\rfloor$ or $\lceil {n/2}\rceil ,$ we conclude that equality implies that *S* consists only of sets of sizes $\lfloor {n/2}\rfloor$ or $\lceil {n/2}\rceil .$ For even *n* that concludes the proof of part 2.

For odd *n* there is more work to do, which we omit here because it is complicated. See Anderson (1987), pp. 3–4.

## Generalizations

There are several generalizations of Sperner's theorem for subsets of ${\mathcal {P}}(E),$ the poset of all subsets of *E*.

### No long chains

A **chain** is a subfamily $\{S_{0},S_{1},\dots ,S_{r}\}\subseteq {\mathcal {P}}(E)$ that is totally ordered, i.e., $S_{0}\subset S_{1}\subset \dots \subset S_{r}$ (possibly after renumbering). The chain has *r* + 1 members and **length** *r*. An *r***-chain-free family** (also called an *r***-family**) is a family of subsets of *E* that contains no chain of length *r*. Erdős (1945) proved that the largest size of an *r*-chain-free family is the sum of the *r* largest binomial coefficients ${\binom {n}{i}}$ . The case *r* = 1 is Sperner's theorem.

### *p*-compositions of a set

In the set ${\mathcal {P}}(E)^{p}$ of *p*-tuples of subsets of *E*, we say a *p*-tuple $(S_{1},\dots ,S_{p})$ is ≤ another one, $(T_{1},\dots ,T_{p}),$ if $S_{i}\subseteq T_{i}$ for each *i* = 1,2,...,*p*. We call $(S_{1},\dots ,S_{p})$ a *p***-composition of** *E* if the sets $S_{1},\dots ,S_{p}$ form a partition of *E*. Meshalkin (1963) proved that the maximum size of an antichain of *p*-compositions is the largest *p*-multinomial coefficient ${\binom {n}{n_{1}\ n_{2}\ \dots \ n_{p}}},$ that is, the coefficient in which all *n**i* are as nearly equal as possible (i.e., they differ by at most 1). Meshalkin proved this by proving a generalized LYM inequality.

The case *p* = 2 is Sperner's theorem, because then $S_{2}=E\setminus S_{1}$ and the assumptions reduce to the sets $S_{1}$ being a Sperner family.

### No long chains in *p*-compositions of a set

Beck & Zaslavsky (2002) combined the Erdös and Meshalkin theorems by adapting Meshalkin's proof of his generalized LYM inequality. They showed that the largest size of a family of *p*-compositions such that the sets in the *i*-th position of the *p*-tuples, ignoring duplications, are *r*-chain-free, for every $i=1,2,\dots ,p-1$ (but not necessarily for *i* = *p*), is not greater than the sum of the $r^{p-1}$ largest *p*-multinomial coefficients.

### Projective geometry analog

In the finite projective geometry PG(*d*, *F**q*) of dimension *d* over a finite field of order *q*, let ${\mathcal {L}}(p,F_{q})$ be the family of all subspaces. When partially ordered by set inclusion, this family is a lattice. Rota & Harper (1971) proved that the largest size of an antichain in ${\mathcal {L}}(p,F_{q})$ is the largest Gaussian coefficient ${\begin{bmatrix}d+1\\k\end{bmatrix}};$ this is the projective-geometry analog, or *q***-analog**, of Sperner's theorem.

They further proved that the largest size of an *r*-chain-free family in ${\mathcal {L}}(p,F_{q})$ is the sum of the *r* largest Gaussian coefficients. Their proof is by a projective analog of the LYM inequality.

### No long chains in *p*-compositions of a projective space

Beck & Zaslavsky (2003) obtained a Meshalkin-like generalization of the Rota–Harper theorem. In PG(*d*, *F**q*), a **Meshalkin sequence** of length *p* is a sequence $(A_{1},\ldots ,A_{p})$ of projective subspaces such that no proper subspace of PG(*d*, *F**q*) contains them all and their dimensions sum to $d-p+1$ . The theorem is that a family of Meshalkin sequences of length *p* in PG(*d*, *F**q*), such that the subspaces appearing in position *i* of the sequences contain no chain of length *r* for each $i=1,2,\dots ,p-1,$ is not more than the sum of the largest $r^{p-1}$ of the quantities

${\begin{bmatrix}d+1\\n_{1}\ n_{2}\ \dots \ n_{p}\end{bmatrix}}q^{s_{2}(n_{1},\ldots ,n_{p})},$

where ${\begin{bmatrix}d+1\\n_{1}\ n_{2}\ \dots \ n_{p}\end{bmatrix}}$ (in which we assume that $d+1=n_{1}+\cdots +n_{p}$ ) denotes the *p*-Gaussian coefficient

${\begin{bmatrix}d+1\\n_{1}\end{bmatrix}}{\begin{bmatrix}d+1-n_{1}\\n_{2}\end{bmatrix}}\cdots {\begin{bmatrix}d+1-(n_{1}+\cdots +n_{p-1})\\n_{p}\end{bmatrix}}$

and

$s_{2}(n_{1},\ldots ,n_{p}):=n_{1}n_{2}+n_{1}n_{3}+n_{2}n_{3}+n_{1}n_{4}+\cdots +n_{p-1}n_{p},$

the second elementary symmetric function of the numbers $n_{1},n_{2},\dots ,n_{p}.$
