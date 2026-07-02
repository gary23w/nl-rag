---
title: "Integer partition"
source: https://en.wikipedia.org/wiki/Partition_(number_theory)
domain: generating-functions
license: CC-BY-SA-4.0
tags: generating function, formal power series, catalan number, binomial coefficient
fetched: 2026-07-02
---

# Integer partition

(Redirected from

Partition (number theory)

)

In number theory and combinatorics, a **partition** of a non-negative integer n, also called an **integer partition**, is a way of writing n as a sum of positive integers. Two sums that differ only in the order of their summands are considered the same partition. (If order matters, the sum becomes a composition.) For example, 4 can be partitioned in five distinct ways:

4

3 + 1

2 + 2

2 + 1 + 1

1 + 1 + 1 + 1

The only partition of zero is the empty sum, having no parts.

The order-dependent composition 1 + 3 is the same partition as 3 + 1, and the two distinct compositions 1 + 2 + 1 and 1 + 1 + 2 represent the same partition as 2 + 1 + 1.

An individual summand in a partition is called a **part**. The number of partitions of n is given by the partition function *p*(*n*). So *p*(4) = 5. The notation *λ* ⊢ *n* means that λ is a partition of n.

Partitions can be graphically visualized with Young diagrams or Ferrers diagrams. They occur in a number of branches of mathematics and physics, including the study of symmetric polynomials and of the symmetric group and in group representation theory in general.

## Examples

The seven partitions of 5 are

- 5
- 4 + 1
- 3 + 2
- 3 + 1 + 1
- 2 + 2 + 1
- 2 + 1 + 1 + 1
- 1 + 1 + 1 + 1 + 1

Some authors treat a partition as a non-increasing sequence of summands, rather than an expression with plus signs. For example, the partition 2 + 2 + 1 might instead be written as the tuple (2, 2, 1) or in the even more compact form (22, 1) where the superscript indicates the number of repetitions of a part.

This multiplicity notation for a partition can be written alternatively as $1^{m_{1}}2^{m_{2}}3^{m_{3}}\cdots$ , where *m*1 is the number of 1's, *m*2 is the number of 2's, etc. (Components with *m**i* = 0 may be omitted.) For example, in this notation, the partitions of 5 are written $5^{1},1^{1}4^{1},2^{1}3^{1},1^{2}3^{1},1^{1}2^{2},1^{3}2^{1}$ , and $1^{5}$ .

## Diagrammatic representations of partitions

There are two common diagrammatic methods to represent partitions: as Ferrers diagrams, named after Norman Macleod Ferrers, and as Young diagrams, named after Alfred Young. Both have several possible conventions; here, we use *English notation*, with diagrams aligned in the upper-left corner.

### Ferrers diagram

The partition 6 + 4 + 3 + 1 of the number 14 can be represented by the following diagram:

(*)(*)(*)(*)(*)(*) (*)(*)(*)(*) (*)(*)(*) (*)

The 14 circles are lined up in 4 rows, each having the size of a part of the partition. The diagrams for the 5 partitions of the number 4 are shown below:

4

=

3 + 1

=

2 + 2

=

2 + 1 + 1

=

1 + 1 + 1 + 1

### Young diagram

An alternative visual representation of an integer partition is its *Young diagram* (often also called a Ferrers diagram). Rather than representing a partition with dots, as in the Ferrers diagram, the Young diagram uses boxes or squares. Thus, the Young diagram for the partition 5 + 4 + 1 is

while the Ferrers diagram for the same partition is

| (*)(*)(*)(*)(*) (*)(*)(*)(*) (*) |
|---|

While this seemingly trivial variation does not appear worthy of separate mention, Young diagrams turn out to be extremely useful in the study of symmetric functions and group representation theory: filling the boxes of Young diagrams with numbers (or sometimes more complicated objects) obeying various rules leads to a family of objects called Young tableaux, and these tableaux have combinatorial and representation-theoretic significance. As a type of shape made by adjacent squares joined together, Young diagrams are a special kind of polyomino.

## Partition function

The partition function $p(n)$ counts the partitions of a non-negative integer n . For instance, $p(4)=5$ because the integer 4 has the five partitions $1+1+1+1$ , $1+1+2$ , $1+3$ , $2+2$ , and 4 . The values of this function for $n=0,1,2,\dots$ are:

1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42, 56, 77, 101, 135, 176, 231, 297, 385, 490, 627, 792, 1002, 1255, 1575, 1958, 2436, 3010, 3718, 4565, 5604, ...

(sequence

A000041

in the

OEIS

)

.

The generating function of p is

$\sum _{n=0}^{\infty }p(n)q^{n}=\prod _{j=1}^{\infty }\sum _{i=0}^{\infty }q^{ji}=\prod _{j=1}^{\infty }(1-q^{j})^{-1}.$

No closed-form expression for the partition function is known, but it has both asymptotic expansions that accurately approximate it and recurrence relations by which it can be calculated exactly. It grows as an exponential function of the square root of its argument., as follows:

$p(n)\sim {\frac {1}{4n{\sqrt {3}}}}\exp \left({\pi {\sqrt {\frac {2n}{3}}}}\right)$

as

$n\to \infty$

In 1937, Hans Rademacher found a way to represent the partition function $p(n)$ by the convergent series

$p(n)={\frac {1}{\pi {\sqrt {2}}}}\sum _{k=1}^{\infty }A_{k}(n){\sqrt {k}}\cdot {\frac {d}{dn}}\left({{\frac {1}{\sqrt {n-{\frac {1}{24}}}}}\sinh \left[{{\frac {\pi }{k}}{\sqrt {{\frac {2}{3}}\left(n-{\frac {1}{24}}\right)}}}\,\,\,\right]}\right)$ where

$A_{k}(n)=\sum _{0\leq m<k,\;(m,k)=1}e^{\pi i\left(s(m,k)-2nm/k\right)}.$ and $s(m,k)$ is the Dedekind sum.

The multiplicative inverse of its generating function is the Euler function; by Euler's pentagonal number theorem this function is an alternating sum of pentagonal number powers of its argument.

$p(n)=p(n-1)+p(n-2)-p(n-5)-p(n-7)+\cdots$

Srinivasa Ramanujan discovered that the partition function has nontrivial patterns in modular arithmetic, now known as Ramanujan's congruences. For instance, whenever the decimal representation of n ends in the digit 4 or 9, the number of partitions of n will be divisible by 5.

## Restricted partitions

In both combinatorics and number theory, families of partitions subject to various restrictions are often studied. This section surveys a few such restrictions.

### Conjugate and self-conjugate partitions

If we flip the diagram of the partition 6 + 4 + 3 + 1 along its main diagonal, we obtain another partition of 14:

| (*)(*)(*)(*)(*)(*) (*)(*)(*)(*) (*)(*)(*) (*) | ↔ | (*)(*)(*)(*) (*)(*)(*) (*)(*)(*) (*)(*) (*) (*) |
|---|---|---|
| 6 + 4 + 3 + 1 | = | 4 + 3 + 3 + 2 + 1 + 1 |

By turning the rows into columns, we obtain the partition 4 + 3 + 3 + 2 + 1 + 1 of the number 14. Such partitions are said to be *conjugate* of one another. In the case of the number 4, partitions 4 and 1 + 1 + 1 + 1 are conjugate pairs, and partitions 3 + 1 and 2 + 1 + 1 are conjugate of each other. Of particular interest are partitions, such as 2 + 2, which have themselves as conjugate. Such partitions are said to be *self-conjugate*.

**Claim**: The number of self-conjugate partitions is the same as the number of partitions with distinct odd parts.

**Proof (outline)**: The crucial observation is that every odd part can be "*folded*" in the middle to form a self-conjugate diagram:

| (*)(*)(*)(*)(*) | ↔ | (*)(*)(*) (*) (*) |
|---|---|---|

One can then obtain a bijection between the set of partitions with distinct odd parts and the set of self-conjugate partitions, as illustrated by the following example:

| (o)(o)(o)(o)(o)(o)(o)(o)(o) (*)(*)(*)(*)(*)(*)(*) (x)(x)(x) | ↔ | (o)(o)(o)(o)(o) (o)(*)(*)(*)(*) (o)(*)(x)(x) (o)(*)(x) (o)(*) |
|---|---|---|
| 9 + 7 + 3 | = | 5 + 5 + 4 + 3 + 2 |
| Dist. odd |   | self-conjugate |

### Odd parts and distinct parts

Among the 22 partitions of the number 8, there are 6 that contain only *odd parts*:

- 7 + 1
- 5 + 3
- 5 + 1 + 1 + 1
- 3 + 3 + 1 + 1
- 3 + 1 + 1 + 1 + 1 + 1
- 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1

Alternatively, we could count partitions in which no number occurs more than once. Such a partition is called a *partition with distinct parts*. If we count the partitions of 8 with distinct parts, we also obtain 6:

- 8
- 7 + 1
- 6 + 2
- 5 + 3
- 5 + 2 + 1
- 4 + 3 + 1

This is a general property. For each positive number, the number of partitions with odd parts equals the number of partitions with distinct parts, denoted by *q*(*n*). This result was proved by Leonhard Euler in 1748 and later was generalized as Glaisher's theorem.

For every type of restricted partition there is a corresponding function for the number of partitions satisfying the given restriction. An important example is *q*(*n*) (partitions into distinct parts). The first few values of *q*(*n*) are (starting with *q*(0)=1):

1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 10, ...

(sequence

A000009

in the

OEIS

)

.

The generating function for *q*(*n*) is given by

$\sum _{n=0}^{\infty }q(n)x^{n}=\prod _{k=1}^{\infty }(1+x^{k})=\prod _{k=1}^{\infty }{\frac {1}{1-x^{2k-1}}}.$

The pentagonal number theorem gives a recurrence for *q*:

q

(

k

) =

a

k

+

q

(

k

−

1) +

q

(

k

−

2)

−

q

(

k

−

5)

−

q

(

k

−

7) +

q

(

k

−

12) +

q

(

k

−

15)

−

q

(

k

−

22)

−

...

where *a**k* is (−1)*m* if *k* = 3*m*2 − *m* for some integer *m* and is 0 otherwise.

### Restricted part size or number of parts

By taking conjugates, the number *p**k*(*n*) of partitions of *n* into exactly *k* parts is equal to the number of partitions of *n* in which the largest part has size *k*. The function *p**k*(*n*) satisfies the recurrence

p

k

(

n

) =

p

k

(

n

−

k

) +

p

k

−1

(

n

−

1)

with initial values *p*0(0) = 1 and *p**k*(*n*) = 0 if *n* ≤ 0 or *k* ≤ 0 and *n* and *k* are not both zero.

One recovers the function *p*(*n*) by

$p(n)=\sum _{k=0}^{n}p_{k}(n).$

One possible generating function for such partitions, taking *k* fixed and *n* variable, is

$\sum _{n\geq 0}p_{k}(n)x^{n}=x^{k}\prod _{i=1}^{k}{\frac {1}{1-x^{i}}}.$

More generally, if *T* is a set of positive integers then the number of partitions of *n*, all of whose parts belong to *T*, has generating function

$\prod _{t\in T}(1-x^{t})^{-1}.$

This can be used to solve change-making problems (where the set *T* specifies the available coins). As two particular cases, one has that the number of partitions of *n* in which all parts are 1 or 2 (or, equivalently, the number of partitions of *n* into 1 or 2 parts) is

$\left\lfloor {\frac {n}{2}}+1\right\rfloor ,$

and the number of partitions of *n* in which all parts are 1, 2 or 3 (or, equivalently, the number of partitions of *n* into at most three parts) is the nearest integer to (*n* + 3)2 / 12.

### Partitions in a rectangle and Gaussian binomial coefficients

One may also simultaneously limit the number and size of the parts. Let *p*(*N*, *M*; *n*) denote the number of partitions of n with at most M parts, each of size at most N. Equivalently, these are the partitions whose Young diagram fits inside an *M* × *N* rectangle. There is a recurrence relation $p(N,M;n)=p(N,M-1;n)+p(N-1,M;n-M)$ obtained by observing that $p(N,M;n)-p(N,M-1;n)$ counts the partitions of n into exactly M parts of size at most N, and subtracting 1 from each part of such a partition yields a partition of *n* − *M* into at most M parts.

The Gaussian binomial coefficient is defined as: ${k+\ell \choose \ell }_{q}={k+\ell \choose k}_{q}={\frac {\prod _{j=1}^{k+\ell }(1-q^{j})}{\prod _{j=1}^{k}(1-q^{j})\prod _{j=1}^{\ell }(1-q^{j})}}.$ The Gaussian binomial coefficient is related to the generating function of *p*(*N*, *M*; *n*) by the equality $\sum _{n=0}^{MN}p(N,M;n)q^{n}={M+N \choose M}_{q}.$

## Rank and Durfee square

The *rank* of a partition is the largest number *k* such that the partition contains at least *k* parts of size at least *k*. For example, the partition 4 + 3 + 3 + 2 + 1 + 1 has rank 3 because it contains 3 parts that are ≥ 3, but does not contain 4 parts that are ≥ 4. In the Ferrers diagram or Young diagram of a partition of rank *r*, the *r* × *r* square of entries in the upper-left is known as the Durfee square:

| (*)(*)(*)(*) (*)(*)(*) (*)(*)(*) (*)(*) (*) (*) |
|---|

The Durfee square has applications within combinatorics in the proofs of various partition identities. It also has some practical significance in the form of the h-index.

A different statistic is also sometimes called the rank of a partition (or Dyson rank), namely, the difference $\lambda _{k}-k$ for a partition of *k* parts with largest part $\lambda _{k}$ . This statistic (which is unrelated to the one described above) appears in the study of Ramanujan congruences.

## Young's lattice

There is a natural partial order on partitions given by inclusion of Young diagrams. This partially ordered set is known as *Young's lattice*. The lattice was originally defined in the context of representation theory, where it is used to describe the irreducible representations of symmetric groups *S**n* for all *n*, together with their branching properties, in characteristic zero. It also has received significant study for its purely combinatorial properties; notably, it is the motivating example of a differential poset.

## Random partitions

There is a deep theory of random partitions chosen according to the uniform probability distribution on the symmetric group via the Robinson–Schensted correspondence. In 1977, Logan and Shepp, as well as Vershik and Kerov, showed that the Young diagram of a typical large partition becomes asymptotically close to the graph of a certain analytic function minimizing a certain functional. In 1988, Baik, Deift and Johansson extended these results to determine the distribution of the longest increasing subsequence of a random permutation in terms of the Tracy–Widom distribution. Okounkov related these results to the combinatorics of Riemann surfaces and representation theory.
