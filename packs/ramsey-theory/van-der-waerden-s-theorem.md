---
title: "Van der Waerden's theorem"
source: https://en.wikipedia.org/wiki/Van_der_Waerden's_theorem
domain: ramsey-theory
license: CC-BY-SA-4.0
tags: ramsey theory, ramsey's theorem, van der waerden's theorem, szemeredi theorem
fetched: 2026-07-02
---

# Van der Waerden's theorem

**Van der Waerden's theorem** is a theorem in Ramsey theory. Van der Waerden's theorem states that for any given positive integers *r* and *k*, there is some number *N* such that if the integers {1, 2, ..., *N*} are colored, each with one of *r* different colors, then there are at least *k* integers in arithmetic progression whose elements are of the same color. The least such *N* is the Van der Waerden number *W*(*r*, *k*), named after the Dutch mathematician B. L. van der Waerden.

This was conjectured by Pierre Joseph Henry Baudet in 1921. Waerden heard of it in 1926 and published his proof in 1927, titled *Beweis einer Baudetschen Vermutung [Proof of Baudet's conjecture]*.

## Example

For example, when *r* = 2, you have two colors, say red and blue. *W*(2, 3) is bigger than 8, because you can color the integers from {1, ..., 8} like this:

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
| **B** | **R** | **R** | **B** | **B** | **R** | **R** | **B** |

and no three integers of the same color form an arithmetic progression. But you can't add a ninth integer to the end without creating such a progression. If you add a red 9, then the red 3, 6, and 9 are in arithmetic progression. Alternatively, if you add a blue 9, then the blue 1, 5, and 9 are in arithmetic progression.

In fact, there is no way of coloring 1 through 9 without creating such a progression (it can be proved by considering examples). Therefore, *W*(2, 3) is 9.

## Open problem

It is an open problem to determine the values of *W*(*r*, *k*) for most values of *r* and *k*. The proof of the theorem provides only an upper bound. For the case of *r* = 2 and *k* = 3, for example, the argument given below shows that it is sufficient to color the integers {1, ..., 325} with two colors to guarantee there will be a single-colored arithmetic progression of length 3. But in fact, the bound of 325 is very loose; the minimum required number of integers is only 9. Any coloring of the integers {1, ..., 9} will have three evenly spaced integers of one color.

For *r* = 3 and *k* = 3, the bound given by the theorem is 7(2·37 + 1)(2·37·(2·37 + 1) + 1), or approximately 4.22·1014616. But actually, you don't need that many integers to guarantee a single-colored progression of length 3; you only need 27. (And it is possible to color {1, ..., 26} with three colors so that there is no single-colored arithmetic progression of length 3; for example:

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

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

R

R

G

G

R

R

G

B

G

B

B

R

B

R

R

G

R

G

G

B

R

B

B

G

B

G

An open problem is the attempt to reduce the general upper bound to any 'reasonable' function. Ronald Graham offered a prize of US$1000 for showing *W*(2, *k*) < 2*k*2. In addition, he offered a US$250 prize for a proof of his conjecture involving more general *off-diagonal* van der Waerden numbers, stating *W*(2; 3, *k*) ≤ *k**O(1)*, while mentioning numerical evidence suggests *W*(2; 3, *k*) = *k*2 + *o(1)*. Ben Green disproved this latter conjecture and proved super-polynomial counterexamples to *W*(2; 3, *k*) < *k*r for any *r*. The best upper bound currently known is due to Timothy Gowers, who establishes

$W(r,k)\leq 2^{2^{r^{2^{2^{k+9}}}}},$

by first establishing a similar result for Szemerédi's theorem, which is a stronger version of Van der Waerden's theorem. The previously best-known bound was due to Saharon Shelah and proceeded via first proving a result for the Hales–Jewett theorem, which is another strengthening of Van der Waerden's theorem.

The best lower bound currently known for $W(2,k)$ is that for all positive $\varepsilon$ we have $W(2,k)>2^{k}/k^{\varepsilon }$ , for all sufficiently large k .

## Proof of Van der Waerden's theorem (in a special case)

The following proof is due to Ron Graham, B.L. Rothschild, and Joel Spencer. Khinchin gives a fairly simple proof of the theorem without estimating *W*(*r*, *k*).

### Proof in the case of *W*(2, 3)

| *b* | *c*(*n*): color of integers |   |   |   |   |
|---|---|---|---|---|---|
| 0 | 1 | 2 | 3 | 4 | 5 |
| **R** | **R** | **B** | **R** | **B** |   |
| 1 | 6 | 7 | 8 | 9 | 10 |
| **B** | **R** | **R** | **B** | **R** |   |
| ... | ... |   |   |   |   |
| 64 | 321 | 322 | 323 | 324 | 325 |
| **R** | **B** | **R** | **B** | **R** |   |

We will prove the special case mentioned above, that *W*(2, 3) ≤ 325. Let *c*(*n*) be a coloring of the integers {1, ..., 325}. We will find three elements of {1, ..., 325} in arithmetic progression that are the same color.

Divide {1, ..., 325} into the 65 blocks {1, ..., 5}, {6, ..., 10}, ... {321, ..., 325}, thus each block is of the form {5*b* + 1, ..., 5*b* + 5} for some *b* in {0, ..., 64}. Since each integer is colored either red or blue, each block is colored in one of 32 different ways. By the pigeonhole principle, there are two blocks among the first 33 blocks that are colored identically. That is, there are two integers *b*1 and *b*2, both in {0,...,32}, such that

c

(5

b

1

+

k

) =

c

(5

b

2

+

k

)

for all *k* in {1, ..., 5}. Among the three integers 5*b*1 + 1, 5*b*1 + 2, 5*b*1 + 3, there must be at least two that are of the same color. (The pigeonhole principle again.) Call these 5*b*1 + *a*1 and 5*b*1 + *a*2, where the *a**i* are in {1,2,3} and *a*1 < *a*2. Suppose (without loss of generality) that these two integers are both red. (If they are both blue, just exchange 'red' and 'blue' in what follows.)

Let *a*3 = 2*a*2 − *a*1. If 5*b*1 + *a*3 is red, then we have found our arithmetic progression: 5*b*1 + *a**i* are all red.

Otherwise, 5*b*1 + *a*3 is blue. Since *a*3 ≤ 5, 5*b*1 + *a*3 is in the *b*1 block, and since the *b*2 block is colored identically, 5*b*2 + *a*3 is also blue.

Now let *b*3 = 2*b*2 − *b*1. Then *b*3 ≤ 64. Consider the integer 5*b*3 + *a*3, which must be ≤ 325. What color is it?

If it is red, then 5*b*1 + *a*1, 5*b*2 + *a*2, and 5*b*3 + *a*3 form a red arithmetic progression. But if it is blue, then 5*b*1 + *a*3, 5*b*2 + *a*3, and 5*b*3 + *a*3 form a blue arithmetic progression. Either way, we are done.

### Proof in the case of *W*(3, 3)

| *b* | *c*(*n*): color of integers |   |   |   |   |
|---|---|---|---|---|---|
| 0 | 1 | 2 | 3 | ... | *m* |
| **G** | **R** | **R** | ... | **B** |   |
| 1 | *m* + 1 | *m* + 2 | *m* + 3 | ... | 2*m* |
| **B** | **R** | **G** | ... | **R** |   |
| ... | ... |   |   |   |   |
| *g* | *gm* + 1 | *gm* + 2 | *gm* + 3 | ... | (*g* + 1)*m* |
| **B** | **R** | **B** | ... | **G** |   |

A similar argument can be advanced to show that *W*(3, 3) ≤ 7(2·37+1)(2·37·(2·37+1)+1). One begins by dividing the integers into 2·37·(2·37 + 1) + 1 groups of 7(2·37 + 1) integers each; of the first 37·(2·37 + 1) + 1 groups, two must be colored identically.

Divide each of these two groups into 2·37+1 subgroups of 7 integers each; of the first 37 + 1 subgroups in each group, two of the subgroups must be colored identically. Within each of these identical subgroups, two of the first four integers must be the same color, say red; this implies either a red progression or an element of a different color, say blue, in the same subgroup.

Since we have two identically-colored subgroups, there is a third subgroup, still in the same group that contains an element which, if either red or blue, would complete a red or blue progression, by a construction analogous to the one for *W*(2, 3). Suppose that this element is green. Since there is a group that is colored identically, it must contain copies of the red, blue, and green elements we have identified; we can now find a pair of red elements, a pair of blue elements, and a pair of green elements that 'focus' on the same integer, so that whatever color it is, it must complete a progression.

### Proof in general case

The proof for *W*(2, 3) depends essentially on proving that *W*(32, 2) ≤ 33. We divide the integers {1,...,325} into 65 'blocks', each of which can be colored in 32 different ways, and then show that two blocks of the first 33 must be the same color, and there is a block colored the opposite way. Similarly, the proof for *W*(3, 3) depends on proving that

$W(3^{7(2\cdot 3^{7}+1)},2)\leq 3^{7(2\cdot 3^{7}+1)}+1.$

By a double induction on the number of colors and the length of the progression, the theorem is proved in general.

## Proof

A *D-dimensional arithmetic progression* (AP) consists of numbers of the form:

$a+i_{1}s_{1}+i_{2}s_{2}+\cdots +i_{D}s_{D}$

where *a* is the basepoint, the *s*'s are positive step-sizes, and the *i*'s range from 0 to *L* − 1. A *d*-dimensional AP is *homogeneous* for some coloring when it is all the same color.

A *D-dimensional arithmetic progression with benefits* is all numbers of the form above, but where you add on some of the "boundary" of the arithmetic progression, i.e. some of the indices *i*'s can be equal to *L*. The sides you tack on are ones where the first *k* *i*'s are equal to *L*, and the remaining *i*'s are less than *L*.

The boundaries of a D-dimensional AP with benefits are these additional arithmetic progressions of dimension $d-1,d-2,d-3,d-4$ , down to 0. The 0-dimensional arithmetic progression is the single point at index value $(L,L,L,L,\ldots ,L)$ . A D-dimensional AP with benefits is *homogeneous* when each of the boundaries are individually homogeneous, but different boundaries do not have to necessarily have the same color.

Next define the quantity MinN(*L*, *D*, *N*) to be the least integer so that any assignment of N colors to an interval of length MinN or more necessarily contains a homogeneous D-dimensional arithmetical progression with benefits.

The goal is to bound the size of MinN. Note that MinN(*L*,1,*N*) is an upper bound for Van der Waerden's number. There are two inductions steps, as follows:

**Lemma 1**—Assume MinN is known for a given lengths *L* for all dimensions of arithmetic progressions with benefits up to *D*. This formula gives a bound on MinN when you increase the dimension to *D* + 1:

let $M=\operatorname {MinN} (L,D,n)$ , then

$\operatorname {MinN} (L,D+1,n)\leq M\cdot \operatorname {MinN} (L,1,n^{M})$

Proof

First, if you have an *n*-coloring of the interval 1...*I*, you can define a *block coloring* of *k*-size blocks. Just consider each sequence of *k* colors in each *k* block to define a unique color. Call this *k-blocking* an *n*-coloring. *k*-blocking an *n* coloring of length *l* produces an *n**k* coloring of length l/*k*.

So given a *n*-coloring of an interval *I* of size $M\cdot \operatorname {MinN} (L,1,n^{M}))$ you can *M*-block it into an *n**M* coloring of length $\operatorname {MinN} (L,1,n^{M})$ . But that means, by the definition of MinN, that you can find a 1-dimensional arithmetic sequence (with benefits) of length *L* in the block coloring, which is a sequence of blocks equally spaced, which are all the same block-color, i.e. you have a bunch of blocks of length *M* in the original sequence, which are equally spaced, which have exactly the same sequence of colors inside.

Now, by the definition of *M*, you can find a *d*-dimensional arithmetic sequence with benefits in any one of these blocks, and since all of the blocks have the same sequence of colors, the same *d*-dimensional AP with benefits appears in all of the blocks, just by translating it from block to block. This is the definition of a *d* + 1 dimensional arithmetic progression, so you have a homogeneous *d* + 1 dimensional AP. The new stride parameter s*D* + 1 is defined to be the distance between the blocks.

But you need benefits. The boundaries you get now are all old boundaries, plus their translations into identically colored blocks, because iD+1 is always less than L. The only boundary which is not like this is the 0-dimensional point when $i_{1}=i_{2}=\cdots =i_{D+1}=L$ . This is a single point, and is automatically homogeneous.

**Lemma 2**—Assume MinN is known for one value of *L* and all possible dimensions *D*. Then you can bound MinN for length *L* + 1.

$\operatorname {MinN} (L+1,1,n)\leq 2\operatorname {MinN} (L,n,n)$

Proof

Given an n-coloring of an interval of size MinN(*L*,*n*,*n*), by definition, you can find an arithmetic sequence with benefits of dimension n of length L. But now, the number of "benefit" boundaries is equal to the number of colors, so one of the homogeneous boundaries, say of dimension k, has to have the same color as another one of the homogeneous benefit boundaries, say the one of dimension *p* < *k*. This allows a length *L* + 1 arithmetic sequence (of dimension 1) to be constructed, by going along a line inside the *k*-dimensional boundary which ends right on the *p*-dimensional boundary, and including the terminal point in the *p*-dimensional boundary. In formulas:

if

$a+Ls_{1}+Ls_{2}+\cdots +Ls_{D-k}$

has the same color as

$a+Ls_{1}+Ls_{2}+\cdots +Ls_{D-p}$

then

$a+L\cdot (s_{1}+\cdots +s_{D-k})+u\cdot (s_{D-k+1}+\cdots +s_{p})$

have the same color

$u=0,1,2,\cdots ,L-1,L$

i.e.

u

makes a sequence of length

L

+1.

This constructs a sequence of dimension 1, and the "benefits" are automatic, just add on another point of whatever color. To include this boundary point, one has to make the interval longer by the maximum possible value of the stride, which is certainly less than the interval size. So doubling the interval size will definitely work, and this is the reason for the factor of two. This completes the induction on *L*.

Base case: MinN(1,*d*,*n*) = 1, i.e. if you want a length 1 homogeneous d-dimensional arithmetic sequence, with or without benefits, you have nothing to do. So this forms the base of the induction. The Van der Waerden theorem itself is the assertion that MinN(*L*,1,*N*) is finite, and it follows from the base case and the induction steps.

## Ergodic theory

Furstenberg and Weiss proved an equivalent form of the theorem in 1978, using ergodic theory.

**multiple Birkhoff recurrence theorem** (Furstenberg and Weiss, 1978)—If ${\textstyle X}$ is a compact metric space, and ${\textstyle T_{1},\dots ,T_{N}:X\to X}$ are homeomorphisms that commute, then ${\textstyle \exists x\in X}$ , and an increasing sequence ${\textstyle n_{1}<n_{2}<\cdots }$ , such that $\lim _{j}d(T_{i}^{n_{j}}x,x)=0,\quad \forall i\in 1:N$

The proof of the above theorem is delicate, and the reader is referred to. With this recurrence theorem, the van der Waerden theorem can be proved in the ergodic-theoretic style.

**Theorem** (van der Waerden, 1927)—If ${\textstyle \mathbb {Z} }$ is partitioned into finitely many subsets ${\textstyle S_{1},\dots ,S_{n}}$ , then one of them ${\textstyle S_{k}}$ contains infinitely many arithmetic progressions of arbitrarily long length

$\forall N,N',\;\exists |a|\geq N',\exists r\geq 1:\{a+ir\}_{i\in 1:N}\subset S_{k}$

Proof

It suffices to show that for each length ${\textstyle N}$ , there exist at least one partition that contains at least one arithmetic progression of length ${\textstyle N}$ .Once this is proved, we can cut out that arithmetic progression into ${\textstyle N}$ singleton sets, and repeat the process to create another arithmetic progression, and so one of the partitions contain infinitely many arithmetic progressions of length ${\textstyle N}$ . Then we can repeat this process to find that there exists at least one partition that contains infinitely many progressions of length ${\textstyle N}$ , for infinitely many ${\textstyle N}$ , and that is the partition we want.

Consider the state space ${\textstyle \Omega =(1:N)^{\mathbb {Z} }}$ , which is compact under the metric (in fact, ultrametric) $d((x_{i}),(y_{i}))=\max\{2^{-\vert {i}\vert }:x_{i}\neq y_{i}\}.$ Since the sets ${\textstyle S_{1},\dots ,S_{n}}$ partition ${\textstyle \mathbb {Z} }$ , we have a well-defined sequence ${\textstyle z=(\dots ,z_{-1},z_{0},z_{1},\dots )=(z_{i})_{i}}$ with ${\textstyle i\in S_{z_{i}}}$ for all ${\textstyle i}$ .

Let ${\textstyle T:\Omega \to \Omega }$ be the shift map $T((x_{i})_{i})=(x_{i+1})_{i},$ and let ${\textstyle X=cl(\{T^{r}z:r\in \mathbb {Z} \})}$ be the closure of all shifts of the sequence ${\textstyle z}$ . By the multiple Birkhoff recurrence theorem (for the maps ${\textstyle T,T^{2},\dots ,T^{N}}$ ), there exist a sequence ${\textstyle x\in X}$ and an integer ${\textstyle s\geq 1}$ such that $d(T^{s}x,x),d(T^{2s}x,x),\dots ,d(T^{Ns}x,x)<{\frac {1}{4}}.$

Since ${\textstyle X}$ is the closure of shifts of ${\textstyle z}$ , and ${\textstyle T}$ is continuous, there exists a shift ${\textstyle T^{m}z}$ such that simultaneously, ${\textstyle x}$ is very close to ${\textstyle T^{m}z}$ , and ${\textstyle T^{s}x}$ is very close to ${\textstyle T^{s+m}z}$ , and so on: $d(x,T^{m}z),d(T^{s}x,T^{m+s}z),\dots ,d(T^{Ns}x,T^{m+Ns}z)<{\frac {1}{4}}.$

By the triangle inequality, we then immediately have ${\textstyle d(T^{m+is}z,T^{m+js}z)<{\frac {3}{4}}}$ for ${\textstyle i,j=0,\dots ,N}$ . But by construction, any sequences ${\textstyle y,y'\in \Omega }$ with ${\textstyle d(y,y')<1}$ must have ${\textstyle y_{0}={y'}\!\!{}_{0}}$ . Thus ${\textstyle z_{m}=z_{m+s}=\dots =z_{m+Ns}}$ , and so all ${\textstyle m,m+s,\dots ,m+Ns}$ lie in the partition ${\textstyle S_{z_{m}}}$ .
