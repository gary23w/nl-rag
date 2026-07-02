---
title: "Stirling numbers of the second kind"
source: https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind
domain: generating-functions
license: CC-BY-SA-4.0
tags: generating function, formal power series, catalan number, binomial coefficient
fetched: 2026-07-02
---

# Stirling numbers of the second kind

In mathematics, particularly in combinatorics, a **Stirling number of the second kind** (or **Stirling partition number**) is the number of ways to partition a set of *n* objects into *k* non-empty subsets and is denoted by $S(n,k)$ or $\textstyle \left\{{n \atop k}\right\}$ . Stirling numbers of the second kind occur in combinatorics and the study of partitions. They are named after James Stirling.

The Stirling numbers of the first and second kind can be understood as inverses of one another when viewed as triangular matrices. This article is devoted to specifics of Stirling numbers of the second kind. Identities linking the two kinds appear in the article on Stirling numbers.

## Definition

The Stirling numbers of the second kind, written $S(n,k)$ or $\lbrace \textstyle {n \atop k}\rbrace$ or with other notations, count the number of ways to partition a set of n labelled objects into k nonempty unlabelled subsets. Equivalently, they count the number of different equivalence relations with precisely k equivalence classes that can be defined on an n element set. In fact, there is a bijection between the set of partitions and the set of equivalence relations on a given set. Obviously,

$\left\{{n \atop 0}\right\}=0$

for

n

≥ 1,

$\left\{{n \atop n}\right\}=1$

for

n

≥ 0, and

$\left\{{n \atop 1}\right\}=1$

for

n

≥ 1,

as there is no empty partition of a nonempty set, the only way to partition an *n*-element set into *n* parts is to put each element of the set into its own part, and the only way to partition a nonempty set into one part is to put all of the elements in the same part. Unlike Stirling numbers of the first kind, they can be calculated using a one-sum formula:

$\left\{{n \atop k}\right\}={\frac {1}{k!}}\sum _{i=0}^{k}(-1)^{k-i}{\binom {k}{i}}i^{n}=\sum _{i=0}^{k}{\frac {(-1)^{k-i}i^{n}}{(k-i)!i!}}.$

(See also Stirling numbers and exponential generating functions in symbolic combinatorics#Stirling numbers of the second kind for a proof of the latter formula.)

The Stirling numbers of the first kind may be characterized as the numbers that arise when one expresses powers of an indeterminate *x* in terms of the falling factorials

$(x)_{n}=x(x-1)(x-2)\cdots (x-n+1).$

(In particular, (*x*)0 = 1 because it is an empty product.)

Stirling numbers of the second kind satisfy the relation

$\sum _{k=0}^{n}\left\{{n \atop k}\right\}(x)_{k}=x^{n}.$

## Notation

Various notations have been used for Stirling numbers of the second kind. The brace notation ${\textstyle \textstyle \lbrace {n \atop k}\rbrace }$ was used by Imanuel Marx and Antonio Salmeri in 1962 for variants of these numbers. This led Knuth to use it, as shown here, in the first volume of *The Art of Computer Programming* (1968). According to the third edition of *The Art of Computer Programming*, this notation was also used earlier by Jovan Karamata in 1935. The notation *S*(*n*, *k*) was used by Richard Stanley in his book *Enumerative Combinatorics* and also, much earlier, by many other writers.

The notations used on this page for Stirling numbers are not universal, and may conflict with notations in other sources.

## Relation to Bell numbers

Since the Stirling number $\left\{{n \atop k}\right\}$ counts set partitions of an *n*-element set into *k* parts, the sum

$B_{n}=\sum _{k=0}^{n}\left\{{n \atop k}\right\}$

over all values of *k* is the total number of partitions of a set with *n* members. This number is known as the *n*th Bell number.

Analogously, the ordered Bell numbers can be computed from the Stirling numbers of the second kind via

$a_{n}=\sum _{k=0}^{n}k!\left\{{n \atop k}\right\}.$

## Table of values

Below is a triangular array of values for the Stirling numbers of the second kind (sequence A048993 in the OEIS):

k

n

0

1

2

3

4

5

6

7

8

9

10

0

1

1

0

1

2

0

1

1

3

0

1

3

1

4

0

1

7

6

1

5

0

1

15

25

10

1

6

0

1

31

90

65

15

1

7

0

1

63

301

350

140

21

1

8

0

1

127

966

1701

1050

266

28

1

9

0

1

255

3025

7770

6951

2646

462

36

1

10

0

1

511

9330

34105

42525

22827

5880

750

45

1

As with the binomial coefficients, this table could be extended to *k* > *n*, but the entries would all be 0.

## Properties

### Recurrence relation

Stirling numbers of the second kind obey the recurrence relation (first discovered by Masanobu Saka in his 1782 *Sanpō-Gakkai*):

$\left\{{n+1 \atop k}\right\}=k\left\{{n \atop k}\right\}+\left\{{n \atop k-1}\right\}\quad {\mbox{for}}\;0<k<n$

with initial conditions

$\left\{{n \atop n}\right\}=1\quad {\mbox{ for}}\;n\geq 0\quad {\text{ and }}\quad \left\{{n \atop 0}\right\}=\left\{{0 \atop n}\right\}=0\quad {\text{ for }}n>0{\text{.}}$

For instance, the number 25 in column *k* = 3 and row *n* = 5 is given by 25 = 7 + (3×6), where 7 is the number above and to the left of 25, 6 is the number above 25 and 3 is the column containing the 6.

To prove this recurrence, observe that a partition of the ⁠ $n+1$ ⁠ objects into *k* nonempty subsets either contains the ⁠ $(n+1)$ ⁠-th object as a singleton or it does not. The number of ways that the singleton is one of the subsets is given by

$\left\{{n \atop k-1}\right\}$

since we must partition the remaining n objects into the available ⁠ $k-1$ ⁠ subsets. In the other case the ⁠ $(n+1)$ ⁠-th object belongs to a subset containing other objects. The number of ways is given by

$k\left\{{n \atop k}\right\}$

since we partition all objects other than the ⁠ $(n+1)$ ⁠-th into *k* subsets, and then we are left with *k* choices for inserting object ⁠ $n+1$ ⁠. Summing these two values gives the desired result.

Another recurrence relation is given by

$\left\lbrace {\begin{matrix}n\\k\end{matrix}}\right\rbrace ={\frac {k^{n}}{k!}}-\sum _{r=1}^{k-1}{\frac {\left\lbrace {\begin{matrix}n\\r\end{matrix}}\right\rbrace }{(k-r)!}}.$

which follows from evaluating $\sum _{r=0}^{n}\left\{{n \atop r}\right\}(x)_{r}=x^{n}$ at $x=k$ .

It is also conjectured that for a fixed n we have

${\begin{aligned}\left\{{n \atop k}\right\}&={\frac {1}{n-k}}\sum _{j=2}^{n-k+1}(j-2)!{\binom {-k}{j}}\left\{{n \atop k+j-1}\right\},\\\left\{{n \atop n}\right\}&=1.\end{aligned}}$

Here we start with recursively computing of $\left\{{n \atop n-1}\right\}$ , then compute $\left\{{n \atop n-2}\right\}$ and so on up to $\left\{{n \atop 1}\right\}$ .

Another conjecture is that for a fixed k we have

${\begin{aligned}\left\{{n \atop k}\right\}&={\frac {1}{n-k}}\sum _{j=2}^{n-k+1}{\binom {n}{j}}\left\{{n-j+1 \atop k}\right\}(-1)^{j},\\\left\{{n \atop n}\right\}&=1.\end{aligned}}$

If you swap $(j-2)!$ from the first sum and $(-1)^{j}$ from the second, you will get similar conjectures, but for Stirling numbers of the first kind.

### Simple identities

Some simple identities include

$\left\{{n \atop n-1}\right\}={\binom {n}{2}}.$

This is because dividing *n* elements into *n* − 1 sets necessarily means dividing it into one set of size 2 and *n* − 2 sets of size 1. Therefore we need only pick those two elements;

and

$\left\{{n \atop 2}\right\}=2^{n-1}-1.$

To see this, first note that there are 2*n* *ordered* pairs of complementary subsets *A* and *B*. In one case, *A* is empty, and in another *B* is empty, so 2*n* − 2 ordered pairs of subsets remain. Finally, since we want *unordered* pairs rather than *ordered* pairs we divide this last number by 2, giving the result above.

Another explicit expansion of the recurrence-relation gives identities in the spirit of the above example.

### Identities

The table in section 6.1 of *Concrete Mathematics* provides a plethora of generalized forms of finite sums involving the Stirling numbers. Several particular finite sums relevant to this article include

${\begin{aligned}\left\{{n+1 \atop k+1}\right\}&=\sum _{j=k}^{n}{n \choose j}\left\{{j \atop k}\right\}\\\left\{{n+1 \atop k+1}\right\}&=\sum _{j=k}^{n}(k+1)^{n-j}\left\{{j \atop k}\right\}\\\left\{{n+k+1 \atop k}\right\}&=\sum _{j=0}^{k}j\left\{{n+j \atop j}\right\}\\\left\{{n \atop \ell +m}\right\}{\binom {\ell +m}{\ell }}&=\sum _{k}\left\{{k \atop \ell }\right\}\left\{{n-k \atop m}\right\}{\binom {n}{k}}\end{aligned}}$

### Explicit formula

The Stirling numbers of the second kind are given by the explicit formula:

$\left\{{n \atop k}\right\}={\frac {1}{k!}}\sum _{j=0}^{k}(-1)^{k-j}{k \choose j}j^{n}=\sum _{j=0}^{k}{\frac {(-1)^{k-j}j^{n}}{(k-j)!j!}}.$

This can be derived by using inclusion-exclusion to count the surjections from *n* to *k* and using the fact that the number of such surjections is ${\textstyle k!\left\{{n \atop k}\right\}}$ .

Additionally, this formula is a special case of the *k*th forward difference of the monomial $x^{n}$ evaluated at *x* = 0:

$\Delta ^{k}x^{n}=\sum _{j=0}^{k}(-1)^{k-j}{k \choose j}(x+j)^{n}.$

Because the Bernoulli polynomials may be written in terms of these forward differences, one immediately obtains a relation in the Bernoulli numbers:

$B_{m}(0)=\sum _{k=0}^{m}{\frac {(-1)^{k}k!}{k+1}}\left\{{m \atop k}\right\}.$

The evaluation of incomplete exponential Bell polynomial *B**n*,*k*(*x*1,*x*2,...) on the sequence of ones equals a Stirling number of the second kind:

$\left\{{n \atop k}\right\}=B_{n,k}(1,1,\dots ,1).$

Another explicit formula given in the *NIST Handbook of Mathematical Functions* is

$\left\{{n \atop k}\right\}=\sum _{\begin{array}{c}c_{1}+\ldots +c_{k}=n-k\\c_{1},\ldots ,\ c_{k}\ \geq \ 0\end{array}}1^{c_{1}}2^{c_{2}}\cdots k^{c_{k}}$

### Parity

The parity of a Stirling number of the second kind is same as the parity of a related binomial coefficient:

$\left\{{n \atop k}\right\}\equiv {\binom {z}{w}}\ {\pmod {2}},$

where

$z=n-\left\lceil \displaystyle {\frac {k+1}{2}}\right\rceil ,\ w=\left\lfloor \displaystyle {\frac {k-1}{2}}\right\rfloor .$

This relation is specified by mapping *n* and *k* coordinates onto the Sierpiński triangle.

More directly, let two sets contain positions of 1's in binary representations of results of respective expressions:

${\begin{aligned}\mathbb {A$

One can mimic a bitwise AND operation by intersecting these two sets:

${\displaystyle {\begin{Bmatrix}n\\k\end{Bmatrix}}\,{\bmod {\,}}2={\begin{cases}0,&\mathbb {A} \cap \mathbb {B} \neq \emptyset$

to obtain the parity of a Stirling number of the second kind in *O*(1) time. In pseudocode:

${\begin{Bmatrix}n\\k\end{Bmatrix}}\,{\bmod {\,}}2:=\left[\left(\left(n-k\right)\ \And \ \left(\left(k-1\right)\,\mathrm {div} \,2\right)\right)=0\right];$

where $\left[b\right]$ is the Iverson bracket.

The parity of a central Stirling number of the second kind $\textstyle \left\{{2n \atop n}\right\}$ is odd if and only if n is a fibbinary number, a number whose binary representation has no two consecutive 1s.

### Generating functions

For a fixed integer *n*, the ordinary generating function for Stirling numbers of the second kind $\left\{{n \atop 0}\right\},\left\{{n \atop 1}\right\},\ldots$ is given by

$\sum _{k=0}^{n}\left\{{n \atop k}\right\}x^{k}=T_{n}(x),$

where $T_{n}(x)$ are Touchard polynomials. If one sums the Stirling numbers against the falling factorial instead, one can show the following identities, among others:

$\sum _{k=0}^{n}\left\{{n \atop k}\right\}(x)_{k}=x^{n}$

and

$\sum _{k=1}^{n+1}\left\{{n+1 \atop k}\right\}(x-1)_{k-1}=x^{n},$

which has special case

$\sum _{k=0}^{n}\left\{{n \atop k}\right\}(n)_{k}=n^{n}.$

For a fixed integer *k*, the Stirling numbers of the second kind have rational ordinary generating function

$\sum _{n=k}^{\infty }\left\{{n \atop k}\right\}x^{n-k}=\prod _{r=1}^{k}{\frac {1}{1-rx}}={\frac {1}{x^{k+1}(1/x)_{k+1}}}$

and have an exponential generating function given by

$\sum _{n=k}^{\infty }\left\{{n \atop k}\right\}{\frac {x^{n}}{n!}}={\frac {(e^{x}-1)^{k}}{k!}}.$

A mixed bivariate generating function for the Stirling numbers of the second kind is

$\sum _{k=0}^{\infty }\sum _{n=k}^{\infty }\left\{{n \atop k}\right\}{\frac {x^{n}}{n!}}y^{k}=e^{y(e^{x}-1)}.$

### Lower and upper bounds

If $n\geq 2$ and $1\leq k\leq n-1$ , then

${\frac {1}{2}}(k^{2}+k+2)k^{n-k-1}-1\leq \left\{{n \atop k}\right\}\leq {\frac {1}{2}}{n \choose k}k^{n-k}$

.

### Asymptotic approximation

For fixed value of $k,$ the asymptotic value of the Stirling numbers of the second kind as $n\rightarrow \infty$ is given by

$\left\{{n \atop k}\right\}{\underset {n\to \infty }{\sim }}{\frac {k^{n}}{k!}}.$

If $k=o({\sqrt {n}})$ (where *o* denotes the little o notation) then

$\left\{{n+k \atop n}\right\}{\underset {n\to \infty }{\sim }}{\frac {n^{2k}}{2^{k}k!}}.$

A uniformly valid approximation also exists: for all k such that 1 < *k* < *n*, one has

$\left\{{n \atop k}\right\}\sim {\sqrt {\frac {v-1}{v(1-G)}}}\left({\frac {v-1}{v-G}}\right)^{n-k}{\frac {k^{n}}{n^{k}}}e^{k(1-G)}\left({n \atop k}\right),$

where $v=n/k$ , and $G\in (0,1)$ is the unique solution to $G=ve^{G-v}$ . Relative error is bounded by about $0.066/n$ .

### Unimodality

For fixed n , $\left\{{n \atop k}\right\}$ is unimodal, that is, the sequence increases and then decreases. The maximum is attained for at most two consecutive values of *k*. That is, there is an integer $k_{n}$ such that

$\left\{{n \atop 1}\right\}<\left\{{n \atop 2}\right\}<\cdots <\left\{{n \atop k_{n}}\right\}\geq \left\{{n \atop k_{n}+1}\right\}>\cdots >\left\{{n \atop n}\right\}.$

Looking at the table of values above, the first few values for $k_{n}$ are $0,1,1,2,2,3,3,4,4,4,5,\ldots$

When n is large

$k_{n}{\underset {n\to \infty }{\sim }}{\frac {n}{\log n}},$

and the maximum value of the Stirling number can be approximated with

$\log \left\{{n \atop k_{n}}\right\}=n\log n-n\log \log n-n+O(n\log \log n/\log n).$

## Applications

### Moments of the Poisson distribution

If *X* is a random variable with a Poisson distribution with expected value λ, then its *n-*th moment is

$E(X^{n})=\sum _{k=0}^{n}\left\{{n \atop k}\right\}\lambda ^{k}.$

In particular, the *n*th moment of the Poisson distribution with expected value 1 is precisely the number of partitions of a set of size *n*, i.e., it is the *n*th Bell number (this fact is Dobiński's formula).

### Moments of fixed points of random permutations

Let the random variable *X* be the number of fixed points of a uniformly distributed random permutation of a finite set of size *m*. Then the *n*th moment of *X* is

$E(X^{n})=\sum _{k=0}^{m}\left\{{n \atop k}\right\}.$

**Note:** The upper bound of summation is *m*, not *n*.

In other words, the *n*th moment of this probability distribution is the number of partitions of a set of size *n* into no more than *m* parts. This is proved in the article on random permutation statistics, although the notation is a bit different.

### Rhyming schemes

The Stirling numbers of the second kind can represent the total number of rhyme schemes for a poem of *n* lines. $S(n,k)$ gives the number of possible rhyming schemes for *n* lines using *k* unique rhyming syllables. As an example, for a poem of 3 lines, there is 1 rhyme scheme using just one rhyme (aaa), 3 rhyme schemes using two rhymes (aab, aba, abb), and 1 rhyme scheme using three rhymes (abc).

## Variants

### *r*-Stirling numbers of the second kind

The *r*-Stirling number of the second kind $\left\{{n \atop k}\right\}_{r}$ counts the number of partitions of a set of *n* objects into *k* non-empty disjoint subsets, such that the first *r* elements are in distinct subsets. These numbers satisfy the recurrence relation

$\left\{{n \atop k}\right\}_{r}=k\left\{{n-1 \atop k}\right\}_{r}+\left\{{n-1 \atop k-1}\right\}_{r}$

Some combinatorial identities and a connection between these numbers and context-free grammars can be found in

### Associated Stirling numbers of the second kind

An *r*-associated Stirling number of the second kind is the number of ways to partition a set of *n* objects into *k* subsets, with each subset containing at least *r* elements. It is denoted by $S_{r}(n,k)$ and obeys the recurrence relation

$S_{r}(n+1,k)=k\ S_{r}(n,k)+{\binom {n}{r-1}}S_{r}(n-r+1,k-1)$

The 2-associated numbers (sequence A008299 in the OEIS) appear elsewhere as "Ward numbers" and as the magnitudes of the coefficients of Mahler polynomials.

### Reduced Stirling numbers of the second kind

Denote the *n* objects to partition by the integers 1, 2, ..., *n*. Define the reduced Stirling numbers of the second kind, denoted $S^{d}(n,k)$ , to be the number of ways to partition the integers 1, 2, ..., *n* into *k* nonempty subsets such that all elements in each subset have pairwise distance at least *d*. That is, for any integers *i* and *j* in a given subset, it is required that $|i-j|\geq d$ . It has been shown that these numbers satisfy

$S^{d}(n,k)=S(n-d+1,k-d+1),n\geq k\geq d$

(hence the name "reduced"). Observe (both by definition and by the reduction formula), that $S^{1}(n,k)=S(n,k)$ , the familiar Stirling numbers of the second kind.
