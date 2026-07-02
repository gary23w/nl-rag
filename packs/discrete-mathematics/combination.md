---
title: "Combination"
source: https://en.wikipedia.org/wiki/Combination
domain: discrete-mathematics
license: CC-BY-SA-4.0
tags: discrete math, discrete mathematics, combinatorics, graph theory, set theory, permutation
fetched: 2026-07-02
---

# Combination

In mathematics, a **combination** is a selection of items from a set that has distinct members, such that the order of selection does not matter (unlike permutations). For example, given three fruits, say an apple, an orange and a pear, there are three combinations of two that can be drawn from this set: an apple and a pear; an apple and an orange; or a pear and an orange. More formally, a *k*-combination of a set *S* is a subset of *k* distinct elements of *S*. So, two combinations are identical if and only if each combination has the same members. (The arrangement of the members in each set does not matter.) If the set has *n* elements, the number of *k*-combinations, denoted by $C(n,k)$ or $C_{k}^{n}$ , is equal to the binomial coefficient:

${\binom {n}{k}}={\frac {n(n-1)\dotsb (n-k+1)}{k(k-1)\dotsb 1}},$

which using factorial notation can be compactly expressed as

${\binom {n}{k}}={\frac {n!}{k!(n-k)!}}$

whenever $n\geq k\geq 0$ . This formula can be derived from the fact that each *k*-combination of a set *S* of *n* members has $k!$ permutations so $P_{k}^{n}=C_{k}^{n}\times k!$ or $C_{k}^{n}=P_{k}^{n}/k!$ . The set of all *k*-combinations of a set *S* is often denoted by $\textstyle {\binom {S}{k}}$ .

A combination is a selection of *n* things taken *k* at a time *without repetition*. To refer to combinations in which repetition is allowed, the terms *k*-combination with repetition, *k*-multiset, or *k*-selection, are often used. If, in the above example, it were possible to have two of any one kind of fruit there would be 3 more 2-selections: one with two apples, one with two oranges, and one with two pears.

Although the set of three fruits was small enough to write a complete list of combinations, this becomes impractical as the size of the set increases. For example, a poker hand can be described as a 5-combination (*k* = 5) of cards from a 52 card deck (*n* = 52). The 5 cards of the hand are all distinct, and the order of cards in the hand does not matter. There are 2,598,960 such combinations, and the chance of drawing any one hand at random is 1 / 2,598,960.

## Number of *k*-combinations

The number of *k*-combinations from a given set *S* of *n* elements is often denoted in elementary combinatorics texts by $C(n,k)$ , or by a variation such as $C_{k}^{n}$ , ${}_{n}C_{k}$ , ${}^{n}C_{k}$ , $C_{n,k}$ or even $C_{n}^{k}$ (the last form is standard in French, Romanian, Russian, and Chinese texts). The same number however occurs in many other mathematical contexts, where it is denoted by ${\tbinom {n}{k}}$ (often read as "*n* choose *k*"); notably it occurs as a coefficient in the binomial formula, hence its name binomial coefficient. One can define ${\tbinom {n}{k}}$ for all natural numbers *k* at once by the relation

$(1+X)^{n}=\sum _{k\geq 0}{\binom {n}{k}}X^{k},$

from which it is clear that

${\binom {n}{0}}={\binom {n}{n}}=1,$

and further

${\binom {n}{k}}=0$

for $k>n$ .

To see that these coefficients count *k*-combinations from *S*, one can first consider a collection of *n* distinct variables *X**s* labeled by the elements *s* of *S*, and expand the product over all elements of *S*:

$\prod _{s\in S}(1+X_{s});$

it has 2*n* distinct terms corresponding to all the subsets of *S*, each subset giving the product of the corresponding variables *X**s*. Now setting all of the *X**s* equal to the unlabeled variable *X*, so that the product becomes (1 + *X*)*n*, the term for each *k*-combination from *S* becomes *X**k*, so that the coefficient of that power in the result equals the number of such *k*-combinations.

Binomial coefficients can be computed explicitly in various ways. To get all of them for the expansions up to (1 + *X*)*n*, one can use (in addition to the basic cases already given) the recursion relation

${\binom {n}{k}}={\binom {n-1}{k-1}}+{\binom {n-1}{k}},$

for 0 < *k* < *n*, which follows from (1 + *X*)*n* = (1 + *X*)*n* − 1(1 + *X*); this leads to the construction of Pascal's triangle.

For determining an individual binomial coefficient, it is more practical to use the formula

${\binom {n}{k}}={\frac {n(n-1)(n-2)\cdots (n-k+1)}{k!}}.$

The numerator gives the number of *k*-permutations of *n*, i.e., of sequences of *k* distinct elements of *S*, while the denominator gives the number of such *k*-permutations that give the same *k*-combination when the order is ignored.

When *k* exceeds *n*/2, the above formula contains factors common to the numerator and the denominator, and canceling them out gives the relation

${\binom {n}{k}}={\binom {n}{n-k}},$

for 0 ≤ *k* ≤ *n*. This expresses a symmetry that is evident from the binomial formula, and can also be understood in terms of *k*-combinations by taking the complement of such a combination, which is an (*n* − *k*)-combination.

Finally there is a formula which exhibits this symmetry directly, and has the merit of being easy to remember:

${\binom {n}{k}}={\frac {n!}{k!(n-k)!}},$

where *n*! denotes the factorial of *n*. It is obtained from the previous formula by multiplying denominator and numerator by (*n* − *k*)!, so it is certainly computationally less efficient than that formula.

The last formula can be understood directly, by considering the *n*! permutations of all the elements of *S*. Each such permutation gives a *k*-combination by selecting its first *k* elements. There are many duplicate selections: any combined permutation of the first *k* elements among each other, and of the final (*n* − *k*) elements among each other produces the same combination; this explains the division in the formula.

From the above formulas follow relations between adjacent numbers in Pascal's triangle in all three directions:

${\binom {n}{k}}={\begin{cases}\displaystyle {\binom {n}{k-1}}{\frac {n-k+1}{k}}&\quad {\text{if }}k>0\\\displaystyle {\binom {n-1}{k}}{\frac {n}{n-k}}&\quad {\text{if }}k<n\\\displaystyle {\binom {n-1}{k-1}}{\frac {n}{k}}&\quad {\text{if }}n,k>0\end{cases}}.$

Together with the basic cases ${\tbinom {n}{0}}=1={\tbinom {n}{n}}$ , these allow successive computation of respectively all numbers of combinations from the same set (a row in Pascal's triangle), of *k*-combinations of sets of growing sizes, and of combinations with a complement of fixed size *n* − *k*.

### Example of counting combinations

As a specific example, one can compute the number of five-card hands possible from a standard fifty-two card deck as:

${\binom {52}{5}}={\frac {52\times 51\times 50\times 49\times 48}{5\times 4\times 3\times 2\times 1}}={\frac {311{,}875{,}200}{120}}=2{,}598{,}960.$

Alternatively, one may use the formula in terms of factorials and cancel the factors in the numerator against parts of the factors in the denominator, after which only multiplication of the remaining factors is required: ${\begin{alignedat}{2}{\binom {52}{5}}&={\frac {52!}{5!47!}}\\[5pt]&={\frac {52\times 51\times 50\times 49\times 48\times {\cancel {47!}}}{5\times 4\times 3\times 2\times {\cancel {1}}\times {\cancel {47!}}}}\\[5pt]&={\frac {52\times 51\times 50\times 49\times 48}{5\times 4\times 3\times 2}}\\[5pt]&={\frac {(26\times {\cancel {2}})\times (17\times {\cancel {3}})\times (10\times {\cancel {5}})\times 49\times (12\times {\cancel {4}})}{{\cancel {5}}\times {\cancel {4}}\times {\cancel {3}}\times {\cancel {2}}}}\\[5pt]&={26\times 17\times 10\times 49\times 12}\\[5pt]&=2{,}598{,}960.\end{alignedat}}$

Another alternative computation, equivalent to the first, is based on writing

${\binom {n}{k}}={\frac {(n-0)}{1}}\times {\frac {(n-1)}{2}}\times {\frac {(n-2)}{3}}\times \cdots \times {\frac {(n-(k-1))}{k}},$

which gives

${\binom {52}{5}}={\frac {52}{1}}\times {\frac {51}{2}}\times {\frac {50}{3}}\times {\frac {49}{4}}\times {\frac {48}{5}}=2{,}598{,}960.$

When evaluated in the following order, 52 ÷ 1 × 51 ÷ 2 × 50 ÷ 3 × 49 ÷ 4 × 48 ÷ 5, this can be computed using only integer arithmetic. The reason is that when each division occurs, the intermediate result that is produced is itself a binomial coefficient, so no remainders ever occur.

Using the symmetric formula in terms of factorials without performing simplifications gives a rather extensive calculation:

${\begin{aligned}{\binom {52}{5}}&={\frac {n!}{k!(n-k)!}}={\frac {52!}{5!(52-5)!}}={\frac {52!}{5!47!}}\\[6pt]&={\tfrac {80,658,175,170,943,878,571,660,636,856,403,766,975,289,505,440,883,277,824,000,000,000,000}{120\times 258,623,241,511,168,180,642,964,355,153,611,979,969,197,632,389,120,000,000,000}}\\[6pt]&=2{,}598{,}960.\end{aligned}}$

### Enumerating *k*-combinations

One can enumerate all *k*-combinations of a given set *S* of *n* elements in some fixed order, which establishes a bijection from an interval of ${\tbinom {n}{k}}$ integers with the set of those *k*-combinations. Assuming *S* is itself ordered, for instance *S* = { 1, 2, ..., *n* }, there are two natural possibilities for ordering its *k*-combinations: by comparing their smallest elements first (as in the illustrations above) or by comparing their largest elements first. The latter option has the advantage that adding a new largest element to *S* will not change the initial part of the enumeration, but just add the new *k*-combinations of the larger set after the previous ones. Repeating this process, the enumeration can be extended indefinitely with *k*-combinations of ever larger sets. If moreover the intervals of the integers are taken to start at 0, then the *k*-combination at a given place *i* in the enumeration can be computed easily from *i*, and the bijection so obtained is known as the combinatorial number system. It is also known as "rank"/"ranking" and "unranking" in computational mathematics.

There are many ways to enumerate *k* combinations. One way is to track *k* index numbers of the elements selected, starting with {0 .. *k*−1} (zero-based) or {1 .. *k*} (one-based) as the first allowed *k*-combination. Then, repeatedly move to the next allowed *k*-combination by incrementing the smallest index number for which this would not create two equal index numbers, at the same time resetting all smaller index numbers to their initial values.

## Number of combinations with repetition

A *k*-**combination with repetitions**, or *k*-**multicombination**, or **multisubset** of size *k* from a set *S* of size *n* is given by a set of *k* not necessarily distinct elements of *S*, where order is not taken into account: two sequences define the same multiset if one can be obtained from the other by permuting the terms. In other words, it is a sample of *k* elements from a set of *n* elements allowing for duplicates (i.e., with replacement) but disregarding different orderings (e.g. {2,1,2} = {1,2,2}). Associate an index to each element of *S* and think of the elements of *S* as *types* of objects, then we can let $x_{i}$ denote the number of elements of type *i* in a multisubset. The number of multisubsets of size *k* is then the number of nonnegative integer (so allowing zero) solutions of the Diophantine equation:

$x_{1}+x_{2}+\ldots +x_{n}=k.$

If *S* has *n* elements, the number of such *k*-multisubsets is denoted by

$\left(\!\!{\binom {n}{k}}\!\!\right),$

a notation that is analogous to the binomial coefficient which counts *k*-subsets. This expression, *n* multichoose *k*, can also be given in terms of binomial coefficients:

$\left(\!\!{\binom {n}{k}}\!\!\right)={\binom {n+k-1}{k}}.$

This relationship can be easily proved using a representation known as stars and bars.

Proof

A solution of the above Diophantine equation can be represented by $x_{1}$ *stars*, a separator (a *bar*), then $x_{2}$ more stars, another separator, and so on. The total number of stars in this representation is *k* and the number of bars is *n* - 1 (since a separation into n parts needs n-1 separators). Thus, a string of *k* + *n* - 1 (or *n* + *k* - 1) symbols (stars and bars) corresponds to a solution if there are *k* stars in the string. Any solution can be represented by choosing *k* out of *k* + *n* − 1 positions to place stars and filling the remaining positions with bars. For example, the solution $x_{1}=3,x_{2}=2,x_{3}=0,x_{4}=5$ of the equation $x_{1}+x_{2}+x_{3}+x_{4}=10$ (*n* = 4 and *k* = 10) can be represented by

$\bigstar \bigstar \bigstar |\bigstar \bigstar ||\bigstar \bigstar \bigstar \bigstar \bigstar .$

The number of such strings is the number of ways to place 10 stars in 13 positions, ${\textstyle {\binom {13}{10}}={\binom {13}{3}}=286,}$ which is the number of 10-multisubsets of a set with 4 elements.

As with binomial coefficients, there are several relationships between these multichoose expressions. For example, for $n\geq 1,k\geq 0$ ,

$\left(\!\!{\binom {n}{k}}\!\!\right)=\left(\!\!{\binom {k+1}{n-1}}\!\!\right).$ This identity follows from interchanging the stars and bars in the above representation.

### Example of counting multisubsets

For example, if you have four types of donuts (*n* = 4) on a menu to choose from and you want three donuts (*k* = 3), the number of ways to choose the donuts with repetition can be calculated as

$\left(\!\!{\binom {4}{3}}\!\!\right)={\binom {4+3-1}{3}}={\binom {6}{3}}={\frac {6\times 5\times 4}{3\times 2\times 1}}=20.$

This result can be verified by listing all the 3-multisubsets of the set *S* = {1,2,3,4}. This is displayed in the following table. The second column lists the donuts you actually chose, the third column shows the nonnegative integer solutions $[x_{1},x_{2},x_{3},x_{4}]$ of the equation $x_{1}+x_{2}+x_{3}+x_{4}=3$ and the last column gives the stars and bars representation of the solutions.

| No. | 3-multiset | Eq. solution | Stars and bars |
|---|---|---|---|
| 1 | {1,1,1} | [3,0,0,0] | $\bigstar \bigstar \bigstar \|\|\|$ |
| 2 | {1,1,2} | [2,1,0,0] | $\bigstar \bigstar \|\bigstar \|\|$ |
| 3 | {1,1,3} | [2,0,1,0] | $\bigstar \bigstar \|\|\bigstar \|$ |
| 4 | {1,1,4} | [2,0,0,1] | $\bigstar \bigstar \|\|\|\bigstar$ |
| 5 | {1,2,2} | [1,2,0,0] | $\bigstar \|\bigstar \bigstar \|\|$ |
| 6 | {1,2,3} | [1,1,1,0] | $\bigstar \|\bigstar \|\bigstar \|$ |
| 7 | {1,2,4} | [1,1,0,1] | $\bigstar \|\bigstar \|\|\bigstar$ |
| 8 | {1,3,3} | [1,0,2,0] | $\bigstar \|\|\bigstar \bigstar \|$ |
| 9 | {1,3,4} | [1,0,1,1] | $\bigstar \|\|\bigstar \|\bigstar$ |
| 10 | {1,4,4} | [1,0,0,2] | $\bigstar \|\|\|\bigstar \bigstar$ |
| 11 | {2,2,2} | [0,3,0,0] | $\|\bigstar \bigstar \bigstar \|\|$ |
| 12 | {2,2,3} | [0,2,1,0] | $\|\bigstar \bigstar \|\bigstar \|$ |
| 13 | {2,2,4} | [0,2,0,1] | $\|\bigstar \bigstar \|\|\bigstar$ |
| 14 | {2,3,3} | [0,1,2,0] | $\|\bigstar \|\bigstar \bigstar \|$ |
| 15 | {2,3,4} | [0,1,1,1] | $\|\bigstar \|\bigstar \|\bigstar$ |
| 16 | {2,4,4} | [0,1,0,2] | $\|\bigstar \|\|\bigstar \bigstar$ |
| 17 | {3,3,3} | [0,0,3,0] | $\|\|\bigstar \bigstar \bigstar \|$ |
| 18 | {3,3,4} | [0,0,2,1] | $\|\|\bigstar \bigstar \|\bigstar$ |
| 19 | {3,4,4} | [0,0,1,2] | $\|\|\bigstar \|\bigstar \bigstar$ |
| 20 | {4,4,4} | [0,0,0,3] | $\|\|\|\bigstar \bigstar \bigstar$ |

## Number of *k*-combinations for all *k*

The number of *k*-combinations for all *k* is the number of subsets of a set of *n* elements. There are several ways to see that this number is 2*n*. In terms of combinations, ${\textstyle \sum _{0\leq {k}\leq {n}}{\binom {n}{k}}=2^{n}}$ , which is the sum of the *n*th row (counting from 0) of the binomial coefficients in Pascal's triangle. These combinations (subsets) are enumerated by the 1 digits of the set of base 2 numbers counting from 0 to 2*n* − 1, where each digit position is an item from the set of *n*.

Given 3 cards numbered 1 to 3, there are 8 distinct combinations (subsets), including the empty set:

$|\{\{\};\{1\};\{2\};\{1,2\};\{3\};\{1,3\};\{2,3\};\{1,2,3\}\}|=2^{3}=8$

Representing these subsets (in the same order) as base 2 numerals:

- 0 – 000
- 1 – 001
- 2 – 010
- 3 – 011
- 4 – 100
- 5 – 101
- 6 – 110
- 7 – 111

## Probability: sampling a random combination

There are various algorithms to pick out a random combination from a given set or list. Rejection sampling is extremely slow for large sample sizes. One way to select a *k*-combination efficiently from a population of size *n* is to iterate across each element of the population, and at each step pick that element with a dynamically changing probability of ${\textstyle {\frac {k-\#{\text{samples chosen}}}{n-\#{\text{samples visited}}}}}$ (see Reservoir sampling). Another is to pick a random non-negative integer less than $\textstyle {\binom {n}{k}}$ and convert it into a combination using the combinatorial number system.

## Number of ways to put objects into bins

A combination can also be thought of as a selection of *two* sets of items: those that go into the chosen bin and those that go into the unchosen bin. This can be generalized to any number of bins with the constraint that every item must go to exactly one bin. The number of ways to put objects into bins is given by the multinomial coefficient

${\binom {n}{k_{1},k_{2},\ldots ,k_{m}}}={\frac {n!}{k_{1}!\,k_{2}!\cdots k_{m}!}},$

where *n* is the number of items, *m* is the number of bins, and $k_{i}$ is the number of items that go into bin *i*.

One way to see why this equation holds is to first number the objects arbitrarily from *1* to *n* and put the objects with numbers $1,2,\ldots ,k_{1}$ into the first bin in order, the objects with numbers $k_{1}+1,k_{1}+2,\ldots ,k_{1}+k_{2}$ into the second bin in order, and so on. There are $n!$ distinct numberings, but many of them are equivalent, because only the set of items in a bin matters, not their order in it. Every combined permutation of each bins' contents produces an equivalent way of putting items into bins. As a result, every equivalence class consists of $k_{1}!\,k_{2}!\cdots k_{m}!$ distinct numberings, and the number of equivalence classes is $\textstyle {\frac {n!}{k_{1}!\,k_{2}!\cdots k_{m}!}}$ .

The binomial coefficient is the special case where *k* items go into the chosen bin and the remaining $n-k$ items go into the unchosen bin:

${\binom {n}{k}}={\binom {n}{k,n-k}}={\frac {n!}{k!(n-k)!}}.$
