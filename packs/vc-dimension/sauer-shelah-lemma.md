---
title: "Sauer–Shelah lemma"
source: https://en.wikipedia.org/wiki/Sauer%E2%80%93Shelah_lemma
domain: vc-dimension
license: CC-BY-SA-4.0
tags: vapnik chervonenkis dimension, shattering set, growth function, sauer shelah lemma
fetched: 2026-07-02
---

# Sauer–Shelah lemma

In combinatorial mathematics and extremal set theory, the **Sauer–Shelah lemma** states that every family of sets with small VC dimension consists of a small number of sets. Here, the VC dimension is the largest size k of a set with the property that all of its subsets can be formed by intersecting it with a member of the family. If the family has n elements in its union, then the Sauer–Shelah lemma states that its number of sets is at most proportional to $n^{k}$ .

It is named after Norbert Sauer and Saharon Shelah, who published it independently of each other in 1972. The same result was also published slightly earlier, and again independently, by Vladimir Vapnik and Alexey Chervonenkis, after whom the VC dimension is named. In his paper containing the lemma, Shelah gives credit also to Micha Perles, and for this reason the lemma has also been called the **Perles–Sauer–Shelah lemma** and the **Sauer–Shelah–Perles lemma**.

Buzaglo et al. call this lemma "one of the most fundamental results on VC-dimension", and it has applications in many areas. Sauer's motivation was in the combinatorics of set systems, while Shelah's was in model theory and that of Vapnik and Chervonenkis was in statistics. It has also been applied in discrete geometry and graph theory.

## Definitions and statement

If $\textstyle {\mathcal {F}}=\{S_{1},S_{2},\dots \}$ is a family of sets and T is a set, then T is said to be shattered by ${\mathcal {F}}$ if every subset of T (including the empty set and T itself) can be obtained as the intersection $T\cap S_{i}$ of T with some set $S_{i}$ in the family. The VC dimension of ${\mathcal {F}}$ is the largest cardinality of a set shattered by ${\mathcal {F}}$ .

In terms of these definitions, the Sauer–Shelah lemma states that if the VC dimension of ${\mathcal {F}}$ is k , and the union of ${\mathcal {F}}$ has n elements, then ${\mathcal {F}}$ can consist of at most $\sum _{i=0}^{k}{\binom {n}{i}}=O(n^{k})$ sets, as expressed using big O notation. Equivalently, if the number of sets in the family, $|{\mathcal {F}}|$ , obeys the inequality $|{\mathcal {F}}|>\sum _{i=0}^{k-1}{\binom {n}{i}},$ then there exists a set of size k that ${\mathcal {F}}$ shatters.

The bound of the lemma is tight: Let the family ${\mathcal {F}}$ be composed of all subsets of $\{1,2,\dots ,n\}$ with size less than k . Then the number of sets in ${\mathcal {F}}$ is exactly ${\textstyle \sum _{i=0}^{k-1}{\binom {n}{i}}}$ but it does not shatter any set of size k , because the set itself cannot be obtained as an intersection with a set in this family.

## The number of shattered sets

A strengthening of the Sauer–Shelah lemma, due to Pajor (1985), states that every finite set family ${\mathcal {F}}$ shatters at least $|{\mathcal {F}}|$ sets. This immediately implies the Sauer–Shelah lemma, because only ${\textstyle \sum _{i=0}^{k-1}{\tbinom {n}{i}}}$ of the subsets of an n -item universe have cardinality less than k . Thus, when $|{\mathcal {F}}|>\sum _{i=0}^{k-1}{\binom {n}{i}},$ there are not enough small sets to be shattered, so one of the shattered sets must have cardinality at least k .

For a restricted type of shattered set, called an order-shattered set, the number of shattered sets always equals the cardinality of the set family.

## Proof

Pajor's variant of the Sauer–Shelah lemma may be proved by mathematical induction; the proof has variously been credited to Noga Alon or to Ron Aharoni and Ron Holzman.

**Base**

Every family of only one set shatters the empty set.

**Step**

Assume the lemma is true for all families of size less than

$|{\mathcal {F}}|$

and let

${\mathcal {F}}$

be a family of two or more sets. Because

${\mathcal {F}}$

has at least two distinct sets, there exists an element

x

that belongs to some but not all of the sets. Split

${\mathcal {F}}$

into two subfamilies, of the sets that contain

x

and the sets that do not contain

x

. By the induction assumption, these two subfamilies shatter two collections of sets whose sizes add to at least

$|{\mathcal {F}}|$

. None of these shattered sets contain

x

, since a set that contains

x

cannot be shattered by a family in which all sets contain

x

or all sets do not contain

x

. Some of the shattered sets may be shattered by both subfamilies. When a set

S

is shattered by only one of the two subfamilies, it contributes one unit both to the number of shattered sets of the subfamily and to the number of shattered sets of

${\mathcal {F}}$

. When a set

S

is shattered by both subfamilies, both

S

and

$S\cup \{x\}$

are shattered by

${\mathcal {F}}$

, so

S

contributes two units to the number of shattered sets of the subfamilies and of

${\mathcal {F}}$

. Therefore, the number of shattered sets of

${\mathcal {F}}$

is at least equal to the number shattered by the two subfamilies of

${\mathcal {F}}$

, which is at least

$|{\mathcal {F}}|$

.

A different proof of the Sauer–Shelah lemma in its original form, by Péter Frankl and János Pach, is based on linear algebra and the inclusion–exclusion principle. This proof extends to other settings such as families of vector spaces and, more generally, geometric lattices.

## Applications

The original application of the lemma, by Vapnik and Chervonenkis, was in showing that every probability distribution can be approximated (with respect to a family of events of a given VC dimension) by a finite set of sample points whose cardinality depends only on the VC dimension of the family of events. In this context, there are two important notions of approximation, both parameterized by a number $\varepsilon$ : a set S of samples, and a probability distribution on S , is said to be an $\varepsilon$ -approximation of the original distribution if the probability of each event with respect to S differs from its original probability by at most $\varepsilon$ . A set S of (unweighted) samples is said to be an $\varepsilon$ -net if every event with probability at least $\varepsilon$ includes at least one point of S . An $\varepsilon$ -approximation must also be an $\varepsilon$ -net but not necessarily vice versa.

Vapnik and Chervonenkis used the lemma to show that set systems of VC dimension d always have $\varepsilon$ -approximations of cardinality $O({\tfrac {d}{\varepsilon ^{2}}}\log {\tfrac {d}{\varepsilon }}).$ Later authors including Haussler & Welzl (1987) and Komlós, Pach & Woeginger (1992) similarly showed that there always exist $\varepsilon$ -nets of cardinality $O({\tfrac {d}{\varepsilon }}\log {\tfrac {1}{\varepsilon }})$ , and more precisely of cardinality at most ${\tfrac {d}{\varepsilon }}\ln {\tfrac {1}{\varepsilon }}+{\tfrac {2d}{\varepsilon }}\ln \ln {\tfrac {1}{\varepsilon }}+{\tfrac {6d}{\varepsilon }}.$ The main idea of the proof of the existence of small $\varepsilon$ -nets is to choose a random sample x of cardinality ${\textstyle O({\tfrac {d}{\varepsilon }}\log {\tfrac {1}{\varepsilon }})}$ and a second independent random sample y of cardinality ${\textstyle O({\tfrac {d}{\varepsilon }}\log ^{2}{\tfrac {1}{\varepsilon }})}$ , and to bound the probability that x is missed by some large event E by the probability that x is missed and simultaneously the intersection of y with E is larger than its median value. For any particular E , the probability that x is missed while y is larger than its median is very small, and the Sauer–Shelah lemma (applied to $x\cup y$ ) shows that only a small number of distinct events E need to be considered, so by the union bound, with nonzero probability, x is an $\varepsilon$ -net.

In turn, $\varepsilon$ -nets and $\varepsilon$ -approximations, and the likelihood that a random sample of large enough cardinality has these properties, have important applications in machine learning, in the area of probably approximately correct learning. In computational geometry, they have been applied to range searching, derandomization, and approximation algorithms.

Kozma & Moran (2013) use generalizations of the Sauer–Shelah lemma to prove results in graph theory such as that the number of strong orientations of a given graph is sandwiched between its numbers of connected and 2-edge-connected subgraphs.
