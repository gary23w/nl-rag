---
title: "Latin square"
source: https://en.wikipedia.org/wiki/Latin_square
domain: experimental-design
license: CC-BY-SA-4.0
tags: design of experiments, statistical blocking, treatment randomization, experimental replication
fetched: 2026-07-02
---

# Latin square

In combinatorics and in experimental design, a **Latin square** is an *n* × *n* array filled with *n* different symbols, each occurring exactly once in each row and exactly once in each column. An example of a 3 × 3 Latin square is

| A | B | C |
|---|---|---|
| C | A | B |
| B | C | A |

The name "Latin square" was inspired by mathematical papers by Leonhard Euler (1707–1783), who used Latin characters as symbols, but any set of symbols can be used: in the above example, the alphabetic sequence A, B, C can be replaced by the integer sequence 1, 2, 3. Euler began the general theory of Latin squares.

## History

The Korean mathematician Choi Seok-jeong was the first to publish an example of Latin squares of order nine, in order to construct a magic square in 1700, predating Leonhard Euler by 67 years.

### Counting

This account follows McKay, Meynert & Myrvold (2007, p. 100).

The counting of Latin squares has a long history, but the published accounts contain many errors. Euler in 1782, and Cayley in 1890, both knew the number of reduced Latin squares up to order five. In 1915, MacMahon approached the problem in a different way, but initially obtained the wrong value for order five. M.Frolov in 1890, and Tarry in 1901, found the number of reduced squares of order six. M. Frolov gave an incorrect count of reduced squares of order seven. R.A. Fisher and F. Yates, unaware of earlier work of E. Schönhardt, gave the number of isotopy classes of orders up to six. In 1939, H. W. Norton found 562 isotopy classes of order seven, but acknowledged that his method was incomplete. A. Sade, in 1951, but privately published earlier in 1948, and P. N. Saxena found more classes and, in 1966, D. A. Preece noted that this corrected Norton's result to 564 isotopy classes. However, in 1968, J. W. Brown announced an incorrect value of 563, which has often been repeated. He also gave the wrong number of isotopy classes of order eight. The correct number of reduced squares of order eight had already been found by M. B. Wells in 1967, and the numbers of isotopy classes, in 1990, by G. Kolesova, C.W.H. Lam and L. Thiel. The number of reduced squares for order nine was obtained by S. E. Bammel and J. Rothstein, for order 10 by B. D. McKay and E. Rogoyski, and for order 11 by B. D. McKay and I. M. Wanless.

## Reduced form

A Latin square is said to be *reduced* (also, *normalized* or *in standard form*) if both its first row and its first column are in their natural order. For example, the Latin square above is not reduced because its first column is A, C, B rather than A, B, C.

Any Latin square can be reduced by permuting (that is, reordering) the rows and columns. Here switching the above matrix's second and third rows yields the following square:

| A | B | C |
|---|---|---|
| B | C | A |
| C | A | B |

This Latin square is reduced; both its first row and its first column are alphabetically ordered A, B, C.

## Properties

### Orthogonal array representation

If each entry of an *n* × *n* Latin square is written as a triple (*r*,*c*,*s*), where *r* is the row, *c* is the column, and *s* is the symbol, we obtain a set of *n*2 triples called the orthogonal array representation of the square. For example, the orthogonal array representation of the Latin square

| 1 | 2 | 3 |
|---|---|---|
| 2 | 3 | 1 |
| 3 | 1 | 2 |

is

{ (1, 1, 1), (1, 2, 2), (1, 3, 3), (2, 1, 2), (2, 2, 3), (2, 3, 1), (3, 1, 3), (3, 2, 1), (3, 3, 2) },

where for example the triple (2, 3, 1) means that in row 2 and column 3 there is the symbol 1. Orthogonal arrays are usually written in array form where the triples are the rows, such as

| *r* | *c* | *s* |
|---|---|---|
| 1 | 1 | 1 |
| 1 | 2 | 2 |
| 1 | 3 | 3 |
| 2 | 1 | 2 |
| 2 | 2 | 3 |
| 2 | 3 | 1 |
| 3 | 1 | 3 |
| 3 | 2 | 1 |
| 3 | 3 | 2 |

The definition of a Latin square can be written in terms of orthogonal arrays:

- A Latin square is a set of *n*2 triples (*r*, *c*, *s*), where 1 ≤ *r*, *c*, *s* ≤ *n*, such that all ordered pairs (*r*, *c*) are distinct, all ordered pairs (*r*, *s*) are distinct, and all ordered pairs (*c*, *s*) are distinct.

This means that the *n*2 ordered pairs (*r*, *c*) are all the pairs (*i*, *j*) with 1 ≤ *i*, *j* ≤ *n*, once each. The same is true of the ordered pairs (*r*, *s*) and the ordered pairs (*c*, *s*).

The orthogonal array representation shows that rows, columns and symbols play rather similar roles, as will be made clear below.

### Equivalence classes of Latin squares

Many operations on a Latin square produce another Latin square (for example, turning it upside down).

If we permute the rows, permute the columns, or permute the names of the symbols of a Latin square, we obtain a new Latin square said to be *isotopic* to the first. Isotopism is an equivalence relation, so the set of all Latin squares is divided into subsets, called *isotopy classes*, such that two squares in the same class are isotopic and two squares in different classes are not isotopic.

A stronger form of equivalence exists. Two Latin squares *L*1 and *L*2 of side n with common symbol set S that is also the index set for the rows and columns of each square are *isomorphic* if there is a bijection *g*: *S* → *S* such that *g*(*L*1(*i*, *j*)) = *L*2(*g*(*i*), *g*(*j*)) for all i, j in S. An alternate way to define isomorphic Latin squares is to say that a pair of isotopic Latin squares are isomorphic if the three bijections used to show that they are isotopic are, in fact, equal. Isomorphism is also an equivalence relation and its equivalence classes are called *isomorphism classes*.

Another type of operation is easiest to explain using the orthogonal array representation of the Latin square. If we systematically and consistently reorder the three items in each triple (that is, permute the three columns in the array form), another orthogonal array (and, thus, another Latin square) is obtained. For example, we can replace each triple (*r*,*c*,*s*) by (*c*,*r*,*s*) which corresponds to transposing the square (reflecting about its main diagonal), or we could replace each triple (*r*,*c*,*s*) by (*c*,*s*,*r*), which is a more complicated operation. Altogether there are 6 possibilities including "do nothing", giving us 6 Latin squares called the conjugates (also parastrophes) of the original square.

Finally, we can combine these two equivalence operations: two Latin squares are said to be *paratopic*, also *main class isotopic*, if one of them is isotopic to a conjugate of the other. This is again an equivalence relation, with the equivalence classes called *main classes*, *species*, or *paratopy classes*. Each main class contains up to six isotopy classes.

### Number of *n* × *n* Latin squares

There is no known easily computable formula for the number *Ln* of *n* × *n* Latin squares with symbols 1, 2, ..., *n*. The most accurate upper and lower bounds known for large n are far apart. One classic result is that $\prod _{k=1}^{n}\left(k!\right)^{n/k}\geq L_{n}\geq {\frac {\left(n!\right)^{2n}}{n^{n^{2}}}}.$

A simple and explicit formula for the number of Latin squares was published in 1992, but it is still not easily computable due to the exponential increase in the number of terms. This formula for the number *Ln* of *n* × *n* Latin squares is $L_{n}=n!\sum _{A\in B_{n}}^{}(-1)^{\sigma _{0}(A)}{\binom {\operatorname {per} A}{n}},$ where *B**n* is the set of all *n* × *n* {0, 1}-matrices, σ0(*A*) is the number of zero entries in matrix A, and per(*A*) is the permanent of matrix A.

The table below contains all known exact values. It can be seen that the numbers grow exceedingly quickly. For each n, the number of Latin squares altogether (sequence A002860 in the OEIS) is *n*! (*n* − 1)! times the number of reduced Latin squares (sequence A000315 in the OEIS).

| n | reduced Latin squares of size n (sequence A000315 in the OEIS) | all Latin squares of size n (sequence A002860 in the OEIS) |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 1 | 2 |
| 3 | 1 | 12 |
| 4 | 4 | 576 |
| 5 | 56 | 161,280 |
| 6 | 9,408 | 812,851,200 |
| 7 | 16,942,080 | 61,479,419,904,000 |
| 8 | 535,281,401,856 | 108,776,032,459,082,956,800 |
| 9 | 377,597,570,964,258,816 | 5,524,751,496,156,892,842,531,225,600 |
| 10 | 7,580,721,483,160,132,811,489,280 | 9,982,437,658,213,039,871,725,064,756,920,320,000 |
| 11 | 5,363,937,773,277,371,298,119,673,540,771,840 | 776,966,836,171,770,144,107,444,346,734,230,682,311,065,600,000 |
| 12 | 1.62 × 1044 |   |
| 13 | 2.51 × 1056 |   |
| 14 | 2.33 × 1070 |   |
| 15 | 1.50 × 1086 |   |

For each n, each isotopy class (sequence A040082 in the OEIS) contains up to (*n*!)3 Latin squares (the exact number varies), while each main class (sequence A003090 in the OEIS) contains either 1, 2, 3 or 6 isotopy classes.

| n | main classes (sequence A003090 in the OEIS) | isotopy classes (sequence A040082 in the OEIS) | structurally distinct squares (sequence A264603 in the OEIS) |
|---|---|---|---|
| 1 | 1 | 1 | 1 |
| 2 | 1 | 1 | 1 |
| 3 | 1 | 1 | 1 |
| 4 | 2 | 2 | 12 |
| 5 | 2 | 2 | 192 |
| 6 | 12 | 22 | 145,164 |
| 7 | 147 | 564 | 1,524,901,344 |
| 8 | 283,657 | 1,676,267 |   |
| 9 | 19,270,853,541 | 115,618,721,533 |   |
| 10 | 34,817,397,894,749,939 | 208,904,371,354,363,006 |   |
| 11 | 2,036,029,552,582,883,134,196,099 | 12,216,177,315,369,229,261,482,540 |   |

The number of structurally distinct Latin squares (i.e. the squares cannot be made identical by means of rotation, reflection, and permutation of the symbols) for n = 1 up to 7 is 1, 1, 1, 12, 192, 145164, 1524901344 respectively (sequence A264603 in the OEIS).

### Examples

We give one example of a Latin square from each main class up to order five.

${\begin{bmatrix}1\end{bmatrix}}\quad {\begin{bmatrix}1&2\\2&1\end{bmatrix}}\quad {\begin{bmatrix}1&2&3\\2&3&1\\3&1&2\end{bmatrix}}$

${\begin{bmatrix}1&2&3&4\\2&1&4&3\\3&4&1&2\\4&3&2&1\end{bmatrix}}\quad {\begin{bmatrix}1&2&3&4\\2&4&1&3\\3&1&4&2\\4&3&2&1\end{bmatrix}}$

${\begin{bmatrix}1&2&3&4&5\\2&3&5&1&4\\3&5&4&2&1\\4&1&2&5&3\\5&4&1&3&2\end{bmatrix}}\quad {\begin{bmatrix}1&2&3&4&5\\2&4&1&5&3\\3&5&4&2&1\\4&1&5&3&2\\5&3&2&1&4\end{bmatrix}}$

They present, respectively, the multiplication tables of the following groups:

- {0} – the trivial 1-element group
- $\mathbb {Z} _{2}$ – the binary group
- $\mathbb {Z} _{3}$ – cyclic group of order 3
- $\mathbb {Z} _{2}\times \mathbb {Z} _{2}$ – the Klein four-group
- $\mathbb {Z} _{4}$ – cyclic group of order 4
- $\mathbb {Z} _{5}$ – cyclic group of order 5
- the last one is an example of a quasigroup, or rather a loop, which is not associative.

### Orthogonal pairs

Two Latin squares of the same order *n* are called **orthogonal** if, by overlaying them, one gets every ordered pair (*a*,*b*) of symbols where *a* is a symbol in the first square and *b* is one in the second square. Orthogonal pairs and more generally sets of pairwise orthogonal Latin squares are important in design theory and finite geometry.

## Completing a partial Latin square

A Latin rectangle is an *m*-by-*n* rectangle, where *m* < *n*, such that each number 1, ..., *n* appears exactly once in each row and at most once in each column. Any Latin rectangle can be completed to a Latin square by adding rows. The proof uses Hall's marriage theorem.

More generally, one may consider the problem of whether a partial filling of an *n*-by-*n* square with numbers 1, ..., *n* that does not contain two equal entries in any row or column can be completed to a Latin square. If *n* − 1 or fewer filled cells are given, this is always possible. Various other completability questions have been considered.

The problem of determining if a partially filled square can be completed to form a Latin square is NP-complete.

A *critical set* in a Latin square is a partial Latin square that has a unique completion, but for which no proper subset has a unique completion. The notations scs(*n*) and lcs(*n*) denote, respectively, the smallest and largest possible size of a critical set in any Latin square of order *n*. The exact values of scs(*n*) are known for *n* ≤ 8, and those of lcs(*n*) for *n* ≤ 7:

Sizes of critical sets

n

1

2

3

4

5

6

7

8

scs(

n

)

0

1

2

4

6

9

12

16

lcs(

n

)

0

1

3

7

11

18

25

—

## Transversals and rainbow matchings

A **transversal** in a Latin square is a choice of *n* cells, where each row contains one cell, each column contains one cell, and there is one cell containing each symbol.

One can consider a Latin square as a complete bipartite graph in which the rows are vertices of one part, the columns are vertices of the other part, each cell is an edge (between its row and its column), and the symbols are colors. The rules of the Latin squares imply that this is a proper edge coloring. With this definition, a Latin transversal is a matching in which each edge has a different color; such a matching is called a rainbow matching.

Therefore, many results on Latin squares/rectangles are contained in papers with the term "rainbow matching" in their title, and vice versa.

Some Latin squares have no transversal. For example, when *n* is even, an *n*-by-*n* Latin square in which the value of cell *i*,*j* is (*i*+*j*) mod *n* has no transversal. Here are two examples: ${\begin{bmatrix}1&2\\2&1\end{bmatrix}}\quad {\begin{bmatrix}1&2&3&4\\2&3&4&1\\3&4&1&2\\4&1&2&3\end{bmatrix}}$ In 1967, H. J. Ryser conjectured that, when *n* is **odd**, every *n*-by-*n* Latin square has a transversal.

In 1975, S. K. Stein and Brualdi conjectured that, when *n* is **even**, every *n*-by-*n* Latin square has a **partial** transversal of size *n*−1.

A more general conjecture of Stein is that a transversal of size *n*−1 exists not only in Latin squares but also in any *n*-by-*n* array of *n* symbols, as long as each symbol appears exactly *n* times.

Some weaker versions of these conjectures have been proved:

- Every *n*-by-*n* Latin square has a partial transversal of size 2*n*/3.
- Every *n*-by-*n* Latin square has a partial transversal of size *n* − sqrt(*n*).
- Every *n*-by-*n* Latin square has a partial transversal of size *n* − 11 log2 2(*n*).
- Every *n*-by-*n* Latin square has a partial transversal of size *n* − O(log n/loglog n).
- Every large enough *n*-by-*n* Latin square has a partial transversal of size *n* −1. (Preprint)

## Algorithms

For small squares it is possible to generate permutations and test whether the Latin square property is met. For larger squares, Jacobson and Matthews' algorithm allows sampling from a uniform distribution over the space of *n* × *n* Latin squares.

## Applications

### Statistics and mathematics

- In the design of experiments, Latin squares are a special case of *row-column designs* for two blocking factors.
- In algebra, Latin squares are related to generalizations of groups; in particular, Latin squares are characterized as being the multiplication tables (Cayley tables) of quasigroups. A binary operation whose table of values forms a Latin square is said to obey the Latin square property.

### Error correcting codes

Sets of Latin squares that are orthogonal to each other have found an application as error correcting codes in situations where communication is disturbed by more types of noise than simple white noise, such as when attempting to transmit broadband Internet over powerlines.

Firstly, the message is sent by using several frequencies, or channels, a common method that makes the signal less vulnerable to noise at any one specific frequency. A letter in the message to be sent is encoded by sending a series of signals at different frequencies at successive time intervals. In the example below, the letters A to L are encoded by sending signals at four different frequencies, in four time slots. The letter C, for instance, is encoded by first sending at frequency 3, then 4, 1 and 2.

${\begin{matrix}A\\B\\C\\D\\\end{matrix}}{\begin{bmatrix}1&2&3&4\\2&1&4&3\\3&4&1&2\\4&3&2&1\\\end{bmatrix}}\quad {\begin{matrix}E\\F\\G\\H\\\end{matrix}}{\begin{bmatrix}1&3&4&2\\2&4&3&1\\3&1&2&4\\4&2&1&3\\\end{bmatrix}}\quad {\begin{matrix}I\\J\\K\\L\\\end{matrix}}{\begin{bmatrix}1&4&2&3\\2&3&1&4\\3&2&4&1\\4&1&3&2\\\end{bmatrix}}$

The encoding of the twelve letters are formed from three Latin squares that are orthogonal to each other. Now imagine that there's added noise in channels 1 and 2 during the whole transmission. The letter A would then be picked up as ${\begin{matrix}12&12&123&124\end{matrix}}$

In other words, in the first slot we receive signals from both frequency 1 and frequency 2; while the third slot has signals from frequencies 1, 2 and 3. Because of the noise, we can no longer tell if the first two slots were 1,1 or 1,2 or 2,1 or 2,2. But the 1,2 case is the only one that yields a sequence matching a letter in the above table, the letter A. Similarly, we may imagine a burst of static over all frequencies in the third slot: ${\begin{matrix}1&2&1234&4\end{matrix}}$

Again, we are able to infer from the table of encodings that it must have been the letter A being transmitted. The number of errors this code can spot is one less than the number of time slots. It has also been proven that if the number of frequencies is a prime or a power of a prime, the orthogonal Latin squares produce error detecting codes that are as efficient as possible.

### Mathematical puzzles

The popular Sudoku puzzles are a special case of Latin squares; any solution to a Sudoku puzzle is a Latin square. Sudoku imposes the additional restriction that nine particular 3 × 3 adjacent subsquares must also contain the digits 1–9 (in the standard version). See also Mathematics of Sudoku.

The more recent KenKen and Strimko puzzles are also examples of Latin squares.

### Board games

Latin squares have been used as the basis for several board games, notably the popular abstract strategy game Kamisado.

### Agronomic research

Latin squares are used in the design of agronomic research experiments to minimise experimental errors.

## Heraldry

The Latin square also figures in the arms of the Statistical Society of Canada, being specifically mentioned in its blazon. Also, it appears in the logo of the International Biometric Society.

## Generalizations

- A Latin rectangle is a generalization of a Latin square in which there are *n* columns and *n* possible values, but the number of rows may be smaller than *n*. Each value still appears at most once in each row and column.
- A Graeco-Latin square is a pair of two Latin squares such that, when one is laid on top of the other, each ordered pair of symbols appears exactly once.
- A Latin hypercube is a generalization of a Latin square from two dimensions to multiple dimensions.
