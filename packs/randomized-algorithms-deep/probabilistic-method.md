---
title: "Probabilistic method"
source: https://en.wikipedia.org/wiki/Probabilistic_method
domain: randomized-algorithms-deep
license: CC-BY-SA-4.0
tags: randomized algorithm, monte carlo algorithm, probabilistic method, chernoff bound
fetched: 2026-07-02
---

# Probabilistic method

In mathematics, the **probabilistic method** is a nonconstructive method, primarily used in combinatorics and pioneered by Paul Erdős, for proving the existence of a prescribed kind of mathematical object. It works by showing that if one randomly chooses objects from a specified class, the probability that the result is of the prescribed kind is strictly greater than zero. Although the proof uses probability, the final conclusion is determined for certain, without any possible error.

This method has now been applied to other areas of mathematics such as number theory, linear algebra, and real analysis, as well as in computer science (e.g. randomized rounding) and information theory.

## Introduction

If every object in a collection of objects fails to have a certain property, then the probability that a random object chosen from the collection has that property is zero. Thus, by contraposition, if the probability that a random object chosen from the collection has that property is nonzero, then some object in the collection must possess the property.

Similarly, showing that the probability is (strictly) less than 1 can be used to prove the existence of an object that does *not* satisfy the prescribed properties.

Another way to use the probabilistic method is by calculating the expected value of some random variable. If it can be shown that the random variable can take on a value less than the expected value, this proves that the random variable can also take on some value greater than the expected value.

Alternatively, the probabilistic method can also be used to guarantee the existence of a desired element in a sample space with a value that is greater than or equal to the calculated expected value, since the non-existence of such element would imply every element in the sample space is less than the expected value, a contradiction.

Common tools used in the probabilistic method include Markov's inequality, the Chernoff bound, and the Lovász local lemma.

## Two examples due to Erdős

Although others before him proved theorems via the probabilistic method (for example, Szele's 1943 result that there exist tournaments containing a large number of Hamiltonian cycles), many of the most well known proofs using this method are due to Erdős. The first example below describes one such result from 1947 that gives a proof of a lower bound for the Ramsey number $R(r,r)$ .

### First example

Suppose we have a complete graph on n vertices. We wish to show (for small enough values of n ) that it is possible to color the edges of the graph in two colors (say red and blue) so that there is no complete subgraph on r vertices which is monochromatic (every edge colored the same color).

To do so, we color the graph randomly. Color each edge independently with probability $1/2$ of being red and $1/2$ of being blue. We calculate the expected number of monochromatic subgraphs on r vertices as follows:

For any set $S_{r}$ of r vertices from our graph, define the variable $X(S_{r})$ to be 1 if every edge amongst the r vertices is the same color, and 0 otherwise. Note that the number of monochromatic r -subgraphs is the sum of $X(S_{r})$ over all possible subsets $S_{r}$ . For any individual set $S_{r}^{i}$ , the expected value of $X(S_{r}^{i})$ is simply the probability that all of the $C(r,2)$ edges in $S_{r}^{i}$ are the same color:

$E[X(S_{r}^{i})]=2\cdot 2^{-{r \choose 2}}$

(the factor of 2 comes because there are two possible colors).

This holds true for any of the $C(n,r)$ possible subsets we could have chosen, i.e. i ranges from 1 to $C(n,r)$ . So we have that the sum of $E[X(S_{r}^{i})]$ over all $S_{r}^{i}$ is

$\sum _{i=1}^{C(n,r)}E[X(S_{r}^{i})]={n \choose r}2^{1-{r \choose 2}}.$

The sum of expectations is the expectation of the sum (*regardless* of whether the variables are independent), so the expectation of the sum (the expected number of all monochromatic r -subgraphs) is

$E[X(S_{r})]={n \choose r}2^{1-{r \choose 2}}.$

Consider what happens if this value is less than 1 . Since the expected number of monochromatic r -subgraphs is strictly less than 1 , there exists a coloring satisfying the condition that the number of monochromatic r -subgraphs is strictly less than 1 . The number of monochromatic r -subgraphs in this random coloring is a non-negative integer, hence it must be 0 ( 0 is the only non-negative integer less than 1 ). It follows that if

$E[X(S_{r})]={n \choose r}2^{1-{r \choose 2}}<1$

(which holds, for example, for $n=5$ and $r=4$ ), there must exist a coloring in which there are no monochromatic r -subgraphs.

By definition of the Ramsey number, this implies that $R(r,r)$ must be bigger than n . In particular, $R(r,r)$ must grow at least exponentially with r .

A weakness of this argument is that it is entirely nonconstructive. The problem of finding such a coloring has been open for more than 50 years.

### Second example

A 1959 paper of Erdős (see reference cited below) addressed the following problem in graph theory: given positive integers g and k, does there exist a graph G containing only cycles of length at least g, such that the chromatic number of G is at least k?

It can be shown that such a graph exists for any g and k, and the proof is reasonably simple. Let n be very large and consider a random graph G on n vertices, where every edge in G exists with probability *p* = *n*1/*g*−1. We show that with positive probability, G satisfies the following two properties:

Property 1.

G

contains at most

n

/2

cycles of length less than

g

.

**Proof.** Let X be the number cycles of length less than g. The number of cycles of length i in the complete graph on n vertices is

${\frac {n!}{2\cdot i\cdot (n-i)!}}\leq {\frac {n^{i}}{2}}$

and each of them is present in G with probability *pi*. Hence by Markov's inequality we have

$\Pr \left(X>{\tfrac {n}{2}}\right)\leq {\frac {2}{n}}E[X]\leq {\frac {1}{n}}\sum _{i=3}^{g-1}p^{i}n^{i}={\frac {1}{n}}\sum _{i=3}^{g-1}n^{\frac {i}{g}}\leq {\frac {g}{n}}n^{\frac {g-1}{g}}=gn^{-{\frac {1}{g}}}=o(1).$

Thus for sufficiently large

n

, property 1 holds with a probability of more than

1/2

.

Property 2.

G

contains no

independent set

of size

$\lceil {\tfrac {n}{2k}}\rceil$

.

**Proof.** Let Y be the size of the largest independent set in G. Clearly, we have

$\Pr(Y\geq y)\leq {n \choose y}(1-p)^{\frac {y(y-1)}{2}}\leq n^{y}e^{-{\frac {py(y-1)}{2}}}=e^{-{\frac {y}{2}}\cdot (py-2\ln n-p)}=o(1),$

when

$y=\left\lceil {\frac {n}{2k}}\right\rceil \!.$

Thus, for sufficiently large

n

, property 2 holds with a probability of more than

1/2

.

For sufficiently large n, the probability that a graph from the distribution has both properties is positive, as the events for these properties cannot be disjoint (if they were, their probabilities would sum up to more than 1).

Here comes the trick: since G has these two properties, we can remove at most *n*/2 vertices from G to obtain a new graph *G′* on $n'\geq n/2$ vertices that contains only cycles of length at least g. We can see that this new graph has no independent set of size $\left\lceil {\frac {n'}{k}}\right\rceil$ . *G′* can only be partitioned into at least k independent sets, and, hence, has chromatic number at least k.

This result gives a hint as to why the computation of the chromatic number of a graph is so difficult: even when there are no local reasons (such as small cycles) for a graph to require many colors the chromatic number can still be arbitrarily large.
